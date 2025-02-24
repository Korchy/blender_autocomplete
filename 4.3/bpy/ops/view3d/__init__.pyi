import typing
import collections.abc
import typing_extensions
import bpy.types

def bone_select_menu(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str | None = "",
    extend: bool | None = False,
    deselect: bool | None = False,
    toggle: bool | None = False,
):
    """Menu bone selection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Bone Name
    :type name: str | None
    :param extend: Extend
    :type extend: bool | None
    :param deselect: Deselect
    :type deselect: bool | None
    :param toggle: Toggle
    :type toggle: bool | None
    """

def camera_background_image_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    relative_path: bool | None = True,
    name: str = "",
    session_uid: int | None = 0,
):
    """Add a new background image to the active camera

    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: Filepath, Path to image file
    :type filepath: str
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool | None
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :type session_uid: int | None
    """

def camera_background_image_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
):
    """Remove a background image from the camera

    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: Index, Background image index to remove
    :type index: int | None
    """

def camera_to_view(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Set camera view to active view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def camera_to_view_selected(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Move the camera so selected objects are framed

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def clear_render_border(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Clear the boundaries of the border render and disable border render

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def clip_border(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
):
    """Set the view clipping region

    :type execution_context: int | str | None
    :type undo: bool | None
    :param xmin: X Min
    :type xmin: int | None
    :param xmax: X Max
    :type xmax: int | None
    :param ymin: Y Min
    :type ymin: int | None
    :param ymax: Y Max
    :type ymax: int | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | None
    """

def copybuffer(execution_context: int | str | None = None, undo: bool | None = None):
    """Copy the selected objects to the internal clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def cursor3d(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_depth: bool | None = True,
    orientation: typing.Literal["NONE", "VIEW", "XFORM", "GEOM"] | None = "VIEW",
):
    """Set the location of the 3D cursor

        :type execution_context: int | str | None
        :type undo: bool | None
        :param use_depth: Surface Project, Project onto the surface
        :type use_depth: bool | None
        :param orientation: Orientation, Preset viewpoint to use

    NONE
    None -- Leave orientation unchanged.

    VIEW
    View -- Orient to the viewport.

    XFORM
    Transform -- Orient to the current transform setting.

    GEOM
    Geometry -- Match the surface normal.
        :type orientation: typing.Literal['NONE','VIEW','XFORM','GEOM'] | None
    """

def dolly(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mx: int | None = 0,
    my: int | None = 0,
    delta: int | None = 0,
    use_cursor_init: bool | None = True,
):
    """Dolly in/out in the view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mx: Region Position X
    :type mx: int | None
    :param my: Region Position Y
    :type my: int | None
    :param delta: Delta
    :type delta: int | None
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    :type use_cursor_init: bool | None
    """

def drop_world(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    session_uid: int | None = 0,
):
    """Drop a world into the scene

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :type session_uid: int | None
    """

def edit_mesh_extrude_individual_move(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Extrude each individual face separately along local normals

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def edit_mesh_extrude_manifold_normal(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Extrude manifold region along normals

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def edit_mesh_extrude_move_normal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    dissolve_and_intersect: bool | None = False,
):
    """Extrude region together along the average normal

    :type execution_context: int | str | None
    :type undo: bool | None
    :param dissolve_and_intersect: dissolve_and_intersect, Dissolves adjacent faces and intersects new geometry
    :type dissolve_and_intersect: bool | None
    """

def edit_mesh_extrude_move_shrink_fatten(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Extrude region together along local normals

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def fly(execution_context: int | str | None = None, undo: bool | None = None):
    """Interactively fly around the scene

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def interactive_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    primitive_type: typing.Literal[
        "CUBE", "CYLINDER", "CONE", "SPHERE_UV", "SPHERE_ICO"
    ]
    | None = "CUBE",
    plane_origin_base: typing.Literal["EDGE", "CENTER"] | None = "EDGE",
    plane_origin_depth: typing.Literal["EDGE", "CENTER"] | None = "EDGE",
    plane_aspect_base: typing.Literal["FREE", "FIXED"] | None = "FREE",
    plane_aspect_depth: typing.Literal["FREE", "FIXED"] | None = "FREE",
    wait_for_input: bool | None = True,
):
    """Interactively add an object

        :type execution_context: int | str | None
        :type undo: bool | None
        :param primitive_type: Primitive
        :type primitive_type: typing.Literal['CUBE','CYLINDER','CONE','SPHERE_UV','SPHERE_ICO'] | None
        :param plane_origin_base: Origin, The initial position for placement

    EDGE
    Edge -- Start placing the edge position.

    CENTER
    Center -- Start placing the center position.
        :type plane_origin_base: typing.Literal['EDGE','CENTER'] | None
        :param plane_origin_depth: Origin, The initial position for placement

    EDGE
    Edge -- Start placing the edge position.

    CENTER
    Center -- Start placing the center position.
        :type plane_origin_depth: typing.Literal['EDGE','CENTER'] | None
        :param plane_aspect_base: Aspect, The initial aspect setting

    FREE
    Free -- Use an unconstrained aspect.

    FIXED
    Fixed -- Use a fixed 1:1 aspect.
        :type plane_aspect_base: typing.Literal['FREE','FIXED'] | None
        :param plane_aspect_depth: Aspect, The initial aspect setting

    FREE
    Free -- Use an unconstrained aspect.

    FIXED
    Fixed -- Use a fixed 1:1 aspect.
        :type plane_aspect_depth: typing.Literal['FREE','FIXED'] | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | None
    """

def localview(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame_selected: bool | None = True,
):
    """Toggle display of selected object(s) separately and centered in view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame_selected: Frame Selected, Move the view to frame the selected objects
    :type frame_selected: bool | None
    """

def localview_remove_from(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Move selected objects out of local view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_cursor_init: bool | None = True,
):
    """Move the view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    :type use_cursor_init: bool | None
    """

def navigate(execution_context: int | str | None = None, undo: bool | None = None):
    """Interactively navigate around the scene (uses the mode (walk/fly) preference)

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def ndof_all(execution_context: int | str | None = None, undo: bool | None = None):
    """Pan and rotate the view with the 3D mouse

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def ndof_orbit(execution_context: int | str | None = None, undo: bool | None = None):
    """Orbit the view using the 3D mouse

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def ndof_orbit_zoom(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Orbit and zoom the view using the 3D mouse

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def ndof_pan(execution_context: int | str | None = None, undo: bool | None = None):
    """Pan the view with the 3D mouse

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def object_as_camera(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Set the active object as the active camera for this view or scene

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def object_mode_pie_or_toggle(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def pastebuffer(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    autoselect: bool | None = True,
    active_collection: bool | None = True,
):
    """Paste objects from the internal clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    :param autoselect: Select, Select pasted objects
    :type autoselect: bool | None
    :param active_collection: Active Collection, Put pasted objects in the active collection
    :type active_collection: bool | None
    """

def render_border(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
):
    """Set the boundaries of the border render and enable border render

    :type execution_context: int | str | None
    :type undo: bool | None
    :param xmin: X Min
    :type xmin: int | None
    :param xmax: X Max
    :type xmax: int | None
    :param ymin: Y Min
    :type ymin: int | None
    :param ymax: Y Max
    :type ymax: int | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | None
    """

def rotate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_cursor_init: bool | None = True,
):
    """Rotate the view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    :type use_cursor_init: bool | None
    """

def ruler_add(execution_context: int | str | None = None, undo: bool | None = None):
    """Add ruler

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def ruler_remove(execution_context: int | str | None = None, undo: bool | None = None):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect: bool | None = False,
    toggle: bool | None = False,
    deselect_all: bool | None = False,
    select_passthrough: bool | None = False,
    center: bool | None = False,
    enumerate: bool | None = False,
    object: bool | None = False,
    location: collections.abc.Iterable[int] | None = (0, 0),
):
    """Select and activate item(s)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | None
    :param deselect: Deselect, Remove from selection
    :type deselect: bool | None
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: bool | None
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool | None
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :type select_passthrough: bool | None
    :param center: Center, Use the object center when selecting, in edit mode used to extend object selection
    :type center: bool | None
    :param enumerate: Enumerate, List objects under the mouse (object mode only)
    :type enumerate: bool | None
    :param object: Object, Use object selection (edit mode only)
    :type object: bool | None
    :param location: Location, Mouse location
    :type location: collections.abc.Iterable[int] | None
    """

def select_box(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB", "XOR", "AND"] | None = "SET",
):
    """Select items using box selection

        :type execution_context: int | str | None
        :type undo: bool | None
        :param xmin: X Min
        :type xmin: int | None
        :param xmax: X Max
        :type xmax: int | None
        :param ymin: Y Min
        :type ymin: int | None
        :param ymax: Y Max
        :type ymax: int | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.

    XOR
    Difference -- Invert existing selection.

    AND
    Intersect -- Intersect existing selection.
        :type mode: typing.Literal['SET','ADD','SUB','XOR','AND'] | None
    """

def select_circle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    x: int | None = 0,
    y: int | None = 0,
    radius: int | None = 25,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
):
    """Select items using circle selection

        :type execution_context: int | str | None
        :type undo: bool | None
        :param x: X
        :type x: int | None
        :param y: Y
        :type y: int | None
        :param radius: Radius
        :type radius: int | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
    """

def select_lasso(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_smooth_stroke: bool | None = False,
    smooth_stroke_factor: float | None = 0.75,
    smooth_stroke_radius: int | None = 35,
    mode: typing.Literal["SET", "ADD", "SUB", "XOR", "AND"] | None = "SET",
):
    """Select items using lasso selection

        :type execution_context: int | str | None
        :type undo: bool | None
        :param path: Path
        :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
        :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
        :type use_smooth_stroke: bool | None
        :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
        :type smooth_stroke_factor: float | None
        :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
        :type smooth_stroke_radius: int | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.

    XOR
    Difference -- Invert existing selection.

    AND
    Intersect -- Intersect existing selection.
        :type mode: typing.Literal['SET','ADD','SUB','XOR','AND'] | None
    """

def select_menu(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str | None = "",
    extend: bool | None = False,
    deselect: bool | None = False,
    toggle: bool | None = False,
):
    """Menu object selection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Object Name
    :type name: str | None
    :param extend: Extend
    :type extend: bool | None
    :param deselect: Deselect
    :type deselect: bool | None
    :param toggle: Toggle
    :type toggle: bool | None
    """

def smoothview(execution_context: int | str | None = None, undo: bool | None = None):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def snap_cursor_to_active(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Snap 3D cursor to the active item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def snap_cursor_to_center(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Snap 3D cursor to the world origin

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def snap_cursor_to_grid(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Snap 3D cursor to the nearest grid division

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def snap_cursor_to_selected(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Snap 3D cursor to the middle of the selected item(s)

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def snap_selected_to_active(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Snap selected item(s) to the active item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def snap_selected_to_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_offset: bool | None = True,
):
    """Snap selected item(s) to the 3D cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_offset: Offset, If the selection should be snapped as a whole or by each object center
    :type use_offset: bool | None
    """

def snap_selected_to_grid(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Snap selected item(s) to their nearest grid division

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def toggle_matcap_flip(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Flip MatCap

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def toggle_shading(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["WIREFRAME", "SOLID", "MATERIAL", "RENDERED"]
    | None = "WIREFRAME",
):
    """Toggle shading type in 3D viewport

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Shading type to toggle

    WIREFRAME
    Wireframe -- Toggle wireframe shading.

    SOLID
    Solid -- Toggle solid shading.

    MATERIAL
    Material Preview -- Toggle material preview shading.

    RENDERED
    Rendered -- Toggle rendered shading.
        :type type: typing.Literal['WIREFRAME','SOLID','MATERIAL','RENDERED'] | None
    """

def toggle_xray(execution_context: int | str | None = None, undo: bool | None = None):
    """Transparent scene display. Allow selecting through items

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def transform_gizmo_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    type: set[typing.Literal["TRANSLATE", "ROTATE", "SCALE"]] | None = {},
):
    """Set the current transform gizmo

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend
    :type extend: bool | None
    :param type: Type
    :type type: set[typing.Literal['TRANSLATE','ROTATE','SCALE']] | None
    """

def view_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_all_regions: bool | None = False,
    center: bool | None = False,
):
    """View all objects in scene

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_all_regions: All Regions, View selected for all regions
    :type use_all_regions: bool | None
    :param center: Center
    :type center: bool | None
    """

def view_axis(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["LEFT", "RIGHT", "BOTTOM", "TOP", "FRONT", "BACK"]
    | None = "LEFT",
    align_active: bool | None = False,
    relative: bool | None = False,
):
    """Use a preset viewpoint

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: View, Preset viewpoint to use

    LEFT
    Left -- View from the left.

    RIGHT
    Right -- View from the right.

    BOTTOM
    Bottom -- View from the bottom.

    TOP
    Top -- View from the top.

    FRONT
    Front -- View from the front.

    BACK
    Back -- View from the back.
        :type type: typing.Literal['LEFT','RIGHT','BOTTOM','TOP','FRONT','BACK'] | None
        :param align_active: Align Active, Align to the active object's axis
        :type align_active: bool | None
        :param relative: Relative, Rotate relative to the current orientation
        :type relative: bool | None
    """

def view_camera(execution_context: int | str | None = None, undo: bool | None = None):
    """Toggle the camera view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_center_camera(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Center the camera view, resizing the view to fit its bounds

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_center_cursor(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Center the view so that the cursor is in the middle of the view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_center_lock(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Center the view lock offset

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_center_pick(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Center the view to the Z-depth position under the mouse cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_lock_clear(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Clear all view locking

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_lock_to_active(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Lock the view to the active object/bone

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_orbit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle: float | None = 0.0,
    type: typing.Literal["ORBITLEFT", "ORBITRIGHT", "ORBITUP", "ORBITDOWN"]
    | None = "ORBITLEFT",
):
    """Orbit the view

        :type execution_context: int | str | None
        :type undo: bool | None
        :param angle: Roll
        :type angle: float | None
        :param type: Orbit, Direction of View Orbit

    ORBITLEFT
    Orbit Left -- Orbit the view around to the left.

    ORBITRIGHT
    Orbit Right -- Orbit the view around to the right.

    ORBITUP
    Orbit Up -- Orbit the view up.

    ORBITDOWN
    Orbit Down -- Orbit the view down.
        :type type: typing.Literal['ORBITLEFT','ORBITRIGHT','ORBITUP','ORBITDOWN'] | None
    """

def view_pan(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["PANLEFT", "PANRIGHT", "PANUP", "PANDOWN"] | None = "PANLEFT",
):
    """Pan the view in a given direction

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Pan, Direction of View Pan

    PANLEFT
    Pan Left -- Pan the view to the left.

    PANRIGHT
    Pan Right -- Pan the view to the right.

    PANUP
    Pan Up -- Pan the view up.

    PANDOWN
    Pan Down -- Pan the view down.
        :type type: typing.Literal['PANLEFT','PANRIGHT','PANUP','PANDOWN'] | None
    """

def view_persportho(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Switch the current view from perspective/orthographic projection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_roll(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle: float | None = 0.0,
    type: typing.Literal["ANGLE", "LEFT", "RIGHT"] | None = "ANGLE",
):
    """Roll the view

        :type execution_context: int | str | None
        :type undo: bool | None
        :param angle: Roll
        :type angle: float | None
        :param type: Roll Angle Source, How roll angle is calculated

    ANGLE
    Roll Angle -- Roll the view using an angle value.

    LEFT
    Roll Left -- Roll the view around to the left.

    RIGHT
    Roll Right -- Roll the view around to the right.
        :type type: typing.Literal['ANGLE','LEFT','RIGHT'] | None
    """

def view_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_all_regions: bool | None = False,
):
    """Move the view to the selection center

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_all_regions: All Regions, View selected for all regions
    :type use_all_regions: bool | None
    """

def walk(execution_context: int | str | None = None, undo: bool | None = None):
    """Interactively walk around the scene

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def zoom(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mx: int | None = 0,
    my: int | None = 0,
    delta: int | None = 0,
    use_cursor_init: bool | None = True,
):
    """Zoom in/out in the view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mx: Region Position X
    :type mx: int | None
    :param my: Region Position Y
    :type my: int | None
    :param delta: Delta
    :type delta: int | None
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    :type use_cursor_init: bool | None
    """

def zoom_border(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    zoom_out: bool | None = False,
):
    """Zoom in the view to the nearest object contained in the border

    :type execution_context: int | str | None
    :type undo: bool | None
    :param xmin: X Min
    :type xmin: int | None
    :param xmax: X Max
    :type xmax: int | None
    :param ymin: Y Min
    :type ymin: int | None
    :param ymax: Y Max
    :type ymax: int | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | None
    :param zoom_out: Zoom Out
    :type zoom_out: bool | None
    """

def zoom_camera_1_to_1(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Match the camera to 1:1 to the render output

    :type execution_context: int | str | None
    :type undo: bool | None
    """
