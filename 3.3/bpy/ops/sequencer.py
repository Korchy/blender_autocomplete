import sys
import typing
import bpy.types
import mathutils
import bpy.ops.transform

GenericType = typing.TypeVar("GenericType")


def change_effect_input(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        swap: typing.Union[str, int] = 'A_B'):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param swap: Swap, The effect inputs to swap
    :type swap: typing.Union[str, int]
    '''

    pass


def change_effect_type(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       type: typing.Union[str, int] = 'CROSS'):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Sequencer effect type * CROSS Crossfade -- Crossfade effect strip type. * ADD Add -- Add effect strip type. * SUBTRACT Subtract -- Subtract effect strip type. * ALPHA_OVER Alpha Over -- Alpha Over effect strip type. * ALPHA_UNDER Alpha Under -- Alpha Under effect strip type. * GAMMA_CROSS Gamma Cross -- Gamma Cross effect strip type. * MULTIPLY Multiply -- Multiply effect strip type. * OVER_DROP Alpha Over Drop -- Alpha Over Drop effect strip type. * WIPE Wipe -- Wipe effect strip type. * GLOW Glow -- Glow effect strip type. * TRANSFORM Transform -- Transform effect strip type. * COLOR Color -- Color effect strip type. * SPEED Speed -- Color effect strip type. * MULTICAM Multicam Selector. * ADJUSTMENT Adjustment Layer. * GAUSSIAN_BLUR Gaussian Blur. * TEXT Text. * COLORMIX Color Mix.
    :type type: typing.Union[str, int]
    '''

    pass


def change_path(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        filepath: str = "",
        directory: str = "",
        files: bpy.types.
        bpy_prop_collection['bpy.types.OperatorFileListElement'] = None,
        hide_props_region: bool = True,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = False,
        filter_movie: bool = False,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = False,
        filter_text: bool = False,
        filter_archive: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_usd: bool = False,
        filter_obj: bool = False,
        filter_volume: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 9,
        relative_path: bool = True,
        display_type: typing.Union[str, int] = 'DEFAULT',
        sort_method: typing.Union[str, int] = '',
        use_placeholders: bool = False):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param files: Files
    :type files: bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int]
    :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip
    :type use_placeholders: bool
    '''

    pass


def change_scene(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 scene: typing.Union[str, int] = ''):
    ''' Change Scene assigned to Strip

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param scene: Scene
    :type scene: typing.Union[str, int]
    '''

    pass


def copy(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None):
    ''' Copy selected strips to clipboard

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def crossfade_sounds(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Do cross-fading volume animation of two selected sound strips :file: startup/bl_operators/sequencer.py\:25 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/sequencer.py$25> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def cursor_set(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        location: typing.Union[typing.List[float], typing.
                               Tuple[float, float], 'mathutils.Vector'] = (
                                   0.0, 0.0)):
    ''' Set 2D cursor location

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param location: Location, Cursor location in normalized preview coordinates
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float], 'mathutils.Vector']
    '''

    pass


def deinterlace_selected_movies(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Deinterlace all selected movie sources :file: startup/bl_operators/sequencer.py\:113 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/sequencer.py$113> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           delete_data: bool = False):
    ''' Erase selected strips from the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param delete_data: Delete Data, After removing the Strip, delete the associated data also
    :type delete_data: bool
    '''

    pass


def duplicate(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Duplicate the selected strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def duplicate_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        SEQUENCER_OT_duplicate: 'duplicate' = None,
        TRANSFORM_OT_seq_slide: 'bpy.ops.transform.seq_slide' = None):
    ''' Duplicate selected strips and move them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips
    :type SEQUENCER_OT_duplicate: 'duplicate'
    :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
    :type TRANSFORM_OT_seq_slide: 'bpy.ops.transform.seq_slide'
    '''

    pass


def effect_strip_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        type: typing.Union[str, int] = 'CROSS',
        frame_start: int = 0,
        frame_end: int = 0,
        channel: int = 1,
        replace_sel: bool = True,
        overlap: bool = False,
        overlap_shuffle_override: bool = False,
        color: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add an effect to the sequencer, most are applied on top of existing strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Sequencer effect type * CROSS Crossfade -- Crossfade effect strip type. * ADD Add -- Add effect strip type. * SUBTRACT Subtract -- Subtract effect strip type. * ALPHA_OVER Alpha Over -- Alpha Over effect strip type. * ALPHA_UNDER Alpha Under -- Alpha Under effect strip type. * GAMMA_CROSS Gamma Cross -- Gamma Cross effect strip type. * MULTIPLY Multiply -- Multiply effect strip type. * OVER_DROP Alpha Over Drop -- Alpha Over Drop effect strip type. * WIPE Wipe -- Wipe effect strip type. * GLOW Glow -- Glow effect strip type. * TRANSFORM Transform -- Transform effect strip type. * COLOR Color -- Color effect strip type. * SPEED Speed -- Color effect strip type. * MULTICAM Multicam Selector. * ADJUSTMENT Adjustment Layer. * GAUSSIAN_BLUR Gaussian Blur. * TEXT Text. * COLORMIX Color Mix.
    :type type: typing.Union[str, int]
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int
    :param frame_end: End Frame, End frame for the color strip
    :type frame_end: int
    :param channel: Channel, Channel to place this strip into
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: bool
    :param color: Color, Initialize the strip with this color
    :type color: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def enable_proxies(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   proxy_25: bool = False,
                   proxy_50: bool = False,
                   proxy_75: bool = False,
                   proxy_100: bool = False,
                   overwrite: bool = False):
    ''' Enable selected proxies on all selected Movie and Image strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param proxy_25: 25%
    :type proxy_25: bool
    :param proxy_50: 50%
    :type proxy_50: bool
    :param proxy_75: 75%
    :type proxy_75: bool
    :param proxy_100: 100%
    :type proxy_100: bool
    :param overwrite: Overwrite
    :type overwrite: bool
    '''

    pass


def export_subtitles(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     filepath: str = "",
                     hide_props_region: bool = True,
                     check_existing: bool = True,
                     filter_blender: bool = False,
                     filter_backup: bool = False,
                     filter_image: bool = False,
                     filter_movie: bool = False,
                     filter_python: bool = False,
                     filter_font: bool = False,
                     filter_sound: bool = False,
                     filter_text: bool = False,
                     filter_archive: bool = False,
                     filter_btx: bool = False,
                     filter_collada: bool = False,
                     filter_alembic: bool = False,
                     filter_usd: bool = False,
                     filter_obj: bool = False,
                     filter_volume: bool = False,
                     filter_folder: bool = True,
                     filter_blenlib: bool = False,
                     filemode: int = 8,
                     display_type: typing.Union[str, int] = 'DEFAULT',
                     sort_method: typing.Union[str, int] = ''):
    ''' Export .srt file containing text strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Path to file
    :type filepath: str
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: bool
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int]
    '''

    pass


def fades_add(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              duration_seconds: float = 1.0,
              type: typing.Union[str, int] = 'IN_OUT'):
    ''' Adds or updates a fade animation for either visual or audio strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param duration_seconds: Fade Duration, Duration of the fade in seconds
    :type duration_seconds: float
    :param type: Fade Type, Fade in, out, both in and out, to, or from the current frame. Default is both in and out * IN_OUT Fade In and Out -- Fade selected strips in and out. * IN Fade In -- Fade in selected strips. * OUT Fade Out -- Fade out selected strips. * CURSOR_FROM From Current Frame -- Fade from the time cursor to the end of overlapping sequences. * CURSOR_TO To Current Frame -- Fade from the start of sequences under the time cursor to the current frame.
    :type type: typing.Union[str, int]
    '''

    pass


def fades_clear(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Removes fade animation from selected sequences :file: startup/bl_operators/sequencer.py\:132 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/sequencer.py$132> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def gap_insert(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               frames: int = 10):
    ''' Insert gap at current frame to first strips at the right, independent of selection or locked state of strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frames: Frames, Frames to insert after current strip
    :type frames: int
    '''

    pass


def gap_remove(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               all: bool = False):
    ''' Remove gap at current frame to first strip at the right, independent of selection or locked state of strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param all: All Gaps, Do all gaps to right of current frame
    :type all: bool
    '''

    pass


def image_strip_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        directory: str = "",
        files: bpy.types.
        bpy_prop_collection['bpy.types.OperatorFileListElement'] = None,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = True,
        filter_movie: bool = False,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = False,
        filter_text: bool = False,
        filter_archive: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_usd: bool = False,
        filter_obj: bool = False,
        filter_volume: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 9,
        relative_path: bool = True,
        show_multiview: bool = False,
        use_multiview: bool = False,
        display_type: typing.Union[str, int] = 'DEFAULT',
        sort_method: typing.Union[str, int] = '',
        frame_start: int = 0,
        frame_end: int = 0,
        channel: int = 1,
        replace_sel: bool = True,
        overlap: bool = False,
        overlap_shuffle_override: bool = False,
        fit_method: typing.Union[str, int] = 'FIT',
        set_view_transform: bool = True,
        use_placeholders: bool = False):
    ''' Add an image or image sequence to the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param directory: Directory, Directory of the file
    :type directory: str
    :param files: Files
    :type files: bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param show_multiview: Enable Multi-View
    :type show_multiview: bool
    :param use_multiview: Use Multi-View
    :type use_multiview: bool
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int]
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int
    :param frame_end: End Frame, End frame for the color strip
    :type frame_end: int
    :param channel: Channel, Channel to place this strip into
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: bool
    :param fit_method: Fit Method, Scale fit method * FIT Scale to Fit -- Scale image to fit within the canvas. * FILL Scale to Fill -- Scale image to completely fill the canvas. * STRETCH Stretch to Fill -- Stretch image to fill the canvas. * ORIGINAL Use Original Size -- Keep image at its original size.
    :type fit_method: typing.Union[str, int]
    :param set_view_transform: Set View Transform, Set appropriate view transform based on media color space
    :type set_view_transform: bool
    :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip
    :type use_placeholders: bool
    '''

    pass


def images_separate(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    length: int = 1):
    ''' On image sequence strips, it returns a strip for each image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param length: Length, Length of each frame
    :type length: int
    '''

    pass


def lock(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None):
    ''' Lock strips so they can't be transformed

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def mask_strip_add(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   frame_start: int = 0,
                   channel: int = 1,
                   replace_sel: bool = True,
                   overlap: bool = False,
                   overlap_shuffle_override: bool = False,
                   mask: typing.Union[str, int] = ''):
    ''' Add a mask strip to the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: bool
    :param mask: Mask
    :type mask: typing.Union[str, int]
    '''

    pass


def meta_make(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Group selected strips into a meta-strip

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def meta_separate(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Put the contents of a meta-strip back in the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def meta_toggle(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Toggle a meta-strip (to edit enclosed strips)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def movie_strip_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        filepath: str = "",
        directory: str = "",
        files: bpy.types.
        bpy_prop_collection['bpy.types.OperatorFileListElement'] = None,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = False,
        filter_movie: bool = True,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = False,
        filter_text: bool = False,
        filter_archive: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_usd: bool = False,
        filter_obj: bool = False,
        filter_volume: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 9,
        relative_path: bool = True,
        show_multiview: bool = False,
        use_multiview: bool = False,
        display_type: typing.Union[str, int] = 'DEFAULT',
        sort_method: typing.Union[str, int] = '',
        frame_start: int = 0,
        channel: int = 1,
        replace_sel: bool = True,
        overlap: bool = False,
        overlap_shuffle_override: bool = False,
        fit_method: typing.Union[str, int] = 'FIT',
        set_view_transform: bool = True,
        adjust_playback_rate: bool = True,
        sound: bool = True,
        use_framerate: bool = True):
    ''' Add a movie strip to the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param files: Files
    :type files: bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param show_multiview: Enable Multi-View
    :type show_multiview: bool
    :param use_multiview: Use Multi-View
    :type use_multiview: bool
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int]
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: bool
    :param fit_method: Fit Method, Scale fit method * FIT Scale to Fit -- Scale image to fit within the canvas. * FILL Scale to Fill -- Scale image to completely fill the canvas. * STRETCH Stretch to Fill -- Stretch image to fill the canvas. * ORIGINAL Use Original Size -- Keep image at its original size.
    :type fit_method: typing.Union[str, int]
    :param set_view_transform: Set View Transform, Set appropriate view transform based on media color space
    :type set_view_transform: bool
    :param adjust_playback_rate: Adjust Playback Rate, Play at normal speed regardless of scene FPS
    :type adjust_playback_rate: bool
    :param sound: Sound, Load sound with the movie
    :type sound: bool
    :param use_framerate: Use Movie Framerate, Use framerate from the movie to keep sound and video in sync
    :type use_framerate: bool
    '''

    pass


def movieclip_strip_add(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        frame_start: int = 0,
                        channel: int = 1,
                        replace_sel: bool = True,
                        overlap: bool = False,
                        overlap_shuffle_override: bool = False,
                        clip: typing.Union[str, int] = ''):
    ''' Add a movieclip strip to the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: bool
    :param clip: Clip
    :type clip: typing.Union[str, int]
    '''

    pass


def mute(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         unselected: bool = False):
    ''' Mute (un)selected strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param unselected: Unselected, Mute unselected rather than selected strips
    :type unselected: bool
    '''

    pass


def offset_clear(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Clear strip offsets from the start and end frames

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
          keep_offset: bool = False):
    ''' Paste strips from clipboard

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param keep_offset: Keep Offset, Keep strip offset relative to the current frame when pasting
    :type keep_offset: bool
    '''

    pass


def reassign_inputs(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Reassign the inputs for the effect strip

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def rebuild_proxy(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Rebuild all selected proxies and timecode indices using the job system

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def refresh_all(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Refresh the sequencer editor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def reload(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           adjust_length: bool = False):
    ''' Reload strips in the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param adjust_length: Adjust Length, Adjust length of strips to their data length
    :type adjust_length: bool
    '''

    pass


def rename_channel(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def rendersize(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Set render size and aspect from active sequence

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def sample(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           size: int = 1):
    ''' Use mouse to sample color in current frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param size: Sample Size
    :type size: int
    '''

    pass


def scene_strip_add(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    frame_start: int = 0,
                    channel: int = 1,
                    replace_sel: bool = True,
                    overlap: bool = False,
                    overlap_shuffle_override: bool = False,
                    scene: typing.Union[str, int] = ''):
    ''' Add a strip to the sequencer using a blender scene as a source

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: bool
    :param scene: Scene
    :type scene: typing.Union[str, int]
    '''

    pass


def scene_strip_add_new(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        frame_start: int = 0,
                        channel: int = 1,
                        replace_sel: bool = True,
                        overlap: bool = False,
                        overlap_shuffle_override: bool = False,
                        type: typing.Union[str, int] = 'NEW'):
    ''' Create a new Strip and add a assign a new Scene as source

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: bool
    :param type: Type * NEW New -- Add new Strip with a new empty Scene with default settings. * EMPTY Copy Settings -- Add a new Strip, with an empty scene, and copy settings from the current scene. * LINK_COPY Linked Copy -- Add a Strip and link in the collections from the current scene (shallow copy). * FULL_COPY Full Copy -- Add a Strip and make a full copy of the current scene.
    :type type: typing.Union[str, int]
    '''

    pass


def select(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           wait_to_deselect_others: bool = False,
           mouse_x: int = 0,
           mouse_y: int = 0,
           extend: bool = False,
           deselect: bool = False,
           toggle: bool = False,
           deselect_all: bool = False,
           select_passthrough: bool = False,
           center: bool = False,
           linked_handle: bool = False,
           linked_time: bool = False,
           side_of_frame: bool = False):
    ''' Select a strip (last selected becomes the "active strip")

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param wait_to_deselect_others: Wait to Deselect Others
    :type wait_to_deselect_others: bool
    :param mouse_x: Mouse X
    :type mouse_x: int
    :param mouse_y: Mouse Y
    :type mouse_y: int
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param deselect: Deselect, Remove from selection
    :type deselect: bool
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: bool
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :type select_passthrough: bool
    :param center: Center, Use the object center when selecting, in edit mode used to extend object selection
    :type center: bool
    :param linked_handle: Linked Handle, Select handles next to the active strip
    :type linked_handle: bool
    :param linked_time: Linked Time, Select other strips at the same time
    :type linked_time: bool
    :param side_of_frame: Side of Frame, Select all strips on same side of the current frame as the mouse cursor
    :type side_of_frame: bool
    '''

    pass


def select_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               action: typing.Union[str, int] = 'TOGGLE'):
    ''' Select or deselect all strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_box(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               xmin: int = 0,
               xmax: int = 0,
               ymin: int = 0,
               ymax: int = 0,
               wait_for_input: bool = True,
               mode: typing.Union[str, int] = 'SET',
               tweak: bool = False,
               include_handles: bool = False):
    ''' Select strips using box selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param xmin: X Min
    :type xmin: int
    :param xmax: X Max
    :type xmax: int
    :param ymin: Y Min
    :type ymin: int
    :param ymax: Y Max
    :type ymax: int
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection.
    :type mode: typing.Union[str, int]
    :param tweak: Tweak, Operator has been activated using a click-drag event
    :type tweak: bool
    :param include_handles: Select Handles, Select the strips and their handles
    :type include_handles: bool
    '''

    pass


