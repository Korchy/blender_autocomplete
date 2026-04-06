import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

def package_disable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Turn off this extension"""

def package_install(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    repo_directory: str = "",
    repo_index: int | None = -1,
    pkg_id: str = "",
    enable_on_install: bool | None = True,
    url: str = "",
    do_legacy_replace: bool | None = False,
) -> None:
    """Download and install the extension

    :param repo_directory: Repo Directory
    :param repo_index: Repo Index
    :param pkg_id: Package ID
    :param enable_on_install: Enable on Install, Enable after installing
    :param url: URL
    :param do_legacy_replace: Do Legacy Replace
    """

def package_install_files(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filter_glob: str = "*.zip;*.py",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    filepath: str = "",
    repo: str | None = "",
    enable_on_install: bool | None = True,
    target: str | None = "",
    overwrite: bool | None = True,
    url: str = "",
) -> None:
    """Install extensions from files into a locally managed repository

    :param filter_glob: filter_glob
    :param directory: Directory
    :param files: files
    :param filepath: filepath
    :param repo: User Repository, The user repository to install extensions into
    :param enable_on_install: Enable on Install, Enable after installing
    :param target: Legacy Target Path, Path to install legacy add-on packages to
    :param overwrite: Legacy Overwrite, Remove existing add-ons with the same ID
    :param url: URL
    """

def package_install_marked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    enable_on_install: bool | None = True,
) -> None:
    """Undocumented, consider contributing.

    :param enable_on_install: Enable on Install, Enable after installing
    """

def package_mark_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pkg_id: str = "",
    repo_index: int | None = -1,
) -> None:
    """Undocumented, consider contributing.

    :param pkg_id: Package ID
    :param repo_index: Repo Index
    """

def package_mark_clear_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

def package_mark_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pkg_id: str = "",
    repo_index: int | None = -1,
) -> None:
    """Undocumented, consider contributing.

    :param pkg_id: Package ID
    :param repo_index: Repo Index
    """

def package_mark_set_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

def package_obsolete_marked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Zeroes package versions, useful for development - to test upgrading"""

def package_show_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pkg_id: str = "",
    repo_index: int | None = -1,
) -> None:
    """Undocumented, consider contributing.

    :param pkg_id: Package ID
    :param repo_index: Repo Index
    """

def package_show_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pkg_id: str = "",
    repo_index: int | None = -1,
) -> None:
    """Undocumented, consider contributing.

    :param pkg_id: Package ID
    :param repo_index: Repo Index
    """

def package_show_settings(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pkg_id: str = "",
    repo_index: int | None = -1,
) -> None:
    """Undocumented, consider contributing.

    :param pkg_id: Package ID
    :param repo_index: Repo Index
    """

def package_theme_disable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pkg_id: str = "",
    repo_index: int | None = -1,
) -> None:
    """Turn off this theme

    :param pkg_id: Package ID
    :param repo_index: Repo Index
    """

def package_theme_enable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pkg_id: str = "",
    repo_index: int | None = -1,
) -> None:
    """Turn off this theme

    :param pkg_id: Package ID
    :param repo_index: Repo Index
    """

def package_uninstall(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    repo_directory: str = "",
    repo_index: int | None = -1,
    pkg_id: str = "",
) -> None:
    """Disable and uninstall the extension

    :param repo_directory: Repo Directory
    :param repo_index: Repo Index
    :param pkg_id: Package ID
    """

def package_uninstall_marked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

def package_uninstall_system(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

def package_upgrade_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_active_only: bool | None = False,
) -> None:
    """Upgrade all the extensions to their latest version for all the remote repositories

    :param use_active_only: Active Only, Only sync the active repository
    """

def repo_enable_from_drop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    repo_index: int | None = -1,
) -> None:
    """Undocumented, consider contributing.

    :param repo_index: Repo Index
    """

def repo_lock_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Lock repositories - to test locking"""

def repo_refresh_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_active_only: bool | None = False,
) -> None:
    """Scan extension & legacy add-ons for changes to modules & meta-data (similar to restarting). Any issues are reported as warnings

    :param use_active_only: Active Only, Only refresh the active repository
    """

def repo_sync(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    repo_directory: str = "",
    repo_index: int | None = -1,
) -> None:
    """Undocumented, consider contributing.

    :param repo_directory: Repo Directory
    :param repo_index: Repo Index
    """

def repo_sync_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_active_only: bool | None = False,
) -> None:
    """Refresh the list of extensions for all the remote repositories

    :param use_active_only: Active Only, Only sync the active repository
    """

def repo_unlock(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the repository file-system lock"""

def repo_unlock_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Unlock repositories - to test unlocking"""

def status_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

def status_clear_errors(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

def userpref_allow_online(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Allow internet access. Blender may access configured online extension repositories. Installed third party add-ons may access the internet for their own functionality"""

def userpref_allow_online_popup(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Allow internet access. Blender may access configured online extension repositories. Installed third party add-ons may access the internet for their own functionality"""

def userpref_show_for_update(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Open extensions preferences"""

def userpref_show_online(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Show system preferences "Network" panel to allow online access"""

def userpref_tags_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: bool | None = False,
    data_path: str = "",
) -> None:
    """Set the value of all tags

    :param value: Value, Enable or disable all tags
    :param data_path: Data Path
    """
