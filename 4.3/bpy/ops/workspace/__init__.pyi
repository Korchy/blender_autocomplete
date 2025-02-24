import typing
import collections.abc
import typing_extensions

def add(execution_context: int | str | None = None, undo: bool | None = None):
    """Add a new workspace by duplicating the current one or appending one from the user configuration

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def append_activate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    idname: str = "",
    filepath: str = "",
):
    """Append a workspace and make it the active one in the current window

    :type execution_context: int | str | None
    :type undo: bool | None
    :param idname: Identifier, Name of the workspace to append and activate
    :type idname: str
    :param filepath: Filepath, Path to the library
    :type filepath: str
    """

def delete(execution_context: int | str | None = None, undo: bool | None = None):
    """Delete the active workspace

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def duplicate(execution_context: int | str | None = None, undo: bool | None = None):
    """Add a new workspace

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def reorder_to_back(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Reorder workspace to be last in the list

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def reorder_to_front(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Reorder workspace to be first in the list

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def scene_pin_toggle(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remember the last used scene for the current workspace and switch to it whenever this workspace is activated again

    :type execution_context: int | str | None
    :type undo: bool | None
    """
