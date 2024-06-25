import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class AppOverrideState:
    """Utility class to encapsulate overriding the application state
    so that settings can be restored afterwards.
    """

    addon_paths: typing.Any
    addons: typing.Any
    class_ignore: typing.Any
    ui_ignore_classes: typing.Any
    ui_ignore_label: typing.Any
    ui_ignore_menu: typing.Any
    ui_ignore_operator: typing.Any
    ui_ignore_property: typing.Any

    def setup(self): ...
    def teardown(self): ...
