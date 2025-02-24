import typing
import collections.abc
import typing_extensions
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
):
    """Make annotations on the active data

        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode, Way to interpret mouse movements

    DRAW
    Draw Freehand -- Draw freehand stroke(s).

    DRAW_STRAIGHT
    Draw Straight Lines -- Draw straight line segment(s).

    DRAW_POLY
    Draw Poly Line -- Click to place endpoints of straight line segments (connected).

    ERASER
    Eraser -- Erase Annotation strokes.
        :type mode: typing.Literal['DRAW','DRAW_STRAIGHT','DRAW_POLY','ERASER'] | None
        :param arrowstyle_start: Start Arrow Style, Stroke start style

    NONE
    None -- Don't use any arrow/style in corner.

    ARROW
    Arrow -- Use closed arrow style.

    ARROW_OPEN
    Open Arrow -- Use open arrow style.

    ARROW_OPEN_INVERTED
    Segment -- Use perpendicular segment style.

    DIAMOND
    Square -- Use square style.
        :type arrowstyle_start: typing.Literal['NONE','ARROW','ARROW_OPEN','ARROW_OPEN_INVERTED','DIAMOND'] | None
        :param arrowstyle_end: End Arrow Style, Stroke end style

    NONE
    None -- Don't use any arrow/style in corner.

    ARROW
    Arrow -- Use closed arrow style.

    ARROW_OPEN
    Open Arrow -- Use open arrow style.

    ARROW_OPEN_INVERTED
    Segment -- Use perpendicular segment style.

    DIAMOND
    Square -- Use square style.
        :type arrowstyle_end: typing.Literal['NONE','ARROW','ARROW_OPEN','ARROW_OPEN_INVERTED','DIAMOND'] | None
        :param use_stabilizer: Stabilize Stroke, Helper to draw smooth and clean lines. Press Shift for an invert effect (even if this option is not active)
        :type use_stabilizer: bool | None
        :param stabilizer_factor: Stabilizer Stroke Factor, Higher values gives a smoother stroke
        :type stabilizer_factor: float | None
        :param stabilizer_radius: Stabilizer Stroke Radius, Minimum distance from last point before stroke continues
        :type stabilizer_radius: int | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param wait_for_input: Wait for Input, Wait for first click instead of painting immediately
        :type wait_for_input: bool | None
    """

def annotation_active_frame_delete(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Delete the active frame for the active Annotation Layer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def annotation_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add new Annotation data-block

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def data_unlink(execution_context: int | str | None = None, undo: bool | None = None):
    """Unlink active Annotation data-block

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def layer_annotation_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add new Annotation layer or note for the active data-block

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def layer_annotation_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move the active Annotation layer up/down in the list

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['UP','DOWN'] | None
    """

def layer_annotation_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove active Annotation layer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def tint_flip(execution_context: int | str | None = None, undo: bool | None = None):
    """Switch tint colors

    :type execution_context: int | str | None
    :type undo: bool | None
    """
