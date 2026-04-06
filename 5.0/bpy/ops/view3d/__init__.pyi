import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
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
) -> None:
    """Menu bone selection

    :param name: Bone Name
    :param extend: Extend
    :param deselect: Deselect
    :param toggle: Toggle
    """

def camera_background_image_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str | None = "",
    relative_path: bool | None = True,
    name: str = "",
    session_uid: int | None = 0,
) -> None:
    """Add a new background image to the active camera

    :param filepath: Filepath, Path to image file
    :param relative_path: Relative Path, Select the file relative to the blend file
    :param name: Name, Name of the data-block to use by the operator
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    """

def camera_background_image_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
) -> None:
    """Remove a background image from the camera

    :param index: Index, Background image index to remove
    """

def camera_to_view(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set camera view to active view"""

def camera_to_view_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move the camera so selected objects are framed"""

def clear_render_border(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear the boundaries of the border render and disable border render"""

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
) -> None:
    """Set the view clipping region

    :param xmin: X Min
    :param xmax: X Max
    :param ymin: Y Min
    :param ymax: Y Max
    :param wait_for_input: Wait for Input
    """

def copybuffer(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the selected objects to the internal clipboard"""

def cursor3d(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_depth: bool | None = True,
    orientation: typing.Literal["NONE", "VIEW", "XFORM", "GEOM"] | None = "VIEW",
) -> None:
    """Set the location of the 3D cursor

        :param use_depth: Surface Project, Project onto the surface
        :param orientation: Orientation, Preset viewpoint to use

    NONE
    None -- Leave orientation unchanged.

    VIEW
    View -- Orient to the viewport.

    XFORM
    Transform -- Orient to the current transform setting.

    GEOM
    Geometry -- Match the surface normal.
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
) -> None:
    """Dolly in/out in the view

    :param mx: Region Position X
    :param my: Region Position Y
    :param delta: Delta
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    """

def drop_world(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    session_uid: int | None = 0,
) -> None:
    """Drop a world into the scene

    :param name: Name, Name of the data-block to use by the operator
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    """

def edit_mesh_extrude_individual_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Extrude each individual face separately along local normals"""

def edit_mesh_extrude_manifold_normal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Extrude manifold region along normals"""

def edit_mesh_extrude_move_normal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    dissolve_and_intersect: bool | None = False,
) -> None:
    """Extrude region together along the average normal

    :param dissolve_and_intersect: dissolve_and_intersect, Dissolves adjacent faces and intersects new geometry
    """

def edit_mesh_extrude_move_shrink_fatten(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Extrude region together along local normals"""

def fly(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Interactively fly around the scene"""

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
) -> None:
    """Interactively add an object

        :param primitive_type: Primitive
        :param plane_origin_base: Origin, The initial position for placement

    EDGE
    Edge -- Start placing the edge position.

    CENTER
    Center -- Start placing the center position.
        :param plane_origin_depth: Origin, The initial position for placement

    EDGE
    Edge -- Start placing the edge position.

    CENTER
    Center -- Start placing the center position.
        :param plane_aspect_base: Aspect, The initial aspect setting

    FREE
    Free -- Use an unconstrained aspect.

    FIXED
    Fixed -- Use a fixed 1:1 aspect.
        :param plane_aspect_depth: Aspect, The initial aspect setting

    FREE
    Free -- Use an unconstrained aspect.

    FIXED
    Fixed -- Use a fixed 1:1 aspect.
        :param wait_for_input: Wait for Input
    """

def localview(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame_selected: bool | None = True,
) -> None:
    """Toggle display of selected object(s) separately and centered in view

    :param frame_selected: Frame Selected, Move the view to frame the selected objects
    """

def localview_remove_from(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move selected objects out of local view"""

def move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_cursor_init: bool | None = True,
) -> None:
    """Move the view

    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    """

def navigate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Interactively navigate around the scene (uses the mode (walk/fly) preference)"""

def ndof_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Pan and rotate the view with the 3D mouse"""

def ndof_orbit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Orbit the view using the 3D mouse"""

def ndof_orbit_zoom(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Orbit and zoom the view using the 3D mouse"""

def ndof_pan(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Pan the view with the 3D mouse"""

def object_as_camera(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set the active object as the active camera for this view or scene"""

def object_mode_pie_or_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

def pastebuffer(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    autoselect: bool | None = True,
    active_collection: bool | None = True,
) -> None:
    """Paste objects from the internal clipboard

    :param autoselect: Select, Select pasted objects
    :param active_collection: Active Collection, Put pasted objects in the active collection
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
) -> None:
    """Set the boundaries of the border render and enable border render

    :param xmin: X Min
    :param xmax: X Max
    :param ymin: Y Min
    :param ymax: Y Max
    :param wait_for_input: Wait for Input
    """

def rotate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_cursor_init: bool | None = True,
) -> None:
    """Rotate the view

    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    """

def ruler_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add ruler"""

def ruler_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

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
) -> None:
    """Select and activate item(s)

    :param extend: Extend, Extend selection instead of deselecting everything first
    :param deselect: Deselect, Remove from selection
    :param toggle: Toggle Selection, Toggle the selection
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :param center: Center, Use the object center when selecting, in edit mode used to extend object selection
    :param enumerate: Enumerate, List objects under the mouse (object mode only)
    :param object: Object, Use object selection (edit mode only)
    :param location: Location, Mouse location
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
) -> None:
    """Select items using box selection

        :param xmin: X Min
        :param xmax: X Max
        :param ymin: Y Min
        :param ymax: Y Max
        :param wait_for_input: Wait for Input
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
) -> None:
    """Select items using circle selection

        :param x: X
        :param y: Y
        :param radius: Radius
        :param wait_for_input: Wait for Input
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
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
) -> None:
    """Select items using lasso selection

        :param path: Path
        :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
        :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
        :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
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
) -> None:
    """Menu object selection

    :param name: Object Name
    :param extend: Extend
    :param deselect: Deselect
    :param toggle: Toggle
    """

