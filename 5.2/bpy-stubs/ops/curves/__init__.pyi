import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

class add_bezier(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add new Bézier curve

                :param execution_context:
                :param undo:
                :param radius: Radius, (in [0, inf], optional)
                :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class add_circle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add new circle curve

                :param execution_context:
                :param undo:
                :param radius: Radius, (in [0, inf], optional)
                :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

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

class convert_from_particle_system(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a new curves object based on the current state of the particle system

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class convert_to_particle_system(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a new or update an existing hair particle system on the surface object

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class curve_type_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[bpy.stub_internal.rna_enums.CurvesTypeItems]
        | None = "POLY",
        use_handles: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set type of selected curves

        :param execution_context:
        :param undo:
        :param type: Type, Curve type (optional)
        :param use_handles: Handles, Take handle information into account in the conversion (optional)
        :return: Result of the operator call.
        """

class cyclic_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make active curve closed/open loop

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove selected control points or curves

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
        *,
        error_threshold: float | None = 0.0,
        fit_method: typing.Literal[bpy.stub_internal.rna_enums.CurveFitMethodItems]
        | None = "REFIT",
        corner_angle: float | None = 1.22173,
        use_cyclic: bool | None = True,
        stroke: None
        | bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
        | None = None,
        wait_for_input: bool | None = True,
        is_curve_2d: bool | None = False,
        bezier_as_nurbs: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Draw a freehand curve

        :param execution_context:
        :param undo:
        :param error_threshold: Error, Error distance threshold (in object units) (in [0, 10], optional)
        :param fit_method: Fit Method, (optional)
        :param corner_angle: Corner Angle, (in [0, 3.14159], optional)
        :param use_cyclic: Cyclic, (optional)
        :param stroke: Stroke, (optional)
        :param wait_for_input: Wait for Input, (optional)
        :param is_curve_2d: Curve 2D, (optional)
        :param bezier_as_nurbs: As NURBS, (optional)
        :return: Result of the operator call.
        """

class duplicate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy selected points or curves

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
        CURVES_OT_duplicate: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make copies of selected elements and move them

        :param execution_context:
        :param undo:
        :param CURVES_OT_duplicate: Duplicate, Copy selected points or curves (optional, `bpy.ops.curves.duplicate` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class extrude(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude selected control point(s)

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class extrude_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        CURVES_OT_extrude: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude curve and move result

        :param execution_context:
        :param undo:
        :param CURVES_OT_extrude: Extrude, Extrude selected control point(s) (optional, `bpy.ops.curves.extrude` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class handle_type_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            "AUTO", "VECTOR", "ALIGN", "FREE_ALIGN", "TOGGLE_FREE_ALIGN"
        ]
        | None = "AUTO",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the handle type for Bézier curves

                :param execution_context:
                :param undo:
                :param type: Type, (optional)

        AUTO
        Auto -- The location is automatically calculated to be smooth.

        VECTOR
        Vector -- The location is calculated to point to the next/previous control point.

        ALIGN
        Align -- The location is constrained to point in the opposite direction as the other handle.

        FREE_ALIGN
        Free -- The handle can be moved anywhere, and does not influence the points other handle.

        TOGGLE_FREE_ALIGN
        Toggle Free/Align -- Replace Free handles with Align, and all Align with Free handles.
                :return: Result of the operator call.
        """

class pen(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        extend: bool | None = False,
        deselect: bool | None = False,
        toggle: bool | None = False,
        deselect_all: bool | None = False,
        select_passthrough: bool | None = False,
        extrude_point: bool | None = False,
        extrude_handle: typing.Literal["AUTO", "VECTOR"] | None = "VECTOR",
        delete_point: bool | None = False,
        insert_point: bool | None = False,
        move_segment: bool | None = False,
        select_point: bool | None = False,
        move_point: bool | None = False,
        cycle_handle_type: bool | None = False,
        size: float | None = 0.01,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Construct and edit Bézier curves

        :param execution_context:
        :param undo:
        :param extend: Extend, Extend selection instead of deselecting everything first (optional)
        :param deselect: Deselect, Remove from selection (optional)
        :param toggle: Toggle Selection, Toggle the selection (optional)
        :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor (optional)
        :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected (optional)
        :param extrude_point: Extrude Point, Add a point connected to the last selected point (optional)
        :param extrude_handle: Extrude Handle Type, Type of the extruded handle (optional)
        :param delete_point: Delete Point, Delete an existing point (optional)
        :param insert_point: Insert Point, Insert Point into a curve segment (optional)
        :param move_segment: Move Segment, Move an existing curve segment (optional)
        :param select_point: Select Point, Select a point or its handles (optional)
        :param move_point: Move Point, Move a point or its handles (optional)
        :param cycle_handle_type: Cycle Handle Type, Cycle between all four handle types (optional)
        :param size: Size, Diameter of new points (in [0, inf], optional)
        :return: Result of the operator call.
        """

class sculptmode_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Enter/Exit sculpt mode for curves

        :param execution_context:
        :param undo:
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
        """(De)select all control points

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

class select_ends(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        amount_start: int | None = 0,
        amount_end: int | None = 1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select end points of curves

        :param execution_context:
        :param undo:
        :param amount_start: Amount Front, Number of points to select from the front (in [0, inf], optional)
        :param amount_end: Amount Back, Number of points to select from the back (in [0, inf], optional)
        :return: Result of the operator call.
        """

class select_less(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Shrink the selection by one point

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_linked(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all points in curves with any point selection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_linked_pick(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        deselect: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all points in the curve under the cursor

        :param execution_context:
        :param undo:
        :param deselect: Deselect, Deselect linked control points rather than selecting them (optional)
        :return: Result of the operator call.
        """

class select_more(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Grow the selection by one point

        :param execution_context:
        :param undo:
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
        :param probability: Probability, Chance of every point or curve being included in the selection (in [0, 1], optional)
        :return: Result of the operator call.
        """

class separate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Separate selected geometry into a new object

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class set_selection_domain(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        domain: typing.Literal[bpy.stub_internal.rna_enums.AttributeCurvesDomainItems]
        | None = "POINT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change the mode used for selection masking in curves sculpt mode

        :param execution_context:
        :param undo:
        :param domain: Domain, (optional)
        :return: Result of the operator call.
        """

class snap_curves_to_surface(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        attach_mode: typing.Literal["NEAREST", "DEFORM"] | None = "NEAREST",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move curves so that the first point is exactly on the surface mesh

                :param execution_context:
                :param undo:
                :param attach_mode: Attach Mode, How to find the point on the surface to attach to (optional)

        NEAREST
        Nearest -- Find the closest point on the surface for the root point of every curve and move the root there.

        DEFORM
        Deform -- Re-attach curves to a deformed surface using the existing attachment information. This only works when the topology of the surface mesh has not changed.
                :return: Result of the operator call.
        """

class split(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Split selected points

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class subdivide(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        number_cuts: int | None = 1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Subdivide selected curve segments

        :param execution_context:
        :param undo:
        :param number_cuts: Number of Cuts, (in [1, 1000], optional)
        :return: Result of the operator call.
        """

class surface_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Use the active object as surface for selected curves objects and set it as the parent

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class switch_direction(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reverse the direction of the selected curves

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class tilt_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear the tilt of selected control points

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
