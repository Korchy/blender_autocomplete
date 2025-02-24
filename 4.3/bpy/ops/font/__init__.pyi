import typing
import collections.abc
import typing_extensions

def case_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    case: typing.Literal["LOWER", "UPPER"] | None = "LOWER",
):
    """Set font case

    :type execution_context: int | str | None
    :type undo: bool | None
    :param case: Case, Lower or upper case
    :type case: typing.Literal['LOWER','UPPER'] | None
    """

def case_toggle(execution_context: int | str | None = None, undo: bool | None = None):
    """Toggle font case

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def change_character(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delta: int | None = 1,
):
    """Change font character code

    :type execution_context: int | str | None
    :type undo: bool | None
    :param delta: Delta, Number to increase or decrease character code with
    :type delta: int | None
    """

def change_spacing(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delta: float | None = 1.0,
):
    """Change font spacing

    :type execution_context: int | str | None
    :type undo: bool | None
    :param delta: Delta, Amount to decrease or increase character spacing with
    :type delta: float | None
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "NEXT_CHARACTER",
        "PREVIOUS_CHARACTER",
        "NEXT_WORD",
        "PREVIOUS_WORD",
        "SELECTION",
        "NEXT_OR_SELECTION",
        "PREVIOUS_OR_SELECTION",
    ]
    | None = "PREVIOUS_CHARACTER",
):
    """Delete text by cursor position

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Which part of the text to delete
    :type type: typing.Literal['NEXT_CHARACTER','PREVIOUS_CHARACTER','NEXT_WORD','PREVIOUS_WORD','SELECTION','NEXT_OR_SELECTION','PREVIOUS_OR_SELECTION'] | None
    """

def line_break(execution_context: int | str | None = None, undo: bool | None = None):
    """Insert line break at cursor position

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "LINE_BEGIN",
        "LINE_END",
        "TEXT_BEGIN",
        "TEXT_END",
        "PREVIOUS_CHARACTER",
        "NEXT_CHARACTER",
        "PREVIOUS_WORD",
        "NEXT_WORD",
        "PREVIOUS_LINE",
        "NEXT_LINE",
        "PREVIOUS_PAGE",
        "NEXT_PAGE",
    ]
    | None = "LINE_BEGIN",
):
    """Move cursor to position type

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Where to move cursor to
    :type type: typing.Literal['LINE_BEGIN','LINE_END','TEXT_BEGIN','TEXT_END','PREVIOUS_CHARACTER','NEXT_CHARACTER','PREVIOUS_WORD','NEXT_WORD','PREVIOUS_LINE','NEXT_LINE','PREVIOUS_PAGE','NEXT_PAGE'] | None
    """

def move_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "LINE_BEGIN",
        "LINE_END",
        "TEXT_BEGIN",
        "TEXT_END",
        "PREVIOUS_CHARACTER",
        "NEXT_CHARACTER",
        "PREVIOUS_WORD",
        "NEXT_WORD",
        "PREVIOUS_LINE",
        "NEXT_LINE",
        "PREVIOUS_PAGE",
        "NEXT_PAGE",
    ]
    | None = "LINE_BEGIN",
):
    """Move the cursor while selecting

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Where to move cursor to, to make a selection
    :type type: typing.Literal['LINE_BEGIN','LINE_END','TEXT_BEGIN','TEXT_END','PREVIOUS_CHARACTER','NEXT_CHARACTER','PREVIOUS_WORD','NEXT_WORD','PREVIOUS_LINE','NEXT_LINE','PREVIOUS_PAGE','NEXT_PAGE'] | None
    """

def open(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = False,
    filter_movie: bool | None = False,
    filter_python: bool | None = False,
    filter_font: bool | None = True,
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
    relative_path: bool | None = True,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "THUMBNAIL",
    sort_method: str | None = "",
):
    """Load a new font from a file

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
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | None
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

def select_all(execution_context: int | str | None = None, undo: bool | None = None):
    """Select all text

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_word(execution_context: int | str | None = None, undo: bool | None = None):
    """Select word under cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def selection_set(execution_context: int | str | None = None, undo: bool | None = None):
    """Set cursor selection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def style_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    style: typing.Literal["BOLD", "ITALIC", "UNDERLINE", "SMALL_CAPS"] | None = "BOLD",
    clear: bool | None = False,
):
    """Set font style

    :type execution_context: int | str | None
    :type undo: bool | None
    :param style: Style, Style to set selection to
    :type style: typing.Literal['BOLD','ITALIC','UNDERLINE','SMALL_CAPS'] | None
    :param clear: Clear, Clear style rather than setting it
    :type clear: bool | None
    """

def style_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    style: typing.Literal["BOLD", "ITALIC", "UNDERLINE", "SMALL_CAPS"] | None = "BOLD",
):
    """Toggle font style

    :type execution_context: int | str | None
    :type undo: bool | None
    :param style: Style, Style to set selection to
    :type style: typing.Literal['BOLD','ITALIC','UNDERLINE','SMALL_CAPS'] | None
    """

def text_copy(execution_context: int | str | None = None, undo: bool | None = None):
    """Copy selected text to clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def text_cut(execution_context: int | str | None = None, undo: bool | None = None):
    """Cut selected text to clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def text_insert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    text: str = "",
    accent: bool | None = False,
):
    """Insert text at cursor position

    :type execution_context: int | str | None
    :type undo: bool | None
    :param text: Text, Text to insert at the cursor position
    :type text: str
    :param accent: Accent Mode, Next typed character will strike through previous, for special character input
    :type accent: bool | None
    """

def text_insert_unicode(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Insert Unicode Character

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def text_paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    selection: bool | None = False,
):
    """Paste text from clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    :param selection: Selection, Paste text selected elsewhere rather than copied (X11/Wayland only)
    :type selection: bool | None
    """

def text_paste_from_file(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = False,
    filter_movie: bool | None = False,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = True,
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
    """Paste contents from file

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

def textbox_add(execution_context: int | str | None = None, undo: bool | None = None):
    """Add a new text box

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def textbox_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
):
    """Remove the text box

    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: Index, The current text box
    :type index: int | None
    """

def unlink(execution_context: int | str | None = None, undo: bool | None = None):
    """Unlink active font data-block

    :type execution_context: int | str | None
    :type undo: bool | None
    """
