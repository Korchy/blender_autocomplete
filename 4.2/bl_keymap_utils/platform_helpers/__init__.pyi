import typing
import collections.abc
import typing_extensions

def keyconfig_data_oskey_from_ctrl(keyconfig_data_src, *, filter_fn=None): ...
def keyconfig_data_oskey_from_ctrl_for_macos(keyconfig_data_src):
    """Use for apple since Cmd is typically used in-place of Ctrl."""
