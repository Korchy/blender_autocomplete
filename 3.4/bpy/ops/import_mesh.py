import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def ply(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
        hide_props_region: typing.Union[bool, typing.Any] = True,
        directory: typing.Union[str, typing.Any] = "",
        filter_glob: typing.Union[str, typing.Any] = "*.ply"):
    ''' Load a PLY geometry file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: typing.Union[str, typing.Any]
    :param files: File Path, File path used for importing the PLY file
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: typing.Union[bool, typing.Any]
    :param directory: directory
    :type directory: typing.Union[str, typing.Any]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    '''

    pass


def stl(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        filter_glob: typing.Union[str, typing.Any] = "*.stl",
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
        directory: typing.Union[str, typing.Any] = "",
        global_scale: typing.Optional[typing.Any] = 1.0,
        use_scene_unit: typing.Union[bool, typing.Any] = False,
        use_facet_normal: typing.Union[bool, typing.Any] = False,
        axis_forward: typing.Optional[typing.Any] = 'Y',
        axis_up: typing.Optional[typing.Any] = 'Z'):
    ''' Load STL triangle mesh data

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: typing.Union[str, typing.Any]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    :param files: File Path
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
    :param directory: directory
    :type directory: typing.Union[str, typing.Any]
    :param global_scale: Scale
    :type global_scale: typing.Optional[typing.Any]
    :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to imported data
    :type use_scene_unit: typing.Union[bool, typing.Any]
    :param use_facet_normal: Facet Normals, Use (import) facet normals (note that this will still give flat shading)
    :type use_facet_normal: typing.Union[bool, typing.Any]
    :param axis_forward: Forward
    :type axis_forward: typing.Optional[typing.Any]
    :param axis_up: Up
    :type axis_up: typing.Optional[typing.Any]
    '''

    pass
