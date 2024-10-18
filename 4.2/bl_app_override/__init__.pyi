import typing
import collections.abc
import typing_extensions
from . import helpers as helpers

def class_filter(cls_parent, **kw): ...
def ui_draw_filter_register(
    *,
    ui_ignore_classes=None,
    ui_ignore_operator=None,
    ui_ignore_property=None,
    ui_ignore_menu=None,
    ui_ignore_label=None,
): ...
def ui_draw_filter_unregister(ui_ignore_store): ...
