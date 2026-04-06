import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops.transform
import bpy.types
import mathutils

def add_feather_vertex(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Add vertex to feather

    :param location: Location, Location of vertex in normalized space
    """

def add_feather_vertex_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MASK_OT_add_feather_vertex: add_feather_vertex | None = None,
    MASK_OT_slide_point: slide_point | None = None,
) -> None:
    """Add new vertex to feather and slide it

    :param MASK_OT_add_feather_vertex: Add Feather Vertex, Add vertex to feather
    :param MASK_OT_slide_point: Slide Point, Slide control points
    """

def add_vertex(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Add vertex to active spline

    :param location: Location, Location of vertex in normalized space
    """

def add_vertex_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MASK_OT_add_vertex: add_vertex | None = None,
    MASK_OT_slide_point: slide_point | None = None,
) -> None:
    """Add new vertex and slide it

    :param MASK_OT_add_vertex: Add Vertex, Add vertex to active spline
    :param MASK_OT_slide_point: Slide Point, Slide control points
    """

def copy_splines(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the selected splines to the internal clipboard"""

def cyclic_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle cyclic for selected splines"""

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
) -> None:
    """Delete selected control points or splines

    :param confirm: Confirm, Prompt for confirmation
    """

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Duplicate selected control points and segments between them"""

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MASK_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Duplicate mask and move

    :param MASK_OT_duplicate: Duplicate Mask, Duplicate selected control points and segments between them
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def feather_weight_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset the feather weight to zero"""

def handle_type_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["AUTO", "VECTOR", "ALIGNED", "ALIGNED_DOUBLESIDE", "FREE"]
    | None = "AUTO",
) -> None:
    """Set type of handles for selected control points

    :param type: Type, Spline type
    """

def hide_view_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
) -> None:
    """Reveal temporarily hidden mask layers

    :param select: Select
    """

def hide_view_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Temporarily hide mask layers

    :param unselected: Unselected, Hide unselected rather than selected layers
    """

def layer_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move the active layer up/down in the list

    :param direction: Direction, Direction to move the active layer
    """

def layer_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
) -> None:
    """Add new mask layer for masking

    :param name: Name, Name of new mask layer
    """

def layer_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove mask layer"""

def new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
) -> None:
    """Create new mask

    :param name: Name, Name of new mask
    """

def normals_make_consistent(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Recalculate the direction of selected handles"""

def parent_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear the masks parenting"""

def parent_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set the masks parenting"""

def paste_splines(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Paste splines from the internal clipboard"""

def primitive_circle_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    size: float | None = 100.0,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Add new circle-shaped spline

    :param size: Size, Size of new circle
    :param location: Location, Location of new circle
    """

def primitive_square_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    size: float | None = 100.0,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Add new square-shaped spline

    :param size: Size, Size of new circle
    :param location: Location, Location of new circle
    """

def select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect: bool | None = False,
    toggle: bool | None = False,
    deselect_all: bool | None = False,
    select_passthrough: bool | None = False,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Select spline points

    :param extend: Extend, Extend selection instead of deselecting everything first
    :param deselect: Deselect, Remove from selection
    :param toggle: Toggle Selection, Toggle the selection
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :param location: Location, Location of vertex in normalized space
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Change selection of all curve points

        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
    """

def select_box(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
) -> None:
    """Select curve points using box selection

        :param xmin: X Min
        :param xmax: X Max
        :param ymin: Y Min
        :param ymax: Y Max
        :param wait_for_input: Wait for Input
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
    """

def select_circle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    x: int | None = 0,
    y: int | None = 0,
    radius: int | None = 25,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
) -> None:
    """Select curve points using circle selection

        :param x: X
        :param y: Y
        :param radius: Radius
        :param wait_for_input: Wait for Input
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
    """

def select_lasso(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_smooth_stroke: bool | None = False,
    smooth_stroke_factor: float | None = 0.75,
    smooth_stroke_radius: int | None = 35,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
) -> None:
    """Select curve points using lasso selection

        :param path: Path
        :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
        :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
        :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
    """

def select_less(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Deselect spline points at the boundary of each selection region"""

def select_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all curve points linked to already selected ones"""

def select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deselect: bool | None = False,
) -> None:
    """(De)select all points linked to the curve under the mouse cursor

    :param deselect: Deselect
    """

def select_more(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select more spline points connected to initial selection"""

def shape_key_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove mask shape keyframe for active mask layer at the current frame"""

def shape_key_feather_reset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset feather weights on all selected points animation values"""

def shape_key_insert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Insert mask shape keyframe for active mask layer at the current frame"""

def shape_key_rekey(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: bool | None = True,
    feather: bool | None = True,
) -> None:
    """Recalculate animation data on selected points for frames selected in the dopesheet

    :param location: Location
    :param feather: Feather
    """

def slide_point(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    slide_feather: bool | None = False,
    is_new_point: bool | None = False,
) -> None:
    """Slide control points

    :param slide_feather: Slide Feather, First try to slide feather instead of vertex
    :param is_new_point: Slide New Point, Newly created vertex is being slid
    """

def slide_spline_curvature(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Slide a point on the spline to define its curvature"""

def switch_direction(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Switch direction of selected splines"""
