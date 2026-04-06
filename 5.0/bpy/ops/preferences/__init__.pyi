import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

def addon_disable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    module: str = "",
) -> None:
    """Turn off this add-on

    :param module: Module, Module name of the add-on to disable
    """

def addon_enable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    module: str = "",
) -> None:
    """Turn on this add-on

    :param module: Module, Module name of the add-on to enable
    """

def addon_expand(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    module: str = "",
) -> None:
    """Display information and preferences for this add-on

    :param module: Module, Module name of the add-on to expand
    """

def addon_install(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    overwrite: bool | None = True,
    enable_on_install: bool | None = False,
    target: str | None = "",
    filepath: str = "",
    filter_folder: bool | None = True,
    filter_python: bool | None = True,
    filter_glob: str = "*.py;*.zip",
) -> None:
    """Install an add-on

    :param overwrite: Overwrite, Remove existing add-ons with the same ID
    :param enable_on_install: Enable on Install, Enable after installing
    :param target: Target Path
    :param filepath: filepath
    :param filter_folder: Filter folders
    :param filter_python: Filter Python
    :param filter_glob: filter_glob
    """

def addon_refresh(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Scan add-on directories for new modules"""

def addon_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    module: str = "",
) -> None:
    """Delete the add-on from the file system

    :param module: Module, Module name of the add-on to remove
    """

def addon_show(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    module: str = "",
) -> None:
    """Show add-on preferences

    :param module: Module, Module name of the add-on to expand
    """

def app_template_install(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    overwrite: bool | None = True,
    filepath: str = "",
    filter_folder: bool | None = True,
    filter_glob: str = "*.zip",
) -> None:
    """Install an application template

    :param overwrite: Overwrite, Remove existing template with the same ID
    :param filepath: filepath
    :param filter_folder: Filter folders
    :param filter_glob: filter_glob
    """

def asset_library_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    directory: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = False,
    filter_movie: bool | None = False,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
) -> None:
    """Add a directory to be used by the Asset Browser as source of assets

        :param directory: Directory, Directory of the file
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :param filter_blender: Filter .blend files
        :param filter_backup: Filter .blend files
        :param filter_image: Filter image files
        :param filter_movie: Filter movie files
        :param filter_python: Filter Python files
        :param filter_font: Filter font files
        :param filter_sound: Filter sound files
        :param filter_text: Filter text files
        :param filter_archive: Filter archive files
        :param filter_btx: Filter btx files
        :param filter_alembic: Filter Alembic files
        :param filter_usd: Filter USD files
        :param filter_obj: Filter OBJ files
        :param filter_volume: Filter OpenVDB volume files
        :param filter_folder: Filter folders
        :param filter_blenlib: Filter Blender IDs
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :param sort_method: File sorting mode
    """

def asset_library_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
) -> None:
    """Remove a path to a .blend file, so the Asset Browser will not attempt to show it anymore

    :param index: Index
    """

def associate_blend(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Use this installation for .blend files and to display thumbnails"""

def autoexec_path_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add path to exclude from auto-execution"""

def autoexec_path_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
) -> None:
    """Remove path to exclude from auto-execution

    :param index: Index
    """

def copy_prev(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy settings from previous version"""

def extension_repo_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remote_url: str = "",
    use_access_token: bool | None = False,
    access_token: str = "",
    use_sync_on_startup: bool | None = False,
    use_custom_directory: bool | None = False,
    custom_directory: str = "",
    type: typing.Literal["REMOTE", "LOCAL"] | None = "REMOTE",
) -> None:
    """Add a new repository used to store extensions

        :param name: Name, Unique repository name
        :param remote_url: URL, Remote URL to the extension repository, the file-system may be referenced using the file URI scheme: "file://"
        :param use_access_token: Requires Access Token, Repository requires an access token
        :param access_token: Secret, Personal access token, may be required by some repositories
        :param use_sync_on_startup: Check for Updates on Startup, Allow Blender to check for updates upon launch
        :param use_custom_directory: Custom Directory, Manually set the path for extensions to be stored. When disabled a users extensions directory is created.
        :param custom_directory: Custom Directory, The local directory containing extensions
        :param type: Type, The kind of repository to add

    REMOTE
    Add Remote Repository -- Add a repository referencing a remote repository with support for listing and updating extensions.

    LOCAL
    Add Local Repository -- Add a repository managed manually without referencing an external repository.
    """

