import sys
import typing
import bpy.types
import bpy.ops.transform

GenericType = typing.TypeVar("GenericType")


def change_effect_input(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        swap: typing.Optional[typing.Any] = 'A_B'):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param swap: Swap, The effect inputs to swap
    :type swap: typing.Optional[typing.Any]
    '''

    pass


def change_effect_type(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'CROSS'):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type, Sequencer effect type * ``CROSS`` Crossfade -- Crossfade effect strip type. * ``ADD`` Add -- Add effect strip type. * ``SUBTRACT`` Subtract -- Subtract effect strip type. * ``ALPHA_OVER`` Alpha Over -- Alpha Over effect strip type. * ``ALPHA_UNDER`` Alpha Under -- Alpha Under effect strip type. * ``GAMMA_CROSS`` Gamma Cross -- Gamma Cross effect strip type. * ``MULTIPLY`` Multiply -- Multiply effect strip type. * ``OVER_DROP`` Alpha Over Drop -- Alpha Over Drop effect strip type. * ``WIPE`` Wipe -- Wipe effect strip type. * ``GLOW`` Glow -- Glow effect strip type. * ``TRANSFORM`` Transform -- Transform effect strip type. * ``COLOR`` Color -- Color effect strip type. * ``SPEED`` Speed -- Color effect strip type. * ``MULTICAM`` Multicam Selector. * ``ADJUSTMENT`` Adjustment Layer. * ``GAUSSIAN_BLUR`` Gaussian Blur. * ``TEXT`` Text. * ``COLORMIX`` Color Mix.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def change_path(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        directory: typing.Union[str, typing.Any] = "",
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
        hide_props_region: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        check_existing: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_blender: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_sound: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_collada: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_alembic: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 9,
        relative_path: typing.Optional[typing.Union[bool, typing.Any]] = True,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        use_placeholders: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param files: Files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: typing.Optional[typing.Union[bool, typing.Any]]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_image: Filter image files
    :type filter_image: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_python: Filter Python files
    :type filter_python: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_font: Filter font files
    :type filter_font: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_text: Filter text files
    :type filter_text: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_archive: Filter archive files
    :type filter_archive: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_usd: Filter USD files
    :type filter_usd: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_obj: Filter OBJ files
    :type filter_obj: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Optional[typing.Union[bool, typing.Any]]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: typing.Optional[typing.Union[bool, typing.Any]]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Optional[typing.Union[str, int, typing.Any]]
    :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip
    :type use_placeholders: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def change_scene(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        scene: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Change Scene assigned to Strip

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param scene: Scene
    :type scene: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def copy(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None):
    ''' Copy the selected strips to the internal clipboard

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def crossfade_sounds(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Do cross-fading volume animation of two selected sound strips :File: `startup/bl_operators/sequencer.py\:28 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/sequencer.py#L28>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def cursor_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        location: typing.Optional[typing.Any] = (0.0, 0.0)):
    ''' Set 2D cursor location

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param location: Location, Cursor location in normalized preview coordinates
    :type location: typing.Optional[typing.Any]
    '''

    pass


def deinterlace_selected_movies(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Deinterlace all selected movie sources :File: `startup/bl_operators/sequencer.py\:116 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/sequencer.py#L116>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def delete(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        delete_data: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Delete selected strips from the sequencer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param delete_data: Delete Data, After removing the Strip, delete the associated data also
    :type delete_data: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def duplicate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Duplicate the selected strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def duplicate_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        SEQUENCER_OT_duplicate: typing.Optional['duplicate'] = None,
        TRANSFORM_OT_seq_slide: typing.
        Optional['bpy.ops.transform.seq_slide'] = None):
    ''' Duplicate selected strips and move them

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips
    :type SEQUENCER_OT_duplicate: typing.Optional['duplicate']
    :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
    :type TRANSFORM_OT_seq_slide: typing.Optional['bpy.ops.transform.seq_slide']
    '''

    pass


