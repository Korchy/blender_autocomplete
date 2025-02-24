import typing
import collections.abc
import typing_extensions

def entry_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    list_path: str = "",
    active_index_path: str = "",
):
    """Add an entry to the list after the current active item

    :type execution_context: int | str | None
    :type undo: bool | None
    :param list_path: list_path
    :type list_path: str
    :param active_index_path: active_index_path
    :type active_index_path: str
    """

def entry_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    list_path: str = "",
    active_index_path: str = "",
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move an entry in the list up or down

        :type execution_context: int | str | None
        :type undo: bool | None
        :param list_path: list_path
        :type list_path: str
        :param active_index_path: active_index_path
        :type active_index_path: str
        :param direction: Direction

    UP
    UP -- UP.

    DOWN
    DOWN -- DOWN.
        :type direction: typing.Literal['UP','DOWN'] | None
    """

def entry_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    list_path: str = "",
    active_index_path: str = "",
):
    """Remove the selected entry from the list

    :type execution_context: int | str | None
    :type undo: bool | None
    :param list_path: list_path
    :type list_path: str
    :param active_index_path: active_index_path
    :type active_index_path: str
    """
