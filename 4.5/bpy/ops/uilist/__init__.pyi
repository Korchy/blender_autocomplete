import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def entry_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    list_path: str = "",
    active_index_path: str = "",
) -> None:
    """Add an entry to the list after the current active item

    :param list_path: list_path
    :param active_index_path: active_index_path
    """

def entry_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    list_path: str = "",
    active_index_path: str = "",
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move an entry in the list up or down

        :param list_path: list_path
        :param active_index_path: active_index_path
        :param direction: Direction

    UP
    UP -- UP.

    DOWN
    DOWN -- DOWN.
    """

def entry_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    list_path: str = "",
    active_index_path: str = "",
) -> None:
    """Remove the selected entry from the list

    :param list_path: list_path
    :param active_index_path: active_index_path
    """
