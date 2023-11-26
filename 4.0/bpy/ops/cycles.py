import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def denoise_animation(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        input_filepath: typing.Union[str, typing.Any] = "",
        output_filepath: typing.Union[str, typing.Any] = ""):
    ''' Denoise rendered animation sequence using current scene and view layer settings. Requires denoising data passes and output to OpenEXR multilayer files :File: `addons/cycles/operators.py\:54 <https://projects.blender.org/blender/blender-addons/addons/cycles/operators.py#L54>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param input_filepath: Input Filepath, File path for image to denoise. If not specified, uses the render file path and frame range from the scene
    :type input_filepath: typing.Union[str, typing.Any]
    :param output_filepath: Output Filepath, If not specified, renders will be denoised in-place
    :type output_filepath: typing.Union[str, typing.Any]
    '''

    pass


def merge_images(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        input_filepath1: typing.Union[str, typing.Any] = "",
        input_filepath2: typing.Union[str, typing.Any] = "",
        output_filepath: typing.Union[str, typing.Any] = ""):
    ''' Combine OpenEXR multi-layer images rendered with different sample ranges into one image with reduced noise :File: `addons/cycles/operators.py\:142 <https://projects.blender.org/blender/blender-addons/addons/cycles/operators.py#L142>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param input_filepath1: Input Filepath, File path for image to merge
    :type input_filepath1: typing.Union[str, typing.Any]
    :param input_filepath2: Input Filepath, File path for image to merge
    :type input_filepath2: typing.Union[str, typing.Any]
    :param output_filepath: Output Filepath, File path for merged image
    :type output_filepath: typing.Union[str, typing.Any]
    '''

    pass


def use_shading_nodes(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Enable nodes on a material, world or light :File: `addons/cycles/operators.py\:24 <https://projects.blender.org/blender/blender-addons/addons/cycles/operators.py#L24>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass
