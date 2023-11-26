import sys
import typing
import bpy.types
import gpu.types

GenericType = typing.TypeVar("GenericType")


def from_image(image: 'bpy.types.Image') -> 'gpu.types.GPUTexture':
    ''' Get GPUTexture corresponding to an Image datablock. The GPUTexture memory is shared with Blender. Note: Colors read from the texture will be in scene linear color space and have premultiplied or straight alpha matching the image alpha mode.

    :param image: The Image datablock.
    :type image: 'bpy.types.Image'
    :rtype: 'gpu.types.GPUTexture'
    :return: The GPUTexture used by the image.
    '''

    pass
