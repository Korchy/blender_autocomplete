import typing
import collections.abc
import typing_extensions

def new(execution_context: int | str | None = None, undo: bool | None = None):
    """Add a new texture

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def slot_copy(execution_context: int | str | None = None, undo: bool | None = None):
    """Copy the material texture settings and nodes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def slot_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move texture slots up and down

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['UP','DOWN'] | None
    """

def slot_paste(execution_context: int | str | None = None, undo: bool | None = None):
    """Copy the texture settings and nodes

    :type execution_context: int | str | None
    :type undo: bool | None
    """
