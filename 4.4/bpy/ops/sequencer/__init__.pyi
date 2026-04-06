import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops.transform
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

def change_effect_input(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

def change_effect_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "CROSS",
        "ADD",
        "SUBTRACT",
        "ALPHA_OVER",
        "ALPHA_UNDER",
        "GAMMA_CROSS",
        "MULTIPLY",
        "OVER_DROP",
        "WIPE",
        "GLOW",
        "TRANSFORM",
        "COLOR",
        "SPEED",
        "MULTICAM",
        "ADJUSTMENT",
        "GAUSSIAN_BLUR",
        "TEXT",
        "COLORMIX",
    ]
    | None = "CROSS",
) -> None:
    """Undocumented, consider contributing.

        :param type: Type, Sequencer effect type

    CROSS
    Crossfade -- Crossfade effect strip type.

    ADD
    Add -- Add effect strip type.

    SUBTRACT
    Subtract -- Subtract effect strip type.

    ALPHA_OVER
    Alpha Over -- Alpha Over effect strip type.

    ALPHA_UNDER
    Alpha Under -- Alpha Under effect strip type.

    GAMMA_CROSS
    Gamma Cross -- Gamma Cross effect strip type.

    MULTIPLY
    Multiply -- Multiply effect strip type.

    OVER_DROP
    Alpha Over Drop -- Alpha Over Drop effect strip type.

    WIPE
    Wipe -- Wipe effect strip type.

    GLOW
    Glow -- Glow effect strip type.

    TRANSFORM
    Transform -- Transform effect strip type.

    COLOR
    Color -- Color effect strip type.

    SPEED
    Speed -- Color effect strip type.

    MULTICAM
    Multicam Selector.

    ADJUSTMENT
    Adjustment Layer.

    GAUSSIAN_BLUR
    Gaussian Blur.

    TEXT
    Text.

    COLORMIX
    Color Mix.
    """

def change_path(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = False,
    filter_movie: bool | None = False,
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
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    use_placeholders: bool | None = False,
) -> None:
    """Undocumented, consider contributing.

        :param filepath: File Path, Path to file
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
        :param filter_collada: Filter COLLADA files
        :param filter_alembic: Filter Alembic files
        :param filter_usd: Filter USD files
        :param filter_obj: Filter OBJ files
        :param filter_volume: Filter OpenVDB volume files
        :param filter_folder: Filter folders
        :param filter_blenlib: Filter Blender IDs
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :param relative_path: Relative Path, Select the file relative to the blend file
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
        :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip
    """

def change_scene(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    scene: str | None = "",
) -> None:
    """Change Scene assigned to Strip

    :param scene: Scene
    """

def connect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    toggle: bool | None = True,
) -> None:
    """Link selected strips together for simplified group selection

    :param toggle: Toggle, Toggle strip connections
    """

def copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the selected strips to the internal clipboard"""

def crossfade_sounds(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Do cross-fading volume animation of two selected sound strips"""

def cursor_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Set 2D cursor location

    :param location: Location, Cursor location in normalized preview coordinates
    """

def deinterlace_selected_movies(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Deinterlace all selected movie sources"""

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delete_data: bool | None = False,
) -> None:
    """Delete selected strips from the sequencer

    :param delete_data: Delete Data, After removing the Strip, delete the associated data also
    """

def disconnect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Unlink selected strips so that they can be selected individually"""

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Duplicate the selected strips"""

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    SEQUENCER_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None = None,
) -> None:
    """Duplicate selected strips and move them

    :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips
    :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
    """

def effect_strip_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "CROSS",
        "ADD",
        "SUBTRACT",
        "ALPHA_OVER",
        "ALPHA_UNDER",
        "GAMMA_CROSS",
        "MULTIPLY",
        "OVER_DROP",
        "WIPE",
        "GLOW",
        "TRANSFORM",
        "COLOR",
        "SPEED",
        "MULTICAM",
        "ADJUSTMENT",
        "GAUSSIAN_BLUR",
        "TEXT",
        "COLORMIX",
    ]
    | None = "CROSS",
    frame_start: int | None = 0,
    frame_end: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    color: collections.abc.Sequence[float] | mathutils.Color | None = (0.0, 0.0, 0.0),
) -> None:
    """Add an effect to the sequencer, most are applied on top of existing strips

        :param type: Type, Sequencer effect type

    CROSS
    Crossfade -- Crossfade effect strip type.

    ADD
    Add -- Add effect strip type.

    SUBTRACT
    Subtract -- Subtract effect strip type.

    ALPHA_OVER
    Alpha Over -- Alpha Over effect strip type.

    ALPHA_UNDER
    Alpha Under -- Alpha Under effect strip type.

    GAMMA_CROSS
    Gamma Cross -- Gamma Cross effect strip type.

    MULTIPLY
    Multiply -- Multiply effect strip type.

    OVER_DROP
    Alpha Over Drop -- Alpha Over Drop effect strip type.

    WIPE
    Wipe -- Wipe effect strip type.

    GLOW
    Glow -- Glow effect strip type.

    TRANSFORM
    Transform -- Transform effect strip type.

    COLOR
    Color -- Color effect strip type.

    SPEED
    Speed -- Color effect strip type.

    MULTICAM
    Multicam Selector.

    ADJUSTMENT
    Adjustment Layer.

    GAUSSIAN_BLUR
    Gaussian Blur.

    TEXT
    Text.

    COLORMIX
    Color Mix.
        :param frame_start: Start Frame, Start frame of the sequence strip
        :param frame_end: End Frame, End frame for the color strip
        :param channel: Channel, Channel to place this strip into
        :param replace_sel: Replace Selection, Deselect previously selected strips
        :param overlap: Allow Overlap, Dont correct overlap on new sequence strips
        :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
        :param color: Color, Initialize the strip with this color
    """

def enable_proxies(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    proxy_25: bool | None = False,
    proxy_50: bool | None = False,
    proxy_75: bool | None = False,
    proxy_100: bool | None = False,
    overwrite: bool | None = False,
) -> None:
    """Enable selected proxies on all selected Movie and Image strips

    :param proxy_25: 25%
    :param proxy_50: 50%
    :param proxy_75: 75%
    :param proxy_100: 100%
    :param overwrite: Overwrite
    """

def export_subtitles(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = True,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = False,
    filter_movie: bool | None = False,
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
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
) -> None:
    """Export .srt file containing text strips

        :param filepath: File Path, Path to file
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
        :param filter_collada: Filter COLLADA files
        :param filter_alembic: Filter Alembic files
        :param filter_usd: Filter USD files
        :param filter_obj: Filter OBJ files
        :param filter_volume: Filter OpenVDB volume files
        :param filter_folder: Filter folders
        :param filter_blenlib: Filter Blender IDs
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
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
    """

def fades_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    duration_seconds: float | None = 1.0,
    type: typing.Literal["IN_OUT", "IN", "OUT", "CURSOR_FROM", "CURSOR_TO"]
    | None = "IN_OUT",
) -> None:
    """Adds or updates a fade animation for either visual or audio strips

        :param duration_seconds: Fade Duration, Duration of the fade in seconds
        :param type: Fade Type, Fade in, out, both in and out, to, or from the current frame. Default is both in and out

    IN_OUT
    Fade In and Out -- Fade selected strips in and out.

    IN
    Fade In -- Fade in selected strips.

    OUT
    Fade Out -- Fade out selected strips.

    CURSOR_FROM
    From Current Frame -- Fade from the time cursor to the end of overlapping sequences.

    CURSOR_TO
    To Current Frame -- Fade from the start of sequences under the time cursor to the current frame.
    """

def fades_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Removes fade animation from selected sequences"""

def gap_insert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frames: int | None = 10,
) -> None:
    """Insert gap at current frame to first strips at the right, independent of selection or locked state of strips

    :param frames: Frames, Frames to insert after current strip
    """

def gap_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
) -> None:
    """Remove gap at current frame to first strip at the right, independent of selection or locked state of strips

    :param all: All Gaps, Do all gaps to right of current frame
    """

def image_strip_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = True,
    filter_movie: bool | None = False,
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
        "ASSET_CATALOG",
    ]
    | None = "",
    frame_start: int | None = 0,
    frame_end: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    fit_method: typing.Literal["FIT", "FILL", "STRETCH", "ORIGINAL"] | None = "FIT",
    set_view_transform: bool | None = True,
    use_placeholders: bool | None = False,
) -> None:
    """Add an image or image sequence to the sequencer

        :param directory: Directory, Directory of the file
        :param files: Files
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
        :param filter_collada: Filter COLLADA files
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
        :param frame_start: Start Frame, Start frame of the sequence strip
        :param frame_end: End Frame, End frame for the color strip
        :param channel: Channel, Channel to place this strip into
        :param replace_sel: Replace Selection, Deselect previously selected strips
        :param overlap: Allow Overlap, Dont correct overlap on new sequence strips
        :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
        :param fit_method: Fit Method, Scale fit method

    FIT
    Scale to Fit -- Scale image to fit within the canvas.

    FILL
    Scale to Fill -- Scale image to completely fill the canvas.

    STRETCH
    Stretch to Fill -- Stretch image to fill the canvas.

    ORIGINAL
    Use Original Size -- Keep image at its original size.
        :param set_view_transform: Set View Transform, Set appropriate view transform based on media color space
        :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip
    """

def images_separate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    length: int | None = 1,
) -> None:
    """On image sequence strips, it returns a strip for each image

    :param length: Length, Length of each frame
    """

def lock(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Lock strips so they cant be transformed"""

def mask_strip_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    mask: str | None = "",
) -> None:
    """Add a mask strip to the sequencer

    :param frame_start: Start Frame, Start frame of the sequence strip
    :param channel: Channel, Channel to place this strip into
    :param replace_sel: Replace Selection, Deselect previously selected strips
    :param overlap: Allow Overlap, Dont correct overlap on new sequence strips
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :param mask: Mask
    """

def meta_make(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Group selected strips into a meta-strip"""

def meta_separate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Put the contents of a meta-strip back in the sequencer"""

def meta_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle a meta-strip (to edit enclosed strips)"""

def movie_strip_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = False,
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
        "ASSET_CATALOG",
    ]
    | None = "",
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    fit_method: typing.Literal["FIT", "FILL", "STRETCH", "ORIGINAL"] | None = "FIT",
    set_view_transform: bool | None = True,
    adjust_playback_rate: bool | None = True,
    sound: bool | None = True,
    use_framerate: bool | None = True,
) -> None:
    """Add a movie strip to the sequencer

        :param filepath: File Path, Path to file
        :param directory: Directory, Directory of the file
        :param files: Files
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
        :param filter_collada: Filter COLLADA files
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
        :param frame_start: Start Frame, Start frame of the sequence strip
        :param channel: Channel, Channel to place this strip into
        :param replace_sel: Replace Selection, Deselect previously selected strips
        :param overlap: Allow Overlap, Dont correct overlap on new sequence strips
        :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
        :param fit_method: Fit Method, Scale fit method

    FIT
    Scale to Fit -- Scale image to fit within the canvas.

    FILL
    Scale to Fill -- Scale image to completely fill the canvas.

    STRETCH
    Stretch to Fill -- Stretch image to fill the canvas.

    ORIGINAL
    Use Original Size -- Keep image at its original size.
        :param set_view_transform: Set View Transform, Set appropriate view transform based on media color space
        :param adjust_playback_rate: Adjust Playback Rate, Play at normal speed regardless of scene FPS
        :param sound: Sound, Load sound with the movie
        :param use_framerate: Set Scene Frame Rate, Set frame rate of the current scene to the frame rate of the movie
    """

def movieclip_strip_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    clip: str | None = "",
) -> None:
    """Add a movieclip strip to the sequencer

    :param frame_start: Start Frame, Start frame of the sequence strip
    :param channel: Channel, Channel to place this strip into
    :param replace_sel: Replace Selection, Deselect previously selected strips
    :param overlap: Allow Overlap, Dont correct overlap on new sequence strips
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :param clip: Clip
    """

def mute(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Mute (un)selected strips

    :param unselected: Unselected, Mute unselected rather than selected strips
    """

def offset_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear strip offsets from the start and end frames"""

def paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keep_offset: bool | None = False,
) -> None:
    """Paste strips from the internal clipboard

    :param keep_offset: Keep Offset, Keep strip offset relative to the current frame when pasting
    """

def preview_duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    SEQUENCER_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Duplicate selected strips and move them

    :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def reassign_inputs(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reassign the inputs for the effect strip"""

def rebuild_proxy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Rebuild all selected proxies and timecode indices"""

def refresh_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Refresh the sequencer editor"""

def reload(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    adjust_length: bool | None = False,
) -> None:
    """Reload strips in the sequencer

    :param adjust_length: Adjust Length, Adjust length of strips to their data length
    """

def rename_channel(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

def rendersize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set render size and aspect from active sequence"""

def retiming_add_freeze_frame_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    SEQUENCER_OT_retiming_freeze_frame_add: retiming_freeze_frame_add | None = None,
    TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None = None,
) -> None:
    """Add freeze frame and move it

    :param SEQUENCER_OT_retiming_freeze_frame_add: Add Freeze Frame, Add freeze frame
    :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
    """

def retiming_add_transition_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    SEQUENCER_OT_retiming_transition_add: retiming_transition_add | None = None,
    TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None = None,
) -> None:
    """Add smooth transition between 2 retimed segments and change its duration

    :param SEQUENCER_OT_retiming_transition_add: Add Speed Transition, Add smooth transition between 2 retimed segments
    :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
    """

def retiming_freeze_frame_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    duration: int | None = 0,
) -> None:
    """Add freeze frame

    :param duration: Duration, Duration of freeze frame segment
    """

def retiming_key_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    timeline_frame: int | None = 0,
) -> None:
    """Add retiming Key

    :param timeline_frame: Timeline Frame, Frame where key will be added
    """

def retiming_key_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete selected strips from the sequencer"""

def retiming_reset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset strip retiming"""

def retiming_segment_speed_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    speed: float | None = 100.0,
    keep_retiming: bool | None = True,
) -> None:
    """Set speed of retimed segment

    :param speed: Speed, New speed of retimed segment
    :param keep_retiming: Preserve Current Retiming, Keep speed of other segments unchanged, change strip length instead
    """

def retiming_show(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Show retiming keys in selected strips"""

def retiming_transition_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    duration: int | None = 0,
) -> None:
    """Add smooth transition between 2 retimed segments

    :param duration: Duration, Duration of freeze frame segment
    """

def sample(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    size: int | None = 1,
) -> None:
    """Use mouse to sample color in current frame

    :param size: Sample Size
    """

def scene_frame_range_update(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Update frame range of scene strip"""

def scene_strip_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    scene: str | None = "",
) -> None:
    """Add a strip to the sequencer using a Blender scene as a source

    :param frame_start: Start Frame, Start frame of the sequence strip
    :param channel: Channel, Channel to place this strip into
    :param replace_sel: Replace Selection, Deselect previously selected strips
    :param overlap: Allow Overlap, Dont correct overlap on new sequence strips
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :param scene: Scene
    """

def scene_strip_add_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    type: typing.Literal["NEW", "EMPTY", "LINK_COPY", "FULL_COPY"] | None = "NEW",
) -> None:
    """Create a new Strip and assign a new Scene as source

        :param frame_start: Start Frame, Start frame of the sequence strip
        :param channel: Channel, Channel to place this strip into
        :param replace_sel: Replace Selection, Deselect previously selected strips
        :param overlap: Allow Overlap, Dont correct overlap on new sequence strips
        :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
        :param type: Type

    NEW
    New -- Add new Strip with a new empty Scene with default settings.

    EMPTY
    Copy Settings -- Add a new Strip, with an empty scene, and copy settings from the current scene.

    LINK_COPY
    Linked Copy -- Add a Strip and link in the collections from the current scene (shallow copy).

    FULL_COPY
    Full Copy -- Add a Strip and make a full copy of the current scene.
    """

def select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    wait_to_deselect_others: bool | None = False,
    mouse_x: int | None = 0,
    mouse_y: int | None = 0,
    extend: bool | None = False,
    deselect: bool | None = False,
    toggle: bool | None = False,
    deselect_all: bool | None = False,
    select_passthrough: bool | None = False,
    center: bool | None = False,
    linked_handle: bool | None = False,
    linked_time: bool | None = False,
    side_of_frame: bool | None = False,
    ignore_connections: bool | None = False,
) -> None:
    """Select a strip (last selected becomes the "active strip")

    :param wait_to_deselect_others: Wait to Deselect Others
    :param mouse_x: Mouse X
    :param mouse_y: Mouse Y
    :param extend: Extend, Extend selection instead of deselecting everything first
    :param deselect: Deselect, Remove from selection
    :param toggle: Toggle Selection, Toggle the selection
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :param center: Center, Use the object center when selecting, in edit mode used to extend object selection
    :param linked_handle: Linked Handle, Select handles next to the active strip
    :param linked_time: Linked Time, Select other strips or handles at the same time, or all retiming keys after the current in retiming mode
    :param side_of_frame: Side of Frame, Select all strips on same side of the current frame as the mouse cursor
    :param ignore_connections: Ignore Connections, Select strips individually whether or not they are connected
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Select or deselect all strips

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
    tweak: bool | None = False,
    include_handles: bool | None = False,
    ignore_connections: bool | None = False,
) -> None:
    """Select strips using box selection

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
        :param tweak: Tweak, Make box select pass through to sequence slide when the cursor is hovering on a strip
        :param include_handles: Select Handles, Select the strips and their handles
        :param ignore_connections: Ignore Connections, Select strips individually whether or not they are connected
    """

def select_grouped(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "TYPE", "TYPE_BASIC", "TYPE_EFFECT", "DATA", "EFFECT", "EFFECT_LINK", "OVERLAP"
    ]
    | None = "TYPE",
    extend: bool | None = False,
    use_active_channel: bool | None = False,
) -> None:
    """Select all strips grouped by various properties

        :param type: Type

    TYPE
    Type -- Shared strip type.

    TYPE_BASIC
    Global Type -- All strips of same basic type (graphical or sound).

    TYPE_EFFECT
    Effect Type -- Shared strip effect type (if active strip is not an effect one, select all non-effect strips).

    DATA
    Data -- Shared data (scene, image, sound, etc.).

    EFFECT
    Effect -- Shared effects.

    EFFECT_LINK
    Effect/Linked -- Other strips affected by the active one (sharing some time, and below or effect-assigned).

    OVERLAP
    Overlap -- Overlapping time.
        :param extend: Extend, Extend selection instead of deselecting everything first
        :param use_active_channel: Same Channel, Only consider strips on the same channel as the active one
    """

