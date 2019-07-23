import sys
import typing
import bpy


def ply(filepath: str = "",
        files: typing.List['bpy.types.OperatorFileListElement'] = None,
        directory: str = "",
        filter_glob: str = "*.ply"):
    '''Load a PLY geometry file 

    :param filepath: File Path, Filepath used for importing the file 
    :type filepath: str
    :param files: File Path, File path used for importing the PLY file 
    :type files: typing.List['bpy.types.OperatorFileListElement']
    :param directory: directory 
    :type directory: str
    :param filter_glob: filter_glob 
    :type filter_glob: str
    '''

    pass


def stl(filepath: str = "",
        filter_glob: str = "*.stl",
        files: typing.List['bpy.types.OperatorFileListElement'] = None,
        directory: str = "",
        global_scale: float = 1.0,
        use_scene_unit: bool = False,
        use_facet_normal: bool = False,
        axis_forward: int = 'Y',
        axis_up: int = 'Z'):
    '''Load STL triangle mesh data 

    :param filepath: File Path, Filepath used for importing the file 
    :type filepath: str
    :param filter_glob: filter_glob 
    :type filter_glob: str
    :param files: File Path 
    :type files: typing.List['bpy.types.OperatorFileListElement']
    :param directory: directory 
    :type directory: str
    :param global_scale: Scale 
    :type global_scale: float
    :param use_scene_unit: Scene Unit, Apply current scene’s unit (as defined by unit scale) to imported data 
    :type use_scene_unit: bool
    :param use_facet_normal: Facet Normals, Use (import) facet normals (note that this will still give flat shading) 
    :type use_facet_normal: bool
    :param axis_forward: Forward 
    :type axis_forward: int
    :param axis_up: Up 
    :type axis_up: int
    '''

    pass
