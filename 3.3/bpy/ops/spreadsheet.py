import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def add_row_filter_rule(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Add a filter to remove rows from the displayed data

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def change_spreadsheet_data_source(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        component_type: int = 0,
        attribute_domain_type: int = 0):
    ''' Change visible data source in the spreadsheet

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param component_type: Component Type
    :type component_type: int
    :param attribute_domain_type: Attribute Domain Type
    :type attribute_domain_type: int
    '''

    pass


def remove_row_filter_rule(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None,
                           *,
                           index: int = 0):
    ''' Remove a row filter from the rules

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param index: Index
    :type index: int
    '''

    pass


def toggle_pin(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Turn on or off pinning :file: startup/bl_operators/spreadsheet.py\:19 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/spreadsheet.py$19> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass
