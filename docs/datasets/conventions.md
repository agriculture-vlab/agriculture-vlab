---

🚧 **TODO TODO_NF** : maintain me 🚧

---

# AVL Dataset Convention

Version 1.2 Draft, 2021-10-27


## Introduction

The purpose of this document is to define a convention how datasets generated 
by the AVL project should look like. The goal of the convention is to ease 
access to data, make it compliant to existing data standards, make it 
comprehensive and understandable, minimize the effort to ingest the data into 
users’ processing, visualisation, and analysis code. Short, the goal is to 
make AVL datasets analysis-ready.
The intention is neither to invent any new data formats nor trying to establish 
new "standards". Instead, the AVL conventions solely build on existing, 
popular, well-established data formats and data standards.
Due to the fundamental difference of gridded and vector datasets, we provide 
two separate conventions.

In this document, the verbs _must_, _should_, and _may_ have a special meaning 
when used to describe conventions. A _must_ is a mandatory requirement that 
must be fulfilled, _should_ is optional but always recommended, and 
_may_ is optional and recommended in cases (like good to have).

## Gridded Dataset Conventions

### Data Model and Format

The data model for AVL gridded datasets is a subset of the 
[Unidata Common Data Model] (CDM). The CDM has originally been established for 
NetCDF (Network Common Data Form) but is implemented also for the OPenDAP 
protocol and the HDF and Zarr formats. Other common gridded data models can be 
easily translated into the CDM, for example GeoTIFF.

AVL gridded datasets must fully comply to the _Climate and Forecast
Metadata Conventions_, short [CF Conventions]. The following sections in this 
chapter describe how these conventions are tailored and applied to AVL datasets.
By default, AVL gridded datasets are made available in the [Zarr format v2] as 
this format is ideal for Cloud storage, e.g. Object Storage such as AWS S3 and 
can be easily converted to other formats such as NetCDF or TIFF.
We consider the popular [xarray] Python package to be the primary in-memory 
representation for AVL gridded datasets. The [xarray.Dataset] data model 
represents a subset of the CDM, interprets CF compliant data correctly, and we 
will follow this simplified CDM model for AVL gridded datasets in both 
structure and terminology:

[Unidata Common Data Model]: https://www.unidata.ucar.edu/software/netcdf-java/v4.6/CDM/
[CF Conventions]: https://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html
[Zarr format v2]: https://zarr.readthedocs.io/en/stable/spec/v2.html
[xarray]: http://xarray.pydata.org/
[xarray.Dataset]: http://xarray.pydata.org/en/stable/user-guide/data-structures.html#dataset

* A **dataset** is a container for _variables_. A dataset has metadata in form 
  of a key-value mapping (global attributes).
* A **variable** has N dimensions in a prescribed order, and each dimension 
  has a name and a size. A variable contains the actual gridded data in form of 
  an N-D data array that has the shape of the dimension sizes. For AVL, the 
  data type of the array should be numeric, however also text strings and 
  complex types are allowed. A variable has metadata in form of a key-value 
  mapping (variable attributes). There are two types of variables, 
  _coordinates_ and _data variables_.
* **Coordinates** usually contain the labels for a dimension. For example, 
  the coordinate `lon` has a 1-D array that contains 3600 longitude values for 
  the dimension `lon` of size 3600. However, coordinates may also be 2-D. 
  For example. a dataset using satellite geometry may provide its `lon` 
  coordinate as a 2-D array for the dimensions `x` and `y` (for which should 
  exists coordinates too).
* All variables that are not coordinates are **data variables**. 
  They provide the actual dataset’s data. For each of the dimensions used by a 
  data variable, a corresponding coordinate must exist. For example, for a 
  data variable `NDVI` with dimensions `time`, `lat`, `lon`, the coordinates
  `time`, `lat`, `lon` must exist too.

### Metadata

Global and variable metadata shall follow the recommendations of the 
[ESIP Attribute Convention for Data Discovery v1.3]. If other metadata 
attributes are used, they should be covered by the [CF Conventions v1.8].

