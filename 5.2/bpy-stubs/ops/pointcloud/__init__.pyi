import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class attribute_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        value_float: float | None = 0.0,
        value_float_vector_2d: collections.abc.Sequence[float] | None = (0.0, 0.0),
        value_float_vector_3d: collections.abc.Sequence[float] | None = (0.0, 0.0, 0.0),
        value_float_vector_4d: collections.abc.Sequence[float] | None = (
            0.0,
            0.0,
            0.0,
            0.0,
        ),
        value_int: int | None = 0,
        value_int_vector_2d: collections.abc.Sequence[int] | None = (0, 0),
        value_color: collections.abc.Sequence[float] | None = (1.0, 1.0, 1.0, 1.0),
        value_bool: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set values of the active attribute for selected elements

        :param execution_context:
        :param undo:
        :param value_float: Value, (in [-inf, inf], optional)
        :param value_float_vector_2d: Value, (array of 2 items, in [-inf, inf], optional)
        :param value_float_vector_3d: Value, (array of 3 items, in [-inf, inf], optional)
        :param value_float_vector_4d: Value, (array of 4 items, in [-inf, inf], optional)
        :param value_int: Value, (in [-inf, inf], optional)
        :param value_int_vector_2d: Value, (array of 2 items, in [-inf, inf], optional)
        :param value_color: Value, (array of 4 items, in [-inf, inf], optional)
        :param value_bool: Value, (optional)
        :return: Result of the operator call.
        """

class delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove selected points

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
        """Copy selected points

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class duplicate_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        POINTCLOUD_OT_duplicate: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make copies of selected elements and move them

        :param execution_context:
        :param undo:
        :param POINTCLOUD_OT_duplicate: Duplicate, Copy selected points (optional, `bpy.ops.pointcloud.duplicate` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class select_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"]
        | None = "TOGGLE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """(De)select all points

                :param execution_context:
                :param undo:
                :param action: Action, Selection action to execute (optional)

        TOGGLE
        Toggle -- Toggle selection for all elements.

        SELECT
        Select -- Select all elements.

        DESELECT
        Deselect -- Deselect all elements.

        INVERT
        Invert -- Invert selection of all elements.
                :return: Result of the operator call.
        """

class select_random(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        seed: int | None = 0,
        probability: float | None = 0.5,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Randomize existing selection or create new random selection

        :param execution_context:
        :param undo:
        :param seed: Seed, Source of randomness (in [-inf, inf], optional)
        :param probability: Probability, Chance of every point being included in the selection (in [0, 1], optional)
        :return: Result of the operator call.
        """

class separate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Separate selected geometry into a new point cloud

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