def effect_strip_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'CROSS',
        frame_start: typing.Optional[typing.Any] = 0,
        frame_end: typing.Optional[typing.Any] = 0,
        channel: typing.Optional[typing.Any] = 1,
        replace_sel: typing.Optional[typing.Union[bool, typing.Any]] = True,
        overlap: typing.Optional[typing.Union[bool, typing.Any]] = False,
        overlap_shuffle_override: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = False,
        color: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add an effect to the sequencer, most are applied on top of existing strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type, Sequencer effect type * ``CROSS`` Crossfade -- Crossfade effect strip type. * ``ADD`` Add -- Add effect strip type. * ``SUBTRACT`` Subtract -- Subtract effect strip type. * ``ALPHA_OVER`` Alpha Over -- Alpha Over effect strip type. * ``ALPHA_UNDER`` Alpha Under -- Alpha Under effect strip type. * ``GAMMA_CROSS`` Gamma Cross -- Gamma Cross effect strip type. * ``MULTIPLY`` Multiply -- Multiply effect strip type. * ``OVER_DROP`` Alpha Over Drop -- Alpha Over Drop effect strip type. * ``WIPE`` Wipe -- Wipe effect strip type. * ``GLOW`` Glow -- Glow effect strip type. * ``TRANSFORM`` Transform -- Transform effect strip type. * ``COLOR`` Color -- Color effect strip type. * ``SPEED`` Speed -- Color effect strip type. * ``MULTICAM`` Multicam Selector. * ``ADJUSTMENT`` Adjustment Layer. * ``GAUSSIAN_BLUR`` Gaussian Blur. * ``TEXT`` Text. * ``COLORMIX`` Color Mix.
    :type type: typing.Optional[typing.Any]
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: typing.Optional[typing.Any]
    :param frame_end: End Frame, End frame for the color strip
    :type frame_end: typing.Optional[typing.Any]
    :param channel: Channel, Channel to place this strip into
    :type channel: typing.Optional[typing.Any]
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: typing.Optional[typing.Union[bool, typing.Any]]
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: typing.Optional[typing.Union[bool, typing.Any]]
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: typing.Optional[typing.Union[bool, typing.Any]]
    :param color: Color, Initialize the strip with this color
    :type color: typing.Optional[typing.Any]
    '''

    pass


def enable_proxies(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        proxy_25: typing.Optional[typing.Union[bool, typing.Any]] = False,
        proxy_50: typing.Optional[typing.Union[bool, typing.Any]] = False,
        proxy_75: typing.Optional[typing.Union[bool, typing.Any]] = False,
        proxy_100: typing.Optional[typing.Union[bool, typing.Any]] = False,
        overwrite: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Enable selected proxies on all selected Movie and Image strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param proxy_25: 25%
    :type proxy_25: typing.Optional[typing.Union[bool, typing.Any]]
    :param proxy_50: 50%
    :type proxy_50: typing.Optional[typing.Union[bool, typing.Any]]
    :param proxy_75: 75%
    :type proxy_75: typing.Optional[typing.Union[bool, typing.Any]]
    :param proxy_100: 100%
    :type proxy_100: typing.Optional[typing.Union[bool, typing.Any]]
    :param overwrite: Overwrite
    :type overwrite: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def export_subtitles(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        hide_props_region: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        check_existing: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blender: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_sound: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_collada: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_alembic: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Export .srt file containing text strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: typing.Optional[typing.Union[bool, typing.Any]]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_image: Filter image files
    :type filter_image: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_python: Filter Python files
    :type filter_python: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_font: Filter font files
    :type filter_font: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_text: Filter text files
    :type filter_text: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_archive: Filter archive files
    :type filter_archive: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_usd: Filter USD files
    :type filter_usd: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_obj: Filter OBJ files
    :type filter_obj: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Optional[typing.Union[bool, typing.Any]]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def fades_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        duration_seconds: typing.Optional[typing.Any] = 1.0,
        type: typing.Optional[typing.Any] = 'IN_OUT'):
    ''' Adds or updates a fade animation for either visual or audio strips :File: `startup/bl_operators/sequencer.py\:194 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/sequencer.py#L194>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param duration_seconds: Fade Duration, Duration of the fade in seconds
    :type duration_seconds: typing.Optional[typing.Any]
    :param type: Fade Type, Fade in, out, both in and out, to, or from the current frame. Default is both in and out * ``IN_OUT`` Fade In and Out -- Fade selected strips in and out. * ``IN`` Fade In -- Fade in selected strips. * ``OUT`` Fade Out -- Fade out selected strips. * ``CURSOR_FROM`` From Current Frame -- Fade from the time cursor to the end of overlapping sequences. * ``CURSOR_TO`` To Current Frame -- Fade from the start of sequences under the time cursor to the current frame.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def fades_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Removes fade animation from selected sequences :File: `startup/bl_operators/sequencer.py\:135 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/sequencer.py#L135>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def gap_insert(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        frames: typing.Optional[typing.Any] = 10):
    ''' Insert gap at current frame to first strips at the right, independent of selection or locked state of strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param frames: Frames, Frames to insert after current strip
    :type frames: typing.Optional[typing.Any]
    '''

    pass


