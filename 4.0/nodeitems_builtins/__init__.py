import sys
import typing
import nodeitems_utils

GenericType = typing.TypeVar("GenericType")


class SortedNodeCategory(nodeitems_utils.NodeCategory):
    def poll(self, _context):
        ''' 

        '''
        pass


class CompositorNodeCategory(SortedNodeCategory, nodeitems_utils.NodeCategory):
    def poll(self, context):
        ''' 

        '''
        pass


class ShaderNodeCategory(SortedNodeCategory, nodeitems_utils.NodeCategory):
    def poll(self, context):
        ''' 

        '''
        pass


def group_input_output_item_poll(context):
    ''' 

    '''

    pass


def group_tools_draw(_self, layout, _context):
    ''' 

    '''

    pass


def node_group_items(context):
    ''' 

    '''

    pass


def register():
    ''' 

    '''

    pass


def unregister():
    ''' 

    '''

    pass
