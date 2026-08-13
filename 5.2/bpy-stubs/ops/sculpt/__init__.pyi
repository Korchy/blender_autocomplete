import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

class brush_stroke(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        stroke: None
        | bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
        | None = None,
        mode: typing.Literal["NORMAL", "INVERT"] | None = "NORMAL",
        brush_toggle: typing.Literal["None", "SMOOTH", "ERASE", "MASK"] | None = "None",
        pen_flip: bool | None = False,
        override_location: bool | None = False,
        ignore_background_click: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Sculpt a stroke into the geometry

                :param execution_context:
                :param undo:
                :param stroke: Stroke, (optional)
                :param mode: Stroke Mode, Action taken when a paint stroke is made (optional)

        NORMAL
        Regular -- Apply brush normally.

        INVERT
        Invert -- Invert action of brush for duration of stroke.
                :param brush_toggle: Temporary Brush Toggle Type, Brush to use for duration of stroke (optional)

        None
        None -- Apply brush normally.

        SMOOTH
        Smooth -- Switch to smooth brush for duration of stroke.

        ERASE
        Erase -- Switch to erase brush for duration of stroke.

        MASK
        Mask -- Switch to mask brush for duration of stroke.
                :param pen_flip: Pen Flip, Whether a tablets eraser mode is being used (optional)
                :param override_location: Override Location, Override the given "location" array by recalculating object space positions from the provided "mouse_event" positions (optional)
                :param ignore_background_click: Ignore Background Click, Clicks on the background do not start the stroke (optional)
                :return: Result of the operator call.
        """

class cloth_filter(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        start_mouse: collections.abc.Sequence[int] | None = (0, 0),
        area_normal_radius: float | None = 0.25,
        strength: float | None = 1.0,
        iteration_count: int | None = 1,
        event_history: None
        | bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
        | None = None,
        type: typing.Literal["GRAVITY", "INFLATE", "EXPAND", "PINCH", "SCALE"]
        | None = "GRAVITY",
        force_axis: set[typing.Literal["X", "Y", "Z"]] | None = {"X", "Y", "Z"},
        orientation: typing.Literal["LOCAL", "WORLD", "VIEW"] | None = "LOCAL",
        cloth_mass: float | None = 1.0,
        cloth_damping: float | None = 0.0,
        use_face_sets: bool | None = False,
        use_collisions: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Applies a cloth simulation deformation to the entire mesh

                :param execution_context:
                :param undo:
                :param start_mouse: Starting Mouse, (array of 2 items, in [0, 16384], optional)
                :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius(in [0.001, 5], optional)
                :param strength: Strength, Filter strength (in [-10, 10], optional)
                :param iteration_count: Repeat, How many times to repeat the filter (in [1, 10000], optional)
                :param event_history: (optional)
                :param type: Filter Type, Operation that is going to be applied to the mesh (optional)

        GRAVITY
        Gravity -- Applies gravity to the simulation.

        INFLATE
        Inflate -- Inflates the cloth.

        EXPAND
        Expand -- Expands the cloths dimensions.

        PINCH
        Pinch -- Pulls the cloth to the cursors start position.

        SCALE
        Scale -- Scales the mesh as a soft body using the origin of the object as scale.
                :param force_axis: Force Axis, Apply the force in the selected axis (optional)

        X
        X -- Apply force in the X axis.

        Y
        Y -- Apply force in the Y axis.

        Z
        Z -- Apply force in the Z axis.
                :param orientation: Orientation, Orientation of the axis to limit the filter force (optional)

        LOCAL
        Local -- Use the local axis to limit the force and set the gravity direction.

        WORLD
        World -- Use the global axis to limit the force and set the gravity direction.

        VIEW
        View -- Use the view axis to limit the force and set the gravity direction.
                :param cloth_mass: Cloth Mass, Mass of each simulation particle (in [0, 2], optional)
                :param cloth_damping: Cloth Damping, How much the applied forces are propagated through the cloth (in [0, 1], optional)
                :param use_face_sets: Use Face Sets, Apply the filter only to the face set under the cursor (optional)
                :param use_collisions: Use Collisions, Collide with other collider objects in the scene (optional)
                :return: Result of the operator call.
        """

class color_filter(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        start_mouse: collections.abc.Sequence[int] | None = (0, 0),
        area_normal_radius: float | None = 0.25,
        strength: float | None = 1.0,
        iteration_count: int | None = 1,
        event_history: None
        | bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
        | None = None,
        type: typing.Literal[
            "FILL",
            "HUE",
            "SATURATION",
            "VALUE",
            "BRIGHTNESS",
            "CONTRAST",
            "SMOOTH",
            "RED",
            "GREEN",
            "BLUE",
        ]
        | None = "FILL",
        fill_color: collections.abc.Sequence[float] | mathutils.Color | None = (
            1.0,
            1.0,
            1.0,
        ),
        use_immediate: bool | None = False,
        use_secondary_color: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Applies a filter to modify the active color attribute

                :param execution_context:
                :param undo:
                :param start_mouse: Starting Mouse, (array of 2 items, in [0, 16384], optional)
                :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius(in [0.001, 5], optional)
                :param strength: Strength, Filter strength (in [-10, 10], optional)
                :param iteration_count: Repeat, How many times to repeat the filter (in [1, 10000], optional)
                :param event_history: (optional)
                :param type: Filter Type, (optional)

        FILL
        Fill -- Fill with a specific color.

        HUE
        Hue -- Change hue.

        SATURATION
        Saturation -- Change saturation.

        VALUE
        Value -- Change value.

        BRIGHTNESS
        Brightness -- Change brightness.

        CONTRAST
        Contrast -- Change contrast.

        SMOOTH
        Smooth -- Smooth colors.

        RED
        Red -- Change red channel.

        GREEN
        Green -- Change green channel.

        BLUE
        Blue -- Change blue channel.
                :param fill_color: Fill Color, (array of 3 items, in [0, inf], optional)
                :param use_immediate: Immediate Apply, Apply once without entering modal interaction (optional)
                :param use_secondary_color: Use Secondary Color, (optional)
                :return: Result of the operator call.
        """

class detail_flood_fill(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Flood fill the mesh with the selected detail setting

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class dynamic_topology_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Dynamic topology alters the mesh topology while sculpting

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class dyntopo_detail_size_edit(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Modify the detail size of dyntopo interactively

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class expand(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        target: typing.Literal["MASK", "FACE_SETS", "COLOR"] | None = "MASK",
        falloff_type: typing.Literal[
            "GEODESIC",
            "TOPOLOGY",
            "TOPOLOGY_DIAGONALS",
            "NORMALS",
            "SPHERICAL",
            "BOUNDARY_TOPOLOGY",
            "BOUNDARY_FACE_SET",
            "ACTIVE_FACE_SET",
        ]
        | None = "GEODESIC",
        invert: bool | None = False,
        use_mask_preserve: bool | None = False,
        use_falloff_gradient: bool | None = False,
        use_modify_active: bool | None = False,
        use_reposition_pivot: bool | None = True,
        max_geodesic_move_preview: int | None = 10000,
        use_auto_mask: bool | None = False,
        normal_falloff_smooth: int | None = 2,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Generic sculpt expand operator

        :param execution_context:
        :param undo:
        :param target: Data Target, Data that is going to be modified in the expand operation (optional)
        :param falloff_type: Falloff Type, Initial falloff of the expand operation (optional)
        :param invert: Invert, Invert the expand active elements (optional)
        :param use_mask_preserve: Preserve Previous, Preserve the previous state of the target data (optional)
        :param use_falloff_gradient: Falloff Gradient, Expand Using a linear falloff (optional)
        :param use_modify_active: Modify Active, Modify the active face set instead of creating a new one (optional)
        :param use_reposition_pivot: Reposition Pivot, Reposition the sculpt transform pivot to the boundary of the expand active area (optional)
        :param max_geodesic_move_preview: Max Vertex Count for Geodesic Move Preview, Maximum number of vertices in the mesh for using geodesic falloff when moving the origin of expand. If the total number of vertices is greater than this value, the falloff will be set to spherical when moving (in [0, inf], optional)
        :param use_auto_mask: Auto Create, Fill in mask if nothing is already masked (optional)
        :param normal_falloff_smooth: Normal Smooth, Blurring steps for normal falloff (in [0, 10], optional)
        :return: Result of the operator call.
        """

class face_set_box_gesture(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        xmin: int | None = 0,
        xmax: int | None = 0,
        ymin: int | None = 0,
        ymax: int | None = 0,
        wait_for_input: bool | None = True,
        use_front_faces_only: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a face set in a rectangle defined by the cursor

        :param execution_context:
        :param undo:
        :param xmin: X Min, (in [-inf, inf], optional)
        :param xmax: X Max, (in [-inf, inf], optional)
        :param ymin: Y Min, (in [-inf, inf], optional)
        :param ymax: Y Max, (in [-inf, inf], optional)
        :param wait_for_input: Wait for Input, (optional)
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
        :return: Result of the operator call.
        """

class face_set_change_visibility(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["TOGGLE", "SHOW_ACTIVE", "HIDE_ACTIVE"] | None = "TOGGLE",
        active_face_set: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change the visibility of the face sets of the sculpt

                :param execution_context:
                :param undo:
                :param mode: Mode, (optional)

        TOGGLE
        Toggle Visibility -- Hide all face sets except for the active one.

        SHOW_ACTIVE
        Show Active Face Set -- Show the active face set.

        HIDE_ACTIVE
        Hide Active Face Set -- Hide the active face set.
                :param active_face_set: Active Face Set, (in [0, inf], optional)
                :return: Result of the operator call.
        """

class face_set_edit(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        active_face_set: int | None = 1,
        mode: typing.Literal[
            "GROW", "SHRINK", "DELETE_GEOMETRY", "FAIR_POSITIONS", "FAIR_TANGENCY"
        ]
        | None = "GROW",
        strength: float | None = 1.0,
        modify_hidden: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Edits the current active face set

                :param execution_context:
                :param undo:
                :param active_face_set: Active Face Set, (in [0, inf], optional)
                :param mode: Mode, (optional)

        GROW
        Grow Face Set -- Grows the face set boundary by one face based on mesh topology.

        SHRINK
        Shrink Face Set -- Shrinks the face set boundary by one face based on mesh topology.

        DELETE_GEOMETRY
        Delete Geometry -- Deletes the faces that are assigned to the face set.

        FAIR_POSITIONS
        Fair Positions -- Creates the smoothest possible geometry patch from the face set minimizing changes in vertex positions.

        FAIR_TANGENCY
        Fair Tangency -- Creates the smoothest possible geometry patch from the face set minimizing changes in vertex tangents.
                :param strength: Strength, (in [0, 1], optional)
                :param modify_hidden: Modify Hidden, Apply the edit operation to hidden geometry (optional)
                :return: Result of the operator call.
        """

class face_set_extract(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        add_boundary_loop: bool | None = True,
        smooth_iterations: int | None = 4,
        apply_shrinkwrap: bool | None = True,
        add_solidify: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a new mesh object from the selected face set

        :param execution_context:
        :param undo:
        :param add_boundary_loop: Add Boundary Loop, Add an extra edge loop to better preserve the shape when applying a subdivision surface modifier (optional)
        :param smooth_iterations: Smooth Iterations, Smooth iterations applied to the extracted mesh (in [0, inf], optional)
        :param apply_shrinkwrap: Project to Sculpt, Project the extracted mesh into the original sculpt (optional)
        :param add_solidify: Extract as Solid, Extract the mask as a solid object with a solidify modifier (optional)
        :return: Result of the operator call.
        """

class face_set_lasso_gesture(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        path: None
        | bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath]
        | None = None,
        use_smooth_stroke: bool | None = False,
        smooth_stroke_factor: float | None = 0.75,
        smooth_stroke_radius: int | None = 35,
        use_front_faces_only: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a face set in a shape defined by the cursor

        :param execution_context:
        :param undo:
        :param path: Path, (optional)
        :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path (optional)
        :param smooth_stroke_factor: Smooth Stroke Factor, Higher values give a smoother stroke (in [0.5, 0.99], optional)
        :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues (in [10, 200], optional)
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
        :return: Result of the operator call.
        """

class face_set_line_gesture(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        xstart: int | None = 0,
        xend: int | None = 0,
        ystart: int | None = 0,
        yend: int | None = 0,
        flip: bool | None = False,
        cursor: int | None = 5,
        use_front_faces_only: bool | None = False,
        use_limit_to_segment: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a face set to one side of a line defined by the cursor

        :param execution_context:
        :param undo:
        :param xstart: X Start, (in [-inf, inf], optional)
        :param xend: X End, (in [-inf, inf], optional)
        :param ystart: Y Start, (in [-inf, inf], optional)
        :param yend: Y End, (in [-inf, inf], optional)
        :param flip: Flip, (optional)
        :param cursor: Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
        :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line (optional)
        :return: Result of the operator call.
        """

class face_set_polyline_gesture(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        path: None
        | bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath]
        | None = None,
        use_front_faces_only: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a face set in a shape defined by the cursor

        :param execution_context:
        :param undo:
        :param path: Path, (optional)
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
        :return: Result of the operator call.
        """

class face_sets_create(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["MASKED", "VISIBLE", "ALL", "SELECTION"] | None = "MASKED",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a new face set

                :param execution_context:
                :param undo:
                :param mode: Mode, (optional)

        MASKED
        Face Set from Masked -- Create a new face set from the masked faces.

        VISIBLE
        Face Set from Visible -- Create a new face set from the visible vertices.

        ALL
        Face Set Full Mesh -- Create a unique face set with all faces in the sculpt.

        SELECTION
        Face Set from Edit Mode Selection -- Create a face set corresponding to the Edit Mode face selection.
                :return: Result of the operator call.
        """

class face_sets_init(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal[
            "LOOSE_PARTS",
            "MATERIALS",
            "NORMALS",
            "UV_SEAMS",
            "CREASES",
            "BEVEL_WEIGHT",
            "SHARP_EDGES",
            "FACE_SET_BOUNDARIES",
        ]
        | None = "LOOSE_PARTS",
        threshold: float | None = 0.5,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Initializes all face sets in the mesh

                :param execution_context:
                :param undo:
                :param mode: Mode, (optional)

        LOOSE_PARTS
        Face Sets from Loose Parts -- Create a face set per loose part in the mesh.

        MATERIALS
        Face Sets from Material Slots -- Create a face set per material slot.

        NORMALS
        Face Sets from Mesh Normals -- Create face sets for faces that have similar normal.

        UV_SEAMS
        Face Sets from UV Seams -- Create face sets using UV seams as boundaries.

        CREASES
        Face Sets from Edge Creases -- Create face sets using edge creases as boundaries.

        BEVEL_WEIGHT
        Face Sets from Bevel Weight -- Create face sets using bevel weights as boundaries.

        SHARP_EDGES
        Face Sets from Sharp Edges -- Create face sets using sharp edges as boundaries.

        FACE_SET_BOUNDARIES
        Face Sets from Face Set Boundaries -- Create a face set per isolated face set.
                :param threshold: Threshold, Minimum value to consider a certain attribute a boundary when creating the face sets (in [0, 1], optional)
                :return: Result of the operator call.
        """

class face_sets_randomize_colors(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Generates a new set of random colors to render the face sets in the viewport

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class mask_by_color(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        contiguous: bool | None = False,
        invert: bool | None = False,
        preserve_previous_mask: bool | None = False,
        threshold: float | None = 0.35,
        location: collections.abc.Sequence[int] | None = (0, 0),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Creates a mask based on the active color attribute

        :param execution_context:
        :param undo:
        :param contiguous: Contiguous, Mask only contiguous color areas (optional)
        :param invert: Invert, Invert the generated mask (optional)
        :param preserve_previous_mask: Preserve Previous Mask, Preserve the previous mask and add or subtract the new one generated by the colors (optional)
        :param threshold: Threshold, How much changes in color affect the mask generation (in [0, 1], optional)
        :param location: Location, Region coordinates of sampling (array of 2 items, in [0, 32767], optional)
        :return: Result of the operator call.
        """

class mask_filter(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filter_type: typing.Literal[
            "SMOOTH",
            "SHARPEN",
            "GROW",
            "SHRINK",
            "CONTRAST_INCREASE",
            "CONTRAST_DECREASE",
        ]
        | None = "SMOOTH",
        iterations: int | None = 1,
        auto_iteration_count: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Applies a filter to modify the current mask

        :param execution_context:
        :param undo:
        :param filter_type: Type, Filter that is going to be applied to the mask (optional)
        :param iterations: Iterations, Number of times that the filter is going to be applied (in [1, 100], optional)
        :param auto_iteration_count: Auto Iteration Count, Use an automatic number of iterations based on the number of vertices of the sculpt (optional)
        :return: Result of the operator call.
        """

class mask_from_boundary(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mix_mode: typing.Literal["MIX", "MULTIPLY", "DIVIDE", "ADD", "SUBTRACT"]
        | None = "MIX",
        mix_factor: float | None = 1.0,
        settings_source: typing.Literal["OPERATOR", "BRUSH", "SCENE"]
        | None = "OPERATOR",
        boundary_mode: typing.Literal["MESH", "FACE_SETS"] | None = "MESH",
        propagation_steps: int | None = 1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Creates a mask based on the boundaries of the surface

                :param execution_context:
                :param undo:
                :param mix_mode: Mode, Mix mode (optional)
                :param mix_factor: Mix Factor, (in [0, 5], optional)
                :param settings_source: Settings, Use settings from here (optional)

        OPERATOR
        Operator -- Use settings from operator properties.

        BRUSH
        Brush -- Use settings from brush.

        SCENE
        Scene -- Use settings from scene.
                :param boundary_mode: Mode, Boundary type to mask (optional)

        MESH
        Mesh -- Calculate the boundary mask based on disconnected mesh topology islands.

        FACE_SETS
        Face Sets -- Calculate the boundary mask between face sets.
                :param propagation_steps: Propagation Steps, (in [1, 20], optional)
                :return: Result of the operator call.
        """

class mask_from_cavity(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mix_mode: typing.Literal["MIX", "MULTIPLY", "DIVIDE", "ADD", "SUBTRACT"]
        | None = "MIX",
        mix_factor: float | None = 1.0,
        settings_source: typing.Literal["OPERATOR", "BRUSH", "SCENE"]
        | None = "OPERATOR",
        factor: float | None = 0.5,
        blur_steps: int | None = 2,
        use_curve: bool | None = False,
        invert: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Creates a mask based on the curvature of the surface

                :param execution_context:
                :param undo:
                :param mix_mode: Mode, Mix mode (optional)
                :param mix_factor: Mix Factor, (in [0, 5], optional)
                :param settings_source: Settings, Use settings from here (optional)

        OPERATOR
        Operator -- Use settings from operator properties.

        BRUSH
        Brush -- Use settings from brush.

        SCENE
        Scene -- Use settings from scene.
                :param factor: Factor, The contrast of the cavity mask (in [0, 5], optional)
                :param blur_steps: Blur, The number of times the cavity mask is blurred (in [0, 25], optional)
                :param use_curve: Custom Curve, (optional)
                :param invert: Cavity (Inverted), (optional)
                :return: Result of the operator call.
        """

class mask_init(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal[
            "RANDOM_PER_VERTEX", "RANDOM_PER_FACE_SET", "RANDOM_PER_LOOSE_PART"
        ]
        | None = "RANDOM_PER_VERTEX",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Creates a new mask for the entire mesh

        :param execution_context:
        :param undo:
        :param mode: Mode, (optional)
        :return: Result of the operator call.
        """

class mesh_filter(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        start_mouse: collections.abc.Sequence[int] | None = (0, 0),
        area_normal_radius: float | None = 0.25,
        strength: float | None = 1.0,
        iteration_count: int | None = 1,
        event_history: None
        | bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
        | None = None,
        type: typing.Literal[
            "SMOOTH",
            "SCALE",
            "INFLATE",
            "SPHERE",
            "RANDOM",
            "RELAX",
            "RELAX_FACE_SETS",
            "SURFACE_SMOOTH",
            "SHARPEN",
            "ENHANCE_DETAILS",
            "ERASE_DISPLACEMENT",
        ]
        | None = "INFLATE",
        deform_axis: set[typing.Literal["X", "Y", "Z"]] | None = {"X", "Y", "Z"},
        orientation: typing.Literal["LOCAL", "WORLD", "VIEW"] | None = "LOCAL",
        surface_smooth_shape_preservation: float | None = 0.5,
        surface_smooth_current_vertex: float | None = 0.5,
        sharpen_smooth_ratio: float | None = 0.35,
        sharpen_intensify_detail_strength: float | None = 0.0,
        sharpen_curvature_smooth_iterations: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Applies a filter to modify the current mesh

                :param execution_context:
                :param undo:
                :param start_mouse: Starting Mouse, (array of 2 items, in [0, 16384], optional)
                :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius(in [0.001, 5], optional)
                :param strength: Strength, Filter strength (in [-10, 10], optional)
                :param iteration_count: Repeat, How many times to repeat the filter (in [1, 10000], optional)
                :param event_history: (optional)
                :param type: Filter Type, Operation that is going to be applied to the mesh (optional)

        SMOOTH
        Smooth -- Smooth mesh.

        SCALE
        Scale -- Scale mesh.

        INFLATE
        Inflate -- Inflate mesh.

        SPHERE
        Sphere -- Morph into sphere.

        RANDOM
        Random -- Randomize vertex positions.

        RELAX
        Relax -- Relax mesh.

        RELAX_FACE_SETS
        Relax Face Sets -- Smooth the edges of all the face sets.

        SURFACE_SMOOTH
        Surface Smooth -- Smooth the surface of the mesh, preserving the volume.

        SHARPEN
        Sharpen -- Sharpen the cavities of the mesh.

        ENHANCE_DETAILS
        Enhance Details -- Enhance the high frequency surface detail.

        ERASE_DISPLACEMENT
        Erase Displacement -- Deletes the displacement of the Multires Modifier.
                :param deform_axis: Deform Axis, Apply the deformation in the selected axis (optional)

        X
        X -- Deform in the X axis.

        Y
        Y -- Deform in the Y axis.

        Z
        Z -- Deform in the Z axis.
                :param orientation: Orientation, Orientation of the axis to limit the filter displacement (optional)

        LOCAL
        Local -- Use the local axis to limit the displacement.

        WORLD
        World -- Use the global axis to limit the displacement.

        VIEW
        View -- Use the view axis to limit the displacement.
                :param surface_smooth_shape_preservation: Shape Preservation, How much of the original shape is preserved when smoothing (in [0, 1], optional)
                :param surface_smooth_current_vertex: Per Vertex Displacement, How much the position of each individual vertex influences the final result (in [0, 1], optional)
                :param sharpen_smooth_ratio: Smooth Ratio, How much smoothing is applied to polished surfaces (in [0, 1], optional)
                :param sharpen_intensify_detail_strength: Intensify Details, How much creases and valleys are intensified (in [0, 10], optional)
                :param sharpen_curvature_smooth_iterations: Curvature Smooth Iterations, How much smooth the resulting shape is, ignoring high frequency details (in [0, 10], optional)
                :return: Result of the operator call.
        """

class optimize(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Recalculate the sculpt BVH to improve performance

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class paint_mask_extract(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mask_threshold: float | None = 0.5,
        add_boundary_loop: bool | None = True,
        smooth_iterations: int | None = 4,
        apply_shrinkwrap: bool | None = True,
        add_solidify: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a new mesh object from the current paint mask

        :param execution_context:
        :param undo:
        :param mask_threshold: Threshold, Minimum mask value to consider the vertex valid to extract a face from the original mesh (in [0, 1], optional)
        :param add_boundary_loop: Add Boundary Loop, Add an extra edge loop to better preserve the shape when applying a subdivision surface modifier (optional)
        :param smooth_iterations: Smooth Iterations, Smooth iterations applied to the extracted mesh (in [0, inf], optional)
        :param apply_shrinkwrap: Project to Sculpt, Project the extracted mesh into the original sculpt (optional)
        :param add_solidify: Extract as Solid, Extract the mask as a solid object with a solidify modifier (optional)
        :return: Result of the operator call.
        """

class paint_mask_slice(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mask_threshold: float | None = 0.5,
        fill_holes: bool | None = True,
        new_object: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Slices the paint mask from the mesh

        :param execution_context:
        :param undo:
        :param mask_threshold: Threshold, Minimum mask value to consider the vertex valid to extract a face from the original mesh (in [0, 1], optional)
        :param fill_holes: Fill Holes, Fill holes after slicing the mask (optional)
        :param new_object: Slice to New Object, Create a new object from the sliced mask (optional)
        :return: Result of the operator call.
        """

class project_line_gesture(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        xstart: int | None = 0,
        xend: int | None = 0,
        ystart: int | None = 0,
        yend: int | None = 0,
        flip: bool | None = False,
        cursor: int | None = 5,
        use_front_faces_only: bool | None = False,
        use_limit_to_segment: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Project the geometry onto a plane defined by a line

        :param execution_context:
        :param undo:
        :param xstart: X Start, (in [-inf, inf], optional)
        :param xend: X End, (in [-inf, inf], optional)
        :param ystart: Y Start, (in [-inf, inf], optional)
        :param yend: Y End, (in [-inf, inf], optional)
        :param flip: Flip, (optional)
        :param cursor: Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
        :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line (optional)
        :return: Result of the operator call.
        """

class sample_detail_size(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        location: collections.abc.Sequence[int] | None = (0, 0),
        mode: typing.Literal["DYNTOPO", "VOXEL"] | None = "DYNTOPO",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Sample the mesh detail on clicked point

                :param execution_context:
                :param undo:
                :param location: Location, Screen coordinates of sampling (array of 2 items, in [0, 32767], optional)
                :param mode: Detail Mode, Target sculpting workflow that is going to use the sampled size (optional)

        DYNTOPO
        Dyntopo -- Sample dyntopo detail.

        VOXEL
        Voxel -- Sample mesh voxel size.
                :return: Result of the operator call.
        """

class sculptmode_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Toggle sculpt mode in 3D view

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class set_persistent_base(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset the copy of the mesh that is being sculpted on

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class set_pivot_position(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["ORIGIN", "UNMASKED", "BORDER", "ACTIVE", "SURFACE"]
        | None = "UNMASKED",
        mouse_x: float | None = 0.0,
        mouse_y: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Sets the sculpt transform pivot position

                :param execution_context:
                :param undo:
                :param mode: Mode, (optional)

        ORIGIN
        Origin -- Sets the pivot to the origin of the sculpt.

        UNMASKED
        Unmasked -- Sets the pivot position to the average position of the unmasked vertices.

        BORDER
        Mask Border -- Sets the pivot position to the center of the border of the mask.

        ACTIVE
        Active Vertex -- Sets the pivot position to the active vertex position.

        SURFACE
        Surface -- Sets the pivot position to the surface under the cursor.
                :param mouse_x: Mouse Position X, Position of the mouse used for "Surface" and "Active Vertex" mode (in [0, inf], optional)
                :param mouse_y: Mouse Position Y, Position of the mouse used for "Surface" and "Active Vertex" mode (in [0, inf], optional)
                :return: Result of the operator call.
        """

class symmetrize(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        merge_tolerance: float | None = 0.0005,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Symmetrize the topology modifications

        :param execution_context:
        :param undo:
        :param merge_tolerance: Merge Distance, Distance within which symmetrical vertices are merged (in [0, inf], optional)
        :return: Result of the operator call.
        """

class trim_box_gesture(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        xmin: int | None = 0,
        xmax: int | None = 0,
        ymin: int | None = 0,
        ymax: int | None = 0,
        wait_for_input: bool | None = True,
        use_front_faces_only: bool | None = False,
        location: collections.abc.Sequence[int] | None = (0, 0),
        trim_mode: typing.Literal["DIFFERENCE", "UNION", "JOIN"] | None = "DIFFERENCE",
        use_cursor_depth: bool | None = False,
        trim_orientation: typing.Literal["VIEW", "SURFACE"] | None = "VIEW",
        trim_extrude_mode: typing.Literal["PROJECT", "FIXED"] | None = "FIXED",
        trim_solver: typing.Literal["EXACT", "FLOAT", "MANIFOLD"] | None = "MANIFOLD",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Execute a boolean operation on the mesh and a rectangle defined by the cursor

                :param execution_context:
                :param undo:
                :param xmin: X Min, (in [-inf, inf], optional)
                :param xmax: X Max, (in [-inf, inf], optional)
                :param ymin: Y Min, (in [-inf, inf], optional)
                :param ymax: Y Max, (in [-inf, inf], optional)
                :param wait_for_input: Wait for Input, (optional)
                :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
                :param location: Location, Mouse location (array of 2 items, in [-inf, inf], optional)
                :param trim_mode: Trim Mode, (optional)

        DIFFERENCE
        Difference -- Use a difference boolean operation.

        UNION
        Union -- Use a union boolean operation.

        JOIN
        Join -- Join the new mesh as separate geometry, without performing any boolean operation.
                :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape (optional)
                :param trim_orientation: Shape Orientation, (optional)

        VIEW
        View -- Use the view to orientate the trimming shape.

        SURFACE
        Surface -- Use the surface normal to orientate the trimming shape.
                :param trim_extrude_mode: Extrude Mode, (optional)

        PROJECT
        Project -- Align trim geometry with the perspective of the current view for a tapered shape.

        FIXED
        Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
                :param trim_solver: Solver, (optional)

        EXACT
        Exact -- Slower solver with the best results for coplanar faces.

        FLOAT
        Float -- Simple solver with good performance, without support for overlapping geometry.

        MANIFOLD
        Manifold -- Fastest solver that works only on manifold meshes but gives better results.
                :return: Result of the operator call.
        """

class trim_lasso_gesture(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        path: None
        | bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath]
        | None = None,
        use_smooth_stroke: bool | None = False,
        smooth_stroke_factor: float | None = 0.75,
        smooth_stroke_radius: int | None = 35,
        use_front_faces_only: bool | None = False,
        location: collections.abc.Sequence[int] | None = (0, 0),
        trim_mode: typing.Literal["DIFFERENCE", "UNION", "JOIN"] | None = "DIFFERENCE",
        use_cursor_depth: bool | None = False,
        trim_orientation: typing.Literal["VIEW", "SURFACE"] | None = "VIEW",
        trim_extrude_mode: typing.Literal["PROJECT", "FIXED"] | None = "FIXED",
        trim_solver: typing.Literal["EXACT", "FLOAT", "MANIFOLD"] | None = "MANIFOLD",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Execute a boolean operation on the mesh and a shape defined by the cursor

                :param execution_context:
                :param undo:
                :param path: Path, (optional)
                :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path (optional)
                :param smooth_stroke_factor: Smooth Stroke Factor, Higher values give a smoother stroke (in [0.5, 0.99], optional)
                :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues (in [10, 200], optional)
                :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
                :param location: Location, Mouse location (array of 2 items, in [-inf, inf], optional)
                :param trim_mode: Trim Mode, (optional)

        DIFFERENCE
        Difference -- Use a difference boolean operation.

        UNION
        Union -- Use a union boolean operation.

        JOIN
        Join -- Join the new mesh as separate geometry, without performing any boolean operation.
                :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape (optional)
                :param trim_orientation: Shape Orientation, (optional)

        VIEW
        View -- Use the view to orientate the trimming shape.

        SURFACE
        Surface -- Use the surface normal to orientate the trimming shape.
                :param trim_extrude_mode: Extrude Mode, (optional)

        PROJECT
        Project -- Align trim geometry with the perspective of the current view for a tapered shape.

        FIXED
        Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
                :param trim_solver: Solver, (optional)

        EXACT
        Exact -- Slower solver with the best results for coplanar faces.

        FLOAT
        Float -- Simple solver with good performance, without support for overlapping geometry.

        MANIFOLD
        Manifold -- Fastest solver that works only on manifold meshes but gives better results.
                :return: Result of the operator call.
        """

class trim_line_gesture(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        xstart: int | None = 0,
        xend: int | None = 0,
        ystart: int | None = 0,
        yend: int | None = 0,
        flip: bool | None = False,
        cursor: int | None = 5,
        use_front_faces_only: bool | None = False,
        use_limit_to_segment: bool | None = False,
        location: collections.abc.Sequence[int] | None = (0, 0),
        trim_mode: typing.Literal["DIFFERENCE", "UNION", "JOIN"] | None = "DIFFERENCE",
        use_cursor_depth: bool | None = False,
        trim_orientation: typing.Literal["VIEW", "SURFACE"] | None = "VIEW",
        trim_extrude_mode: typing.Literal["PROJECT", "FIXED"] | None = "FIXED",
        trim_solver: typing.Literal["EXACT", "FLOAT", "MANIFOLD"] | None = "MANIFOLD",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove a portion of the mesh on one side of a line

                :param execution_context:
                :param undo:
                :param xstart: X Start, (in [-inf, inf], optional)
                :param xend: X End, (in [-inf, inf], optional)
                :param ystart: Y Start, (in [-inf, inf], optional)
                :param yend: Y End, (in [-inf, inf], optional)
                :param flip: Flip, (optional)
                :param cursor: Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)
                :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
                :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line (optional)
                :param location: Location, Mouse location (array of 2 items, in [-inf, inf], optional)
                :param trim_mode: Trim Mode, (optional)

        DIFFERENCE
        Difference -- Use a difference boolean operation.

        UNION
        Union -- Use a union boolean operation.

        JOIN
        Join -- Join the new mesh as separate geometry, without performing any boolean operation.
                :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape (optional)
                :param trim_orientation: Shape Orientation, (optional)

        VIEW
        View -- Use the view to orientate the trimming shape.

        SURFACE
        Surface -- Use the surface normal to orientate the trimming shape.
                :param trim_extrude_mode: Extrude Mode, (optional)

        PROJECT
        Project -- Align trim geometry with the perspective of the current view for a tapered shape.

        FIXED
        Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
                :param trim_solver: Solver, (optional)

        EXACT
        Exact -- Slower solver with the best results for coplanar faces.

        FLOAT
        Float -- Simple solver with good performance, without support for overlapping geometry.

        MANIFOLD
        Manifold -- Fastest solver that works only on manifold meshes but gives better results.
                :return: Result of the operator call.
        """

class trim_polyline_gesture(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        path: None
        | bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath]
        | None = None,
        use_front_faces_only: bool | None = False,
        location: collections.abc.Sequence[int] | None = (0, 0),
        trim_mode: typing.Literal["DIFFERENCE", "UNION", "JOIN"] | None = "DIFFERENCE",
        use_cursor_depth: bool | None = False,
        trim_orientation: typing.Literal["VIEW", "SURFACE"] | None = "VIEW",
        trim_extrude_mode: typing.Literal["PROJECT", "FIXED"] | None = "FIXED",
        trim_solver: typing.Literal["EXACT", "FLOAT", "MANIFOLD"] | None = "MANIFOLD",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Execute a boolean operation on the mesh and a polygonal shape defined by the cursor

                :param execution_context:
                :param undo:
                :param path: Path, (optional)
                :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
                :param location: Location, Mouse location (array of 2 items, in [-inf, inf], optional)
                :param trim_mode: Trim Mode, (optional)

        DIFFERENCE
        Difference -- Use a difference boolean operation.

        UNION
        Union -- Use a union boolean operation.

        JOIN
        Join -- Join the new mesh as separate geometry, without performing any boolean operation.
                :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape (optional)
                :param trim_orientation: Shape Orientation, (optional)

        VIEW
        View -- Use the view to orientate the trimming shape.

        SURFACE
        Surface -- Use the surface normal to orientate the trimming shape.
                :param trim_extrude_mode: Extrude Mode, (optional)

        PROJECT
        Project -- Align trim geometry with the perspective of the current view for a tapered shape.

        FIXED
        Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
                :param trim_solver: Solver, (optional)

        EXACT
        Exact -- Slower solver with the best results for coplanar faces.

        FLOAT
        Float -- Simple solver with good performance, without support for overlapping geometry.

        MANIFOLD
        Manifold -- Fastest solver that works only on manifold meshes but gives better results.
                :return: Result of the operator call.
        """

class uv_sculpt_grab(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_invert: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Grab UVs

        :param execution_context:
        :param undo:
        :param use_invert: Invert, Invert action for the duration of the stroke (optional)
        :return: Result of the operator call.
        """

class uv_sculpt_pinch(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_invert: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Pinch UVs

        :param execution_context:
        :param undo:
        :param use_invert: Invert, Invert action for the duration of the stroke (optional)
        :return: Result of the operator call.
        """

class uv_sculpt_relax(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_invert: bool | None = False,
        relax_method: typing.Literal["LAPLACIAN", "HC", "COTAN"] | None = "LAPLACIAN",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Relax UVs

                :param execution_context:
                :param undo:
                :param use_invert: Invert, Invert action for the duration of the stroke (optional)
                :param relax_method: Relax Method, Algorithm used for UV relaxation (optional)

        LAPLACIAN
        Laplacian -- Use Laplacian method for relaxation.

        HC
        HC -- Use HC method for relaxation.

        COTAN
        Geometry -- Use Geometry (cotangent) relaxation, making UVs follow the underlying 3D geometry.
                :return: Result of the operator call.
        """
