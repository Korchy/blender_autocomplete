"""
This module provides access to Blender's text drawing functions.


--------------------

Example of using the blf module. For this module to work we
need to use the GPU module gpu as well.

```../examples/blf.0.py```


--------------------

Example showing how text can be drawn into an image.
This can be done by binding an image buffer (imbuf) to the font's ID.

```../examples/blf.1.py```

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import imbuf.types

def aspect(fontid: int, aspect: float) -> None:
    """Set the aspect for drawing text.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param aspect: The aspect ratio for non-uniform scaling of text.
    """

def bind_imbuf(
    fontid: int, imbuf: imbuf.types.ImBuf, *, display_name: None | str | None = None
) -> None:
    """Context manager to draw text into an image buffer instead of the GPUs context.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param imbuf: The image to draw into.
    :param display_name: Ignored (formerly a color-space transform name), kept for backwards compatibility.
    :return: The BLF ImBuf context manager.
    """

def clipping(fontid: int, xmin: float, ymin: float, xmax: float, ymax: float) -> None:
    """Set the clipping, enable/disable using `CLIPPING`.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param xmin: Left edge of the clipping rectangle.
    :param ymin: Bottom edge of the clipping rectangle.
    :param xmax: Right edge of the clipping rectangle.
    :param ymax: Top edge of the clipping rectangle.
    """

def color(fontid: int, r: float, g: float, b: float, a: float) -> None:
    """Set the color for drawing text.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param r: Red channel 0.0 - 1.0.
    :param g: Green channel 0.0 - 1.0.
    :param b: Blue channel 0.0 - 1.0.
    :param a: Alpha channel 0.0 - 1.0.
    """

def dimensions(fontid: int, text: str) -> tuple[float, float]:
    """Return the width and height of the text.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param text: The text to measure.
    :return: The width and height of the text.
    """

def disable(fontid: int, option: int) -> None:
    """Disable a font drawing option.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param option: One of `ROTATION`, `CLIPPING`, `SHADOW`, `MONOCHROME` or `WORD_WRAP`.
    """

def draw(fontid: int, text: str) -> None:
    """Draw text in the current context.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param text: The text to draw.
    """

def draw_buffer(fontid: int, text: str) -> None:
    """Draw text into the image buffer bound via `blf.bind_imbuf`.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param text: The text to draw into the bound image buffer.
    """

def enable(fontid: int, option: int) -> None:
    """Enable a font drawing option.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param option: One of `ROTATION`, `CLIPPING`, `SHADOW`, `MONOCHROME` or `WORD_WRAP`.
    """

def load(filepath: bytes | str) -> int:
    """Load a new font.

    :param filepath: The filepath of the font.
    :return: The new fonts fontid or -1 if there was an error.
    """

def position(fontid: int, x: float, y: float, z: float) -> None:
    """Set the position for drawing text.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param x: X axis position to draw the text.
    :param y: Y axis position to draw the text.
    :param z: Z axis position to draw the text (typically 0).
    """

def rotation(fontid: int, angle: float) -> None:
    """Set the text rotation angle, enable/disable using `ROTATION`.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param angle: The angle for text drawing to use (in radians).
    """

def shadow(fontid: int, level: int, r: float, g: float, b: float, a: float) -> None:
    """Shadow options, enable/disable using `SHADOW`.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param level: The shadow type: 0 for none, 3 for 3x3 blur, 5 for 5x5 blur or 6 for outline. Other values raise a `TypeError`.
    :param r: Shadow color (red channel 0.0 - 1.0).
    :param g: Shadow color (green channel 0.0 - 1.0).
    :param b: Shadow color (blue channel 0.0 - 1.0).
    :param a: Shadow color (alpha channel 0.0 - 1.0).
    """

def shadow_offset(fontid: int, x: int, y: int) -> None:
    """Set the offset for shadow text, enable/disable using `SHADOW`.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param x: Horizontal shadow offset value in pixels.
    :param y: Vertical shadow offset value in pixels.
    """

def size(fontid: int, size: float) -> None:
    """Set the size for drawing text.

    :param fontid: The id of the typeface as returned by `blf.load`, for default font use 0.
    :param size: Point size of the font.
    """

def unload(filepath: bytes | str) -> None:
    """Unload an existing font.

    :param filepath: The filepath of the font.
    """

def word_wrap(fontid: int, wrap_width: int) -> None:
    """Set the wrap width, enable/disable using `WORD_WRAP`.

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