def select_handle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    wait_to_deselect_others: bool | None = False,
    mouse_x: int | None = 0,
    mouse_y: int | None = 0,
    ignore_connections: bool | None = False,
) -> None:
    """Select strip handle

    :param wait_to_deselect_others: Wait to Deselect Others
    :param mouse_x: Mouse X
    :param mouse_y: Mouse Y
    :param ignore_connections: Ignore Connections, Select strips individually whether or not they are connected
    """

def select_handles(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    side: typing.Literal[
        "LEFT", "RIGHT", "BOTH", "LEFT_NEIGHBOR", "RIGHT_NEIGHBOR", "BOTH_NEIGHBORS"
    ]
    | None = "BOTH",
) -> None:
    """Select gizmo handles on the sides of the selected strip

    :param side: Side, The side of the handle that is selected
    """

def select_less(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Shrink the current selection of adjacent selected strips"""

def select_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all strips adjacent to the current selection"""

def select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
) -> None:
    """Select a chain of linked strips nearest to the mouse pointer

    :param extend: Extend, Extend the selection
    """

def select_more(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select more strips adjacent to the current selection"""

def select_side(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    side: typing.Literal["MOUSE", "LEFT", "RIGHT", "BOTH", "NO_CHANGE"] | None = "BOTH",
) -> None:
    """Select strips on the nominated side of the selected strips

    :param side: Side, The side to which the selection is applied
    """

def select_side_of_frame(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    side: typing.Literal["LEFT", "RIGHT", "CURRENT"] | None = "LEFT",
) -> None:
    """Select strips relative to the current frame

        :param extend: Extend, Extend the selection
        :param side: Side

    LEFT
    Left -- Select to the left of the current frame.

    RIGHT
    Right -- Select to the right of the current frame.

    CURRENT
    Current Frame -- Select intersecting with the current frame.
    """

def set_range_to_strips(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    preview: bool | None = False,
) -> None:
    """Set the frame range to the selected strips start and end

    :param preview: Preview, Set the preview range instead
    """

def slip(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: float | None = 0.0,
) -> None:
    """Slip the contents of selected strips

    :param offset: Offset, Offset to the data of the strip
    """

def snap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame: int | None = 0,
) -> None:
    """Frame where selected strips will be snapped

    :param frame: Frame, Frame where selected strips will be snapped
    """

def sound_strip_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = False,
    filter_movie: bool | None = False,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = True,
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
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    cache: bool | None = False,
    mono: bool | None = False,
) -> None:
    """Add a sound strip to the sequencer

        :param filepath: File Path, Path to file
        :param directory: Directory, Directory of the file
        :param files: Files
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
        :param filter_collada: Filter COLLADA files
        :param filter_alembic: Filter Alembic files
        :param filter_usd: Filter USD files
        :param filter_obj: Filter OBJ files
        :param filter_volume: Filter OpenVDB volume files
        :param filter_folder: Filter folders
        :param filter_blenlib: Filter Blender IDs
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :param relative_path: Relative Path, Select the file relative to the blend file
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
        :param frame_start: Start Frame, Start frame of the sequence strip
        :param channel: Channel, Channel to place this strip into
        :param replace_sel: Replace Selection, Deselect previously selected strips
        :param overlap: Allow Overlap, Dont correct overlap on new sequence strips
        :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
        :param cache: Cache, Cache the sound in memory
        :param mono: Mono, Merge all the sounds channels into one
    """

def split(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame: int | None = 0,
    channel: int | None = 0,
    type: typing.Literal["SOFT", "HARD"] | None = "SOFT",
    use_cursor_position: bool | None = False,
    side: typing.Literal["MOUSE", "LEFT", "RIGHT", "BOTH", "NO_CHANGE"]
    | None = "MOUSE",
    ignore_selection: bool | None = False,
) -> None:
    """Split the selected strips in two

    :param frame: Frame, Frame where selected strips will be split
    :param channel: Channel, Channel in which strip will be cut
    :param type: Type, The type of split operation to perform on strips
    :param use_cursor_position: Use Cursor Position, Split at position of the cursor instead of current frame
    :param side: Side, The side that remains selected after splitting
    :param ignore_selection: Ignore Selection, Make cut even if strip is not selected preserving selection state after cut
    """

def split_multicam(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    camera: int | None = 1,
) -> None:
    """Split multicam strip and select camera

    :param camera: Camera
    """

def strip_color_tag_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    color: bpy.stub_internal.rna_enums.StripColorItems | None = "NONE",
) -> None:
    """Set a color tag for the selected strips

    :param color: Color Tag
    """

def strip_jump(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    next: bool | None = True,
    center: bool | None = True,
) -> None:
    """Move frame to previous edit point

    :param next: Next Strip
    :param center: Use Strip Center
    """

def strip_modifier_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "",
) -> None:
    """Add a modifier to the strip

    :param type: Type
    """

def strip_modifier_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["REPLACE", "APPEND"] | None = "REPLACE",
) -> None:
    """Copy modifiers of the active strip to all selected strips

        :param type: Type

    REPLACE
    Replace -- Replace modifiers in destination.

    APPEND
    Append -- Append active modifiers to selected strips.
    """

def strip_modifier_equalizer_redefine(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    graphs: typing.Literal["SIMPLE", "DOUBLE", "TRIPLE"] | None = "SIMPLE",
    name: str = "Name",
) -> None:
    """Redefine equalizer graphs

        :param graphs: Graphs, Number of graphs

    SIMPLE
    Unique -- One unique graphical definition.

    DOUBLE
    Double -- Graphical definition in 2 sections.

    TRIPLE
    Triplet -- Graphical definition in 3 sections.
        :param name: Name, Name of modifier to redefine
    """

def strip_modifier_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "Name",
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move modifier up and down in the stack

        :param name: Name, Name of modifier to remove
        :param direction: Type

    UP
    Up -- Move modifier up in the stack.

    DOWN
    Down -- Move modifier down in the stack.
    """

def strip_modifier_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "Name",
) -> None:
    """Remove a modifier from the strip

    :param name: Name, Name of modifier to remove
    """

def strip_transform_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    property: typing.Literal["POSITION", "SCALE", "ROTATION", "ALL"] | None = "ALL",
) -> None:
    """Reset image transformation to default value

        :param property: Property, Strip transform property to be reset

    POSITION
    Position -- Reset strip transform location.

    SCALE
    Scale -- Reset strip transform scale.

    ROTATION
    Rotation -- Reset strip transform rotation.

    ALL
    All -- Reset strip transform location, scale and rotation.
    """

def strip_transform_fit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    fit_method: typing.Literal["FIT", "FILL", "STRETCH"] | None = "FIT",
) -> None:
    """Undocumented, consider contributing.

        :param fit_method: Fit Method, Scale fit fit_method

    FIT
    Scale to Fit -- Scale image so fits in preview.

    FILL
    Scale to Fill -- Scale image so it fills preview completely.

    STRETCH
    Stretch to Fill -- Stretch image so it fills preview.
    """

def swap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    side: typing.Literal["LEFT", "RIGHT"] | None = "RIGHT",
) -> None:
    """Swap active strip with strip to the right or left

    :param side: Side, Side of the strip to swap
    """

def swap_data(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Swap 2 sequencer strips"""

def swap_inputs(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Swap the two inputs of the effect strip"""

def text_cursor_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "LINE_BEGIN",
        "LINE_END",
        "TEXT_BEGIN",
        "TEXT_END",
        "PREVIOUS_CHARACTER",
        "NEXT_CHARACTER",
        "PREVIOUS_WORD",
        "NEXT_WORD",
        "PREVIOUS_LINE",
        "NEXT_LINE",
    ]
    | None = "LINE_BEGIN",
    select_text: bool | None = False,
) -> None:
    """Move cursor in text

    :param type: Type, Where to move cursor to, to make a selection
    :param select_text: Select Text, Select text while moving cursor
    """

