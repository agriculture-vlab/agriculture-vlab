# Software used by AVL

## Software used in thematic processing subsystem

| Name              | Version | Purpose                                                   | License      | URL                                               |
| ----------------- | ------- | --------------------------------------------------------  | ------------ | ------------------------------------------------- |
| apache commons    | various | Components of Apache Commons collection                   | Apache 2.0   | <https://commons.apache.org>                      |
| docker            | 20.10.7 | Software container packaging, management, and deployment  | Apache 2.0   | <https://www.docker.com>                          |
| gdal              | 3.2.4+  | Geospatial data format conversion                         | MIT          | <https://gdal.org>                                |
| geotools          | 26.0    | Java geospatial library                                   | LGPL         | <https://geotools.org>                            |
| hibernate         | 5.4.7   | Java ORM library                                          | LGPL v2.1    | <https://hibernate.org>                           |
| jackson           | 2.13    | JSON/XML serialization and deserialization                | Apache 2.0   | <https://github.com/FasterXML/jackson>            |
| jna               | 5.5.0   | Java to native libraries bridge                           | Apache 2.0   | <https://github.com/java-native-access/jna>       |
| jquery            | 3.2.1   | General purpose javascript library                        | MIT          | <https://jquery.com>                              |
| jsch              | 0.1.55  | Java SSH client                                           | BSD          | <http://www.jcraft.com/jsch>                      |
| jsplumb           | 2.4.2   | Javascript library for graph building (community edition) | jsPlumb      | <https://jsplumbtoolkit.com/>                     |
| jts               | 1.18.2  | Java topology suite library for geometries                | EPL 2.0      | <http://locationtech.github.io/jts>               |
| openjdk           | 8u212+  | Java runtime and development libraries                    | GPL v2+cpath | <http://openjdk.java.net>                         |
| orfeo toolbox     | 7.3.0   | Geospatial image processing toolbox                       | Apache 2.0   | <https://www.orfeo-toolbox.org>                   |
| postgresql        | 11.0    | Database server                                           | Postgres/MIT | <https://www.postgresql.org>                      |
| postgis           | 3.1.2   | PostgreSQL geospatial extensions                          | Postgres/MIT | <https://postgis.net>                             |
| pty4j             | 0.11.4  | Java terminal emulator                                    | EPL 1.0      | <https://github.com/JetBrains/pty4j>              |
| reactor           | 2.0.8   | Non-blocking messaging bus abstraction library            | Apache 2.0   | <https://projectreactor.io/>                      |
| snap              | 8.0.5   | Sentinels Application Platform                            | GPL v3       | <http://step.esa.int/main/download/snap-download> |
| spring            | 5.2.3   | Java framework for microservices                          | Apache 2.0   | <https://spring.io>                               |
| velocity          | 1.7     | Script engine                                             | Apache 2.0   | <https://velocity.apache.org>                     |

---

## Software used in exploitation subsystem

