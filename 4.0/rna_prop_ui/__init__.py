import sys
import typing

GenericType = typing.TypeVar("GenericType")


class PropertyPanel:
    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_order = None
    ''' '''

    def draw(self, context):
        ''' 

        '''
        pass

    def poll(self, context):
        ''' 

        '''
        pass


def draw(layout, context, context_member, property_type, use_edit):
    ''' 

    '''

    pass


def rna_idprop_context_value(context, context_member, property_type):
    ''' 

    '''

    pass


def rna_idprop_has_properties(rna_item):
    ''' 

    '''

    pass


def rna_idprop_quote_path(prop):
    ''' 

    '''

    pass


def rna_idprop_ui_create(item, prop, default, min, max, soft_min, soft_max,
                         description, overridable, subtype, step, precision,
                         id_type):
    ''' 

    '''

    pass


def rna_idprop_ui_prop_clear(item, prop):
    ''' 

    '''

    pass


def rna_idprop_ui_prop_default_set(item, prop, value):
    ''' 

    '''

    pass


def rna_idprop_ui_prop_update(item, prop):
    ''' 

    '''

    pass


def rna_idprop_value_item_type(value):
    ''' 

    '''

    pass


def rna_idprop_value_to_python(value):
    ''' 

    '''

    pass
