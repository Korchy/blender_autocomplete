import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def addon_keymap_register(keymap_data) -> None:
    """Register a set of keymaps for addons using a list of keymaps.See blender_defaults.py for examples of the format this takes."""

def addon_keymap_unregister(keymap_data) -> None:
    """Unregister a set of keymaps for addons."""

def keyconfig_test(kc) -> None: ...
