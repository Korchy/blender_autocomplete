import sys
import typing


def autopack_toggle():
    '''Automatically pack all external files into the .blend file 

    '''

    pass


def bookmark_add():
    '''Add a bookmark for the selected/active directory 

    '''

    pass


def bookmark_cleanup():
    '''Delete all invalid bookmarks 

    '''

    pass


def bookmark_delete(index: int = -1):
    '''Delete selected bookmark 

    :param index: Index 
    :type index: int
    '''

    pass


def bookmark_move(direction: int = 'TOP'):
    '''Move the active bookmark up/down in the list 

    :param direction: Direction, Direction to move the active bookmark towardsTOP Top, Top of the list.UP Up.DOWN Down.BOTTOM Bottom, Bottom of the list. 
    :type direction: int
    '''

    pass


def bookmark_toggle():
    '''Toggle bookmarks display 

    '''

    pass


def cancel():
    '''Cancel loading of selected file 

    '''

    pass


def delete():
    '''Delete selected files 

    '''

    pass


def directory_new(directory: str = "", open: bool = False):
    '''Create a new directory 

    :param directory: Directory, Name of new directory 
    :type directory: str
    :param open: Open, Open new directory 
    :type open: bool
    '''

    pass


def execute(need_active: bool = False):
    '''Execute selected file 

    :param need_active: Need Active, Only execute if there’s an active selected file in the file list 
    :type need_active: bool
    '''

    pass


def filenum(increment: int = 1):
    '''Increment number in filename 

    :param increment: Increment 
    :type increment: int
    '''

    pass


def filepath_drop(filepath="Path"):
    '''Undocumented 

    '''

    pass


def find_missing_files(find_all: bool = False,
                       directory: str = "",
                       filter_blender: bool = False,
                       filter_backup: bool = False,
                       filter_image: bool = False,
                       filter_movie: bool = False,
                       filter_python: bool = False,
                       filter_font: bool = False,
                       filter_sound: bool = False,
                       filter_text: bool = False,
                       filter_btx: bool = False,
                       filter_collada: bool = False,
                       filter_alembic: bool = False,
                       filter_folder: bool = False,
                       filter_blenlib: bool = False,
                       filemode: int = 9,
                       display_type: int = 'DEFAULT',
                       sort_method: int = 'FILE_SORT_ALPHA'):
    '''Try to find missing external files 

    :param find_all: Find All, Find all files in the search path (not just missing) 
    :type find_all: bool
    :param directory: Directory, Directory of the file 
    :type directory: str
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
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    '''

    pass


def hidedot():
    '''Toggle hide hidden dot files 

    '''

    pass


def highlight():
    '''Highlight selected file(s) 

    '''

    pass


def make_paths_absolute():
    '''Make all paths to external files absolute 

    '''

    pass


def make_paths_relative():
    '''Make all paths to external files relative to current .blend 

    '''

    pass


def next():
    '''Move to next folder 

    '''

    pass


def pack_all():
    '''Pack all used external files into the .blend 

    '''

    pass


def pack_libraries():
    '''Pack all used Blender library files into the current .blend 

    '''

    pass


def parent():
    '''Move to parent directory 

    '''

    pass


def previous():
    '''Move to previous folder 

    '''

    pass


def refresh():
    '''Refresh the file list 

    '''

    pass


def rename():
    '''Rename file or file directory 

    '''

    pass


def report_missing_files():
    '''Report all missing external files 

    '''

    pass


def reset_recent():
    '''Reset Recent files 

    '''

    pass


def select(extend: bool = False, fill: bool = False, open: bool = True):
    '''Activate/select file 

    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: bool
    :param fill: Fill, Select everything beginning with the last selection 
    :type fill: bool
    :param open: Open, Open a directory when selecting it 
    :type open: bool
    '''

    pass


def select_all_toggle():
    '''Select or deselect all files 

    '''

    pass


def select_bookmark(dir: str = ""):
    '''Select a bookmarked directory 

    :param dir: Dir 
    :type dir: str
    '''

    pass


def select_border(gesture_mode: int = 0,
                  xmin: int = 0,
                  xmax: int = 0,
                  ymin: int = 0,
                  ymax: int = 0,
                  extend: bool = True):
    '''Activate/select the file(s) contained in the border 

    :param gesture_mode: Gesture Mode 
    :type gesture_mode: int
    :param xmin: X Min 
    :type xmin: int
    :param xmax: X Max 
    :type xmax: int
    :param ymin: Y Min 
    :type ymin: int
    :param ymax: Y Max 
    :type ymax: int
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: bool
    '''

    pass


def select_walk(direction: int = 'UP',
                extend: bool = False,
                fill: bool = False):
    '''Select/Deselect files by walking through them 

    :param direction: Walk Direction, Select/Deselect file in this direction 
    :type direction: int
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: bool
    :param fill: Fill, Select everything beginning with the last selection 
    :type fill: bool
    '''

    pass


def smoothscroll():
    '''Smooth scroll to make editable file visible 

    '''

    pass


def unpack_all(method: int = 'USE_LOCAL'):
    '''Unpack all files packed into this .blend to external ones 

    :param method: Method, How to unpack 
    :type method: int
    '''

    pass


def unpack_item(method: int = 'USE_LOCAL',
                id_name: str = "",
                id_type: int = 19785):
    '''Unpack this file to an external file 

    :param method: Method, How to unpack 
    :type method: int
    :param id_name: ID name, Name of ID block to unpack 
    :type id_name: str
    :param id_type: ID Type, Identifier type of ID block 
    :type id_type: int
    '''

    pass


def unpack_libraries():
    '''Unpack all used Blender library files from this .blend file 

    '''

    pass
