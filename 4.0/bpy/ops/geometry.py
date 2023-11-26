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


def execute_node_group(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        asset_library_type: typing.Optional[typing.Union[str, int]] = 'LOCAL',
        asset_library_identifier: typing.Union[str, typing.Any] = "",
        relative_asset_identifier: typing.Union[str, typing.Any] = "",
        name: typing.Union[str, typing.Any] = "",
        session_uuid: typing.Optional[typing.Any] = 0):
    ''' Execute a node group on geometry

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param asset_library_type: Asset Library Type
    :type asset_library_type: typing.Optional[typing.Union[str, int]]
    :param asset_library_identifier: Asset Library Identifier
    :type asset_library_identifier: typing.Union[str, typing.Any]
    :param relative_asset_identifier: Relative Asset Identifier
    :type relative_asset_identifier: typing.Union[str, typing.Any]
    :param name: Name, Name of the data-block to use by the operator
    :type name: typing.Union[str, typing.Any]
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: typing.Optional[typing.Any]
    '''

    pass


def geometry_randomization(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        value: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Toggle geometry randomization for debugging purposes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param value: Value, Randomize the order of geometry elements (e.g. vertices or edges) after some operations where there are no guarantees about the order. This avoids accidentally depending on something that may change in the future
    :type value: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass
