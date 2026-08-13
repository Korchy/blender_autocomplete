import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

class cyclic_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal["CYCLIC_U", "CYCLIC_V"] | None = "CYCLIC_U",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make active spline closed/open loop

        :param execution_context:
        :param undo:
        :param direction: Direction, Direction to make surface cyclic in (optional)
        :return: Result of the operator call.
        """

class de_select_first(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """(De)select first of visible part of each NURBS

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class de_select_last(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """(De)select last of visible part of each NURBS

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class decimate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        ratio: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Simplify selected curves

        :param execution_context:
        :param undo:
        :param ratio: Ratio, (in [0, 1], optional)
        :return: Result of the operator call.
        """

class delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["VERT", "SEGMENT"] | None = "VERT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete selected control points or segments

        :param execution_context:
        :param undo:
        :param type: Type, Which elements to delete (optional)
        :return: Result of the operator call.
        """

class dissolve_verts(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete selected control points, correcting surrounding handles

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
        stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
        | None = None,
        wait_for_input: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Draw a freehand spline

        :param execution_context:
        :param undo:
        :param error_threshold: Error, Error distance threshold (in object units) (in [0, 10], optional)
        :param fit_method: Fit Method, (optional)
        :param corner_angle: Corner Angle, (in [0, 3.14159], optional)
        :param use_cyclic: Cyclic, (optional)
        :param stroke: Stroke, (optional)
        :param wait_for_input: Wait for Input, (optional)
        :return: Result of the operator call.
        """

class duplicate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate selected control points

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
        CURVE_OT_duplicate: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate curve and move

        :param execution_context:
        :param undo:
        :param CURVE_OT_duplicate: Duplicate Curve, Duplicate selected control points (optional, `bpy.ops.curve.duplicate` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class extrude(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal[bpy.stub_internal.rna_enums.TransformModeTypeItems]
        | None = "TRANSLATION",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude selected control point(s)

        :param execution_context:
        :param undo:
        :param mode: Mode, (optional)
        :return: Result of the operator call.
        """

class extrude_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        CURVE_OT_extrude: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude curve and move result

        :param execution_context:
        :param undo:
        :param CURVE_OT_extrude: Extrude, Extrude selected control point(s) (optional, `bpy.ops.curve.extrude` keyword arguments)
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
            "AUTOMATIC", "VECTOR", "ALIGNED", "FREE_ALIGN", "TOGGLE_FREE_ALIGN"
        ]
        | None = "AUTOMATIC",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set type of handles for selected control points

        :param execution_context:
        :param undo:
        :param type: Type, Spline type (optional)
        :return: Result of the operator call.
        """

class hide(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        unselected: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Hide (un)selected control points

        :param execution_context:
        :param undo:
        :param unselected: Unselected, Hide unselected rather than selected (optional)
        :return: Result of the operator call.
        """

class make_segment(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Join two curves by their selected ends

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class match_texture_space(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Match texture space to objects bounding box

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class normals_make_consistent(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        calc_length: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Recalculate the direction of selected handles

        :param execution_context:
        :param undo:
        :param calc_length: Length, Recalculate handle length (optional)
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
        close_spline: bool | None = True,
        close_spline_method: typing.Literal["OFF", "ON_PRESS", "ON_CLICK"]
        | None = "OFF",
        toggle_vector: bool | None = False,
        cycle_handle_type: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Construct and edit splines

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
                :param close_spline: Close Spline, Make a spline cyclic by clicking endpoints (optional)
                :param close_spline_method: Close Spline Method, The condition for close spline to activate (optional)

        OFF
        None.

        ON_PRESS
        On Press -- Move handles after closing the spline.

        ON_CLICK
        On Click -- Spline closes on release if not dragged.
                :param toggle_vector: Toggle Vector, Toggle between Vector and Auto handles (optional)
                :param cycle_handle_type: Cycle Handle Type, Cycle between all four handle types (optional)
                :return: Result of the operator call.
        """

class primitive_bezier_circle_add(bpy.ops._BPyOpsSubModOp):
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
        """Construct a Bézier Circle

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

class primitive_bezier_curve_add(bpy.ops._BPyOpsSubModOp):
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
        """Construct a Bézier Curve

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

class primitive_nurbs_circle_add(bpy.ops._BPyOpsSubModOp):
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
        """Construct a Nurbs Circle

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

class primitive_nurbs_curve_add(bpy.ops._BPyOpsSubModOp):
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
        """Construct a Nurbs Curve

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

class primitive_nurbs_path_add(bpy.ops._BPyOpsSubModOp):
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
        """Construct a Path

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

class radius_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        radius: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set per-point radius which is used for bevel tapering

        :param execution_context:
        :param undo:
        :param radius: Radius, (in [0, inf], optional)
        :return: Result of the operator call.
        """

class reveal(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        select: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reveal hidden control points

        :param execution_context:
        :param undo:
        :param select: Select, (optional)
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

class select_less(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Deselect control points at the boundary of each selection region

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
        """Select all control points linked to the current selection

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
        """Select all control points linked to already selected ones

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
        """Select control points at the boundary of each selection region

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_next(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select control points following already selected ones along the curves

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_nth(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        skip: int | None = 1,
        nth: int | None = 1,
        offset: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Deselect every Nth point starting from the active one

        :param execution_context:
        :param undo:
        :param skip: Deselected, Number of deselected elements in the repetitive sequence (in [1, inf], optional)
        :param nth: Selected, Number of selected elements in the repetitive sequence (in [1, inf], optional)
        :param offset: Offset, Offset from the starting point (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class select_previous(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select control points preceding already selected ones along the curves

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
        ratio: float | None = 0.5,
        seed: int | None = 0,
        action: typing.Literal["SELECT", "DESELECT"] | None = "SELECT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Randomly select some control points

                :param execution_context:
                :param undo:
                :param ratio: Ratio, Portion of items to select randomly (in [0, 1], optional)
                :param seed: Random Seed, Seed for the random number generator (in [0, inf], optional)
                :param action: Action, Selection action to execute (optional)

        SELECT
        Select -- Select all elements.

        DESELECT
        Deselect -- Deselect all elements.
                :return: Result of the operator call.
        """

class select_row(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select a row of control points including active one. Successive use on the same point switches between U/V directions

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_similar(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["TYPE", "RADIUS", "WEIGHT", "DIRECTION"] | None = "WEIGHT",
        compare: typing.Literal["EQUAL", "GREATER", "LESS"] | None = "EQUAL",
        threshold: float | None = 0.1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select similar curve points by property type

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :param compare: Compare, (optional)
        :param threshold: Threshold, (in [0, inf], optional)
        :return: Result of the operator call.
        """

class separate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Separate selected points from connected unselected points into a new object

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class shade_flat(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set shading to flat

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class shade_smooth(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set shading to smooth

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class shortest_path_pick(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select shortest path between two selections

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class smooth(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Flatten angles of selected points

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class smooth_radius(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Interpolate radii of selected points

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class smooth_tilt(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Interpolate tilt of selected points

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class smooth_weight(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Interpolate weight of selected points

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class spin(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        center: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
        axis: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude selected boundary row around pivot point and current view axis

        :param execution_context:
        :param undo:
        :param center: Center, Center in global view space (array of 3 items, in [-inf, inf], optional)
        :param axis: Axis, Axis in global view space (array of 3 items, in [-1, 1], optional)
        :return: Result of the operator call.
        """

class spline_type_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["POLY", "BEZIER", "NURBS"] | None = "POLY",
        use_handles: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set type of active spline

        :param execution_context:
        :param undo:
        :param type: Type, Spline type (optional)
        :param use_handles: Handles, Use handles when converting Bézier curves into polygons (optional)
        :return: Result of the operator call.
        """

class spline_weight_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        weight: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set softbody goal weight for selected points

        :param execution_context:
        :param undo:
        :param weight: Weight, (in [0, 1], optional)
        :return: Result of the operator call.
        """

class split(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Split off selected points from connected unselected points

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
        """Subdivide selected segments

        :param execution_context:
        :param undo:
        :param number_cuts: Number of Cuts, (in [1, 1000], optional)
        :return: Result of the operator call.
        """

class switch_direction(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Switch direction of selected splines

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

class vertex_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        location: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a new control point (linked to only selected end-curve one, if any)

        :param execution_context:
        :param undo:
        :param location: Location, Location to add new vertex at (array of 3 items, in [-inf, inf], optional)
        :return: Result of the operator call.
        """
