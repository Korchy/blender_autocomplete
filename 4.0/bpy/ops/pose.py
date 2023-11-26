import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def armature_apply(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        selected: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Apply the current pose as the new rest pose

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param selected: Selected Only, Only apply the selected bones (with propagation to children)
    :type selected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def autoside_names(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        axis: typing.Optional[typing.Any] = 'XAXIS'):
    ''' Automatically renames the selected bones according to which side of the target axis they fall on

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param axis: Axis, Axis to tag names with * ``XAXIS`` X-Axis -- Left/Right. * ``YAXIS`` Y-Axis -- Front/Back. * ``ZAXIS`` Z-Axis -- Top/Bottom.
    :type axis: typing.Optional[typing.Any]
    '''

    pass


def blend_to_neighbor(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 0.5,
        prev_frame: typing.Optional[typing.Any] = 0,
        next_frame: typing.Optional[typing.Any] = 0,
        channels: typing.Optional[typing.Any] = 'ALL',
        axis_lock: typing.Optional[typing.Any] = 'FREE'):
    ''' Blend from current position to previous or next keyframe

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor, Weighting factor for which keyframe is favored more
    :type factor: typing.Optional[typing.Any]
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
    :type prev_frame: typing.Optional[typing.Any]
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
    :type next_frame: typing.Optional[typing.Any]
    :param channels: Channels, Set of properties that are affected * ``ALL`` All Properties -- All properties, including transforms, bendy bone shape, and custom properties. * ``LOC`` Location -- Location only. * ``ROT`` Rotation -- Rotation only. * ``SIZE`` Scale -- Scale only. * ``BBONE`` Bendy Bone -- Bendy Bone shape properties. * ``CUSTOM`` Custom Properties -- Custom properties.
    :type channels: typing.Optional[typing.Any]
    :param axis_lock: Axis Lock, Transform axis to restrict effects to * ``FREE`` Free -- All axes are affected. * ``X`` X -- Only X-axis transforms are affected. * ``Y`` Y -- Only Y-axis transforms are affected. * ``Z`` Z -- Only Z-axis transforms are affected.
    :type axis_lock: typing.Optional[typing.Any]
    '''

    pass


def blend_with_rest(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 0.5,
        prev_frame: typing.Optional[typing.Any] = 0,
        next_frame: typing.Optional[typing.Any] = 0,
        channels: typing.Optional[typing.Any] = 'ALL',
        axis_lock: typing.Optional[typing.Any] = 'FREE'):
    ''' Make the current pose more similar to, or further away from, the rest pose

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor, Weighting factor for which keyframe is favored more
    :type factor: typing.Optional[typing.Any]
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
    :type prev_frame: typing.Optional[typing.Any]
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
    :type next_frame: typing.Optional[typing.Any]
    :param channels: Channels, Set of properties that are affected * ``ALL`` All Properties -- All properties, including transforms, bendy bone shape, and custom properties. * ``LOC`` Location -- Location only. * ``ROT`` Rotation -- Rotation only. * ``SIZE`` Scale -- Scale only. * ``BBONE`` Bendy Bone -- Bendy Bone shape properties. * ``CUSTOM`` Custom Properties -- Custom properties.
    :type channels: typing.Optional[typing.Any]
    :param axis_lock: Axis Lock, Transform axis to restrict effects to * ``FREE`` Free -- All axes are affected. * ``X`` X -- Only X-axis transforms are affected. * ``Y`` Y -- Only Y-axis transforms are affected. * ``Z`` Z -- Only Z-axis transforms are affected.
    :type axis_lock: typing.Optional[typing.Any]
    '''

    pass


def breakdown(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 0.5,
        prev_frame: typing.Optional[typing.Any] = 0,
        next_frame: typing.Optional[typing.Any] = 0,
        channels: typing.Optional[typing.Any] = 'ALL',
        axis_lock: typing.Optional[typing.Any] = 'FREE'):
    ''' Create a suitable breakdown pose on the current frame

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor, Weighting factor for which keyframe is favored more
    :type factor: typing.Optional[typing.Any]
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
    :type prev_frame: typing.Optional[typing.Any]
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
    :type next_frame: typing.Optional[typing.Any]
    :param channels: Channels, Set of properties that are affected * ``ALL`` All Properties -- All properties, including transforms, bendy bone shape, and custom properties. * ``LOC`` Location -- Location only. * ``ROT`` Rotation -- Rotation only. * ``SIZE`` Scale -- Scale only. * ``BBONE`` Bendy Bone -- Bendy Bone shape properties. * ``CUSTOM`` Custom Properties -- Custom properties.
    :type channels: typing.Optional[typing.Any]
    :param axis_lock: Axis Lock, Transform axis to restrict effects to * ``FREE`` Free -- All axes are affected. * ``X`` X -- Only X-axis transforms are affected. * ``Y`` Y -- Only Y-axis transforms are affected. * ``Z`` Z -- Only Z-axis transforms are affected.
    :type axis_lock: typing.Optional[typing.Any]
    '''

    pass


def constraint_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = ''):
    ''' Add a constraint to the active bone

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def constraint_add_with_targets(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = ''):
    ''' Add a constraint to the active bone, with target (where applicable) set to the selected Objects/Bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def constraints_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Clear all constraints from the selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def constraints_copy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Copy constraints to other selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def copy(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None):
    ''' Copy the current pose of the selected bones to the internal clipboard

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def flip_names(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        do_strip_numbers: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False):
    ''' Flips (and corrects) the axis suffixes of the names of selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param do_strip_numbers: May result in incoherent naming in some cases
    :type do_strip_numbers: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def hide(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         unselected: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Tag selected bones to not be visible in Pose Mode

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected
    :type unselected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def ik_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        with_targets: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Add IK Constraint to the active Bone

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param with_targets: With Targets, Assign IK Constraint with targets derived from the select bones/objects
    :type with_targets: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def ik_clear(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None):
    ''' Remove all IK Constraints from selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def loc_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Reset locations of selected bones to their default values

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def paste(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None,
          *,
          flipped: typing.Optional[typing.Union[bool, typing.Any]] = False,
          selected_mask: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False):
    ''' Paste the stored pose on to the current pose

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param flipped: Flipped on X-Axis, Paste the stored pose flipped on to current pose
    :type flipped: typing.Optional[typing.Union[bool, typing.Any]]
    :param selected_mask: On Selected Only, Only paste the stored pose on to selected bones in the current pose
    :type selected_mask: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def paths_calculate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        display_type: typing.Optional[typing.Union[str, int]] = 'RANGE',
        range: typing.Optional[typing.Union[str, int]] = 'SCENE',
        bake_location: typing.Optional[typing.Union[str, int]] = 'HEADS'):
    ''' Calculate paths for the selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param display_type: Display type
    :type display_type: typing.Optional[typing.Union[str, int]]
    :param range: Computation Range
    :type range: typing.Optional[typing.Union[str, int]]
    :param bake_location: Bake Location, Which point on the bones is used when calculating paths
    :type bake_location: typing.Optional[typing.Union[str, int]]
    '''

    pass


