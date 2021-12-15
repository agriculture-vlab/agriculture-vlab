#!/usr/bin/env python3

"""Read SH data and write to local or S3 Zarrs"""

import argparse
from datetime import datetime
from types import SimpleNamespace

import pandas as pd
import xarray as xr
from packaging import version
from xcube_sh.config import CubeConfig
from xcube_sh.cube import open_cube
import yaml

assert(version.parse(xr.__version__) >= version.parse('0.20.1'))


def main():
    parser = argparse.ArgumentParser(
        description='Read SH data by band and write to Zarrs')
    parser.add_argument('config', metavar='yaml-filename', type=str,
                        help='YAML configuration')
    parser.add_argument('--output', '-o', metavar='filename', type=str,
                        help='Write list of output Zarr paths to this file')
    args = parser.parse_args()

    with open(args.config, 'r') as fh:
        config = SimpleNamespace(**yaml.safe_load(fh))

    zarr_paths = sh_to_s3_bands(config)

    print('Output Zarr paths:')
    print('\n'.join(zarr_paths))
    if args.output is not None:
        with open(args.output, 'w') as fh:
            for zarr_path in zarr_paths:
                fh.write(zarr_path + '\n')


def sh_to_s3_bands(config: SimpleNamespace):
    start_date, end_date = list(map(pd.to_datetime, config.time_range))

    zarr_paths = []
    for band_name in config.bands:
        log('Opening from SH: ' + band_name)
        names = [band_name]
        # SH_CLIENT_ID and SH_CLIENT_SECRET must be set.
        cube_config = CubeConfig(dataset_name=config.dataset_name,
                                 band_names=names,
                                 tile_size=tuple(config.tile_size),
                                 bbox=tuple(config.bbox),
                                 spatial_res=config.spatial_res,
                                 time_range=(start_date.isoformat(),
                                             (end_date.isoformat())),
                                 time_period=config.time_period)
        cube = open_cube(cube_config)
        sub_cube = cube
        full_path = f'{config.output_prefix}{band_name}.zarr'
        zarr_paths.append(full_path)

        if hasattr(config, 'rechunk_to'):
            log("Rechunking")
            for v in sub_cube.data_vars:
                time_chunk, lat_chunk, lon_chunk = config.rechunk_to
                sub_cube[v].encoding['chunks'] = \
                    (time_chunk, lat_chunk, lon_chunk)
                sub_cube[v] = \
                    sub_cube[v].chunk(dict(time=time_chunk, lat=lat_chunk,
                                           lon=lon_chunk))

        log(f'Writing Zarr to {full_path}')
        # to_zarr seems to specify wrong type for storage_options, so disable
        # type check.
        # noinspection PyTypeChecker
        sub_cube.to_zarr(
            full_path,
            consolidated=True,
            storage_options=dict(
                # No key or secret given here. They will be taken
                # from AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
                # (or AWS_SESSION_TOKEN) or from .aws/credentials.
                client_kwargs=dict(
                    region_name='eu-central-1',
                ),
                s3_additional_kwargs=dict(
                    ACL='public-read'
                ))
        )
        print('Zarr written.')
    return zarr_paths


def log(s):
    print(datetime.now().isoformat(' ', 'seconds') + ': ' + s)


if __name__ == '__main__':
    main()