def gap_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        all: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Remove gap at current frame to first strip at the right, independent of selection or locked state of strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param all: All Gaps, Do all gaps to right of current frame
    :type all: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def image_strip_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        directory: typing.Union[str, typing.Any] = "",
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
        check_existing: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_blender: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_sound: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_collada: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_alembic: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 9,
        relative_path: typing.Optional[typing.Union[bool, typing.Any]] = True,
        show_multiview: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        use_multiview: typing.Optional[typing.Union[bool, typing.Any]] = False,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        frame_start: typing.Optional[typing.Any] = 0,
        frame_end: typing.Optional[typing.Any] = 0,
        channel: typing.Optional[typing.Any] = 1,
        replace_sel: typing.Optional[typing.Union[bool, typing.Any]] = True,
        overlap: typing.Optional[typing.Union[bool, typing.Any]] = False,
        overlap_shuffle_override: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = False,
        fit_method: typing.Optional[typing.Any] = 'FIT',
        set_view_transform: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = True,
        use_placeholders: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False):
    ''' Add an image or image sequence to the sequencer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param files: Files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_image: Filter image files
    :type filter_image: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_python: Filter Python files
    :type filter_python: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_font: Filter font files
    :type filter_font: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_text: Filter text files
    :type filter_text: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_archive: Filter archive files
    :type filter_archive: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_usd: Filter USD files
    :type filter_usd: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_obj: Filter OBJ files
    :type filter_obj: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Optional[typing.Union[bool, typing.Any]]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: typing.Optional[typing.Union[bool, typing.Any]]
    :param show_multiview: Enable Multi-View
    :type show_multiview: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_multiview: Use Multi-View
    :type use_multiview: typing.Optional[typing.Union[bool, typing.Any]]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Optional[typing.Union[str, int, typing.Any]]
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: typing.Optional[typing.Any]
    :param frame_end: End Frame, End frame for the color strip
    :type frame_end: typing.Optional[typing.Any]
    :param channel: Channel, Channel to place this strip into
    :type channel: typing.Optional[typing.Any]
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: typing.Optional[typing.Union[bool, typing.Any]]
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: typing.Optional[typing.Union[bool, typing.Any]]
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: typing.Optional[typing.Union[bool, typing.Any]]
    :param fit_method: Fit Method, Scale fit method * ``FIT`` Scale to Fit -- Scale image to fit within the canvas. * ``FILL`` Scale to Fill -- Scale image to completely fill the canvas. * ``STRETCH`` Stretch to Fill -- Stretch image to fill the canvas. * ``ORIGINAL`` Use Original Size -- Keep image at its original size.
    :type fit_method: typing.Optional[typing.Any]
    :param set_view_transform: Set View Transform, Set appropriate view transform based on media color space
    :type set_view_transform: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip
    :type use_placeholders: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def images_separate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        length: typing.Optional[typing.Any] = 1):
    ''' On image sequence strips, it returns a strip for each image

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param length: Length, Length of each frame
    :type length: typing.Optional[typing.Any]
    '''

    pass


def lock(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None):
    ''' Lock strips so they can't be transformed

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def mask_strip_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        frame_start: typing.Optional[typing.Any] = 0,
        channel: typing.Optional[typing.Any] = 1,
        replace_sel: typing.Optional[typing.Union[bool, typing.Any]] = True,
        overlap: typing.Optional[typing.Union[bool, typing.Any]] = False,
        overlap_shuffle_override: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = False,
        mask: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Add a mask strip to the sequencer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: typing.Optional[typing.Any]
    :param channel: Channel, Channel to place this strip into
    :type channel: typing.Optional[typing.Any]
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: typing.Optional[typing.Union[bool, typing.Any]]
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: typing.Optional[typing.Union[bool, typing.Any]]
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: typing.Optional[typing.Union[bool, typing.Any]]
    :param mask: Mask
    :type mask: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def meta_make(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Group selected strips into a meta-strip

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def meta_separate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Put the contents of a meta-strip back in the sequencer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def meta_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Toggle a meta-strip (to edit enclosed strips)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def movie_strip_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        directory: typing.Union[str, typing.Any] = "",
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
        check_existing: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_blender: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_sound: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_collada: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_alembic: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 9,
        relative_path: typing.Optional[typing.Union[bool, typing.Any]] = True,
        show_multiview: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        use_multiview: typing.Optional[typing.Union[bool, typing.Any]] = False,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        frame_start: typing.Optional[typing.Any] = 0,
        channel: typing.Optional[typing.Any] = 1,
        replace_sel: typing.Optional[typing.Union[bool, typing.Any]] = True,
        overlap: typing.Optional[typing.Union[bool, typing.Any]] = False,
        overlap_shuffle_override: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = False,
        fit_method: typing.Optional[typing.Any] = 'FIT',
        set_view_transform: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = True,
        adjust_playback_rate: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = True,
        sound: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_framerate: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Add a movie strip to the sequencer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param files: Files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_image: Filter image files
    :type filter_image: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_python: Filter Python files
    :type filter_python: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_font: Filter font files
    :type filter_font: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_text: Filter text files
    :type filter_text: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_archive: Filter archive files
    :type filter_archive: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_usd: Filter USD files
    :type filter_usd: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_obj: Filter OBJ files
    :type filter_obj: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Optional[typing.Union[bool, typing.Any]]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: typing.Optional[typing.Union[bool, typing.Any]]
    :param show_multiview: Enable Multi-View
    :type show_multiview: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_multiview: Use Multi-View
    :type use_multiview: typing.Optional[typing.Union[bool, typing.Any]]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Optional[typing.Union[str, int, typing.Any]]
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: typing.Optional[typing.Any]
    :param channel: Channel, Channel to place this strip into
    :type channel: typing.Optional[typing.Any]
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: typing.Optional[typing.Union[bool, typing.Any]]
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: typing.Optional[typing.Union[bool, typing.Any]]
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: typing.Optional[typing.Union[bool, typing.Any]]
    :param fit_method: Fit Method, Scale fit method * ``FIT`` Scale to Fit -- Scale image to fit within the canvas. * ``FILL`` Scale to Fill -- Scale image to completely fill the canvas. * ``STRETCH`` Stretch to Fill -- Stretch image to fill the canvas. * ``ORIGINAL`` Use Original Size -- Keep image at its original size.
    :type fit_method: typing.Optional[typing.Any]
    :param set_view_transform: Set View Transform, Set appropriate view transform based on media color space
    :type set_view_transform: typing.Optional[typing.Union[bool, typing.Any]]
    :param adjust_playback_rate: Adjust Playback Rate, Play at normal speed regardless of scene FPS
    :type adjust_playback_rate: typing.Optional[typing.Union[bool, typing.Any]]
    :param sound: Sound, Load sound with the movie
    :type sound: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_framerate: Use Movie Framerate, Use framerate from the movie to keep sound and video in sync
    :type use_framerate: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def movieclip_strip_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        frame_start: typing.Optional[typing.Any] = 0,
        channel: typing.Optional[typing.Any] = 1,
        replace_sel: typing.Optional[typing.Union[bool, typing.Any]] = True,
        overlap: typing.Optional[typing.Union[bool, typing.Any]] = False,
        overlap_shuffle_override: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = False,
        clip: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Add a movieclip strip to the sequencer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: typing.Optional[typing.Any]
    :param channel: Channel, Channel to place this strip into
    :type channel: typing.Optional[typing.Any]
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: typing.Optional[typing.Union[bool, typing.Any]]
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: typing.Optional[typing.Union[bool, typing.Any]]
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: typing.Optional[typing.Union[bool, typing.Any]]
    :param clip: Clip
    :type clip: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def mute(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         unselected: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Mute (un)selected strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected, Mute unselected rather than selected strips
    :type unselected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def offset_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Clear strip offsets from the start and end frames

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def paste(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        keep_offset: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Paste strips from the internal clipboard

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param keep_offset: Keep Offset, Keep strip offset relative to the current frame when pasting
    :type keep_offset: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def reassign_inputs(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Reassign the inputs for the effect strip

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def rebuild_proxy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Rebuild all selected proxies and timecode indices using the job system

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def refresh_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Refresh the sequencer editor

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def reload(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None,
           *,
           adjust_length: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False):
    ''' Reload strips in the sequencer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param adjust_length: Adjust Length, Adjust length of strips to their data length
    :type adjust_length: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def rename_channel(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def rendersize(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Set render size and aspect from active sequence

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def retiming_freeze_frame_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        duration: typing.Optional[typing.Any] = 0):
    ''' Add freeze frame

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param duration: Duration, Duration of freeze frame segment
    :type duration: typing.Optional[typing.Any]
    '''

    pass


def retiming_key_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        timeline_frame: typing.Optional[typing.Any] = 0):
    ''' Add retiming Key

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param timeline_frame: Timeline Frame, Frame where key will be added
    :type timeline_frame: typing.Optional[typing.Any]
    '''

    pass


def retiming_reset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Reset strip retiming

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def retiming_segment_speed_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        speed: typing.Optional[typing.Any] = 100.0):
    ''' Set speed of retimed segment

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param speed: Speed, New speed of retimed segment
    :type speed: typing.Optional[typing.Any]
    '''

    pass


def retiming_show(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Show retiming keys in selected strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def retiming_transition_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        duration: typing.Optional[typing.Any] = 0):
    ''' Add smooth transition between 2 retimed segments

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param duration: Duration, Duration of freeze frame segment
    :type duration: typing.Optional[typing.Any]
    '''

    pass


def sample(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None,
           *,
           size: typing.Optional[typing.Any] = 1):
    ''' Use mouse to sample color in current frame

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param size: Sample Size
    :type size: typing.Optional[typing.Any]
    '''

    pass


def scene_frame_range_update(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Update frame range of scene strip

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def scene_strip_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        frame_start: typing.Optional[typing.Any] = 0,
        channel: typing.Optional[typing.Any] = 1,
        replace_sel: typing.Optional[typing.Union[bool, typing.Any]] = True,
        overlap: typing.Optional[typing.Union[bool, typing.Any]] = False,
        overlap_shuffle_override: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = False,
        scene: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Add a strip to the sequencer using a Blender scene as a source

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: typing.Optional[typing.Any]
    :param channel: Channel, Channel to place this strip into
    :type channel: typing.Optional[typing.Any]
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: typing.Optional[typing.Union[bool, typing.Any]]
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: typing.Optional[typing.Union[bool, typing.Any]]
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: typing.Optional[typing.Union[bool, typing.Any]]
    :param scene: Scene
    :type scene: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def scene_strip_add_new(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        frame_start: typing.Optional[typing.Any] = 0,
        channel: typing.Optional[typing.Any] = 1,
        replace_sel: typing.Optional[typing.Union[bool, typing.Any]] = True,
        overlap: typing.Optional[typing.Union[bool, typing.Any]] = False,
        overlap_shuffle_override: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = False,
        type: typing.Optional[typing.Any] = 'NEW'):
    ''' Create a new Strip and assign a new Scene as source

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: typing.Optional[typing.Any]
    :param channel: Channel, Channel to place this strip into
    :type channel: typing.Optional[typing.Any]
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: typing.Optional[typing.Union[bool, typing.Any]]
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: typing.Optional[typing.Union[bool, typing.Any]]
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: typing.Optional[typing.Union[bool, typing.Any]]
    :param type: Type * ``NEW`` New -- Add new Strip with a new empty Scene with default settings. * ``EMPTY`` Copy Settings -- Add a new Strip, with an empty scene, and copy settings from the current scene. * ``LINK_COPY`` Linked Copy -- Add a Strip and link in the collections from the current scene (shallow copy). * ``FULL_COPY`` Full Copy -- Add a Strip and make a full copy of the current scene.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        wait_to_deselect_others: typing.Optional[typing.Union[bool, typing.
                                                              Any]] = False,
        mouse_x: typing.Optional[typing.Any] = 0,
        mouse_y: typing.Optional[typing.Any] = 0,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False,
        deselect: typing.Optional[typing.Union[bool, typing.Any]] = False,
        toggle: typing.Optional[typing.Union[bool, typing.Any]] = False,
        deselect_all: typing.Optional[typing.Union[bool, typing.Any]] = False,
        select_passthrough: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = False,
        center: typing.Optional[typing.Union[bool, typing.Any]] = False,
        linked_handle: typing.Optional[typing.Union[bool, typing.Any]] = False,
        linked_time: typing.Optional[typing.Union[bool, typing.Any]] = False,
        side_of_frame: typing.Optional[typing.Union[bool, typing.
                                                    Any]] = False):
    ''' Select a strip (last selected becomes the "active strip")

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param wait_to_deselect_others: Wait to Deselect Others
    :type wait_to_deselect_others: typing.Optional[typing.Union[bool, typing.Any]]
    :param mouse_x: Mouse X
    :type mouse_x: typing.Optional[typing.Any]
    :param mouse_y: Mouse Y
    :type mouse_y: typing.Optional[typing.Any]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    :param deselect: Deselect, Remove from selection
    :type deselect: typing.Optional[typing.Union[bool, typing.Any]]
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: typing.Optional[typing.Union[bool, typing.Any]]
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: typing.Optional[typing.Union[bool, typing.Any]]
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :type select_passthrough: typing.Optional[typing.Union[bool, typing.Any]]
    :param center: Center, Use the object center when selecting, in edit mode used to extend object selection
    :type center: typing.Optional[typing.Union[bool, typing.Any]]
    :param linked_handle: Linked Handle, Select handles next to the active strip
    :type linked_handle: typing.Optional[typing.Union[bool, typing.Any]]
    :param linked_time: Linked Time, Select other strips at the same time
    :type linked_time: typing.Optional[typing.Union[bool, typing.Any]]
    :param side_of_frame: Side of Frame, Select all strips on same side of the current frame as the mouse cursor
    :type side_of_frame: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Select or deselect all strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param action: Action, Selection action to execute * ``TOGGLE`` Toggle -- Toggle selection for all elements. * ``SELECT`` Select -- Select all elements. * ``DESELECT`` Deselect -- Deselect all elements. * ``INVERT`` Invert -- Invert selection of all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_box(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        xmin: typing.Optional[typing.Any] = 0,
        xmax: typing.Optional[typing.Any] = 0,
        ymin: typing.Optional[typing.Any] = 0,
        ymax: typing.Optional[typing.Any] = 0,
        wait_for_input: typing.Optional[typing.Union[bool, typing.Any]] = True,
        mode: typing.Optional[typing.Any] = 'SET',
        tweak: typing.Optional[typing.Union[bool, typing.Any]] = False,
        include_handles: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False):
    ''' Select strips using box selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param xmin: X Min
    :type xmin: typing.Optional[typing.Any]
    :param xmax: X Max
    :type xmax: typing.Optional[typing.Any]
    :param ymin: Y Min
    :type ymin: typing.Optional[typing.Any]
    :param ymax: Y Max
    :type ymax: typing.Optional[typing.Any]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    :param mode: Mode * ``SET`` Set -- Set a new selection. * ``ADD`` Extend -- Extend existing selection. * ``SUB`` Subtract -- Subtract existing selection.
    :type mode: typing.Optional[typing.Any]
    :param tweak: Tweak, Operator has been activated using a click-drag event
    :type tweak: typing.Optional[typing.Union[bool, typing.Any]]
    :param include_handles: Select Handles, Select the strips and their handles
    :type include_handles: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_grouped(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'TYPE',
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_active_channel: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = False):
    ''' Select all strips grouped by various properties

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type * ``TYPE`` Type -- Shared strip type. * ``TYPE_BASIC`` Global Type -- All strips of same basic type (graphical or sound). * ``TYPE_EFFECT`` Effect Type -- Shared strip effect type (if active strip is not an effect one, select all non-effect strips). * ``DATA`` Data -- Shared data (scene, image, sound, etc.). * ``EFFECT`` Effect -- Shared effects. * ``EFFECT_LINK`` Effect/Linked -- Other strips affected by the active one (sharing some time, and below or effect-assigned). * ``OVERLAP`` Overlap -- Overlapping time.
    :type type: typing.Optional[typing.Any]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_active_channel: Same Channel, Only consider strips on the same channel as the active one
    :type use_active_channel: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_handles(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        side: typing.Optional[typing.Any] = 'BOTH'):
    ''' Select gizmo handles on the sides of the selected strip

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param side: Side, The side of the handle that is selected
    :type side: typing.Optional[typing.Any]
    '''

    pass


def select_less(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Shrink the current selection of adjacent selected strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_linked(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select all strips adjacent to the current selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_linked_pick(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select a chain of linked strips nearest to the mouse pointer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend the selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_more(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select more strips adjacent to the current selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_side(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        side: typing.Optional[typing.Any] = 'BOTH'):
    ''' Select strips on the nominated side of the selected strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param side: Side, The side to which the selection is applied
    :type side: typing.Optional[typing.Any]
    '''

    pass


def select_side_of_frame(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False,
        side: typing.Optional[typing.Any] = 'LEFT'):
    ''' Select strips relative to the current frame

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend the selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    :param side: Side * ``LEFT`` Left -- Select to the left of the current frame. * ``RIGHT`` Right -- Select to the right of the current frame. * ``CURRENT`` Current Frame -- Select intersecting with the current frame.
    :type side: typing.Optional[typing.Any]
    '''

    pass


def set_range_to_strips(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        preview: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Set the frame range to the selected strips start and end

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param preview: Preview, Set the preview range instead
    :type preview: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def slip(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         offset: typing.Optional[typing.Any] = 0):
    ''' Slip the contents of selected strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param offset: Offset, Offset to the data of the strip
    :type offset: typing.Optional[typing.Any]
    '''

    pass


def snap(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         frame: typing.Optional[typing.Any] = 0):
    ''' Frame where selected strips will be snapped

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param frame: Frame, Frame where selected strips will be snapped
    :type frame: typing.Optional[typing.Any]
    '''

    pass


def sound_strip_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        directory: typing.Union[str, typing.Any] = "",
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
        check_existing: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_blender: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_sound: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_collada: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_alembic: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 9,
        relative_path: typing.Optional[typing.Union[bool, typing.Any]] = True,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        frame_start: typing.Optional[typing.Any] = 0,
        channel: typing.Optional[typing.Any] = 1,
        replace_sel: typing.Optional[typing.Union[bool, typing.Any]] = True,
        overlap: typing.Optional[typing.Union[bool, typing.Any]] = False,
        overlap_shuffle_override: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = False,
        cache: typing.Optional[typing.Union[bool, typing.Any]] = False,
        mono: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Add a sound strip to the sequencer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param files: Files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_image: Filter image files
    :type filter_image: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_python: Filter Python files
    :type filter_python: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_font: Filter font files
    :type filter_font: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_text: Filter text files
    :type filter_text: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_archive: Filter archive files
    :type filter_archive: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_usd: Filter USD files
    :type filter_usd: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_obj: Filter OBJ files
    :type filter_obj: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Optional[typing.Union[bool, typing.Any]]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: typing.Optional[typing.Union[bool, typing.Any]]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Optional[typing.Union[str, int, typing.Any]]
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: typing.Optional[typing.Any]
    :param channel: Channel, Channel to place this strip into
    :type channel: typing.Optional[typing.Any]
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: typing.Optional[typing.Union[bool, typing.Any]]
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: typing.Optional[typing.Union[bool, typing.Any]]
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: typing.Optional[typing.Union[bool, typing.Any]]
    :param cache: Cache, Cache the sound in memory
    :type cache: typing.Optional[typing.Union[bool, typing.Any]]
    :param mono: Mono, Merge all the sound's channels into one
    :type mono: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def split(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None,
          *,
          frame: typing.Optional[typing.Any] = 0,
          channel: typing.Optional[typing.Any] = 0,
          type: typing.Optional[typing.Any] = 'SOFT',
          use_cursor_position: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
          side: typing.Optional[typing.Any] = 'MOUSE',
          ignore_selection: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = False):
    ''' Split the selected strips in two

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param frame: Frame, Frame where selected strips will be split
    :type frame: typing.Optional[typing.Any]
    :param channel: Channel, Channel in which strip will be cut
    :type channel: typing.Optional[typing.Any]
    :param type: Type, The type of split operation to perform on strips
    :type type: typing.Optional[typing.Any]
    :param use_cursor_position: Use Cursor Position, Split at position of the cursor instead of current frame
    :type use_cursor_position: typing.Optional[typing.Union[bool, typing.Any]]
    :param side: Side, The side that remains selected after splitting
    :type side: typing.Optional[typing.Any]
    :param ignore_selection: Ignore Selection, Make cut even if strip is not selected preserving selection state after cut
    :type ignore_selection: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def split_multicam(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        camera: typing.Optional[typing.Any] = 1):
    ''' Split multicam strip and select camera :File: `startup/bl_operators/sequencer.py\:83 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/sequencer.py#L83>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param camera: Camera
    :type camera: typing.Optional[typing.Any]
    '''

    pass


def strip_color_tag_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        color: typing.Optional[typing.Union[str, int]] = 'NONE'):
    ''' Set a color tag for the selected strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param color: Color Tag
    :type color: typing.Optional[typing.Union[str, int]]
    '''

    pass


def strip_jump(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        next: typing.Optional[typing.Union[bool, typing.Any]] = True,
        center: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Move frame to previous edit point

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param next: Next Strip
    :type next: typing.Optional[typing.Union[bool, typing.Any]]
    :param center: Use Strip Center
    :type center: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def strip_modifier_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Add a modifier to the strip

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def strip_modifier_copy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'REPLACE'):
    ''' Copy modifiers of the active strip to all selected strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type * ``REPLACE`` Replace -- Replace modifiers in destination. * ``APPEND`` Append -- Append active modifiers to selected strips.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def strip_modifier_equalizer_redefine(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        graphs: typing.Optional[typing.Any] = 'SIMPLE',
        name: typing.Union[str, typing.Any] = "Name"):
    ''' Redefine equalizer graphs

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param graphs: Graphs, Number of graphs * ``SIMPLE`` Unique -- One unique graphical definition. * ``DOUBLE`` Double -- Graphical definition in 2 sections. * ``TRIPLE`` Triplet -- Graphical definition in 3 sections.
    :type graphs: typing.Optional[typing.Any]
    :param name: Name, Name of modifier to redefine
    :type name: typing.Union[str, typing.Any]
    '''

    pass


def strip_modifier_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "Name",
        direction: typing.Optional[typing.Any] = 'UP'):
    ''' Move modifier up and down in the stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of modifier to remove
    :type name: typing.Union[str, typing.Any]
    :param direction: Type * ``UP`` Up -- Move modifier up in the stack. * ``DOWN`` Down -- Move modifier down in the stack.
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def strip_modifier_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "Name"):
    ''' Remove a modifier from the strip

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of modifier to remove
    :type name: typing.Union[str, typing.Any]
    '''

    pass


def strip_transform_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        property: typing.Optional[typing.Any] = 'ALL'):
    ''' Reset image transformation to default value

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param property: Property, Strip transform property to be reset * ``POSITION`` Position -- Reset strip transform location. * ``SCALE`` Scale -- Reset strip transform scale. * ``ROTATION`` Rotation -- Reset strip transform rotation. * ``ALL`` All -- Reset strip transform location, scale and rotation.
    :type property: typing.Optional[typing.Any]
    '''

    pass


