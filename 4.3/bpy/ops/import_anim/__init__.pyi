import typing
import collections.abc
import typing_extensions

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
):
    """Load a BVH motion capture file

        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Filepath used for importing the file
        :type filepath: str
        :param filter_glob: filter_glob
        :type filter_glob: str
        :param target: Target, Import target type
        :type target: typing.Literal['ARMATURE','OBJECT'] | None
        :param global_scale: Scale, Scale the BVH by this value
        :type global_scale: float | None
        :param frame_start: Start Frame, Starting frame for the animation
        :type frame_start: int | None
        :param use_fps_scale: Scale FPS, Scale the framerate from the BVH to the current scenes, otherwise each BVH frame maps directly to a Blender frame
        :type use_fps_scale: bool | None
        :param update_scene_fps: Update Scene FPS, Set the scene framerate to that of the BVH file (note that this nullifies the 'Scale FPS' option, as the scale will be 1:1)
        :type update_scene_fps: bool | None
        :param update_scene_duration: Update Scene Duration, Extend the scene's duration to the BVH duration (never shortens the scene)
        :type update_scene_duration: bool | None
        :param use_cyclic: Loop, Loop the animation playback
        :type use_cyclic: bool | None
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
        :type rotate_mode: typing.Literal['QUATERNION','NATIVE','XYZ','XZY','YXZ','YZX','ZXY','ZYX'] | None
        :param axis_forward: Forward
        :type axis_forward: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param axis_up: Up
        :type axis_up: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
    """
