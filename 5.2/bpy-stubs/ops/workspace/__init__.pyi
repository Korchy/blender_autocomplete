import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a new workspace by duplicating the current one or appending one from the user configuration

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class append_activate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        idname: str = "",
        filepath: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Append a workspace and make it the active one in the current window

        :param execution_context:
        :param undo:
        :param idname: Identifier, Name of the workspace to append and activate (optional, never None)
        :param filepath: Filepath, Path to the library (optional, never None, blend relative // prefix supported)
        :return: Result of the operator call.
        """

class delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete the active workspace

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class delete_all_others(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete all workspaces except this one

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class duplicate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a new workspace

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class reorder_to_back(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reorder workspace to be last in the list

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class reorder_to_front(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reorder workspace to be first in the list

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class scene_pin_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remember the last used scene for the current workspace and switch to it whenever this workspace is activated again

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
