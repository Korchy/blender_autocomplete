import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class BUILTIN_KSI_Available(_bpy_types.KeyingSetInfo):
    """Insert a keyframe on each of the already existing F-Curves"""

    bl_idname: typing.Any
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

    def poll(self, context) -> None:
        """

        :param context:
        """

class BUILTIN_KSI_BendyBones(_bpy_types.KeyingSetInfo):
    """Insert a keyframe for each of the B-Bone shape properties"""

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

class BUILTIN_KSI_DeltaLocation(_bpy_types.KeyingSetInfo):
    """Insert keyframes for additional location offset"""

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

    def generate(self, _context, ks, data) -> None:
        """

        :param _context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_DeltaRotation(_bpy_types.KeyingSetInfo):
    """Insert keyframes for additional rotation offset"""

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

    def generate(self, _context, ks, data) -> None:
        """

        :param _context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_DeltaScale(_bpy_types.KeyingSetInfo):
    """Insert keyframes for additional scale factor"""

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

    def generate(self, _context, ks, data) -> None:
        """

        :param _context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_LocRot(_bpy_types.KeyingSetInfo):
    """Insert a keyframe on each of the location and rotation channels"""

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

    def generate(self, context, ks, data) -> None:
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_LocRotScale(_bpy_types.KeyingSetInfo):
    """Insert a keyframe on each of the location, rotation, and scale channels"""

    bl_idname: typing.Any
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

    def generate(self, context, ks, data) -> None:
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_LocRotScaleCProp(_bpy_types.KeyingSetInfo):
    """Key location/rotation/scale as well as custom properties"""

    bl_idname: typing.Any
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

    def generate(self, context, ks, data) -> None:
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_LocScale(_bpy_types.KeyingSetInfo):
    """Insert a keyframe on each of the location and scale channels"""

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

    def generate(self, context, ks, data) -> None:
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_Location(_bpy_types.KeyingSetInfo):
    """Insert a keyframe on each of the location channels"""

    bl_idname: typing.Any
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

class BUILTIN_KSI_RotScale(_bpy_types.KeyingSetInfo):
    """Insert a keyframe on each of the rotation and scale channels"""

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

    def generate(self, context, ks, data) -> None:
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_Rotation(_bpy_types.KeyingSetInfo):
    """Insert a keyframe on each of the rotation channels"""

    bl_idname: typing.Any
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

class BUILTIN_KSI_Scaling(_bpy_types.KeyingSetInfo):
    """Insert a keyframe on each of the scale channels"""

    bl_idname: typing.Any
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

class BUILTIN_KSI_VisualLoc(_bpy_types.KeyingSetInfo):
    """Insert a keyframe on each of the location channels, taking into account effects of constraints and relationships"""

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

class BUILTIN_KSI_VisualLocRot(_bpy_types.KeyingSetInfo):
    """Insert a keyframe on each of the location and rotation channels, taking into account effects of constraints and relationships"""

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

    def generate(self, context, ks, data) -> None:
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_VisualLocRotScale(_bpy_types.KeyingSetInfo):
    """Insert a keyframe on each of the location, rotation and scale channels, taking into account effects of constraints and relationships"""

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

    def generate(self, context, ks, data) -> None:
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_VisualLocScale(_bpy_types.KeyingSetInfo):
    """Insert a keyframe on each of the location and scale channels, taking into account effects of constraints and relationships"""

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

    def generate(self, context, ks, data) -> None:
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_VisualRot(_bpy_types.KeyingSetInfo):
    """Insert a keyframe on each of the rotation channels, taking into account effects of constraints and relationships"""

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

class BUILTIN_KSI_VisualRotScale(_bpy_types.KeyingSetInfo):
    """Insert a keyframe on each of the rotation and scale channels, taking into account effects of constraints and relationships"""

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

    def generate(self, context, ks, data) -> None:
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_VisualScaling(_bpy_types.KeyingSetInfo):
    """Insert a keyframe on each of the scale channels, taking into account effects of constraints and relationships"""

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

class BUILTIN_KSI_WholeCharacter(WholeCharacterMixin, _bpy_types.KeyingSetInfo):
    """Insert a keyframe for all properties that are likely to get animated in a character rig (useful when blocking out a shot)"""

    badBonePrefixes: typing.Any
    bl_idname: typing.Any
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

class BUILTIN_KSI_WholeCharacterSelected(WholeCharacterMixin, _bpy_types.KeyingSetInfo):
    """Insert a keyframe for all properties that are likely to get animated in a character rig (only selected bones)"""

    badBonePrefixes: typing.Any
    bl_idname: typing.Any
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

    def iterator(self, context, ks) -> None:
        """

        :param context:
        :param ks:
        """

class WholeCharacterMixin:
    badBonePrefixes: typing.Any

    def addProp(self, ks, bone, prop, index=-1, use_groups=True) -> None:
        """

        :param ks:
        :param bone:
        :param prop:
        :param index:
        :param use_groups:
        """

    def doBBone(self, context, ks, pchan) -> None:
        """

        :param context:
        :param ks:
        :param pchan:
        """

    def doCustomProps(self, ks, bone) -> None:
        """

        :param ks:
        :param bone:
        """

    def doLoc(self, ks, bone) -> None:
        """

        :param ks:
        :param bone:
        """

    def doRot3d(self, ks, bone) -> None:
        """

        :param ks:
        :param bone:
        """

    def doRot4d(self, ks, bone) -> None:
        """

        :param ks:
        :param bone:
        """

    def doScale(self, ks, bone) -> None:
        """

        :param ks:
        :param bone:
        """

    def generate(self, context, ks, bone) -> None:
        """

        :param context:
        :param ks:
        :param bone:
        """

    def iterator(self, context, ks) -> None:
        """

        :param context:
        :param ks:
        """

    def poll(self, context) -> None:
        """

        :param context:
        """

def register() -> None: ...
def unregister() -> None: ...
