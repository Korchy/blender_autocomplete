import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class AssetCatalog:
    """AssetCatalog(uuid: str, path: PurePosixPath, simple_name: str)"""

def parse_catalogs(library_path) -> None:
    """Parse all asset catalog files in the asset library.Returns a collection of all asset catalogs in the library, as a mapping from
    UUID to the catalog.If there are multiple catalog definition files, they will be merged
    together.

    """

def write(catalogs, catalog_filepath, asset_library_meta) -> None:
    """Create a catalog file from the list of catalogs."""
