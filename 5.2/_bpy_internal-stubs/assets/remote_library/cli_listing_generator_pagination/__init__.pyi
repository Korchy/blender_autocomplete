import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def paginate_asset_list(assets, files, num_assets_per_page=0) -> None:
    """Return a list of asset pages.Each page is no longer than num_assets_per_page long. If zero, all assets
    are put in the same page.The files listed in each page are determined by the assets on that page.
    This means that its possible for multiple pages to list the same file; this
    occurs when that file contains multiple assets, spread across multiple pages.

    """
