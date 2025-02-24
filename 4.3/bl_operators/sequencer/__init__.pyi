import typing
import collections.abc
import typing_extensions
import bpy.types

class Fade:
    animated_property: typing.Any
    duration: typing.Any
    end: typing.Any
    max_value: typing.Any
    start: typing.Any
    type: typing.Any

    def calculate_max_value(self, sequence, fade_fcurve):
        """Returns the maximum Y coordinate the fade animation should use for a given sequence
        Uses either the sequence's value for the animated property, or the next keyframe after the fade

                :param sequence:
                :param fade_fcurve:
        """

class SequencerFileHandlerBase:
    @classmethod
    def poll_drop(cls, context):
        """

        :param context:
        """

class SequencerCrossfadeSounds(bpy.types.Operator):
    """Do cross-fading volume animation of two selected sound strips"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def execute(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class SequencerDeinterlaceSelectedMovies(bpy.types.Operator):
    """Deinterlace all selected movie sources"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def execute(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class SequencerFadesAdd(bpy.types.Operator):
    """Adds or updates a fade animation for either visual or audio strips"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def calculate_fade_duration(self, context, sequence):
        """

        :param context:
        :param sequence:
        """

    def calculate_fades(self, sequence, fade_fcurve, animated_property, duration):
        """Returns a list of Fade objects

        :param sequence:
        :param fade_fcurve:
        :param animated_property:
        :param duration:
        """

    def execute(self, context):
        """

        :param context:
        """

    def fade_animation_clear(self, fade_fcurve, fades):
        """Removes existing keyframes in the fades' time range, in fast mode, without
        updating the fcurve

                :param fade_fcurve:
                :param fades:
        """

    def fade_animation_create(self, fade_fcurve, fades):
        """Inserts keyframes in the fade_fcurve in fast mode using the Fade objects.
        Updates the fcurve after having inserted all keyframes to finish the animation.

                :param fade_fcurve:
                :param fades:
        """

    def fade_find_or_create_fcurve(self, context, sequence, animated_property):
        """Iterates over all the fcurves until it finds an fcurve with a data path
        that corresponds to the sequence.
        Returns the matching FCurve or creates a new one if the function can't find a match.

                :param context:
                :param sequence:
                :param animated_property:
        """

    def is_long_enough(self, sequence, duration=0.0):
        """

        :param sequence:
        :param duration:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class SequencerFadesClear(bpy.types.Operator):
    """Removes fade animation from selected sequences"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def execute(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class SequencerSplitMulticam(bpy.types.Operator):
    """Split multicam strip and select camera"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def execute(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class SEQUENCER_FH_image_strip(bpy.types.FileHandler, SequencerFileHandlerBase):
    bl_file_extensions: typing.Any
    bl_idname: typing.Any
    bl_import_operator: typing.Any
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class SEQUENCER_FH_movie_strip(bpy.types.FileHandler, SequencerFileHandlerBase):
    bl_file_extensions: typing.Any
    bl_idname: typing.Any
    bl_import_operator: typing.Any
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class SEQUENCER_FH_sound_strip(bpy.types.FileHandler, SequencerFileHandlerBase):
    bl_file_extensions: typing.Any
    bl_idname: typing.Any
    bl_import_operator: typing.Any
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

def calculate_duration_frames(scene, duration_seconds): ...
