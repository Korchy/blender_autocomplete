import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums
import bpy.types

class annotate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["DRAW", "DRAW_STRAIGHT", "DRAW_POLY", "ERASER"]
        | None = "DRAW",
        arrowstyle_start: typing.Literal[
            "NONE", "ARROW", "ARROW_OPEN", "ARROW_OPEN_INVERTED", "DIAMOND"
        ]
        | None = "NONE",
        arrowstyle_end: typing.Literal[
            "NONE", "ARROW", "ARROW_OPEN", "ARROW_OPEN_INVERTED", "DIAMOND"
        ]
        | None = "NONE",
        use_stabilizer: bool | None = False,
        stabilizer_factor: float | None = 0.75,
        stabilizer_radius: int | None = 35,
        stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
        | None = None,
        wait_for_input: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make annotations on the active data

                :param execution_context:
                :param undo:
                :param mode: Mode, Way to interpret mouse movements (optional)

        DRAW
        Draw Freehand -- Draw freehand stroke(s).

        DRAW_STRAIGHT
        Draw Straight Lines -- Draw straight line segment(s).

        DRAW_POLY
        Draw Poly Line -- Click to place endpoints of straight line segments (connected).

        ERASER
        Eraser -- Erase Annotation strokes.
                :param arrowstyle_start: Start Arrow Style, Stroke start style (optional)

        NONE
        None -- Dont use any arrow/style in corner.

        ARROW
        Arrow -- Use closed arrow style.

        ARROW_OPEN
        Open Arrow -- Use open arrow style.

        ARROW_OPEN_INVERTED
        Segment -- Use perpendicular segment style.

        DIAMOND
        Square -- Use square style.
                :param arrowstyle_end: End Arrow Style, Stroke end style (optional)

        NONE
        None -- Dont use any arrow/style in corner.

        ARROW
        Arrow -- Use closed arrow style.

        ARROW_OPEN
        Open Arrow -- Use open arrow style.

        ARROW_OPEN_INVERTED
        Segment -- Use perpendicular segment style.

        DIAMOND
        Square -- Use square style.
                :param use_stabilizer: Stabilize Stroke, Helper to draw smooth and clean lines. Press Shift for an invert effect (even if this option is not active) (optional)
                :param stabilizer_factor: Stabilizer Stroke Factor, Higher values give a smoother stroke (in [0, 1], optional)
                :param stabilizer_radius: Stabilizer Stroke Radius, Minimum distance from last point before stroke continues (in [0, 200], optional)
                :param stroke: Stroke, (optional)
                :param wait_for_input: Wait for Input, Wait for first click instead of painting immediately (optional)
                :return: Result of the operator call.
        """

class annotation_active_frame_delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete the active frame for the active Annotation Layer

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class annotation_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add new Annotation data-block

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class data_unlink(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Unlink active Annotation data-block

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class layer_annotation_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add new Annotation layer or note for the active data-block

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class layer_annotation_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["UP", "DOWN"] | None = "UP",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move the active Annotation layer up/down in the list

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class layer_annotation_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove active Annotation layer

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
