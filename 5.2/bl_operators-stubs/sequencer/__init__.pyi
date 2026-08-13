import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class Fade:
    animated_property: typing.Any
    duration: typing.Any
    end: typing.Any
    max_value: typing.Any
    start: typing.Any
    type: typing.Any

    def calculate_max_value(self, strip, fade_fcurve) -> None:
        """Returns the maximum Y coordinate the fade animation should use for a given strip
        Uses either the strips value for the animated property, or the next keyframe after the fade

                :param strip:
                :param fade_fcurve:
        """

class SequencerFileHandlerBase:
    @classmethod
    def poll_drop(cls, context) -> None:
        """

        :param context:
        """

class SequencerCrossfadeSounds(_bpy_types.Operator):
    """Do cross-fading volume animation of two selected sound strips"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class SequencerDeinterlaceSelectedMovies(_bpy_types.Operator):
    """Deinterlace all selected movie sources"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class SequencerFadesAdd(_bpy_types.Operator):
    """Adds or updates a fade animation for either visual or audio strips"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def calculate_fade_duration(self, context, strip) -> None:
        """

        :param context:
        :param strip:
        """

    def calculate_fades(self, strip, fade_fcurve, animated_property, duration) -> None:
        """Returns a list of Fade objects

        :param strip:
        :param fade_fcurve:
        :param animated_property:
        :param duration:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

    def fade_animation_clear(self, fade_fcurve, fades) -> None:
        """Removes existing keyframes in the fades time range, in fast mode, without
        updating the fcurve

                :param fade_fcurve:
                :param fades:
        """

    def fade_animation_create(self, fade_fcurve, fades) -> None:
        """Inserts keyframes in the fade_fcurve in fast mode using the Fade objects.
        Updates the fcurve after having inserted all keyframes to finish the animation.

                :param fade_fcurve:
                :param fades:
        """

    def fade_find_or_create_fcurve(self, context, strip, animated_property) -> None:
        """Iterates over all the fcurves until it finds an fcurve with a data path
        that corresponds to the strip.
        Returns the matching FCurve or creates a new one if the function cant find a match.

                :param context:
                :param strip:
                :param animated_property:
        """

    def is_long_enough(self, strip, duration=0.0) -> None:
        """

        :param strip:
        :param duration:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class SequencerFadesClear(_bpy_types.Operator):
    """Removes fade animation from selected strips"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class SequencerSplitMulticam(_bpy_types.Operator):
    """Split multicam strip and select camera"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class SEQUENCER_FH_image_strip(_bpy_types.FileHandler, SequencerFileHandlerBase):
    bl_file_extensions: typing.Any
    bl_idname: typing.Any
    bl_import_operator: typing.Any
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class SEQUENCER_FH_movie_strip(_bpy_types.FileHandler, SequencerFileHandlerBase):
    bl_file_extensions: typing.Any
    bl_idname: typing.Any
    bl_import_operator: typing.Any
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class SEQUENCER_FH_sound_strip(_bpy_types.FileHandler, SequencerFileHandlerBase):
    bl_file_extensions: typing.Any
    bl_idname: typing.Any
    bl_import_operator: typing.Any
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

def calculate_duration_frames(scene, duration_seconds) -> None: ...
