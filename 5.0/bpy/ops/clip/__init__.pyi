import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops.transform
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

def add_marker(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Place new marker at specified location

    :param location: Location, Location of marker on frame
    """

def add_marker_at_click(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Place new marker at the desired (clicked) position"""

def add_marker_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    CLIP_OT_add_marker: add_marker | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Add new marker and move it on movie

    :param CLIP_OT_add_marker: Add Marker, Place new marker at specified location
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def add_marker_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    CLIP_OT_add_marker: add_marker | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Add new marker and slide it with mouse until mouse button release

    :param CLIP_OT_add_marker: Add Marker, Place new marker at specified location
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def apply_solution_scale(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    distance: float | None = 0.0,
) -> None:
    """Apply scale on solution itself to make distance between selected tracks equals to desired

    :param distance: Distance, Distance between selected tracks
    """

def average_tracks(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keep_original: bool | None = True,
) -> None:
    """Average selected tracks into active

    :param keep_original: Keep Original, Keep original tracks
    """

def bundles_to_mesh(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create vertex cloud using coordinates of reconstructed tracks"""

def camera_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
    use_focal_length: bool | None = True,
) -> None:
    """Add or remove a Tracking Camera Intrinsics Preset

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    :param use_focal_length: Include Focal Length, Include focal length into the preset
    """

def change_frame(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame: int | None = 0,
) -> None:
    """Interactively change the current frame number

    :param frame: Frame
    """

def clean_tracks(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frames: int | None = 0,
    error: float | None = 0.0,
    action: typing.Literal["SELECT", "DELETE_TRACK", "DELETE_SEGMENTS"]
    | None = "SELECT",
) -> None:
    """Clean tracks with high error values or few frames

        :param frames: Tracked Frames, Affect tracks which are tracked less than the specified number of frames
        :param error: Reprojection Error, Affect tracks which have a larger reprojection error
        :param action: Action, Cleanup action to execute

    SELECT
    Select -- Select unclean tracks.

    DELETE_TRACK
    Delete Track -- Delete unclean tracks.

    DELETE_SEGMENTS
    Delete Segments -- Delete unclean segments of tracks.
    """

def clear_solution(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear all calculated data"""

def clear_track_path(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["UPTO", "REMAINED", "ALL"] | None = "REMAINED",
    clear_active: bool | None = False,
) -> None:
    """Clear tracks after/before current position or clear the whole track

        :param action: Action, Clear action to execute

    UPTO
    Clear Up To -- Clear path up to current frame.

    REMAINED
    Clear Remained -- Clear path at remaining frames (after current).

    ALL
    Clear All -- Clear the whole path.
        :param clear_active: Clear Active, Clear active track only instead of all selected tracks
    """

def constraint_to_fcurve(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create F-Curves for object which will copy objects movement caused by this constraint"""

def copy_tracks(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the selected tracks to the internal clipboard"""

def create_plane_track(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create new plane track out of selected point tracks"""

def cursor_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Set 2D cursor location

    :param location: Location, Cursor location in normalized clip coordinates
    """

def delete_marker(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
) -> None:
    """Delete marker for current frame from selected tracks

    :param confirm: Confirm, Prompt for confirmation
    """

def delete_proxy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete movie clip proxy files from the hard drive"""

def delete_track(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
) -> None:
    """Delete selected tracks

    :param confirm: Confirm, Prompt for confirmation
    """

def detect_features(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    placement: typing.Literal["FRAME", "INSIDE_GPENCIL", "OUTSIDE_GPENCIL"]
    | None = "FRAME",
    margin: int | None = 16,
    threshold: float | None = 0.5,
    min_distance: int | None = 120,
) -> None:
    """Automatically detect features and place markers to track

        :param placement: Placement, Placement for detected features

    FRAME
    Whole Frame -- Place markers across the whole frame.

    INSIDE_GPENCIL
    Inside Annotated Area -- Place markers only inside areas outlined with the Annotation tool.

    OUTSIDE_GPENCIL
    Outside Annotated Area -- Place markers only outside areas outlined with the Annotation tool.
        :param margin: Margin, Only features further than margin pixels from the image edges are considered
        :param threshold: Threshold, Threshold level to consider feature good enough for tracking
        :param min_distance: Distance, Minimal distance accepted between two features
    """

def disable_markers(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["DISABLE", "ENABLE", "TOGGLE"] | None = "DISABLE",
) -> None:
    """Disable/enable selected markers

        :param action: Action, Disable action to execute

    DISABLE
    Disable -- Disable selected markers.

    ENABLE
    Enable -- Enable selected markers.

    TOGGLE
    Toggle -- Toggle disabled flag for selected markers.
    """

def dopesheet_select_channel(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
    extend: bool | None = False,
) -> None:
    """Select movie tracking channel

    :param location: Location, Mouse location to select channel
    :param extend: Extend, Extend selection rather than clearing the existing selection
    """

def dopesheet_view_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset viewable area to show full keyframe range"""

def filter_tracks(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    track_threshold: float | None = 5.0,
) -> None:
    """Filter tracks which has weirdly looking spikes in motion curves

    :param track_threshold: Track Threshold, Filter Threshold to select problematic tracks
    """

def frame_jump(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    position: typing.Literal["PATHSTART", "PATHEND", "FAILEDPREV", "FAILNEXT"]
    | None = "PATHSTART",
) -> None:
    """Jump to special frame

        :param position: Position, Position to jump to

    PATHSTART
    Path Start -- Jump to start of current path.

    PATHEND
    Path End -- Jump to end of current path.

    FAILEDPREV
    Previous Failed -- Jump to previous failed frame.

    FAILNEXT
    Next Failed -- Jump to next failed frame.
    """

def graph_center_current_frame(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Scroll view so current frame would be centered"""

def graph_delete_curve(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
) -> None:
    """Delete track corresponding to the selected curve

    :param confirm: Confirm, Prompt for confirmation
    """

def graph_delete_knot(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete curve knots"""

def graph_disable_markers(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["DISABLE", "ENABLE", "TOGGLE"] | None = "DISABLE",
) -> None:
    """Disable/enable selected markers

        :param action: Action, Disable action to execute

    DISABLE
    Disable -- Disable selected markers.

    ENABLE
    Enable -- Enable selected markers.

    TOGGLE
    Toggle -- Toggle disabled flag for selected markers.
    """

def graph_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
    extend: bool | None = False,
) -> None:
    """Select graph curves

    :param location: Location, Mouse location to select nearest entity
    :param extend: Extend, Extend selection rather than clearing the existing selection
    """

def graph_select_all_markers(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Change selection of all markers of active track

        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
    """

def graph_select_box(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    deselect: bool | None = False,
    extend: bool | None = True,
) -> None:
    """Select curve points using box selection

    :param xmin: X Min
    :param xmax: X Max
    :param ymin: Y Min
    :param ymax: Y Max
    :param wait_for_input: Wait for Input
    :param deselect: Deselect, Deselect rather than select items
    :param extend: Extend, Extend selection instead of deselecting everything first
    """

def graph_view_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """View all curves in editor"""

def hide_tracks(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Hide selected tracks

    :param unselected: Unselected, Hide unselected tracks
    """

def hide_tracks_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear hide selected tracks"""

def join_tracks(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Join selected tracks"""

def keyframe_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete a keyframe from selected tracks at current frame"""

def keyframe_insert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Insert a keyframe to selected tracks at current frame"""

def lock_selection_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle Lock Selection option of the current clip editor"""

def lock_tracks(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["LOCK", "UNLOCK", "TOGGLE"] | None = "LOCK",
) -> None:
    """Lock/unlock selected tracks

        :param action: Action, Lock action to execute

    LOCK
    Lock -- Lock selected tracks.

    UNLOCK
    Unlock -- Unlock selected tracks.

    TOGGLE
    Toggle -- Toggle locked flag for selected tracks.
    """

def mode_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: bpy.stub_internal.rna_enums.ClipEditorModeItems | None = "TRACKING",
) -> None:
    """Set the clip interaction mode

    :param mode: Mode
    """

def new_image_from_plane_marker(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create new image from the content of the plane marker"""

def open(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = True,
    filter_movie: bool | None = True,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    relative_path: bool | None = True,
    show_multiview: bool | None = False,
    use_multiview: bool | None = False,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: typing.Literal[
        "DEFAULT",
        "FILE_SORT_ALPHA",
        "FILE_SORT_EXTENSION",
        "FILE_SORT_TIME",
        "FILE_SORT_SIZE",
        "ASSET_CATALOG",
    ]
    | None = "",
) -> None:
    """Load a sequence of frames or a movie file

        :param directory: Directory, Directory of the file
        :param files: Files
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :param filter_blender: Filter .blend files
        :param filter_backup: Filter .blend files
        :param filter_image: Filter image files
        :param filter_movie: Filter movie files
        :param filter_python: Filter Python files
        :param filter_font: Filter font files
        :param filter_sound: Filter sound files
        :param filter_text: Filter text files
        :param filter_archive: Filter archive files
        :param filter_btx: Filter btx files
        :param filter_alembic: Filter Alembic files
        :param filter_usd: Filter USD files
        :param filter_obj: Filter OBJ files
        :param filter_volume: Filter OpenVDB volume files
        :param filter_folder: Filter folders
        :param filter_blenlib: Filter Blender IDs
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :param relative_path: Relative Path, Select the file relative to the blend file
        :param show_multiview: Enable Multi-View
        :param use_multiview: Use Multi-View
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :param sort_method: File sorting mode

    DEFAULT
    Default -- Automatically determine sort method for files.

    FILE_SORT_ALPHA
    Name -- Sort the file list alphabetically.

    FILE_SORT_EXTENSION
    Extension -- Sort the file list by extension/type.

    FILE_SORT_TIME
    Modified Date -- Sort files by modification time.

    FILE_SORT_SIZE
    Size -- Sort files by size.

    ASSET_CATALOG
    Asset Catalog -- Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..
    """

def paste_tracks(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Paste tracks from the internal clipboard"""

def prefetch(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Prefetch frames from disk for faster playback/tracking"""

def rebuild_proxy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Rebuild all selected proxies and timecode indices in the background"""

def refine_markers(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    backwards: bool | None = False,
) -> None:
    """Refine selected markers positions by running the tracker from tracks reference to current frame

    :param backwards: Backwards, Do backwards tracking
    """

def reload(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reload clip"""

def select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect_all: bool | None = False,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Select tracking markers

    :param extend: Extend, Extend selection rather than clearing the existing selection
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Change selection of all tracking markers

        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
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
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
) -> None:
    """Select markers using box selection

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
    """Select markers using circle selection

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

def select_grouped(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    group: typing.Literal[
        "KEYFRAMED", "ESTIMATED", "TRACKED", "LOCKED", "DISABLED", "COLOR", "FAILED"
    ]
    | None = "ESTIMATED",
) -> None:
    """Select all tracks from specified group

        :param group: Action, Clear action to execute

    KEYFRAMED
    Keyframed Tracks -- Select all keyframed tracks.

    ESTIMATED
    Estimated Tracks -- Select all estimated tracks.

    TRACKED
    Tracked Tracks -- Select all tracked tracks.

    LOCKED
    Locked Tracks -- Select all locked tracks.

    DISABLED
    Disabled Tracks -- Select all disabled tracks.

    COLOR
    Tracks with Same Color -- Select all tracks with same color as active track.

    FAILED
    Failed Tracks -- Select all tracks which failed to be reconstructed.
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
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
) -> None:
    """Select markers using lasso selection

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
    """

def set_active_clip(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

def set_axis(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    axis: typing.Literal["X", "Y"] | None = "X",
) -> None:
    """Set the direction of a scene axis by rotating the camera (or its parent if present). This assumes that the selected track lies on a real axis connecting it to the origin

        :param axis: Axis, Axis to use to align bundle along

    X
    X -- Align bundle align X axis.

    Y
    Y -- Align bundle align Y axis.
    """

def set_origin(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_median: bool | None = False,
) -> None:
    """Set active marker as origin by moving camera (or its parent if present) in 3D space

    :param use_median: Use Median, Set origin to median point of selected bundles
    """

def set_plane(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    plane: typing.Literal["FLOOR", "WALL"] | None = "FLOOR",
) -> None:
    """Set plane based on 3 selected bundles by moving camera (or its parent if present) in 3D space

        :param plane: Plane, Plane to be used for orientation

    FLOOR
    Floor -- Set floor plane.

    WALL
    Wall -- Set wall plane.
    """

def set_scale(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    distance: float | None = 0.0,
) -> None:
    """Set scale of scene by scaling camera (or its parent if present)

    :param distance: Distance, Distance between selected tracks
    """

def set_scene_frames(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set scenes start and end frame to match clips start frame and length"""

def set_solution_scale(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    distance: float | None = 0.0,
) -> None:
    """Set object solution scale using distance between two selected tracks

    :param distance: Distance, Distance between selected tracks
    """

def set_solver_keyframe(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keyframe: typing.Literal["KEYFRAME_A", "KEYFRAME_B"] | None = "KEYFRAME_A",
) -> None:
    """Set keyframe used by solver

    :param keyframe: Keyframe, Keyframe to set
    """

def set_viewport_background(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set current movie clip as a camera background in 3D Viewport (works only when a 3D Viewport is visible)"""

def setup_tracking_scene(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Prepare scene for compositing 3D objects into this footage"""

def slide_marker(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Slide marker areas

    :param offset: Offset, Offset in floating-point units, 1.0 is the width and height of the image
    """

def slide_plane_marker(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Slide plane marker areas"""

def solve_camera(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Solve camera motion from tracks"""

def stabilize_2d_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add selected tracks to 2D translation stabilization"""

def stabilize_2d_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove selected track from translation stabilization"""

def stabilize_2d_rotation_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add selected tracks to 2D rotation stabilization"""

def stabilize_2d_rotation_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove selected track from rotation stabilization"""

def stabilize_2d_rotation_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select tracks which are used for rotation stabilization"""

def stabilize_2d_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select tracks which are used for translation stabilization"""

def track_color_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add or remove a Clip Track Color Preset

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def track_copy_color(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy color to all selected tracks"""

def track_markers(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    backwards: bool | None = False,
    sequence: bool | None = False,
) -> None:
    """Track selected markers

    :param backwards: Backwards, Do backwards tracking
    :param sequence: Track Sequence, Track marker during image sequence rather than single image
    """

def track_settings_as_default(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy tracking settings from active track to default settings"""

def track_settings_to_track(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy tracking settings from active track to selected tracks"""

def track_to_empty(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create an Empty object which will be copying movement of active track"""

def tracking_object_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add new object for tracking"""

def tracking_object_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove object for tracking"""

def tracking_settings_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add or remove a motion tracking settings preset

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def update_image_from_plane_marker(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Update current image used by plane marker from the content of the plane marker"""

def view_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    fit_view: bool | None = False,
) -> None:
    """View whole image with markers

    :param fit_view: Fit View, Fit frame to the viewport
    """

def view_center_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Center the view so that the cursor is in the middle of the view"""

def view_ndof(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Use a 3D mouse device to pan/zoom the view"""

def view_pan(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Pan the view

    :param offset: Offset, Offset in floating-point units, 1.0 is the width and height of the image
    """

def view_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """View all selected elements"""

def view_zoom(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.0,
    use_cursor_init: bool | None = True,
) -> None:
    """Zoom in/out the view

    :param factor: Factor, Zoom factor, values higher than 1.0 zoom in, lower values zoom out
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    """

def view_zoom_in(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Zoom in the view

    :param location: Location, Cursor location in screen coordinates
    """

def view_zoom_out(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Zoom out the view

    :param location: Location, Cursor location in normalized (0.0 to 1.0) coordinates
    """

def view_zoom_ratio(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 0.0,
) -> None:
    """Set the zoom ratio (based on clip size)

    :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out
    """
