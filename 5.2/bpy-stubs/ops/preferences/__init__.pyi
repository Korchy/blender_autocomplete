import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums
import bpy.types

class addon_disable(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        module: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Turn off this add-on

        :param execution_context:
        :param undo:
        :param module: Module, Module name of the add-on to disable (optional, never None)
        :return: Result of the operator call.
        """

class addon_enable(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        module: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Turn on this add-on

        :param execution_context:
        :param undo:
        :param module: Module, Module name of the add-on to enable (optional, never None)
        :return: Result of the operator call.
        """

class addon_expand(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        module: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Display information and preferences for this add-on

        :param execution_context:
        :param undo:
        :param module: Module, Module name of the add-on to expand (optional, never None)
        :return: Result of the operator call.
        """

class addon_install(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Install an add-on

        :param execution_context:
        :param undo:
        :param overwrite: Overwrite, Remove existing add-ons with the same ID (optional)
        :param enable_on_install: Enable on Install, Enable after installing (optional)
        :param target: Target Path, (optional)
        :param filepath: filepath, (optional, never None)
        :param filter_folder: Filter folders, (optional)
        :param filter_python: Filter Python, (optional)
        :param filter_glob: filter_glob, (optional, never None)
        :return: Result of the operator call.
        """

class addon_refresh(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Scan add-on directories for new modules

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class addon_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        module: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete the add-on from the file system

        :param execution_context:
        :param undo:
        :param module: Module, Module name of the add-on to remove (optional, never None)
        :return: Result of the operator call.
        """

class addon_show(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        module: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Show add-on preferences

        :param execution_context:
        :param undo:
        :param module: Module, Module name of the add-on to expand (optional, never None)
        :return: Result of the operator call.
        """

class app_template_install(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        overwrite: bool | None = True,
        filepath: str = "",
        filter_folder: bool | None = True,
        filter_glob: str = "*.zip",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Install an application template

        :param execution_context:
        :param undo:
        :param overwrite: Overwrite, Remove existing template with the same ID (optional)
        :param filepath: filepath, (optional, never None)
        :param filter_folder: Filter folders, (optional)
        :param filter_glob: filter_glob, (optional, never None)
        :return: Result of the operator call.
        """

class asset_library_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        name: str = "",
        remote_url: str = "",
        type: typing.Literal["REMOTE", "LOCAL"] | None = "LOCAL",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a directory to be used by the Asset Browser as source of assets

                :param execution_context:
                :param undo:
                :param directory: Directory, Directory of the file (optional, never None)
                :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
                :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
                :param filter_blender: Filter .blend files, (optional)
                :param filter_backup: Filter backup .blend files, (optional)
                :param filter_image: Filter image files, (optional)
                :param filter_movie: Filter movie files, (optional)
                :param filter_python: Filter Python files, (optional)
                :param filter_font: Filter font files, (optional)
                :param filter_sound: Filter sound files, (optional)
                :param filter_text: Filter text files, (optional)
                :param filter_archive: Filter archive files, (optional)
                :param filter_btx: Filter btx files, (optional)
                :param filter_alembic: Filter Alembic files, (optional)
                :param filter_usd: Filter USD files, (optional)
                :param filter_obj: Filter OBJ files, (optional)
                :param filter_volume: Filter OpenVDB volume files, (optional)
                :param filter_folder: Filter folders, (optional)
                :param filter_blenlib: Filter Blender IDs, (optional)
                :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
                :param display_type: Display Type, (optional)

        DEFAULT
        Default -- Automatically determine display type for files.

        LIST_VERTICAL
        Short List -- Display files as short list.

        LIST_HORIZONTAL
        Long List -- Display files as a detailed list.

        THUMBNAIL
        Thumbnails -- Display files as thumbnails.
                :param sort_method: File sorting mode, (optional)
                :param name: Name, Identifier (not necessarily unique) for the asset library (optional, never None)
                :param remote_url: URL, Remote URL to the asset library (optional, never None)
                :param type: Type, The kind of asset library to add (optional)

        REMOTE
        Add Remote Asset Library -- Add an asset library referencing a remote repository with support for listing and updating asset libraries.

        LOCAL
        Add Local Asset Library -- Add an asset library managed via the file system without referencing an external repository.
                :return: Result of the operator call.
        """

class asset_library_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        index: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove a path to a .blend file, so the Asset Browser will not attempt to show it anymore

        :param execution_context:
        :param undo:
        :param index: Index, (in [0, inf], optional)
        :return: Result of the operator call.
        """

class associate_blend(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Use this installation for .blend files and to display thumbnails

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class autoexec_path_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add path to exclude from auto-execution

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class autoexec_path_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        index: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove path to exclude from auto-execution

        :param execution_context:
        :param undo:
        :param index: Index, (in [0, inf], optional)
        :return: Result of the operator call.
        """

class clear_filter(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear the search filter

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class copy_prev(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy settings from previous version

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class extension_repo_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a new repository used to store extensions

                :param execution_context:
                :param undo:
                :param name: Name, Unique repository name (optional, never None)
                :param remote_url: URL, Remote URL to the extension repository, the file-system may be referenced using the file URI scheme: "file://" (optional, never None)
                :param use_access_token: Requires Access Token, Repository requires an access token (optional)
                :param access_token: Secret, Personal access token, may be required by some repositories (optional, never None)
                :param use_sync_on_startup: Check for Updates on Startup, Allow Blender to check for updates upon launch (optional)
                :param use_custom_directory: Custom Directory, Manually set the path for extensions to be stored. When disabled a users extensions directory is created. (optional)
                :param custom_directory: Custom Directory, The local directory containing extensions (optional, never None)
                :param type: Type, The kind of repository to add (optional)

        REMOTE
        Add Remote Repository -- Add a repository referencing a remote repository with support for listing and updating extensions.

        LOCAL
        Add Local Repository -- Add a repository managed manually without referencing an external repository.
                :return: Result of the operator call.
        """

class extension_repo_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        index: int | None = 0,
        remove_files: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove an extension repository

        :param execution_context:
        :param undo:
        :param index: Index, (in [0, inf], optional)
        :param remove_files: Remove Files, Remove extension files when removing the repository (optional)
        :return: Result of the operator call.
        """

class extension_url_drop(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        url: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Handle dropping an extension URL

        :param execution_context:
        :param undo:
        :param url: URL, Location of the extension to install (optional, never None)
        :return: Result of the operator call.
        """

class keyconfig_activate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param filepath: filepath, (optional, never None)
        :return: Result of the operator call.
        """

class keyconfig_export(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        all: bool | None = False,
        filepath: str = "",
        filter_folder: bool | None = True,
        filter_text: bool | None = True,
        filter_python: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Export key configuration to a Python script

        :param execution_context:
        :param undo:
        :param all: All Keymaps, Write all keymaps (not just user modified) (optional)
        :param filepath: filepath, (optional, never None)
        :param filter_folder: Filter folders, (optional)
        :param filter_text: Filter text, (optional)
        :param filter_python: Filter Python, (optional)
        :return: Result of the operator call.
        """

class keyconfig_import(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "keymap.py",
        filter_folder: bool | None = True,
        filter_text: bool | None = True,
        filter_python: bool | None = True,
        keep_original: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Import key configuration from a Python script

        :param execution_context:
        :param undo:
        :param filepath: filepath, (optional, never None)
        :param filter_folder: Filter folders, (optional)
        :param filter_text: Filter text, (optional)
        :param filter_python: Filter Python, (optional)
        :param keep_original: Keep Original, Keep original file after copying to configuration folder (optional)
        :return: Result of the operator call.
        """

class keyconfig_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove key config

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class keyconfig_test(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Test key configuration for conflicts

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class keyitem_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add key map item

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class keyitem_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        item_id: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove key map item

        :param execution_context:
        :param undo:
        :param item_id: Item Identifier, Identifier of the item to remove (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class keyitem_restore(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        item_id: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Restore key map item

        :param execution_context:
        :param undo:
        :param item_id: Item Identifier, Identifier of the item to restore (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class keymap_restore(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        all: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Restore key map(s)

        :param execution_context:
        :param undo:
        :param all: All Keymaps, Restore all keymaps to default (optional)
        :return: Result of the operator call.
        """

class reset_default_theme(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset to the default theme colors

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class script_directory_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        directory: str = "",
        filter_folder: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param directory: directory, (optional, never None)
        :param filter_folder: Filter Folders, (optional)
        :return: Result of the operator call.
        """

class script_directory_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        index: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param index: Index, Index of the script directory to remove (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class start_filter(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Start entering filter text

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class studiolight_copy_settings(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        index: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy Studio Light settings to the Studio Light editor

        :param execution_context:
        :param undo:
        :param index: index, (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class studiolight_install(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        files: None
        | bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
        | None = None,
        directory: str = "",
        filter_folder: bool | None = True,
        filter_glob: str = "*.png;*.jpg;*.hdr;*.exr",
        type: typing.Literal["MATCAP", "WORLD", "STUDIO"] | None = "MATCAP",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Install a user defined light

                :param execution_context:
                :param undo:
                :param files: File Path, (optional)
                :param directory: directory, (optional, never None)
                :param filter_folder: Filter Folders, (optional)
                :param filter_glob: filter_glob, (optional, never None)
                :param type: Type, (optional)

        MATCAP
        MatCap -- Install custom MatCaps.

        WORLD
        World -- Install custom HDRIs.

        STUDIO
        Studio -- Install custom Studio Lights.
                :return: Result of the operator call.
        """

class studiolight_new(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filename: str = "StudioLight",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Save custom studio light from the studio light editor settings

        :param execution_context:
        :param undo:
        :param filename: Name, (optional, never None)
        :return: Result of the operator call.
        """

class studiolight_uninstall(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        index: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete Studio Light

        :param execution_context:
        :param undo:
        :param index: index, (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class theme_install(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        overwrite: bool | None = True,
        filepath: str = "",
        filter_folder: bool | None = True,
        filter_glob: str = "*.xml",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Load and apply a Blender XML theme file

        :param execution_context:
        :param undo:
        :param overwrite: Overwrite, Remove existing theme file if exists (optional)
        :param filepath: filepath, (optional, never None)
        :param filter_folder: Filter folders, (optional)
        :param filter_glob: filter_glob, (optional, never None)
        :return: Result of the operator call.
        """

class unassociate_blend(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove this installations associations with .blend files

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
