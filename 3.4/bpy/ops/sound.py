import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def bake_animation(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None):
    ''' Update the audio animation cache

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def mixdown(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: typing.Optional[bool] = None,
            *,
            filepath: typing.Union[str, typing.Any] = "",
            check_existing: typing.Union[bool, typing.Any] = True,
            filter_blender: typing.Union[bool, typing.Any] = False,
            filter_backup: typing.Union[bool, typing.Any] = False,
            filter_image: typing.Union[bool, typing.Any] = False,
            filter_movie: typing.Union[bool, typing.Any] = False,
            filter_python: typing.Union[bool, typing.Any] = False,
            filter_font: typing.Union[bool, typing.Any] = False,
            filter_sound: typing.Union[bool, typing.Any] = True,
            filter_text: typing.Union[bool, typing.Any] = False,
            filter_archive: typing.Union[bool, typing.Any] = False,
            filter_btx: typing.Union[bool, typing.Any] = False,
            filter_collada: typing.Union[bool, typing.Any] = False,
            filter_alembic: typing.Union[bool, typing.Any] = False,
            filter_usd: typing.Union[bool, typing.Any] = False,
            filter_obj: typing.Union[bool, typing.Any] = False,
            filter_volume: typing.Union[bool, typing.Any] = False,
            filter_folder: typing.Union[bool, typing.Any] = True,
            filter_blenlib: typing.Union[bool, typing.Any] = False,
            filemode: typing.Optional[typing.Any] = 9,
            relative_path: typing.Union[bool, typing.Any] = True,
            display_type: typing.Optional[typing.Any] = 'DEFAULT',
            sort_method: typing.Union[str, int, typing.Any] = '',
            accuracy: typing.Optional[typing.Any] = 1024,
            container: typing.Optional[typing.Any] = 'FLAC',
            codec: typing.Optional[typing.Any] = 'FLAC',
            format: typing.Optional[typing.Any] = 'S16',
            bitrate: typing.Optional[typing.Any] = 192,
            split_channels: typing.Union[bool, typing.Any] = False):
    ''' Mix the scene's audio to a sound file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Union[bool, typing.Any]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Union[bool, typing.Any]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Union[bool, typing.Any]
    :param filter_image: Filter image files
    :type filter_image: typing.Union[bool, typing.Any]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Union[bool, typing.Any]
    :param filter_python: Filter python files
    :type filter_python: typing.Union[bool, typing.Any]
    :param filter_font: Filter font files
    :type filter_font: typing.Union[bool, typing.Any]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Union[bool, typing.Any]
    :param filter_text: Filter text files
    :type filter_text: typing.Union[bool, typing.Any]
    :param filter_archive: Filter archive files
    :type filter_archive: typing.Union[bool, typing.Any]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Union[bool, typing.Any]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Union[bool, typing.Any]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Union[bool, typing.Any]
    :param filter_usd: Filter USD files
    :type filter_usd: typing.Union[bool, typing.Any]
    :param filter_obj: Filter OBJ files
    :type filter_obj: typing.Union[bool, typing.Any]
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: typing.Union[bool, typing.Any]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Union[bool, typing.Any]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Union[bool, typing.Any]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: typing.Union[bool, typing.Any]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int, typing.Any]
    :param accuracy: Accuracy, Sample accuracy, important for animation data (the lower the value, the more accurate)
    :type accuracy: typing.Optional[typing.Any]
    :param container: Container, File format * ``AC3`` ac3 -- Dolby Digital ATRAC 3. * ``FLAC`` flac -- Free Lossless Audio Codec. * ``MATROSKA`` mkv -- Matroska. * ``MP2`` mp2 -- MPEG-1 Audio Layer II. * ``MP3`` mp3 -- MPEG-2 Audio Layer III. * ``OGG`` ogg -- Xiph.Org Ogg Container. * ``WAV`` wav -- Waveform Audio File Format.
    :type container: typing.Optional[typing.Any]
    :param codec: Codec, Audio Codec * ``AAC`` AAC -- Advanced Audio Coding. * ``AC3`` AC3 -- Dolby Digital ATRAC 3. * ``FLAC`` FLAC -- Free Lossless Audio Codec. * ``MP2`` MP2 -- MPEG-1 Audio Layer II. * ``MP3`` MP3 -- MPEG-2 Audio Layer III. * ``PCM`` PCM -- Pulse Code Modulation (RAW). * ``VORBIS`` Vorbis -- Xiph.Org Vorbis Codec.
    :type codec: typing.Optional[typing.Any]
    :param format: Format, Sample format * ``U8`` U8 -- 8-bit unsigned. * ``S16`` S16 -- 16-bit signed. * ``S24`` S24 -- 24-bit signed. * ``S32`` S32 -- 32-bit signed. * ``F32`` F32 -- 32-bit floating-point. * ``F64`` F64 -- 64-bit floating-point.
    :type format: typing.Optional[typing.Any]
    :param bitrate: Bitrate, Bitrate in kbit/s
    :type bitrate: typing.Optional[typing.Any]
    :param split_channels: Split channels, Each channel will be rendered into a mono file
    :type split_channels: typing.Union[bool, typing.Any]
    '''

    pass


def open(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         filepath: typing.Union[str, typing.Any] = "",
         hide_props_region: typing.Union[bool, typing.Any] = True,
         check_existing: typing.Union[bool, typing.Any] = False,
         filter_blender: typing.Union[bool, typing.Any] = False,
         filter_backup: typing.Union[bool, typing.Any] = False,
         filter_image: typing.Union[bool, typing.Any] = False,
         filter_movie: typing.Union[bool, typing.Any] = True,
         filter_python: typing.Union[bool, typing.Any] = False,
         filter_font: typing.Union[bool, typing.Any] = False,
         filter_sound: typing.Union[bool, typing.Any] = True,
         filter_text: typing.Union[bool, typing.Any] = False,
         filter_archive: typing.Union[bool, typing.Any] = False,
         filter_btx: typing.Union[bool, typing.Any] = False,
         filter_collada: typing.Union[bool, typing.Any] = False,
         filter_alembic: typing.Union[bool, typing.Any] = False,
         filter_usd: typing.Union[bool, typing.Any] = False,
         filter_obj: typing.Union[bool, typing.Any] = False,
         filter_volume: typing.Union[bool, typing.Any] = False,
         filter_folder: typing.Union[bool, typing.Any] = True,
         filter_blenlib: typing.Union[bool, typing.Any] = False,
         filemode: typing.Optional[typing.Any] = 9,
         relative_path: typing.Union[bool, typing.Any] = True,
         show_multiview: typing.Union[bool, typing.Any] = False,
         use_multiview: typing.Union[bool, typing.Any] = False,
         display_type: typing.Optional[typing.Any] = 'DEFAULT',
         sort_method: typing.Union[str, int, typing.Any] = '',
         cache: typing.Union[bool, typing.Any] = False,
         mono: typing.Union[bool, typing.Any] = False):
    ''' Load a sound file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: typing.Union[bool, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Union[bool, typing.Any]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Union[bool, typing.Any]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Union[bool, typing.Any]
    :param filter_image: Filter image files
    :type filter_image: typing.Union[bool, typing.Any]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Union[bool, typing.Any]
    :param filter_python: Filter python files
    :type filter_python: typing.Union[bool, typing.Any]
    :param filter_font: Filter font files
    :type filter_font: typing.Union[bool, typing.Any]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Union[bool, typing.Any]
    :param filter_text: Filter text files
    :type filter_text: typing.Union[bool, typing.Any]
    :param filter_archive: Filter archive files
    :type filter_archive: typing.Union[bool, typing.Any]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Union[bool, typing.Any]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Union[bool, typing.Any]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Union[bool, typing.Any]
    :param filter_usd: Filter USD files
    :type filter_usd: typing.Union[bool, typing.Any]
    :param filter_obj: Filter OBJ files
    :type filter_obj: typing.Union[bool, typing.Any]
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: typing.Union[bool, typing.Any]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Union[bool, typing.Any]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Union[bool, typing.Any]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: typing.Union[bool, typing.Any]
    :param show_multiview: Enable Multi-View
    :type show_multiview: typing.Union[bool, typing.Any]
    :param use_multiview: Use Multi-View
    :type use_multiview: typing.Union[bool, typing.Any]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int, typing.Any]
    :param cache: Cache, Cache the sound in memory
    :type cache: typing.Union[bool, typing.Any]
    :param mono: Mono, Merge all the sound's channels into one
    :type mono: typing.Union[bool, typing.Any]
    '''

    pass


def open_mono(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              filepath: typing.Union[str, typing.Any] = "",
              hide_props_region: typing.Union[bool, typing.Any] = True,
              check_existing: typing.Union[bool, typing.Any] = False,
              filter_blender: typing.Union[bool, typing.Any] = False,
              filter_backup: typing.Union[bool, typing.Any] = False,
              filter_image: typing.Union[bool, typing.Any] = False,
              filter_movie: typing.Union[bool, typing.Any] = True,
              filter_python: typing.Union[bool, typing.Any] = False,
              filter_font: typing.Union[bool, typing.Any] = False,
              filter_sound: typing.Union[bool, typing.Any] = True,
              filter_text: typing.Union[bool, typing.Any] = False,
              filter_archive: typing.Union[bool, typing.Any] = False,
              filter_btx: typing.Union[bool, typing.Any] = False,
              filter_collada: typing.Union[bool, typing.Any] = False,
              filter_alembic: typing.Union[bool, typing.Any] = False,
              filter_usd: typing.Union[bool, typing.Any] = False,
              filter_obj: typing.Union[bool, typing.Any] = False,
              filter_volume: typing.Union[bool, typing.Any] = False,
              filter_folder: typing.Union[bool, typing.Any] = True,
              filter_blenlib: typing.Union[bool, typing.Any] = False,
              filemode: typing.Optional[typing.Any] = 9,
              relative_path: typing.Union[bool, typing.Any] = True,
              show_multiview: typing.Union[bool, typing.Any] = False,
              use_multiview: typing.Union[bool, typing.Any] = False,
              display_type: typing.Optional[typing.Any] = 'DEFAULT',
              sort_method: typing.Union[str, int, typing.Any] = '',
              cache: typing.Union[bool, typing.Any] = False,
              mono: typing.Union[bool, typing.Any] = True):
    ''' Load a sound file as mono

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: typing.Union[bool, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Union[bool, typing.Any]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Union[bool, typing.Any]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Union[bool, typing.Any]
    :param filter_image: Filter image files
    :type filter_image: typing.Union[bool, typing.Any]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Union[bool, typing.Any]
    :param filter_python: Filter python files
    :type filter_python: typing.Union[bool, typing.Any]
    :param filter_font: Filter font files
    :type filter_font: typing.Union[bool, typing.Any]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Union[bool, typing.Any]
    :param filter_text: Filter text files
    :type filter_text: typing.Union[bool, typing.Any]
    :param filter_archive: Filter archive files
    :type filter_archive: typing.Union[bool, typing.Any]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Union[bool, typing.Any]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Union[bool, typing.Any]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Union[bool, typing.Any]
    :param filter_usd: Filter USD files
    :type filter_usd: typing.Union[bool, typing.Any]
    :param filter_obj: Filter OBJ files
    :type filter_obj: typing.Union[bool, typing.Any]
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: typing.Union[bool, typing.Any]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Union[bool, typing.Any]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Union[bool, typing.Any]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: typing.Union[bool, typing.Any]
    :param show_multiview: Enable Multi-View
    :type show_multiview: typing.Union[bool, typing.Any]
    :param use_multiview: Use Multi-View
    :type use_multiview: typing.Union[bool, typing.Any]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int, typing.Any]
    :param cache: Cache, Cache the sound in memory
    :type cache: typing.Union[bool, typing.Any]
    :param mono: Mono, Mixdown the sound to mono
    :type mono: typing.Union[bool, typing.Any]
    '''

    pass


def pack(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None):
    ''' Pack the sound into the current blend file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def unpack(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None,
           *,
           method: typing.Union[str, int] = 'USE_LOCAL',
           id: typing.Union[str, typing.Any] = ""):
    ''' Unpack the sound to the samples filename

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param method: Method, How to unpack
    :type method: typing.Union[str, int]
    :param id: Sound Name, Sound data-block name to unpack
    :type id: typing.Union[str, typing.Any]
    '''

    pass


def update_animation_flags(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: typing.Optional[bool] = None):
    ''' Update animation flags

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass
