import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def assign_action(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set this pose Action as active Action on the active Object"""

def bundle_install(
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
) -> None:
    """Copy the current .blend file into an Asset Library. Only works on standalone .blend files (i.e. when no other files are referenced)

        :param asset_library_reference: asset_library_reference
        :param filepath: File Path, Path to file
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

def catalog_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    catalog_id: str = "",
) -> None:
    """Remove an asset catalog from the asset library (contained assets will not be affected and show up as unassigned)

    :param catalog_id: Catalog ID, ID of the catalog to delete
    """

def catalog_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    parent_path: str = "",
) -> None:
    """Create a new catalog to put assets in

    :param parent_path: Parent Path, Optional path defining the location to put the new catalog under
    """

def catalog_redo(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Redo the last undone edit to the asset catalogs"""

def catalog_undo(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undo the last edit to the asset catalogs"""

def catalog_undo_push(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Store the current state of the asset catalogs in the undo buffer"""

def catalogs_save(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Make any edits to any catalogs permanent by writing the current set up to the asset library"""

def clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    set_fake_user: bool | None = False,
) -> None:
    """Delete all asset metadata and turn the selected asset data-blocks back into normal data-blocks

    :param set_fake_user: Set Fake User, Ensure the data-block is saved, even when it is no longer marked as asset
    """

def clear_single(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    set_fake_user: bool | None = False,
) -> None:
    """Delete all asset metadata and turn the asset data-block back into a normal data-block

    :param set_fake_user: Set Fake User, Ensure the data-block is saved, even when it is no longer marked as asset
    """

def library_refresh(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reread assets and asset catalogs from the asset library on disk"""

def mark(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Enable easier reuse of selected data-blocks through the Asset Browser, with the help of customizable metadata (like previews, descriptions and tags)"""

def mark_single(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Enable easier reuse of a data-block through the Asset Browser, with the help of customizable metadata (like previews, descriptions and tags)"""

def open_containing_blend_file(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Open the blend file that contains the active asset"""

def screenshot_preview(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    p1: collections.abc.Iterable[int] | None = (0, 0),
    p2: collections.abc.Iterable[int] | None = (0, 0),
    force_square: bool | None = True,
) -> None:
    """Capture a screenshot to use as a preview for the selected asset

    :param p1: Point 1, First point of the screenshot in screenspace
    :param p2: Point 2, Second point of the screenshot in screenspace
    :param force_square: Force Square, If enabled, the screenshot will have the same height as width
    """

def tag_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a new keyword tag to the active asset"""

def tag_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove an existing keyword tag from the active asset"""
