import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types
import mathutils

def brush_stroke(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH", "ERASE"] | None = "NORMAL",
    pen_flip: bool | None = False,
    override_location: bool | None = False,
    ignore_background_click: bool | None = False,
) -> None:
    """Sculpt a stroke into the geometry

        :param stroke: Stroke
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL
    Regular -- Apply brush normally.

    INVERT
    Invert -- Invert action of brush for duration of stroke.

    SMOOTH
    Smooth -- Switch brush to smooth mode for duration of stroke.

    ERASE
    Erase -- Switch brush to erase mode for duration of stroke.
        :param pen_flip: Pen Flip, Whether a tablets eraser mode is being used
        :param override_location: Override Location, Override the given location array by recalculating object space positions from the provided mouse_event positions
        :param ignore_background_click: Ignore Background Click, Clicks on the background do not start the stroke
    """

def cloth_filter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    start_mouse: collections.abc.Iterable[int] | None = (0, 0),
    area_normal_radius: float | None = 0.25,
    strength: float | None = 1.0,
    iteration_count: int | None = 1,
    event_history: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    type: typing.Literal["GRAVITY", "INFLATE", "EXPAND", "PINCH", "SCALE"]
    | None = "GRAVITY",
    force_axis: set[typing.Literal["X", "Y", "Z"]] | None = {"X", "Y", "Z"},
    orientation: typing.Literal["LOCAL", "WORLD", "VIEW"] | None = "LOCAL",
    cloth_mass: float | None = 1.0,
    cloth_damping: float | None = 0.0,
    use_face_sets: bool | None = False,
    use_collisions: bool | None = False,
) -> None:
    """Applies a cloth simulation deformation to the entire mesh

        :param start_mouse: Starting Mouse
        :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
        :param strength: Strength, Filter strength
        :param iteration_count: Repeat, How many times to repeat the filter
        :param type: Filter Type, Operation that is going to be applied to the mesh

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
        :param force_axis: Force Axis, Apply the force in the selected axis

    X
    X -- Apply force in the X axis.

    Y
    Y -- Apply force in the Y axis.

    Z
    Z -- Apply force in the Z axis.
        :param orientation: Orientation, Orientation of the axis to limit the filter force

    LOCAL
    Local -- Use the local axis to limit the force and set the gravity direction.

    WORLD
    World -- Use the global axis to limit the force and set the gravity direction.

    VIEW
    View -- Use the view axis to limit the force and set the gravity direction.
        :param cloth_mass: Cloth Mass, Mass of each simulation particle
        :param cloth_damping: Cloth Damping, How much the applied forces are propagated through the cloth
        :param use_face_sets: Use Face Sets, Apply the filter only to the Face Set under the cursor
        :param use_collisions: Use Collisions, Collide with other collider objects in the scene
    """

def color_filter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    start_mouse: collections.abc.Iterable[int] | None = (0, 0),
    area_normal_radius: float | None = 0.25,
    strength: float | None = 1.0,
    iteration_count: int | None = 1,
    event_history: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
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
) -> None:
    """Applies a filter to modify the active color attribute

        :param start_mouse: Starting Mouse
        :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
        :param strength: Strength, Filter strength
        :param iteration_count: Repeat, How many times to repeat the filter
        :param type: Filter Type

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
        :param fill_color: Fill Color
    """

