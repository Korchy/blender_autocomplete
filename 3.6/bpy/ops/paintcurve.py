import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def add_point(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        location: typing.Optional[typing.Any] = (0, 0)):
    ''' Add New Paint Curve Point

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param location: Location, Location of vertex in area space
    :type location: typing.Optional[typing.Any]
    '''

    pass


def add_point_slide(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        PAINTCURVE_OT_add_point: typing.Optional['add_point'] = None,
        PAINTCURVE_OT_slide: typing.Optional['slide'] = None):
    ''' Add new curve point and slide it

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param PAINTCURVE_OT_add_point: Add New Paint Curve Point, Add New Paint Curve Point
    :type PAINTCURVE_OT_add_point: typing.Optional['add_point']
    :param PAINTCURVE_OT_slide: Slide Paint Curve Point, Select and slide paint curve point
    :type PAINTCURVE_OT_slide: typing.Optional['slide']
    '''

    pass


def cursor(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None):
    ''' Place cursor

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def delete_point(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove Paint Curve Point

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def draw(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None):
    ''' Draw curve

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def new(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add new paint curve

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None,
           *,
           location: typing.Optional[typing.Any] = (0, 0),
           toggle: typing.Optional[typing.Union[bool, typing.Any]] = False,
           extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select a paint curve point

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param location: Location, Location of vertex in area space
    :type location: typing.Optional[typing.Any]
    :param toggle: Toggle, (De)select all
    :type toggle: typing.Optional[typing.Union[bool, typing.Any]]
    :param extend: Extend, Extend selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def slide(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None,
          *,
          align: typing.Optional[typing.Union[bool, typing.Any]] = False,
          select: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Select and slide paint curve point

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param align: Align Handles, Aligns opposite point handle during transform
    :type align: typing.Optional[typing.Union[bool, typing.Any]]
    :param select: Select, Attempt to select a point handle before transform
    :type select: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass
