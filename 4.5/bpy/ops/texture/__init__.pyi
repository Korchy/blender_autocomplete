import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a new texture"""

def slot_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the material texture settings and nodes"""

def slot_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move texture slots up and down

    :param type: Type
    """

def slot_paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the texture settings and nodes"""