def detail_flood_fill(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Flood fill the mesh with the selected detail setting"""

def dynamic_topology_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Dynamic topology alters the mesh topology while sculpting"""

def dyntopo_detail_size_edit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Modify the detail size of dyntopo interactively"""

def expand(
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
) -> None:
    """Generic sculpt expand operator

    :param target: Data Target, Data that is going to be modified in the expand operation
    :param falloff_type: Falloff Type, Initial falloff of the expand operation
    :param invert: Invert, Invert the expand active elements
    :param use_mask_preserve: Preserve Previous, Preserve the previous state of the target data
    :param use_falloff_gradient: Falloff Gradient, Expand Using a linear falloff
    :param use_modify_active: Modify Active, Modify the active Face Set instead of creating a new one
    :param use_reposition_pivot: Reposition Pivot, Reposition the sculpt transform pivot to the boundary of the expand active area
    :param max_geodesic_move_preview: Max Vertex Count for Geodesic Move Preview, Maximum number of vertices in the mesh for using geodesic falloff when moving the origin of expand. If the total number of vertices is greater than this value, the falloff will be set to spherical when moving
    :param use_auto_mask: Auto Create, Fill in mask if nothing is already masked
    :param normal_falloff_smooth: Normal Smooth, Blurring steps for normal falloff
    """

def face_set_box_gesture(
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
) -> None:
    """Add a face set in a rectangle defined by the cursor

    :param xmin: X Min
    :param xmax: X Max
    :param ymin: Y Min
    :param ymax: Y Max
    :param wait_for_input: Wait for Input
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    """

def face_set_change_visibility(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["TOGGLE", "SHOW_ACTIVE", "HIDE_ACTIVE"] | None = "TOGGLE",
) -> None:
    """Change the visibility of the Face Sets of the sculpt

        :param mode: Mode

    TOGGLE
    Toggle Visibility -- Hide all Face Sets except for the active one.

    SHOW_ACTIVE
    Show Active Face Set -- Show Active Face Set.

    HIDE_ACTIVE
    Hide Active Face Sets -- Hide Active Face Sets.
    """

def face_set_edit(
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
) -> None:
    """Edits the current active Face Set

        :param active_face_set: Active Face Set
        :param mode: Mode

    GROW
    Grow Face Set -- Grows the Face Sets boundary by one face based on mesh topology.

    SHRINK
    Shrink Face Set -- Shrinks the Face Sets boundary by one face based on mesh topology.

    DELETE_GEOMETRY
    Delete Geometry -- Deletes the faces that are assigned to the Face Set.

    FAIR_POSITIONS
    Fair Positions -- Creates a smooth as possible geometry patch from the Face Set minimizing changes in vertex positions.

    FAIR_TANGENCY
    Fair Tangency -- Creates a smooth as possible geometry patch from the Face Set minimizing changes in vertex tangents.
        :param strength: Strength
        :param modify_hidden: Modify Hidden, Apply the edit operation to hidden geometry
    """

def face_set_lasso_gesture(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_smooth_stroke: bool | None = False,
    smooth_stroke_factor: float | None = 0.75,
    smooth_stroke_radius: int | None = 35,
    use_front_faces_only: bool | None = False,
) -> None:
    """Add a face set in a shape defined by the cursor

    :param path: Path
    :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
    :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
    :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    """

def face_set_line_gesture(
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
) -> None:
    """Add a face set to one side of a line defined by the cursor

    :param xstart: X Start
    :param xend: X End
    :param ystart: Y Start
    :param yend: Y End
    :param flip: Flip
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    """

def face_set_polyline_gesture(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_front_faces_only: bool | None = False,
) -> None:
    """Add a face set in a shape defined by the cursor

    :param path: Path
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    """

def face_sets_create(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["MASKED", "VISIBLE", "ALL", "SELECTION"] | None = "MASKED",
) -> None:
    """Create a new Face Set

        :param mode: Mode

    MASKED
    Face Set from Masked -- Create a new Face Set from the masked faces.

    VISIBLE
    Face Set from Visible -- Create a new Face Set from the visible vertices.

    ALL
    Face Set Full Mesh -- Create an unique Face Set with all faces in the sculpt.

    SELECTION
    Face Set from Edit Mode Selection -- Create an Face Set corresponding to the Edit Mode face selection.
    """

def face_sets_init(
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
) -> None:
    """Initializes all Face Sets in the mesh

        :param mode: Mode

    LOOSE_PARTS
    Face Sets from Loose Parts -- Create a Face Set per loose part in the mesh.

    MATERIALS
    Face Sets from Material Slots -- Create a Face Set per Material Slot.

    NORMALS
    Face Sets from Mesh Normals -- Create Face Sets for Faces that have similar normal.

    UV_SEAMS
    Face Sets from UV Seams -- Create Face Sets using UV Seams as boundaries.

    CREASES
    Face Sets from Edge Creases -- Create Face Sets using Edge Creases as boundaries.

    BEVEL_WEIGHT
    Face Sets from Bevel Weight -- Create Face Sets using Bevel Weights as boundaries.

    SHARP_EDGES
    Face Sets from Sharp Edges -- Create Face Sets using Sharp Edges as boundaries.

    FACE_SET_BOUNDARIES
    Face Sets from Face Set Boundaries -- Create a Face Set per isolated Face Set.
        :param threshold: Threshold, Minimum value to consider a certain attribute a boundary when creating the Face Sets
    """

def face_sets_randomize_colors(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Generates a new set of random colors to render the Face Sets in the viewport"""

def mask_by_color(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    contiguous: bool | None = False,
    invert: bool | None = False,
    preserve_previous_mask: bool | None = False,
    threshold: float | None = 0.35,
) -> None:
    """Creates a mask based on the active color attribute

    :param contiguous: Contiguous, Mask only contiguous color areas
    :param invert: Invert, Invert the generated mask
    :param preserve_previous_mask: Preserve Previous Mask, Preserve the previous mask and add or subtract the new one generated by the colors
    :param threshold: Threshold, How much changes in color affect the mask generation
    """

def mask_filter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filter_type: typing.Literal[
        "SMOOTH", "SHARPEN", "GROW", "SHRINK", "CONTRAST_INCREASE", "CONTRAST_DECREASE"
    ]
    | None = "SMOOTH",
    iterations: int | None = 1,
    auto_iteration_count: bool | None = True,
) -> None:
    """Applies a filter to modify the current mask

    :param filter_type: Type, Filter that is going to be applied to the mask
    :param iterations: Iterations, Number of times that the filter is going to be applied
    :param auto_iteration_count: Auto Iteration Count, Use an automatic number of iterations based on the number of vertices of the sculpt
    """

def mask_from_boundary(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mix_mode: typing.Literal["MIX", "MULTIPLY", "DIVIDE", "ADD", "SUBTRACT"]
    | None = "MIX",
    mix_factor: float | None = 1.0,
    settings_source: typing.Literal["OPERATOR", "BRUSH", "SCENE"] | None = "OPERATOR",
    boundary_mode: typing.Literal["MESH", "FACE_SETS"] | None = "MESH",
    propagation_steps: int | None = 1,
) -> None:
    """Creates a mask based on the boundaries of the surface

        :param mix_mode: Mode, Mix mode
        :param mix_factor: Mix Factor
        :param settings_source: Settings, Use settings from here

    OPERATOR
    Operator -- Use settings from operator properties.

    BRUSH
    Brush -- Use settings from brush.

    SCENE
    Scene -- Use settings from scene.
        :param boundary_mode: Mode, Boundary type to mask

    MESH
    Mesh -- Calculate the boundary mask based on disconnected mesh topology islands.

    FACE_SETS
    Face Sets -- Calculate the boundary mask between face sets.
        :param propagation_steps: Propagation Steps
    """

def mask_from_cavity(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mix_mode: typing.Literal["MIX", "MULTIPLY", "DIVIDE", "ADD", "SUBTRACT"]
    | None = "MIX",
    mix_factor: float | None = 1.0,
    settings_source: typing.Literal["OPERATOR", "BRUSH", "SCENE"] | None = "OPERATOR",
    factor: float | None = 0.5,
    blur_steps: int | None = 2,
    use_curve: bool | None = False,
    invert: bool | None = False,
) -> None:
    """Creates a mask based on the curvature of the surface

        :param mix_mode: Mode, Mix mode
        :param mix_factor: Mix Factor
        :param settings_source: Settings, Use settings from here

    OPERATOR
    Operator -- Use settings from operator properties.

    BRUSH
    Brush -- Use settings from brush.

    SCENE
    Scene -- Use settings from scene.
        :param factor: Factor, The contrast of the cavity mask
        :param blur_steps: Blur, The number of times the cavity mask is blurred
        :param use_curve: Custom Curve
        :param invert: Cavity (Inverted)
    """

def mask_init(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal[
        "RANDOM_PER_VERTEX", "RANDOM_PER_FACE_SET", "RANDOM_PER_LOOSE_PART"
    ]
    | None = "RANDOM_PER_VERTEX",
) -> None:
    """Creates a new mask for the entire mesh

    :param mode: Mode
    """

def mesh_filter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    start_mouse: collections.abc.Iterable[int] | None = (0, 0),
    area_normal_radius: float | None = 0.25,
    strength: float | None = 1.0,
    iteration_count: int | None = 1,
    event_history: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
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
) -> None:
    """Applies a filter to modify the current mesh

        :param start_mouse: Starting Mouse
        :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
        :param strength: Strength, Filter strength
        :param iteration_count: Repeat, How many times to repeat the filter
        :param type: Filter Type, Operation that is going to be applied to the mesh

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
    Relax Face Sets -- Smooth the edges of all the Face Sets.

    SURFACE_SMOOTH
    Surface Smooth -- Smooth the surface of the mesh, preserving the volume.

    SHARPEN
    Sharpen -- Sharpen the cavities of the mesh.

    ENHANCE_DETAILS
    Enhance Details -- Enhance the high frequency surface detail.

    ERASE_DISPLACEMENT
    Erase Displacement -- Deletes the displacement of the Multires Modifier.
        :param deform_axis: Deform Axis, Apply the deformation in the selected axis

    X
    X -- Deform in the X axis.

    Y
    Y -- Deform in the Y axis.

    Z
    Z -- Deform in the Z axis.
        :param orientation: Orientation, Orientation of the axis to limit the filter displacement

    LOCAL
    Local -- Use the local axis to limit the displacement.

    WORLD
    World -- Use the global axis to limit the displacement.

    VIEW
    View -- Use the view axis to limit the displacement.
        :param surface_smooth_shape_preservation: Shape Preservation, How much of the original shape is preserved when smoothing
        :param surface_smooth_current_vertex: Per Vertex Displacement, How much the position of each individual vertex influences the final result
        :param sharpen_smooth_ratio: Smooth Ratio, How much smoothing is applied to polished surfaces
        :param sharpen_intensify_detail_strength: Intensify Details, How much creases and valleys are intensified
        :param sharpen_curvature_smooth_iterations: Curvature Smooth Iterations, How much smooth the resulting shape is, ignoring high frequency details
    """

def optimize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Recalculate the sculpt BVH to improve performance"""

def project_line_gesture(
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
) -> None:
    """Project the geometry onto a plane defined by a line

    :param xstart: X Start
    :param xend: X End
    :param ystart: Y Start
    :param yend: Y End
    :param flip: Flip
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    """

def sample_color(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Sample the vertex color of the active vertex"""

def sample_detail_size(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Iterable[int] | None = (0, 0),
    mode: typing.Literal["DYNTOPO", "VOXEL"] | None = "DYNTOPO",
) -> None:
    """Sample the mesh detail on clicked point

        :param location: Location, Screen coordinates of sampling
        :param mode: Detail Mode, Target sculpting workflow that is going to use the sampled size

    DYNTOPO
    Dyntopo -- Sample dyntopo detail.

    VOXEL
    Voxel -- Sample mesh voxel size.
    """

def sculptmode_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle sculpt mode in 3D view"""

def set_persistent_base(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset the copy of the mesh that is being sculpted on"""

def set_pivot_position(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["ORIGIN", "UNMASKED", "BORDER", "ACTIVE", "SURFACE"]
    | None = "UNMASKED",
    mouse_x: float | None = 0.0,
    mouse_y: float | None = 0.0,
) -> None:
    """Sets the sculpt transform pivot position

        :param mode: Mode

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
        :param mouse_x: Mouse Position X, Position of the mouse used for "Surface" mode
        :param mouse_y: Mouse Position Y, Position of the mouse used for "Surface" mode
    """

