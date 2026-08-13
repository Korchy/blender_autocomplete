import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class bvh(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        check_existing: bool | None = True,
        filter_glob: str = "*.bvh",
        global_scale: float | None = 1.0,
        frame_start: int | None = 0,
        frame_end: int | None = 0,
        rotate_mode: typing.Literal["NATIVE", "XYZ", "XZY", "YXZ", "YZX", "ZXY", "ZYX"]
        | None = "NATIVE",
        root_transform_only: bool | None = False,
        sort_children_by_names: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Save a BVH motion capture file from an armature

                :param execution_context:
                :param undo:
                :param filepath: File Path, Filepath used for exporting the file (optional, never None)
                :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
                :param filter_glob: filter_glob, (optional, never None)
                :param global_scale: Scale, Scale the BVH by this value (in [0.0001, 1e+06], optional)
                :param frame_start: Start Frame, Starting frame to export (in [-inf, inf], optional)
                :param frame_end: End Frame, End frame to export (in [-inf, inf], optional)
                :param rotate_mode: Rotation, Rotation conversion (optional)

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
                :param root_transform_only: Root Translation Only, Only write out translation channels for the root bone (optional)
                :param sort_children_by_names: Sort Children By Name, Sort the children of each bone alphabetically (optional)
                :return: Result of the operator call.
        """
