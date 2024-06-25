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
    filter_glob: str | typing.Any = "*.bvh",
    target: str | None = "ARMATURE",
    global_scale: typing.Any | None = 1.0,
    frame_start: typing.Any | None = 1,
    use_fps_scale: bool | typing.Any | None = False,
    update_scene_fps: bool | typing.Any | None = False,
    update_scene_duration: bool | typing.Any | None = False,
    use_cyclic: bool | typing.Any | None = False,
    rotate_mode: str | None = "NATIVE",
    axis_forward: str | None = "-Z",
    axis_up: str | None = "Y",
):
    """Load a BVH motion capture file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Filepath used for importing the file
        :type filepath: str | typing.Any
        :param filter_glob: filter_glob
        :type filter_glob: str | typing.Any
        :param target: Target, Import target type
        :type target: str | None
        :param global_scale: Scale, Scale the BVH by this value
        :type global_scale: typing.Any | None
        :param frame_start: Start Frame, Starting frame for the animation
        :type frame_start: typing.Any | None
        :param use_fps_scale: Scale FPS, Scale the framerate from the BVH to the current scenes, otherwise each BVH frame maps directly to a Blender frame
        :type use_fps_scale: bool | typing.Any | None
        :param update_scene_fps: Update Scene FPS, Set the scene framerate to that of the BVH file (note that this nullifies the 'Scale FPS' option, as the scale will be 1:1)
        :type update_scene_fps: bool | typing.Any | None
        :param update_scene_duration: Update Scene Duration, Extend the scene's duration to the BVH duration (never shortens the scene)
        :type update_scene_duration: bool | typing.Any | None
        :param use_cyclic: Loop, Loop the animation playback
        :type use_cyclic: bool | typing.Any | None
        :param rotate_mode: Rotation, Rotation conversion

    QUATERNION
    Quaternion -- Convert rotations to quaternions.

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
        :param axis_forward: Forward
        :type axis_forward: str | None
        :param axis_up: Up
        :type axis_up: str | None
    """

    ...
