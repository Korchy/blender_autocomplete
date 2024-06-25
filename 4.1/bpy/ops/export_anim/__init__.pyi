import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def bvh(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    check_existing: bool | typing.Any | None = True,
    filter_glob: str | typing.Any = "*.bvh",
    global_scale: typing.Any | None = 1.0,
    frame_start: typing.Any | None = 0,
    frame_end: typing.Any | None = 0,
    rotate_mode: str | None = "NATIVE",
    root_transform_only: bool | typing.Any | None = False,
):
    """Save a BVH motion capture file from an armature

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Filepath used for exporting the file
        :type filepath: str | typing.Any
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_glob: filter_glob
        :type filter_glob: str | typing.Any
        :param global_scale: Scale, Scale the BVH by this value
        :type global_scale: typing.Any | None
        :param frame_start: Start Frame, Starting frame to export
        :type frame_start: typing.Any | None
        :param frame_end: End Frame, End frame to export
        :type frame_end: typing.Any | None
        :param rotate_mode: Rotation, Rotation conversion

    NATIVE
    Euler (Native) -- Use the rotation order defined in the BVH file.

    XYZ
    Euler (XYZ) -- Convert rotations to euler XYZ.

    XZY
    Euler (XZY) -- Convert rotations to euler XZY.

    YXZ
    Euler (YXZ) -- Convert rotations to euler YXZ.

    YZX
    Euler (YZX) -- Convert rotations to euler YZX.

    ZXY
    Euler (ZXY) -- Convert rotations to euler ZXY.

    ZYX
    Euler (ZYX) -- Convert rotations to euler ZYX.
        :type rotate_mode: str | None
        :param root_transform_only: Root Translation Only, Only write out translation channels for the root bone
        :type root_transform_only: bool | typing.Any | None
    """

    ...