def symmetrize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    merge_tolerance: float | None = 0.0005,
) -> None:
    """Symmetrize the topology modifications

    :param merge_tolerance: Merge Distance, Distance within which symmetrical vertices are merged
    """

def trim_box_gesture(
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
    location: collections.abc.Iterable[int] | None = (0, 0),
    trim_mode: typing.Literal["DIFFERENCE", "UNION", "JOIN"] | None = "DIFFERENCE",
    use_cursor_depth: bool | None = False,
    trim_orientation: typing.Literal["VIEW", "SURFACE"] | None = "VIEW",
    trim_extrude_mode: typing.Literal["PROJECT", "FIXED"] | None = "FIXED",
    trim_solver: typing.Literal["EXACT", "FAST"] | None = "FAST",
) -> None:
    """Execute a boolean operation on the mesh and a rectangle defined by the cursor

        :param xmin: X Min
        :param xmax: X Max
        :param ymin: Y Min
        :param ymax: Y Max
        :param wait_for_input: Wait for Input
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :param location: Location, Mouse location
        :param trim_mode: Trim Mode

    DIFFERENCE
    Difference -- Use a difference boolean operation.

    UNION
    Union -- Use a union boolean operation.

    JOIN
    Join -- Join the new mesh as separate geometry, without performing any boolean operation.
        :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
        :param trim_orientation: Shape Orientation

    VIEW
    View -- Use the view to orientate the trimming shape.

    SURFACE
    Surface -- Use the surface normal to orientate the trimming shape.
        :param trim_extrude_mode: Extrude Mode

    PROJECT
    Project -- Align trim geometry with the perspective of the current view for a tapered shape.

    FIXED
    Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
        :param trim_solver: Solver

    EXACT
    Exact -- Use the exact boolean solver.

    FAST
    Fast -- Use the fast float boolean solver.
    """

def trim_lasso_gesture(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_smooth_stroke: bool | None = False,
    smooth_stroke_factor: float | None = 0.75,
    smooth_stroke_radius: int | None = 35,
    use_front_faces_only: bool | None = False,
    location: collections.abc.Iterable[int] | None = (0, 0),
    trim_mode: typing.Literal["DIFFERENCE", "UNION", "JOIN"] | None = "DIFFERENCE",
    use_cursor_depth: bool | None = False,
    trim_orientation: typing.Literal["VIEW", "SURFACE"] | None = "VIEW",
    trim_extrude_mode: typing.Literal["PROJECT", "FIXED"] | None = "FIXED",
    trim_solver: typing.Literal["EXACT", "FAST"] | None = "FAST",
) -> None:
    """Execute a boolean operation on the mesh and a shape defined by the cursor

        :param path: Path
        :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
        :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
        :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :param location: Location, Mouse location
        :param trim_mode: Trim Mode

    DIFFERENCE
    Difference -- Use a difference boolean operation.

    UNION
    Union -- Use a union boolean operation.

    JOIN
    Join -- Join the new mesh as separate geometry, without performing any boolean operation.
        :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
        :param trim_orientation: Shape Orientation

    VIEW
    View -- Use the view to orientate the trimming shape.

    SURFACE
    Surface -- Use the surface normal to orientate the trimming shape.
        :param trim_extrude_mode: Extrude Mode

    PROJECT
    Project -- Align trim geometry with the perspective of the current view for a tapered shape.

    FIXED
    Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
        :param trim_solver: Solver

    EXACT
    Exact -- Use the exact boolean solver.

    FAST
    Fast -- Use the fast float boolean solver.
    """

