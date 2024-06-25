import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def brush_stroke(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: str | None = "NORMAL",
    ignore_background_click: bool | typing.Any | None = False,
):
    """Sculpt a stroke into the geometry

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL
    Regular -- Apply brush normally.

    INVERT
    Invert -- Invert action of brush for duration of stroke.

    SMOOTH
    Smooth -- Switch brush to smooth mode for duration of stroke.
        :type mode: str | None
        :param ignore_background_click: Ignore Background Click, Clicks on the background do not start the stroke
        :type ignore_background_click: bool | typing.Any | None
    """

    ...

def cloth_filter(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    start_mouse: typing.Any | None = (0, 0),
    area_normal_radius: typing.Any | None = 0.25,
    strength: typing.Any | None = 1.0,
    iteration_count: typing.Any | None = 1,
    event_history: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    type: str | None = "GRAVITY",
    force_axis: set[str] | None = {"X", "Y", "Z"},
    orientation: str | None = "LOCAL",
    cloth_mass: typing.Any | None = 1.0,
    cloth_damping: typing.Any | None = 0.0,
    use_face_sets: bool | typing.Any | None = False,
    use_collisions: bool | typing.Any | None = False,
):
    """Applies a cloth simulation deformation to the entire mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param start_mouse: Starting Mouse
        :type start_mouse: typing.Any | None
        :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
        :type area_normal_radius: typing.Any | None
        :param strength: Strength, Filter strength
        :type strength: typing.Any | None
        :param iteration_count: Repeat, How many times to repeat the filter
        :type iteration_count: typing.Any | None
        :type event_history: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param type: Filter Type, Operation that is going to be applied to the mesh

    GRAVITY
    Gravity -- Applies gravity to the simulation.

    INFLATE
    Inflate -- Inflates the cloth.

    EXPAND
    Expand -- Expands the cloth's dimensions.

    PINCH
    Pinch -- Pulls the cloth to the cursor's start position.

    SCALE
    Scale -- Scales the mesh as a soft body using the origin of the object as scale.
        :type type: str | None
        :param force_axis: Force Axis, Apply the force in the selected axis

    X
    X -- Apply force in the X axis.

    Y
    Y -- Apply force in the Y axis.

    Z
    Z -- Apply force in the Z axis.
        :type force_axis: set[str] | None
        :param orientation: Orientation, Orientation of the axis to limit the filter force

    LOCAL
    Local -- Use the local axis to limit the force and set the gravity direction.

    WORLD
    World -- Use the global axis to limit the force and set the gravity direction.

    VIEW
    View -- Use the view axis to limit the force and set the gravity direction.
        :type orientation: str | None
        :param cloth_mass: Cloth Mass, Mass of each simulation particle
        :type cloth_mass: typing.Any | None
        :param cloth_damping: Cloth Damping, How much the applied forces are propagated through the cloth
        :type cloth_damping: typing.Any | None
        :param use_face_sets: Use Face Sets, Apply the filter only to the Face Set under the cursor
        :type use_face_sets: bool | typing.Any | None
        :param use_collisions: Use Collisions, Collide with other collider objects in the scene
        :type use_collisions: bool | typing.Any | None
    """

    ...

def color_filter(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    start_mouse: typing.Any | None = (0, 0),
    area_normal_radius: typing.Any | None = 0.25,
    strength: typing.Any | None = 1.0,
    iteration_count: typing.Any | None = 1,
    event_history: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    type: str | None = "FILL",
    fill_color: typing.Any | None = (1.0, 1.0, 1.0),
):
    """Applies a filter to modify the active color attribute

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param start_mouse: Starting Mouse
        :type start_mouse: typing.Any | None
        :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
        :type area_normal_radius: typing.Any | None
        :param strength: Strength, Filter strength
        :type strength: typing.Any | None
        :param iteration_count: Repeat, How many times to repeat the filter
        :type iteration_count: typing.Any | None
        :type event_history: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
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
        :type type: str | None
        :param fill_color: Fill Color
        :type fill_color: typing.Any | None
    """

    ...

