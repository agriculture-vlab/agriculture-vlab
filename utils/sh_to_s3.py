#!/usr/bin/env python3

"""Read SH data and write to local or S3 Zarrs"""

import argparse
import time
from typing import Tuple, List

import pandas as pd
import xarray as xr
from packaging import version
from xcube_sh.config import CubeConfig
from xcube_sh.cube import open_cube

assert(version.parse(xr.__version__) >= version.parse('0.20.1'))


def sh_to_s3_parts(bbox: Tuple[float, float, float, float],
                   spatial_res: float, time_span: Tuple[str, str],
                   band_names: List[str], destination: str,
                   delay: int):
    start_date, end_date = time_span
    time_gap = pd.Timedelta('1 hour')  # avoid duplicate time-points
    start_dates = list(pd.date_range(start=start_date, end=end_date,
                                     freq='20D', tz='UTC', closed='left'))
    end_dates = (list(map(lambda ts: ts - time_gap, start_dates)) +
                 [pd.to_datetime(end_date, utc=True)])[1:]
    sub_periods = list(zip(start_dates, end_dates))

    zarr_paths = []
    for sub_start, sub_end in sub_periods:
        print('Fetching from SH:', sub_start, sub_end)
        sub_cube = read_cube_from_sentinel_hub(
            bbox, sub_start.isoformat(), sub_end.isoformat(),
            spatial_res, band_names
        )
        datestring = sub_start.strftime(r'%Y-%m-%d')
        full_path = f'{destination}-{datestring}.zarr'
        zarr_paths.append(full_path)

        for v in sub_cube.data_vars:
            sub_cube[v].encoding['chunks'] = (2, 1024, 1024)
            sub_cube[v] = sub_cube[v].chunk(dict(time=2, lat=1024, lon=1024))
        print('Writing Zarr:', full_path)
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
        if delay > 0:
            time.sleep(delay)
    return zarr_paths


def read_cube_from_sentinel_hub(bbox: Tuple[float, float, float, float],
                                start_date: str, end_date: str,
                                spatial_res: float, band_names: List[str])\
        -> xr.Dataset:
    # SH_CLIENT_ID and SH_CLIENT_SECRET must be set.
    time_range = (start_date, end_date)
    cube_config = CubeConfig(dataset_name='S2L2A',
                             band_names=band_names,
                             tile_size=(1024, 1024),
                             bbox=bbox,
                             spatial_res=spatial_res,
                             time_range=time_range,
                             time_period='10D')
    cube = open_cube(cube_config)
    return cube


def main():
    bboxes = dict(
        belgium=(4.44, 49.56, 6.02, 51.44),
        france=(-3.00, 46.86, -0.20, 47.85),
        test=(-1.75, 47.28, -1.41, 47.53),
    )
    resolutions = dict(
        full=0.00013,
        low=0.0002,
        verylow=0.0013,
    )
    band_names = dict(
        oneband=['B07'],
        allbands=['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09',
                  'B11', 'B12', 'B8A', 'SCL'],
    )
    time_spans = {
        'short': ('2019-01-01', '2019-02-28'),
        '2019': ('2019-01-01', '2019-12-31'),
        '2019-2020': ('2019-01-01', '2020-12-31'),
    }

    parser = argparse.ArgumentParser(description='Write SH data to Zarrs.')
    parser.add_argument('bbox', metavar='bounding-box', type=str,
                        choices=bboxes.keys(), help='{%(choices)s}')
    parser.add_argument('resolution', metavar='resolution', type=str,
                        choices=resolutions.keys(), help='{%(choices)s}')
    parser.add_argument('band_names', metavar='band_names', type=str,
                        choices=band_names.keys(), help='{%(choices)s}')
    parser.add_argument('time_span', metavar='timespan', type=str,
                        choices=time_spans.keys(), help='{%(choices)s}')
    parser.add_argument('destination', metavar='path-or-s3path', type=str,
                        help='Destination prefix (file path or s3://...)')
    parser.add_argument('--output', '-o', metavar='filename', type=str,
                        help='Write list of output Zarr paths to this file')
    parser.add_argument('--delay', '-d', metavar='seconds', type=int,
                        default=0,
                        help='Delay between SH fetches')
    args = parser.parse_args()

    zarr_paths = sh_to_s3_parts(bbox=bboxes[args.bbox],
                                spatial_res=resolutions[args.resolution],
                                time_span=time_spans[args.time_span],
                                band_names=band_names[args.band_names],
                                destination=args.destination,
                                delay=args.delay)

    print('Output Zarr paths:')
    print('\n'.join(zarr_paths))
    if args.output is not None:
        with open(args.output, 'w') as fh:
            for zarr_path in zarr_paths:
                fh.write(zarr_path + '\n')


if __name__ == '__main__':
    main()
