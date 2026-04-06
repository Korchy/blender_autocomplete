import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def case_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    case: typing.Literal["LOWER", "UPPER"] | None = "LOWER",
) -> None:
    """Set font case

    :param case: Case, Lower or upper case
    """

def case_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle font case"""

def change_character(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delta: int | None = 1,
) -> None:
    """Change font character code

    :param delta: Delta, Number to increase or decrease character code with
    """

def change_spacing(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delta: float | None = 1.0,
) -> None:
    """Change font spacing

    :param delta: Delta, Amount to decrease or increase character spacing with
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
) -> None:
    """Delete text by cursor position

    :param type: Type, Which part of the text to delete
    """

def line_break(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Insert line break at cursor position"""

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
) -> None:
    """Move cursor to position type

    :param type: Type, Where to move cursor to
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
) -> None:
    """Move the cursor while selecting

    :param type: Type, Where to move cursor to, to make a selection
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
) -> None:
    """Load a new font from a file

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
        :param relative_path: Relative Path, Select the file relative to the blend file
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

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all text"""

def select_word(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select word under cursor"""

def selection_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set cursor selection"""

def style_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    style: typing.Literal["BOLD", "ITALIC", "UNDERLINE", "SMALL_CAPS"] | None = "BOLD",
    clear: bool | None = False,
) -> None:
    """Set font style

    :param style: Style, Style to set selection to
    :param clear: Clear, Clear style rather than setting it
    """

def style_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    style: typing.Literal["BOLD", "ITALIC", "UNDERLINE", "SMALL_CAPS"] | None = "BOLD",
) -> None:
    """Toggle font style

    :param style: Style, Style to set selection to
    """

def text_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy selected text to clipboard"""

def text_cut(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Cut selected text to clipboard"""

def text_insert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    text: str = "",
    accent: bool | None = False,
) -> None:
    """Insert text at cursor position

    :param text: Text, Text to insert at the cursor position
    :param accent: Accent Mode, Next typed character will strike through previous, for special character input
    """

def text_insert_unicode(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Insert Unicode Character"""

def text_paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    selection: bool | None = False,
) -> None:
    """Paste text from clipboard

    :param selection: Selection, Paste text selected elsewhere rather than copied (X11/Wayland only)
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
    """Paste contents from file

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

def textbox_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a new text box"""

def textbox_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
) -> None:
    """Remove the text box

    :param index: Index, The current text box
    """

def unlink(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Unlink active font data-block"""
