import sys
import typing


def blend_depth_test_get():
    ''' Current depth_test equation.

    '''

    pass


def blend_get():
    ''' Current blending equation.

    '''

    pass


def blend_set(mode: str):
    ''' Defines the fixed pipeline blending equation.

    :param mode: The type of blend mode. * NONE No blending. * ALPHA The original color channels are interpolated according to the alpha value. * ALPHA_PREMULT The original color channels are interpolated according to the alpha value with the new colors pre-multiplied by this value. * ADDITIVE The original color channels are added by the corresponding ones. * ADDITIVE_PREMULT The original color channels are added by the corresponding ones that are pre-multiplied by the alpha value. * MULTIPLY The original color channels are multiplied by the corresponding ones. * SUBTRACT The original color channels are subtracted by the corresponding ones. * INVERT The original color channels are replaced by its complementary color.
    :type mode: str
    '''

    pass


def clip_distances_set(distances_enabled: int):
    ''' Sets the number of gl_ClipDistance planes used for clip geometry.

    :param distances_enabled: Number of clip distances enabled.
    :type distances_enabled: int
    '''

    pass


def color_mask_set(r: bool, g: bool, b: bool, a: bool):
    ''' Enable or disable writing of frame buffer color components.

    :param r: components red, green, blue, and alpha.
    :type r: bool
    :param g: components red, green, blue, and alpha.
    :type g: bool
    :param b: components red, green, blue, and alpha.
    :type b: bool
    :param a: components red, green, blue, and alpha.
    :type a: bool
    '''

    pass


def depth_mask_set(value):
    ''' Write to depth component.

    :type near: bool
    '''

    pass


def depth_mask_set_get():
    ''' Writing status in the depth component.

    '''

    pass


def depth_test_set(mode: str):
    ''' Defines the depth_test equation.

    :param mode: The depth test equation name. Possible values are NONE , ALWAYS , LESS , LESS_EQUAL , EQUAL , GREATER and GREATER_EQUAL .
    :type mode: str
    '''

    pass


def face_culling_set(culling):
    ''' Specify whether none, front-facing or back-facing facets can be culled.

    :param mode: NONE , FRONT or BACK .
    :type mode: str
    '''

    pass


def framebuffer_active_get(enable):
    ''' Return the active framefuffer in context.

    '''

    pass


def front_facing_set(invert):
    ''' Specifies the orientation of front-facing polygons.

    :type mode: bool
    '''

    pass


def line_width_get():
    ''' Current width of rasterized lines.

    '''

    pass


def line_width_set(width):
    ''' Specify the width of rasterized lines.

    :type mode: float
    '''

    pass


def point_size_set(size):
    ''' Specify the diameter of rasterized points.

    :type mode: float
    '''

    pass


def use_program_point_size(enable: bool):
    ''' If enabled, the derived point size is taken from the (potentially clipped) shader builtin gl_PointSize.

    :param enable: True for shader builtin gl_PointSize.
    :type enable: bool
    '''

    pass


def viewport_get():
    ''' Viewport of the active framebuffer.

    '''

    pass


def viewport_set(x: int, y: int, xsize: int, ysize: int):
    ''' Specifies the viewport of the active framebuffer. Note: The viewport state is not saved upon framebuffer rebind.

    :param x: lower left corner of the viewport_set rectangle, in pixels.
    :type x: int
    :param y: lower left corner of the viewport_set rectangle, in pixels.
    :type y: int
    :type xsize: int
    :type ysize: int
    '''

    pass
