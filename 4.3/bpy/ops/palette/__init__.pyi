import typing
import collections.abc
import typing_extensions

def color_add(execution_context: int | str | None = None, undo: bool | None = None):
    """Add new color to active palette

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def color_delete(execution_context: int | str | None = None, undo: bool | None = None):
    """Remove active color from palette

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def color_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move the active Color up/down in the list

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['UP','DOWN'] | None
    """

def extract_from_image(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    threshold: int | None = 1,
):
    """Extract all colors used in Image and create a Palette

    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Threshold
    :type threshold: int | None
    """

def join(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    palette: str = "",
):
    """Join Palette Swatches

    :type execution_context: int | str | None
    :type undo: bool | None
    :param palette: Palette, Name of the Palette
    :type palette: str
    """

def new(execution_context: int | str | None = None, undo: bool | None = None):
    """Add new palette

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def sort(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["HSV", "SVH", "VHS", "LUMINANCE"] | None = "HSV",
):
    """Sort Palette Colors

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['HSV','SVH','VHS','LUMINANCE'] | None
    """
