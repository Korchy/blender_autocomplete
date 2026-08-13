import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class entry_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        list_path: str = "",
        active_index_path: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add an entry to the list after the current active item

        :param execution_context:
        :param undo:
        :param list_path: list_path, (optional, never None)
        :param active_index_path: active_index_path, (optional, never None)
        :return: Result of the operator call.
        """

class entry_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        list_path: str = "",
        active_index_path: str = "",
        direction: typing.Literal["UP", "DOWN"] | None = "UP",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move an entry in the list up or down

                :param execution_context:
                :param undo:
                :param list_path: list_path, (optional, never None)
                :param active_index_path: active_index_path, (optional, never None)
                :param direction: Direction, (optional)

        UP
        Up -- Move the active entry up.

        DOWN
        Down -- Move the active entry down.
                :return: Result of the operator call.
        """

class entry_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        list_path: str = "",
        active_index_path: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the selected entry from the list

        :param execution_context:
        :param undo:
        :param list_path: list_path, (optional, never None)
        :param active_index_path: active_index_path, (optional, never None)
        :return: Result of the operator call.
        """
