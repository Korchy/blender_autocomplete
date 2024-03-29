import sys
import typing
import bpy.types
import mathutils

GenericType = typing.TypeVar("GenericType")


def bbone_resize(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                1.0, 1.0, 1.0),
        orient_type: typing.Union[str, int] = 'GLOBAL',
        orient_matrix: typing.
        Union[typing.List[typing.List[float]], typing.
              Tuple[typing.Tuple[float, float, float], typing.
                    Tuple[float, float, float], typing.
                    Tuple[float, float, float]], 'mathutils.Matrix'] = ((0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0)),
        orient_matrix_type: typing.Union[str, int] = 'GLOBAL',
        constraint_axis: typing.List[bool] = (False, False, False),
        mirror: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Scale selected bendy bones display size

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Display Size
    :type value: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: typing.Union[str, int]
    :param orient_matrix: Matrix
    :type orient_matrix: typing.Union[typing.List[typing.List[float]], typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]], 'mathutils.Matrix']
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: typing.Union[str, int]
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.List[bool]
    :param mirror: Mirror Editing
    :type mirror: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def bend(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         value: typing.Union[typing.List[float], typing.
                             Tuple[float], 'mathutils.Vector'] = (0.0),
         mirror: bool = False,
         use_proportional_edit: bool = False,
         proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
         proportional_size: float = 1.0,
         use_proportional_connected: bool = False,
         use_proportional_projected: bool = False,
         snap: bool = False,
         snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
             'INCREMENT'
         },
         use_snap_project: bool = False,
         snap_target: typing.Union[int, str] = 'CLOSEST',
         use_snap_self: bool = True,
         use_snap_edit: bool = True,
         use_snap_nonedit: bool = True,
         use_snap_selectable_only: bool = False,
         use_snap_to_same_target: bool = False,
         snap_face_nearest_steps: int = 1,
         snap_point: typing.
         Union[typing.List[float], typing.
               Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                  0.0),
         snap_align: bool = False,
         snap_normal: typing.
         Union[typing.List[float], typing.
               Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                  0.0),
         gpencil_strokes: bool = False,
         center_override: typing.
         Union[typing.List[float], typing.
               Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                  0.0),
         release_confirm: bool = False,
         use_accurate: bool = False):
    ''' Bend selected items between the 3D cursor and the mouse

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Angle
    :type value: typing.Union[typing.List[float], typing.Tuple[float], 'mathutils.Vector']
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param center_override: Center Override, Force using this center value (when set)
    :type center_override: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def create_orientation(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       name: str = "",
                       use_view: bool = False,
                       use: bool = False,
                       overwrite: bool = False):
    ''' Create transformation orientation from selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the new custom orientation
    :type name: str
    :param use_view: Use View, Use the current view instead of the active object to create the new orientation
    :type use_view: bool
    :param use: Use After Creation, Select orientation after its creation
    :type use: bool
    :param overwrite: Overwrite Previous, Overwrite previously created orientation with same name
    :type overwrite: bool
    '''

    pass


def delete_orientation(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Delete transformation orientation

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def edge_bevelweight(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        snap: bool = False,
        snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
            'INCREMENT'
        },
        use_snap_project: bool = False,
        snap_target: typing.Union[int, str] = 'CLOSEST',
        use_snap_self: bool = True,
        use_snap_edit: bool = True,
        use_snap_nonedit: bool = True,
        use_snap_selectable_only: bool = False,
        use_snap_to_same_target: bool = False,
        snap_face_nearest_steps: int = 1,
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Change the bevel weight of edges

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Factor
    :type value: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def edge_crease(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        snap: bool = False,
        snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
            'INCREMENT'
        },
        use_snap_project: bool = False,
        snap_target: typing.Union[int, str] = 'CLOSEST',
        use_snap_self: bool = True,
        use_snap_edit: bool = True,
        use_snap_nonedit: bool = True,
        use_snap_selectable_only: bool = False,
        use_snap_to_same_target: bool = False,
        snap_face_nearest_steps: int = 1,
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Change the crease of edges

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Factor
    :type value: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def edge_slide(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        single_side: bool = False,
        use_even: bool = False,
        flipped: bool = False,
        use_clamp: bool = True,
        mirror: bool = False,
        snap: bool = False,
        snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
            'INCREMENT'
        },
        use_snap_project: bool = False,
        snap_target: typing.Union[int, str] = 'CLOSEST',
        use_snap_self: bool = True,
        use_snap_edit: bool = True,
        use_snap_nonedit: bool = True,
        use_snap_selectable_only: bool = False,
        use_snap_to_same_target: bool = False,
        snap_face_nearest_steps: int = 1,
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        correct_uv: bool = True,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Slide an edge loop along a mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Factor
    :type value: float
    :param single_side: Single Side
    :type single_side: bool
    :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop
    :type use_even: bool
    :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
    :type flipped: bool
    :param use_clamp: Clamp, Clamp within the edge extents
    :type use_clamp: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param correct_uv: Correct UVs, Correct UV coordinates when transforming
    :type correct_uv: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def from_gizmo(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Transform selected items by mode type

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def mirror(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        orient_type: typing.Union[str, int] = 'GLOBAL',
        orient_matrix: typing.
        Union[typing.List[typing.List[float]], typing.
              Tuple[typing.Tuple[float, float, float], typing.
                    Tuple[float, float, float], typing.
                    Tuple[float, float, float]], 'mathutils.Matrix'] = ((0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0)),
        orient_matrix_type: typing.Union[str, int] = 'GLOBAL',
        constraint_axis: typing.List[bool] = (False, False, False),
        gpencil_strokes: bool = False,
        center_override: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Mirror selected items around one or more axes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: typing.Union[str, int]
    :param orient_matrix: Matrix
    :type orient_matrix: typing.Union[typing.List[typing.List[float]], typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]], 'mathutils.Matrix']
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: typing.Union[str, int]
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.List[bool]
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param center_override: Center Override, Force using this center value (when set)
    :type center_override: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def push_pull(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        mirror: bool = False,
        use_proportional_edit: bool = False,
        proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
        proportional_size: float = 1.0,
        use_proportional_connected: bool = False,
        use_proportional_projected: bool = False,
        snap: bool = False,
        snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
            'INCREMENT'
        },
        use_snap_project: bool = False,
        snap_target: typing.Union[int, str] = 'CLOSEST',
        use_snap_self: bool = True,
        use_snap_edit: bool = True,
        use_snap_nonedit: bool = True,
        use_snap_selectable_only: bool = False,
        use_snap_to_same_target: bool = False,
        snap_face_nearest_steps: int = 1,
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        center_override: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Push/Pull selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Distance
    :type value: float
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param center_override: Center Override, Force using this center value (when set)
    :type center_override: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def resize(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                1.0, 1.0, 1.0),
        mouse_dir_constraint: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        orient_type: typing.Union[str, int] = 'GLOBAL',
        orient_matrix: typing.
        Union[typing.List[typing.List[float]], typing.
              Tuple[typing.Tuple[float, float, float], typing.
                    Tuple[float, float, float], typing.
                    Tuple[float, float, float]], 'mathutils.Matrix'] = ((0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0)),
        orient_matrix_type: typing.Union[str, int] = 'GLOBAL',
        constraint_axis: typing.List[bool] = (False, False, False),
        mirror: bool = False,
        use_proportional_edit: bool = False,
        proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
        proportional_size: float = 1.0,
        use_proportional_connected: bool = False,
        use_proportional_projected: bool = False,
        snap: bool = False,
        snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
            'INCREMENT'
        },
        use_snap_project: bool = False,
        snap_target: typing.Union[int, str] = 'CLOSEST',
        use_snap_self: bool = True,
        use_snap_edit: bool = True,
        use_snap_nonedit: bool = True,
        use_snap_selectable_only: bool = False,
        use_snap_to_same_target: bool = False,
        snap_face_nearest_steps: int = 1,
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        gpencil_strokes: bool = False,
        texture_space: bool = False,
        remove_on_cancel: bool = False,
        center_override: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Scale (resize) selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Scale
    :type value: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param mouse_dir_constraint: Mouse Directional Constraint
    :type mouse_dir_constraint: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: typing.Union[str, int]
    :param orient_matrix: Matrix
    :type orient_matrix: typing.Union[typing.List[typing.List[float]], typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]], 'mathutils.Matrix']
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: typing.Union[str, int]
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.List[bool]
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param texture_space: Edit Texture Space, Edit object data texture space
    :type texture_space: bool
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
    :type remove_on_cancel: bool
    :param center_override: Center Override, Force using this center value (when set)
    :type center_override: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def rotate(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        orient_axis: typing.Union[int, str] = 'Z',
        orient_type: typing.Union[str, int] = 'GLOBAL',
        orient_matrix: typing.
        Union[typing.List[typing.List[float]], typing.
              Tuple[typing.Tuple[float, float, float], typing.
                    Tuple[float, float, float], typing.
                    Tuple[float, float, float]], 'mathutils.Matrix'] = ((0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0)),
        orient_matrix_type: typing.Union[str, int] = 'GLOBAL',
        constraint_axis: typing.List[bool] = (False, False, False),
        mirror: bool = False,
        use_proportional_edit: bool = False,
        proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
        proportional_size: float = 1.0,
        use_proportional_connected: bool = False,
        use_proportional_projected: bool = False,
        snap: bool = False,
        snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
            'INCREMENT'
        },
        use_snap_project: bool = False,
        snap_target: typing.Union[int, str] = 'CLOSEST',
        use_snap_self: bool = True,
        use_snap_edit: bool = True,
        use_snap_nonedit: bool = True,
        use_snap_selectable_only: bool = False,
        use_snap_to_same_target: bool = False,
        snap_face_nearest_steps: int = 1,
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        gpencil_strokes: bool = False,
        center_override: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Rotate selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Angle
    :type value: float
    :param orient_axis: Axis
    :type orient_axis: typing.Union[int, str]
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: typing.Union[str, int]
    :param orient_matrix: Matrix
    :type orient_matrix: typing.Union[typing.List[typing.List[float]], typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]], 'mathutils.Matrix']
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: typing.Union[str, int]
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.List[bool]
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param center_override: Center Override, Force using this center value (when set)
    :type center_override: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def rotate_normal(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        orient_axis: typing.Union[int, str] = 'Z',
        orient_type: typing.Union[str, int] = 'GLOBAL',
        orient_matrix: typing.
        Union[typing.List[typing.List[float]], typing.
              Tuple[typing.Tuple[float, float, float], typing.
                    Tuple[float, float, float], typing.
                    Tuple[float, float, float]], 'mathutils.Matrix'] = ((0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0)),
        orient_matrix_type: typing.Union[str, int] = 'GLOBAL',
        constraint_axis: typing.List[bool] = (False, False, False),
        mirror: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Rotate split normal of selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Angle
    :type value: float
    :param orient_axis: Axis
    :type orient_axis: typing.Union[int, str]
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: typing.Union[str, int]
    :param orient_matrix: Matrix
    :type orient_matrix: typing.Union[typing.List[typing.List[float]], typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]], 'mathutils.Matrix']
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: typing.Union[str, int]
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.List[bool]
    :param mirror: Mirror Editing
    :type mirror: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def select_orientation(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       orientation: typing.Union[str, int] = 'GLOBAL'):
    ''' Select transformation orientation

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param orientation: Orientation, Transformation orientation
    :type orientation: typing.Union[str, int]
    '''

    pass


def seq_slide(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: typing.Union[typing.List[float], typing.
                            Tuple[float, float], 'mathutils.Vector'] = (0.0,
                                                                        0.0),
        orient_axis_ortho: typing.Union[int, str] = 'X',
        snap: bool = False,
        snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
            'INCREMENT'
        },
        use_snap_project: bool = False,
        snap_target: typing.Union[int, str] = 'CLOSEST',
        use_snap_self: bool = True,
        use_snap_edit: bool = True,
        use_snap_nonedit: bool = True,
        use_snap_selectable_only: bool = False,
        use_snap_to_same_target: bool = False,
        snap_face_nearest_steps: int = 1,
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        view2d_edge_pan: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Slide a sequence strip in time

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Offset
    :type value: typing.Union[typing.List[float], typing.Tuple[float, float], 'mathutils.Vector']
    :param orient_axis_ortho: Axis Ortho
    :type orient_axis_ortho: typing.Union[int, str]
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param view2d_edge_pan: Edge Pan, Enable edge panning in 2D view
    :type view2d_edge_pan: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def shear(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        orient_axis: typing.Union[int, str] = 'Z',
        orient_axis_ortho: typing.Union[int, str] = 'X',
        orient_type: typing.Union[str, int] = 'GLOBAL',
        orient_matrix: typing.
        Union[typing.List[typing.List[float]], typing.
              Tuple[typing.Tuple[float, float, float], typing.
                    Tuple[float, float, float], typing.
                    Tuple[float, float, float]], 'mathutils.Matrix'] = ((0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0)),
        orient_matrix_type: typing.Union[str, int] = 'GLOBAL',
        mirror: bool = False,
        use_proportional_edit: bool = False,
        proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
        proportional_size: float = 1.0,
        use_proportional_connected: bool = False,
        use_proportional_projected: bool = False,
        snap: bool = False,
        snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
            'INCREMENT'
        },
        use_snap_project: bool = False,
        snap_target: typing.Union[int, str] = 'CLOSEST',
        use_snap_self: bool = True,
        use_snap_edit: bool = True,
        use_snap_nonedit: bool = True,
        use_snap_selectable_only: bool = False,
        use_snap_to_same_target: bool = False,
        snap_face_nearest_steps: int = 1,
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        gpencil_strokes: bool = False,
        view2d_edge_pan: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Shear selected items along the horizontal screen axis

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Offset
    :type value: float
    :param orient_axis: Axis
    :type orient_axis: typing.Union[int, str]
    :param orient_axis_ortho: Axis Ortho
    :type orient_axis_ortho: typing.Union[int, str]
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: typing.Union[str, int]
    :param orient_matrix: Matrix
    :type orient_matrix: typing.Union[typing.List[typing.List[float]], typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]], 'mathutils.Matrix']
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: typing.Union[str, int]
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param view2d_edge_pan: Edge Pan, Enable edge panning in 2D view
    :type view2d_edge_pan: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def shrink_fatten(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        use_even_offset: bool = False,
        mirror: bool = False,
        use_proportional_edit: bool = False,
        proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
        proportional_size: float = 1.0,
        use_proportional_connected: bool = False,
        use_proportional_projected: bool = False,
        snap: bool = False,
        snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
            'INCREMENT'
        },
        use_snap_project: bool = False,
        snap_target: typing.Union[int, str] = 'CLOSEST',
        use_snap_self: bool = True,
        use_snap_edit: bool = True,
        use_snap_nonedit: bool = True,
        use_snap_selectable_only: bool = False,
        use_snap_to_same_target: bool = False,
        snap_face_nearest_steps: int = 1,
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Shrink/fatten selected vertices along normals

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Offset
    :type value: float
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :type use_even_offset: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def skin_resize(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                1.0, 1.0, 1.0),
        orient_type: typing.Union[str, int] = 'GLOBAL',
        orient_matrix: typing.
        Union[typing.List[typing.List[float]], typing.
              Tuple[typing.Tuple[float, float, float], typing.
                    Tuple[float, float, float], typing.
                    Tuple[float, float, float]], 'mathutils.Matrix'] = ((0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0)),
        orient_matrix_type: typing.Union[str, int] = 'GLOBAL',
        constraint_axis: typing.List[bool] = (False, False, False),
        mirror: bool = False,
        use_proportional_edit: bool = False,
        proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
        proportional_size: float = 1.0,
        use_proportional_connected: bool = False,
        use_proportional_projected: bool = False,
        snap: bool = False,
        snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
            'INCREMENT'
        },
        use_snap_project: bool = False,
        snap_target: typing.Union[int, str] = 'CLOSEST',
        use_snap_self: bool = True,
        use_snap_edit: bool = True,
        use_snap_nonedit: bool = True,
        use_snap_selectable_only: bool = False,
        use_snap_to_same_target: bool = False,
        snap_face_nearest_steps: int = 1,
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Scale selected vertices' skin radii

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Scale
    :type value: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: typing.Union[str, int]
    :param orient_matrix: Matrix
    :type orient_matrix: typing.Union[typing.List[typing.List[float]], typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]], 'mathutils.Matrix']
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: typing.Union[str, int]
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.List[bool]
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def tilt(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         value: float = 0.0,
         mirror: bool = False,
         use_proportional_edit: bool = False,
         proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
         proportional_size: float = 1.0,
         use_proportional_connected: bool = False,
         use_proportional_projected: bool = False,
         snap: bool = False,
         snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
             'INCREMENT'
         },
         use_snap_project: bool = False,
         snap_target: typing.Union[int, str] = 'CLOSEST',
         use_snap_self: bool = True,
         use_snap_edit: bool = True,
         use_snap_nonedit: bool = True,
         use_snap_selectable_only: bool = False,
         use_snap_to_same_target: bool = False,
         snap_face_nearest_steps: int = 1,
         snap_point: typing.
         Union[typing.List[float], typing.
               Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                  0.0),
         snap_align: bool = False,
         snap_normal: typing.
         Union[typing.List[float], typing.
               Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                  0.0),
         release_confirm: bool = False,
         use_accurate: bool = False):
    ''' Tilt selected control vertices of 3D curve

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Angle
    :type value: float
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def tosphere(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             value: float = 0.0,
             mirror: bool = False,
             use_proportional_edit: bool = False,
             proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
             proportional_size: float = 1.0,
             use_proportional_connected: bool = False,
             use_proportional_projected: bool = False,
             snap: bool = False,
             snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
                 'INCREMENT'
             },
             use_snap_project: bool = False,
             snap_target: typing.Union[int, str] = 'CLOSEST',
             use_snap_self: bool = True,
             use_snap_edit: bool = True,
             use_snap_nonedit: bool = True,
             use_snap_selectable_only: bool = False,
             use_snap_to_same_target: bool = False,
             snap_face_nearest_steps: int = 1,
             snap_point: typing.
             Union[typing.List[float], typing.
                   Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                      0.0),
             snap_align: bool = False,
             snap_normal: typing.
             Union[typing.List[float], typing.
                   Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                      0.0),
             gpencil_strokes: bool = False,
             center_override: typing.
             Union[typing.List[float], typing.
                   Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                      0.0),
             release_confirm: bool = False,
             use_accurate: bool = False):
    ''' Move selected items outward in a spherical shape around geometric center

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Factor
    :type value: float
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param center_override: Center Override, Force using this center value (when set)
    :type center_override: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def trackball(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: typing.Union[typing.List[float], typing.
                            Tuple[float, float], 'mathutils.Vector'] = (0.0,
                                                                        0.0),
        mirror: bool = False,
        use_proportional_edit: bool = False,
        proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
        proportional_size: float = 1.0,
        use_proportional_connected: bool = False,
        use_proportional_projected: bool = False,
        snap: bool = False,
        snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
            'INCREMENT'
        },
        use_snap_project: bool = False,
        snap_target: typing.Union[int, str] = 'CLOSEST',
        use_snap_self: bool = True,
        use_snap_edit: bool = True,
        use_snap_nonedit: bool = True,
        use_snap_selectable_only: bool = False,
        use_snap_to_same_target: bool = False,
        snap_face_nearest_steps: int = 1,
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        gpencil_strokes: bool = False,
        center_override: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Trackball style rotation of selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Angle
    :type value: typing.Union[typing.List[float], typing.Tuple[float, float], 'mathutils.Vector']
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param center_override: Center Override, Force using this center value (when set)
    :type center_override: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def transform(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        mode: typing.Union[int, str] = 'TRANSLATION',
        value: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float, float], 'mathutils.Vector'] = (0.0,
                                                                        0.0,
                                                                        0.0,
                                                                        0.0),
        orient_axis: typing.Union[int, str] = 'Z',
        orient_type: typing.Union[int, str] = 'GLOBAL',
        orient_matrix: typing.
        Union[typing.List[typing.List[float]], typing.
              Tuple[typing.Tuple[float, float, float], typing.
                    Tuple[float, float, float], typing.
                    Tuple[float, float, float]], 'mathutils.Matrix'] = ((0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0)),
        orient_matrix_type: typing.Union[int, str] = 'GLOBAL',
        constraint_axis: typing.List[bool] = (False, False, False),
        mirror: bool = False,
        use_proportional_edit: bool = False,
        proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
        proportional_size: float = 1.0,
        use_proportional_connected: bool = False,
        use_proportional_projected: bool = False,
        snap: bool = False,
        snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
            'INCREMENT'
        },
        use_snap_project: bool = False,
        snap_target: typing.Union[int, str] = 'CLOSEST',
        use_snap_self: bool = True,
        use_snap_edit: bool = True,
        use_snap_nonedit: bool = True,
        use_snap_selectable_only: bool = False,
        use_snap_to_same_target: bool = False,
        snap_face_nearest_steps: int = 1,
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        gpencil_strokes: bool = False,
        center_override: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Transform selected items by mode type

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[int, str]
    :param value: Values
    :type value: typing.Union[typing.List[float], typing.Tuple[float, float, float, float], 'mathutils.Vector']
    :param orient_axis: Axis
    :type orient_axis: typing.Union[int, str]
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: typing.Union[int, str]
    :param orient_matrix: Matrix
    :type orient_matrix: typing.Union[typing.List[typing.List[float]], typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]], 'mathutils.Matrix']
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: typing.Union[int, str]
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.List[bool]
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param center_override: Center Override, Force using this center value (when set)
    :type center_override: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def translate(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0),
        orient_axis_ortho: typing.Union[int, str] = 'X',
        orient_type: typing.Union[int, str] = 'GLOBAL',
        orient_matrix: typing.
        Union[typing.List[typing.List[float]], typing.
              Tuple[typing.Tuple[float, float, float], typing.
                    Tuple[float, float, float], typing.
                    Tuple[float, float, float]], 'mathutils.Matrix'] = ((0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0),
                                                                        (0.0,
                                                                         0.0,
                                                                         0.0)),
        orient_matrix_type: typing.Union[int, str] = 'GLOBAL',
        constraint_axis: typing.List[bool] = (False, False, False),
        mirror: bool = False,
        use_proportional_edit: bool = False,
        proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
        proportional_size: float = 1.0,
        use_proportional_connected: bool = False,
        use_proportional_projected: bool = False,
        snap: bool = False,
        snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
            'INCREMENT'
        },
        use_snap_project: bool = False,
        snap_target: typing.Union[int, str] = 'CLOSEST',
        use_snap_self: bool = True,
        use_snap_edit: bool = True,
        use_snap_nonedit: bool = True,
        use_snap_selectable_only: bool = False,
        use_snap_to_same_target: bool = False,
        snap_face_nearest_steps: int = 1,
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        gpencil_strokes: bool = False,
        cursor_transform: bool = False,
        texture_space: bool = False,
        remove_on_cancel: bool = False,
        view2d_edge_pan: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False,
        use_automerge_and_split: bool = False):
    ''' Move selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Move
    :type value: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param orient_axis_ortho: Axis Ortho
    :type orient_axis_ortho: typing.Union[int, str]
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: typing.Union[int, str]
    :param orient_matrix: Matrix
    :type orient_matrix: typing.Union[typing.List[typing.List[float]], typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]], 'mathutils.Matrix']
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: typing.Union[int, str]
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.List[bool]
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param cursor_transform: Transform Cursor
    :type cursor_transform: bool
    :param texture_space: Edit Texture Space, Edit object data texture space
    :type texture_space: bool
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
    :type remove_on_cancel: bool
    :param view2d_edge_pan: Edge Pan, Enable edge panning in 2D view
    :type view2d_edge_pan: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    :param use_automerge_and_split: Auto Merge & Split, Forces the use of Auto Merge and Split
    :type use_automerge_and_split: bool
    '''

    pass


def vert_crease(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        snap: bool = False,
        snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
            'INCREMENT'
        },
        use_snap_project: bool = False,
        snap_target: typing.Union[int, str] = 'CLOSEST',
        use_snap_self: bool = True,
        use_snap_edit: bool = True,
        use_snap_nonedit: bool = True,
        use_snap_selectable_only: bool = False,
        use_snap_to_same_target: bool = False,
        snap_face_nearest_steps: int = 1,
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Change the crease of vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Factor
    :type value: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def vert_slide(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        use_even: bool = False,
        flipped: bool = False,
        use_clamp: bool = True,
        mirror: bool = False,
        snap: bool = False,
        snap_elements: typing.Union[typing.Set[int], typing.Set[str]] = {
            'INCREMENT'
        },
        use_snap_project: bool = False,
        snap_target: typing.Union[int, str] = 'CLOSEST',
        use_snap_self: bool = True,
        use_snap_edit: bool = True,
        use_snap_nonedit: bool = True,
        use_snap_selectable_only: bool = False,
        use_snap_to_same_target: bool = False,
        snap_face_nearest_steps: int = 1,
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        correct_uv: bool = True,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Slide a vertex along a mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Factor
    :type value: float
    :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop
    :type use_even: bool
    :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
    :type flipped: bool
    :param use_clamp: Clamp, Clamp within the edge extents
    :type use_clamp: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_elements: Snap to Elements
    :type snap_elements: typing.Union[typing.Set[int], typing.Set[str]]
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool
    :param snap_target: Snap With
    :type snap_target: typing.Union[int, str]
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool
    :param use_snap_selectable_only: Target: Exclude Non-Selectable
    :type use_snap_selectable_only: bool
    :param use_snap_to_same_target: Snap to Same Target
    :type use_snap_to_same_target: bool
    :param snap_face_nearest_steps: Face Nearest Steps
    :type snap_face_nearest_steps: int
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param correct_uv: Correct UVs, Correct UV coordinates when transforming
    :type correct_uv: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def vertex_random(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  offset: float = 0.0,
                  uniform: float = 0.0,
                  normal: float = 0.0,
                  seed: int = 0,
                  wait_for_input: bool = True):
    ''' Randomize vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param offset: Amount, Distance to offset
    :type offset: float
    :param uniform: Uniform, Increase for uniform offset distance
    :type uniform: float
    :param normal: Normal, Align offset direction to normals
    :type normal: float
    :param seed: Random Seed, Seed for the random number generator
    :type seed: int
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def vertex_warp(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        warp_angle: float = 6.28319,
        offset_angle: float = 0.0,
        min: float = -1.0,
        max: float = 1.0,
        viewmat: typing.
        Union[typing.List[typing.List[float]], typing.
              Tuple[typing.Tuple[float, float, float, float], typing.
                    Tuple[float, float, float, float], typing.
                    Tuple[float, float, float, float], typing.
                    Tuple[float, float, float, float]], 'mathutils.Matrix'] = (
                        (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0),
                        (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)),
        center: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0)):
    ''' Warp vertices around the cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param warp_angle: Warp Angle, Amount to warp about the cursor
    :type warp_angle: float
    :param offset_angle: Offset Angle, Angle to use as the basis for warping
    :type offset_angle: float
    :param min: Min
    :type min: float
    :param max: Max
    :type max: float
    :param viewmat: Matrix
    :type viewmat: typing.Union[typing.List[typing.List[float]], typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]], 'mathutils.Matrix']
    :param center: Center
    :type center: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass
