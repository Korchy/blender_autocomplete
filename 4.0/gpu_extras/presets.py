import sys
import typing
import mathutils
import gpu.types

GenericType = typing.TypeVar("GenericType")


def draw_circle_2d(position: 'mathutils.Vector',
                   color: typing.Tuple,
                   radius: float,
                   *,
                   segments: typing.Optional[int] = None):
    ''' Draw a circle.

    :param position: Position where the circle will be drawn.
    :type position: 'mathutils.Vector'
    :param color: Color of the circle. To use transparency GL_BLEND has to be enabled.
    :type color: typing.Tuple
    :param radius: Radius of the circle.
    :type radius: float
    :param segments: How many segments will be used to draw the circle. Higher values give better results but the drawing will take longer. If None or not specified, an automatic value will be calculated.
    :type segments: typing.Optional[int]
    '''

    pass


def draw_texture_2d(texture: 'gpu.types.GPUTexture',
                    position: 'mathutils.Vector', width: float, height: float):
    ''' Draw a 2d texture.

    :param texture: `bpy.types.Image`).
    :type texture: 'gpu.types.GPUTexture'
    :param position: Position of the lower left corner.
    :type position: 'mathutils.Vector'
    :param width: Width of the image when drawn (not necessarily the original width of the texture).
    :type width: float
    :param height: Height of the image when drawn.
    :type height: float
    '''

    pass
