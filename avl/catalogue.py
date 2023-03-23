import math
import re
import os
import cartopy
import cartopy.io.img_tiles
import matplotlib.patches as patches
from matplotlib import pyplot as plt
from typing import Any, Dict, Optional, List
from xcube.core.store import new_data_store
import pathlib


class Catalogue:
    def __init__(
        self,
        dest_dir: str,
        max_datasets: Optional[int] = None,
        use_stock_map: bool = False,
        store_ids: Optional[List[str]] = None,
        data_suffixes: Optional[List[str]] = None,
    ):
        self.store_records = self.create_stores()
        self.dest_dir = pathlib.Path(dest_dir)
        self.max_datasets = max_datasets
        self.use_stock_map = use_stock_map
        self.store_ids = store_ids
        self.data_suffixes = (
            ('',)
            if data_suffixes is None
            else tuple(s.lower() for s in data_suffixes)
        )

    @staticmethod
    def create_stores() -> Dict[str, 'StoreRecord']:
        max_depth = 8

        user_store = (
            [
                (
                    'user',
                    'User data (private)',
                    'user_store',
                    dict(
                        data_store_id="s3",
                        root=f"agriculture-vlab-user/"
                        f"{os.environ['JUPYTERHUB_USER']}/",
                        max_depth=max_depth,
                    ),
                )
            ]
            if 'JUPYTERHUB_USER' in os.environ
            else []
        )

        # noinspection PyTypeChecker
        store_definitions = (
            [
                (
                    'lab',
                    'Jupyter lab',
                    'lab_store',
                    dict(data_store_id="file", root=str(pathlib.Path.home())),
                )
            ]
            + user_store
            + [
                (
                    'scratch',
                    'Scratch (temporary)',
                    'scratch_store',
                    dict(
                        data_store_id="s3",
                        root="agriculture-vlab-scratch/",
                        max_depth=max_depth,
                    ),
                ),
                (
                    'test',
                    'AVL data (testing)',
                    'test_store',
                    dict(
                        data_store_id="s3",
                        root="agriculture-vlab-data-test/",
                        max_depth=max_depth,
                    ),
                ),
                (
                    'staging',
                    'AVL data (staging)',
                    'staging_store',
                    dict(
                        data_store_id="s3",
                        root="agriculture-vlab-data-staging/",
                        max_depth=max_depth,
                    ),
                ),
                (
                    'data',
                    'AVL data',
                    'data_store',
                    dict(
                        data_store_id="s3",
                        root="agriculture-vlab-data/",
                        max_depth=max_depth,
                    ),
                ),
                (
                    'public',
                    'User data (shared)',
                    'public_store_read',
                    dict(
                        data_store_id="s3",
                        root=f"agriculture-vlab-public/",
                        max_depth=max_depth,
                    ),
                ),
            ]
        )

        return {args[0]: StoreRecord(*args) for args in store_definitions}

    def write_catalogue(self):
        pathlib.Path.mkdir(self.dest_dir, parents=True, exist_ok=True)
        index_path = self.dest_dir / 'index.md'
        with open(index_path, 'w') as fh:
            fh.write(
                '# AVL Dataset catalogue\n\n## Data stores\n\n'
                'Click on a store name for more details.\n\n'
                '| Store name | Description |\n'
                '|------------|-------------|\n'
            )

            for store_id in self.store_records:
                if self.store_ids is None or store_id in self.store_ids:
                    fh.write(
                        f'| [{store_id}]({store_id}/index.md) | '
                        f'{self.store_records[store_id].desc} |\n'
                    )

                    self.write_catalogue_for_store(store_id)

    def write_catalogue_for_store(self, store_id: str):
        path = self.dest_dir / store_id
        pathlib.Path.mkdir(path, parents=True, exist_ok=True)
        data_ids = self.store_records[store_id].store.get_data_ids()

        def filter_ids(ids):
            count = 0
            for id_ in ids:
                if id_.lower().endswith(self.data_suffixes):
                    yield id_
                    count += 1
                if count == self.max_datasets:
                    return

        with open(path / 'index.md', 'w') as fh:
            fh.write(f'# Data store: {store_id}\n\n')
            var_name = self.store_records[store_id].var_name
            fh.write(
                f'## Store variable name in JupyterLab: `{var_name}` &emsp;'
                f'{self._make_copy_button("variable name", var_name)}\n\n'
            )
            empty = True
            for data_id in filter_ids(data_ids):
                if empty:
                    fh.write('## Datasets in this store\n\n')
                    fh.write('Click on a dataset link for more details\n\n')
                empty = False
                fh.write(
                    f'[{data_id}]({self.data_id_to_filename(data_id)})<br>\n'
                )
                self.write_catalogue_for_dataset(store_id, data_id)
            if empty:
                fh.write('## There are no datasets available in this store.')

    def write_catalogue_for_dataset(self, store_id: str, data_id: str):
        basename = self.data_id_to_filename(data_id)
        path = self.dest_dir / store_id / basename
        with open(str(path) + '.md', 'w') as fh:
            print(store_id, data_id)
            ds = self.store_records[store_id].store.open_data(data_id)
            title = (
                ds.attrs.get('title', data_id)
                if hasattr(ds, 'attrs')
                else data_id
            )
            fh.write(f'# Dataset: {title}\n\n')
            fh.write(f'**Dataset identifier:** {data_id}<br>\n')
            fh.write(f'**Data store:** {store_id}<br>\n')
            # TODO: link to open in viewer?
            open_command = (
                f"ds = {self.store_records[store_id].var_name}"
                f".open_data('{data_id}')"
            )
            fh.write(
                f'## How to open this dataset in AVL JupyterLab '
                f'&emsp;{self._make_copy_button("code", open_command)}\n'
                f'```python\n{open_command}\n```\n\n'
            )
            if not hasattr(ds, 'attrs'):
                return
            fh.write(
                f'## Bounding box map\n\n'
                f'![Bounding box map]({basename + ".png"})<br>\n'
                '<span style="font-size: x-small">Map tiles by '
                '<a href="http://stamen.com">Stamen Design</a>, under '
                '<a href="http://creativecommons.org/licenses/by/3.0">'
                'CC BY 3.0</a>. Data by '
                '<a href="http://openstreetmap.org">OpenStreetMap</a>,'
                ' under '
                '<a href="http://www.openstreetmap.org/copyright">'
                'ODbL</a>.</span>\n\n'
            )
            self.make_map(ds.attrs, str(path) + '.png')
            fh.write('## Basic information\n\n')
            fh.write(self.dataset_attrs_to_markdown(ds.attrs))
            fh.write(
                '## Variable list\n\nClick on a variable name to jump to the '
                'variable’s full metadata.\n\n'
            )
            fh.write(self.variables_to_markdown(ds.variables))

            fh.write('## Full variable metadata\n\n')
            for var_name, variable in ds.variables.items():
                variable_source_filename = basename + '-' + var_name + '.md'
                variable_source_path = (
                    self.dest_dir / store_id / variable_source_filename
                )
                fh.write(f'### <a name="{var_name}"></a>' f'{var_name}\n\n')
                fh.write(
                    self.make_table(
                        variable.attrs, source_link=variable_source_filename
                    )
                )
                if 'source' in variable.attrs:
                    with open(variable_source_path, 'w') as var_source_fh:
                        var_source_fh.write(f'`{variable["source"]}`\n')
            fh.write(
                '## <a name="full-metadata"></a>Full dataset metadata\n\n'
            )
            fh.write(self.make_table(ds.attrs))

    @staticmethod
    def _make_copy_button(description, content):
        html_snippet = (
            '<button id="copybutton"'
            f'title="Copy the {description} to the clipboard">⧉</button>'
            '<script>copybutton.addEventListener("pointerdown",'
            f'() =\\> navigator.clipboard.writeText("{content}"))'
            '</script>'
        )
        return html_snippet

    @staticmethod
    def data_id_to_filename(data_id: str):
        return data_id.replace('/', '-').replace('.', '-')

    @staticmethod
    def dataset_attrs_to_markdown(props: Dict[str, Any]) -> str:
        """Create a brief summary from a dictionary of dataset properties.

        Args:
            props: dictionary of dataset properties

        Returns:
            Markdown source containing information about the dataset
        """

        def prop(key):
            return props.get(key, "?")

        return (
            f'| Parameter | Value |\n'
            f'| ---- | ---- |\n'
            f'| Bounding box latitude | {prop("geospatial_lat_min")} to '
            f'{prop("geospatial_lat_max")} |\n'
            f'| Bounding box longitude | {prop("geospatial_lon_min")} to '
            f'{prop("geospatial_lon_max")} |\n'
            f'| Time range | {prop("time_coverage_start")} to '
            f'{prop("time_coverage_end")} |\n'
            + (
                f'| Time period | {prop("time_period")} |\n'
                if 'time_period' in props
                else ''
            )
            + f'| Publisher | {prop("publisher_name")} |\n\n'
            '[Click here for full dataset metadata.](#full-metadata)\n\n'
        )

    def variables_to_markdown(self, variables: Dict[str, Any]) -> str:
        """Create table with brief information about the variables in a dataset

        Args:
            variables: a list of dictionaries of variable properties

        Returns:
            Markdown source for a table summarizing the variables

        """
        lines = ['| Variable | Long name | Units |', '| ---- | ---- | ---- |']
        for varname, variable in variables.items():
            if varname == 'crs':
                continue
            attrs = variable.attrs
            long_name = self.escape_for_markdown(
                attrs.get('long_name', '[none]')
            )
            name = self.escape_for_markdown(varname)
            units = self.escape_for_markdown(attrs.get('units', '[none]'))
            lines.append(f'| [{name}](#{name}) | {long_name} | {units} |')
        return '\n'.join(lines) + '\n\n'

    def make_table(self, data: Dict[str, Any], source_link: str = None) -> str:
        """Create a Markdown table showing the entries in a dictionary

        Args:
            data: the data to be displayed
            source_link: if supplied and if a `source` key is present, the
                value for "source" in the table will be replaced with a
                Markdown link to this location.

        Returns:
            Markdown source for a table
        """
        lines = ['| Field | Value |', '| ---- | ---- |']
        for field, raw_value in data.items():
            value = (
                f'[Click here for source.]({source_link})'
                if field == 'source' and source_link is not None
                else f'{self.escape_for_markdown(raw_value)}'
            )
            lines.append(f'| {self.escape_for_markdown(field)} | {value} |')
        return '\n'.join(lines) + '\n\n'

    @staticmethod
    def escape_for_markdown(content: Any) -> str:
        """Turn any value into a Markdown source string

        For a string, characters which have special meaning in Markdown will
        be escaped to ensure that they display correctly. Additionally, if the
        string begins with "http://", "https://", or "www." it will be turned
        into a Markdown link.

        For a dictionary or list, each element will be processed recursively
        with another call to this function, and they will be joined into a
        single string with ", " and/or ": " as separators.

        Any other type will be turned into a string with the ``str`` function
        and processed as a string.

        Args:
            content: anything

        Returns:
            a correctly escaped Markdown representation of the input
        """

        if type(content) == list:
            return ', '.join(map(Catalogue.escape_for_markdown, content))
        elif type(content) == dict:
            return ', '.join(
                Catalogue.escape_for_markdown(k)
                + ': '
                + Catalogue.escape_for_markdown(v)
                for k, v in content.items()
            )
        elif type(content) == str:
            escaped_text = re.sub(r'[][({`*_#+.!})\\-]', r'\\\g<0>', content)
            if re.match('https?://', content):
                return f'[{escaped_text}]({content})'
            elif re.match('www[.]', content):
                return f'[{escaped_text}](http://{content})'
            else:
                return escaped_text
        else:
            return Catalogue.escape_for_markdown(str(content))

    def make_map(self, props: Dict[str, Any], output_path: str) -> None:
        """Create a bounding box map from a dataset's properties

        The map shows the dataset's bounding box at the centre of a map covering a
        larger area.

        Args:
            props: property dictionary for a dataset
            output_path: the path to which to write the map. The output format
                is determined by the file extension of this path.
        """
        x0 = props.get('geospatial_lon_min', -180)
        x1 = props.get('geospatial_lon_max', 180)
        y0 = props.get('geospatial_lat_min', -90)
        y1 = props.get('geospatial_lat_max', 90)
        w = x1 - x0
        h = y1 - y0

        # Above a certain size, we switch from a regional LAEA projection to
        # a global Mollweide projection.
        large = w > 45 or h > 45

        margin_factor = 0.2  # how much margin to include around the bbox
        image_tiles = cartopy.io.img_tiles.Stamen('terrain-background')
        plt.figure()
        projection = (
            cartopy.crs.Mollweide(central_longitude=(x0 + x1) / 2)
            if large
            else cartopy.crs.LambertAzimuthalEqualArea(
                (x0 + x1) / 2,
                (y0 + y1) / 2
                # centre the projection over our bbox
            )
        )
        ax = plt.axes(projection=projection)
        if large:
            ax.set_global()
        else:
            ax.set_extent(
                [
                    x0 - margin_factor * w,
                    x1 + margin_factor * w,
                    y0 - margin_factor * h,
                    y1 + margin_factor * h,
                ],
                crs=cartopy.crs.Geodetic(),
            )

        # We use a fairly crude calculation to choose the tile resolution;
        # ideally we should take the pixel dimensions of the final image
        # into account here as well as the geographical bounding box size.
        max_dim_deg = max(w, h)
        if max_dim_deg > 45:
            max_dim_deg = 360
        zoom_level = 3 + int(math.log2(360 / max_dim_deg))
        if self.use_stock_map:
            ax.stock_img()  # very low-res but very fast, so useful for testing
        else:
            ax.add_image(image_tiles, zoom_level)

        bbox_rect_patch = patches.Rectangle((x0, y0), w, h)
        # Since projected rectangle sides may not be straight, we interpolate
        # them into many short line segments which can be projected
        # separately. In some cases cartopy can do this automatically,
        # but it doesn't seem to work for our projection and parameters (as
        # of cartopy 0.21.0), so we use the manual approach.
        bbox_path_patch = patches.PathPatch(
            bbox_rect_patch.get_path()
            .transformed(bbox_rect_patch.get_patch_transform())
            .interpolated(100),
            linewidth=2,
            edgecolor='red',
            facecolor='none',
            transform=cartopy.crs.Geodetic(),
            zorder=1e6,  # on top
        )
        ax.add_patch(bbox_path_patch)
        ax.gridlines(draw_labels=not large, color='white')
        plt.tight_layout(pad=0)
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0.1)
        # plt.close()  # TODO fix this


class StoreRecord:
    """Creates and wraps a store with some catalogue-releant metadata"""

    def __init__(
        self, store_id: str, desc: str, var_name: str, store_args: Dict
    ):
        """Initialize a store record

        Args:
            store_id: store identifier to use in the catalogue
            desc: human-readable description of the store
            var_name: name of pre-initialized store variable in JupyterLab
            store_args: passed directly to `new_data_store`
        """

        self.store_id = store_id
        self.desc = desc
        self.var_name = var_name
        self.store_args = store_args
        self.store = new_data_store(**store_args)
