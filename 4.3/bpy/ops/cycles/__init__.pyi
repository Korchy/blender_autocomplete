import typing
import collections.abc
import typing_extensions

def denoise_animation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    input_filepath: str = "",
    output_filepath: str = "",
):
    """Denoise rendered animation sequence using current scene and view layer settings. Requires denoising data passes and output to OpenEXR multilayer files

    :type execution_context: int | str | None
    :type undo: bool | None
    :param input_filepath: Input Filepath, File path for image to denoise. If not specified, uses the render file path and frame range from the scene
    :type input_filepath: str
    :param output_filepath: Output Filepath, If not specified, renders will be denoised in-place
    :type output_filepath: str
    """

def merge_images(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    input_filepath1: str = "",
    input_filepath2: str = "",
    output_filepath: str = "",
):
    """Combine OpenEXR multi-layer images rendered with different sample ranges into one image with reduced noise

    :type execution_context: int | str | None
    :type undo: bool | None
    :param input_filepath1: Input Filepath, File path for image to merge
    :type input_filepath1: str
    :param input_filepath2: Input Filepath, File path for image to merge
    :type input_filepath2: str
    :param output_filepath: Output Filepath, File path for merged image
    :type output_filepath: str
    """

def use_shading_nodes(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Enable nodes on a material, world or light

    :type execution_context: int | str | None
    :type undo: bool | None
    """
