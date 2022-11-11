import sys
import typing
import bpy.types
import mathutils

GenericType = typing.TypeVar("GenericType")


def ply(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        filepath: str = "",
        check_existing: bool = True,
        filter_glob: str = "*.ply",
        use_ascii: bool = False,
        use_selection: bool = False,
        use_mesh_modifiers: bool = True,
        use_normals: bool = True,
        use_uv_coords: bool = True,
        use_colors: bool = True,
        global_scale: float = 1.0,
        axis_forward: typing.Union[str, int] = 'Y',
        axis_up: typing.Union[str, int] = 'Z'):
    ''' Export as a Stanford PLY with normals, vertex colors and texture coordinates

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Filepath used for exporting the file
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_glob: filter_glob
    :type filter_glob: str
    :param use_ascii: ASCII, Export using ASCII file format, otherwise use binary
    :type use_ascii: bool
    :param use_selection: Selection Only, Export selected objects only
    :type use_selection: bool
    :param use_mesh_modifiers: Apply Modifiers, Apply Modifiers to the exported mesh
    :type use_mesh_modifiers: bool
    :param use_normals: Normals, Export vertex normals
    :type use_normals: bool
    :param use_uv_coords: UVs, Export the active UV layer (will split edges by seams)
    :type use_uv_coords: bool
    :param use_colors: Vertex Colors, Export the active vertex color layer
    :type use_colors: bool
    :param global_scale: Scale
    :type global_scale: float
    :param axis_forward: Forward
    :type axis_forward: typing.Union[str, int]
    :param axis_up: Up
    :type axis_up: typing.Union[str, int]
    '''

    pass


def stl(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        filepath: str = "",
        check_existing: bool = True,
        filter_glob: str = "*.stl",
        use_selection: bool = False,
        global_scale: float = 1.0,
        use_scene_unit: bool = False,
        ascii: bool = False,
        use_mesh_modifiers: bool = True,
        batch_mode: typing.Union[str, int] = 'OFF',
        global_space: typing.
        Union[typing.List[typing.List[float]], typing.
              Tuple[typing.Tuple[float, float, float, float], typing.
                    Tuple[float, float, float, float], typing.
                    Tuple[float, float, float, float], typing.
                    Tuple[float, float, float, float]], 'mathutils.Matrix'] = (
                        (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0),
                        (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)),
        axis_forward: typing.Union[str, int] = 'Y',
        axis_up: typing.Union[str, int] = 'Z'):
    ''' Save STL triangle mesh data

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Filepath used for exporting the file
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_glob: filter_glob
    :type filter_glob: str
    :param use_selection: Selection Only, Export selected objects only
    :type use_selection: bool
    :param global_scale: Scale
    :type global_scale: float
    :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to exported data
    :type use_scene_unit: bool
    :param ascii: Ascii, Save the file in ASCII file format
    :type ascii: bool
    :param use_mesh_modifiers: Apply Modifiers, Apply the modifiers before saving
    :type use_mesh_modifiers: bool
    :param batch_mode: Batch Mode * OFF Off -- All data in one file. * OBJECT Object -- Each object as a file.
    :type batch_mode: typing.Union[str, int]
    :param global_space: Global Space, Export in this reference space
    :type global_space: typing.Union[typing.List[typing.List[float]], typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]], 'mathutils.Matrix']
    :param axis_forward: Forward
    :type axis_forward: typing.Union[str, int]
    :param axis_up: Up
    :type axis_up: typing.Union[str, int]
    '''

    pass
