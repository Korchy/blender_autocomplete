import typing
import collections.abc
import typing_extensions
import bpy.ops.transform
import bpy.types
import mathutils

def add_feather_vertex(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Add vertex to feather

    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Location of vertex in normalized space
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def add_feather_vertex_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MASK_OT_add_feather_vertex: add_feather_vertex | None = None,
    MASK_OT_slide_point: slide_point | None = None,
):
    """Add new vertex to feather and slide it

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MASK_OT_add_feather_vertex: Add Feather Vertex, Add vertex to feather
    :type MASK_OT_add_feather_vertex: add_feather_vertex | None
    :param MASK_OT_slide_point: Slide Point, Slide control points
    :type MASK_OT_slide_point: slide_point | None
    """

def add_vertex(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Add vertex to active spline

    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Location of vertex in normalized space
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def add_vertex_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MASK_OT_add_vertex: add_vertex | None = None,
    MASK_OT_slide_point: slide_point | None = None,
):
    """Add new vertex and slide it

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MASK_OT_add_vertex: Add Vertex, Add vertex to active spline
    :type MASK_OT_add_vertex: add_vertex | None
    :param MASK_OT_slide_point: Slide Point, Slide control points
    :type MASK_OT_slide_point: slide_point | None
    """

def copy_splines(execution_context: int | str | None = None, undo: bool | None = None):
    """Copy the selected splines to the internal clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def cyclic_toggle(execution_context: int | str | None = None, undo: bool | None = None):
    """Toggle cyclic for selected splines

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
):
    """Delete selected control points or splines

    :type execution_context: int | str | None
    :type undo: bool | None
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool | None
    """

def duplicate(execution_context: int | str | None = None, undo: bool | None = None):
    """Duplicate selected control points and segments between them

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MASK_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Duplicate mask and move

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MASK_OT_duplicate: Duplicate Mask, Duplicate selected control points and segments between them
    :type MASK_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def feather_weight_clear(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Reset the feather weight to zero

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def handle_type_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["AUTO", "VECTOR", "ALIGNED", "ALIGNED_DOUBLESIDE", "FREE"]
    | None = "AUTO",
):
    """Set type of handles for selected control points

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Spline type
    :type type: typing.Literal['AUTO','VECTOR','ALIGNED','ALIGNED_DOUBLESIDE','FREE'] | None
    """

def hide_view_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
):
    """Reveal temporarily hidden mask layers

    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | None
    """

def hide_view_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
):
    """Temporarily hide mask layers

    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected layers
    :type unselected: bool | None
    """

def layer_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move the active layer up/down in the list

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to move the active layer
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def layer_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
):
    """Add new mask layer for masking

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of new mask layer
    :type name: str
    """

def layer_remove(execution_context: int | str | None = None, undo: bool | None = None):
    """Remove mask layer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
):
    """Create new mask

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of new mask
    :type name: str
    """

def normals_make_consistent(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Recalculate the direction of selected handles

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def parent_clear(execution_context: int | str | None = None, undo: bool | None = None):
    """Clear the mask's parenting

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def parent_set(execution_context: int | str | None = None, undo: bool | None = None):
    """Set the mask's parenting

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def paste_splines(execution_context: int | str | None = None, undo: bool | None = None):
    """Paste splines from the internal clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def primitive_circle_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    size: float | None = 100.0,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Add new circle-shaped spline

    :type execution_context: int | str | None
    :type undo: bool | None
    :param size: Size, Size of new circle
    :type size: float | None
    :param location: Location, Location of new circle
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def primitive_square_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    size: float | None = 100.0,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Add new square-shaped spline

    :type execution_context: int | str | None
    :type undo: bool | None
    :param size: Size, Size of new circle
    :type size: float | None
    :param location: Location, Location of new circle
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
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
):
    """Select spline points

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | None
    :param deselect: Deselect, Remove from selection
    :type deselect: bool | None
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: bool | None
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool | None
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :type select_passthrough: bool | None
    :param location: Location, Location of vertex in normalized space
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Change selection of all curve points

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
        :type action: typing.Literal['TOGGLE','SELECT','DESELECT','INVERT'] | None
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
):
    """Select curve points using box selection

        :type execution_context: int | str | None
        :type undo: bool | None
        :param xmin: X Min
        :type xmin: int | None
        :param xmax: X Max
        :type xmax: int | None
        :param ymin: Y Min
        :type ymin: int | None
        :param ymax: Y Max
        :type ymax: int | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
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
):
    """Select curve points using circle selection

        :type execution_context: int | str | None
        :type undo: bool | None
        :param x: X
        :type x: int | None
        :param y: Y
        :type y: int | None
        :param radius: Radius
        :type radius: int | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
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
):
    """Select curve points using lasso selection

        :type execution_context: int | str | None
        :type undo: bool | None
        :param path: Path
        :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
        :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
        :type use_smooth_stroke: bool | None
        :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
        :type smooth_stroke_factor: float | None
        :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
        :type smooth_stroke_radius: int | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
    """

def select_less(execution_context: int | str | None = None, undo: bool | None = None):
    """Deselect spline points at the boundary of each selection region

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked(execution_context: int | str | None = None, undo: bool | None = None):
    """Select all curve points linked to already selected ones

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deselect: bool | None = False,
):
    """(De)select all points linked to the curve under the mouse cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param deselect: Deselect
    :type deselect: bool | None
    """

def select_more(execution_context: int | str | None = None, undo: bool | None = None):
    """Select more spline points connected to initial selection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def shape_key_clear(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove mask shape keyframe for active mask layer at the current frame

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def shape_key_feather_reset(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Reset feather weights on all selected points animation values

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def shape_key_insert(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Insert mask shape keyframe for active mask layer at the current frame

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def shape_key_rekey(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: bool | None = True,
    feather: bool | None = True,
):
    """Recalculate animation data on selected points for frames selected in the dopesheet

    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location
    :type location: bool | None
    :param feather: Feather
    :type feather: bool | None
    """

def slide_point(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    slide_feather: bool | None = False,
    is_new_point: bool | None = False,
):
    """Slide control points

    :type execution_context: int | str | None
    :type undo: bool | None
    :param slide_feather: Slide Feather, First try to slide feather instead of vertex
    :type slide_feather: bool | None
    :param is_new_point: Slide New Point, Newly created vertex is being slid
    :type is_new_point: bool | None
    """

def slide_spline_curvature(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Slide a point on the spline to define its curvature

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def switch_direction(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Switch direction of selected splines

    :type execution_context: int | str | None
    :type undo: bool | None
    """
