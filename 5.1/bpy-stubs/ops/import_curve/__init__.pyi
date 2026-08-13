import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums
import bpy.types

class svg(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        filter_glob: str = "*.svg",
        directory: str = "",
        files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
        | None = None,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Load a SVG file

        :param execution_context:
        :param undo:
        :param filepath: File Path, Filepath used for importing the file (optional, never None)
        :param filter_glob: filter_glob, (optional, never None)
        :param directory: directory, (optional, never None)
        :param files: File Path, (optional)
        :return: Result of the operator call.
        """
