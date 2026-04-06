import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def get_all_referenced_ids(id, ref_map) -> None:
    """Return a set of IDs directly or indirectly referenced by id."""

def get_id_reference_map() -> None:
    """Return a dictionary of direct data-block references for every data-block in the blend file."""

def recursive_get_referenced_ids(ref_map, id, referenced_ids, visited) -> None:
    """Recursively populate referenced_ids with IDs referenced by id."""
