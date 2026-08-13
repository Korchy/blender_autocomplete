import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class convert_volume_to_mesh(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Convert the volume of a world to a mesh. The worlds volume used to be rendered by EEVEE Legacy. Conversion is needed for it to render properly

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class new(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a new world Data-Block

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
