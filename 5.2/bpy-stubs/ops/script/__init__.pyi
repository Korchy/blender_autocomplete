import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class execute_preset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        menu_idname: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Load a preset

        :param execution_context:
        :param undo:
        :param filepath: filepath, (optional, never None)
        :param menu_idname: Menu ID Name, ID name of the menu this was called from (optional, never None)
        :return: Result of the operator call.
        """

class python_file_run(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Run Python file

        :param execution_context:
        :param undo:
        :param filepath: Path, (optional, never None)
        :return: Result of the operator call.
        """

class reload(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reload scripts

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
