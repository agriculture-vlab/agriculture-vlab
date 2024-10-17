#!/usr/bin/env python3

"""Convert an archive containing EnMAP products to one or more Zarrs"""

import os
import pathlib
import argparse
import tarfile
import zipfile
import xml.etree
import tempfile
import shutil
from collections.abc import Iterable
import logging

import rioxarray
import xarray as xr
import numcodecs
import shapely

LOGGER = logging.getLogger(__name__)

VAR_MAP = dict(
    reflectance="SPECTRAL_IMAGE",
    mask="QL_PIXELMASK",
    cirrus="QL_QUALITY_CIRRUS",
    classes="QL_QUALITY_CLASSES",
    cloudshadow="QL_QUALITY_CLOUDSHADOW",
    cloud="QL_QUALITY_CLOUD",
    haze="QL_QUALITY_HAZE",
    snow="QL_QUALITY_SNOW",
    testflags="QL_QUALITY_TESTFLAGS",
    # We omit the quicklook files QL_SWIR and QL_VNIR.
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_filename",
        type=str,
        help="Either a Zip for a single product, "
        "or a .tar.gz containing multiple Zips",
    )
    parser.add_argument(
        "output_dir", type=str, help="Write output to this directory."
    )
    parser.add_argument(
        "--tempdir",
        "-t",
        type=str,
        help="Use specified path as temporary directory, and don't "
        "delete it afterwards (useful for debugging)",
    )
    parser.add_argument(
        "--compress",
        "-c",
        action="store_true",
        help="Higher output compression. ~25%% smaller. "
        "Compression (but not decompression) much slower.",
    )
    parser.add_argument(
        "--extract-only",
        "-e",
        action="store_true",
        help="Just extract data from sub-archives, don't convert to Zarr.",
    )
    parser.add_argument("--verbose", "-v", action="count", default=0)
    args = parser.parse_args()

    if args.verbose > 1:
        logging.basicConfig(level=logging.DEBUG)
    elif args.verbose > 0:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARN)
    if args.tempdir is None:
        with tempfile.TemporaryDirectory() as temp_dir:
            process(
                args.input_filename,
                args.output_dir,
                temp_dir,
                args.compress,
                args.extract_only,
            )
    else:
        temp_dir = os.path.expanduser(args.tempdir)
        shutil.rmtree(temp_dir, ignore_errors=True)
        os.mkdir(temp_dir)
        process(
            args.input_filename,
            os.path.expanduser(args.output_dir),
            temp_dir,
            args.compress,
            args.extract_only,
        )


def process(
    input_filename: str,
    output_dir: str,
    temp_dir: str,
    compress: bool = False,
    extract_only: bool = False,
):
    if extract_only:
        paths = extract_archives(input_filename, temp_dir)
        for path in paths:
            shutil.copytree(path, pathlib.Path(output_dir) / path.name)
    else:
        convert(input_filename, output_dir, temp_dir, compress)


def convert(
    input_filename: str, output_dir: str, temp_dir: str, compress: bool = False
):
    data_dirs = extract_archives(input_filename, temp_dir)
    for data_dir in data_dirs:
        LOGGER.info(f"Processing {data_dir}")
        arrays = {
            name: rioxarray.open_rasterio(
                data_dir / (filename + ".TIF")
            ).squeeze()
            for name, filename in VAR_MAP.items()
        }
        ds = xr.Dataset(arrays)
        for var in ds.data_vars:
            chunks = dict(x=2000, y=2000)
            if var == "mask":
                chunks["band"] = 1000
            if var == "reflectance":
                chunks["band"] = 5
            ds[var] = ds[var].chunk(chunks=chunks)
        add_metadata(ds, data_dir)
        zarr_args = {
            "store": pathlib.Path(output_dir) / (data_dir.name + ".zarr")
        }
        if compress:
            zarr_args["encoding"] = {
                "reflectance": {
                    "compressor": numcodecs.Blosc(
                        cname="zstd", clevel=9, shuffle=numcodecs.Blosc.SHUFFLE
                    )
                }
            }
        ds.to_zarr(**zarr_args)


