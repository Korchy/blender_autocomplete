import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums
import mathutils

def bbone_resize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Sequence[float] | mathutils.Vector | None = (1.0, 1.0, 1.0),
    orient_type: str | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: str | None = "GLOBAL",
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    mirror: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Scale selected bendy bones display size

    :param value: Display Size
    :param orient_type: Orientation, Transformation orientation
    :param orient_matrix: Matrix
    :param orient_matrix_type: Matrix Orientation
    :param constraint_axis: Constraint Axis
    :param mirror: Mirror Editing
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def bend(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Iterable[float] | None = 0.0,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    gpencil_strokes: bool | None = False,
    center_override: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Bend selected items between the 3D cursor and the mouse

    :param value: Angle
    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param snap: Use Snapping Options
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :param center_override: Center Override, Force using this center value (when set)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def create_orientation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    use_view: bool | None = False,
    use: bool | None = False,
    overwrite: bool | None = False,
) -> None:
    """Create transformation orientation from selection

    :param name: Name, Name of the new custom orientation
    :param use_view: Use View, Use the current view instead of the active object to create the new orientation
    :param use: Use After Creation, Select orientation after its creation
    :param overwrite: Overwrite Previous, Overwrite previously created orientation with same name
    """

def delete_orientation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete transformation orientation"""

def edge_bevelweight(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    snap: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Change the bevel weight of edges

    :param value: Factor
    :param snap: Use Snapping Options
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def edge_crease(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    snap: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Change the crease of edges

    :param value: Factor
    :param snap: Use Snapping Options
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def edge_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    single_side: bool | None = False,
    use_even: bool | None = False,
    flipped: bool | None = False,
    use_clamp: bool | None = True,
    mirror: bool | None = False,
    snap: bool | None = False,
    snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None = {
        "INCREMENT"
    },
    use_snap_project: bool | None = False,
    snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None = "CLOSEST",
    use_snap_self: bool | None = True,
    use_snap_edit: bool | None = True,
    use_snap_nonedit: bool | None = True,
    use_snap_selectable: bool | None = False,
    snap_point: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    correct_uv: bool | None = True,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Slide an edge loop along a mesh

    :param value: Factor
    :param single_side: Single Side
    :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop
    :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
    :param use_clamp: Clamp, Clamp within the edge extents
    :param mirror: Mirror Editing
    :param snap: Use Snapping Options
    :param snap_elements: Snap to Elements
    :param use_snap_project: Project Individual Elements
    :param snap_target: Snap Base, Point on source that will snap to target
    :param use_snap_self: Target: Include Active
    :param use_snap_edit: Target: Include Edit
    :param use_snap_nonedit: Target: Include Non-Edited
    :param use_snap_selectable: Target: Exclude Non-Selectable
    :param snap_point: Point
    :param correct_uv: Correct UVs, Correct UV coordinates when transforming
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def from_gizmo(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Transform selected items by mode type"""

