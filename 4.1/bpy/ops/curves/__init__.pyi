import typing
import collections.abc
import bpy.ops.transform
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def attribute_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value_float: typing.Any | None = 0.0,
    value_float_vector_2d: typing.Any | None = (0.0, 0.0),
    value_float_vector_3d: typing.Any | None = (0.0, 0.0, 0.0),
    value_int: typing.Any | None = 0,
    value_color: typing.Any | None = (1.0, 1.0, 1.0, 1.0),
    value_bool: bool | typing.Any | None = False,
):
    """Set values of the active attribute for selected elements

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param value_float: Value
    :type value_float: typing.Any | None
    :param value_float_vector_2d: Value
    :type value_float_vector_2d: typing.Any | None
    :param value_float_vector_3d: Value
    :type value_float_vector_3d: typing.Any | None
    :param value_int: Value
    :type value_int: typing.Any | None
    :param value_color: Value
    :type value_color: typing.Any | None
    :param value_bool: Value
    :type value_bool: bool | typing.Any | None
    """

    ...

def convert_from_particle_system(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a new curves object based on the current state of the particle system

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def convert_to_particle_system(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a new or update an existing hair particle system on the surface object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove selected control points or curves

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
    is_curve_2d: bool | typing.Any | None = False,
    bezier_as_nurbs: bool | typing.Any | None = False,
):
    """Draw a freehand curve

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
    :param is_curve_2d: Curve 2D
    :type is_curve_2d: bool | typing.Any | None
    :param bezier_as_nurbs: As NURBS
    :type bezier_as_nurbs: bool | typing.Any | None
    """

    ...

def duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy selected points or curves

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
    CURVES_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Make copies of selected elements and move them

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param CURVES_OT_duplicate: Duplicate, Copy selected points or curves
    :type CURVES_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def extrude(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Extrude selected control point(s)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def extrude_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    CURVES_OT_extrude: extrude | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Extrude curve and move result

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param CURVES_OT_extrude: Extrude, Extrude selected control point(s)
    :type CURVES_OT_extrude: extrude | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def sculptmode_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Enter/Exit sculpt mode for curves

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
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

def select_ends(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    amount_start: typing.Any | None = 0,
    amount_end: typing.Any | None = 1,
):
    """Select end points of curves

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param amount_start: Amount Front, Number of points to select from the front
    :type amount_start: typing.Any | None
    :param amount_end: Amount Back, Number of points to select from the back
    :type amount_end: typing.Any | None
    """

    ...

def select_less(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Shrink the selection by one point

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
    """Select all points in curves with any point selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_more(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Grow the selection by one point

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
    seed: typing.Any | None = 0,
    probability: typing.Any | None = 0.5,
):
    """Randomizes existing selection or create new random selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param seed: Seed, Source of randomness
    :type seed: typing.Any | None
    :param probability: Probability, Chance of every point or curve being included in the selection
    :type probability: typing.Any | None
    """

    ...

def set_selection_domain(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    domain: str | None = "POINT",
):
    """Change the mode used for selection masking in curves sculpt mode

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param domain: Domain
    :type domain: str | None
    """

    ...

def snap_curves_to_surface(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    attach_mode: str | None = "NEAREST",
):
    """Move curves so that the first point is exactly on the surface mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param attach_mode: Attach Mode, How to find the point on the surface to attach to

    NEAREST
    Nearest -- Find the closest point on the surface for the root point of every curve and move the root there.

    DEFORM
    Deform -- Re-attach curves to a deformed surface using the existing attachment information. This only works when the topology of the surface mesh has not changed.
        :type attach_mode: str | None
    """

    ...

def surface_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Use the active object as surface for selected curves objects and set it as the parent

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
