"""
This module provides access to Blender's text drawing functions.


--------------------

Example of using the blf module. For this module to work we
need to use the GPU module gpu as well.

```../examples/blf.py```

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def aspect(fontid: int, aspect: float) -> None:
    """Set the aspect for drawing text.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param aspect: The aspect ratio for text drawing to use.
    """

def clipping(fontid: int, xmin: float, ymin: float, xmax: float, ymax: float) -> None:
    """Set the clipping, enable/disable using CLIPPING.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param xmin: Clip the drawing area by these bounds.
    :param ymin: Clip the drawing area by these bounds.
    :param xmax: Clip the drawing area by these bounds.
    :param ymax: Clip the drawing area by these bounds.
    """

def color(fontid: int, r: float, g: float, b: float, a: float) -> None:
    """Set the color for drawing text.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param r: red channel 0.0 - 1.0.
    :param g: green channel 0.0 - 1.0.
    :param b: blue channel 0.0 - 1.0.
    :param a: alpha channel 0.0 - 1.0.
    """

def dimensions(fontid: int, text: str) -> tuple[float, float]:
    """Return the width and height of the text.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param text: the text to draw.
    :return: the width and height of the text.
    """

def disable(fontid: int, option: int) -> None:
    """Disable option.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param option: One of ROTATION, CLIPPING, SHADOW or KERNING_DEFAULT.
    """

def draw(fontid: int, text: str) -> None:
    """Draw text in the current context.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param text: the text to draw.
    """

def enable(fontid: int, option: int) -> None:
    """Enable option.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param option: One of ROTATION, CLIPPING, SHADOW or KERNING_DEFAULT.
    """

def load(filepath: bytes | str) -> int:
    """Load a new font.

    :param filepath: the filepath of the font.
    :return: the new fonts fontid or -1 if there was an error.
    """

def position(fontid: int, x: float, y: float, z: float) -> None:
    """Set the position for drawing text.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param x: X axis position to draw the text.
    :param y: Y axis position to draw the text.
    :param z: Z axis position to draw the text.
    """

def rotation(fontid: int, angle: float) -> None:
    """Set the text rotation angle, enable/disable using ROTATION.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param angle: The angle for text drawing to use.
    """

def shadow(fontid: int, level: int, r: float, g: float, b: float, a: float) -> None:
    """Shadow options, enable/disable using SHADOW .

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param level: The blur level (0, 3, 5) or outline (6).
    :param r: Shadow color (red channel 0.0 - 1.0).
    :param g: Shadow color (green channel 0.0 - 1.0).
    :param b: Shadow color (blue channel 0.0 - 1.0).
    :param a: Shadow color (alpha channel 0.0 - 1.0).
    """

def shadow_offset(fontid: int, x: float, y: float) -> None:
    """Set the offset for shadow text.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param x: Vertical shadow offset value in pixels.
    :param y: Horizontal shadow offset value in pixels.
    """

def size(fontid: int, size: float) -> None:
    """Set the size for drawing text.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param size: Point size of the font.
    """

def unload(filepath: bytes | str) -> None:
    """Unload an existing font.

    :param filepath: the filepath of the font.
    """

def word_wrap(fontid: int, wrap_width: int) -> None:
    """Set the wrap width, enable/disable using WORD_WRAP.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param wrap_width: The width (in pixels) to wrap words at.
    """

CLIPPING: typing.Any
""" Constant value 2
"""

MONOCHROME: typing.Any
""" Constant value 128
"""

ROTATION: typing.Any
""" Constant value 1
"""

SHADOW: typing.Any
""" Constant value 4
"""

WORD_WRAP: typing.Any
""" Constant value 64
"""
