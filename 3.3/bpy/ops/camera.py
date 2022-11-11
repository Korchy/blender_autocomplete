import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def preset_add(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               name: str = "",
               remove_name: bool = False,
               remove_active: bool = False,
               use_focal_length: bool = False):
    ''' Add or remove a Camera Preset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool
    :param remove_active: remove_active
    :type remove_active: bool
    :param use_focal_length: Include Focal Length, Include focal length into the preset
    :type use_focal_length: bool
    '''

    pass
