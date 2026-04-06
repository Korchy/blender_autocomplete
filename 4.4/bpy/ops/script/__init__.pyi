import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def execute_preset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    menu_idname: str = "",
) -> None:
    """Load a preset

    :param filepath: filepath
    :param menu_idname: Menu ID Name, ID name of the menu this was called from
    """

def python_file_run(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
) -> None:
    """Run Python file

    :param filepath: Path
    """

def reload(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reload scripts"""
