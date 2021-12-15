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

    output_params = dict(consolidated=True)
    if output.startswith('s3://'):
        output_params['storage_options'] = storage_options

    for zarr_path in zarr_paths:
        input_params = dict(consolidated=True)
        if zarr_path.startswith('s3://'):
            input_params['storage_options'] = storage_options
        with xr.open_zarr(zarr_path, **input_params) as ds:
            print(f'Writing {zarr_path}')
            if first_part:
                ds.to_zarr(output, mode='w', **output_params)
            else:
                ds.to_zarr(output, mode='a', append_dim='time',
                           **output_params)
        first_part = False


if __name__ == '__main__':
    main()
