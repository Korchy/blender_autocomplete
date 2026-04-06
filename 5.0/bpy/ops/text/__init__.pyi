import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def autocomplete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Show a list of used text in the open document"""

def comment_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["TOGGLE", "COMMENT", "UNCOMMENT"] | None = "TOGGLE",
) -> None:
    """Undocumented, consider contributing.

    :param type: Type, Add or remove comments
    """

def convert_whitespace(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["SPACES", "TABS"] | None = "SPACES",
) -> None:
    """Convert whitespaces by type

    :param type: Type, Type of whitespace to convert to
    """

def copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy selected text to clipboard"""

def cursor_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    x: int | None = 0,
    y: int | None = 0,
) -> None:
    """Set cursor position

    :param x: X
    :param y: Y
    """

def cut(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Cut selected text to clipboard"""

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "NEXT_CHARACTER", "PREVIOUS_CHARACTER", "NEXT_WORD", "PREVIOUS_WORD"
    ]
    | None = "NEXT_CHARACTER",
) -> None:
    """Delete text by cursor position

    :param type: Type, Which part of the text to delete
    """

def duplicate_line(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Duplicate the current line"""

def find(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Find specified text"""

def find_set_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Find specified text and set as selected"""

def indent(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Indent selected text"""

def indent_or_autocomplete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Indent selected text or autocomplete"""

def insert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    text: str = "",
) -> None:
    """Insert text at cursor position

    :param text: Text, Text to insert at the cursor position
    """

def jump(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    line: int | None = 1,
) -> None:
    """Jump cursor to line

    :param line: Line, Line number to jump to
    """

def jump_to_file_at_point(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    line: int | None = 0,
    column: int | None = 0,
) -> None:
    """Jump to a file for the text editor

    :param filepath: Filepath
    :param line: Line, Line to jump to
    :param column: Column, Column to jump to
    """

def line_break(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Insert line break at cursor position"""

def line_number(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """The current line number"""

def make_internal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Make active text file internal"""

def move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "LINE_BEGIN",
        "LINE_END",
        "FILE_TOP",
        "FILE_BOTTOM",
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

def move_lines(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "DOWN",
) -> None:
    """Move the currently selected line(s) up/down

    :param direction: Direction
    """

def move_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "LINE_BEGIN",
        "LINE_END",
        "FILE_TOP",
        "FILE_BOTTOM",
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

def new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create a new text data-block"""

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
    filter_python: bool | None = True,
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
    relative_path: bool | None = True,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: typing.Literal[
        "DEFAULT",
        "FILE_SORT_ALPHA",
        "FILE_SORT_EXTENSION",
        "FILE_SORT_TIME",
        "FILE_SORT_SIZE",
        "ASSET_CATALOG",
    ]
    | None = "",
    internal: bool | None = False,
) -> None:
    """Open a new text data-block

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

    DEFAULT
    Default -- Automatically determine sort method for files.

    FILE_SORT_ALPHA
    Name -- Sort the file list alphabetically.

    FILE_SORT_EXTENSION
    Extension -- Sort the file list by extension/type.

    FILE_SORT_TIME
    Modified Date -- Sort files by modification time.

    FILE_SORT_SIZE
    Size -- Sort files by size.

    ASSET_CATALOG
    Asset Catalog -- Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..
        :param internal: Make Internal, Make text file internal after loading
    """

def overwrite_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle overwrite while typing"""

def paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    selection: bool | None = False,
) -> None:
    """Paste text from clipboard

    :param selection: Selection, Paste text selected elsewhere rather than copied (X11/Wayland only)
    """

def reload(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reload active text data-block from its file"""

def replace(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
) -> None:
    """Replace text with the specified text

    :param all: Replace All, Replace all occurrences
    """

def replace_set_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Replace text with specified text and set as selected"""

def resolve_conflict(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    resolution: typing.Literal["IGNORE", "RELOAD", "SAVE", "MAKE_INTERNAL"]
    | None = "IGNORE",
) -> None:
    """When external text is out of sync, resolve the conflict

    :param resolution: Resolution, How to solve conflict due to differences in internal and external text
    """

def run_script(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Run active script"""

def save(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Save active text data-block"""

def save_as(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = True,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = False,
    filter_movie: bool | None = False,
    filter_python: bool | None = True,
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
    """Save active text file with options

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

def scroll(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    lines: int | None = 1,
) -> None:
    """Undocumented, consider contributing.

    :param lines: Lines, Number of lines to scroll
    """

def scroll_bar(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    lines: int | None = 1,
) -> None:
    """Undocumented, consider contributing.

    :param lines: Lines, Number of lines to scroll
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all text"""

def select_line(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select text by line"""

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
    """Set text selection"""

def start_find(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Start searching text"""

def to_3d_object(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    split_lines: bool | None = False,
) -> None:
    """Create 3D text object from active text data-block

    :param split_lines: Split Lines, Create one object per line in the text
    """

def unindent(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Unindent selected text"""

def unlink(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Unlink active text data-block"""

def update_shader(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Update users of this shader, such as custom cameras and script nodes, with its new sockets and options"""
