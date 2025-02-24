import typing
import collections.abc
import typing_extensions
import gpu.types
import mathutils

def draw_circle_2d(
    position: collections.abc.Sequence[float],
    color: collections.abc.Sequence[float],
    radius: float,
    *,
    segments: None | int | None = None,
):
    """Draw a circle.

        :param position: 2D position where the circle will be drawn.
        :type position: collections.abc.Sequence[float]
        :param color: Color of the circle (RGBA).
    To use transparency blend must be set to ALPHA, see: `gpu.state.blend_set`.
        :type color: collections.abc.Sequence[float]
        :param radius: Radius of the circle.
        :type radius: float
        :param segments: How many segments will be used to draw the circle.
    Higher values give better results but the drawing will take longer.
    If None or not specified, an automatic value will be calculated.
        :type segments: None | int | None
    """

def draw_texture_2d(
    texture: gpu.types.GPUTexture,
    position: collections.abc.Sequence[float] | mathutils.Vector,
    width: float,
    height: float,
):
    """Draw a 2d texture.

        :param texture: GPUTexture to draw (e.g. gpu.texture.from_image(image) for `bpy.types.Image`).
        :type texture: gpu.types.GPUTexture
        :param position: Position of the lower left corner.
        :type position: collections.abc.Sequence[float] | mathutils.Vector
        :param width: Width of the image when drawn (not necessarily
    the original width of the texture).
        :type width: float
        :param height: Height of the image when drawn.
        :type height: float
    """
