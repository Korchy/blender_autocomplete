import typing
import collections.abc
from . import helpers

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def class_filter(cls_parent, kw): ...
def ui_draw_filter_register(
    ui_ignore_classes=None,
    ui_ignore_operator=None,
    ui_ignore_property=None,
    ui_ignore_menu=None,
    ui_ignore_label=None,
): ...
def ui_draw_filter_unregister(ui_ignore_store): ...
