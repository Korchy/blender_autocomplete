import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def clear_filter(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Clear the search filter

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def context_menu(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Display properties editor context_menu

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def directory_browse(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     directory: typing.Union[str, typing.Any] = "",
                     hide_props_region: typing.Union[bool, typing.Any] = True,
                     check_existing: typing.Union[bool, typing.Any] = False,
                     filter_blender: typing.Union[bool, typing.Any] = False,
                     filter_backup: typing.Union[bool, typing.Any] = False,
                     filter_image: typing.Union[bool, typing.Any] = False,
                     filter_movie: typing.Union[bool, typing.Any] = False,
                     filter_python: typing.Union[bool, typing.Any] = False,
                     filter_font: typing.Union[bool, typing.Any] = False,
                     filter_sound: typing.Union[bool, typing.Any] = False,
                     filter_text: typing.Union[bool, typing.Any] = False,
                     filter_archive: typing.Union[bool, typing.Any] = False,
                     filter_btx: typing.Union[bool, typing.Any] = False,
                     filter_collada: typing.Union[bool, typing.Any] = False,
                     filter_alembic: typing.Union[bool, typing.Any] = False,
                     filter_usd: typing.Union[bool, typing.Any] = False,
                     filter_obj: typing.Union[bool, typing.Any] = False,
                     filter_volume: typing.Union[bool, typing.Any] = False,
                     filter_folder: typing.Union[bool, typing.Any] = False,
                     filter_blenlib: typing.Union[bool, typing.Any] = False,
                     filemode: typing.Optional[typing.Any] = 9,
                     relative_path: typing.Union[bool, typing.Any] = True,
                     display_type: typing.Optional[typing.Any] = 'DEFAULT',
                     sort_method: typing.Union[str, int, typing.Any] = ''):
    ''' Open a directory browser, hold Shift to open the file, Alt to browse containing directory

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: typing.Union[bool, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Union[bool, typing.Any]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Union[bool, typing.Any]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Union[bool, typing.Any]
    :param filter_image: Filter image files
    :type filter_image: typing.Union[bool, typing.Any]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Union[bool, typing.Any]
    :param filter_python: Filter python files
    :type filter_python: typing.Union[bool, typing.Any]
    :param filter_font: Filter font files
    :type filter_font: typing.Union[bool, typing.Any]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Union[bool, typing.Any]
    :param filter_text: Filter text files
    :type filter_text: typing.Union[bool, typing.Any]
    :param filter_archive: Filter archive files
    :type filter_archive: typing.Union[bool, typing.Any]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Union[bool, typing.Any]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Union[bool, typing.Any]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Union[bool, typing.Any]
    :param filter_usd: Filter USD files
    :type filter_usd: typing.Union[bool, typing.Any]
    :param filter_obj: Filter OBJ files
    :type filter_obj: typing.Union[bool, typing.Any]
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: typing.Union[bool, typing.Any]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Union[bool, typing.Any]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Union[bool, typing.Any]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: typing.Union[bool, typing.Any]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int, typing.Any]
    '''

    pass


def file_browse(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                filepath: typing.Union[str, typing.Any] = "",
                hide_props_region: typing.Union[bool, typing.Any] = True,
                check_existing: typing.Union[bool, typing.Any] = False,
                filter_blender: typing.Union[bool, typing.Any] = False,
                filter_backup: typing.Union[bool, typing.Any] = False,
                filter_image: typing.Union[bool, typing.Any] = False,
                filter_movie: typing.Union[bool, typing.Any] = False,
                filter_python: typing.Union[bool, typing.Any] = False,
                filter_font: typing.Union[bool, typing.Any] = False,
                filter_sound: typing.Union[bool, typing.Any] = False,
                filter_text: typing.Union[bool, typing.Any] = False,
                filter_archive: typing.Union[bool, typing.Any] = False,
                filter_btx: typing.Union[bool, typing.Any] = False,
                filter_collada: typing.Union[bool, typing.Any] = False,
                filter_alembic: typing.Union[bool, typing.Any] = False,
                filter_usd: typing.Union[bool, typing.Any] = False,
                filter_obj: typing.Union[bool, typing.Any] = False,
                filter_volume: typing.Union[bool, typing.Any] = False,
                filter_folder: typing.Union[bool, typing.Any] = False,
                filter_blenlib: typing.Union[bool, typing.Any] = False,
                filemode: typing.Optional[typing.Any] = 9,
                relative_path: typing.Union[bool, typing.Any] = True,
                display_type: typing.Optional[typing.Any] = 'DEFAULT',
                sort_method: typing.Union[str, int, typing.Any] = ''):
    ''' Open a file browser, hold Shift to open the file, Alt to browse containing directory

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: typing.Union[bool, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Union[bool, typing.Any]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Union[bool, typing.Any]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Union[bool, typing.Any]
    :param filter_image: Filter image files
    :type filter_image: typing.Union[bool, typing.Any]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Union[bool, typing.Any]
    :param filter_python: Filter python files
    :type filter_python: typing.Union[bool, typing.Any]
    :param filter_font: Filter font files
    :type filter_font: typing.Union[bool, typing.Any]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Union[bool, typing.Any]
    :param filter_text: Filter text files
    :type filter_text: typing.Union[bool, typing.Any]
    :param filter_archive: Filter archive files
    :type filter_archive: typing.Union[bool, typing.Any]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Union[bool, typing.Any]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Union[bool, typing.Any]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Union[bool, typing.Any]
    :param filter_usd: Filter USD files
    :type filter_usd: typing.Union[bool, typing.Any]
    :param filter_obj: Filter OBJ files
    :type filter_obj: typing.Union[bool, typing.Any]
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: typing.Union[bool, typing.Any]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Union[bool, typing.Any]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Union[bool, typing.Any]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: typing.Union[bool, typing.Any]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int, typing.Any]
    '''

    pass


def start_filter(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Start entering filter text

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def toggle_pin(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None):
    ''' Keep the current data-block displayed

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass
