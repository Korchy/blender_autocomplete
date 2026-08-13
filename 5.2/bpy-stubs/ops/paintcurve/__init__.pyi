import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class add_point(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        location: collections.abc.Sequence[int] | None = (0, 0),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add New Paint Curve Point

        :param execution_context:
        :param undo:
        :param location: Location, Location of vertex in area space (array of 2 items, in [0, 32767], optional)
        :return: Result of the operator call.
        """

class add_point_slide(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        PAINTCURVE_OT_add_point: dict[str, typing.Any] | None = {},
        PAINTCURVE_OT_slide: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add new curve point and slide it

        :param execution_context:
        :param undo:
        :param PAINTCURVE_OT_add_point: Add New Paint Curve Point, Add New Paint Curve Point (optional, `bpy.ops.paintcurve.add_point` keyword arguments)
        :param PAINTCURVE_OT_slide: Slide Paint Curve Point, Select and slide paint curve point (optional, `bpy.ops.paintcurve.slide` keyword arguments)
        :return: Result of the operator call.
        """

class cursor(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Place cursor

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class delete_point(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove Paint Curve Point

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class draw(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Draw curve

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
        """Add new paint curve

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        location: collections.abc.Sequence[int] | None = (0, 0),
        toggle: bool | None = False,
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select a paint curve point

        :param execution_context:
        :param undo:
        :param location: Location, Location of vertex in area space (array of 2 items, in [0, 32767], optional)
        :param toggle: Toggle, (De)select all (optional)
        :param extend: Extend, Extend selection (optional)
        :return: Result of the operator call.
        """

class slide(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        align: bool | None = False,
        select: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select and slide paint curve point

        :param execution_context:
        :param undo:
        :param align: Align Handles, Aligns opposite point handle during transform (optional)
        :param select: Select, Attempt to select a point handle before transform (optional)
        :return: Result of the operator call.
        """