def add_metadata(ds: xr.Dataset, data_dir: pathlib.Path):
    root = xml.etree.ElementTree.parse(data_dir / "METADATA.XML").getroot()

    points = root.findall("base/spatialCoverage/boundingPolygon/point")
    bounds = shapely.Polygon(
        [float(p.find("longitude").text), p.find("latitude").text]
        for p in points
        if p.find("frame").text != "center"
    )
    bbox = bounds.bounds

    def text(xpath):
        return root.find(xpath).text

    global_attrs = {
        "id": text("product/image/merge/name").removesuffix(
            "-SPECTRAL_IMAGE.TIF"
        ),
        "title": text("metadata/comment"),
        "summary": text("metadata/citation"),
        "keywords": "EnMAP,hyperspectral,remote sensing",
        "Conventions": "ACDD-1.3,CF-1.8",
        "naming_authority": "de.dlr",
        "processing_level": "2A",
        "geospatial_bounds": shapely.to_wkt(bounds),
        "geospatial_bounds_crs": "EPSG:4326",
        "geospatial_lat_min": bbox[1],
        "geospatial_lat_max": bbox[3],
        "geospatial_lon_min": bbox[0],
        "geospatial_lon_max": bbox[2],
        "time_coverage_start": text("base/temporalCoverage/startTime"),
        "time_coverage_end": text("base/temporalCoverage/stopTime"),
    }
    ds.attrs.update(global_attrs)

    var_attrs = {
        "reflectance": (
            "reflectance",
            "surface_bidirectional_reflectance",
            1,
            "physicalMeasurement",
        ),
        "cirrus": (
            "cirrus mask",
            "cirrus",
            1,
            "qualityInformation",
        ),
        "classes": (
            "area type",
            "area_type",
            1,
            "qualityInformation",
            {
                "flag_values": [1, 2, 3],
                "flag_meanings": ["Land", "Water", "Background"],
            },
        ),
        "cloud": ("cloud mask", "cloud_binary_mask", 1, "qualityInformation"),
        "cloudshadow": (
            "cloud shadow",
            "cloud_shadow",
            1,
            "qualityInformation",
        ),
        "haze": ("haze mask", "haze", 1, "qualityInformation"),
        "mask": ("pixel mask", "mask", 1, "qualityInformation"),
        "snow": (
            "snow mask",
            "surface_snow_binary_mask",
            1,
            "qualityInformation",
        ),
        "testflags": ("test flags", "test_flags", 1, "qualityInformation"),
    }

    for var, values in var_attrs.items():
        attrs = {
            "long_name": values[0],
            "standard_name": values[1],
            "units": values[2],
            "coverage_content_type": values[3],
        }
        if len(values) > 4:
            attrs.update(values[4])
        ds[var].attrs.update(attrs)


def extract_archives(
    archive_path: os.PathLike | str, dest_dir: os.PathLike | str
) -> Iterable[pathlib.Path]:
    dest_path = pathlib.Path(dest_dir)
    archive_path = pathlib.Path(archive_path)
    if archive_path.name.endswith(".tar.gz"):
        # An EnMAP tgz usually contains one or more zip archives
        # containing the actual data files.
        outer_path = dest_path / "outer-archive"
        LOGGER.info(f"Extracting {archive_path.name}")
        with tarfile.open(archive_path) as tgz_file:
            tgz_file.extractall(path=outer_path)
    else:
        # Assume it's a zip and skip the outer archive
        # extraction step.
        LOGGER.info(f"Assuming {archive_path} is an inner zipfile")
        outer_path = archive_path.parent
    inner_path = dest_path / "inner-archive"

    data_paths = []
    final_path = dest_path / "data"
    os.mkdir(final_path)
    for index, path_to_zip_file in enumerate(find_zips(outer_path)):
        LOGGER.info(f"Extracting {path_to_zip_file.name}")
        extract_path = inner_path / str(index)
        with zipfile.ZipFile(path_to_zip_file, "r") as zip_ref:
            zip_ref.extractall(extract_path)
        input_data_path = list(extract_path.iterdir())[0]
        input_data_dir = input_data_path.name
        output_data_path = final_path / input_data_dir
        data_paths.append(output_data_path)
        prefix_length = len(input_data_path.name) + 1
        os.mkdir(output_data_path)
        for filepath in input_data_path.iterdir():
            os.rename(
                filepath, output_data_path / filepath.name[prefix_length:]
            )
    return data_paths


def find_zips(root: os.PathLike):
    root_path = pathlib.Path(root)
    for parent, dirs, files in root_path.walk(on_error=print):
        for filename in files:
            if filename.endswith(".ZIP"):
                yield pathlib.Path(parent, filename)


if __name__ == "__main__":
    main()
