import typing
import collections.abc
import typing_extensions
import bpy._typing.rna_enums
import bpy.ops.transform
import bpy.types
import mathutils

def add_marker(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Place new marker at specified location

    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Location of marker on frame
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def add_marker_at_click(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Place new marker at the desired (clicked) position

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def add_marker_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    CLIP_OT_add_marker: add_marker | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Add new marker and move it on movie

    :type execution_context: int | str | None
    :type undo: bool | None
    :param CLIP_OT_add_marker: Add Marker, Place new marker at specified location
    :type CLIP_OT_add_marker: add_marker | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def add_marker_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    CLIP_OT_add_marker: add_marker | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Add new marker and slide it with mouse until mouse button release

    :type execution_context: int | str | None
    :type undo: bool | None
    :param CLIP_OT_add_marker: Add Marker, Place new marker at specified location
    :type CLIP_OT_add_marker: add_marker | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def apply_solution_scale(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    distance: float | None = 0.0,
):
    """Apply scale on solution itself to make distance between selected tracks equals to desired

    :type execution_context: int | str | None
    :type undo: bool | None
    :param distance: Distance, Distance between selected tracks
    :type distance: float | None
    """

def average_tracks(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keep_original: bool | None = True,
):
    """Average selected tracks into active

    :type execution_context: int | str | None
    :type undo: bool | None
    :param keep_original: Keep Original, Keep original tracks
    :type keep_original: bool | None
    """

def bundles_to_mesh(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Create vertex cloud using coordinates of reconstructed tracks

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def camera_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
    use_focal_length: bool | None = True,
):
    """Add or remove a Tracking Camera Intrinsics Preset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    :param use_focal_length: Include Focal Length, Include focal length into the preset
    :type use_focal_length: bool | None
    """

def change_frame(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame: int | None = 0,
):
    """Interactively change the current frame number

    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame: Frame
    :type frame: int | None
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
):
    """Clean tracks with high error values or few frames

        :type execution_context: int | str | None
        :type undo: bool | None
        :param frames: Tracked Frames, Affect tracks which are tracked less than the specified number of frames
        :type frames: int | None
        :param error: Reprojection Error, Affect tracks which have a larger reprojection error
        :type error: float | None
        :param action: Action, Cleanup action to execute

    SELECT
    Select -- Select unclean tracks.

    DELETE_TRACK
    Delete Track -- Delete unclean tracks.

    DELETE_SEGMENTS
    Delete Segments -- Delete unclean segments of tracks.
        :type action: typing.Literal['SELECT','DELETE_TRACK','DELETE_SEGMENTS'] | None
    """

def clear_solution(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Clear all calculated data

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def clear_track_path(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["UPTO", "REMAINED", "ALL"] | None = "REMAINED",
    clear_active: bool | None = False,
):
    """Clear tracks after/before current position or clear the whole track

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Clear action to execute

    UPTO
    Clear Up To -- Clear path up to current frame.

    REMAINED
    Clear Remained -- Clear path at remaining frames (after current).

    ALL
    Clear All -- Clear the whole path.
        :type action: typing.Literal['UPTO','REMAINED','ALL'] | None
        :param clear_active: Clear Active, Clear active track only instead of all selected tracks
        :type clear_active: bool | None
    """

def constraint_to_fcurve(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Create F-Curves for object which will copy object's movement caused by this constraint

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def copy_tracks(execution_context: int | str | None = None, undo: bool | None = None):
    """Copy the selected tracks to the internal clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def create_plane_track(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Create new plane track out of selected point tracks

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def cursor_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Set 2D cursor location

    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Cursor location in normalized clip coordinates
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def delete_marker(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
):
    """Delete marker for current frame from selected tracks

    :type execution_context: int | str | None
    :type undo: bool | None
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool | None
    """

def delete_proxy(execution_context: int | str | None = None, undo: bool | None = None):
    """Delete movie clip proxy files from the hard drive

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def delete_track(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
):
    """Delete selected tracks

    :type execution_context: int | str | None
    :type undo: bool | None
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool | None
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
):
    """Automatically detect features and place markers to track

        :type execution_context: int | str | None
        :type undo: bool | None
        :param placement: Placement, Placement for detected features

    FRAME
    Whole Frame -- Place markers across the whole frame.

    INSIDE_GPENCIL
    Inside Annotated Area -- Place markers only inside areas outlined with the Annotation tool.

    OUTSIDE_GPENCIL
    Outside Annotated Area -- Place markers only outside areas outlined with the Annotation tool.
        :type placement: typing.Literal['FRAME','INSIDE_GPENCIL','OUTSIDE_GPENCIL'] | None
        :param margin: Margin, Only features further than margin pixels from the image edges are considered
        :type margin: int | None
        :param threshold: Threshold, Threshold level to consider feature good enough for tracking
        :type threshold: float | None
        :param min_distance: Distance, Minimal distance accepted between two features
        :type min_distance: int | None
    """

def disable_markers(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["DISABLE", "ENABLE", "TOGGLE"] | None = "DISABLE",
):
    """Disable/enable selected markers

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Disable action to execute

    DISABLE
    Disable -- Disable selected markers.

    ENABLE
    Enable -- Enable selected markers.

    TOGGLE
    Toggle -- Toggle disabled flag for selected markers.
        :type action: typing.Literal['DISABLE','ENABLE','TOGGLE'] | None
    """

def dopesheet_select_channel(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
    extend: bool | None = False,
):
    """Select movie tracking channel

    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Mouse location to select channel
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool | None
    """

def dopesheet_view_all(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Reset viewable area to show full keyframe range

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def filter_tracks(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    track_threshold: float | None = 5.0,
):
    """Filter tracks which has weirdly looking spikes in motion curves

    :type execution_context: int | str | None
    :type undo: bool | None
    :param track_threshold: Track Threshold, Filter Threshold to select problematic tracks
    :type track_threshold: float | None
    """

def frame_jump(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    position: typing.Literal["PATHSTART", "PATHEND", "FAILEDPREV", "FAILNEXT"]
    | None = "PATHSTART",
):
    """Jump to special frame

        :type execution_context: int | str | None
        :type undo: bool | None
        :param position: Position, Position to jump to

    PATHSTART
    Path Start -- Jump to start of current path.

    PATHEND
    Path End -- Jump to end of current path.

    FAILEDPREV
    Previous Failed -- Jump to previous failed frame.

    FAILNEXT
    Next Failed -- Jump to next failed frame.
        :type position: typing.Literal['PATHSTART','PATHEND','FAILEDPREV','FAILNEXT'] | None
    """

def graph_center_current_frame(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Scroll view so current frame would be centered

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def graph_delete_curve(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
):
    """Delete track corresponding to the selected curve

    :type execution_context: int | str | None
    :type undo: bool | None
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool | None
    """

def graph_delete_knot(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Delete curve knots

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def graph_disable_markers(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["DISABLE", "ENABLE", "TOGGLE"] | None = "DISABLE",
):
    """Disable/enable selected markers

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Disable action to execute

    DISABLE
    Disable -- Disable selected markers.

    ENABLE
    Enable -- Enable selected markers.

    TOGGLE
    Toggle -- Toggle disabled flag for selected markers.
        :type action: typing.Literal['DISABLE','ENABLE','TOGGLE'] | None
    """

def graph_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
    extend: bool | None = False,
):
    """Select graph curves

    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Mouse location to select nearest entity
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool | None
    """

def graph_select_all_markers(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Change selection of all markers of active track

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
        :type action: typing.Literal['TOGGLE','SELECT','DESELECT','INVERT'] | None
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
):
    """Select curve points using box selection

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
    :param deselect: Deselect, Deselect rather than select items
    :type deselect: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | None
    """

def graph_view_all(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """View all curves in editor

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def hide_tracks(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
):
    """Hide selected tracks

    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected tracks
    :type unselected: bool | None
    """

def hide_tracks_clear(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Clear hide selected tracks

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def join_tracks(execution_context: int | str | None = None, undo: bool | None = None):
    """Join selected tracks

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def keyframe_delete(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Delete a keyframe from selected tracks at current frame

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def keyframe_insert(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Insert a keyframe to selected tracks at current frame

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def lock_selection_toggle(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Toggle Lock Selection option of the current clip editor

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def lock_tracks(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["LOCK", "UNLOCK", "TOGGLE"] | None = "LOCK",
):
    """Lock/unlock selected tracks

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Lock action to execute

    LOCK
    Lock -- Lock selected tracks.

    UNLOCK
    Unlock -- Unlock selected tracks.

    TOGGLE
    Toggle -- Toggle locked flag for selected tracks.
        :type action: typing.Literal['LOCK','UNLOCK','TOGGLE'] | None
    """

def mode_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: bpy._typing.rna_enums.ClipEditorModeItems | None = "TRACKING",
):
    """Set the clip interaction mode

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: bpy._typing.rna_enums.ClipEditorModeItems | None
    """

def new_image_from_plane_marker(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Create new image from the content of the plane marker

    :type execution_context: int | str | None
    :type undo: bool | None
    """

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
    filter_collada: bool | None = False,
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
    ]
    | None = "",
):
    """Load a sequence of frames or a movie file

        :type execution_context: int | str | None
        :type undo: bool | None
        :param directory: Directory, Directory of the file
        :type directory: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | None
        :param show_multiview: Enable Multi-View
        :type show_multiview: bool | None
        :param use_multiview: Use Multi-View
        :type use_multiview: bool | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
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
        :type sort_method: typing.Literal['DEFAULT','FILE_SORT_ALPHA','FILE_SORT_EXTENSION','FILE_SORT_TIME','FILE_SORT_SIZE'] | None
    """

def paste_tracks(execution_context: int | str | None = None, undo: bool | None = None):
    """Paste tracks from the internal clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def prefetch(execution_context: int | str | None = None, undo: bool | None = None):
    """Prefetch frames from disk for faster playback/tracking

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def rebuild_proxy(execution_context: int | str | None = None, undo: bool | None = None):
    """Rebuild all selected proxies and timecode indices in the background

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def refine_markers(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    backwards: bool | None = False,
):
    """Refine selected markers positions by running the tracker from track's reference to current frame

    :type execution_context: int | str | None
    :type undo: bool | None
    :param backwards: Backwards, Do backwards tracking
    :type backwards: bool | None
    """

def reload(execution_context: int | str | None = None, undo: bool | None = None):
    """Reload clip

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect_all: bool | None = False,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Select tracking markers

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool | None
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool | None
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Change selection of all tracking markers

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
        :type action: typing.Literal['TOGGLE','SELECT','DESELECT','INVERT'] | None
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
):
    """Select markers using box selection

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
        :type mode: typing.Literal['SET','ADD','SUB'] | None
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
    """Select markers using circle selection

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

def select_grouped(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    group: typing.Literal[
        "KEYFRAMED", "ESTIMATED", "TRACKED", "LOCKED", "DISABLED", "COLOR", "FAILED"
    ]
    | None = "ESTIMATED",
):
    """Select all tracks from specified group

        :type execution_context: int | str | None
        :type undo: bool | None
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
        :type group: typing.Literal['KEYFRAMED','ESTIMATED','TRACKED','LOCKED','DISABLED','COLOR','FAILED'] | None
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
):
    """Select markers using lasso selection

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
        :type mode: typing.Literal['SET','ADD','SUB'] | None
    """

def set_active_clip(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def set_axis(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    axis: typing.Literal["X", "Y"] | None = "X",
):
    """Set the direction of a scene axis by rotating the camera (or its parent if present). This assumes that the selected track lies on a real axis connecting it to the origin

        :type execution_context: int | str | None
        :type undo: bool | None
        :param axis: Axis, Axis to use to align bundle along

    X
    X -- Align bundle align X axis.

    Y
    Y -- Align bundle align Y axis.
        :type axis: typing.Literal['X','Y'] | None
    """

def set_origin(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_median: bool | None = False,
):
    """Set active marker as origin by moving camera (or its parent if present) in 3D space

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_median: Use Median, Set origin to median point of selected bundles
    :type use_median: bool | None
    """

def set_plane(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    plane: typing.Literal["FLOOR", "WALL"] | None = "FLOOR",
):
    """Set plane based on 3 selected bundles by moving camera (or its parent if present) in 3D space

        :type execution_context: int | str | None
        :type undo: bool | None
        :param plane: Plane, Plane to be used for orientation

    FLOOR
    Floor -- Set floor plane.

    WALL
    Wall -- Set wall plane.
        :type plane: typing.Literal['FLOOR','WALL'] | None
    """

def set_scale(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    distance: float | None = 0.0,
):
    """Set scale of scene by scaling camera (or its parent if present)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param distance: Distance, Distance between selected tracks
    :type distance: float | None
    """

def set_scene_frames(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Set scene's start and end frame to match clip's start frame and length

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def set_solution_scale(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    distance: float | None = 0.0,
):
    """Set object solution scale using distance between two selected tracks

    :type execution_context: int | str | None
    :type undo: bool | None
    :param distance: Distance, Distance between selected tracks
    :type distance: float | None
    """

def set_solver_keyframe(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keyframe: typing.Literal["KEYFRAME_A", "KEYFRAME_B"] | None = "KEYFRAME_A",
):
    """Set keyframe used by solver

    :type execution_context: int | str | None
    :type undo: bool | None
    :param keyframe: Keyframe, Keyframe to set
    :type keyframe: typing.Literal['KEYFRAME_A','KEYFRAME_B'] | None
    """

def set_viewport_background(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Set current movie clip as a camera background in 3D Viewport (works only when a 3D Viewport is visible)

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def setup_tracking_scene(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Prepare scene for compositing 3D objects into this footage

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def slide_marker(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Slide marker areas

    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Offset, Offset in floating-point units, 1.0 is the width and height of the image
    :type offset: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def slide_plane_marker(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Slide plane marker areas

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def solve_camera(execution_context: int | str | None = None, undo: bool | None = None):
    """Solve camera motion from tracks

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def stabilize_2d_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add selected tracks to 2D translation stabilization

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def stabilize_2d_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove selected track from translation stabilization

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def stabilize_2d_rotation_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add selected tracks to 2D rotation stabilization

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def stabilize_2d_rotation_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove selected track from rotation stabilization

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def stabilize_2d_rotation_select(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Select tracks which are used for rotation stabilization

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def stabilize_2d_select(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Select tracks which are used for translation stabilization

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def track_color_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
):
    """Add or remove a Clip Track Color Preset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def track_copy_color(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Copy color to all selected tracks

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def track_markers(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    backwards: bool | None = False,
    sequence: bool | None = False,
):
    """Track selected markers

    :type execution_context: int | str | None
    :type undo: bool | None
    :param backwards: Backwards, Do backwards tracking
    :type backwards: bool | None
    :param sequence: Track Sequence, Track marker during image sequence rather than single image
    :type sequence: bool | None
    """

def track_settings_as_default(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Copy tracking settings from active track to default settings

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def track_settings_to_track(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Copy tracking settings from active track to selected tracks

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def track_to_empty(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Create an Empty object which will be copying movement of active track

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def tracking_object_new(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add new object for tracking

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def tracking_object_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove object for tracking

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def tracking_settings_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
):
    """Add or remove a motion tracking settings preset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def update_image_from_plane_marker(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Update current image used by plane marker from the content of the plane marker

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    fit_view: bool | None = False,
):
    """View whole image with markers

    :type execution_context: int | str | None
    :type undo: bool | None
    :param fit_view: Fit View, Fit frame to the viewport
    :type fit_view: bool | None
    """

def view_center_cursor(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Center the view so that the cursor is in the middle of the view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_ndof(execution_context: int | str | None = None, undo: bool | None = None):
    """Use a 3D mouse device to pan/zoom the view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_pan(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Pan the view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Offset, Offset in floating-point units, 1.0 is the width and height of the image
    :type offset: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def view_selected(execution_context: int | str | None = None, undo: bool | None = None):
    """View all selected elements

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_zoom(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.0,
    use_cursor_init: bool | None = True,
):
    """Zoom in/out the view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, Zoom factor, values higher than 1.0 zoom in, lower values zoom out
    :type factor: float | None
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    :type use_cursor_init: bool | None
    """

def view_zoom_in(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Zoom in the view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Cursor location in screen coordinates
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def view_zoom_out(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Zoom out the view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Cursor location in normalized (0.0 to 1.0) coordinates
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def view_zoom_ratio(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 0.0,
):
    """Set the zoom ratio (based on clip size)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out
    :type ratio: float | None
    """
