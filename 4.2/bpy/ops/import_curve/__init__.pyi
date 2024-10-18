import typing
import collections.abc
import typing_extensions
import bpy.types

def svg(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    filter_glob: str = "*.svg",
):
    """Load a SVG file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: str
    :param filter_glob: filter_glob
    :type filter_glob: str
    """
