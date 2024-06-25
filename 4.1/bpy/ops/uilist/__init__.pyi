import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def entry_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    list_path: str | typing.Any = "",
    active_index_path: str | typing.Any = "",
):
    """Add an entry to the list after the current active item

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param list_path: list_path
    :type list_path: str | typing.Any
    :param active_index_path: active_index_path
    :type active_index_path: str | typing.Any
    """

    ...

def entry_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    list_path: str | typing.Any = "",
    active_index_path: str | typing.Any = "",
    direction: str | None = "UP",
):
    """Move an entry in the list up or down

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param list_path: list_path
        :type list_path: str | typing.Any
        :param active_index_path: active_index_path
        :type active_index_path: str | typing.Any
        :param direction: Direction

    UP
    UP -- UP.

    DOWN
    DOWN -- DOWN.
        :type direction: str | None
    """

    ...

def entry_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    list_path: str | typing.Any = "",
    active_index_path: str | typing.Any = "",
):
    """Remove the selected entry from the list

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param list_path: list_path
    :type list_path: str | typing.Any
    :param active_index_path: active_index_path
    :type active_index_path: str | typing.Any
    """

    ...
