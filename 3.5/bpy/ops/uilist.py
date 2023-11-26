import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def entry_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        list_path: typing.Union[str, typing.Any] = "",
        active_index_path: typing.Union[str, typing.Any] = ""):
    ''' Add an entry to the list after the current active item

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param list_path: list_path
    :type list_path: typing.Union[str, typing.Any]
    :param active_index_path: active_index_path
    :type active_index_path: typing.Union[str, typing.Any]
    '''

    pass


def entry_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        list_path: typing.Union[str, typing.Any] = "",
        active_index_path: typing.Union[str, typing.Any] = "",
        direction: typing.Optional[typing.Any] = 'UP'):
    ''' Move an entry in the list up or down

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param list_path: list_path
    :type list_path: typing.Union[str, typing.Any]
    :param active_index_path: active_index_path
    :type active_index_path: typing.Union[str, typing.Any]
    :param direction: Direction * ``UP`` UP -- UP. * ``DOWN`` DOWN -- DOWN.
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def entry_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        list_path: typing.Union[str, typing.Any] = "",
        active_index_path: typing.Union[str, typing.Any] = ""):
    ''' Remove the selected entry from the list

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param list_path: list_path
    :type list_path: typing.Union[str, typing.Any]
    :param active_index_path: active_index_path
    :type active_index_path: typing.Union[str, typing.Any]
    '''

    pass
