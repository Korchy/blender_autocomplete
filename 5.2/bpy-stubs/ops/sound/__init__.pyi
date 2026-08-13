import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class bake_animation(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Update the audio animation cache

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class mixdown(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        check_existing: bool | None = True,
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
        accuracy: int | None = 1024,
        container: typing.Literal[
            "AAC", "AC3", "FLAC", "MATROSKA", "MP2", "MP3", "OGG", "WAV"
        ]
        | None = "FLAC",
        codec: typing.Literal["AAC", "AC3", "FLAC", "MP2", "MP3", "PCM", "VORBIS"]
        | None = "FLAC",
        channels: typing.Literal[
            "MONO",
            "STEREO",
            "STEREO_LFE",
            "SURROUND4",
            "SURROUND5",
            "SURROUND51",
            "SURROUND61",
            "SURROUND71",
        ]
        | None = "STEREO",
        format: typing.Literal["U8", "S16", "S24", "S32", "F32", "F64"] | None = "S16",
        mixrate: int | None = 48000,
        bitrate: int | None = 192,
        split_channels: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Mix the scenes audio to a sound file

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
                :param filter_blender: Filter .blend files, (optional)
                :param filter_backup: Filter backup .blend files, (optional)
                :param filter_image: Filter image files, (optional)
                :param filter_movie: Filter movie files, (optional)
                :param filter_python: Filter Python files, (optional)
                :param filter_font: Filter font files, (optional)
                :param filter_sound: Filter sound files, (optional)
                :param filter_text: Filter text files, (optional)
                :param filter_archive: Filter archive files, (optional)
                :param filter_btx: Filter btx files, (optional)
                :param filter_alembic: Filter Alembic files, (optional)
                :param filter_usd: Filter USD files, (optional)
                :param filter_obj: Filter OBJ files, (optional)
                :param filter_volume: Filter OpenVDB volume files, (optional)
                :param filter_folder: Filter folders, (optional)
                :param filter_blenlib: Filter Blender IDs, (optional)
                :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
                :param relative_path: Relative Path, Select the file relative to the blend file (optional)
                :param display_type: Display Type, (optional)

        DEFAULT
        Default -- Automatically determine display type for files.

        LIST_VERTICAL
        Short List -- Display files as short list.

        LIST_HORIZONTAL
        Long List -- Display files as a detailed list.

        THUMBNAIL
        Thumbnails -- Display files as thumbnails.
                :param sort_method: File sorting mode, (optional)
                :param accuracy: Accuracy, Sample accuracy, important for animation data (the lower the value, the more accurate) (in [1, inf], optional)
                :param container: Container, File format (optional)

        AAC
        AAC -- Advanced Audio Coding.

        AC3
        AC3 -- Dolby Digital ATRAC 3.

        FLAC
        FLAC -- Free Lossless Audio Codec.

        MATROSKA
        MKV -- Matroska.

        MP2
        MP2 -- MPEG-1 Audio Layer II.

        MP3
        MP3 -- MPEG-2 Audio Layer III.

        OGG
        OGG -- Xiph.Org Ogg Container.

        WAV
        WAV -- Waveform Audio File Format.
                :param codec: Codec, Audio Codec (optional)

        AAC
        AAC -- Advanced Audio Coding.

        AC3
        AC3 -- Dolby Digital ATRAC 3.

        FLAC
        FLAC -- Free Lossless Audio Codec.

        MP2
        MP2 -- MPEG-1 Audio Layer II.

        MP3
        MP3 -- MPEG-2 Audio Layer III.

        PCM
        PCM -- Pulse Code Modulation (RAW).

        VORBIS
        Vorbis -- Xiph.Org Vorbis Codec.
                :param channels: Channels, Audio channel count (optional)

        MONO
        Mono -- Single audio channel.

        STEREO
        Stereo -- Stereo audio channels.

        STEREO_LFE
        Stereo LFE -- Stereo with LFE channel.

        SURROUND4
        4 Channels -- 4 channel surround sound.

        SURROUND5
        5 Channels -- 5 channel surround sound.

        SURROUND51
        5.1 Surround -- 5.1 surround sound.

        SURROUND61
        6.1 Surround -- 6.1 surround sound.

        SURROUND71
        7.1 Surround -- 7.1 surround sound.
                :param format: Format, Sample format (optional)

        U8
        U8 -- 8-bit unsigned.

        S16
        S16 -- 16-bit signed.

        S24
        S24 -- 24-bit signed.

        S32
        S32 -- 32-bit signed.

        F32
        F32 -- 32-bit floating-point.

        F64
        F64 -- 64-bit floating-point.
                :param mixrate: Sample Rate, Sample rate in samples/s (in [8000, 192000], optional)
                :param bitrate: Bitrate, Bitrate in kbit/s (in [32, 512], optional)
                :param split_channels: Split channels, Each channel will be rendered into a mono file (optional)
                :return: Result of the operator call.
        """

class open(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        hide_props_region: bool | None = True,
        check_existing: bool | None = False,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = True,
        filter_python: bool | None = False,
        filter_font: bool | None = False,
        filter_sound: bool | None = True,
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
        sort_method: str | None = "",
        cache: bool | None = False,
        mono: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Load a sound file

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
                :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
                :param filter_blender: Filter .blend files, (optional)
                :param filter_backup: Filter backup .blend files, (optional)
                :param filter_image: Filter image files, (optional)
                :param filter_movie: Filter movie files, (optional)
                :param filter_python: Filter Python files, (optional)
                :param filter_font: Filter font files, (optional)
                :param filter_sound: Filter sound files, (optional)
                :param filter_text: Filter text files, (optional)
                :param filter_archive: Filter archive files, (optional)
                :param filter_btx: Filter btx files, (optional)
                :param filter_alembic: Filter Alembic files, (optional)
                :param filter_usd: Filter USD files, (optional)
                :param filter_obj: Filter OBJ files, (optional)
                :param filter_volume: Filter OpenVDB volume files, (optional)
                :param filter_folder: Filter folders, (optional)
                :param filter_blenlib: Filter Blender IDs, (optional)
                :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
                :param relative_path: Relative Path, Select the file relative to the blend file (optional)
                :param show_multiview: Enable Multi-View, (optional)
                :param use_multiview: Use Multi-View, (optional)
                :param display_type: Display Type, (optional)

        DEFAULT
        Default -- Automatically determine display type for files.

        LIST_VERTICAL
        Short List -- Display files as short list.

        LIST_HORIZONTAL
        Long List -- Display files as a detailed list.

        THUMBNAIL
        Thumbnails -- Display files as thumbnails.
                :param sort_method: File sorting mode, (optional)
                :param cache: Cache, Cache the sound in memory (optional)
                :param mono: Mono, Merge all the sounds channels into one (optional)
                :return: Result of the operator call.
        """

class open_mono(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        hide_props_region: bool | None = True,
        check_existing: bool | None = False,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = True,
        filter_python: bool | None = False,
        filter_font: bool | None = False,
        filter_sound: bool | None = True,
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
        sort_method: str | None = "",
        cache: bool | None = False,
        mono: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Load a sound file as mono

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
                :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
                :param filter_blender: Filter .blend files, (optional)
                :param filter_backup: Filter backup .blend files, (optional)
                :param filter_image: Filter image files, (optional)
                :param filter_movie: Filter movie files, (optional)
                :param filter_python: Filter Python files, (optional)
                :param filter_font: Filter font files, (optional)
                :param filter_sound: Filter sound files, (optional)
                :param filter_text: Filter text files, (optional)
                :param filter_archive: Filter archive files, (optional)
                :param filter_btx: Filter btx files, (optional)
                :param filter_alembic: Filter Alembic files, (optional)
                :param filter_usd: Filter USD files, (optional)
                :param filter_obj: Filter OBJ files, (optional)
                :param filter_volume: Filter OpenVDB volume files, (optional)
                :param filter_folder: Filter folders, (optional)
                :param filter_blenlib: Filter Blender IDs, (optional)
                :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
                :param relative_path: Relative Path, Select the file relative to the blend file (optional)
                :param show_multiview: Enable Multi-View, (optional)
                :param use_multiview: Use Multi-View, (optional)
                :param display_type: Display Type, (optional)

        DEFAULT
        Default -- Automatically determine display type for files.

        LIST_VERTICAL
        Short List -- Display files as short list.

        LIST_HORIZONTAL
        Long List -- Display files as a detailed list.

        THUMBNAIL
        Thumbnails -- Display files as thumbnails.
                :param sort_method: File sorting mode, (optional)
                :param cache: Cache, Cache the sound in memory (optional)
                :param mono: Mono, Mixdown the sound to mono (optional)
                :return: Result of the operator call.
        """

class pack(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Pack the sound into the current blend file

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class unpack(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        method: typing.Literal[bpy.stub_internal.rna_enums.UnpackMethodItems]
        | None = "USE_LOCAL",
        id: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Unpack the sound to the samples filename

        :param execution_context:
        :param undo:
        :param method: Method, How to unpack (optional)
        :param id: Sound Name, Sound data-block name to unpack (optional, never None)
        :return: Result of the operator call.
        """

class update_animation_flags(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Update animation flags

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
