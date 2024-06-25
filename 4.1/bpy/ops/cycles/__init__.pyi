import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def denoise_animation(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    input_filepath: str | typing.Any = "",
    output_filepath: str | typing.Any = "",
):
    """Denoise rendered animation sequence using current scene and view layer settings. Requires denoising data passes and output to OpenEXR multilayer files

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param input_filepath: Input Filepath, File path for image to denoise. If not specified, uses the render file path and frame range from the scene
    :type input_filepath: str | typing.Any
    :param output_filepath: Output Filepath, If not specified, renders will be denoised in-place
    :type output_filepath: str | typing.Any
    """

    ...

def merge_images(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    input_filepath1: str | typing.Any = "",
    input_filepath2: str | typing.Any = "",
    output_filepath: str | typing.Any = "",
):
    """Combine OpenEXR multi-layer images rendered with different sample ranges into one image with reduced noise

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param input_filepath1: Input Filepath, File path for image to merge
    :type input_filepath1: str | typing.Any
    :param input_filepath2: Input Filepath, File path for image to merge
    :type input_filepath2: str | typing.Any
    :param output_filepath: Output Filepath, File path for merged image
    :type output_filepath: str | typing.Any
    """

    ...

def use_shading_nodes(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Enable nodes on a material, world or light

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...
