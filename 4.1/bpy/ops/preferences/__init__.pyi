import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def addon_disable(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    module: str | typing.Any = "",
):
    """Disable an add-on

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param module: Module, Module name of the add-on to disable
    :type module: str | typing.Any
    """

    ...

def addon_enable(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    module: str | typing.Any = "",
):
    """Enable an add-on

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param module: Module, Module name of the add-on to enable
    :type module: str | typing.Any
    """

    ...

def addon_expand(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    module: str | typing.Any = "",
):
    """Display information and preferences for this add-on

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param module: Module, Module name of the add-on to expand
    :type module: str | typing.Any
    """

    ...

def addon_install(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    overwrite: bool | typing.Any | None = True,
    target: str | None = "",
    filepath: str | typing.Any = "",
    filter_folder: bool | typing.Any | None = True,
    filter_python: bool | typing.Any | None = True,
    filter_glob: str | typing.Any = "*.py;*.zip",
):
    """Install an add-on

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param overwrite: Overwrite, Remove existing add-ons with the same ID
    :type overwrite: bool | typing.Any | None
    :param target: Target Path
    :type target: str | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    :param filter_folder: Filter folders
    :type filter_folder: bool | typing.Any | None
    :param filter_python: Filter Python
    :type filter_python: bool | typing.Any | None
    :param filter_glob: filter_glob
    :type filter_glob: str | typing.Any
    """

    ...

def addon_refresh(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Scan add-on directories for new modules

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def addon_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    module: str | typing.Any = "",
):
    """Delete the add-on from the file system

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param module: Module, Module name of the add-on to remove
    :type module: str | typing.Any
    """

    ...

def addon_show(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    module: str | typing.Any = "",
):
    """Show add-on preferences

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param module: Module, Module name of the add-on to expand
    :type module: str | typing.Any
    """

    ...

def app_template_install(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    overwrite: bool | typing.Any | None = True,
    filepath: str | typing.Any = "",
    filter_folder: bool | typing.Any | None = True,
    filter_glob: str | typing.Any = "*.zip",
):
    """Install an application template

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param overwrite: Overwrite, Remove existing template with the same ID
    :type overwrite: bool | typing.Any | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    :param filter_folder: Filter folders
    :type filter_folder: bool | typing.Any | None
    :param filter_glob: filter_glob
    :type filter_glob: str | typing.Any
    """

    ...

def asset_library_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    directory: str | typing.Any = "",
    hide_props_region: bool | typing.Any | None = True,
    check_existing: bool | typing.Any | None = False,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 9,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
):
    """Add a directory to be used by the Asset Browser as source of assets

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param directory: Directory, Directory of the file
        :type directory: str | typing.Any
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
    """

    ...

def asset_library_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    index: typing.Any | None = 0,
):
    """Remove a path to a .blend file, so the Asset Browser will not attempt to show it anymore

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: Index
    :type index: typing.Any | None
    """

    ...

def associate_blend(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Use this installation for .blend files and to display thumbnails

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def autoexec_path_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add path to exclude from auto-execution

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def autoexec_path_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    index: typing.Any | None = 0,
):
    """Remove path to exclude from auto-execution

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: Index
    :type index: typing.Any | None
    """

    ...

def copy_prev(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy settings from previous version

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def extension_repo_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
    remote_path: str | typing.Any = "",
    use_custom_directory: bool | typing.Any | None = False,
    custom_directory: str | typing.Any = "",
    type: str | None = "REMOTE",
):
    """Add a directory to be used as a local extension repository

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param name: Name, Unique repository name
        :type name: str | typing.Any
        :param remote_path: URL, Remote URL or path for extension repository
        :type remote_path: str | typing.Any
        :param use_custom_directory: Custom Directory, Manually set the path for extensions to be stored. When disabled a users extensions directory is created
        :type use_custom_directory: bool | typing.Any | None
        :param custom_directory: Custom Directory, The local directory containing extensions
        :type custom_directory: str | typing.Any
        :param type: Type, The kind of repository to add

    REMOTE
    Add Remote Repository -- Add a repository referencing an remote repository with support for listing and updating extensions.

    LOCAL
    Add Local Repository -- Add a repository managed manually without referencing an external repository.
        :type type: str | None
    """

    ...

def extension_repo_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    index: typing.Any | None = 0,
    type: str | None = "REPO_ONLY",
):
    """Remove an extension repository

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param index: Index
        :type index: typing.Any | None
        :param type: Type, Method for removing the repository

    REPO_ONLY
    Remove Repository.

    REPO_AND_DIRECTORY
    Remove Repository & Files -- Delete all associated local files when removing.
        :type type: str | None
    """

    ...

