"""
This module provides access to the gpu state.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import gpu.types

def active_framebuffer_get() -> gpu.types.GPUFrameBuffer:
    """Return the active frame-buffer in context.

    :return: The active framebuffer.
    """

def blend_get() -> str:
    """Current blending equation.

    :return: The current blend mode.
    """

def blend_set(
    mode: typing.Literal[
        "NONE",
        "ALPHA",
        "ALPHA_PREMULT",
        "ADDITIVE",
        "ADDITIVE_PREMULT",
        "MULTIPLY",
        "SUBTRACT",
        "INVERT",
    ],
) -> None:
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

def color_mask_set(r: bool, g: bool, b: bool, a: bool) -> None:
    """Enable or disable writing of frame buffer color components.

    :param r: Red component.
    :param g: Green component.
    :param b: Blue component.
    :param a: Alpha component.
    """

def depth_mask_get() -> bool:
    """Writing status in the depth component.

    :return: True if writing to the depth component is enabled.
    """

def depth_mask_set(value: bool) -> None:
    """Write to depth component.

    :param value: True for writing to the depth component.
    """

def depth_test_get() -> str:
    """Current depth_test equation.

    :return: The current depth test mode.
    """

def depth_test_set(
    mode: typing.Literal[
        "NONE", "ALWAYS", "LESS", "LESS_EQUAL", "EQUAL", "GREATER", "GREATER_EQUAL"
    ],
) -> None:
    """Defines the depth_test equation.

    :param mode: The depth test equation name.
    """

def face_culling_set(culling: typing.Literal["NONE", "FRONT", "BACK"]) -> None:
    """Specify whether none, front-facing or back-facing facets can be culled.

    :param culling: The face culling mode.
    """

def front_facing_set(invert: bool) -> None:
    """Specifies the orientation of front-facing polygons.

    :param invert: True for clockwise polygons as front-facing.
    """

def line_width_get() -> float:
    """Current width of rasterized lines.

    :return: The current line width.
    """

def line_width_set(width: float) -> None:
    """Specify the width of rasterized lines.

    :param width: New width.
    """

def point_size_set(size: float) -> None:
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

def scissor_set(x: int, y: int, xsize: int, ysize: int) -> None:
    """Specifies the scissor area of the active framebuffer.
    Note: The scissor state is not saved upon framebuffer rebind.

        :param x: Lower left corner x coordinate, in pixels.
        :param y: Lower left corner y coordinate, in pixels.
        :param xsize: Width of the scissor rectangle.
        :param ysize: Height of the scissor rectangle.
    """

def scissor_test_set(enable: bool) -> None:
    """Enable/disable scissor testing on the active framebuffer.

        :param enable: True - enable scissor testing.
    False - disable scissor testing.
    """

def viewport_get() -> tuple[int, int, int, int]:
    """Viewport of the active framebuffer.

    :return: The viewport as a tuple (x, y, xsize, ysize).
    """

def viewport_set(x: int, y: int, xsize: int, ysize: int) -> None:
    """Specifies the viewport of the active framebuffer.
    Note: The viewport state is not saved upon framebuffer rebind.

        :param x: Lower left corner x coordinate, in pixels.
        :param y: Lower left corner y coordinate, in pixels.
        :param xsize: Width of the viewport.
        :param ysize: Height of the viewport.
    """