def extension_repo_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
    remove_files: bool | None = False,
) -> None:
    """Remove an extension repository

    :param index: Index
    :param remove_files: Remove Files, Remove extension files when removing the repository
    """

def extension_url_drop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    url: str = "",
) -> None:
    """Handle dropping an extension URL

    :param url: URL, Location of the extension to install
    """

def keyconfig_activate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
) -> None:
    """Undocumented, consider contributing.

    :param filepath: filepath
    """

def keyconfig_export(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
    filepath: str = "",
    filter_folder: bool | None = True,
    filter_text: bool | None = True,
    filter_python: bool | None = True,
) -> None:
    """Export key configuration to a Python script

    :param all: All Keymaps, Write all keymaps (not just user modified)
    :param filepath: filepath
    :param filter_folder: Filter folders
    :param filter_text: Filter text
    :param filter_python: Filter Python
    """

def keyconfig_import(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "keymap.py",
    filter_folder: bool | None = True,
    filter_text: bool | None = True,
    filter_python: bool | None = True,
    keep_original: bool | None = True,
) -> None:
    """Import key configuration from a Python script

    :param filepath: filepath
    :param filter_folder: Filter folders
    :param filter_text: Filter text
    :param filter_python: Filter Python
    :param keep_original: Keep Original, Keep original file after copying to configuration folder
    """

def keyconfig_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove key config"""

def keyconfig_test(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Test key configuration for conflicts"""

def keyitem_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add key map item"""

def keyitem_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    item_id: int | None = 0,
) -> None:
    """Remove key map item

    :param item_id: Item Identifier, Identifier of the item to remove
    """

def keyitem_restore(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    item_id: int | None = 0,
) -> None:
    """Restore key map item

    :param item_id: Item Identifier, Identifier of the item to restore
    """

def keymap_restore(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
) -> None:
    """Restore key map(s)

    :param all: All Keymaps, Restore all keymaps to default
    """

def reset_default_theme(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset to the default theme colors"""

def script_directory_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    directory: str = "",
    filter_folder: bool | None = True,
) -> None:
    """Undocumented, consider contributing.

    :param directory: directory
    :param filter_folder: Filter Folders
    """

def script_directory_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
) -> None:
    """Undocumented, consider contributing.

    :param index: Index, Index of the script directory to remove
    """

def studiolight_copy_settings(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
) -> None:
    """Copy Studio Light settings to the Studio Light editor

    :param index: index
    """

def studiolight_install(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    directory: str = "",
    filter_folder: bool | None = True,
    filter_glob: str = "*.png;*.jpg;*.hdr;*.exr",
    type: typing.Literal["MATCAP", "WORLD", "STUDIO"] | None = "MATCAP",
) -> None:
    """Install a user defined light

        :param files: File Path
        :param directory: directory
        :param filter_folder: Filter Folders
        :param filter_glob: filter_glob
        :param type: Type

    MATCAP
    MatCap -- Install custom MatCaps.

    WORLD
    World -- Install custom HDRIs.

    STUDIO
    Studio -- Install custom Studio Lights.
    """

def studiolight_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filename: str = "StudioLight",
) -> None:
    """Save custom studio light from the studio light editor settings

    :param filename: Name
    """

def studiolight_uninstall(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
) -> None:
    """Delete Studio Light

    :param index: index
    """

def theme_install(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    overwrite: bool | None = True,
    filepath: str = "",
    filter_folder: bool | None = True,
    filter_glob: str = "*.xml",
) -> None:
    """Load and apply a Blender XML theme file

    :param overwrite: Overwrite, Remove existing theme file if exists
    :param filepath: filepath
    :param filter_folder: Filter folders
    :param filter_glob: filter_glob
    """

def unassociate_blend(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove this installations associations with .blend files"""
