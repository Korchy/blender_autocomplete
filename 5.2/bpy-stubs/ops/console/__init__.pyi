import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class autocomplete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Evaluate the namespace up until the cursor and give a list of options or complete the name if there is only one

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class banner(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Print a message when the terminal initializes

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
        scrollback: bool | None = True,
        history: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear text by type

        :param execution_context:
        :param undo:
        :param scrollback: Scrollback, Clear the scrollback history (optional)
        :param history: History, Clear the command history (optional)
        :return: Result of the operator call.
        """

class clear_line(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear the line and store in history

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        delete: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy selected text to clipboard

        :param execution_context:
        :param undo:
        :param delete: Delete Selection, Whether to delete the selection after copying (optional)
        :return: Result of the operator call.
        """

class copy_as_script(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy the console contents for use in a script

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            "NEXT_CHARACTER", "PREVIOUS_CHARACTER", "NEXT_WORD", "PREVIOUS_WORD"
        ]
        | None = "NEXT_CHARACTER",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete text by cursor position

        :param execution_context:
        :param undo:
        :param type: Type, Which part of the text to delete (optional)
        :return: Result of the operator call.
        """

class execute(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        interactive: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Execute the current console line as a Python expression

        :param execution_context:
        :param undo:
        :param interactive: interactive, (optional)
        :return: Result of the operator call.
        """

class history_append(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        text: str = "",
        current_character: int | None = 0,
        remove_duplicates: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Append history at cursor position

        :param execution_context:
        :param undo:
        :param text: Text, Text to insert at the cursor position (optional, never None)
        :param current_character: Cursor, The index of the cursor (in [0, inf], optional)
        :param remove_duplicates: Remove Duplicates, Remove duplicate items in the history (optional)
        :return: Result of the operator call.
        """

class history_cycle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        reverse: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Cycle through history

        :param execution_context:
        :param undo:
        :param reverse: Reverse, Reverse cycle history (optional)
        :return: Result of the operator call.
        """

class indent(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add 4 spaces at line beginning

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class indent_or_autocomplete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Indent selected text or autocomplete

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class insert(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        text: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Insert text at cursor position

        :param execution_context:
        :param undo:
        :param text: Text, Text to insert at the cursor position (optional, never None)
        :return: Result of the operator call.
        """

class language(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        language: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the current language for this console

        :param execution_context:
        :param undo:
        :param language: Language, (optional, never None)
        :return: Result of the operator call.
        """

class move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move cursor position

        :param execution_context:
        :param undo:
        :param type: Type, Where to move cursor to (optional)
        :param select: Select, Whether to select while moving (optional)
        :return: Result of the operator call.
        """

class paste(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        selection: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Paste text from clipboard

        :param execution_context:
        :param undo:
        :param selection: Selection, Paste text selected elsewhere rather than copied (X11/Wayland only) (optional)
        :return: Result of the operator call.
        """

class scrollback_append(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        text: str = "",
        type: typing.Literal["OUTPUT", "INPUT", "INFO", "ERROR"] | None = "OUTPUT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Append scrollback text by type

        :param execution_context:
        :param undo:
        :param text: Text, Text to insert at the cursor position (optional, never None)
        :param type: Type, Console output type (optional)
        :return: Result of the operator call.
        """

class select_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all the text

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the console selection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_word(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select word at cursor position

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class unindent(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete 4 spaces from line beginning

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