def mirror(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    orient_type: str | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: str | None = "GLOBAL",
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    gpencil_strokes: bool | None = False,
    center_override: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Mirror selected items around one or more axes

    :param orient_type: Orientation, Transformation orientation
    :param orient_matrix: Matrix
    :param orient_matrix_type: Matrix Orientation
    :param constraint_axis: Constraint Axis
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :param center_override: Center Override, Force using this center value (when set)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def push_pull(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    center_override: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Push/Pull selected items

    :param value: Distance
    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param snap: Use Snapping Options
    :param center_override: Center Override, Force using this center value (when set)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def resize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Sequence[float] | mathutils.Vector | None = (1.0, 1.0, 1.0),
    mouse_dir_constraint: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    orient_type: str | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: str | None = "GLOBAL",
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None = {
        "INCREMENT"
    },
    use_snap_project: bool | None = False,
    snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None = "CLOSEST",
    use_snap_self: bool | None = True,
    use_snap_edit: bool | None = True,
    use_snap_nonedit: bool | None = True,
    use_snap_selectable: bool | None = False,
    snap_point: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    gpencil_strokes: bool | None = False,
    texture_space: bool | None = False,
    remove_on_cancel: bool | None = False,
    use_duplicated_keyframes: bool | None = False,
    center_override: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Scale (resize) selected items

    :param value: Scale
    :param mouse_dir_constraint: Mouse Directional Constraint
    :param orient_type: Orientation, Transformation orientation
    :param orient_matrix: Matrix
    :param orient_matrix_type: Matrix Orientation
    :param constraint_axis: Constraint Axis
    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param snap: Use Snapping Options
    :param snap_elements: Snap to Elements
    :param use_snap_project: Project Individual Elements
    :param snap_target: Snap Base, Point on source that will snap to target
    :param use_snap_self: Target: Include Active
    :param use_snap_edit: Target: Include Edit
    :param use_snap_nonedit: Target: Include Non-Edited
    :param use_snap_selectable: Target: Exclude Non-Selectable
    :param snap_point: Point
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :param texture_space: Edit Texture Space, Edit object data texture space
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
    :param use_duplicated_keyframes: Duplicated Keyframes, Transform duplicated keyframes
    :param center_override: Center Override, Force using this center value (when set)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def rotate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    orient_axis: bpy.stub_internal.rna_enums.AxisXyzItems | None = "Z",
    orient_type: str | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: str | None = "GLOBAL",
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None = {
        "INCREMENT"
    },
    use_snap_project: bool | None = False,
    snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None = "CLOSEST",
    use_snap_self: bool | None = True,
    use_snap_edit: bool | None = True,
    use_snap_nonedit: bool | None = True,
    use_snap_selectable: bool | None = False,
    snap_point: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    gpencil_strokes: bool | None = False,
    center_override: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Rotate selected items

    :param value: Angle
    :param orient_axis: Axis
    :param orient_type: Orientation, Transformation orientation
    :param orient_matrix: Matrix
    :param orient_matrix_type: Matrix Orientation
    :param constraint_axis: Constraint Axis
    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param snap: Use Snapping Options
    :param snap_elements: Snap to Elements
    :param use_snap_project: Project Individual Elements
    :param snap_target: Snap Base, Point on source that will snap to target
    :param use_snap_self: Target: Include Active
    :param use_snap_edit: Target: Include Edit
    :param use_snap_nonedit: Target: Include Non-Edited
    :param use_snap_selectable: Target: Exclude Non-Selectable
    :param snap_point: Point
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :param center_override: Center Override, Force using this center value (when set)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def rotate_normal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    orient_axis: bpy.stub_internal.rna_enums.AxisXyzItems | None = "Z",
    orient_type: str | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: str | None = "GLOBAL",
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    mirror: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Rotate split normal of selected items

    :param value: Angle
    :param orient_axis: Axis
    :param orient_type: Orientation, Transformation orientation
    :param orient_matrix: Matrix
    :param orient_matrix_type: Matrix Orientation
    :param constraint_axis: Constraint Axis
    :param mirror: Mirror Editing
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def select_orientation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    orientation: str | None = "GLOBAL",
) -> None:
    """Select transformation orientation

    :param orientation: Orientation, Transformation orientation
    """

def seq_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
    use_restore_handle_selection: bool | None = False,
    snap: bool | None = False,
    view2d_edge_pan: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Slide a sequence strip in time

    :param value: Offset
    :param use_restore_handle_selection: Restore Handle Selection, Restore handle selection after tweaking
    :param snap: Use Snapping Options
    :param view2d_edge_pan: Edge Pan, Enable edge panning in 2D view
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def shear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    orient_axis: bpy.stub_internal.rna_enums.AxisXyzItems | None = "Z",
    orient_axis_ortho: bpy.stub_internal.rna_enums.AxisXyzItems | None = "X",
    orient_type: str | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: str | None = "GLOBAL",
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    gpencil_strokes: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Shear selected items along the given axis

    :param value: Offset
    :param orient_axis: Axis
    :param orient_axis_ortho: Axis Ortho
    :param orient_type: Orientation, Transformation orientation
    :param orient_matrix: Matrix
    :param orient_matrix_type: Matrix Orientation
    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param snap: Use Snapping Options
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def shrink_fatten(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    use_even_offset: bool | None = False,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Shrink/fatten selected vertices along normals

    :param value: Offset
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param snap: Use Snapping Options
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def skin_resize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Sequence[float] | mathutils.Vector | None = (1.0, 1.0, 1.0),
    orient_type: str | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: str | None = "GLOBAL",
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None = {
        "INCREMENT"
    },
    use_snap_project: bool | None = False,
    snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None = "CLOSEST",
    use_snap_self: bool | None = True,
    use_snap_edit: bool | None = True,
    use_snap_nonedit: bool | None = True,
    use_snap_selectable: bool | None = False,
    snap_point: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Scale selected vertices skin radii

    :param value: Scale
    :param orient_type: Orientation, Transformation orientation
    :param orient_matrix: Matrix
    :param orient_matrix_type: Matrix Orientation
    :param constraint_axis: Constraint Axis
    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param snap: Use Snapping Options
    :param snap_elements: Snap to Elements
    :param use_snap_project: Project Individual Elements
    :param snap_target: Snap Base, Point on source that will snap to target
    :param use_snap_self: Target: Include Active
    :param use_snap_edit: Target: Include Edit
    :param use_snap_nonedit: Target: Include Non-Edited
    :param use_snap_selectable: Target: Exclude Non-Selectable
    :param snap_point: Point
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def tilt(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Tilt selected control vertices of 3D curve

    :param value: Angle
    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param snap: Use Snapping Options
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def tosphere(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    gpencil_strokes: bool | None = False,
    center_override: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Move selected items outward in a spherical shape around geometric center

    :param value: Factor
    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param snap: Use Snapping Options
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :param center_override: Center Override, Force using this center value (when set)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def trackball(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Iterable[float] | None = (0.0, 0.0),
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    gpencil_strokes: bool | None = False,
    center_override: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Trackball style rotation of selected items

    :param value: Angle
    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param snap: Use Snapping Options
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :param center_override: Center Override, Force using this center value (when set)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def transform(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: bpy.stub_internal.rna_enums.TransformModeTypeItems | None = "TRANSLATION",
    value: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
        0.0,
    ),
    orient_axis: bpy.stub_internal.rna_enums.AxisXyzItems | None = "Z",
    orient_type: bpy.stub_internal.rna_enums.TransformOrientationItems
    | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: bpy.stub_internal.rna_enums.TransformOrientationItems
    | None = "GLOBAL",
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None = {
        "INCREMENT"
    },
    use_snap_project: bool | None = False,
    snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None = "CLOSEST",
    use_snap_self: bool | None = True,
    use_snap_edit: bool | None = True,
    use_snap_nonedit: bool | None = True,
    use_snap_selectable: bool | None = False,
    snap_point: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    gpencil_strokes: bool | None = False,
    texture_space: bool | None = False,
    remove_on_cancel: bool | None = False,
    use_duplicated_keyframes: bool | None = False,
    center_override: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
    use_automerge_and_split: bool | None = False,
) -> None:
    """Transform selected items by mode type

    :param mode: Mode
    :param value: Values
    :param orient_axis: Axis
    :param orient_type: Orientation, Transformation orientation
    :param orient_matrix: Matrix
    :param orient_matrix_type: Matrix Orientation
    :param constraint_axis: Constraint Axis
    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param snap: Use Snapping Options
    :param snap_elements: Snap to Elements
    :param use_snap_project: Project Individual Elements
    :param snap_target: Snap Base, Point on source that will snap to target
    :param use_snap_self: Target: Include Active
    :param use_snap_edit: Target: Include Edit
    :param use_snap_nonedit: Target: Include Non-Edited
    :param use_snap_selectable: Target: Exclude Non-Selectable
    :param snap_point: Point
    :param snap_align: Align with Point Normal
    :param snap_normal: Normal
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :param texture_space: Edit Texture Space, Edit object data texture space
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
    :param use_duplicated_keyframes: Duplicated Keyframes, Transform duplicated keyframes
    :param center_override: Center Override, Force using this center value (when set)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    :param use_automerge_and_split: Auto Merge & Split, Forces the use of Auto Merge and Split
    """

def translate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
    orient_type: bpy.stub_internal.rna_enums.TransformOrientationItems
    | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: bpy.stub_internal.rna_enums.TransformOrientationItems
    | None = "GLOBAL",
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None = {
        "INCREMENT"
    },
    use_snap_project: bool | None = False,
    snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None = "CLOSEST",
    use_snap_self: bool | None = True,
    use_snap_edit: bool | None = True,
    use_snap_nonedit: bool | None = True,
    use_snap_selectable: bool | None = False,
    snap_point: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    gpencil_strokes: bool | None = False,
    cursor_transform: bool | None = False,
    texture_space: bool | None = False,
    remove_on_cancel: bool | None = False,
    use_duplicated_keyframes: bool | None = False,
    view2d_edge_pan: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
    use_automerge_and_split: bool | None = False,
) -> None:
    """Move selected items

    :param value: Move
    :param orient_type: Orientation, Transformation orientation
    :param orient_matrix: Matrix
    :param orient_matrix_type: Matrix Orientation
    :param constraint_axis: Constraint Axis
    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param snap: Use Snapping Options
    :param snap_elements: Snap to Elements
    :param use_snap_project: Project Individual Elements
    :param snap_target: Snap Base, Point on source that will snap to target
    :param use_snap_self: Target: Include Active
    :param use_snap_edit: Target: Include Edit
    :param use_snap_nonedit: Target: Include Non-Edited
    :param use_snap_selectable: Target: Exclude Non-Selectable
    :param snap_point: Point
    :param snap_align: Align with Point Normal
    :param snap_normal: Normal
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :param cursor_transform: Transform Cursor
    :param texture_space: Edit Texture Space, Edit object data texture space
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
    :param use_duplicated_keyframes: Duplicated Keyframes, Transform duplicated keyframes
    :param view2d_edge_pan: Edge Pan, Enable edge panning in 2D view
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    :param use_automerge_and_split: Auto Merge & Split, Forces the use of Auto Merge and Split
    """

def vert_crease(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    snap: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Change the crease of vertices

    :param value: Factor
    :param snap: Use Snapping Options
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def vert_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    use_even: bool | None = False,
    flipped: bool | None = False,
    use_clamp: bool | None = True,
    mirror: bool | None = False,
    snap: bool | None = False,
    snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None = {
        "INCREMENT"
    },
    use_snap_project: bool | None = False,
    snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None = "CLOSEST",
    use_snap_self: bool | None = True,
    use_snap_edit: bool | None = True,
    use_snap_nonedit: bool | None = True,
    use_snap_selectable: bool | None = False,
    snap_point: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    correct_uv: bool | None = True,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Slide a vertex along a mesh

    :param value: Factor
    :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop
    :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
    :param use_clamp: Clamp, Clamp within the edge extents
    :param mirror: Mirror Editing
    :param snap: Use Snapping Options
    :param snap_elements: Snap to Elements
    :param use_snap_project: Project Individual Elements
    :param snap_target: Snap Base, Point on source that will snap to target
    :param use_snap_self: Target: Include Active
    :param use_snap_edit: Target: Include Edit
    :param use_snap_nonedit: Target: Include Non-Edited
    :param use_snap_selectable: Target: Exclude Non-Selectable
    :param snap_point: Point
    :param correct_uv: Correct UVs, Correct UV coordinates when transforming
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def vertex_random(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: float | None = 0.0,
    uniform: float | None = 0.0,
    normal: float | None = 0.0,
    seed: int | None = 0,
    wait_for_input: bool | None = True,
) -> None:
    """Randomize vertices

    :param offset: Amount, Distance to offset
    :param uniform: Uniform, Increase for uniform offset distance
    :param normal: Normal, Align offset direction to normals
    :param seed: Random Seed, Seed for the random number generator
    :param wait_for_input: Wait for Input
    """

def vertex_warp(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    warp_angle: float | None = 6.28319,
    offset_angle: float | None = 0.0,
    min: float | None = -1.0,
    max: float | None = 1.0,
    viewmat: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = (
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
    ),
    center: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Warp vertices around the cursor

    :param warp_angle: Warp Angle, Amount to warp about the cursor
    :param offset_angle: Offset Angle, Angle to use as the basis for warping
    :param min: Min
    :param max: Max
    :param viewmat: Matrix
    :param center: Center
    """
