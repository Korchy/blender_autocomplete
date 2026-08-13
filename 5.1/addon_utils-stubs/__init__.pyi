import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class _ext_global:
    idmap_pair: typing.Any
    module_handle: typing.Any

def check(module_name: str) -> tuple[bool, bool]:
    """Returns the loaded state of the addon.

    :param module_name: The name of the addon and module.
    :return: (loaded_default, loaded_state)
    """

def check_extension(module_name) -> None:
    """Return true if the module is an extension."""

def disable(
    module_name: str,
    *,
    default_set: bool = False,
    refresh_handled=False,
    handle_error: None | collections.abc.Callable[None] | None = None,
) -> None:
    """Disables an addon by name.

    :param module_name: The name of the addon and module.
    :param default_set: Set the user-preference.
    :param handle_error: Called in the case of an error, taking an exception argument.
    """

def disable_all() -> None: ...
def enable(
    module_name: str,
    *,
    default_set: bool = False,
    persistent: bool = False,
    refresh_handled: bool = False,
    handle_error: None | collections.abc.Callable[None] | None = None,
) -> None:
    """Enables an addon by name.

        :param module_name: the name of the addon and module.
        :param default_set: Set the user-preference.
        :param persistent: Ensure the addon is enabled for the entire session (after loading new files).
        :param refresh_handled: When true, `extensions_refresh` must have been called with module_name
    included in addon_modules_pending.
    This should be used to avoid many calls to refresh extensions when enabling multiple add-ons at once.
        :param handle_error: Called in the case of an error, taking an exception argument.
        :return: the loaded module or None on failure.
    """

def extensions_refresh(
    ensure_wheels: bool = True,
    addon_modules_pending: None | collections.abc.Sequence[str] | None = None,
    handle_error: None | collections.abc.Callable[None] | None = None,
) -> None:
    """Ensure data relating to extensions is up to date.
    This should be called after extensions on the file-system have changed.

        :param ensure_wheels: When true, refresh installed wheels with wheels used by extensions.
        :param addon_modules_pending: Refresh these add-ons by listing their package names, as if they are enabled.
    This is needed so wheels can be setup before the add-on is enabled.
        :param handle_error: Called in the case of an error, taking an exception argument.
    """

def module_bl_info(mod, *, info_basis=None) -> None: ...
def modules(*, module_cache={}, refresh=True) -> None: ...
def modules_refresh(*, module_cache={}) -> None: ...
def paths() -> None: ...
def reset_all(*, reload_scripts=False) -> None:
    """Sets the addon state based on the user preferences."""

def stale_pending_remove_paths(path_base, paths) -> None: ...
def stale_pending_stage_paths(path_base, paths) -> None: ...
