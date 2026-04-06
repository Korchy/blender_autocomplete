import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

def annotate(
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
) -> None:
    """Make annotations on the active data

        :param mode: Mode, Way to interpret mouse movements

    DRAW
    Draw Freehand -- Draw freehand stroke(s).

    DRAW_STRAIGHT
    Draw Straight Lines -- Draw straight line segment(s).

    DRAW_POLY
    Draw Poly Line -- Click to place endpoints of straight line segments (connected).

    ERASER
    Eraser -- Erase Annotation strokes.
        :param arrowstyle_start: Start Arrow Style, Stroke start style

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
        :param arrowstyle_end: End Arrow Style, Stroke end style

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
        :param use_stabilizer: Stabilize Stroke, Helper to draw smooth and clean lines. Press Shift for an invert effect (even if this option is not active)
        :param stabilizer_factor: Stabilizer Stroke Factor, Higher values gives a smoother stroke
        :param stabilizer_radius: Stabilizer Stroke Radius, Minimum distance from last point before stroke continues
        :param stroke: Stroke
        :param wait_for_input: Wait for Input, Wait for first click instead of painting immediately
    """

def annotation_active_frame_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete the active frame for the active Annotation Layer"""

def annotation_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add new Annotation data-block"""

def data_unlink(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Unlink active Annotation data-block"""

def layer_annotation_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add new Annotation layer or note for the active data-block"""

def layer_annotation_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move the active Annotation layer up/down in the list

    :param type: Type
    """

def layer_annotation_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove active Annotation layer"""
