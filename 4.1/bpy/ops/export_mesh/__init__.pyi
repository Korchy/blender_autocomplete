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
    check_existing: bool | typing.Any | None = True,
    filter_glob: str | typing.Any = "*.stl",
    use_selection: bool | typing.Any | None = False,
    global_scale: typing.Any | None = 1.0,
    use_scene_unit: bool | typing.Any | None = False,
    ascii: bool | typing.Any | None = False,
    use_mesh_modifiers: bool | typing.Any | None = True,
    batch_mode: str | None = "OFF",
    global_space: typing.Any | None = (
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
    ),
    axis_forward: str | None = "Y",
    axis_up: str | None = "Z",
):
    """Save STL triangle mesh data

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Filepath used for exporting the file
        :type filepath: str | typing.Any
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_glob: filter_glob
        :type filter_glob: str | typing.Any
        :param use_selection: Selection Only, Export selected objects only
        :type use_selection: bool | typing.Any | None
        :param global_scale: Scale
        :type global_scale: typing.Any | None
        :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to exported data
        :type use_scene_unit: bool | typing.Any | None
        :param ascii: Ascii, Save the file in ASCII file format
        :type ascii: bool | typing.Any | None
        :param use_mesh_modifiers: Apply Modifiers, Apply the modifiers before saving
        :type use_mesh_modifiers: bool | typing.Any | None
        :param batch_mode: Batch Mode

    OFF
    Off -- All data in one file.

    OBJECT
    Object -- Each object as a file.
        :type batch_mode: str | None
        :param global_space: Global Space, Export in this reference space
        :type global_space: typing.Any | None
        :param axis_forward: Forward
        :type axis_forward: str | None
        :param axis_up: Up
        :type axis_up: str | None
    """

    ...
