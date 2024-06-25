import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def stl(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    filter_glob: str | typing.Any = "*.stl",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    directory: str | typing.Any = "",
    global_scale: typing.Any | None = 1.0,
    use_scene_unit: bool | typing.Any | None = False,
    use_facet_normal: bool | typing.Any | None = False,
    axis_forward: str | None = "Y",
    axis_up: str | None = "Z",
):
    """Load STL triangle mesh data

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: str | typing.Any
    :param filter_glob: filter_glob
    :type filter_glob: str | typing.Any
    :param files: File Path
    :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
    :param directory: directory
    :type directory: str | typing.Any
    :param global_scale: Scale
    :type global_scale: typing.Any | None
    :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to imported data
    :type use_scene_unit: bool | typing.Any | None
    :param use_facet_normal: Facet Normals, Use (import) facet normals (note that this will still give flat shading)
    :type use_facet_normal: bool | typing.Any | None
    :param axis_forward: Forward
    :type axis_forward: str | None
    :param axis_up: Up
    :type axis_up: str | None
    """

    ...
