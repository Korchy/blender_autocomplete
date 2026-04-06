import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def denoise_animation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    input_filepath: str = "",
    output_filepath: str = "",
) -> None:
    """Denoise rendered animation sequence using current scene and view layer settings. Requires denoising data passes and output to OpenEXR multilayer files

    :param input_filepath: Input Filepath, File path for image to denoise. If not specified, uses the render file path and frame range from the scene
    :param output_filepath: Output Filepath, If not specified, renders will be denoised in-place
    """

def merge_images(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    input_filepath1: str = "",
    input_filepath2: str = "",
    output_filepath: str = "",
) -> None:
    """Combine OpenEXR multi-layer images rendered with different sample ranges into one image with reduced noise

    :param input_filepath1: Input Filepath, File path for image to merge
    :param input_filepath2: Input Filepath, File path for image to merge
    :param output_filepath: Output Filepath, File path for merged image
    """

def use_shading_nodes(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Enable nodes on a light"""
