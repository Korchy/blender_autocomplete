import sys
import typing
import bpy.types
import mathutils

GenericType = typing.TypeVar("GenericType")


def attribute_add(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  name: str = "Attribute",
                  domain: typing.Union[int, str] = 'POINT',
                  data_type: typing.Union[int, str] = 'FLOAT'):
    ''' Add attribute to geometry

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of new attribute
    :type name: str
    :param domain: Domain, Type of element that attribute is stored on
    :type domain: typing.Union[int, str]
    :param data_type: Data Type, Type of data stored in attribute
    :type data_type: typing.Union[int, str]
    '''

    pass


def attribute_convert(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      mode: typing.Union[str, int] = 'GENERIC',
                      domain: typing.Union[int, str] = 'POINT',
                      data_type: typing.Union[int, str] = 'FLOAT'):
    ''' Change how the attribute is stored

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param domain: Domain, Which geometry element to move the attribute to
    :type domain: typing.Union[int, str]
    :param data_type: Data Type
    :type data_type: typing.Union[int, str]
    '''

    pass


def attribute_remove(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Remove attribute from geometry

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def color_attribute_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        name: str = "Color",
        domain: typing.Union[int, str] = 'POINT',
        data_type: typing.Union[int, str] = 'FLOAT_COLOR',
        color: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float, float], 'mathutils.Vector'] = (0.0,
                                                                        0.0,
                                                                        0.0,
                                                                        1.0)):
    ''' Add color attribute to geometry

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of new color attribute
    :type name: str
    :param domain: Domain, Type of element that attribute is stored on
    :type domain: typing.Union[int, str]
    :param data_type: Data Type, Type of data stored in attribute
    :type data_type: typing.Union[int, str]
    :param color: Color, Default fill color
    :type color: typing.Union[typing.List[float], typing.Tuple[float, float, float, float], 'mathutils.Vector']
    '''

    pass


def color_attribute_duplicate(override_context: typing.
                              Union[typing.Dict, 'bpy.types.Context'] = None,
                              execution_context: typing.Union[str, int] = None,
                              undo: bool = None):
    ''' Duplicate color attribute

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def color_attribute_remove(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None):
    ''' Remove color attribute from geometry

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def color_attribute_render_set(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        name: str = "Color"):
    ''' Set default color attribute used for rendering

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of color attribute
    :type name: str
    '''

    pass
