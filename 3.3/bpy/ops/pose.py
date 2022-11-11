import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def armature_apply(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   selected: bool = False):
    ''' Apply the current pose as the new rest pose

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param selected: Selected Only, Only apply the selected bones (with propagation to children)
    :type selected: bool
    '''

    pass


def autoside_names(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   axis: typing.Union[str, int] = 'XAXIS'):
    ''' Automatically renames the selected bones according to which side of the target axis they fall on

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param axis: Axis, Axis tag names with * XAXIS X-Axis -- Left/Right. * YAXIS Y-Axis -- Front/Back. * ZAXIS Z-Axis -- Top/Bottom.
    :type axis: typing.Union[str, int]
    '''

    pass


def blend_to_neighbor(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      factor: float = 0.5,
                      prev_frame: int = 0,
                      next_frame: int = 0,
                      channels: typing.Union[str, int] = 'ALL',
                      axis_lock: typing.Union[str, int] = 'FREE'):
    ''' Blend from current position to previous or next keyframe

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param factor: Factor, Weighting factor for which keyframe is favored more
    :type factor: float
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
    :type prev_frame: int
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
    :type next_frame: int
    :param channels: Channels, Set of properties that are affected * ALL All Properties -- All properties, including transforms, bendy bone shape, and custom properties. * LOC Location -- Location only. * ROT Rotation -- Rotation only. * SIZE Scale -- Scale only. * BBONE Bendy Bone -- Bendy Bone shape properties. * CUSTOM Custom Properties -- Custom properties.
    :type channels: typing.Union[str, int]
    :param axis_lock: Axis Lock, Transform axis to restrict effects to * FREE Free -- All axes are affected. * X X -- Only X-axis transforms are affected. * Y Y -- Only Y-axis transforms are affected. * Z Z -- Only Z-axis transforms are affected.
    :type axis_lock: typing.Union[str, int]
    '''

    pass


def bone_layers(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        layers: typing.List[bool] = (False, False, False, False, False, False,
                                     False, False, False, False, False, False,
                                     False, False, False, False, False, False,
                                     False, False, False, False, False, False,
                                     False, False, False, False, False, False,
                                     False, False)):
    ''' Change the layers that the selected bones belong to

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param layers: Layer, Armature layers that bone belongs to
    :type layers: typing.List[bool]
    '''

    pass


def breakdown(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              factor: float = 0.5,
              prev_frame: int = 0,
              next_frame: int = 0,
              channels: typing.Union[str, int] = 'ALL',
              axis_lock: typing.Union[str, int] = 'FREE'):
    ''' Create a suitable breakdown pose on the current frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param factor: Factor, Weighting factor for which keyframe is favored more
    :type factor: float
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
    :type prev_frame: int
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
    :type next_frame: int
    :param channels: Channels, Set of properties that are affected * ALL All Properties -- All properties, including transforms, bendy bone shape, and custom properties. * LOC Location -- Location only. * ROT Rotation -- Rotation only. * SIZE Scale -- Scale only. * BBONE Bendy Bone -- Bendy Bone shape properties. * CUSTOM Custom Properties -- Custom properties.
    :type channels: typing.Union[str, int]
    :param axis_lock: Axis Lock, Transform axis to restrict effects to * FREE Free -- All axes are affected. * X X -- Only X-axis transforms are affected. * Y Y -- Only Y-axis transforms are affected. * Z Z -- Only Z-axis transforms are affected.
    :type axis_lock: typing.Union[str, int]
    '''

    pass


def constraint_add(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   type: typing.Union[int, str] = ''):
    ''' Add a constraint to the active bone

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[int, str]
    '''

    pass


def constraint_add_with_targets(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        type: typing.Union[int, str] = ''):
    ''' Add a constraint to the active bone, with target (where applicable) set to the selected Objects/Bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[int, str]
    '''

    pass


