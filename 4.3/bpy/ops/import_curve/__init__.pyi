import typing
import collections.abc
import typing_extensions

def svg(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    filter_glob: str = "*.svg",
):
    """Load a SVG file

    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: str
    :param filter_glob: filter_glob
    :type filter_glob: str
    """
