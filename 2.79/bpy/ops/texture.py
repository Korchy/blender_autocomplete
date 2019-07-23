import sys
import typing


def envmap_clear():
    '''Discard the environment map and free it from memory 

    '''

    pass


def envmap_clear_all():
    '''Discard all environment maps in the .blend file and free them from memory 

    '''

    pass


def envmap_save(layout: float = (0.0, 0.0, 1.0, 0.0, 2.0, 0.0, 0.0, 1.0, 1.0,
                                 1.0, 2.0, 1.0),
                filepath: str = "",
                check_existing: bool = True,
                filter_blender: bool = False,
                filter_backup: bool = False,
                filter_image: bool = True,
                filter_movie: bool = True,
                filter_python: bool = False,
                filter_font: bool = False,
                filter_sound: bool = False,
                filter_text: bool = False,
                filter_btx: bool = False,
                filter_collada: bool = False,
                filter_alembic: bool = False,
                filter_folder: bool = True,
                filter_blenlib: bool = False,
                filemode: int = 9,
                show_multiview: bool = False,
                use_multiview: bool = False,
                display_type: int = 'DEFAULT',
                sort_method: int = 'FILE_SORT_ALPHA'):
    '''Save the current generated Environment map to an image file 

    :param layout: File layout, Flat array describing the X,Y position of each cube face in the output image, where 1 is the size of a face - order is [+Z -Z +Y -X -Y +X] (use -1 to skip a face) 
    :type layout: float
    :param filepath: File Path, Path to file 
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: bool
    :param filter_blender: Filter .blend files 
    :type filter_blender: bool
    :param filter_backup: Filter .blend files 
    :type filter_backup: bool
    :param filter_image: Filter image files 
    :type filter_image: bool
    :param filter_movie: Filter movie files 
    :type filter_movie: bool
    :param filter_python: Filter python files 
    :type filter_python: bool
    :param filter_font: Filter font files 
    :type filter_font: bool
    :param filter_sound: Filter sound files 
    :type filter_sound: bool
    :param filter_text: Filter text files 
    :type filter_text: bool
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param show_multiview: Enable Multi-View 
    :type show_multiview: bool
    :param use_multiview: Use Multi-View 
    :type use_multiview: bool
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    '''

    pass


def new():
    '''Add a new texture 

    '''

    pass


def slot_copy():
    '''Copy the material texture settings and nodes 

    '''

    pass


def slot_move(type: int = 'UP'):
    '''Move texture slots up and down 

    :param type: Type 
    :type type: int
    '''

    pass


def slot_paste():
    '''Copy the texture settings and nodes 

    '''

    pass