def strip_transform_fit(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        fit_method: typing.Optional[typing.Any] = 'FIT'):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param fit_method: Fit Method, Scale fit fit_method * ``FIT`` Scale to Fit -- Scale image so fits in preview. * ``FILL`` Scale to Fill -- Scale image so it fills preview completely. * ``STRETCH`` Stretch to Fill -- Stretch image so it fills preview.
    :type fit_method: typing.Optional[typing.Any]
    '''

    pass


def swap(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         side: typing.Optional[typing.Any] = 'RIGHT'):
    ''' Swap active strip with strip to the right or left

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param side: Side, Side of the strip to swap
    :type side: typing.Optional[typing.Any]
    '''

    pass


def swap_data(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Swap 2 sequencer strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def swap_inputs(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Swap the first two inputs for the effect strip

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def unlock(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None):
    ''' Unlock strips so they can be transformed

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def unmute(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        unselected: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Unmute (un)selected strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected, Unmute unselected rather than selected strips
    :type unselected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def view_all(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None):
    ''' View all the strips in the sequencer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def view_all_preview(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Zoom preview to fit in the area

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def view_frame(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Move the view to the current frame

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def view_ghost_border(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        xmin: typing.Optional[typing.Any] = 0,
        xmax: typing.Optional[typing.Any] = 0,
        ymin: typing.Optional[typing.Any] = 0,
        ymax: typing.Optional[typing.Any] = 0,
        wait_for_input: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = True):
    ''' Set the boundaries of the border used for offset view

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param xmin: X Min
    :type xmin: typing.Optional[typing.Any]
    :param xmax: X Max
    :type xmax: typing.Optional[typing.Any]
    :param ymin: Y Min
    :type ymin: typing.Optional[typing.Any]
    :param ymax: Y Max
    :type ymax: typing.Optional[typing.Any]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def view_selected(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Zoom the sequencer on the selected strips

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def view_zoom_ratio(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        ratio: typing.Optional[typing.Any] = 1.0):
    ''' Change zoom ratio of sequencer preview

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param ratio: 1, higher is zoomed in, lower is zoomed out
    :type ratio: typing.Optional[typing.Any]
    '''

    pass
