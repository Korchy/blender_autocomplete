import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops.transform
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

def add_bezier(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add new bezier curve

        :param radius: Radius
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def add_circle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add new circle curve

        :param radius: Radius
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def attribute_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value_float: float | None = 0.0,
    value_float_vector_2d: collections.abc.Iterable[float] | None = (0.0, 0.0),
    value_float_vector_3d: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    value_int: int | None = 0,
    value_int_vector_2d: collections.abc.Iterable[int] | None = (0, 0),
    value_color: collections.abc.Iterable[float] | None = (1.0, 1.0, 1.0, 1.0),
    value_bool: bool | None = False,
) -> None:
    """Set values of the active attribute for selected elements

    :param value_float: Value
    :param value_float_vector_2d: Value
    :param value_float_vector_3d: Value
    :param value_int: Value
    :param value_int_vector_2d: Value
    :param value_color: Value
    :param value_bool: Value
    """

def convert_from_particle_system(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a new curves object based on the current state of the particle system"""

def convert_to_particle_system(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a new or update an existing hair particle system on the surface object"""

def curve_type_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.CurvesTypeItems | None = "POLY",
    use_handles: bool | None = False,
) -> None:
    """Set type of selected curves

    :param type: Type, Curve type
    :param use_handles: Handles, Take handle information into account in the conversion
    """

def cyclic_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Make active curve closed/opened loop"""

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove selected control points or curves"""

def draw(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    error_threshold: float | None = 0.0,
    fit_method: bpy.stub_internal.rna_enums.CurveFitMethodItems | None = "REFIT",
    corner_angle: float | None = 1.22173,
    use_cyclic: bool | None = True,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    wait_for_input: bool | None = True,
    is_curve_2d: bool | None = False,
    bezier_as_nurbs: bool | None = False,
) -> None:
    """Draw a freehand curve

    :param error_threshold: Error, Error distance threshold (in object units)
    :param fit_method: Fit Method
    :param corner_angle: Corner Angle
    :param use_cyclic: Cyclic
    :param stroke: Stroke
    :param wait_for_input: Wait for Input
    :param is_curve_2d: Curve 2D
    :param bezier_as_nurbs: As NURBS
    """

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy selected points or curves"""

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    CURVES_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Make copies of selected elements and move them

    :param CURVES_OT_duplicate: Duplicate, Copy selected points or curves
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def extrude(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Extrude selected control point(s)"""

def extrude_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    CURVES_OT_extrude: extrude | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Extrude curve and move result

    :param CURVES_OT_extrude: Extrude, Extrude selected control point(s)
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def handle_type_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.CurvesHandleTypeItems | None = "AUTO",
) -> None:
    """Set the handle type for bezier curves

    :param type: Type
    """

def sculptmode_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Enter/Exit sculpt mode for curves"""

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """(De)select all control points

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

def select_ends(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    amount_start: int | None = 0,
    amount_end: int | None = 1,
) -> None:
    """Select end points of curves

    :param amount_start: Amount Front, Number of points to select from the front
    :param amount_end: Amount Back, Number of points to select from the back
    """

def select_less(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Shrink the selection by one point"""

def select_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all points in curves with any point selection"""

def select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deselect: bool | None = False,
) -> None:
    """Select all points in the curve under the cursor

    :param deselect: Deselect, Deselect linked control points rather than selecting them
    """

def select_more(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Grow the selection by one point"""

def select_random(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    seed: int | None = 0,
    probability: float | None = 0.5,
) -> None:
    """Randomizes existing selection or create new random selection

    :param seed: Seed, Source of randomness
    :param probability: Probability, Chance of every point or curve being included in the selection
    """

def set_selection_domain(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    domain: bpy.stub_internal.rna_enums.AttributeCurvesDomainItems | None = "POINT",
) -> None:
    """Change the mode used for selection masking in curves sculpt mode

    :param domain: Domain
    """

def snap_curves_to_surface(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    attach_mode: typing.Literal["NEAREST", "DEFORM"] | None = "NEAREST",
) -> None:
    """Move curves so that the first point is exactly on the surface mesh

        :param attach_mode: Attach Mode, How to find the point on the surface to attach to

    NEAREST
    Nearest -- Find the closest point on the surface for the root point of every curve and move the root there.

    DEFORM
    Deform -- Re-attach curves to a deformed surface using the existing attachment information. This only works when the topology of the surface mesh has not changed.
    """

def subdivide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    number_cuts: int | None = 1,
) -> None:
    """Subdivide selected curve segments

    :param number_cuts: Number of Cuts
    """

def surface_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Use the active object as surface for selected curves objects and set it as the parent"""

def switch_direction(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reverse the direction of the selected curves"""

def tilt_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear the tilt of selected control points"""
