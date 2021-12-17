from avl import dataset
import pyproj
import pandas as pd


def test_new_dataset():
    ds = dataset.new_dataset()
    assert {'time', 'lon', 'lat', 'bnds'} == set(ds.dims)


def test_get_geospatial_attrs():
    attrs = dataset.get_geospatial_attrs(
        (-12, -34, 56, 78),
        (1, 1),
        pyproj.crs.CRS('CRS84'))
    assert 'POLYGON((-12 -34, -12 78, 56 78, 56 -34, -12 -34))' == \
           attrs['geospatial_bounds']


def test_get_time_coverage_attrs():
    # noinspection PyTypeChecker
    attrs = dataset.get_time_coverage_attrs(
        (pd.to_datetime('2020-01-01T01:00:00Z'),
         pd.to_datetime('2021-04-15-T02:00:00Z')),
        '1D')
    assert '470 days 01:00:00' == attrs['time_coverage_duration']
