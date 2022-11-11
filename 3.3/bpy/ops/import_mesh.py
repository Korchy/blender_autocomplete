import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def ply(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        filepath: str = "",
        files: bpy.types.
        bpy_prop_collection['bpy.types.OperatorFileListElement'] = None,
        hide_props_region: bool = True,
        directory: str = "",
        filter_glob: str = "*.ply"):
    ''' Load a PLY geometry file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: str
    :param files: File Path, File path used for importing the PLY file
    :type files: bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: bool
    :param directory: directory
    :type directory: str
    :param filter_glob: filter_glob
    :type filter_glob: str
    '''

    pass


def stl(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        filepath: str = "",
        filter_glob: str = "*.stl",
        files: bpy.types.
        bpy_prop_collection['bpy.types.OperatorFileListElement'] = None,
        directory: str = "",
        global_scale: float = 1.0,
        use_scene_unit: bool = False,
        use_facet_normal: bool = False,
        axis_forward: typing.Union[str, int] = 'Y',
        axis_up: typing.Union[str, int] = 'Z'):
    ''' Load STL triangle mesh data

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: str
    :param filter_glob: filter_glob
    :type filter_glob: str
    :param files: File Path
    :type files: bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']
    :param directory: directory
    :type directory: str
    :param global_scale: Scale
    :type global_scale: float
    :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to imported data
    :type use_scene_unit: bool
    :param use_facet_normal: Facet Normals, Use (import) facet normals (note that this will still give flat shading)
    :type use_facet_normal: bool
    :param axis_forward: Forward
    :type axis_forward: typing.Union[str, int]
    :param axis_up: Up
    :type axis_up: typing.Union[str, int]
    '''

    pass
