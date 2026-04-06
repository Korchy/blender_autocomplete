import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def autocomplete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Evaluate the namespace up until the cursor and give a list of options or complete the name if there is only one"""

def banner(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Print a message when the terminal initializes"""

def clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    scrollback: bool | None = True,
    history: bool | None = False,
) -> None:
    """Clear text by type

    :param scrollback: Scrollback, Clear the scrollback history
    :param history: History, Clear the command history
    """

def clear_line(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear the line and store in history"""

def copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delete: bool | None = False,
) -> None:
    """Copy selected text to clipboard

    :param delete: Delete Selection, Whether to delete the selection after copying
    """

def copy_as_script(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the console contents for use in a script"""

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

def execute(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    interactive: bool | None = False,
) -> None:
    """Execute the current console line as a Python expression

    :param interactive: interactive
    """

def history_append(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    text: str = "",
    current_character: int | None = 0,
    remove_duplicates: bool | None = False,
) -> None:
    """Append history at cursor position

    :param text: Text, Text to insert at the cursor position
    :param current_character: Cursor, The index of the cursor
    :param remove_duplicates: Remove Duplicates, Remove duplicate items in the history
    """

def history_cycle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    reverse: bool | None = False,
) -> None:
    """Cycle through history

    :param reverse: Reverse, Reverse cycle history
    """

def indent(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add 4 spaces at line beginning"""

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

def language(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    language: str = "",
) -> None:
    """Set the current language for this console

    :param language: Language
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
) -> None:
    """Move cursor position

    :param type: Type, Where to move cursor to
    :param select: Select, Whether to select while moving
    """

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

def scrollback_append(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    text: str = "",
    type: typing.Literal["OUTPUT", "INPUT", "INFO", "ERROR"] | None = "OUTPUT",
) -> None:
    """Append scrollback text by type

    :param text: Text, Text to insert at the cursor position
    :param type: Type, Console output type
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all the text"""

def select_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set the console selection"""

def select_word(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select word at cursor position"""

def unindent(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete 4 spaces from line beginning"""