def paths_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        only_selected: typing.Optional[typing.Union[bool, typing.
                                                    Any]] = False):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param only_selected: Only Selected, Only clear motion paths of selected bones
    :type only_selected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def paths_range_update(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Update frame range for motion paths from the Scene's current frame range

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def paths_update(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Recalculate paths for bones that already have them

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def propagate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'NEXT_KEY',
        end_frame: typing.Optional[typing.Any] = 250.0):
    ''' Copy selected aspects of the current pose to subsequent poses already keyframed

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Terminate Mode, Method used to determine when to stop propagating pose to keyframes * ``NEXT_KEY`` To Next Keyframe -- Propagate pose to first keyframe following the current frame only. * ``LAST_KEY`` To Last Keyframe -- Propagate pose to the last keyframe only (i.e. making action cyclic). * ``BEFORE_FRAME`` Before Frame -- Propagate pose to all keyframes between current frame and 'Frame' property. * ``BEFORE_END`` Before Last Keyframe -- Propagate pose to all keyframes from current frame until no more are found. * ``SELECTED_KEYS`` On Selected Keyframes -- Propagate pose to all selected keyframes. * ``SELECTED_MARKERS`` On Selected Markers -- Propagate pose to all keyframes occurring on frames with Scene Markers after the current frame.
    :type mode: typing.Optional[typing.Any]
    :param end_frame: End Frame, Frame to stop propagating frames to (for 'Before Frame' mode)
    :type end_frame: typing.Optional[typing.Any]
    '''

    pass


def push(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         factor: typing.Optional[typing.Any] = 0.5,
         prev_frame: typing.Optional[typing.Any] = 0,
         next_frame: typing.Optional[typing.Any] = 0,
         channels: typing.Optional[typing.Any] = 'ALL',
         axis_lock: typing.Optional[typing.Any] = 'FREE'):
    ''' Exaggerate the current pose in regards to the breakdown pose

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor, Weighting factor for which keyframe is favored more
    :type factor: typing.Optional[typing.Any]
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
    :type prev_frame: typing.Optional[typing.Any]
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
    :type next_frame: typing.Optional[typing.Any]
    :param channels: Channels, Set of properties that are affected * ``ALL`` All Properties -- All properties, including transforms, bendy bone shape, and custom properties. * ``LOC`` Location -- Location only. * ``ROT`` Rotation -- Rotation only. * ``SIZE`` Scale -- Scale only. * ``BBONE`` Bendy Bone -- Bendy Bone shape properties. * ``CUSTOM`` Custom Properties -- Custom properties.
    :type channels: typing.Optional[typing.Any]
    :param axis_lock: Axis Lock, Transform axis to restrict effects to * ``FREE`` Free -- All axes are affected. * ``X`` X -- Only X-axis transforms are affected. * ``Y`` Y -- Only Y-axis transforms are affected. * ``Z`` Z -- Only Z-axis transforms are affected.
    :type axis_lock: typing.Optional[typing.Any]
    '''

    pass


def quaternions_flip(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Flip quaternion values to achieve desired rotations, while maintaining the same orientations

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def relax(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None,
          *,
          factor: typing.Optional[typing.Any] = 0.5,
          prev_frame: typing.Optional[typing.Any] = 0,
          next_frame: typing.Optional[typing.Any] = 0,
          channels: typing.Optional[typing.Any] = 'ALL',
          axis_lock: typing.Optional[typing.Any] = 'FREE'):
    ''' Make the current pose more similar to its breakdown pose

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor, Weighting factor for which keyframe is favored more
    :type factor: typing.Optional[typing.Any]
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
    :type prev_frame: typing.Optional[typing.Any]
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
    :type next_frame: typing.Optional[typing.Any]
    :param channels: Channels, Set of properties that are affected * ``ALL`` All Properties -- All properties, including transforms, bendy bone shape, and custom properties. * ``LOC`` Location -- Location only. * ``ROT`` Rotation -- Rotation only. * ``SIZE`` Scale -- Scale only. * ``BBONE`` Bendy Bone -- Bendy Bone shape properties. * ``CUSTOM`` Custom Properties -- Custom properties.
    :type channels: typing.Optional[typing.Any]
    :param axis_lock: Axis Lock, Transform axis to restrict effects to * ``FREE`` Free -- All axes are affected. * ``X`` X -- Only X-axis transforms are affected. * ``Y`` Y -- Only Y-axis transforms are affected. * ``Z`` Z -- Only Z-axis transforms are affected.
    :type axis_lock: typing.Optional[typing.Any]
    '''

    pass


def reveal(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None,
           *,
           select: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Reveal all bones hidden in Pose Mode

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param select: Select
    :type select: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def rot_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Reset rotations of selected bones to their default values

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def rotation_mode_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'QUATERNION'):
    ''' Set the rotation representation used by selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Rotation Mode
    :type type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def scale_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Reset scaling of selected bones to their default values

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Toggle selection status of all bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param action: Action, Selection action to execute * ``TOGGLE`` Toggle -- Toggle selection for all elements. * ``SELECT`` Select -- Select all elements. * ``DESELECT`` Deselect -- Deselect all elements. * ``INVERT`` Invert -- Invert selection of all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_constraint_target(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select bones used as targets for the currently selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_grouped(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False,
        type: typing.Optional[typing.Any] = 'COLLECTION'):
    ''' Select all visible bones grouped by similar properties

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    :param type: Type * ``COLLECTION`` Collection -- Same collections as the active bone. * ``COLOR`` Color -- Same color as the active bone. * ``KEYINGSET`` Keying Set -- All bones affected by active Keying Set.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def select_hierarchy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        direction: typing.Optional[typing.Any] = 'PARENT',
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select immediate parent/children of selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param direction: Direction
    :type direction: typing.Optional[typing.Any]
    :param extend: Extend, Extend the selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_linked(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select all bones linked by parent/child connections to the current selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_linked_pick(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select bones linked by parent/child connections under the mouse cursor

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_mirror(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        only_active: typing.Optional[typing.Union[bool, typing.Any]] = False,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Mirror the bone selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param only_active: Active Only, Only operate on the active bone
    :type only_active: typing.Optional[typing.Union[bool, typing.Any]]
    :param extend: Extend, Extend the selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_parent(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select bones that are parents of the currently selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def transforms_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Reset location, rotation, and scaling of selected bones to their default values

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def user_transforms_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        only_selected: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Reset pose bone transforms to keyframed state

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param only_selected: Only Selected, Only visible/selected bones
    :type only_selected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def visual_transform_apply(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Apply final constrained position of pose bones to their transform

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass
