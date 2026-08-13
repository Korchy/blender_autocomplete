import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class asset_download(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        asset_library_type: typing.Literal[
            bpy.stub_internal.rna_enums.AssetLibraryTypeItems
        ]
        | None = "LOCAL",
        asset_library_identifier: str = "",
        relative_asset_identifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make the asset available without internet access

        :param execution_context:
        :param undo:
        :param asset_library_type: Asset Library Type, (optional)
        :param asset_library_identifier: Asset Library Identifier, (optional, never None)
        :param relative_asset_identifier: Relative Asset Identifier, (optional, never None)
        :return: Result of the operator call.
        """

class assets_download(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Download the selected asset(s)

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class assign_action(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set this pose Action as active Action on the active Object

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class browse_containing_blend_file(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open the systems file browser with the blend file that contains the active asset

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class bundle_install(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        asset_library_reference: str | None = "",
        filepath: str = "",
        hide_props_region: bool | None = True,
        check_existing: bool | None = True,
        filter_blender: bool | None = True,
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
        filemode: int | None = 8,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy the current .blend file into an Asset Library. Only works on standalone .blend files (i.e. when no other files are referenced)

                :param execution_context:
                :param undo:
                :param asset_library_reference: asset_library_reference, (optional)
                :param filepath: File Path, Path to file (optional, never None)
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
                :return: Result of the operator call.
        """

class catalog_delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        catalog_id: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove an asset catalog from the asset library (contained assets will not be affected and show up as unassigned)

        :param execution_context:
        :param undo:
        :param catalog_id: Catalog ID, ID of the catalog to delete (optional, never None)
        :return: Result of the operator call.
        """

class catalog_new(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        parent_path: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a new catalog to put assets in

        :param execution_context:
        :param undo:
        :param parent_path: Parent Path, Optional path defining the location to put the new catalog under (optional, never None)
        :return: Result of the operator call.
        """

class catalog_redo(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Redo the last undone edit to the asset catalogs

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class catalog_undo(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undo the last edit to the asset catalogs

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class catalog_undo_push(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Store the current state of the asset catalogs in the undo buffer

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class catalogs_save(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make any edits to any catalogs permanent by writing the current set up to the asset library

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        set_fake_user: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete all asset metadata and turn the selected asset data-blocks back into normal data-blocks

        :param execution_context:
        :param undo:
        :param set_fake_user: Set Fake User, Ensure the data-block is saved, even when it is no longer marked as asset (optional)
        :return: Result of the operator call.
        """

class clear_single(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        set_fake_user: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete all asset metadata and turn the asset data-block back into a normal data-block

        :param execution_context:
        :param undo:
        :param set_fake_user: Set Fake User, Ensure the data-block is saved, even when it is no longer marked as asset (optional)
        :return: Result of the operator call.
        """

class library_refresh(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_remote_listing: bool | None = False,
        use_shift_for_remote_listing: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reread assets and asset catalogs from the asset library on disk

        :param execution_context:
        :param undo:
        :param use_remote_listing: Remote Listing, Re-download the asset listing of a remote library. Only supported when the active asset library is remote or has a remote component (the Essentials library) (optional)
        :param use_shift_for_remote_listing: Use Shift for Remote Listing, When this operator is invoked and the Shift key is pressed, download the remote asset library listing (optional)
        :return: Result of the operator call.
        """

class library_reload_listing(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Re-download the asset listing of a remote library. Only supported when the active asset library is remote or has a remote component (the Essentials library)

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class mark(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Enable easier reuse of selected data-blocks through the Asset Browser, with the help of customizable metadata (like previews, descriptions and tags)

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class mark_single(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Enable easier reuse of a data-block through the Asset Browser, with the help of customizable metadata (like previews, descriptions and tags)

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class open_containing_blend_file(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open the blend file that contains the active asset

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class screenshot_preview(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        p1: collections.abc.Sequence[int] | None = (0, 0),
        p2: collections.abc.Sequence[int] | None = (0, 0),
        force_square: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Capture a screenshot to use as a preview for the selected asset

        :param execution_context:
        :param undo:
        :param p1: Point 1, First point of the screenshot in screenspace (array of 2 items, in [0, inf], optional)
        :param p2: Point 2, Second point of the screenshot in screenspace (array of 2 items, in [0, inf], optional)
        :param force_square: Force Square, If enabled, the screenshot will have the same height as width (optional)
        :return: Result of the operator call.
        """

class tag_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a new keyword tag to the active asset

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class tag_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove an existing keyword tag from the active asset

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
