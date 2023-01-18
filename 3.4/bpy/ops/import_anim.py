import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def bvh(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        filter_glob: typing.Union[str, typing.Any] = "*.bvh",
        target: typing.Optional[typing.Any] = 'ARMATURE',
        global_scale: typing.Optional[typing.Any] = 1.0,
        frame_start: typing.Optional[typing.Any] = 1,
        use_fps_scale: typing.Union[bool, typing.Any] = False,
        update_scene_fps: typing.Union[bool, typing.Any] = False,
        update_scene_duration: typing.Union[bool, typing.Any] = False,
        use_cyclic: typing.Union[bool, typing.Any] = False,
        rotate_mode: typing.Optional[typing.Any] = 'NATIVE',
        axis_forward: typing.Optional[typing.Any] = '-Z',
        axis_up: typing.Optional[typing.Any] = 'Y'):
    ''' Load a BVH motion capture file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: typing.Union[str, typing.Any]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    :param target: Target, Import target type
    :type target: typing.Optional[typing.Any]
    :param global_scale: Scale, Scale the BVH by this value
    :type global_scale: typing.Optional[typing.Any]
    :param frame_start: Start Frame, Starting frame for the animation
    :type frame_start: typing.Optional[typing.Any]
    :param use_fps_scale: Scale FPS, Scale the framerate from the BVH to the current scenes, otherwise each BVH frame maps directly to a Blender frame
    :type use_fps_scale: typing.Union[bool, typing.Any]
    :param update_scene_fps: 1)
    :type update_scene_fps: typing.Union[bool, typing.Any]
    :param update_scene_duration: Update Scene Duration, Extend the scene's duration to the BVH duration (never shortens the scene)
    :type update_scene_duration: typing.Union[bool, typing.Any]
    :param use_cyclic: Loop, Loop the animation playback
    :type use_cyclic: typing.Union[bool, typing.Any]
    :param rotate_mode: Rotation, Rotation conversion * ``QUATERNION`` Quaternion -- Convert rotations to quaternions. * ``NATIVE`` Euler (Native) -- Use the rotation order defined in the BVH file. * ``XYZ`` Euler (XYZ) -- Convert rotations to euler XYZ. * ``XZY`` Euler (XZY) -- Convert rotations to euler XZY. * ``YXZ`` Euler (YXZ) -- Convert rotations to euler YXZ. * ``YZX`` Euler (YZX) -- Convert rotations to euler YZX. * ``ZXY`` Euler (ZXY) -- Convert rotations to euler ZXY. * ``ZYX`` Euler (ZYX) -- Convert rotations to euler ZYX.
    :type rotate_mode: typing.Optional[typing.Any]
    :param axis_forward: Forward
    :type axis_forward: typing.Optional[typing.Any]
    :param axis_up: Up
    :type axis_up: typing.Optional[typing.Any]
    '''

    pass