def trim_line_gesture(
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
    location: collections.abc.Iterable[int] | None = (0, 0),
    trim_mode: typing.Literal["DIFFERENCE", "UNION", "JOIN"] | None = "DIFFERENCE",
    use_cursor_depth: bool | None = False,
    trim_orientation: typing.Literal["VIEW", "SURFACE"] | None = "VIEW",
    trim_extrude_mode: typing.Literal["PROJECT", "FIXED"] | None = "FIXED",
    trim_solver: typing.Literal["EXACT", "FAST"] | None = "FAST",
) -> None:
    """Remove a portion of the mesh on one side of a line

        :param xstart: X Start
        :param xend: X End
        :param ystart: Y Start
        :param yend: Y End
        :param flip: Flip
        :param cursor: Cursor, Mouse cursor style to use during the modal operator
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
        :param location: Location, Mouse location
        :param trim_mode: Trim Mode

    DIFFERENCE
    Difference -- Use a difference boolean operation.

    UNION
    Union -- Use a union boolean operation.

    JOIN
    Join -- Join the new mesh as separate geometry, without performing any boolean operation.
        :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
        :param trim_orientation: Shape Orientation

    VIEW
    View -- Use the view to orientate the trimming shape.

    SURFACE
    Surface -- Use the surface normal to orientate the trimming shape.
        :param trim_extrude_mode: Extrude Mode

    PROJECT
    Project -- Align trim geometry with the perspective of the current view for a tapered shape.

    FIXED
    Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
        :param trim_solver: Solver

    EXACT
    Exact -- Use the exact boolean solver.

    FAST
    Fast -- Use the fast float boolean solver.
    """

def trim_polyline_gesture(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_front_faces_only: bool | None = False,
    location: collections.abc.Iterable[int] | None = (0, 0),
    trim_mode: typing.Literal["DIFFERENCE", "UNION", "JOIN"] | None = "DIFFERENCE",
    use_cursor_depth: bool | None = False,
    trim_orientation: typing.Literal["VIEW", "SURFACE"] | None = "VIEW",
    trim_extrude_mode: typing.Literal["PROJECT", "FIXED"] | None = "FIXED",
    trim_solver: typing.Literal["EXACT", "FAST"] | None = "FAST",
) -> None:
    """Execute a boolean operation on the mesh and a polygonal shape defined by the cursor

        :param path: Path
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :param location: Location, Mouse location
        :param trim_mode: Trim Mode

    DIFFERENCE
    Difference -- Use a difference boolean operation.

    UNION
    Union -- Use a union boolean operation.

    JOIN
    Join -- Join the new mesh as separate geometry, without performing any boolean operation.
        :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
        :param trim_orientation: Shape Orientation

    VIEW
    View -- Use the view to orientate the trimming shape.

    SURFACE
    Surface -- Use the surface normal to orientate the trimming shape.
        :param trim_extrude_mode: Extrude Mode

    PROJECT
    Project -- Align trim geometry with the perspective of the current view for a tapered shape.

    FIXED
    Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
        :param trim_solver: Solver

    EXACT
    Exact -- Use the exact boolean solver.

    FAST
    Fast -- Use the fast float boolean solver.
    """

def uv_sculpt_grab(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_invert: bool | None = False,
) -> None:
    """Grab UVs

    :param use_invert: Invert, Invert action for the duration of the stroke
    """

def uv_sculpt_pinch(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_invert: bool | None = False,
) -> None:
    """Pinch UVs

    :param use_invert: Invert, Invert action for the duration of the stroke
    """

def uv_sculpt_relax(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_invert: bool | None = False,
    relax_method: typing.Literal["LAPLACIAN", "HC", "COTAN"] | None = "COTAN",
) -> None:
    """Relax UVs

        :param use_invert: Invert, Invert action for the duration of the stroke
        :param relax_method: Relax Method, Algorithm used for UV relaxation

    LAPLACIAN
    Laplacian -- Use Laplacian method for relaxation.

    HC
    HC -- Use HC method for relaxation.

    COTAN
    Geometry -- Use Geometry (cotangent) relaxation, making UVs follow the underlying 3D geometry.
    """
