import sys
import typing

GenericType = typing.TypeVar("GenericType")


def aspect(fontid: int, aspect: float):
    ''' Set the aspect for drawing text.

    :param fontid: `blf.load`, for default font use 0.
    :type fontid: int
    :param aspect: The aspect ratio for text drawing to use.
    :type aspect: float
    '''

    pass


def clipping(fontid: int, xmin: float, ymin: float, xmax: float, ymax: float):
    ''' Set the clipping, enable/disable using CLIPPING.

    :param fontid: `blf.load`, for default font use 0.
    :type fontid: int
    :param xmin: Clip the drawing area by these bounds.
    :type xmin: float
    :param ymin: Clip the drawing area by these bounds.
    :type ymin: float
    :param xmax: Clip the drawing area by these bounds.
    :type xmax: float
    :param ymax: Clip the drawing area by these bounds.
    :type ymax: float
    '''

    pass


def color(fontid: int, r: float, g: float, b: float, a: float):
    ''' Set the color for drawing text.

    :param fontid: `blf.load`, for default font use 0.
    :type fontid: int
    :param r: red channel 0.0 - 1.0.
    :type r: float
    :param g: green channel 0.0 - 1.0.
    :type g: float
    :param b: blue channel 0.0 - 1.0.
    :type b: float
    :param a: alpha channel 0.0 - 1.0.
    :type a: float
    '''

    pass


def dimensions(fontid: int, text: str) -> typing.Tuple:
    ''' Return the width and height of the text.

    :param fontid: `blf.load`, for default font use 0.
    :type fontid: int
    :param text: the text to draw.
    :type text: str
    :rtype: typing.Tuple
    :return: the width and height of the text.
    '''

    pass


def disable(fontid: int, option: int):
    ''' Disable option.

    :param fontid: `blf.load`, for default font use 0.
    :type fontid: int
    :param option: One of ROTATION, CLIPPING, SHADOW or KERNING_DEFAULT.
    :type option: int
    '''

    pass


def draw(fontid: int, text: str):
    ''' Draw text in the current context.

    :param fontid: `blf.load`, for default font use 0.
    :type fontid: int
    :param text: the text to draw.
    :type text: str
    '''

    pass


def enable(fontid: int, option: int):
    ''' Enable option.

    :param fontid: `blf.load`, for default font use 0.
    :type fontid: int
    :param option: One of ROTATION, CLIPPING, SHADOW or KERNING_DEFAULT.
    :type option: int
    '''

    pass


def load(filepath: typing.Union[str, bytes]) -> typing.Any:
    ''' Load a new font.

    :param filepath: the filepath of the font.
    :type filepath: typing.Union[str, bytes]
    :rtype: typing.Any
    :return: the new font's fontid or -1 if there was an error.
    '''

    pass


def position(fontid: int, x: float, y: float, z: float):
    ''' Set the position for drawing text.

    :param fontid: `blf.load`, for default font use 0.
    :type fontid: int
    :param x: X axis position to draw the text.
    :type x: float
    :param y: Y axis position to draw the text.
    :type y: float
    :param z: Z axis position to draw the text.
    :type z: float
    '''

    pass


def rotation(fontid: int, angle: float):
    ''' Set the text rotation angle, enable/disable using ROTATION.

    :param fontid: `blf.load`, for default font use 0.
    :type fontid: int
    :param angle: The angle for text drawing to use.
    :type angle: float
    '''

    pass


def shadow(fontid: int, level: int, r: float, g: float, b: float, a: float):
    ''' Shadow options, enable/disable using SHADOW .

    :param fontid: `blf.load`, for default font use 0.
    :type fontid: int
    :param level: The blur level, can be 3, 5 or 0.
    :type level: int
    :param r: Shadow color (red channel 0.0 - 1.0).
    :type r: float
    :param g: Shadow color (green channel 0.0 - 1.0).
    :type g: float
    :param b: Shadow color (blue channel 0.0 - 1.0).
    :type b: float
    :param a: Shadow color (alpha channel 0.0 - 1.0).
    :type a: float
    '''

    pass


def shadow_offset(fontid: int, x: float, y: float):
    ''' Set the offset for shadow text.

    :param fontid: `blf.load`, for default font use 0.
    :type fontid: int
    :param x: Vertical shadow offset value in pixels.
    :type x: float
    :param y: Horizontal shadow offset value in pixels.
    :type y: float
    '''

    pass


def size(fontid: int, size: float):
    ''' Set the size for drawing text.

    :param fontid: `blf.load`, for default font use 0.
    :type fontid: int
    :param size: Point size of the font.
    :type size: float
    '''

    pass


def unload(filepath: typing.Union[str, bytes]):
    ''' Unload an existing font.

    :param filepath: the filepath of the font.
    :type filepath: typing.Union[str, bytes]
    '''

    pass


def word_wrap(fontid: int, wrap_width: int):
    ''' Set the wrap width, enable/disable using WORD_WRAP.

    :param fontid: `blf.load`, for default font use 0.
    :type fontid: int
    :param wrap_width: The width (in pixels) to wrap words at.
    :type wrap_width: int
    '''

    pass


CLIPPING = None
''' Constant value 2
'''

MONOCHROME = None
''' Constant value 128
'''

ROTATION = None
''' Constant value 1
'''

SHADOW = None
''' Constant value 4
'''

WORD_WRAP = None
''' Constant value 64
'''
