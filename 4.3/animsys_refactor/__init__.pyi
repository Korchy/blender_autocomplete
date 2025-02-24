import typing
import collections.abc
import typing_extensions

class DataPathBuilder:
    """Dummy class used to parse fcurve and driver data paths."""

    data_path: typing.Any

    def resolve(self, real_base, rna_update_from_map, fcurve, log):
        """Return (attribute, value) pairs.

        :param real_base:
        :param rna_update_from_map:
        :param fcurve:
        :param log:
        """

def anim_data_actions(anim_data): ...
def classes_recursive(base_type, clss=None): ...
def find_path_new(id_data, data_path, rna_update_from_map, fcurve, log): ...
def id_iter(): ...
def update_data_paths(rna_update, log=None): ...
