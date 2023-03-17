import math
import os
import re
import cartopy
import cartopy.io.img_tiles
import matplotlib.patches as patches
from matplotlib import pyplot as plt
from typing import Union, Any, Dict, List
from xcube.core.store.store import DataStore, MutableDataStore
import pathlib
import itertools


class Catalogue:
    def __init__(
        self,
        stores: Dict[str, Union['DataStore', 'MutableDataStore']],
        dest_dir: str,
    ):
        self.stores = stores
        self.dest_dir = pathlib.Path(dest_dir)

    def create_catalogue(self):
        pathlib.Path.mkdir(self.dest_dir, parents=True, exist_ok=True)
        index_path = self.dest_dir / 'index.md'
        with open(index_path, 'w') as fh:
            fh.write('# Dataset catalogue\n\n## Stores\n\n')
            for store_id in self.stores:
                fh.write(f' - [{store_id}]({store_id}/index.md)\n')
                self.make_catalogue_for_store(store_id)

    def make_catalogue_for_store(self, store_id: str):
        path = self.dest_dir / store_id
        pathlib.Path.mkdir(path, parents=True, exist_ok=True)
        data_ids = self.stores[store_id].get_data_ids()
        with open(path / 'index.md', 'w') as fh:
            fh.write(f'# Data store: {store_id}\n\n')
            for data_id in itertools.islice(
                data_ids, 0, 40
            ):  # TODO add parameter
                fh.write(
                    f' - [{data_id}]({self.data_id_to_filename(data_id)})\n'
                )
                self.make_catalogue_for_dataset(store_id, data_id)

    def make_catalogue_for_dataset(self, store_id: str, data_id: str):
        basename = self.data_id_to_filename(data_id)
        path = self.dest_dir / store_id / basename
        with open(str(path) + '.md', 'w') as fh:
            ds = self.stores[store_id].open_data(data_id)
            title = (
                ds.attrs.get('title', data_id)
                if hasattr(ds, 'attrs')
                else data_id
            )
            fh.write(f'# Dataset: {title}\n\n')
            fh.write(f'Identifier: {data_id}<br>\n')
            fh.write(f'Data store: {store_id}<br>\n')
            if not hasattr(ds, 'attrs'):
                return
            fh.write(f'![Bounding box map]({basename + ".png"})<br>\n')
            fh.write(
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
            fh.write(self.dataset_attrs_to_markdown(ds.attrs))
            fh.write(
                self.variables_to_markdown(ds.variables)
            )
            # TODO: link to open in viewer?
            fh.write(
                '## How to open this dataset in AVL JupyterLab\n'
                '```python\n'
                f'ds = {store_id}.open_data("{data_id}")\n'
                '```\n\n'
            )
            fh.write('## Full variable metadata\n\n')
            for var_name, variable in ds.variables.items():
                variable_source_filename = (
                    basename + '-' + var_name + '.md'
                )
                variable_source_path = \
                    self.dest_dir / store_id / variable_source_filename
                fh.write(
                    f'### <a name="{var_name}"></a>'
                    f'{var_name}\n\n'
                )
                fh.write(
                    self.make_table(variable.attrs,
                                    source_link=variable_source_filename)
                )
                if 'source' in variable.attrs:
                    with open(variable_source_path, 'w') as var_source_fh:
                        var_source_fh.write(f'`{variable["source"]}`\n')
            fh.write(
                '## <a name="full-metadata"></a>Full dataset metadata\n\n'
            )
            fh.write(self.make_table(ds.attrs))

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
        lines = ['| Variable | Identifier | Units |', '| ---- | ---- | ---- |']
        for varname, variable in variables.items():
            if varname == 'crs':
                continue
            attrs = variable.attrs
            long_name = self.escape_for_markdown(
                attrs.get('long_name', '[none]')
            )
            name = self.escape_for_markdown(varname)
            units = self.escape_for_markdown(attrs.get('units', '[none]'))
            lines.append(f'| [{long_name}](#{name}) | {name} | {units} |')
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
    def escape_for_markdown(content: Any) -> Any:
        """Turn a string or list into a Markdown source string

        For a string, characters which have special meaning in Markdown will
        be escaped to ensure that they display correctly. Additionally, if the
        string begins with "http://", "https://", or "www." it will be turned
        into a Markdown link.

        For a list, each element will be processed recursively with another call
        to this function, and they will be joined into a single string with ", "
        as separator.

        For any other type, the output is the same as the input.

        Args:
            content: anything

        Returns:
            For strings and lists: Markdown source which will produce a
            representation of the input. For any other type: the input value.
        """
        if type(content) == list:
            return ', '.join(map(Catalogue.escape_for_markdown, content))
        elif type(content) == str:
            escaped_text = re.sub(r'[][({`*_#+.!})\\-]', r'\\\g<0>', content)
            if re.match('https?://', content):
                return f'[{escaped_text}]({content})'
            elif re.match('www[.]', content):
                return f'[{escaped_text}](http://{content})'
            else:
                return escaped_text
        else:
            return content

    @staticmethod
    def make_map(props: Dict[str, Any], output_path: str) -> None:
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

        # We use a crude test to choose the tile resolution; ideally we should
        # calculate this more carefully from the bbox size and final image
        # resolution.
        max_dim_deg = max(w, h)
        if max_dim_deg > 45:
            max_dim_deg = 360
        zoom_level = 3 + int(math.log2(360 / max_dim_deg))
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
