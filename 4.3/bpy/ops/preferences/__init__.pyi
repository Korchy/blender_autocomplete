import typing
import collections.abc
import typing_extensions
import bpy.types

def addon_disable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    module: str = "",
):
    """Turn off this add-on

    :type execution_context: int | str | None
    :type undo: bool | None
    :param module: Module, Module name of the add-on to disable
    :type module: str
    """

def addon_enable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    module: str = "",
):
    """Turn on this add-on

    :type execution_context: int | str | None
    :type undo: bool | None
    :param module: Module, Module name of the add-on to enable
    :type module: str
    """

def addon_expand(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    module: str = "",
):
    """Display information and preferences for this add-on

    :type execution_context: int | str | None
    :type undo: bool | None
    :param module: Module, Module name of the add-on to expand
    :type module: str
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
):
    """Install an add-on

    :type execution_context: int | str | None
    :type undo: bool | None
    :param overwrite: Overwrite, Remove existing add-ons with the same ID
    :type overwrite: bool | None
    :param enable_on_install: Enable on Install, Enable after installing
    :type enable_on_install: bool | None
    :param target: Target Path
    :type target: str | None
    :param filepath: filepath
    :type filepath: str
    :param filter_folder: Filter folders
    :type filter_folder: bool | None
    :param filter_python: Filter Python
    :type filter_python: bool | None
    :param filter_glob: filter_glob
    :type filter_glob: str
    """

def addon_refresh(execution_context: int | str | None = None, undo: bool | None = None):
    """Scan add-on directories for new modules

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def addon_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    module: str = "",
):
    """Delete the add-on from the file system

    :type execution_context: int | str | None
    :type undo: bool | None
    :param module: Module, Module name of the add-on to remove
    :type module: str
    """

def addon_show(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    module: str = "",
):
    """Show add-on preferences

    :type execution_context: int | str | None
    :type undo: bool | None
    :param module: Module, Module name of the add-on to expand
    :type module: str
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
):
    """Install an application template

    :type execution_context: int | str | None
    :type undo: bool | None
    :param overwrite: Overwrite, Remove existing template with the same ID
    :type overwrite: bool | None
    :param filepath: filepath
    :type filepath: str
    :param filter_folder: Filter folders
    :type filter_folder: bool | None
    :param filter_glob: filter_glob
    :type filter_glob: str
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
    filter_collada: bool | None = False,
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
):
    """Add a directory to be used by the Asset Browser as source of assets

        :type execution_context: int | str | None
        :type undo: bool | None
        :param directory: Directory, Directory of the file
        :type directory: str
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
    """

def asset_library_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
):
    """Remove a path to a .blend file, so the Asset Browser will not attempt to show it anymore

    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: Index
    :type index: int | None
    """

def associate_blend(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Use this installation for .blend files and to display thumbnails

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def autoexec_path_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add path to exclude from auto-execution

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def autoexec_path_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
):
    """Remove path to exclude from auto-execution

    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: Index
    :type index: int | None
    """

def copy_prev(execution_context: int | str | None = None, undo: bool | None = None):
    """Copy settings from previous version

    :type execution_context: int | str | None
    :type undo: bool | None
    """

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
):
    """Add a new repository used to store extensions

        :type execution_context: int | str | None
        :type undo: bool | None
        :param name: Name, Unique repository name
        :type name: str
        :param remote_url: URL, Remote URL to the extension repository, the file-system may be referenced using the file URI scheme: "file://"
        :type remote_url: str
        :param use_access_token: Requires Access Token, Repository requires an access token
        :type use_access_token: bool | None
        :param access_token: Secret, Personal access token, may be required by some repositories
        :type access_token: str
        :param use_sync_on_startup: Check for Updates on Startup, Allow Blender to check for updates upon launch
        :type use_sync_on_startup: bool | None
        :param use_custom_directory: Custom Directory, Manually set the path for extensions to be stored. When disabled a user's extensions directory is created.
        :type use_custom_directory: bool | None
        :param custom_directory: Custom Directory, The local directory containing extensions
        :type custom_directory: str
        :param type: Type, The kind of repository to add

    REMOTE
    Add Remote Repository -- Add a repository referencing an remote repository with support for listing and updating extensions.

    LOCAL
    Add Local Repository -- Add a repository managed manually without referencing an external repository.
        :type type: typing.Literal['REMOTE','LOCAL'] | None
    """