def extension_repo_sync(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Synchronize the active extension repository with its remote URL

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def extension_repo_upgrade(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Update any outdated extensions for the active extension repository

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def keyconfig_activate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    """

    ...

def keyconfig_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    all: bool | typing.Any | None = False,
    filepath: str | typing.Any = "",
    filter_folder: bool | typing.Any | None = True,
    filter_text: bool | typing.Any | None = True,
    filter_python: bool | typing.Any | None = True,
):
    """Export key configuration to a Python script

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All Keymaps, Write all keymaps (not just user modified)
    :type all: bool | typing.Any | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    :param filter_folder: Filter folders
    :type filter_folder: bool | typing.Any | None
    :param filter_text: Filter text
    :type filter_text: bool | typing.Any | None
    :param filter_python: Filter Python
    :type filter_python: bool | typing.Any | None
    """

    ...

def keyconfig_import(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "keymap.py",
    filter_folder: bool | typing.Any | None = True,
    filter_text: bool | typing.Any | None = True,
    filter_python: bool | typing.Any | None = True,
    keep_original: bool | typing.Any | None = True,
):
    """Import key configuration from a Python script

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    :param filter_folder: Filter folders
    :type filter_folder: bool | typing.Any | None
    :param filter_text: Filter text
    :type filter_text: bool | typing.Any | None
    :param filter_python: Filter Python
    :type filter_python: bool | typing.Any | None
    :param keep_original: Keep Original, Keep original file after copying to configuration folder
    :type keep_original: bool | typing.Any | None
    """

    ...

def keyconfig_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove key config

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def keyconfig_test(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Test key configuration for conflicts

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def keyitem_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add key map item

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def keyitem_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    item_id: typing.Any | None = 0,
):
    """Remove key map item

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param item_id: Item Identifier, Identifier of the item to remove
    :type item_id: typing.Any | None
    """

    ...

def keyitem_restore(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    item_id: typing.Any | None = 0,
):
    """Restore key map item

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param item_id: Item Identifier, Identifier of the item to restore
    :type item_id: typing.Any | None
    """

    ...

def keymap_restore(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    all: bool | typing.Any | None = False,
):
    """Restore key map(s)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All Keymaps, Restore all keymaps to default
    :type all: bool | typing.Any | None
    """

    ...

def reset_default_theme(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset to the default theme colors

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def script_directory_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    directory: str | typing.Any = "",
    filter_folder: bool | typing.Any | None = True,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param directory: directory
    :type directory: str | typing.Any
    :param filter_folder: Filter Folders
    :type filter_folder: bool | typing.Any | None
    """

    ...

def script_directory_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    index: typing.Any | None = 0,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: Index, Index of the script directory to remove
    :type index: typing.Any | None
    """

    ...

def studiolight_copy_settings(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    index: typing.Any | None = 0,
):
    """Copy Studio Light settings to the Studio Light editor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: index
    :type index: typing.Any | None
    """

    ...

def studiolight_install(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    directory: str | typing.Any = "",
    filter_folder: bool | typing.Any | None = True,
    filter_glob: str | typing.Any = "*.png;*.jpg;*.hdr;*.exr",
    type: str | None = "MATCAP",
):
    """Install a user defined light

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param files: File Path
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param directory: directory
        :type directory: str | typing.Any
        :param filter_folder: Filter Folders
        :type filter_folder: bool | typing.Any | None
        :param filter_glob: filter_glob
        :type filter_glob: str | typing.Any
        :param type: Type

    MATCAP
    MatCap -- Install custom MatCaps.

    WORLD
    World -- Install custom HDRIs.

    STUDIO
    Studio -- Install custom Studio Lights.
        :type type: str | None
    """

    ...

def studiolight_new(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filename: str | typing.Any = "StudioLight",
):
    """Save custom studio light from the studio light editor settings

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filename: Name
    :type filename: str | typing.Any
    """

    ...

def studiolight_show(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Show light preferences

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def studiolight_uninstall(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    index: typing.Any | None = 0,
):
    """Delete Studio Light

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: index
    :type index: typing.Any | None
    """

    ...

def theme_install(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    overwrite: bool | typing.Any | None = True,
    filepath: str | typing.Any = "",
    filter_folder: bool | typing.Any | None = True,
    filter_glob: str | typing.Any = "*.xml",
):
    """Load and apply a Blender XML theme file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param overwrite: Overwrite, Remove existing theme file if exists
    :type overwrite: bool | typing.Any | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    :param filter_folder: Filter folders
    :type filter_folder: bool | typing.Any | None
    :param filter_glob: filter_glob
    :type filter_glob: str | typing.Any
    """

    ...

def unassociate_blend(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove this installation's associations with .blend files

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...
