import typing
import collections.abc
import typing_extensions

def flush_edits(execution_context: int | str | None = None, undo: bool | None = None):
    """Flush edit data from active editing modes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def lib_id_fake_user_toggle(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Save this data-block even if it has no users

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def lib_id_generate_preview(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Create an automatic preview for the selected data-block

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def lib_id_generate_preview_from_object(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Create a preview for this asset by rendering the active object

    :type execution_context: int | str | None
    :type undo: bool | None
    """

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
    filter_collada: bool | None = False,
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
):
    """Choose an image to help identify the data-block visually

        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
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
        :param show_multiview: Enable Multi-View
        :type show_multiview: bool | None
        :param use_multiview: Use Multi-View
        :type use_multiview: bool | None
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

def lib_id_override_editable_toggle(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Set if this library override data-block can be edited

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def lib_id_unlink(execution_context: int | str | None = None, undo: bool | None = None):
    """Remove a usage of a data-block, clearing the assignment

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def redo(execution_context: int | str | None = None, undo: bool | None = None):
    """Redo previous action

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def undo(execution_context: int | str | None = None, undo: bool | None = None):
    """Undo previous action

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def undo_history(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    item: int | None = 0,
):
    """Redo specific action in history

    :type execution_context: int | str | None
    :type undo: bool | None
    :param item: Item
    :type item: int | None
    """

def undo_push(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    message: str = "Add an undo step *function may be moved*",
):
    """Add an undo state (internal use only)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param message: Undo Message
    :type message: str
    """

def undo_redo(execution_context: int | str | None = None, undo: bool | None = None):
    """Undo and redo previous action

    :type execution_context: int | str | None
    :type undo: bool | None
    """