def extension_repo_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
    remove_files: bool | None = False,
):
    """Remove an extension repository

    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: Index
    :type index: int | None
    :param remove_files: Remove Files, Remove extension files when removing the repository
    :type remove_files: bool | None
    """

def extension_url_drop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    url: str = "",
):
    """Handle dropping an extension URL

    :type execution_context: int | str | None
    :type undo: bool | None
    :param url: URL, Location of the extension to install
    :type url: str
    """

def keyconfig_activate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str
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
):
    """Export key configuration to a Python script

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All Keymaps, Write all keymaps (not just user modified)
    :type all: bool | None
    :param filepath: filepath
    :type filepath: str
    :param filter_folder: Filter folders
    :type filter_folder: bool | None
    :param filter_text: Filter text
    :type filter_text: bool | None
    :param filter_python: Filter Python
    :type filter_python: bool | None
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
):
    """Import key configuration from a Python script

    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str
    :param filter_folder: Filter folders
    :type filter_folder: bool | None
    :param filter_text: Filter text
    :type filter_text: bool | None
    :param filter_python: Filter Python
    :type filter_python: bool | None
    :param keep_original: Keep Original, Keep original file after copying to configuration folder
    :type keep_original: bool | None
    """

def keyconfig_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove key config

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def keyconfig_test(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Test key configuration for conflicts

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def keyitem_add(execution_context: int | str | None = None, undo: bool | None = None):
    """Add key map item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def keyitem_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    item_id: int | None = 0,
):
    """Remove key map item

    :type execution_context: int | str | None
    :type undo: bool | None
    :param item_id: Item Identifier, Identifier of the item to remove
    :type item_id: int | None
    """

def keyitem_restore(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    item_id: int | None = 0,
):
    """Restore key map item

    :type execution_context: int | str | None
    :type undo: bool | None
    :param item_id: Item Identifier, Identifier of the item to restore
    :type item_id: int | None
    """

def keymap_restore(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
):
    """Restore key map(s)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All Keymaps, Restore all keymaps to default
    :type all: bool | None
    """

def reset_default_theme(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Reset to the default theme colors

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def script_directory_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    directory: str = "",
    filter_folder: bool | None = True,
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param directory: directory
    :type directory: str
    :param filter_folder: Filter Folders
    :type filter_folder: bool | None
    """

def script_directory_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: Index, Index of the script directory to remove
    :type index: int | None
    """

def studiolight_copy_settings(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
):
    """Copy Studio Light settings to the Studio Light editor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: index
    :type index: int | None
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
):
    """Install a user defined light

        :type execution_context: int | str | None
        :type undo: bool | None
        :param files: File Path
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param directory: directory
        :type directory: str
        :param filter_folder: Filter Folders
        :type filter_folder: bool | None
        :param filter_glob: filter_glob
        :type filter_glob: str
        :param type: Type

    MATCAP
    MatCap -- Install custom MatCaps.

    WORLD
    World -- Install custom HDRIs.

    STUDIO
    Studio -- Install custom Studio Lights.
        :type type: typing.Literal['MATCAP','WORLD','STUDIO'] | None
    """

def studiolight_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filename: str = "StudioLight",
):
    """Save custom studio light from the studio light editor settings

    :type execution_context: int | str | None
    :type undo: bool | None
    :param filename: Name
    :type filename: str
    """

def studiolight_uninstall(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
):
    """Delete Studio Light

    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: index
    :type index: int | None
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
):
    """Load and apply a Blender XML theme file

    :type execution_context: int | str | None
    :type undo: bool | None
    :param overwrite: Overwrite, Remove existing theme file if exists
    :type overwrite: bool | None
    :param filepath: filepath
    :type filepath: str
    :param filter_folder: Filter folders
    :type filter_folder: bool | None
    :param filter_glob: filter_glob
    :type filter_glob: str
    """

def unassociate_blend(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove this installation's associations with .blend files

    :type execution_context: int | str | None
    :type undo: bool | None
    """
