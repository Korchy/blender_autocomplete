import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class _ext_global:
    idmap_pair: typing.Any
    module_handle: typing.Any

def check(module_name: str):
    """Returns the loaded state of the addon.

    :param module_name: The name of the addon and module.
    :type module_name: str
    :return: (loaded_default, loaded_state)
    """

    ...

def check_extension(module_name):
    """Return true if the module is an extension."""

    ...

def disable(
    module_name: str, default_set: bool = False, handle_error: typing.Any = None
):
    """Disables an addon by name.

    :param module_name: The name of the addon and module.
    :type module_name: str
    :param default_set: Set the user-preference.
    :type default_set: bool
    :param handle_error: Called in the case of an error, taking an exception argument.
    :type handle_error: typing.Any
    """

    ...

def disable_all(): ...
def enable(
    module_name: str,
    default_set: bool = False,
    persistent: bool = False,
    handle_error: typing.Any = None,
):
    """Enables an addon by name.

    :param module_name: the name of the addon and module.
    :type module_name: str
    :param default_set: Set the user-preference.
    :type default_set: bool
    :param persistent: Ensure the addon is enabled for the entire session (after loading new files).
    :type persistent: bool
    :param handle_error: Called in the case of an error, taking an exception argument.
    :type handle_error: typing.Any
    :return: the loaded module or None on failure.
    """

    ...

def module_bl_info(mod, info_basis=None): ...
def modules(module_cache={"add_camera_rigs": None}, refresh=True): ...
def modules_refresh(module_cache={"add_camera_rigs": None}): ...
def paths(): ...
def reset_all(reload_scripts=False):
    """Sets the addon state based on the user preferences."""

    ...
