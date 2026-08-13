import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class DataPathBuilder:
    """Dummy class used to parse fcurve and driver data paths."""

    data_path: typing.Any

    def resolve(self, real_base, rna_update_from_map, fcurve, log) -> None:
        """Return (attribute, value) pairs.

        :param real_base:
        :param rna_update_from_map:
        :param fcurve:
        :param log:
        """

def anim_data_actions(anim_data) -> None: ...
def classes_recursive(base_type, clss=None) -> None: ...
def find_path_new(id_data, data_path, rna_update_from_map, fcurve, log) -> None: ...
def id_iter() -> None: ...
def update_data_paths(rna_update, log=None) -> None: ...
