import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class PropertyPanel:
    """The subclass should have its own poll function
    and the variable '_context_path' MUST be set.
    """

    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any

    def draw(self, context):
        """

        :param context:
        """
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

def draw(layout, context, context_member, property_type, use_edit=True): ...
def rna_idprop_context_value(context, context_member, property_type): ...
def rna_idprop_has_properties(rna_item): ...
def rna_idprop_quote_path(prop): ...
def rna_idprop_ui_create(
    item,
    prop,
    default,
    min=0,
    max=1,
    soft_min=None,
    soft_max=None,
    description=None,
    overridable=False,
    subtype=None,
    step=None,
    precision=None,
    id_type="OBJECT",
    items=None,
):
    """Create and initialize a custom property with limits, defaults and other settings."""

    ...

def rna_idprop_ui_prop_clear(item, prop): ...
def rna_idprop_ui_prop_default_set(item, prop, value): ...
def rna_idprop_ui_prop_update(item, prop): ...
def rna_idprop_value_item_type(value): ...
def rna_idprop_value_to_python(value): ...
