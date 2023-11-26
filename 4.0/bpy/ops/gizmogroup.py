import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def gizmo_select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False,
        deselect: typing.Optional[typing.Union[bool, typing.Any]] = False,
        toggle: typing.Optional[typing.Union[bool, typing.Any]] = False,
        deselect_all: typing.Optional[typing.Union[bool, typing.Any]] = False,
        select_passthrough: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = False):
    ''' Select the currently highlighted gizmo

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    :param deselect: Deselect, Remove from selection
    :type deselect: typing.Optional[typing.Union[bool, typing.Any]]
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: typing.Optional[typing.Union[bool, typing.Any]]
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: typing.Optional[typing.Union[bool, typing.Any]]
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :type select_passthrough: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def gizmo_tweak(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Tweak the active gizmo

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass
