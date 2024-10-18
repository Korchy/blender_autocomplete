import typing
import collections.abc
import typing_extensions
import bpy.ops.transform
import bpy.types
import bpy.typing
import mathutils

def change_effect_input(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    swap: typing.Literal["A_B", "B_C", "A_C"] | None = "A_B",
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param swap: Swap, The effect inputs to swap
    :type swap: typing.Literal['A_B','B_C','A_C'] | None
    """

def change_effect_type(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
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
):
    """Undocumented, consider contributing.

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
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
        :type type: typing.Literal['CROSS','ADD','SUBTRACT','ALPHA_OVER','ALPHA_UNDER','GAMMA_CROSS','MULTIPLY','OVER_DROP','WIPE','GLOW','TRANSFORM','COLOR','SPEED','MULTICAM','ADJUSTMENT','GAUSSIAN_BLUR','TEXT','COLORMIX'] | None
    """

def change_path(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
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
):
    """Undocumented, consider contributing.

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
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
        :type sort_method: str | None
        :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip
        :type use_placeholders: bool | None
    """

def change_scene(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    scene: str | None = "",
):
    """Change Scene assigned to Strip

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param scene: Scene
    :type scene: str | None
    """

def copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy the selected strips to the internal clipboard

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def crossfade_sounds(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Do cross-fading volume animation of two selected sound strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def cursor_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Set 2D cursor location

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Cursor location in normalized preview coordinates
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def deinterlace_selected_movies(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Deinterlace all selected movie sources

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    delete_data: bool | None = False,
):
    """Delete selected strips from the sequencer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param delete_data: Delete Data, After removing the Strip, delete the associated data also
    :type delete_data: bool | None
    """

def duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Duplicate the selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def duplicate_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    SEQUENCER_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None = None,
):
    """Duplicate selected strips and move them

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips
    :type SEQUENCER_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
    :type TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None
    """

def effect_strip_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
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
):
    """Add an effect to the sequencer, most are applied on top of existing strips

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
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
        :type type: typing.Literal['CROSS','ADD','SUBTRACT','ALPHA_OVER','ALPHA_UNDER','GAMMA_CROSS','MULTIPLY','OVER_DROP','WIPE','GLOW','TRANSFORM','COLOR','SPEED','MULTICAM','ADJUSTMENT','GAUSSIAN_BLUR','TEXT','COLORMIX'] | None
        :param frame_start: Start Frame, Start frame of the sequence strip
        :type frame_start: int | None
        :param frame_end: End Frame, End frame for the color strip
        :type frame_end: int | None
        :param channel: Channel, Channel to place this strip into
        :type channel: int | None
        :param replace_sel: Replace Selection, Replace the current selection
        :type replace_sel: bool | None
        :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
        :type overlap: bool | None
        :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
        :type overlap_shuffle_override: bool | None
        :param color: Color, Initialize the strip with this color
        :type color: collections.abc.Sequence[float] | mathutils.Color | None
    """

def enable_proxies(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    proxy_25: bool | None = False,
    proxy_50: bool | None = False,
    proxy_75: bool | None = False,
    proxy_100: bool | None = False,
    overwrite: bool | None = False,
):
    """Enable selected proxies on all selected Movie and Image strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param proxy_25: 25%
    :type proxy_25: bool | None
    :param proxy_50: 50%
    :type proxy_50: bool | None
    :param proxy_75: 75%
    :type proxy_75: bool | None
    :param proxy_100: 100%
    :type proxy_100: bool | None
    :param overwrite: Overwrite
    :type overwrite: bool | None
    """

def export_subtitles(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
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
):
    """Export .srt file containing text strips

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
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
        :type sort_method: str | None
    """

def fades_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    duration_seconds: float | None = 1.0,
    type: typing.Literal["IN_OUT", "IN", "OUT", "CURSOR_FROM", "CURSOR_TO"]
    | None = "IN_OUT",
):
    """Adds or updates a fade animation for either visual or audio strips

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param duration_seconds: Fade Duration, Duration of the fade in seconds
        :type duration_seconds: float | None
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
        :type type: typing.Literal['IN_OUT','IN','OUT','CURSOR_FROM','CURSOR_TO'] | None
    """

def fades_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Removes fade animation from selected sequences

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def gap_insert(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    frames: int | None = 10,
):
    """Insert gap at current frame to first strips at the right, independent of selection or locked state of strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param frames: Frames, Frames to insert after current strip
    :type frames: int | None
    """

def gap_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    all: bool | None = False,
):
    """Remove gap at current frame to first strip at the right, independent of selection or locked state of strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All Gaps, Do all gaps to right of current frame
    :type all: bool | None
    """

def image_strip_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
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
):
    """Add an image or image sequence to the sequencer

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param directory: Directory, Directory of the file
        :type directory: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
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
        :param frame_start: Start Frame, Start frame of the sequence strip
        :type frame_start: int | None
        :param frame_end: End Frame, End frame for the color strip
        :type frame_end: int | None
        :param channel: Channel, Channel to place this strip into
        :type channel: int | None
        :param replace_sel: Replace Selection, Replace the current selection
        :type replace_sel: bool | None
        :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
        :type overlap: bool | None
        :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
        :type overlap_shuffle_override: bool | None
        :param fit_method: Fit Method, Scale fit method

    FIT
    Scale to Fit -- Scale image to fit within the canvas.

    FILL
    Scale to Fill -- Scale image to completely fill the canvas.

    STRETCH
    Stretch to Fill -- Stretch image to fill the canvas.

    ORIGINAL
    Use Original Size -- Keep image at its original size.
        :type fit_method: typing.Literal['FIT','FILL','STRETCH','ORIGINAL'] | None
        :param set_view_transform: Set View Transform, Set appropriate view transform based on media color space
        :type set_view_transform: bool | None
        :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip
        :type use_placeholders: bool | None
    """

def images_separate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    length: int | None = 1,
):
    """On image sequence strips, it returns a strip for each image

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param length: Length, Length of each frame
    :type length: int | None
    """

def lock(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Lock strips so they can't be transformed

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def mask_strip_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    mask: str | None = "",
):
    """Add a mask strip to the sequencer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int | None
    :param channel: Channel, Channel to place this strip into
    :type channel: int | None
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool | None
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool | None
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: bool | None
    :param mask: Mask
    :type mask: str | None
    """

def meta_make(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Group selected strips into a meta-strip

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def meta_separate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Put the contents of a meta-strip back in the sequencer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def meta_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle a meta-strip (to edit enclosed strips)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def movie_strip_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
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
):
    """Add a movie strip to the sequencer

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param directory: Directory, Directory of the file
        :type directory: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
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
        :param frame_start: Start Frame, Start frame of the sequence strip
        :type frame_start: int | None
        :param channel: Channel, Channel to place this strip into
        :type channel: int | None
        :param replace_sel: Replace Selection, Replace the current selection
        :type replace_sel: bool | None
        :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
        :type overlap: bool | None
        :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
        :type overlap_shuffle_override: bool | None
        :param fit_method: Fit Method, Scale fit method

    FIT
    Scale to Fit -- Scale image to fit within the canvas.

    FILL
    Scale to Fill -- Scale image to completely fill the canvas.

    STRETCH
    Stretch to Fill -- Stretch image to fill the canvas.

    ORIGINAL
    Use Original Size -- Keep image at its original size.
        :type fit_method: typing.Literal['FIT','FILL','STRETCH','ORIGINAL'] | None
        :param set_view_transform: Set View Transform, Set appropriate view transform based on media color space
        :type set_view_transform: bool | None
        :param adjust_playback_rate: Adjust Playback Rate, Play at normal speed regardless of scene FPS
        :type adjust_playback_rate: bool | None
        :param sound: Sound, Load sound with the movie
        :type sound: bool | None
        :param use_framerate: Use Movie Framerate, Use framerate from the movie to keep sound and video in sync
        :type use_framerate: bool | None
    """

def movieclip_strip_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    clip: str | None = "",
):
    """Add a movieclip strip to the sequencer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int | None
    :param channel: Channel, Channel to place this strip into
    :type channel: int | None
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool | None
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool | None
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: bool | None
    :param clip: Clip
    :type clip: str | None
    """

def mute(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselected: bool | None = False,
):
    """Mute (un)selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Mute unselected rather than selected strips
    :type unselected: bool | None
    """

def offset_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Clear strip offsets from the start and end frames

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def paste(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    keep_offset: bool | None = False,
):
    """Paste strips from the internal clipboard

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param keep_offset: Keep Offset, Keep strip offset relative to the current frame when pasting
    :type keep_offset: bool | None
    """

def reassign_inputs(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reassign the inputs for the effect strip

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def rebuild_proxy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Rebuild all selected proxies and timecode indices using the job system

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def refresh_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Refresh the sequencer editor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def reload(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    adjust_length: bool | None = False,
):
    """Reload strips in the sequencer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param adjust_length: Adjust Length, Adjust length of strips to their data length
    :type adjust_length: bool | None
    """

def rename_channel(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def rendersize(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Set render size and aspect from active sequence

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def retiming_add_freeze_frame_slide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    SEQUENCER_OT_retiming_freeze_frame_add: retiming_freeze_frame_add | None = None,
    TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None = None,
):
    """Add freeze frame and move it

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param SEQUENCER_OT_retiming_freeze_frame_add: Add Freeze Frame, Add freeze frame
    :type SEQUENCER_OT_retiming_freeze_frame_add: retiming_freeze_frame_add | None
    :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
    :type TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None
    """

def retiming_add_transition_slide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    SEQUENCER_OT_retiming_transition_add: retiming_transition_add | None = None,
    TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None = None,
):
    """Add smooth transition between 2 retimed segments and change its duration

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param SEQUENCER_OT_retiming_transition_add: Add Speed Transition, Add smooth transition between 2 retimed segments
    :type SEQUENCER_OT_retiming_transition_add: retiming_transition_add | None
    :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
    :type TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None
    """

def retiming_freeze_frame_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    duration: int | None = 0,
):
    """Add freeze frame

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param duration: Duration, Duration of freeze frame segment
    :type duration: int | None
    """

def retiming_key_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    timeline_frame: int | None = 0,
):
    """Add retiming Key

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param timeline_frame: Timeline Frame, Frame where key will be added
    :type timeline_frame: int | None
    """

def retiming_key_delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete selected strips from the sequencer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def retiming_reset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset strip retiming

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def retiming_segment_speed_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    speed: float | None = 100.0,
    keep_retiming: bool | None = True,
):
    """Set speed of retimed segment

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param speed: Speed, New speed of retimed segment
    :type speed: float | None
    :param keep_retiming: Preserve Current Retiming, Keep speed of other segments unchanged, change strip length instead
    :type keep_retiming: bool | None
    """

def retiming_show(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Show retiming keys in selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def retiming_transition_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    duration: int | None = 0,
):
    """Add smooth transition between 2 retimed segments

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param duration: Duration, Duration of freeze frame segment
    :type duration: int | None
    """

def sample(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    size: int | None = 1,
):
    """Use mouse to sample color in current frame

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param size: Sample Size
    :type size: int | None
    """

def scene_frame_range_update(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Update frame range of scene strip

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def scene_strip_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    scene: str | None = "",
):
    """Add a strip to the sequencer using a Blender scene as a source

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int | None
    :param channel: Channel, Channel to place this strip into
    :type channel: int | None
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool | None
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool | None
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: bool | None
    :param scene: Scene
    :type scene: str | None
    """

def scene_strip_add_new(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    type: typing.Literal["NEW", "EMPTY", "LINK_COPY", "FULL_COPY"] | None = "NEW",
):
    """Create a new Strip and assign a new Scene as source

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param frame_start: Start Frame, Start frame of the sequence strip
        :type frame_start: int | None
        :param channel: Channel, Channel to place this strip into
        :type channel: int | None
        :param replace_sel: Replace Selection, Replace the current selection
        :type replace_sel: bool | None
        :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
        :type overlap: bool | None
        :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
        :type overlap_shuffle_override: bool | None
        :param type: Type

    NEW
    New -- Add new Strip with a new empty Scene with default settings.

    EMPTY
    Copy Settings -- Add a new Strip, with an empty scene, and copy settings from the current scene.

    LINK_COPY
    Linked Copy -- Add a Strip and link in the collections from the current scene (shallow copy).

    FULL_COPY
    Full Copy -- Add a Strip and make a full copy of the current scene.
        :type type: typing.Literal['NEW','EMPTY','LINK_COPY','FULL_COPY'] | None
    """

def select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
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
):
    """Select a strip (last selected becomes the "active strip")

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param wait_to_deselect_others: Wait to Deselect Others
    :type wait_to_deselect_others: bool | None
    :param mouse_x: Mouse X
    :type mouse_x: int | None
    :param mouse_y: Mouse Y
    :type mouse_y: int | None
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
    :param linked_handle: Linked Handle, Select handles next to the active strip
    :type linked_handle: bool | None
    :param linked_time: Linked Time, Select other strips at the same time
    :type linked_time: bool | None
    :param side_of_frame: Side of Frame, Select all strips on same side of the current frame as the mouse cursor
    :type side_of_frame: bool | None
    """

def select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Select or deselect all strips

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
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
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
    tweak: bool | None = False,
    include_handles: bool | None = False,
):
    """Select strips using box selection

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
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
        :param tweak: Tweak, Operator has been activated using a click-drag event
        :type tweak: bool | None
        :param include_handles: Select Handles, Select the strips and their handles
        :type include_handles: bool | None
    """

def select_grouped(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: typing.Literal[
        "TYPE", "TYPE_BASIC", "TYPE_EFFECT", "DATA", "EFFECT", "EFFECT_LINK", "OVERLAP"
    ]
    | None = "TYPE",
    extend: bool | None = False,
    use_active_channel: bool | None = False,
):
    """Select all strips grouped by various properties

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
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
        :type type: typing.Literal['TYPE','TYPE_BASIC','TYPE_EFFECT','DATA','EFFECT','EFFECT_LINK','OVERLAP'] | None
        :param extend: Extend, Extend selection instead of deselecting everything first
        :type extend: bool | None
        :param use_active_channel: Same Channel, Only consider strips on the same channel as the active one
        :type use_active_channel: bool | None
    """

def select_handle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    wait_to_deselect_others: bool | None = False,
    mouse_x: int | None = 0,
    mouse_y: int | None = 0,
):
    """Select strip handle

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param wait_to_deselect_others: Wait to Deselect Others
    :type wait_to_deselect_others: bool | None
    :param mouse_x: Mouse X
    :type mouse_x: int | None
    :param mouse_y: Mouse Y
    :type mouse_y: int | None
    """

def select_handles(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    side: typing.Literal[
        "LEFT", "RIGHT", "BOTH", "LEFT_NEIGHBOR", "RIGHT_NEIGHBOR", "BOTH_NEIGHBORS"
    ]
    | None = "BOTH",
):
    """Select gizmo handles on the sides of the selected strip

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param side: Side, The side of the handle that is selected
    :type side: typing.Literal['LEFT','RIGHT','BOTH','LEFT_NEIGHBOR','RIGHT_NEIGHBOR','BOTH_NEIGHBORS'] | None
    """

def select_less(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Shrink the current selection of adjacent selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select all strips adjacent to the current selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked_pick(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | None = False,
):
    """Select a chain of linked strips nearest to the mouse pointer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def select_more(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select more strips adjacent to the current selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_side(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    side: typing.Literal["MOUSE", "LEFT", "RIGHT", "BOTH", "NO_CHANGE"] | None = "BOTH",
):
    """Select strips on the nominated side of the selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param side: Side, The side to which the selection is applied
    :type side: typing.Literal['MOUSE','LEFT','RIGHT','BOTH','NO_CHANGE'] | None
    """

def select_side_of_frame(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | None = False,
    side: typing.Literal["LEFT", "RIGHT", "CURRENT"] | None = "LEFT",
):
    """Select strips relative to the current frame

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param extend: Extend, Extend the selection
        :type extend: bool | None
        :param side: Side

    LEFT
    Left -- Select to the left of the current frame.

    RIGHT
    Right -- Select to the right of the current frame.

    CURRENT
    Current Frame -- Select intersecting with the current frame.
        :type side: typing.Literal['LEFT','RIGHT','CURRENT'] | None
    """

def set_range_to_strips(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    preview: bool | None = False,
):
    """Set the frame range to the selected strips start and end

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param preview: Preview, Set the preview range instead
    :type preview: bool | None
    """

def slip(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    offset: int | None = 0,
):
    """Slip the contents of selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Offset, Offset to the data of the strip
    :type offset: int | None
    """

def snap(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    frame: int | None = 0,
):
    """Frame where selected strips will be snapped

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame: Frame, Frame where selected strips will be snapped
    :type frame: int | None
    """

def sound_strip_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
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
    ]
    | None = "",
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    cache: bool | None = False,
    mono: bool | None = False,
):
    """Add a sound strip to the sequencer

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param directory: Directory, Directory of the file
        :type directory: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
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
        :param frame_start: Start Frame, Start frame of the sequence strip
        :type frame_start: int | None
        :param channel: Channel, Channel to place this strip into
        :type channel: int | None
        :param replace_sel: Replace Selection, Replace the current selection
        :type replace_sel: bool | None
        :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
        :type overlap: bool | None
        :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
        :type overlap_shuffle_override: bool | None
        :param cache: Cache, Cache the sound in memory
        :type cache: bool | None
        :param mono: Mono, Merge all the sound's channels into one
        :type mono: bool | None
    """

def split(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    frame: int | None = 0,
    channel: int | None = 0,
    type: typing.Literal["SOFT", "HARD"] | None = "SOFT",
    use_cursor_position: bool | None = False,
    side: typing.Literal["MOUSE", "LEFT", "RIGHT", "BOTH", "NO_CHANGE"]
    | None = "MOUSE",
    ignore_selection: bool | None = False,
):
    """Split the selected strips in two

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame: Frame, Frame where selected strips will be split
    :type frame: int | None
    :param channel: Channel, Channel in which strip will be cut
    :type channel: int | None
    :param type: Type, The type of split operation to perform on strips
    :type type: typing.Literal['SOFT','HARD'] | None
    :param use_cursor_position: Use Cursor Position, Split at position of the cursor instead of current frame
    :type use_cursor_position: bool | None
    :param side: Side, The side that remains selected after splitting
    :type side: typing.Literal['MOUSE','LEFT','RIGHT','BOTH','NO_CHANGE'] | None
    :param ignore_selection: Ignore Selection, Make cut even if strip is not selected preserving selection state after cut
    :type ignore_selection: bool | None
    """

def split_multicam(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    camera: int | None = 1,
):
    """Split multicam strip and select camera

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param camera: Camera
    :type camera: int | None
    """

def strip_color_tag_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    color: bpy.typing.StripColorItems | None = "NONE",
):
    """Set a color tag for the selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param color: Color Tag
    :type color: bpy.typing.StripColorItems | None
    """

def strip_jump(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    next: bool | None = True,
    center: bool | None = True,
):
    """Move frame to previous edit point

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param next: Next Strip
    :type next: bool | None
    :param center: Use Strip Center
    :type center: bool | None
    """

def strip_modifier_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "",
):
    """Add a modifier to the strip

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

def strip_modifier_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: typing.Literal["REPLACE", "APPEND"] | None = "REPLACE",
):
    """Copy modifiers of the active strip to all selected strips

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    REPLACE
    Replace -- Replace modifiers in destination.

    APPEND
    Append -- Append active modifiers to selected strips.
        :type type: typing.Literal['REPLACE','APPEND'] | None
    """

def strip_modifier_equalizer_redefine(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    graphs: typing.Literal["SIMPLE", "DOUBLE", "TRIPLE"] | None = "SIMPLE",
    name: str = "Name",
):
    """Redefine equalizer graphs

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param graphs: Graphs, Number of graphs

    SIMPLE
    Unique -- One unique graphical definition.

    DOUBLE
    Double -- Graphical definition in 2 sections.

    TRIPLE
    Triplet -- Graphical definition in 3 sections.
        :type graphs: typing.Literal['SIMPLE','DOUBLE','TRIPLE'] | None
        :param name: Name, Name of modifier to redefine
        :type name: str
    """

def strip_modifier_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str = "Name",
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move modifier up and down in the stack

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param name: Name, Name of modifier to remove
        :type name: str
        :param direction: Type

    UP
    Up -- Move modifier up in the stack.

    DOWN
    Down -- Move modifier down in the stack.
        :type direction: typing.Literal['UP','DOWN'] | None
    """

