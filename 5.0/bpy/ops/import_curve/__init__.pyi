import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

def svg(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    filter_glob: str = "*.svg",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
) -> None:
    """Load a SVG file

    :param filepath: File Path, Filepath used for importing the file
    :param filter_glob: filter_glob
    :param directory: directory
    :param files: File Path
    """
