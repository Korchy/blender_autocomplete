import typing
import collections.abc
import typing_extensions

def autocomplete(execution_context: int | str | None = None, undo: bool | None = None):
    """Evaluate the namespace up until the cursor and give a list of options or complete the name if there is only one

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def banner(execution_context: int | str | None = None, undo: bool | None = None):
    """Print a message when the terminal initializes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    scrollback: bool | None = True,
    history: bool | None = False,
):
    """Clear text by type

    :type execution_context: int | str | None
    :type undo: bool | None
    :param scrollback: Scrollback, Clear the scrollback history
    :type scrollback: bool | None
    :param history: History, Clear the command history
    :type history: bool | None
    """

def clear_line(execution_context: int | str | None = None, undo: bool | None = None):
    """Clear the line and store in history

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delete: bool | None = False,
):
    """Copy selected text to clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    :param delete: Delete Selection, Whether to delete the selection after copying
    :type delete: bool | None
    """

def copy_as_script(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Copy the console contents for use in a script

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "NEXT_CHARACTER", "PREVIOUS_CHARACTER", "NEXT_WORD", "PREVIOUS_WORD"
    ]
    | None = "NEXT_CHARACTER",
):
    """Delete text by cursor position

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Which part of the text to delete
    :type type: typing.Literal['NEXT_CHARACTER','PREVIOUS_CHARACTER','NEXT_WORD','PREVIOUS_WORD'] | None
    """

def execute(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    interactive: bool | None = False,
):
    """Execute the current console line as a Python expression

    :type execution_context: int | str | None
    :type undo: bool | None
    :param interactive: interactive
    :type interactive: bool | None
    """

def history_append(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    text: str = "",
    current_character: int | None = 0,
    remove_duplicates: bool | None = False,
):
    """Append history at cursor position

    :type execution_context: int | str | None
    :type undo: bool | None
    :param text: Text, Text to insert at the cursor position
    :type text: str
    :param current_character: Cursor, The index of the cursor
    :type current_character: int | None
    :param remove_duplicates: Remove Duplicates, Remove duplicate items in the history
    :type remove_duplicates: bool | None
    """

def history_cycle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    reverse: bool | None = False,
):
    """Cycle through history

    :type execution_context: int | str | None
    :type undo: bool | None
    :param reverse: Reverse, Reverse cycle history
    :type reverse: bool | None
    """

def indent(execution_context: int | str | None = None, undo: bool | None = None):
    """Add 4 spaces at line beginning

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def indent_or_autocomplete(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Indent selected text or autocomplete

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def insert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    text: str = "",
):
    """Insert text at cursor position

    :type execution_context: int | str | None
    :type undo: bool | None
    :param text: Text, Text to insert at the cursor position
    :type text: str
    """

def language(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    language: str = "",
):
    """Set the current language for this console

    :type execution_context: int | str | None
    :type undo: bool | None
    :param language: Language
    :type language: str
    """

def move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "LINE_BEGIN",
        "LINE_END",
        "PREVIOUS_CHARACTER",
        "NEXT_CHARACTER",
        "PREVIOUS_WORD",
        "NEXT_WORD",
    ]
    | None = "LINE_BEGIN",
    select: bool | None = False,
):
    """Move cursor position

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Where to move cursor to
    :type type: typing.Literal['LINE_BEGIN','LINE_END','PREVIOUS_CHARACTER','NEXT_CHARACTER','PREVIOUS_WORD','NEXT_WORD'] | None
    :param select: Select, Whether to select while moving
    :type select: bool | None
    """

def paste(
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

def scrollback_append(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    text: str = "",
    type: typing.Literal["OUTPUT", "INPUT", "INFO", "ERROR"] | None = "OUTPUT",
):
    """Append scrollback text by type

    :type execution_context: int | str | None
    :type undo: bool | None
    :param text: Text, Text to insert at the cursor position
    :type text: str
    :param type: Type, Console output type
    :type type: typing.Literal['OUTPUT','INPUT','INFO','ERROR'] | None
    """

def select_all(execution_context: int | str | None = None, undo: bool | None = None):
    """Select all the text

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_set(execution_context: int | str | None = None, undo: bool | None = None):
    """Set the console selection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_word(execution_context: int | str | None = None, undo: bool | None = None):
    """Select word at cursor position

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def unindent(execution_context: int | str | None = None, undo: bool | None = None):
    """Delete 4 spaces from line beginning

    :type execution_context: int | str | None
    :type undo: bool | None
    """