def smoothview(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

def snap_cursor_to_active(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Snap 3D cursor to the active item"""

def snap_cursor_to_center(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Snap 3D cursor to the world origin"""

def snap_cursor_to_grid(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Snap 3D cursor to the nearest grid division"""

def snap_cursor_to_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Snap 3D cursor to the middle of the selected item(s)"""

def snap_selected_to_active(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Snap selected item(s) to the active item"""

def snap_selected_to_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_offset: bool | None = True,
    use_rotation: bool | None = False,
) -> None:
    """Snap selected item(s) to the 3D cursor

    :param use_offset: Offset, If the selection should be snapped as a whole or by each object center
    :param use_rotation: Rotation, If the selection should be rotated to match the cursor
    """

def snap_selected_to_grid(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Snap selected item(s) to their nearest grid division"""

def toggle_matcap_flip(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Flip MatCap"""

def toggle_shading(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["WIREFRAME", "SOLID", "MATERIAL", "RENDERED"]
    | None = "WIREFRAME",
) -> None:
    """Toggle shading type in 3D viewport

        :param type: Type, Shading type to toggle

    WIREFRAME
    Wireframe -- Toggle wireframe shading.

    SOLID
    Solid -- Toggle solid shading.

    MATERIAL
    Material Preview -- Toggle material preview shading.

    RENDERED
    Rendered -- Toggle rendered shading.
    """

def toggle_xray(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Transparent scene display. Allow selecting through items"""

def transform_gizmo_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    type: set[typing.Literal["TRANSLATE", "ROTATE", "SCALE"]] | None = {},
) -> None:
    """Set the current transform gizmo

    :param extend: Extend
    :param type: Type
    """

def view_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_all_regions: bool | None = False,
    center: bool | None = False,
) -> None:
    """View all objects in scene

    :param use_all_regions: All Regions, View selected for all regions
    :param center: Center
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
) -> None:
    """Use a preset viewpoint

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
        :param align_active: Align Active, Align to the active objects axis
        :param relative: Relative, Rotate relative to the current orientation
    """

def view_camera(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle the camera view"""

def view_center_camera(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Center the camera view, resizing the view to fit its bounds"""

def view_center_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Center the view so that the cursor is in the middle of the view"""

def view_center_lock(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Center the view lock offset"""

def view_center_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Center the view to the Z-depth position under the mouse cursor"""

def view_lock_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear all view locking"""

def view_lock_to_active(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Lock the view to the active object/bone"""

def view_orbit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle: float | None = 0.0,
    type: typing.Literal["ORBITLEFT", "ORBITRIGHT", "ORBITUP", "ORBITDOWN"]
    | None = "ORBITLEFT",
) -> None:
    """Orbit the view

        :param angle: Roll
        :param type: Orbit, Direction of View Orbit

    ORBITLEFT
    Orbit Left -- Orbit the view around to the left.

    ORBITRIGHT
    Orbit Right -- Orbit the view around to the right.

    ORBITUP
    Orbit Up -- Orbit the view up.

    ORBITDOWN
    Orbit Down -- Orbit the view down.
    """

def view_pan(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["PANLEFT", "PANRIGHT", "PANUP", "PANDOWN"] | None = "PANLEFT",
) -> None:
    """Pan the view in a given direction

        :param type: Pan, Direction of View Pan

    PANLEFT
    Pan Left -- Pan the view to the left.

    PANRIGHT
    Pan Right -- Pan the view to the right.

    PANUP
    Pan Up -- Pan the view up.

    PANDOWN
    Pan Down -- Pan the view down.
    """

def view_persportho(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Switch the current view from perspective/orthographic projection"""

def view_roll(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle: float | None = 0.0,
    type: typing.Literal["ANGLE", "LEFT", "RIGHT"] | None = "ANGLE",
) -> None:
    """Roll the view

        :param angle: Roll
        :param type: Roll Angle Source, How roll angle is calculated

    ANGLE
    Roll Angle -- Roll the view using an angle value.

    LEFT
    Roll Left -- Roll the view around to the left.

    RIGHT
    Roll Right -- Roll the view around to the right.
    """

def view_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_all_regions: bool | None = False,
) -> None:
    """Move the view to the selection center

    :param use_all_regions: All Regions, View selected for all regions
    """

def walk(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Interactively walk around the scene"""

def zoom(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mx: int | None = 0,
    my: int | None = 0,
    delta: int | None = 0,
    use_cursor_init: bool | None = True,
) -> None:
    """Zoom in/out in the view

    :param mx: Region Position X
    :param my: Region Position Y
    :param delta: Delta
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
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
) -> None:
    """Zoom in the view to the nearest object contained in the border

    :param xmin: X Min
    :param xmax: X Max
    :param ymin: Y Min
    :param ymax: Y Max
    :param wait_for_input: Wait for Input
    :param zoom_out: Zoom Out
    """

def zoom_camera_1_to_1(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Match the camera to 1:1 to the render output"""
