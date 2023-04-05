# Tools

## Dataset compliance

Verify given dataset conforms to the AVL dataset convention.

CLI:
```text
Usage: avl ver [OPTIONS] DATASET

  Verify given dataset conforms to the AVL dataset convention.

Options:
  -l, --level [ERROR|WARNING]  Level of messages to include.
  --help                       Show this message and exit. 
```

Python API:
```python
import xarray as xr
import s3fs
from avl.verify import verify_dataset

s3 = s3fs.S3FileSystem(anon=True)
store = s3fs.S3Map('agriculture-vlab-data-staging/avl/l3b/2020/bel/S2_L3B_LAI_31UFS.zarr', s3=s3)
dataset = xr.open_zarr(store) 
issues = verify_dataset(dataset)
```

## Synthetic example datasets

Generate AVL sample dataset into current working directory.

CLI:
```text
Usage: avl new [OPTIONS]

  Generate AVL sample dataset into current working directory.

Options:
  --help  Show this message and exit.
```

## Generate simple catalogue

Generate the markdown page of all available AVL datasets in the AWS S3
buckets.

CLI:
```text
Usage: avl cat [OPTIONS]

  Generate the markdown page of all available AVL datasets in the AWS S3
  buckets.

Options:
  -f, --file JSON_FILE  JSON file path
  --json                Write the JSON_FILE and exit. Ignored if JSON_FILE is
                        not given.
  --help                Show this message and exit.
```

## Generate full catalogue

Generate a tree of markdown files with details of all specified stores and
datasets.

```text
Usage: avl catalogue [OPTIONS]

Options:
  --max-datasets N       maximum number of datasets to catalogue per data
                         store
  --use-stock-map        use very low-res stock map tiles instead of web tiles
  --stores TEXT          comma-separated IDs of stores to catalogue (if
                         omitted, catalogue all stores)
  --suffixes TEXT        comma-separated list of data ID suffixes to include
                         for s3 and file stores (if omitted, include all
                         suffixes)
  --data-id-filter TEXT  only include datasets whose ID contains this string
  --help                 Show this message and exit.
```
