import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def addon_keymap_register(keymap_data):
    """Register a set of keymaps for addons using a list of keymaps.See 'blender_defaults.py' for examples of the format this takes."""

    ...

def addon_keymap_register(keymap_data):
    """Register a set of keymaps for addons using a list of keymaps.See 'blender_defaults.py' for examples of the format this takes."""

    ...

def addon_keymap_unregister(keymap_data):
    """Unregister a set of keymaps for addons."""

    ...

def addon_keymap_unregister(keymap_data):
    """Unregister a set of keymaps for addons."""

    ...

def keyconfig_test(kc): ...
def keyconfig_test(kc): ...
