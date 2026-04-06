"""
The Blender Freestyle.ContextFunctions submodule

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import freestyle.types

def get_border() -> tuple[int, int, int, int]:
    """Returns the border.

    :return: A tuple of 4 numbers (xmin, ymin, xmax, ymax).
    """

def get_canvas_height() -> int:
    """Returns the canvas height.

    :return: The canvas height.
    """

def get_canvas_width() -> int:
    """Returns the canvas width.

    :return: The canvas width.
    """

def get_selected_fedge() -> freestyle.types.FEdge:
    """Returns the selected FEdge.

    :return: The selected FEdge.
    """

def get_time_stamp() -> int:
    """Returns the system time stamp.

    :return: The system time stamp.
    """

def load_map(
    file_name: str, map_name: str, num_levels: int = 4, sigma: float = 1.0
) -> None:
    """Loads an image map for further reading.

        :param file_name: The name of the image file.
        :param map_name: The name that will be used to access this image.
        :param num_levels: The number of levels in the map pyramid
    (default = 4). If num_levels == 0, the complete pyramid is
    built.
        :param sigma: The sigma value of the gaussian function.
    """

def read_complete_view_map_pixel(level: int, x: int, y: int) -> float:
    """Reads a pixel in the complete view map.

        :param level: The level of the pyramid in which we wish to read the
    pixel.
        :param x: The x coordinate of the pixel we wish to read. The origin
    is in the lower-left corner.
        :param y: The y coordinate of the pixel we wish to read. The origin
    is in the lower-left corner.
        :return: The floating-point value stored for that pixel.
    """

def read_directional_view_map_pixel(
    orientation: int, level: int, x: int, y: int
) -> float:
    """Reads a pixel in one of the oriented view map images.

        :param orientation: The number telling which orientation we want to
    check.
        :param level: The level of the pyramid in which we wish to read the
    pixel.
        :param x: The x coordinate of the pixel we wish to read. The origin
    is in the lower-left corner.
        :param y: The y coordinate of the pixel we wish to read. The origin
    is in the lower-left corner.
        :return: The floating-point value stored for that pixel.
    """

def read_map_pixel(map_name: str, level: int, x: int, y: int) -> float:
    """Reads a pixel in a user-defined map.

        :param map_name: The name of the map.
        :param level: The level of the pyramid in which we wish to read the
    pixel.
        :param x: The x coordinate of the pixel we wish to read. The origin
    is in the lower-left corner.
        :param y: The y coordinate of the pixel we wish to read. The origin
    is in the lower-left corner.
        :return: The floating-point value stored for that pixel.
    """