def text_cursor_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select_text: bool | None = False,
) -> None:
    """Set cursor position in text

    :param select_text: Select Text, Select text while moving cursor
    """

def text_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["NEXT_OR_SELECTION", "PREVIOUS_OR_SELECTION"]
    | None = "NEXT_OR_SELECTION",
) -> None:
    """Delete text at cursor position

    :param type: Type, Which part of the text to delete
    """

def text_deselect_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Deselect all characters"""

def text_edit_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy text to clipboard"""

def text_edit_cut(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Cut text to clipboard"""

def text_edit_mode_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle text editing"""

def text_edit_paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Paste text to clipboard"""

def text_insert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    string: str = "",
) -> None:
    """Insert text at cursor position

    :param string: String, String to be inserted at cursor position
    """

def text_line_break(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Insert line break at cursor position"""

def text_select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all characters"""

def unlock(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Unlock strips so they can be transformed"""

def unmute(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Unmute (un)selected strips

    :param unselected: Unselected, Unmute unselected rather than selected strips
    """

def view_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """View all the strips in the sequencer"""

def view_all_preview(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Zoom preview to fit in the area"""

def view_frame(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move the view to the current frame"""

def view_ghost_border(
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
    """Set the boundaries of the border used for offset view

    :param xmin: X Min
    :param xmax: X Max
    :param ymin: Y Min
    :param ymax: Y Max
    :param wait_for_input: Wait for Input
    """

def view_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Zoom the sequencer on the selected strips"""

def view_zoom_ratio(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 1.0,
) -> None:
    """Change zoom ratio of sequencer preview

    :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out
    """
