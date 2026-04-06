import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a new workspace by duplicating the current one or appending one from the user configuration"""

def append_activate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    idname: str = "",
    filepath: str | None = "",
) -> None:
    """Append a workspace and make it the active one in the current window

    :param idname: Identifier, Name of the workspace to append and activate
    :param filepath: Filepath, Path to the library
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete the active workspace"""

def delete_all_others(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete all workspaces except this one"""

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a new workspace"""

def reorder_to_back(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reorder workspace to be last in the list"""

def reorder_to_front(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reorder workspace to be first in the list"""

def scene_pin_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remember the last used scene for the current workspace and switch to it whenever this workspace is activated again"""
