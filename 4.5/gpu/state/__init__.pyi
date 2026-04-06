"""
This module provides access to the gpu state.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def active_framebuffer_get(enable) -> None:
    """Return the active frame-buffer in context."""

def blend_get() -> None:
    """Current blending equation."""

def blend_set(mode: str) -> None:
    """Defines the fixed pipeline blending equation.

        :param mode: The type of blend mode.

    NONE No blending.

    ALPHA The original color channels are interpolated according to the alpha value.

    ALPHA_PREMULT The original color channels are interpolated according to the alpha value with the new colors pre-multiplied by this value.

    ADDITIVE The original color channels are added by the corresponding ones.

    ADDITIVE_PREMULT The original color channels are added by the corresponding ones that are pre-multiplied by the alpha value.

    MULTIPLY The original color channels are multiplied by the corresponding ones.

    SUBTRACT The original color channels are subtracted by the corresponding ones.

    INVERT The original color channels are replaced by its complementary color.
    """

def clip_distances_set(distances_enabled: int) -> None:
    """Sets the number of gl_ClipDistance planes used for clip geometry.

    :param distances_enabled: Number of clip distances enabled.
    """

def color_mask_set(r: bool, g, b, a) -> None:
    """Enable or disable writing of frame buffer color components.

    :param r: components red, green, blue, and alpha.
    """

def depth_mask_get() -> None:
    """Writing status in the depth component."""

def depth_mask_set(value) -> None:
    """Write to depth component.

    :param value: True for writing to the depth component.
    """

def depth_test_get() -> None:
    """Current depth_test equation."""

def depth_test_set(mode: str) -> None:
    """Defines the depth_test equation.

        :param mode: The depth test equation name.
    Possible values are NONE, ALWAYS, LESS, LESS_EQUAL, EQUAL, GREATER and GREATER_EQUAL.
    """

def face_culling_set(culling) -> None:
    """Specify whether none, front-facing or back-facing facets can be culled."""

def front_facing_set(invert) -> None:
    """Specifies the orientation of front-facing polygons.

    :param invert: True for clockwise polygons as front-facing.
    """

def line_width_get() -> None:
    """Current width of rasterized lines."""

def line_width_set(width) -> None:
    """Specify the width of rasterized lines."""

def point_size_set(size) -> None:
    """Specify the diameter of rasterized points.

    :param size: New diameter.
    """

def program_point_size_set(enable: bool) -> None:
    """If enabled, the derived point size is taken from the (potentially clipped) shader builtin gl_PointSize.

    :param enable: True for shader builtin gl_PointSize.
    """

def scissor_get() -> tuple[int, int, int, int]:
    """Retrieve the scissors of the active framebuffer.
    Note: Only valid between scissor_set and a framebuffer rebind.

        :return: The scissor of the active framebuffer as a tuple
    (x, y, xsize, ysize).
    x, y: lower left corner of the scissor rectangle, in pixels.
    xsize, ysize: width and height of the scissor rectangle.
    """

def scissor_set(x: int, y, xsize: int, ysize) -> None:
    """Specifies the scissor area of the active framebuffer.
    Note: The scissor state is not saved upon framebuffer rebind.

        :param x: lower left corner of the scissor rectangle, in pixels.
        :param xsize: width and height of the scissor rectangle.
    """

def scissor_test_set(enable: bool) -> None:
    """Enable/disable scissor testing on the active framebuffer.

        :param enable: True - enable scissor testing.
    False - disable scissor testing.
    """

def viewport_get() -> None:
    """Viewport of the active framebuffer."""

def viewport_set(x: int, y, xsize: int, ysize) -> None:
    """Specifies the viewport of the active framebuffer.
    Note: The viewport state is not saved upon framebuffer rebind.

        :param x: lower left corner of the viewport_set rectangle, in pixels.
        :param xsize: width and height of the viewport_set.
    """