def constraints_clear(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Clear all the constraints for the selected bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def constraints_copy(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Copy constraints to other selected bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def copy(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None):
    ''' Copies the current pose of the selected bones to copy/paste buffer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def flip_names(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               do_strip_numbers: bool = False):
    ''' Flips (and corrects) the axis suffixes of the names of selected bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param do_strip_numbers: Strip Numbers, Try to remove right-most dot-number from flipped names. Warning: May result in incoherent naming in some cases
    :type do_strip_numbers: bool
    '''

    pass


def group_add(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Add a new bone group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def group_assign(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 type: int = 0):
    ''' Add selected bones to the chosen bone group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Bone Group Index
    :type type: int
    '''

    pass


def group_deselect(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Deselect bones of active Bone Group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def group_move(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               direction: typing.Union[str, int] = 'UP'):
    ''' Change position of active Bone Group in list of Bone Groups

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param direction: Direction, Direction to move the active Bone Group towards
    :type direction: typing.Union[str, int]
    '''

    pass


def group_remove(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Remove the active bone group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def group_select(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Select bones in active Bone Group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def group_sort(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Sort Bone Groups by their names in ascending order

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def group_unassign(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Remove selected bones from all bone groups

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def hide(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         unselected: bool = False):
    ''' Tag selected bones to not be visible in Pose Mode

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param unselected: Unselected
    :type unselected: bool
    '''

    pass


def ik_add(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           with_targets: bool = True):
    ''' Add IK Constraint to the active Bone

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param with_targets: With Targets, Assign IK Constraint with targets derived from the select bones/objects
    :type with_targets: bool
    '''

    pass


def ik_clear(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None):
    ''' Remove all IK Constraints from selected bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def loc_clear(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Reset locations of selected bones to their default values

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def paste(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None,
          *,
          flipped: bool = False,
          selected_mask: bool = False):
    ''' Paste the stored pose on to the current pose

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param flipped: Flipped on X-Axis, Paste the stored pose flipped on to current pose
    :type flipped: bool
    :param selected_mask: On Selected Only, Only paste the stored pose on to selected bones in the current pose
    :type selected_mask: bool
    '''

    pass


def paths_calculate(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    display_type: typing.Union[int, str] = 'RANGE',
                    range: typing.Union[int, str] = 'SCENE',
                    bake_location: typing.Union[int, str] = 'HEADS'):
    ''' Calculate paths for the selected bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param display_type: Display type
    :type display_type: typing.Union[int, str]
    :param range: Computation Range
    :type range: typing.Union[int, str]
    :param bake_location: Bake Location, Which point on the bones is used when calculating paths
    :type bake_location: typing.Union[int, str]
    '''

    pass


def paths_clear(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                only_selected: bool = False):
    ''' Clear path caches for all bones, hold Shift key for selected bones only

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param only_selected: Only Selected, Only clear paths from selected bones
    :type only_selected: bool
    '''

    pass


def paths_range_update(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Update frame range for motion paths from the Scene's current frame range

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def paths_update(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Recalculate paths for bones that already have them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def propagate(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              mode: typing.Union[str, int] = 'WHILE_HELD',
              end_frame: float = 250.0):
    ''' Copy selected aspects of the current pose to subsequent poses already keyframed

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Terminate Mode, Method used to determine when to stop propagating pose to keyframes * WHILE_HELD While Held -- Propagate pose to all keyframes after current frame that don't change (Default behavior). * NEXT_KEY To Next Keyframe -- Propagate pose to first keyframe following the current frame only. * LAST_KEY To Last Keyframe -- Propagate pose to the last keyframe only (i.e. making action cyclic). * BEFORE_FRAME Before Frame -- Propagate pose to all keyframes between current frame and 'Frame' property. * BEFORE_END Before Last Keyframe -- Propagate pose to all keyframes from current frame until no more are found. * SELECTED_KEYS On Selected Keyframes -- Propagate pose to all selected keyframes. * SELECTED_MARKERS On Selected Markers -- Propagate pose to all keyframes occurring on frames with Scene Markers after the current frame.
    :type mode: typing.Union[str, int]
    :param end_frame: End Frame, Frame to stop propagating frames to (for 'Before Frame' mode)
    :type end_frame: float
    '''

    pass


def push(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         factor: float = 0.5,
         prev_frame: int = 0,
         next_frame: int = 0,
         channels: typing.Union[str, int] = 'ALL',
         axis_lock: typing.Union[str, int] = 'FREE'):
    ''' Exaggerate the current pose in regards to the breakdown pose

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param factor: Factor, Weighting factor for which keyframe is favored more
    :type factor: float
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
    :type prev_frame: int
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
    :type next_frame: int
    :param channels: Channels, Set of properties that are affected * ALL All Properties -- All properties, including transforms, bendy bone shape, and custom properties. * LOC Location -- Location only. * ROT Rotation -- Rotation only. * SIZE Scale -- Scale only. * BBONE Bendy Bone -- Bendy Bone shape properties. * CUSTOM Custom Properties -- Custom properties.
    :type channels: typing.Union[str, int]
    :param axis_lock: Axis Lock, Transform axis to restrict effects to * FREE Free -- All axes are affected. * X X -- Only X-axis transforms are affected. * Y Y -- Only Y-axis transforms are affected. * Z Z -- Only Z-axis transforms are affected.
    :type axis_lock: typing.Union[str, int]
    '''

    pass


def push_rest(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              factor: float = 0.5,
              prev_frame: int = 0,
              next_frame: int = 0,
              channels: typing.Union[str, int] = 'ALL',
              axis_lock: typing.Union[str, int] = 'FREE'):
    ''' Push the current pose further away from the rest pose

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param factor: Factor, Weighting factor for which keyframe is favored more
    :type factor: float
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
    :type prev_frame: int
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
    :type next_frame: int
    :param channels: Channels, Set of properties that are affected * ALL All Properties -- All properties, including transforms, bendy bone shape, and custom properties. * LOC Location -- Location only. * ROT Rotation -- Rotation only. * SIZE Scale -- Scale only. * BBONE Bendy Bone -- Bendy Bone shape properties. * CUSTOM Custom Properties -- Custom properties.
    :type channels: typing.Union[str, int]
    :param axis_lock: Axis Lock, Transform axis to restrict effects to * FREE Free -- All axes are affected. * X X -- Only X-axis transforms are affected. * Y Y -- Only Y-axis transforms are affected. * Z Z -- Only Z-axis transforms are affected.
    :type axis_lock: typing.Union[str, int]
    '''

    pass


def quaternions_flip(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Flip quaternion values to achieve desired rotations, while maintaining the same orientations

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def relax(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None,
          *,
          factor: float = 0.5,
          prev_frame: int = 0,
          next_frame: int = 0,
          channels: typing.Union[str, int] = 'ALL',
          axis_lock: typing.Union[str, int] = 'FREE'):
    ''' Make the current pose more similar to its breakdown pose

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param factor: Factor, Weighting factor for which keyframe is favored more
    :type factor: float
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
    :type prev_frame: int
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
    :type next_frame: int
    :param channels: Channels, Set of properties that are affected * ALL All Properties -- All properties, including transforms, bendy bone shape, and custom properties. * LOC Location -- Location only. * ROT Rotation -- Rotation only. * SIZE Scale -- Scale only. * BBONE Bendy Bone -- Bendy Bone shape properties. * CUSTOM Custom Properties -- Custom properties.
    :type channels: typing.Union[str, int]
    :param axis_lock: Axis Lock, Transform axis to restrict effects to * FREE Free -- All axes are affected. * X X -- Only X-axis transforms are affected. * Y Y -- Only Y-axis transforms are affected. * Z Z -- Only Z-axis transforms are affected.
    :type axis_lock: typing.Union[str, int]
    '''

    pass


def relax_rest(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               factor: float = 0.5,
               prev_frame: int = 0,
               next_frame: int = 0,
               channels: typing.Union[str, int] = 'ALL',
               axis_lock: typing.Union[str, int] = 'FREE'):
    ''' Make the current pose more similar to the rest pose

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param factor: Factor, Weighting factor for which keyframe is favored more
    :type factor: float
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
    :type prev_frame: int
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
    :type next_frame: int
    :param channels: Channels, Set of properties that are affected * ALL All Properties -- All properties, including transforms, bendy bone shape, and custom properties. * LOC Location -- Location only. * ROT Rotation -- Rotation only. * SIZE Scale -- Scale only. * BBONE Bendy Bone -- Bendy Bone shape properties. * CUSTOM Custom Properties -- Custom properties.
    :type channels: typing.Union[str, int]
    :param axis_lock: Axis Lock, Transform axis to restrict effects to * FREE Free -- All axes are affected. * X X -- Only X-axis transforms are affected. * Y Y -- Only Y-axis transforms are affected. * Z Z -- Only Z-axis transforms are affected.
    :type axis_lock: typing.Union[str, int]
    '''

    pass


def reveal(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           select: bool = True):
    ''' Reveal all bones hidden in Pose Mode

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param select: Select
    :type select: bool
    '''

    pass


def rot_clear(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Reset rotations of selected bones to their default values

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def rotation_mode_set(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      type: typing.Union[int, str] = 'QUATERNION'):
    ''' Set the rotation representation used by selected bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Rotation Mode
    :type type: typing.Union[int, str]
    '''

    pass


def scale_clear(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Reset scaling of selected bones to their default values

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               action: typing.Union[str, int] = 'TOGGLE'):
    ''' Toggle selection status of all bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_constraint_target(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None):
    ''' Select bones used as targets for the currently selected bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_grouped(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   extend: bool = False,
                   type: typing.Union[str, int] = 'LAYER'):
    ''' Select all visible bones grouped by similar properties

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param type: Type * LAYER Layer -- Shared layers. * GROUP Group -- Shared group. * KEYINGSET Keying Set -- All bones affected by active Keying Set.
    :type type: typing.Union[str, int]
    '''

    pass


def select_hierarchy(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     direction: typing.Union[str, int] = 'PARENT',
                     extend: bool = False):
    ''' Select immediate parent/children of selected bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param direction: Direction
    :type direction: typing.Union[str, int]
    :param extend: Extend, Extend the selection
    :type extend: bool
    '''

    pass


def select_linked(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Select all bones linked by parent/child connections to the current selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_linked_pick(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       extend: bool = False):
    ''' Select bones linked by parent/child connections under the mouse cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    '''

    pass


def select_mirror(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  only_active: bool = False,
                  extend: bool = False):
    ''' Mirror the bone selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param only_active: Active Only, Only operate on the active bone
    :type only_active: bool
    :param extend: Extend, Extend the selection
    :type extend: bool
    '''

    pass


def select_parent(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Select bones that are parents of the currently selected bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def transforms_clear(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Reset location, rotation, and scaling of selected bones to their default values

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def user_transforms_clear(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          only_selected: bool = True):
    ''' Reset pose bone transforms to keyframed state

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param only_selected: Only Selected, Only visible/selected bones
    :type only_selected: bool
    '''

    pass


def visual_transform_apply(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None):
    ''' Apply final constrained position of pose bones to their transform

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass
