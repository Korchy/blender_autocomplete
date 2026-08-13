import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class denoise_animation(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        input_filepath: str = "",
        output_filepath: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Denoise rendered animation sequence using current scene and view layer settings. Requires denoising data passes and output to OpenEXR multilayer files

        :param execution_context:
        :param undo:
        :param input_filepath: Input Filepath, File path for image to denoise. If not specified, uses the render file path and frame range from the scene (optional, never None)
        :param output_filepath: Output Filepath, If not specified, renders will be denoised in-place (optional, never None)
        :return: Result of the operator call.
        """

class merge_images(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        input_filepath1: str = "",
        input_filepath2: str = "",
        output_filepath: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Combine OpenEXR multi-layer images rendered with different sample ranges into one image with reduced noise

        :param execution_context:
        :param undo:
        :param input_filepath1: Input Filepath, File path for image to merge (optional, never None)
        :param input_filepath2: Input Filepath, File path for image to merge (optional, never None)
        :param output_filepath: Output Filepath, File path for merged image (optional, never None)
        :return: Result of the operator call.
        """

class use_shading_nodes(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Enable nodes on a light

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
