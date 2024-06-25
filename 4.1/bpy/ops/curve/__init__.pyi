import typing
import collections.abc
import bpy.ops.transform
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def cyclic_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    direction: str | None = "CYCLIC_U",
):
    """Make active spline closed/opened loop

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to make surface cyclic in
    :type direction: str | None
    """

    ...

def de_select_first(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """(De)select first of visible part of each NURBS

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def de_select_last(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """(De)select last of visible part of each NURBS

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def decimate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    ratio: typing.Any | None = 1.0,
):
    """Simplify selected curves

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param ratio: Ratio
    :type ratio: typing.Any | None
    """

    ...

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "VERT",
):
    """Delete selected control points or segments

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Which elements to delete
    :type type: str | None
    """

    ...

def dissolve_verts(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete selected control points, correcting surrounding handles

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def draw(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    error_threshold: typing.Any | None = 0.0,
    fit_method: str | None = "REFIT",
    corner_angle: typing.Any | None = 1.22173,
    use_cyclic: bool | typing.Any | None = True,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    wait_for_input: bool | typing.Any | None = True,
):
    """Draw a freehand spline

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param error_threshold: Error, Error distance threshold (in object units)
    :type error_threshold: typing.Any | None
    :param fit_method: Fit Method
    :type fit_method: str | None
    :param corner_angle: Corner Angle
    :type corner_angle: typing.Any | None
    :param use_cyclic: Cyclic
    :type use_cyclic: bool | typing.Any | None
    :param stroke: Stroke
    :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | typing.Any | None
    """

    ...

def duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Duplicate selected control points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def duplicate_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    CURVE_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Duplicate curve and move

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param CURVE_OT_duplicate: Duplicate Curve, Duplicate selected control points
    :type CURVE_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def extrude(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "TRANSLATION",
):
    """Extrude selected control point(s)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: str | None
    """

    ...

def extrude_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    CURVE_OT_extrude: extrude | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Extrude curve and move result

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param CURVE_OT_extrude: Extrude, Extrude selected control point(s)
    :type CURVE_OT_extrude: extrude | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def handle_type_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "AUTOMATIC",
):
    """Set type of handles for selected control points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Spline type
    :type type: str | None
    """

    ...

def hide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselected: bool | typing.Any | None = False,
):
    """Hide (un)selected control points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: bool | typing.Any | None
    """

    ...

def make_segment(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Join two curves by their selected ends

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def match_texture_space(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Match texture space to object's bounding box

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def normals_make_consistent(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    calc_length: bool | typing.Any | None = False,
):
    """Recalculate the direction of selected handles

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param calc_length: Length, Recalculate handle length
    :type calc_length: bool | typing.Any | None
    """

    ...

def pen(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
    deselect: bool | typing.Any | None = False,
    toggle: bool | typing.Any | None = False,
    deselect_all: bool | typing.Any | None = False,
    select_passthrough: bool | typing.Any | None = False,
    extrude_point: bool | typing.Any | None = False,
    extrude_handle: str | None = "VECTOR",
    delete_point: bool | typing.Any | None = False,
    insert_point: bool | typing.Any | None = False,
    move_segment: bool | typing.Any | None = False,
    select_point: bool | typing.Any | None = False,
    move_point: bool | typing.Any | None = False,
    close_spline: bool | typing.Any | None = True,
    close_spline_method: str | None = "OFF",
    toggle_vector: bool | typing.Any | None = False,
    cycle_handle_type: bool | typing.Any | None = False,
):
    """Construct and edit splines

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param extend: Extend, Extend selection instead of deselecting everything first
        :type extend: bool | typing.Any | None
        :param deselect: Deselect, Remove from selection
        :type deselect: bool | typing.Any | None
        :param toggle: Toggle Selection, Toggle the selection
        :type toggle: bool | typing.Any | None
        :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
        :type deselect_all: bool | typing.Any | None
        :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
        :type select_passthrough: bool | typing.Any | None
        :param extrude_point: Extrude Point, Add a point connected to the last selected point
        :type extrude_point: bool | typing.Any | None
        :param extrude_handle: Extrude Handle Type, Type of the extruded handle
        :type extrude_handle: str | None
        :param delete_point: Delete Point, Delete an existing point
        :type delete_point: bool | typing.Any | None
        :param insert_point: Insert Point, Insert Point into a curve segment
        :type insert_point: bool | typing.Any | None
        :param move_segment: Move Segment, Delete an existing point
        :type move_segment: bool | typing.Any | None
        :param select_point: Select Point, Select a point or its handles
        :type select_point: bool | typing.Any | None
        :param move_point: Move Point, Move a point or its handles
        :type move_point: bool | typing.Any | None
        :param close_spline: Close Spline, Make a spline cyclic by clicking endpoints
        :type close_spline: bool | typing.Any | None
        :param close_spline_method: Close Spline Method, The condition for close spline to activate

    OFF
    None.

    ON_PRESS
    On Press -- Move handles after closing the spline.

    ON_CLICK
    On Click -- Spline closes on release if not dragged.
        :type close_spline_method: str | None
        :param toggle_vector: Toggle Vector, Toggle between Vector and Auto handles
        :type toggle_vector: bool | typing.Any | None
        :param cycle_handle_type: Cycle Handle Type, Cycle between all four handle types
        :type cycle_handle_type: bool | typing.Any | None
    """

    ...

def primitive_bezier_circle_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    radius: typing.Any | None = 1.0,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    scale: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Construct a Bézier Circle

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
        :param scale: Scale, Scale for the newly added object
        :type scale: typing.Any | None
    """

    ...

def primitive_bezier_curve_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    radius: typing.Any | None = 1.0,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    scale: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Construct a Bézier Curve

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
        :param scale: Scale, Scale for the newly added object
        :type scale: typing.Any | None
    """

    ...

def primitive_nurbs_circle_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    radius: typing.Any | None = 1.0,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    scale: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Construct a Nurbs Circle

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
        :param scale: Scale, Scale for the newly added object
        :type scale: typing.Any | None
    """

    ...

def primitive_nurbs_curve_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    radius: typing.Any | None = 1.0,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    scale: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Construct a Nurbs Curve

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
        :param scale: Scale, Scale for the newly added object
        :type scale: typing.Any | None
    """

    ...

def primitive_nurbs_path_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    radius: typing.Any | None = 1.0,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    scale: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Construct a Path

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
        :param scale: Scale, Scale for the newly added object
        :type scale: typing.Any | None
    """

    ...

def radius_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    radius: typing.Any | None = 1.0,
):
    """Set per-point radius which is used for bevel tapering

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param radius: Radius
    :type radius: typing.Any | None
    """

    ...

def reveal(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    select: bool | typing.Any | None = True,
):
    """Reveal hidden control points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | typing.Any | None
    """

    ...

def select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: str | None = "TOGGLE",
):
    """(De)select all control points

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
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
        :type action: str | None
    """

    ...

def select_less(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Deselect control points at the boundary of each selection region

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select all control points linked to the current selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_linked_pick(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    deselect: bool | typing.Any | None = False,
):
    """Select all control points linked to already selected ones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param deselect: Deselect, Deselect linked control points rather than selecting them
    :type deselect: bool | typing.Any | None
    """

    ...

def select_more(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select control points at the boundary of each selection region

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_next(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select control points following already selected ones along the curves

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_nth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    skip: typing.Any | None = 1,
    nth: typing.Any | None = 1,
    offset: typing.Any | None = 0,
):
    """Deselect every Nth point starting from the active one

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: typing.Any | None
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: typing.Any | None
    :param offset: Offset, Offset from the starting point
    :type offset: typing.Any | None
    """

    ...

def select_previous(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select control points preceding already selected ones along the curves

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_random(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    ratio: typing.Any | None = 0.5,
    seed: typing.Any | None = 0,
    action: str | None = "SELECT",
):
    """Randomly select some control points

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param ratio: Ratio, Portion of items to select randomly
        :type ratio: typing.Any | None
        :param seed: Random Seed, Seed for the random number generator
        :type seed: typing.Any | None
        :param action: Action, Selection action to execute

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.
        :type action: str | None
    """

    ...

def select_row(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select a row of control points including active one

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_similar(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "WEIGHT",
    compare: str | None = "EQUAL",
    threshold: typing.Any | None = 0.1,
):
    """Select similar curve points by property type

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    :param compare: Compare
    :type compare: str | None
    :param threshold: Threshold
    :type threshold: typing.Any | None
    """

    ...

def separate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    confirm: bool | typing.Any | None = True,
):
    """Separate selected points from connected unselected points into a new object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool | typing.Any | None
    """

    ...

def shade_flat(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Set shading to flat

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def shade_smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Set shading to smooth

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def shortest_path_pick(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select shortest path between two selections

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Flatten angles of selected points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def smooth_radius(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Interpolate radii of selected points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def smooth_tilt(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Interpolate tilt of selected points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def smooth_weight(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Interpolate weight of selected points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def spin(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    center: typing.Any | None = (0.0, 0.0, 0.0),
    axis: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Extrude selected boundary row around pivot point and current view axis

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param center: Center, Center in global view space
    :type center: typing.Any | None
    :param axis: Axis, Axis in global view space
    :type axis: typing.Any | None
    """

    ...

def spline_type_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "POLY",
    use_handles: bool | typing.Any | None = False,
):
    """Set type of active spline

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Spline type
    :type type: str | None
    :param use_handles: Handles, Use handles when converting Bézier curves into polygons
    :type use_handles: bool | typing.Any | None
    """

    ...

def spline_weight_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    weight: typing.Any | None = 1.0,
):
    """Set softbody goal weight for selected points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param weight: Weight
    :type weight: typing.Any | None
    """

    ...

def split(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Split off selected points from connected unselected points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def subdivide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    number_cuts: typing.Any | None = 1,
):
    """Subdivide selected segments

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param number_cuts: Number of Cuts
    :type number_cuts: typing.Any | None
    """

    ...

def switch_direction(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Switch direction of selected splines

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def tilt_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Clear the tilt of selected control points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    location: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Add a new control point (linked to only selected end-curve one, if any)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Location to add new vertex at
    :type location: typing.Any | None
    """

    ...
