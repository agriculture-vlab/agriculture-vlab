#!/usr/bin/env python3

"""Concatenate Zarrs along the time axis and write to a new Zarr"""

import argparse
from typing import List
import xarray as xr


def main():
    parser = argparse.ArgumentParser(description='Concatenate Zarrs')
    parser.add_argument('zarr_list', type=str,
                        help='name of file listing Zarr paths to read')
    parser.add_argument('output_path', type=str,
                        help='Zarr path (local or "s3://...") '
                             'to which to write')
    args = parser.parse_args()

    with open(args.zarr_list, 'r') as fh:
        input_paths = list(map(lambda s: s.strip(), fh.readlines()))

    combine_s3_parts(input_paths, args.output_path)


def combine_s3_parts(zarr_paths: List[str], output):
    first_part = True
    storage_options = dict(
        # No key or secret given here. They will be taken
        # from AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
        # (or AWS_SESSION_TOKEN) or from .aws/credentials.
        client_kwargs=dict(
            region_name='eu-central-1',
        ),
        s3_additional_kwargs=dict(
            ACL='public-read'
        )
    )
    for zarr_path in zarr_paths:
        with xr.open_zarr(zarr_path, consolidated=True,
                          storage_options=storage_options) as ds:
            print(f'Writing {zarr_path}')
            if first_part:
                ds.to_zarr(output, consolidated=True, mode='w',
                           storage_options=storage_options)
            else:
                ds.to_zarr(output, consolidated=True, mode='a',
                           append_dim='time', storage_options=storage_options)
        first_part = False


if __name__ == '__main__':
    main()
