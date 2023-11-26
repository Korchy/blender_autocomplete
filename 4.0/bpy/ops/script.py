import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def execute_preset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        menu_idname: typing.Union[str, typing.Any] = ""):
    ''' Load a preset :File: `startup/bl_operators/presets.py\:233 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L233>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: filepath
    :type filepath: typing.Union[str, typing.Any]
    :param menu_idname: Menu ID Name, ID name of the menu this was called from
    :type menu_idname: typing.Union[str, typing.Any]
    '''

    pass


def python_file_run(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = ""):
    ''' Run Python file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: Path
    :type filepath: typing.Union[str, typing.Any]
    '''

    pass


def reload(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None):
    ''' Reload scripts

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass
