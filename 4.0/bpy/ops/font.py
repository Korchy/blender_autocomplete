import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def case_set(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None,
             *,
             case: typing.Optional[typing.Any] = 'LOWER'):
    ''' Set font case

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param case: Case, Lower or upper case
    :type case: typing.Optional[typing.Any]
    '''

    pass


def case_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Toggle font case

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def change_character(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        delta: typing.Optional[typing.Any] = 1):
    ''' Change font character code

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param delta: Delta, Number to increase or decrease character code with
    :type delta: typing.Optional[typing.Any]
    '''

    pass


def change_spacing(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        delta: typing.Optional[typing.Any] = 1.0):
    ''' Change font spacing

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param delta: Delta, Amount to decrease or increase character spacing with
    :type delta: typing.Optional[typing.Any]
    '''

    pass


def delete(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None,
           *,
           type: typing.Optional[typing.Any] = 'PREVIOUS_CHARACTER'):
    ''' Delete text by cursor position

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type, Which part of the text to delete
    :type type: typing.Optional[typing.Any]
    '''

    pass


def line_break(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Insert line break at cursor position

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def move(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         type: typing.Optional[typing.Any] = 'LINE_BEGIN'):
    ''' Move cursor to position type

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type, Where to move cursor to
    :type type: typing.Optional[typing.Any]
    '''

    pass


def move_select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'LINE_BEGIN'):
    ''' Move the cursor while selecting

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type, Where to move cursor to, to make a selection
    :type type: typing.Optional[typing.Any]
    '''

    pass


def open(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        hide_props_region: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        check_existing: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_blender: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_sound: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_collada: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_alembic: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 9,
        relative_path: typing.Optional[typing.Union[bool, typing.Any]] = True,
        display_type: typing.Optional[typing.Any] = 'THUMBNAIL',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Load a new font from a file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: typing.Optional[typing.Union[bool, typing.Any]]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_image: Filter image files
    :type filter_image: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_python: Filter Python files
    :type filter_python: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_font: Filter font files
    :type filter_font: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_text: Filter text files
    :type filter_text: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_archive: Filter archive files
    :type filter_archive: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_usd: Filter USD files
    :type filter_usd: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_obj: Filter OBJ files
    :type filter_obj: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Optional[typing.Union[bool, typing.Any]]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: typing.Optional[typing.Union[bool, typing.Any]]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def select_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select all text

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_word(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select word under cursor

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def selection_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Set cursor selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def style_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        style: typing.Optional[typing.Any] = 'BOLD',
        clear: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Set font style

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param style: Style, Style to set selection to
    :type style: typing.Optional[typing.Any]
    :param clear: Clear, Clear style rather than setting it
    :type clear: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def style_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        style: typing.Optional[typing.Any] = 'BOLD'):
    ''' Toggle font style

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param style: Style, Style to set selection to
    :type style: typing.Optional[typing.Any]
    '''

    pass


def text_copy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Copy selected text to clipboard

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def text_cut(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None):
    ''' Cut selected text to clipboard

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def text_insert(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        text: typing.Union[str, typing.Any] = "",
        accent: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Insert text at cursor position

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param text: Text, Text to insert at the cursor position
    :type text: typing.Union[str, typing.Any]
    :param accent: Accent Mode, Next typed character will strike through previous, for special character input
    :type accent: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def text_paste(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        selection: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Paste text from clipboard

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param selection: Selection, Paste text selected elsewhere rather than copied (X11/Wayland only)
    :type selection: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def text_paste_from_file(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        hide_props_region: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        check_existing: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_blender: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_sound: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_collada: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_alembic: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 9,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Paste contents from file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: typing.Optional[typing.Union[bool, typing.Any]]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_image: Filter image files
    :type filter_image: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_python: Filter Python files
    :type filter_python: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_font: Filter font files
    :type filter_font: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_text: Filter text files
    :type filter_text: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_archive: Filter archive files
    :type filter_archive: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_usd: Filter USD files
    :type filter_usd: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_obj: Filter OBJ files
    :type filter_obj: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Optional[typing.Union[bool, typing.Any]]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def textbox_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add a new text box

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def textbox_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        index: typing.Optional[typing.Any] = 0):
    ''' Remove the text box

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param index: Index, The current text box
    :type index: typing.Optional[typing.Any]
    '''

    pass


def unlink(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None):
    ''' Unlink active font data-block

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass
