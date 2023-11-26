import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def attribute_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "Attribute",
        domain: typing.Optional[typing.Union[str, int]] = 'POINT',
        data_type: typing.Optional[typing.Union[str, int]] = 'FLOAT'):
    ''' Add attribute to geometry

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of new attribute
    :type name: typing.Union[str, typing.Any]
    :param domain: Domain, Type of element that attribute is stored on
    :type domain: typing.Optional[typing.Union[str, int]]
    :param data_type: Data Type, Type of data stored in attribute
    :type data_type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def attribute_convert(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'GENERIC',
        domain: typing.Optional[typing.Union[str, int]] = 'POINT',
        data_type: typing.Optional[typing.Union[str, int]] = 'FLOAT'):
    ''' Change how the attribute is stored

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    :param domain: Domain, Which geometry element to move the attribute to
    :type domain: typing.Optional[typing.Union[str, int]]
    :param data_type: Data Type
    :type data_type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def attribute_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove attribute from geometry

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def color_attribute_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "Color",
        domain: typing.Optional[typing.Union[str, int]] = 'POINT',
        data_type: typing.Optional[typing.Union[str, int]] = 'FLOAT_COLOR',
        color: typing.Optional[typing.Any] = (0.0, 0.0, 0.0, 1.0)):
    ''' Add color attribute to geometry

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of new color attribute
    :type name: typing.Union[str, typing.Any]
    :param domain: Domain, Type of element that attribute is stored on
    :type domain: typing.Optional[typing.Union[str, int]]
    :param data_type: Data Type, Type of data stored in attribute
    :type data_type: typing.Optional[typing.Union[str, int]]
    :param color: Color, Default fill color
    :type color: typing.Optional[typing.Any]
    '''

    pass


def color_attribute_convert(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        domain: typing.Optional[typing.Union[str, int]] = 'POINT',
        data_type: typing.Optional[typing.Union[str, int]] = 'FLOAT_COLOR'):
    ''' Change how the color attribute is stored

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param domain: Domain, Type of element that attribute is stored on
    :type domain: typing.Optional[typing.Union[str, int]]
    :param data_type: Data Type, Type of data stored in attribute
    :type data_type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def color_attribute_duplicate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Duplicate color attribute

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def color_attribute_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove color attribute from geometry

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def color_attribute_render_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "Color"):
    ''' Set default color attribute used for rendering

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of color attribute
    :type name: typing.Union[str, typing.Any]
    '''

    pass