def strip_modifier_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str = "Name",
):
    """Remove a modifier from the strip

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of modifier to remove
    :type name: str
    """

def strip_transform_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    property: typing.Literal["POSITION", "SCALE", "ROTATION", "ALL"] | None = "ALL",
):
    """Reset image transformation to default value

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param property: Property, Strip transform property to be reset

    POSITION
    Position -- Reset strip transform location.

    SCALE
    Scale -- Reset strip transform scale.

    ROTATION
    Rotation -- Reset strip transform rotation.

    ALL
    All -- Reset strip transform location, scale and rotation.
        :type property: typing.Literal['POSITION','SCALE','ROTATION','ALL'] | None
    """

def strip_transform_fit(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    fit_method: typing.Literal["FIT", "FILL", "STRETCH"] | None = "FIT",
):
    """Undocumented, consider contributing.

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param fit_method: Fit Method, Scale fit fit_method

    FIT
    Scale to Fit -- Scale image so fits in preview.

    FILL
    Scale to Fill -- Scale image so it fills preview completely.

    STRETCH
    Stretch to Fill -- Stretch image so it fills preview.
        :type fit_method: typing.Literal['FIT','FILL','STRETCH'] | None
    """

def swap(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    side: typing.Literal["LEFT", "RIGHT"] | None = "RIGHT",
):
    """Swap active strip with strip to the right or left

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param side: Side, Side of the strip to swap
    :type side: typing.Literal['LEFT','RIGHT'] | None
    """

def swap_data(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Swap 2 sequencer strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def swap_inputs(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Swap the first two inputs for the effect strip

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def unlock(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Unlock strips so they can be transformed

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def unmute(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselected: bool | None = False,
):
    """Unmute (un)selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Unmute unselected rather than selected strips
    :type unselected: bool | None
    """

def view_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """View all the strips in the sequencer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_all_preview(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Zoom preview to fit in the area

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_frame(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Move the view to the current frame

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_ghost_border(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
):
    """Set the boundaries of the border used for offset view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
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

def view_selected(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Zoom the sequencer on the selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_zoom_ratio(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    ratio: float | None = 1.0,
):
    """Change zoom ratio of sequencer preview

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out
    :type ratio: float | None
    """
