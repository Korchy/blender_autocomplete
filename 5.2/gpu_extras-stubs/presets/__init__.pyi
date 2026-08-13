import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import gpu.types

def draw_circle_2d(
    position: collections.abc.Sequence[float],
    color: collections.abc.Sequence[float],
    radius: float,
    *,
    segments: None | int | None = None,
) -> None:
    """Draw a circle.

        :param position: 2D position where the circle will be drawn.
        :param color: Color of the circle (RGBA).
    To use transparency blend must be set to ALPHA, see: `gpu.state.blend_set`.
        :param radius: Radius of the circle.
        :param segments: How many segments will be used to draw the circle.
    Higher values give better results but the drawing will take longer.
    If None or not specified, an automatic value will be calculated.
    """

def draw_texture_2d(
    texture: gpu.types.GPUTexture,
    position: collections.abc.Sequence[float],
    width: float,
    height: float,
    is_scene_linear_with_rec709_srgb_target: bool = False,
) -> None:
    """Draw a 2d texture.

        :param texture: GPUTexture to draw (e.g. gpu.texture.from_image(image) for `bpy.types.Image`).
        :param position: 2D position of the lower left corner.
        :param width: Width of the image when drawn (not necessarily
    the original width of the texture).
        :param height: Height of the image when drawn.
        :param is_scene_linear_with_rec709_srgb_target: True if the texture is stored in scene linear color space and
    the destination frame-buffer uses the Rec.709 sRGB color space
    (which is true when drawing textures acquired from `bpy.types.Image` inside a
    PRE_VIEW, POST_VIEW or POST_PIXEL draw handler).
    Otherwise the color space is assumed to match the one of the frame-buffer. (default=False)
    """
