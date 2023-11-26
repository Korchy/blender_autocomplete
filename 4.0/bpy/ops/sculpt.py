import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def brush_stroke(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        stroke: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorStrokeElement']] = None,
        mode: typing.Optional[typing.Any] = 'NORMAL',
        ignore_background_click: typing.Optional[typing.Union[bool, typing.
                                                              Any]] = False):
    ''' Sculpt a stroke into the geometry

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param stroke: Stroke
    :type stroke: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param mode: Stroke Mode, Action taken when a paint stroke is made * ``NORMAL`` Regular -- Apply brush normally. * ``INVERT`` Invert -- Invert action of brush for duration of stroke. * ``SMOOTH`` Smooth -- Switch brush to smooth mode for duration of stroke.
    :type mode: typing.Optional[typing.Any]
    :param ignore_background_click: Ignore Background Click, Clicks on the background do not start the stroke
    :type ignore_background_click: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def cloth_filter(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        start_mouse: typing.Optional[typing.Any] = (0, 0),
        area_normal_radius: typing.Optional[typing.Any] = 0.25,
        strength: typing.Optional[typing.Any] = 1.0,
        iteration_count: typing.Optional[typing.Any] = 1,
        event_history: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorStrokeElement']] = None,
        type: typing.Optional[typing.Any] = 'GRAVITY',
        force_axis: typing.Optional[typing.Any] = {'X', 'Y', 'Z'},
        orientation: typing.Optional[typing.Any] = 'LOCAL',
        cloth_mass: typing.Optional[typing.Any] = 1.0,
        cloth_damping: typing.Optional[typing.Any] = 0.0,
        use_face_sets: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_collisions: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False):
    ''' Applies a cloth simulation deformation to the entire mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param start_mouse: Starting Mouse
    :type start_mouse: typing.Optional[typing.Any]
    :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
    :type area_normal_radius: typing.Optional[typing.Any]
    :param strength: Strength, Filter strength
    :type strength: typing.Optional[typing.Any]
    :param iteration_count: Repeat, How many times to repeat the filter
    :type iteration_count: typing.Optional[typing.Any]
    :type event_history: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param type: Filter Type, Operation that is going to be applied to the mesh * ``GRAVITY`` Gravity -- Applies gravity to the simulation. * ``INFLATE`` Inflate -- Inflates the cloth. * ``EXPAND`` Expand -- Expands the cloth's dimensions. * ``PINCH`` Pinch -- Pulls the cloth to the cursor's start position. * ``SCALE`` Scale -- Scales the mesh as a soft body using the origin of the object as scale.
    :type type: typing.Optional[typing.Any]
    :param force_axis: Force Axis, Apply the force in the selected axis * ``X`` X -- Apply force in the X axis. * ``Y`` Y -- Apply force in the Y axis. * ``Z`` Z -- Apply force in the Z axis.
    :type force_axis: typing.Optional[typing.Any]
    :param orientation: Orientation, Orientation of the axis to limit the filter force * ``LOCAL`` Local -- Use the local axis to limit the force and set the gravity direction. * ``WORLD`` World -- Use the global axis to limit the force and set the gravity direction. * ``VIEW`` View -- Use the view axis to limit the force and set the gravity direction.
    :type orientation: typing.Optional[typing.Any]
    :param cloth_mass: Cloth Mass, Mass of each simulation particle
    :type cloth_mass: typing.Optional[typing.Any]
    :param cloth_damping: Cloth Damping, How much the applied forces are propagated through the cloth
    :type cloth_damping: typing.Optional[typing.Any]
    :param use_face_sets: Use Face Sets, Apply the filter only to the Face Set under the cursor
    :type use_face_sets: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_collisions: Use Collisions, Collide with other collider objects in the scene
    :type use_collisions: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def color_filter(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        start_mouse: typing.Optional[typing.Any] = (0, 0),
        area_normal_radius: typing.Optional[typing.Any] = 0.25,
        strength: typing.Optional[typing.Any] = 1.0,
        iteration_count: typing.Optional[typing.Any] = 1,
        event_history: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorStrokeElement']] = None,
        type: typing.Optional[typing.Any] = 'FILL',
        fill_color: typing.Optional[typing.Any] = (1.0, 1.0, 1.0)):
    ''' Applies a filter to modify the active color attribute

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param start_mouse: Starting Mouse
    :type start_mouse: typing.Optional[typing.Any]
    :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
    :type area_normal_radius: typing.Optional[typing.Any]
    :param strength: Strength, Filter strength
    :type strength: typing.Optional[typing.Any]
    :param iteration_count: Repeat, How many times to repeat the filter
    :type iteration_count: typing.Optional[typing.Any]
    :type event_history: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param type: Filter Type * ``FILL`` Fill -- Fill with a specific color. * ``HUE`` Hue -- Change hue. * ``SATURATION`` Saturation -- Change saturation. * ``VALUE`` Value -- Change value. * ``BRIGHTNESS`` Brightness -- Change brightness. * ``CONTRAST`` Contrast -- Change contrast. * ``SMOOTH`` Smooth -- Smooth colors. * ``RED`` Red -- Change red channel. * ``GREEN`` Green -- Change green channel. * ``BLUE`` Blue -- Change blue channel.
    :type type: typing.Optional[typing.Any]
    :param fill_color: Fill Color
    :type fill_color: typing.Optional[typing.Any]
    '''

    pass


def detail_flood_fill(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Flood fill the mesh with the selected detail setting

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def dynamic_topology_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Dynamic topology alters the mesh topology while sculpting

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def dyntopo_detail_size_edit(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Modify the detail size of dyntopo interactively

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def expand(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        target: typing.Optional[typing.Any] = 'MASK',
        falloff_type: typing.Optional[typing.Any] = 'GEODESIC',
        invert: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_mask_preserve: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False,
        use_falloff_gradient: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        use_modify_active: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False,
        use_reposition_pivot: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = True,
        max_geodesic_move_preview: typing.Optional[typing.Any] = 10000,
        use_auto_mask: typing.Optional[typing.Union[bool, typing.Any]] = False,
        normal_falloff_smooth: typing.Optional[typing.Any] = 2):
    ''' Generic sculpt expand operator

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param target: Data Target, Data that is going to be modified in the expand operation
    :type target: typing.Optional[typing.Any]
    :param falloff_type: Falloff Type, Initial falloff of the expand operation
    :type falloff_type: typing.Optional[typing.Any]
    :param invert: Invert, Invert the expand active elements
    :type invert: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_mask_preserve: Preserve Previous, Preserve the previous state of the target data
    :type use_mask_preserve: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_falloff_gradient: Falloff Gradient, Expand Using a linear falloff
    :type use_falloff_gradient: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_modify_active: Modify Active, Modify the active Face Set instead of creating a new one
    :type use_modify_active: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_reposition_pivot: Reposition Pivot, Reposition the sculpt transform pivot to the boundary of the expand active area
    :type use_reposition_pivot: typing.Optional[typing.Union[bool, typing.Any]]
    :param max_geodesic_move_preview: Max Vertex Count for Geodesic Move Preview, Maximum number of vertices in the mesh for using geodesic falloff when moving the origin of expand. If the total number of vertices is greater than this value, the falloff will be set to spherical when moving
    :type max_geodesic_move_preview: typing.Optional[typing.Any]
    :param use_auto_mask: Auto Create, Fill in mask if nothing is already masked
    :type use_auto_mask: typing.Optional[typing.Union[bool, typing.Any]]
    :param normal_falloff_smooth: Normal Smooth, Blurring steps for normal falloff
    :type normal_falloff_smooth: typing.Optional[typing.Any]
    '''

    pass


def face_set_box_gesture(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        xmin: typing.Optional[typing.Any] = 0,
        xmax: typing.Optional[typing.Any] = 0,
        ymin: typing.Optional[typing.Any] = 0,
        ymax: typing.Optional[typing.Any] = 0,
        wait_for_input: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_front_faces_only: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        use_limit_to_segment: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False):
    ''' Add face set within the box as you move the brush

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param xmin: X Min
    :type xmin: typing.Optional[typing.Any]
    :param xmax: X Max
    :type xmax: typing.Optional[typing.Any]
    :param ymin: Y Min
    :type ymin: typing.Optional[typing.Any]
    :param ymax: Y Max
    :type ymax: typing.Optional[typing.Any]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    :type use_limit_to_segment: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def face_set_change_visibility(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Change the visibility of the Face Sets of the sculpt

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode * ``TOGGLE`` Toggle Visibility -- Hide all Face Sets except for the active one. * ``SHOW_ACTIVE`` Show Active Face Set -- Show Active Face Set. * ``HIDE_ACTIVE`` Hide Active Face Sets -- Hide Active Face Sets.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def face_set_edit(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        active_face_set: typing.Optional[typing.Any] = 1,
        mode: typing.Optional[typing.Any] = 'GROW',
        strength: typing.Optional[typing.Any] = 1.0,
        modify_hidden: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Edits the current active Face Set

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param active_face_set: Active Face Set
    :type active_face_set: typing.Optional[typing.Any]
    :param mode: Mode * ``GROW`` Grow Face Set -- Grows the Face Sets boundary by one face based on mesh topology. * ``SHRINK`` Shrink Face Set -- Shrinks the Face Sets boundary by one face based on mesh topology. * ``DELETE_GEOMETRY`` Delete Geometry -- Deletes the faces that are assigned to the Face Set. * ``FAIR_POSITIONS`` Fair Positions -- Creates a smooth as possible geometry patch from the Face Set minimizing changes in vertex positions. * ``FAIR_TANGENCY`` Fair Tangency -- Creates a smooth as possible geometry patch from the Face Set minimizing changes in vertex tangents.
    :type mode: typing.Optional[typing.Any]
    :param strength: Strength
    :type strength: typing.Optional[typing.Any]
    :param modify_hidden: Modify Hidden, Apply the edit operation to hidden Face Sets
    :type modify_hidden: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def face_set_invert_visibility(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Invert the visibility of the Face Sets of the sculpt

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def face_set_lasso_gesture(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        path: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorMousePath']] = None,
        use_front_faces_only: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        use_limit_to_segment: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False):
    ''' Add face set within the lasso as you move the brush

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param path: Path
    :type path: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']]
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    :type use_limit_to_segment: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def face_sets_create(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'MASKED'):
    ''' Create a new Face Set

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode * ``MASKED`` Face Set from Masked -- Create a new Face Set from the masked faces. * ``VISIBLE`` Face Set from Visible -- Create a new Face Set from the visible vertices. * ``ALL`` Face Set Full Mesh -- Create an unique Face Set with all faces in the sculpt. * ``SELECTION`` Face Set from Edit Mode Selection -- Create an Face Set corresponding to the Edit Mode face selection.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def face_sets_init(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'LOOSE_PARTS',
        threshold: typing.Optional[typing.Any] = 0.5):
    ''' Initializes all Face Sets in the mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode * ``LOOSE_PARTS`` Face Sets from Loose Parts -- Create a Face Set per loose part in the mesh. * ``MATERIALS`` Face Sets from Material Slots -- Create a Face Set per Material Slot. * ``NORMALS`` Face Sets from Mesh Normals -- Create Face Sets for Faces that have similar normal. * ``UV_SEAMS`` Face Sets from UV Seams -- Create Face Sets using UV Seams as boundaries. * ``CREASES`` Face Sets from Edge Creases -- Create Face Sets using Edge Creases as boundaries. * ``BEVEL_WEIGHT`` Face Sets from Bevel Weight -- Create Face Sets using Bevel Weights as boundaries. * ``SHARP_EDGES`` Face Sets from Sharp Edges -- Create Face Sets using Sharp Edges as boundaries. * ``FACE_SET_BOUNDARIES`` Face Sets from Face Set Boundaries -- Create a Face Set per isolated Face Set.
    :type mode: typing.Optional[typing.Any]
    :param threshold: Threshold, Minimum value to consider a certain attribute a boundary when creating the Face Sets
    :type threshold: typing.Optional[typing.Any]
    '''

    pass


def face_sets_randomize_colors(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Generates a new set of random colors to render the Face Sets in the viewport

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def mask_by_color(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        contiguous: typing.Optional[typing.Union[bool, typing.Any]] = False,
        invert: typing.Optional[typing.Union[bool, typing.Any]] = False,
        preserve_previous_mask: typing.Optional[typing.Union[bool, typing.
                                                             Any]] = False,
        threshold: typing.Optional[typing.Any] = 0.35):
    ''' Creates a mask based on the active color attribute

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param contiguous: Contiguous, Mask only contiguous color areas
    :type contiguous: typing.Optional[typing.Union[bool, typing.Any]]
    :param invert: Invert, Invert the generated mask
    :type invert: typing.Optional[typing.Union[bool, typing.Any]]
    :param preserve_previous_mask: Preserve Previous Mask, Preserve the previous mask and add or subtract the new one generated by the colors
    :type preserve_previous_mask: typing.Optional[typing.Union[bool, typing.Any]]
    :param threshold: Threshold, How much changes in color affect the mask generation
    :type threshold: typing.Optional[typing.Any]
    '''

    pass


def mask_filter(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filter_type: typing.Optional[typing.Any] = 'SMOOTH',
        iterations: typing.Optional[typing.Any] = 1,
        auto_iteration_count: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = True):
    ''' Applies a filter to modify the current mask

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filter_type: Type, Filter that is going to be applied to the mask * ``SMOOTH`` Smooth Mask -- Smooth mask. * ``SHARPEN`` Sharpen Mask -- Sharpen mask. * ``GROW`` Grow Mask -- Grow mask. * ``SHRINK`` Shrink Mask -- Shrink mask. * ``CONTRAST_INCREASE`` Increase Contrast -- Increase the contrast of the paint mask. * ``CONTRAST_DECREASE`` Decrease Contrast -- Decrease the contrast of the paint mask.
    :type filter_type: typing.Optional[typing.Any]
    :param iterations: Iterations, Number of times that the filter is going to be applied
    :type iterations: typing.Optional[typing.Any]
    :param auto_iteration_count: Auto Iteration Count, Use a automatic number of iterations based on the number of vertices of the sculpt
    :type auto_iteration_count: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def mask_from_cavity(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mix_mode: typing.Optional[typing.Any] = 'MIX',
        mix_factor: typing.Optional[typing.Any] = 1.0,
        settings_source: typing.Optional[typing.Any] = 'OPERATOR',
        factor: typing.Optional[typing.Any] = 0.5,
        blur_steps: typing.Optional[typing.Any] = 2,
        use_curve: typing.Optional[typing.Union[bool, typing.Any]] = False,
        invert: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Creates a mask based on the curvature of the surface

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mix_mode: Mode, Mix mode
    :type mix_mode: typing.Optional[typing.Any]
    :param mix_factor: Mix Factor
    :type mix_factor: typing.Optional[typing.Any]
    :param settings_source: Settings, Use settings from here * ``OPERATOR`` Operator -- Use settings from operator properties. * ``BRUSH`` Brush -- Use settings from brush. * ``SCENE`` Scene -- Use settings from scene.
    :type settings_source: typing.Optional[typing.Any]
    :param factor: Factor, The contrast of the cavity mask
    :type factor: typing.Optional[typing.Any]
    :param blur_steps: Blur, The number of times the cavity mask is blurred
    :type blur_steps: typing.Optional[typing.Any]
    :param use_curve: Custom Curve
    :type use_curve: typing.Optional[typing.Union[bool, typing.Any]]
    :param invert: Cavity (Inverted)
    :type invert: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def mask_init(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'RANDOM_PER_VERTEX'):
    ''' Creates a new mask for the entire mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def mesh_filter(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        start_mouse: typing.Optional[typing.Any] = (0, 0),
        area_normal_radius: typing.Optional[typing.Any] = 0.25,
        strength: typing.Optional[typing.Any] = 1.0,
        iteration_count: typing.Optional[typing.Any] = 1,
        event_history: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorStrokeElement']] = None,
        type: typing.Optional[typing.Any] = 'INFLATE',
        deform_axis: typing.Optional[typing.Any] = {'X', 'Y', 'Z'},
        orientation: typing.Optional[typing.Any] = 'LOCAL',
        surface_smooth_shape_preservation: typing.Optional[typing.Any] = 0.5,
        surface_smooth_current_vertex: typing.Optional[typing.Any] = 0.5,
        sharpen_smooth_ratio: typing.Optional[typing.Any] = 0.35,
        sharpen_intensify_detail_strength: typing.Optional[typing.Any] = 0.0,
        sharpen_curvature_smooth_iterations: typing.Optional[typing.Any] = 0):
    ''' Applies a filter to modify the current mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param start_mouse: Starting Mouse
    :type start_mouse: typing.Optional[typing.Any]
    :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
    :type area_normal_radius: typing.Optional[typing.Any]
    :param strength: Strength, Filter strength
    :type strength: typing.Optional[typing.Any]
    :param iteration_count: Repeat, How many times to repeat the filter
    :type iteration_count: typing.Optional[typing.Any]
    :type event_history: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param type: Filter Type, Operation that is going to be applied to the mesh * ``SMOOTH`` Smooth -- Smooth mesh. * ``SCALE`` Scale -- Scale mesh. * ``INFLATE`` Inflate -- Inflate mesh. * ``SPHERE`` Sphere -- Morph into sphere. * ``RANDOM`` Random -- Randomize vertex positions. * ``RELAX`` Relax -- Relax mesh. * ``RELAX_FACE_SETS`` Relax Face Sets -- Smooth the edges of all the Face Sets. * ``SURFACE_SMOOTH`` Surface Smooth -- Smooth the surface of the mesh, preserving the volume. * ``SHARPEN`` Sharpen -- Sharpen the cavities of the mesh. * ``ENHANCE_DETAILS`` Enhance Details -- Enhance the high frequency surface detail. * ``ERASE_DISCPLACEMENT`` Erase Displacement -- Deletes the displacement of the Multires Modifier.
    :type type: typing.Optional[typing.Any]
    :param deform_axis: Deform Axis, Apply the deformation in the selected axis * ``X`` X -- Deform in the X axis. * ``Y`` Y -- Deform in the Y axis. * ``Z`` Z -- Deform in the Z axis.
    :type deform_axis: typing.Optional[typing.Any]
    :param orientation: Orientation, Orientation of the axis to limit the filter displacement * ``LOCAL`` Local -- Use the local axis to limit the displacement. * ``WORLD`` World -- Use the global axis to limit the displacement. * ``VIEW`` View -- Use the view axis to limit the displacement.
    :type orientation: typing.Optional[typing.Any]
    :param surface_smooth_shape_preservation: Shape Preservation, How much of the original shape is preserved when smoothing
    :type surface_smooth_shape_preservation: typing.Optional[typing.Any]
    :param surface_smooth_current_vertex: Per Vertex Displacement, How much the position of each individual vertex influences the final result
    :type surface_smooth_current_vertex: typing.Optional[typing.Any]
    :param sharpen_smooth_ratio: Smooth Ratio, How much smoothing is applied to polished surfaces
    :type sharpen_smooth_ratio: typing.Optional[typing.Any]
    :param sharpen_intensify_detail_strength: Intensify Details, How much creases and valleys are intensified
    :type sharpen_intensify_detail_strength: typing.Optional[typing.Any]
    :param sharpen_curvature_smooth_iterations: Curvature Smooth Iterations, How much smooth the resulting shape is, ignoring high frequency details
    :type sharpen_curvature_smooth_iterations: typing.Optional[typing.Any]
    '''

    pass


def optimize(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None):
    ''' Recalculate the sculpt BVH to improve performance

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def project_line_gesture(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        xstart: typing.Optional[typing.Any] = 0,
        xend: typing.Optional[typing.Any] = 0,
        ystart: typing.Optional[typing.Any] = 0,
        yend: typing.Optional[typing.Any] = 0,
        flip: typing.Optional[typing.Union[bool, typing.Any]] = False,
        cursor: typing.Optional[typing.Any] = 5,
        use_front_faces_only: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        use_limit_to_segment: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False):
    ''' Project the geometry onto a plane defined by a line

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param xstart: X Start
    :type xstart: typing.Optional[typing.Any]
    :param xend: X End
    :type xend: typing.Optional[typing.Any]
    :param ystart: Y Start
    :type ystart: typing.Optional[typing.Any]
    :param yend: Y End
    :type yend: typing.Optional[typing.Any]
    :param flip: Flip
    :type flip: typing.Optional[typing.Union[bool, typing.Any]]
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: typing.Optional[typing.Any]
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    :type use_limit_to_segment: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def reveal_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Unhide all geometry

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def sample_color(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Sample the vertex color of the active vertex

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def sample_detail_size(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        location: typing.Optional[typing.Any] = (0, 0),
        mode: typing.Optional[typing.Any] = 'DYNTOPO'):
    ''' Sample the mesh detail on clicked point

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param location: Location, Screen coordinates of sampling
    :type location: typing.Optional[typing.Any]
    :param mode: Detail Mode, Target sculpting workflow that is going to use the sampled size * ``DYNTOPO`` Dyntopo -- Sample dyntopo detail. * ``VOXEL`` Voxel -- Sample mesh voxel size.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def sculptmode_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Toggle sculpt mode in 3D view

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def set_detail_size(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Set the mesh detail (either relative or constant one, depending on current dyntopo mode)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def set_persistent_base(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Reset the copy of the mesh that is being sculpted on

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def set_pivot_position(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'UNMASKED',
        mouse_x: typing.Optional[typing.Any] = 0.0,
        mouse_y: typing.Optional[typing.Any] = 0.0):
    ''' Sets the sculpt transform pivot position

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode * ``ORIGIN`` Origin -- Sets the pivot to the origin of the sculpt. * ``UNMASKED`` Unmasked -- Sets the pivot position to the average position of the unmasked vertices. * ``BORDER`` Mask Border -- Sets the pivot position to the center of the border of the mask. * ``ACTIVE`` Active Vertex -- Sets the pivot position to the active vertex position. * ``SURFACE`` Surface -- Sets the pivot position to the surface under the cursor.
    :type mode: typing.Optional[typing.Any]
    :param mouse_x: Mouse Position X, Position of the mouse used for "Surface" mode
    :type mouse_x: typing.Optional[typing.Any]
    :param mouse_y: Mouse Position Y, Position of the mouse used for "Surface" mode
    :type mouse_y: typing.Optional[typing.Any]
    '''

    pass


def symmetrize(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        merge_tolerance: typing.Optional[typing.Any] = 0.0005):
    ''' Symmetrize the topology modifications

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param merge_tolerance: Merge Distance, Distance within which symmetrical vertices are merged
    :type merge_tolerance: typing.Optional[typing.Any]
    '''

    pass


def trim_box_gesture(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        xmin: typing.Optional[typing.Any] = 0,
        xmax: typing.Optional[typing.Any] = 0,
        ymin: typing.Optional[typing.Any] = 0,
        ymax: typing.Optional[typing.Any] = 0,
        wait_for_input: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_front_faces_only: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        use_limit_to_segment: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        trim_mode: typing.Optional[typing.Any] = 'DIFFERENCE',
        use_cursor_depth: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        trim_orientation: typing.Optional[typing.Any] = 'VIEW',
        trim_extrude_mode: typing.Optional[typing.Any] = 'FIXED'):
    ''' Trims the mesh within the box as you move the brush

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param xmin: X Min
    :type xmin: typing.Optional[typing.Any]
    :param xmax: X Max
    :type xmax: typing.Optional[typing.Any]
    :param ymin: Y Min
    :type ymin: typing.Optional[typing.Any]
    :param ymax: Y Max
    :type ymax: typing.Optional[typing.Any]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    :type use_limit_to_segment: typing.Optional[typing.Union[bool, typing.Any]]
    :param trim_mode: Trim Mode * ``DIFFERENCE`` Difference -- Use a difference boolean operation. * ``UNION`` Union -- Use a union boolean operation. * ``JOIN`` Join -- Join the new mesh as separate geometry, without performing any boolean operation.
    :type trim_mode: typing.Optional[typing.Any]
    :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
    :type use_cursor_depth: typing.Optional[typing.Union[bool, typing.Any]]
    :param trim_orientation: Shape Orientation * ``VIEW`` View -- Use the view to orientate the trimming shape. * ``SURFACE`` Surface -- Use the surface normal to orientate the trimming shape.
    :type trim_orientation: typing.Optional[typing.Any]
    :param trim_extrude_mode: Extrude Mode * ``PROJECT`` Project -- Project back faces when extruding. * ``FIXED`` Fixed -- Extrude back faces by fixed amount.
    :type trim_extrude_mode: typing.Optional[typing.Any]
    '''

    pass


def trim_lasso_gesture(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        path: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorMousePath']] = None,
        use_front_faces_only: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        use_limit_to_segment: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        trim_mode: typing.Optional[typing.Any] = 'DIFFERENCE',
        use_cursor_depth: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        trim_orientation: typing.Optional[typing.Any] = 'VIEW',
        trim_extrude_mode: typing.Optional[typing.Any] = 'FIXED'):
    ''' Trims the mesh within the lasso as you move the brush

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param path: Path
    :type path: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']]
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    :type use_limit_to_segment: typing.Optional[typing.Union[bool, typing.Any]]
    :param trim_mode: Trim Mode * ``DIFFERENCE`` Difference -- Use a difference boolean operation. * ``UNION`` Union -- Use a union boolean operation. * ``JOIN`` Join -- Join the new mesh as separate geometry, without performing any boolean operation.
    :type trim_mode: typing.Optional[typing.Any]
    :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
    :type use_cursor_depth: typing.Optional[typing.Union[bool, typing.Any]]
    :param trim_orientation: Shape Orientation * ``VIEW`` View -- Use the view to orientate the trimming shape. * ``SURFACE`` Surface -- Use the surface normal to orientate the trimming shape.
    :type trim_orientation: typing.Optional[typing.Any]
    :param trim_extrude_mode: Extrude Mode * ``PROJECT`` Project -- Project back faces when extruding. * ``FIXED`` Fixed -- Extrude back faces by fixed amount.
    :type trim_extrude_mode: typing.Optional[typing.Any]
    '''

    pass


def uv_sculpt_stroke(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'NORMAL'):
    ''' Sculpt UVs using a brush

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode, Stroke Mode * ``NORMAL`` Regular -- Apply brush normally. * ``INVERT`` Invert -- Invert action of brush for duration of stroke. * ``RELAX`` Relax -- Switch brush to relax mode for duration of stroke.
    :type mode: typing.Optional[typing.Any]
    '''

    pass