[CF Conventions v1.8]: https://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html
[ESIP Attribute Convention for Data Discovery v1.3]: https://wiki.esipfed.org/Attribute_Convention_for_Data_Discovery_1-3

### Spatial Reference

The spatial dimensions of a data variable must be the innermost dimensions, 
namely `y`, `x` - in this order. If the coordinate reference system (CRS) 
is geographic (e.g. CRS is `EPGS:4326`, `WGS84` or `CRS84`) it is ok and common 
to use dimensions `lat`, `lon` - in this order.

#### Regular grid mappings

If the spatial grid mapping is regular, the spatial dimensions should 
have corresponding 1-D coordinate variables using the same name. That is, 
datasets with spatial dimensions `x`, `y` should provide the 1-D coordinate 
variables `x` and `y`. Spatial coordinates must follow the 
[CF Conventions on Coordinates].

The 1-D coordinates of regular grids should have a uniform spacing, i.e. there 
should be a unique linear mapping between coordinate values and the spatial 
image grid. This implies strictly monotonically increasing or decreasing 
coordinate values. Ideally, the spacing should also be the same in 
the x and y directions.

If the coordinate variables and their 1-D dimensions are named `lon` and `lat`, 
this implies a geographic coordinate reference system. 
If the coordinate variables and their 1-D dimensions are named `x` and `y`, 
this indicates either a geographic or projected CRS, indicated by the
CRS encoding described in the [CF Conventions on Grid Mapping]. This 
requires adding an extra variable named `crs` or `spatial_ref` to the datasets
and refer to it using the `grid_mapping` attribute in the global attributes
or the attributes of data variables.

For non-geographic, projected grids, if space is not a problem, is it a 
common practice to also add 2-D geographic coordinate variables `lat` and `lon`
(WGS-84 implied) both having the dimensions `y`, `x` - in this order.
See also [CF Conventions on 2-D Lat and Lon].

#### Irregular grid mappings 

For irregular grids, the only spatial reference is provided by 2-D coordinate 
variables `lat` and `lon` (WGS-84 implied) both having the dimensions 
`y`, `x` - in this order. A typical use case is a dataset where images are 
provided in satellite viewing geometry. 
See also [CF Conventions on 2-D Lat and Lon].


[CF Conventions on Grid Mapping]: https://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html#grid-mappings-and-projections
[CF Conventions on 2-D Lat and Lon]: https://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html#_two_dimensional_latitude_longitude_coordinate_variables
[CF Conventions on Coordinates]: https://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html#coordinate-types

### Temporal Reference

The temporal dimension of a data variables should be named `time`. It should be 
the variable’s outermost dimension. A corresponding coordinate named `time` 
must exists and the [CF Conventions on the Time Coordinate] must be applied.
For datasets generated within AVL, it is recommended to use the unit 
`seconds since 1970-01-01T00:00:00` UTC.

Data variables may contain other dimensions in between the temporal dimension 
and the spatial dimensions, i.e. a variable’s dimensions may be 
`time`, …,`lat`, `lon` (geographic CRS), or `time`, …, `y`, `x` 
(non-geographic CRS) – both in exactly this order, where the ellipsis … refers 
to such extra dimensions. If there is a requirement to store individual time 
stamps per pixel value, this could still be done by adding a variable to the 
dataset which would then be e.g. `pixel_time` with dimensions 
`time`, `lat`, and `lon`. 

[CF Conventions on the Time Coordinate]: https://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html#time-coordinate

### Encoding of Units

All variables that represent quantities must set the attribute  
`units` according to the [CF Convention on Units]. 
Even if the quantity is dimensionless, the `units` attribute must be set
to indicate its dimensionless-ness by using the value `"1"`.

[CF Convention on Units]: https://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html#units

### Encoding of Flags

For data variables that are encoded as flags using named bits or bit 
masks/ranges, we strictly follow the [CF Convention on Flags]. 