| Name              | Version   | Purpose                                                  | License      | URL                                              |
| ----------------- | --------- | -------------------------------------------------------- | ------------ | ------------------------------------------------ |
| affine            | 2.3.1     | Perform affine transformations of geographic data        | BSD 3-clause | <https://github.com/rasterio/affine>             |
| click             | 8.1.3     | Process command-line arguments                           | BSD 3-clause | <https://click.palletsprojects.com/>             |
| cmocean           | 2.0       | Provide colour maps                                      | MIT          | <https://github.com/matplotlib/cmocean>          |
| coiled            | 0.2.52    | Provide on-demand dask clusters                          | BSD 3-clause | <https://pypi.org/project/coiled/>               |
| dask              | 2022.11.1 | Parallel computation                                     | BSD 3-clause | <https://dask.org/>                              |
| dask-image        | 2022.9.0  | Distributed image processing                             | BSD 3-clause | <http://image.dask.org/>                         |
| distributed       | 2022.11.1 | Distributed scheduler for dask                           | BSD 3-clause | <http://distributed.dask.org/>                   |
| docker            | 20.10.7   | Software container packaging, management, and deployment | Apache 2.0   | <https://www.docker.com/>                        |
| fiona             | 1.8.21    | Vector API for gdal                                      | BSD 3-clause | <https://github.com/Toblerity/Fiona>             |
| fsspec            | 2022.11.0 | File-system interface layer                              | BSD 3-clause | <https://github.com/intake/filesystem_spec>      |
| gdal              | 3.5.1     | Geospatial data format conversion                        | MIT          | <https://gdal.org/>                              |
| geopandas         | 0.12.1    | Geospatial extensions for the pandas library             | BSD 3-clause | <https://geopandas.org/>                         |
| helm              | 3.7.0     | Package manager for kubernetes                           | Apache 2.0   | <https://helm.sh/>                               |
| jdcal             | 1.4.1     | Conversion between Julian and calendar dates             | BSD 2-clause | <https://github.com/phn/jdcal>                   |
| jsonschema        | 4.2.1     | Validation of JSON data                                  | MIT          | <https://json-schema.org/>                       |
| jupyterhub        | 1.5.0     | Multi-user server for Jupyter notebooks                  | BSD 3-clause | <https://jupyter.org/hub>                        |
| jupyterlab        | 3.5.0     | Web-based scientific notebook IDE                        | BSD 3-clause | <https://github.com/jupyterlab/jupyterlab>       |
| kubernetes        | 1.22.2    | Container workload deployment, scaling, and operation    | Apache 2.0   | <https://kubernetes.io/>                         |
| mamba             | 1.1.0     | Python package management                                | BSD 3-clause | <https://github.com/mamba-org/mamba>             |
| matplotlib-base   | 3.5.0     | Data visualization                                       | Matplotlib   | <https://matplotlib.org/>                        |
| mkdocs            | 1.2       | Format and build documentation                           | BSD 2-clause | <https://www.mkdocs.org/>                        |
| netcdf4           | 1.6.0     | Reading and writing NetCDF files                         | MIT          | <https://github.com/Unidata/netcdf4-python>      |
| numba             | 0.56.4    | Just-in-time compilation of Python code                  | BSD 2-clause | <https://numba.pydata.org/>                      |
| numpy             | 1.23.5    | Numerical, scientific, and mathematical functions        | BSD 3-clause | <https://numpy.org/>                             |
| pandas            | 1.5.2     | Analysis of tabular, relation, and labelled data         | BSD 3-clause | <https://pandas.pydata.org/>                     |
| pillow            | 8.4.0     | Image processing                                         | HPND         | <https://python-pillow.org/>                     |
| pyjwt             | 2.6.0     | Encode and decode JSON web tokens                        | MIT          | <https://github.com/jpadilla/pyjwt>              |
| pyproj            | 3.4.0     | Cartographic projection, coordinate transformation       | MIT          | <https://pyproj4.github.io/>                     |
| python            | 3.9.7     | Main implementation language                             | PSFL         | <https://python.org/>                            |
| pyyaml            | 6.0       | Serialize and deserialize data using YAML format         | MIT          | <https://pyyaml.org/>                            |
| rasterio          | 1.3.2     | Read and write geospational raster daa                   | BSD 3-clause | <https://github.com/rasterio/rasterio/>          |
| rasterstats       | 0.17.0    | Statistics of raster datasets based on vector geometries | BSD 3-clause | <https://github.com/perrygeo/python-rasterstats> |
| requests          | 2.26.0    | Make HTTP requests                                       | Apache 2.0   | <https://python-requests.org/>                   |
| requests-oauthlib | 1.3.1     | OAuth library support for requests library               | ISC          | <https://github.com/requests/requests-oauthlib>  |
| rfc3339-validator | 0.1.4     | Validation of date and time strings                      | MIT          | <https://github.com/naimetti/rfc3339-validator>  |
| rioxarray         | 0.13.1    | rasterio support for xarray                              | Apache 2.0   | <https://corteva.github.io/rioxarray/>           |
| s3fs              | 2022.11.0 | Filesystem-like access to S3 data stores                 | BSD 3-clause | <https://github.com/dask/s3fs>                   |
| scipy             | 1.8.0     | Fundamental algorithms for scientific computing          | BSD 3-clause | <https://scipy.org/>                             |
| sentinelhub       | 3.4.4     | Access to Sentinel Hub datasets                          | MIT          | <https://github.com/sentinel-hub/sentinelhub-py> |
| setuptools        | 59.2.0    | Facilitate packaging for Python projects                 | MIT          | <https://setuptools.pypa.io/>                    |
| shapely           | 1.8.5     | Manipulation and analysis of geometric objects           | BSD 3-clause | <https://github.com/Toblerity/Shapely>           |
| tornado           | 6.1       | Python web framework and asynchronous networking library | Apache 2.0   | <https://www.tornadoweb.org/>                    |
| urllib3           | 1.26.7    | HTTP client for Python                                   | MIT          | <https://github.com/urllib3/urllib3>             |
| xarray            | 2022.11.0 | Process labelled multi-dimensional arrays                | Apache 2.0   | <http://xarray.pydata.org/en/stable/>            |
| xcube             | 0.12.1    | Toolkit for managing EO/climate data cubes.              | MIT          | <https://github.com/dcs4cop/xcube>               |
| xcube-cci         | 0.9.6     | xcube access to ESA CCI Open Data Portal                 | MIT          | <https://github.com/dcs4cop/xcube-cci>           |
| xcube-cds         | 0.9.1     | xcube access to Copernicus Climate Data Store            | MIT          | <https://github.com/dcs4cop/xcube-cds>           |
| xcube-geodb       | 1.0.4     | Geospatial database plugin for xcube                     | MIT          | <https://github.com/dcs4cop/xcube-geodb>         |
| xcube-sh          | 0.9.5     | xcube access to Sentinel Hub datasets                    | MIT          | <https://github.com/dcs4cop/xcube-sh>            |
| zarr              | 2.13.3    | Implement compressed, chunked, N-dimensional arrays      | MIT          | <https://github.com/zarr-developers/zarr-python> |