def select_grouped(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   type: typing.Union[str, int] = 'TYPE',
                   extend: bool = False,
                   use_active_channel: bool = False):
    ''' Select all strips grouped by various properties

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type * TYPE Type -- Shared strip type. * TYPE_BASIC Global Type -- All strips of same basic type (graphical or sound). * TYPE_EFFECT Effect Type -- Shared strip effect type (if active strip is not an effect one, select all non-effect strips). * DATA Data -- Shared data (scene, image, sound, etc.). * EFFECT Effect -- Shared effects. * EFFECT_LINK Effect/Linked -- Other strips affected by the active one (sharing some time, and below or effect-assigned). * OVERLAP Overlap -- Overlapping time.
    :type type: typing.Union[str, int]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param use_active_channel: Same Channel, Only consider strips on the same channel as the active one
    :type use_active_channel: bool
    '''

    pass


def select_handles(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   side: typing.Union[str, int] = 'BOTH'):
    ''' Select gizmo handles on the sides of the selected strip

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param side: Side, The side of the handle that is selected
    :type side: typing.Union[str, int]
    '''

    pass


def select_less(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Shrink the current selection of adjacent selected strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_linked(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Select all strips adjacent to the current selection

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
    ''' Select a chain of linked strips nearest to the mouse pointer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend the selection
    :type extend: bool
    '''

    pass


def select_more(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Select more strips adjacent to the current selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_side(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                side: typing.Union[str, int] = 'BOTH'):
    ''' Select strips on the nominated side of the selected strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param side: Side, The side to which the selection is applied
    :type side: typing.Union[str, int]
    '''

    pass


def select_side_of_frame(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         extend: bool = False,
                         side: typing.Union[str, int] = 'LEFT'):
    ''' Select strips relative to the current frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend the selection
    :type extend: bool
    :param side: Side * LEFT Left -- Select to the left of the current frame. * RIGHT Right -- Select to the right of the current frame. * CURRENT Current Frame -- Select intersecting with the current frame.
    :type side: typing.Union[str, int]
    '''

    pass


def set_range_to_strips(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        preview: bool = False):
    ''' Set the frame range to the selected strips start and end

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param preview: Preview, Set the preview range instead
    :type preview: bool
    '''

    pass


def slip(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         offset: int = 0):
    ''' Slip the contents of selected strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param offset: Offset, Offset to the data of the strip
    :type offset: int
    '''

    pass


def snap(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         frame: int = 0):
    ''' Frame where selected strips will be snapped

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame: Frame, Frame where selected strips will be snapped
    :type frame: int
    '''

    pass


def sound_strip_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        filepath: str = "",
        directory: str = "",
        files: bpy.types.
        bpy_prop_collection['bpy.types.OperatorFileListElement'] = None,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = False,
        filter_movie: bool = False,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = True,
        filter_text: bool = False,
        filter_archive: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_usd: bool = False,
        filter_obj: bool = False,
        filter_volume: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 9,
        relative_path: bool = True,
        display_type: typing.Union[str, int] = 'DEFAULT',
        sort_method: typing.Union[str, int] = '',
        frame_start: int = 0,
        channel: int = 1,
        replace_sel: bool = True,
        overlap: bool = False,
        overlap_shuffle_override: bool = False,
        cache: bool = False,
        mono: bool = False):
    ''' Add a sound strip to the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param files: Files
    :type files: bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int]
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: bool
    :param cache: Cache, Cache the sound in memory
    :type cache: bool
    :param mono: Mono, Merge all the sound's channels into one
    :type mono: bool
    '''

    pass


def split(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None,
          *,
          frame: int = 0,
          channel: int = 0,
          type: typing.Union[str, int] = 'SOFT',
          use_cursor_position: bool = False,
          side: typing.Union[str, int] = 'MOUSE',
          ignore_selection: bool = False):
    ''' Split the selected strips in two

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame: Frame, Frame where selected strips will be split
    :type frame: int
    :param channel: Channel, Channel in which strip will be cut
    :type channel: int
    :param type: Type, The type of split operation to perform on strips
    :type type: typing.Union[str, int]
    :param use_cursor_position: Use Cursor Position, Split at position of the cursor instead of current frame
    :type use_cursor_position: bool
    :param side: Side, The side that remains selected after splitting
    :type side: typing.Union[str, int]
    :param ignore_selection: Ignore Selection, Make cut event if strip is not selected preserving selection state after cut
    :type ignore_selection: bool
    '''

    pass


def split_multicam(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   camera: int = 1):
    ''' Split multicam strip and select camera

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param camera: Camera
    :type camera: int
    '''

    pass


def strip_color_tag_set(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        color: typing.Union[int, str] = 'NONE'):
    ''' Set a color tag for the selected strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param color: Color Tag
    :type color: typing.Union[int, str]
    '''

    pass


def strip_jump(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               next: bool = True,
               center: bool = True):
    ''' Move frame to previous edit point

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param next: Next Strip
    :type next: bool
    :param center: Use Strip Center
    :type center: bool
    '''

    pass


def strip_modifier_add(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       type: typing.Union[int, str] = 'COLOR_BALANCE'):
    ''' Add a modifier to the strip

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[int, str]
    '''

    pass


def strip_modifier_copy(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        type: typing.Union[str, int] = 'REPLACE'):
    ''' Copy modifiers of the active strip to all selected strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type * REPLACE Replace -- Replace modifiers in destination. * APPEND Append -- Append active modifiers to selected strips.
    :type type: typing.Union[str, int]
    '''

    pass


def strip_modifier_move(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        name: str = "Name",
                        direction: typing.Union[str, int] = 'UP'):
    ''' Move modifier up and down in the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of modifier to remove
    :type name: str
    :param direction: Type * UP Up -- Move modifier up in the stack. * DOWN Down -- Move modifier down in the stack.
    :type direction: typing.Union[str, int]
    '''

    pass


def strip_modifier_remove(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          name: str = "Name"):
    ''' Remove a modifier from the strip

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of modifier to remove
    :type name: str
    '''

    pass


def strip_transform_clear(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          property: typing.Union[str, int] = 'ALL'):
    ''' Reset image transformation to default value

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param property: Property, Strip transform property to be reset * POSITION Position -- Reset strip transform location. * SCALE Scale -- Reset strip transform scale. * ROTATION Rotation -- Reset strip transform rotation. * ALL All -- Reset strip transform location, scale and rotation.
    :type property: typing.Union[str, int]
    '''

    pass


def strip_transform_fit(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        fit_method: typing.Union[str, int] = 'FIT'):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param fit_method: Fit Method, Scale fit fit_method * FIT Scale to Fit -- Scale image so fits in preview. * FILL Scale to Fill -- Scale image so it fills preview completely. * STRETCH Stretch to Fill -- Stretch image so it fills preview.
    :type fit_method: typing.Union[str, int]
    '''

    pass


def swap(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         side: typing.Union[str, int] = 'RIGHT'):
    ''' Swap active strip with strip to the right or left

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param side: Side, Side of the strip to swap
    :type side: typing.Union[str, int]
    '''

    pass


def swap_data(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Swap 2 sequencer strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def swap_inputs(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Swap the first two inputs for the effect strip

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def unlock(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Unlock strips so they can be transformed

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def unmute(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           unselected: bool = False):
    ''' Unmute (un)selected strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param unselected: Unselected, Unmute unselected rather than selected strips
    :type unselected: bool
    '''

    pass


def view_all(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None):
    ''' View all the strips in the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_all_preview(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Zoom preview to fit in the area

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_frame(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Move the view to the current frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_ghost_border(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      xmin: int = 0,
                      xmax: int = 0,
                      ymin: int = 0,
                      ymax: int = 0,
                      wait_for_input: bool = True):
    ''' Set the boundaries of the border used for offset view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param xmin: X Min
    :type xmin: int
    :param xmax: X Max
    :type xmax: int
    :param ymin: Y Min
    :type ymin: int
    :param ymax: Y Max
    :type ymax: int
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def view_selected(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Zoom the sequencer on the selected strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_zoom_ratio(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    ratio: float = 1.0):
    ''' Change zoom ratio of sequencer preview

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out
    :type ratio: float
    '''

    pass
