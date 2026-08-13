import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

def addon_keymap_register(
    keymap_data: list[tuple[str, dict[str, typing.Any], dict[str, typing.Any]]],
) -> None:
    """Register a set of keymaps for addons using a list of keymaps.See blender_default.py for examples of the format this takes.

    :param keymap_data: A list of keymap definitions to register.
    """

def addon_keymap_unregister(
    keymap_data: list[tuple[str, dict[str, typing.Any], dict[str, typing.Any]]],
) -> None:
    """Unregister a set of keymaps for addons.

    :param keymap_data: A list of keymap definitions to unregister.
    """

def keyconfig_test(kc: bpy.types.KeyConfig) -> bool:
    """Test a key configuration for duplicate key-map item assignments.

    :param kc: The key configuration to test.
    :return: True if any duplicates were found.
    """
