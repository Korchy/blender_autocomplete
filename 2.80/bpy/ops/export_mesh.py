import sys
import typing


def ply(filepath: str = "",
        check_existing: bool = True,
        filter_glob: str = "*.ply",
        use_mesh_modifiers: bool = True,
        use_normals: bool = True,
        use_uv_coords: bool = True,
        use_colors: bool = True,
        global_scale: float = 1.0,
        axis_forward: int = 'Y',
        axis_up: int = 'Z'):
    '''Export a single object as a Stanford PLY with normals, colors and texture coordinates 

    :param filepath: File Path, Filepath used for exporting the file 
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: bool
    :param filter_glob: filter_glob 
    :type filter_glob: str
    :param use_mesh_modifiers: Apply Modifiers, Apply Modifiers to the exported mesh 
    :type use_mesh_modifiers: bool
    :param use_normals: Normals, Export Normals for smooth and hard shaded faces (hard shaded faces will be exported as individual faces) 
    :type use_normals: bool
    :param use_uv_coords: UVs, Export the active UV layer 
    :type use_uv_coords: bool
    :param use_colors: Vertex Colors, Export the active vertex color layer 
    :type use_colors: bool
    :param global_scale: Scale 
    :type global_scale: float
    :param axis_forward: Forward 
    :type axis_forward: int
    :param axis_up: Up 
    :type axis_up: int
    '''

    pass


def stl(filepath: str = "",
        check_existing: bool = True,
        filter_glob: str = "*.stl",
        use_selection: bool = False,
        global_scale: float = 1.0,
        use_scene_unit: bool = False,
        ascii: bool = False,
        use_mesh_modifiers: bool = True,
        batch_mode: int = 'OFF',
        axis_forward: int = 'Y',
        axis_up: int = 'Z'):
    '''Save STL triangle mesh data from the active object 

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
    :param use_scene_unit: Scene Unit, Apply current scene’s unit (as defined by unit scale) to exported data 
    :type use_scene_unit: bool
    :param ascii: Ascii, Save the file in ASCII file format 
    :type ascii: bool
    :param use_mesh_modifiers: Apply Modifiers, Apply the modifiers before saving 
    :type use_mesh_modifiers: bool
    :param batch_mode: Batch ModeOFF Off, All data in one file.OBJECT Object, Each object as a file. 
    :type batch_mode: int
    :param axis_forward: Forward 
    :type axis_forward: int
    :param axis_up: Up 
    :type axis_up: int
    '''

    pass
