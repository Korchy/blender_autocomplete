import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def flush_edits(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Flush edit data from active editing modes"""

def lib_id_fake_user_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Save this data-block even if it has no users"""

def lib_id_generate_preview(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create an automatic preview for the selected data-block"""

def lib_id_generate_preview_from_object(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create a preview for this asset by rendering the active object"""

def lib_id_load_custom_preview(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = True,
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
    show_multiview: bool | None = False,
    use_multiview: bool | None = False,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
) -> None:
    """Choose an image to help identify the data-block visually

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
        :param show_multiview: Enable Multi-View
        :param use_multiview: Use Multi-View
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

def lib_id_override_editable_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set if this library override data-block can be edited"""

def lib_id_remove_preview(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the preview of this data-block"""

def lib_id_unlink(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove a usage of a data-block, clearing the assignment"""

def redo(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Redo previous action"""

def undo(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undo previous action"""

def undo_history(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    item: int | None = 0,
) -> None:
    """Redo specific action in history

    :param item: Item
    """

def undo_push(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    message: str = "Add an undo step *function may be moved*",
) -> None:
    """Add an undo state (internal use only)

    :param message: Undo Message
    """

def undo_redo(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undo and redo previous action"""
