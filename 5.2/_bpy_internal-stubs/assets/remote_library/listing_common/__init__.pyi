import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def api_versioned(subpath) -> None:
    """Return the subpath, prefixed with API_VERSIONED_SUBDIR."""
