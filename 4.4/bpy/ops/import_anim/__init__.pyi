import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def bvh(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    filter_glob: str = "*.bvh",
    target: typing.Literal["ARMATURE", "OBJECT"] | None = "ARMATURE",
    global_scale: float | None = 1.0,
    frame_start: int | None = 1,
    use_fps_scale: bool | None = False,
    update_scene_fps: bool | None = False,
    update_scene_duration: bool | None = False,
    use_cyclic: bool | None = False,
    rotate_mode: typing.Literal[
        "QUATERNION", "NATIVE", "XYZ", "XZY", "YXZ", "YZX", "ZXY", "ZYX"
    ]
    | None = "NATIVE",
    axis_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "-Z",
    axis_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
) -> None:
    """Load a BVH motion capture file

        :param filepath: File Path, Filepath used for importing the file
        :param filter_glob: filter_glob
        :param target: Target, Import target type
        :param global_scale: Scale, Scale the BVH by this value
        :param frame_start: Start Frame, Starting frame for the animation
        :param use_fps_scale: Scale FPS, Scale the framerate from the BVH to the current scenes, otherwise each BVH frame maps directly to a Blender frame
        :param update_scene_fps: Update Scene FPS, Set the scene framerate to that of the BVH file (note that this nullifies the Scale FPS option, as the scale will be 1:1)
        :param update_scene_duration: Update Scene Duration, Extend the scenes duration to the BVH duration (never shortens the scene)
        :param use_cyclic: Loop, Loop the animation playback
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
        :param axis_forward: Forward
        :param axis_up: Up
    """
