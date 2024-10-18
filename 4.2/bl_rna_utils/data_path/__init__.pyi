import typing
import collections.abc
import typing_extensions

class _TokenizeDataPath:
    """Class to split up tokens of a data-path.Note that almost all access generates new objects with additional paths,
    with the exception of iteration which is the intended way to access the resulting data.
    """

    data_path: typing.Any

def decompose_data_path(data_path):
    """Return the components of a data path split into a list."""

def property_definition_from_data_path(base, data_path):
    """Return an RNA property definition from an object and a data path.In Blender this is often used with context as the base and a
    path that it references, for example .space_data.lock_camera.

    """
