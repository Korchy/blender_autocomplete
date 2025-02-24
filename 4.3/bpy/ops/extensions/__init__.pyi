import typing
import collections.abc
import typing_extensions
import bpy.types

def dummy_progress(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def package_disable(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Turn off this extension

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def package_enable_not_installed(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Turn on this extension

    :type execution_context: int | str | None
    :type undo: bool | None
    """

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
):
    """Download and install the extension

    :type execution_context: int | str | None
    :type undo: bool | None
    :param repo_directory: Repo Directory
    :type repo_directory: str
    :param repo_index: Repo Index
    :type repo_index: int | None
    :param pkg_id: Package ID
    :type pkg_id: str
    :param enable_on_install: Enable on Install, Enable after installing
    :type enable_on_install: bool | None
    :param url: URL
    :type url: str
    :param do_legacy_replace: Do Legacy Replace
    :type do_legacy_replace: bool | None
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
):
    """Install extensions from files into a locally managed repository

    :type execution_context: int | str | None
    :type undo: bool | None
    :param filter_glob: filter_glob
    :type filter_glob: str
    :param directory: Directory
    :type directory: str
    :param files: files
    :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
    :param filepath: filepath
    :type filepath: str
    :param repo: User Repository, The user repository to install extensions into
    :type repo: str | None
    :param enable_on_install: Enable on Install, Enable after installing
    :type enable_on_install: bool | None
    :param target: Legacy Target Path, Path to install legacy add-on packages to
    :type target: str | None
    :param overwrite: Legacy Overwrite, Remove existing add-ons with the same ID
    :type overwrite: bool | None
    :param url: URL
    :type url: str
    """

def package_install_marked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    enable_on_install: bool | None = True,
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param enable_on_install: Enable on Install, Enable after installing
    :type enable_on_install: bool | None
    """

def package_mark_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pkg_id: str = "",
    repo_index: int | None = -1,
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param pkg_id: Package ID
    :type pkg_id: str
    :param repo_index: Repo Index
    :type repo_index: int | None
    """

def package_mark_clear_all(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def package_mark_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pkg_id: str = "",
    repo_index: int | None = -1,
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param pkg_id: Package ID
    :type pkg_id: str
    :param repo_index: Repo Index
    :type repo_index: int | None
    """

def package_mark_set_all(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def package_obsolete_marked(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Zeroes package versions, useful for development - to test upgrading

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def package_show_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pkg_id: str = "",
    repo_index: int | None = -1,
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param pkg_id: Package ID
    :type pkg_id: str
    :param repo_index: Repo Index
    :type repo_index: int | None
    """

def package_show_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pkg_id: str = "",
    repo_index: int | None = -1,
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param pkg_id: Package ID
    :type pkg_id: str
    :param repo_index: Repo Index
    :type repo_index: int | None
    """

def package_show_settings(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pkg_id: str = "",
    repo_index: int | None = -1,
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param pkg_id: Package ID
    :type pkg_id: str
    :param repo_index: Repo Index
    :type repo_index: int | None
    """

def package_theme_disable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pkg_id: str = "",
    repo_index: int | None = -1,
):
    """Turn off this theme

    :type execution_context: int | str | None
    :type undo: bool | None
    :param pkg_id: Package ID
    :type pkg_id: str
    :param repo_index: Repo Index
    :type repo_index: int | None
    """

def package_theme_enable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pkg_id: str = "",
    repo_index: int | None = -1,
):
    """Turn off this theme

    :type execution_context: int | str | None
    :type undo: bool | None
    :param pkg_id: Package ID
    :type pkg_id: str
    :param repo_index: Repo Index
    :type repo_index: int | None
    """

def package_uninstall(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    repo_directory: str = "",
    repo_index: int | None = -1,
    pkg_id: str = "",
):
    """Disable and uninstall the extension

    :type execution_context: int | str | None
    :type undo: bool | None
    :param repo_directory: Repo Directory
    :type repo_directory: str
    :param repo_index: Repo Index
    :type repo_index: int | None
    :param pkg_id: Package ID
    :type pkg_id: str
    """

def package_uninstall_marked(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def package_uninstall_system(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def package_upgrade_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_active_only: bool | None = False,
):
    """Upgrade all the extensions to their latest version for all the remote repositories

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_active_only: Active Only, Only sync the active repository
    :type use_active_only: bool | None
    """

def repo_enable_from_drop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    repo_index: int | None = -1,
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param repo_index: Repo Index
    :type repo_index: int | None
    """

def repo_lock_all(execution_context: int | str | None = None, undo: bool | None = None):
    """Lock repositories - to test locking

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def repo_refresh_all(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Scan extension & legacy add-ons for changes to modules & meta-data (similar to restarting). Any issues are reported as warnings

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def repo_sync(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    repo_directory: str = "",
    repo_index: int | None = -1,
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param repo_directory: Repo Directory
    :type repo_directory: str
    :param repo_index: Repo Index
    :type repo_index: int | None
    """

def repo_sync_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_active_only: bool | None = False,
):
    """Refresh the list of extensions for all the remote repositories

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_active_only: Active Only, Only sync the active repository
    :type use_active_only: bool | None
    """

def repo_unlock(execution_context: int | str | None = None, undo: bool | None = None):
    """Remove the repository file-system lock

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def repo_unlock_all(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Unlock repositories - to test unlocking

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def status_clear(execution_context: int | str | None = None, undo: bool | None = None):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def status_clear_errors(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def userpref_allow_online(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Allow internet access. Blender may access configured online extension repositories. Installed third party add-ons may access the internet for their own functionality

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def userpref_allow_online_popup(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Allow internet access. Blender may access configured online extension repositories. Installed third party add-ons may access the internet for their own functionality

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def userpref_show_for_update(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Open extensions preferences

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def userpref_show_online(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Show system preferences "Network" panel to allow online access

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def userpref_tags_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: bool | None = False,
    data_path: str = "",
):
    """Set the value of all tags

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Value, Enable or disable all tags
    :type value: bool | None
    :param data_path: Data Path
    :type data_path: str
    """