[CF Convention on Flags]: https://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html#flags

### Missing Values

According to the [CF Convention on Missing Data], missing data should be 
indicated by the variable attribute `_FillValue`. 
However, Zarr does not define or interpret (decode) array attributes at all. 
The Zarr equivalent of the CF attribute `_FillValue` is the array property 
`fill_value` (not an attribute). `fill_value` can and should be set for all 
data types including integers, also because it is given in raw units,
that is, before `scaling_factor` and `add_offset` are applied (by xarray). 
Zarr’s `fill_value` has the advantage that data array chunks comprising 
only `fill_value` values can and should be dropped entirely. This can reduce 
number of chunks dramatically and improve data access performance a lot for 
many no-data chunks. In our case we should use `fill_value` to indicate 
that a data cube’s grid cell does not contain a value at all, 
it does not exist, it does not make sense, it had no input, etc.

However, when reading a Zarr with Python xarray using `decode_cf=True` 
(the new default), then xarray will also encode variable attribute 
`_FillValue` and `missing_value` and mask the data accordingly. It will 
unfortunately ignore `valid_min`, `valid_max`, `valid_range`.

Missing values shall therefore be indicated by the Zarr array property 
`fill_value`. In addition `valid_min`, `valid_max`, `valid_range`
variable attributes may be given, but they will not be decoded. However,
applications might still find them useful, e.g. xcube Viewer uses them,
if provided as value range for mapping color bars.

[CF Convention on Missing Data]: https://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html#missing-data

### Scale/Offset Values

Scale and offset encoding of bands / variables follows the 
[CF Convention on Packed Data]. In practice, affected variables must have 
attributes `scaling_factor` (default is 1) and `add_offset` (with default 0).  

[CF Convention on Packed Data]: https://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html#packed-data

### Multi-Band Products

Individual bands of a dataset should be stored as variables. This is also the 
case for multi-band products, like Sentinel-2, where each wavelength will be 
represented by a separate variable, `B01`, `B02`, etc.

### Metadata Consolidation

AVL datasets should provide consolidated dataset metadata in their root
directories. This allows reading the metadata of datasets with many 
variables more efficiently, especially when data is stored in Object Storage
and every metadata file would need to fetched via an individual HTTP request. 

The consolidated metadata file should be named `.zmetadata`,
which is also the default name used by the Zarr format.

The format of the consolidated metadata must be JSON. It is a 
JSON object using the following structure:

```json
    {
        "zarr_consolidated_format": 1
        "metadata": {
            ".zattrs": {…},
            ".zgroup": {…},
            "band_1/.zarray": {…},
            "band_1/.zattrs": {…},
            "band_2/.zarray": {…},
            "band_2/.zattrs": {…},
            …
        }
    }
```

### Zip Archives

AVL Zarr datasets may be provided as Zip archives. Such Zip archives 
should contain the contents of the archived Zarr directory in their root.
In other words, the keys of the entries in such an archive should not 
have a common prefix as is often the case when directories are zipped 
for convenience. The name of a zipped Zarr dataset should be the original 
Zarr dataset name plus the `.zip` extension. For example:

Desired:

    ${dataset-name}.zarr.zip/
        .zarray
        .zgroup
        .zmetadata
        band_1/
        time/
        …

Zipping the Zarrs this way allows opening the Zarr datasets directly from the 
Zip, e.g. for xarray this is `xarray.open_zarr("./dataset.zarr.zip")`.

### Dataset Examples

* Global WGS-84: [dataset_global.zarr.zip](https://github.com/agriculture-vlab/agriculture-vlab/raw/main/data-samples/dataset_global.zarr.zip)
* Projected CRS: [dataset_utm33n.zarr.zip](https://github.com/agriculture-vlab/agriculture-vlab/raw/main/data-samples/dataset_utm33n.zarr.zip)
* Satellite Viewing Geometry: TODO

---

🚧 **TODO TODO_NF** : add satellite viewing geometry example 🚧

---