def detail_flood_fill(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Flood fill the mesh with the selected detail setting

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def dynamic_topology_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Dynamic topology alters the mesh topology while sculpting

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def dyntopo_detail_size_edit(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Modify the detail size of dyntopo interactively

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def expand(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    target: str | None = "MASK",
    falloff_type: str | None = "GEODESIC",
    invert: bool | typing.Any | None = False,
    use_mask_preserve: bool | typing.Any | None = False,
    use_falloff_gradient: bool | typing.Any | None = False,
    use_modify_active: bool | typing.Any | None = False,
    use_reposition_pivot: bool | typing.Any | None = True,
    max_geodesic_move_preview: typing.Any | None = 10000,
    use_auto_mask: bool | typing.Any | None = False,
    normal_falloff_smooth: typing.Any | None = 2,
):
    """Generic sculpt expand operator

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param target: Data Target, Data that is going to be modified in the expand operation
    :type target: str | None
    :param falloff_type: Falloff Type, Initial falloff of the expand operation
    :type falloff_type: str | None
    :param invert: Invert, Invert the expand active elements
    :type invert: bool | typing.Any | None
    :param use_mask_preserve: Preserve Previous, Preserve the previous state of the target data
    :type use_mask_preserve: bool | typing.Any | None
    :param use_falloff_gradient: Falloff Gradient, Expand Using a linear falloff
    :type use_falloff_gradient: bool | typing.Any | None
    :param use_modify_active: Modify Active, Modify the active Face Set instead of creating a new one
    :type use_modify_active: bool | typing.Any | None
    :param use_reposition_pivot: Reposition Pivot, Reposition the sculpt transform pivot to the boundary of the expand active area
    :type use_reposition_pivot: bool | typing.Any | None
    :param max_geodesic_move_preview: Max Vertex Count for Geodesic Move Preview, Maximum number of vertices in the mesh for using geodesic falloff when moving the origin of expand. If the total number of vertices is greater than this value, the falloff will be set to spherical when moving
    :type max_geodesic_move_preview: typing.Any | None
    :param use_auto_mask: Auto Create, Fill in mask if nothing is already masked
    :type use_auto_mask: bool | typing.Any | None
    :param normal_falloff_smooth: Normal Smooth, Blurring steps for normal falloff
    :type normal_falloff_smooth: typing.Any | None
    """

    ...

def face_set_box_gesture(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    xmin: typing.Any | None = 0,
    xmax: typing.Any | None = 0,
    ymin: typing.Any | None = 0,
    ymax: typing.Any | None = 0,
    wait_for_input: bool | typing.Any | None = True,
    use_front_faces_only: bool | typing.Any | None = False,
    use_limit_to_segment: bool | typing.Any | None = False,
):
    """Add face set within the box as you move the brush

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param xmin: X Min
    :type xmin: typing.Any | None
    :param xmax: X Max
    :type xmax: typing.Any | None
    :param ymin: Y Min
    :type ymin: typing.Any | None
    :param ymax: Y Max
    :type ymax: typing.Any | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | typing.Any | None
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: bool | typing.Any | None
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    :type use_limit_to_segment: bool | typing.Any | None
    """

    ...

def face_set_change_visibility(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "TOGGLE",
):
    """Change the visibility of the Face Sets of the sculpt

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    TOGGLE
    Toggle Visibility -- Hide all Face Sets except for the active one.

    SHOW_ACTIVE
    Show Active Face Set -- Show Active Face Set.

    HIDE_ACTIVE
    Hide Active Face Sets -- Hide Active Face Sets.
        :type mode: str | None
    """

    ...

def face_set_edit(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    active_face_set: typing.Any | None = 1,
    mode: str | None = "GROW",
    strength: typing.Any | None = 1.0,
    modify_hidden: bool | typing.Any | None = True,
):
    """Edits the current active Face Set

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param active_face_set: Active Face Set
        :type active_face_set: typing.Any | None
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
        :type mode: str | None
        :param strength: Strength
        :type strength: typing.Any | None
        :param modify_hidden: Modify Hidden, Apply the edit operation to hidden geometry
        :type modify_hidden: bool | typing.Any | None
    """

    ...

def face_set_lasso_gesture(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_front_faces_only: bool | typing.Any | None = False,
    use_limit_to_segment: bool | typing.Any | None = False,
):
    """Add face set within the lasso as you move the brush

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param path: Path
    :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: bool | typing.Any | None
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    :type use_limit_to_segment: bool | typing.Any | None
    """

    ...

def face_sets_create(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "MASKED",
):
    """Create a new Face Set

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    MASKED
    Face Set from Masked -- Create a new Face Set from the masked faces.

    VISIBLE
    Face Set from Visible -- Create a new Face Set from the visible vertices.

    ALL
    Face Set Full Mesh -- Create an unique Face Set with all faces in the sculpt.

    SELECTION
    Face Set from Edit Mode Selection -- Create an Face Set corresponding to the Edit Mode face selection.
        :type mode: str | None
    """

    ...

def face_sets_init(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "LOOSE_PARTS",
    threshold: typing.Any | None = 0.5,
):
    """Initializes all Face Sets in the mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
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
        :type mode: str | None
        :param threshold: Threshold, Minimum value to consider a certain attribute a boundary when creating the Face Sets
        :type threshold: typing.Any | None
    """

    ...

def face_sets_randomize_colors(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Generates a new set of random colors to render the Face Sets in the viewport

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def mask_by_color(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    contiguous: bool | typing.Any | None = False,
    invert: bool | typing.Any | None = False,
    preserve_previous_mask: bool | typing.Any | None = False,
    threshold: typing.Any | None = 0.35,
):
    """Creates a mask based on the active color attribute

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param contiguous: Contiguous, Mask only contiguous color areas
    :type contiguous: bool | typing.Any | None
    :param invert: Invert, Invert the generated mask
    :type invert: bool | typing.Any | None
    :param preserve_previous_mask: Preserve Previous Mask, Preserve the previous mask and add or subtract the new one generated by the colors
    :type preserve_previous_mask: bool | typing.Any | None
    :param threshold: Threshold, How much changes in color affect the mask generation
    :type threshold: typing.Any | None
    """

    ...

def mask_filter(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filter_type: str | None = "SMOOTH",
    iterations: typing.Any | None = 1,
    auto_iteration_count: bool | typing.Any | None = True,
):
    """Applies a filter to modify the current mask

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filter_type: Type, Filter that is going to be applied to the mask

    SMOOTH
    Smooth Mask -- Smooth mask.

    SHARPEN
    Sharpen Mask -- Sharpen mask.

    GROW
    Grow Mask -- Grow mask.

    SHRINK
    Shrink Mask -- Shrink mask.

    CONTRAST_INCREASE
    Increase Contrast -- Increase the contrast of the paint mask.

    CONTRAST_DECREASE
    Decrease Contrast -- Decrease the contrast of the paint mask.
        :type filter_type: str | None
        :param iterations: Iterations, Number of times that the filter is going to be applied
        :type iterations: typing.Any | None
        :param auto_iteration_count: Auto Iteration Count, Use a automatic number of iterations based on the number of vertices of the sculpt
        :type auto_iteration_count: bool | typing.Any | None
    """

    ...

def mask_from_cavity(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mix_mode: str | None = "MIX",
    mix_factor: typing.Any | None = 1.0,
    settings_source: str | None = "OPERATOR",
    factor: typing.Any | None = 0.5,
    blur_steps: typing.Any | None = 2,
    use_curve: bool | typing.Any | None = False,
    invert: bool | typing.Any | None = False,
):
    """Creates a mask based on the curvature of the surface

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mix_mode: Mode, Mix mode
        :type mix_mode: str | None
        :param mix_factor: Mix Factor
        :type mix_factor: typing.Any | None
        :param settings_source: Settings, Use settings from here

    OPERATOR
    Operator -- Use settings from operator properties.

    BRUSH
    Brush -- Use settings from brush.

    SCENE
    Scene -- Use settings from scene.
        :type settings_source: str | None
        :param factor: Factor, The contrast of the cavity mask
        :type factor: typing.Any | None
        :param blur_steps: Blur, The number of times the cavity mask is blurred
        :type blur_steps: typing.Any | None
        :param use_curve: Custom Curve
        :type use_curve: bool | typing.Any | None
        :param invert: Cavity (Inverted)
        :type invert: bool | typing.Any | None
    """

    ...

def mask_init(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "RANDOM_PER_VERTEX",
):
    """Creates a new mask for the entire mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: str | None
    """

    ...

def mesh_filter(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    start_mouse: typing.Any | None = (0, 0),
    area_normal_radius: typing.Any | None = 0.25,
    strength: typing.Any | None = 1.0,
    iteration_count: typing.Any | None = 1,
    event_history: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    type: str | None = "INFLATE",
    deform_axis: set[str] | None = {"X", "Y", "Z"},
    orientation: str | None = "LOCAL",
    surface_smooth_shape_preservation: typing.Any | None = 0.5,
    surface_smooth_current_vertex: typing.Any | None = 0.5,
    sharpen_smooth_ratio: typing.Any | None = 0.35,
    sharpen_intensify_detail_strength: typing.Any | None = 0.0,
    sharpen_curvature_smooth_iterations: typing.Any | None = 0,
):
    """Applies a filter to modify the current mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param start_mouse: Starting Mouse
        :type start_mouse: typing.Any | None
        :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
        :type area_normal_radius: typing.Any | None
        :param strength: Strength, Filter strength
        :type strength: typing.Any | None
        :param iteration_count: Repeat, How many times to repeat the filter
        :type iteration_count: typing.Any | None
        :type event_history: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
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

    ERASE_DISCPLACEMENT
    Erase Displacement -- Deletes the displacement of the Multires Modifier.
        :type type: str | None
        :param deform_axis: Deform Axis, Apply the deformation in the selected axis

    X
    X -- Deform in the X axis.

    Y
    Y -- Deform in the Y axis.

    Z
    Z -- Deform in the Z axis.
        :type deform_axis: set[str] | None
        :param orientation: Orientation, Orientation of the axis to limit the filter displacement

    LOCAL
    Local -- Use the local axis to limit the displacement.

    WORLD
    World -- Use the global axis to limit the displacement.

    VIEW
    View -- Use the view axis to limit the displacement.
        :type orientation: str | None
        :param surface_smooth_shape_preservation: Shape Preservation, How much of the original shape is preserved when smoothing
        :type surface_smooth_shape_preservation: typing.Any | None
        :param surface_smooth_current_vertex: Per Vertex Displacement, How much the position of each individual vertex influences the final result
        :type surface_smooth_current_vertex: typing.Any | None
        :param sharpen_smooth_ratio: Smooth Ratio, How much smoothing is applied to polished surfaces
        :type sharpen_smooth_ratio: typing.Any | None
        :param sharpen_intensify_detail_strength: Intensify Details, How much creases and valleys are intensified
        :type sharpen_intensify_detail_strength: typing.Any | None
        :param sharpen_curvature_smooth_iterations: Curvature Smooth Iterations, How much smooth the resulting shape is, ignoring high frequency details
        :type sharpen_curvature_smooth_iterations: typing.Any | None
    """

    ...

def optimize(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Recalculate the sculpt BVH to improve performance

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def project_line_gesture(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    xstart: typing.Any | None = 0,
    xend: typing.Any | None = 0,
    ystart: typing.Any | None = 0,
    yend: typing.Any | None = 0,
    flip: bool | typing.Any | None = False,
    cursor: typing.Any | None = 5,
    use_front_faces_only: bool | typing.Any | None = False,
    use_limit_to_segment: bool | typing.Any | None = False,
):
    """Project the geometry onto a plane defined by a line

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param xstart: X Start
    :type xstart: typing.Any | None
    :param xend: X End
    :type xend: typing.Any | None
    :param ystart: Y Start
    :type ystart: typing.Any | None
    :param yend: Y End
    :type yend: typing.Any | None
    :param flip: Flip
    :type flip: bool | typing.Any | None
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: typing.Any | None
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: bool | typing.Any | None
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    :type use_limit_to_segment: bool | typing.Any | None
    """

    ...

def sample_color(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Sample the vertex color of the active vertex

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def sample_detail_size(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    location: typing.Any | None = (0, 0),
    mode: str | None = "DYNTOPO",
):
    """Sample the mesh detail on clicked point

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param location: Location, Screen coordinates of sampling
        :type location: typing.Any | None
        :param mode: Detail Mode, Target sculpting workflow that is going to use the sampled size

    DYNTOPO
    Dyntopo -- Sample dyntopo detail.

    VOXEL
    Voxel -- Sample mesh voxel size.
        :type mode: str | None
    """

    ...

def sculptmode_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle sculpt mode in 3D view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def set_detail_size(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Set the mesh detail (either relative or constant one, depending on current dyntopo mode)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def set_persistent_base(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset the copy of the mesh that is being sculpted on

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def set_pivot_position(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "UNMASKED",
    mouse_x: typing.Any | None = 0.0,
    mouse_y: typing.Any | None = 0.0,
):
    """Sets the sculpt transform pivot position

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
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
        :type mode: str | None
        :param mouse_x: Mouse Position X, Position of the mouse used for "Surface" mode
        :type mouse_x: typing.Any | None
        :param mouse_y: Mouse Position Y, Position of the mouse used for "Surface" mode
        :type mouse_y: typing.Any | None
    """

    ...

def symmetrize(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    merge_tolerance: typing.Any | None = 0.0005,
):
    """Symmetrize the topology modifications

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param merge_tolerance: Merge Distance, Distance within which symmetrical vertices are merged
    :type merge_tolerance: typing.Any | None
    """

    ...

def trim_box_gesture(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    xmin: typing.Any | None = 0,
    xmax: typing.Any | None = 0,
    ymin: typing.Any | None = 0,
    ymax: typing.Any | None = 0,
    wait_for_input: bool | typing.Any | None = True,
    use_front_faces_only: bool | typing.Any | None = False,
    use_limit_to_segment: bool | typing.Any | None = False,
    trim_mode: str | None = "DIFFERENCE",
    use_cursor_depth: bool | typing.Any | None = False,
    trim_orientation: str | None = "VIEW",
    trim_extrude_mode: str | None = "FIXED",
):
    """Trims the mesh within the box as you move the brush

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param xmin: X Min
        :type xmin: typing.Any | None
        :param xmax: X Max
        :type xmax: typing.Any | None
        :param ymin: Y Min
        :type ymin: typing.Any | None
        :param ymax: Y Max
        :type ymax: typing.Any | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | typing.Any | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | typing.Any | None
        :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
        :type use_limit_to_segment: bool | typing.Any | None
        :param trim_mode: Trim Mode

    DIFFERENCE
    Difference -- Use a difference boolean operation.

    UNION
    Union -- Use a union boolean operation.

    JOIN
    Join -- Join the new mesh as separate geometry, without performing any boolean operation.
        :type trim_mode: str | None
        :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
        :type use_cursor_depth: bool | typing.Any | None
        :param trim_orientation: Shape Orientation

    VIEW
    View -- Use the view to orientate the trimming shape.

    SURFACE
    Surface -- Use the surface normal to orientate the trimming shape.
        :type trim_orientation: str | None
        :param trim_extrude_mode: Extrude Mode

    PROJECT
    Project -- Project back faces when extruding.

    FIXED
    Fixed -- Extrude back faces by fixed amount.
        :type trim_extrude_mode: str | None
    """

    ...

def trim_lasso_gesture(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_front_faces_only: bool | typing.Any | None = False,
    use_limit_to_segment: bool | typing.Any | None = False,
    trim_mode: str | None = "DIFFERENCE",
    use_cursor_depth: bool | typing.Any | None = False,
    trim_orientation: str | None = "VIEW",
    trim_extrude_mode: str | None = "FIXED",
):
    """Trims the mesh within the lasso as you move the brush

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param path: Path
        :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | typing.Any | None
        :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
        :type use_limit_to_segment: bool | typing.Any | None
        :param trim_mode: Trim Mode

    DIFFERENCE
    Difference -- Use a difference boolean operation.

    UNION
    Union -- Use a union boolean operation.

    JOIN
    Join -- Join the new mesh as separate geometry, without performing any boolean operation.
        :type trim_mode: str | None
        :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
        :type use_cursor_depth: bool | typing.Any | None
        :param trim_orientation: Shape Orientation

    VIEW
    View -- Use the view to orientate the trimming shape.

    SURFACE
    Surface -- Use the surface normal to orientate the trimming shape.
        :type trim_orientation: str | None
        :param trim_extrude_mode: Extrude Mode

    PROJECT
    Project -- Project back faces when extruding.

    FIXED
    Fixed -- Extrude back faces by fixed amount.
        :type trim_extrude_mode: str | None
    """

    ...

def uv_sculpt_stroke(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "NORMAL",
):
    """Sculpt UVs using a brush

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode, Stroke Mode

    NORMAL
    Regular -- Apply brush normally.

    INVERT
    Invert -- Invert action of brush for duration of stroke.

    RELAX
    Relax -- Switch brush to relax mode for duration of stroke.
        :type mode: str | None
    """

    ...
