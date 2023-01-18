import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def actionzone(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               modifier: typing.Optional[typing.Any] = 0):
    ''' Handle area action zones for mouse actions/gestures

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Modifier state
    :type modifier: typing.Optional[typing.Any]
    '''

    pass


def animation_cancel(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     restore_frame: typing.Union[bool, typing.Any] = True):
    ''' Cancel animation, returning to the original frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param restore_frame: Restore Frame, Restore the frame when animation was initialized
    :type restore_frame: typing.Union[bool, typing.Any]
    '''

    pass


def animation_play(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   reverse: typing.Union[bool, typing.Any] = False,
                   sync: typing.Union[bool, typing.Any] = False):
    ''' Play animation

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param reverse: Play in Reverse, Animation is played backwards
    :type reverse: typing.Union[bool, typing.Any]
    :param sync: Sync, Drop frames to maintain framerate
    :type sync: typing.Union[bool, typing.Any]
    '''

    pass


def animation_step(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None):
    ''' Step through animation by position

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def area_close(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None):
    ''' Close selected area

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def area_dupli(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None):
    ''' Duplicate selected area into new window

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def area_join(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              cursor: typing.Optional[typing.Any] = (0, 0)):
    ''' Join selected areas into new window

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param cursor: Cursor
    :type cursor: typing.Optional[typing.Any]
    '''

    pass


def area_move(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              x: typing.Optional[typing.Any] = 0,
              y: typing.Optional[typing.Any] = 0,
              delta: typing.Optional[typing.Any] = 0):
    ''' Move selected area edges

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param x: X
    :type x: typing.Optional[typing.Any]
    :param y: Y
    :type y: typing.Optional[typing.Any]
    :param delta: Delta
    :type delta: typing.Optional[typing.Any]
    '''

    pass


def area_options(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Operations for splitting and merging

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def area_split(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               direction: typing.Optional[typing.Any] = 'HORIZONTAL',
               factor: typing.Optional[typing.Any] = 0.5,
               cursor: typing.Optional[typing.Any] = (0, 0)):
    ''' Split selected area into new windows

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param direction: Direction
    :type direction: typing.Optional[typing.Any]
    :param factor: Factor
    :type factor: typing.Optional[typing.Any]
    :param cursor: Cursor
    :type cursor: typing.Optional[typing.Any]
    '''

    pass


def area_swap(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              cursor: typing.Optional[typing.Any] = (0, 0)):
    ''' Swap selected areas screen positions

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param cursor: Cursor
    :type cursor: typing.Optional[typing.Any]
    '''

    pass


def back_to_previous(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None):
    ''' Revert back to the original screen layout, before fullscreen area overlay

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None):
    ''' Delete active screen

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def drivers_editor_show(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Show drivers editor in a separate window

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def frame_jump(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               end: typing.Union[bool, typing.Any] = False):
    ''' Jump to first/last frame in frame range

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param end: Last Frame, Jump to the last frame of the frame range
    :type end: typing.Union[bool, typing.Any]
    '''

    pass


def frame_offset(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 delta: typing.Optional[typing.Any] = 0):
    ''' Move current frame forward/backward by a given number

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param delta: Delta
    :type delta: typing.Optional[typing.Any]
    '''

    pass


def header_toggle_menus(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Expand or collapse the header pulldown menus

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def info_log_show(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None):
    ''' Show info log in a separate window

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def keyframe_jump(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  next: typing.Union[bool, typing.Any] = True):
    ''' Jump to previous/next keyframe

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param next: Next Keyframe
    :type next: typing.Union[bool, typing.Any]
    '''

    pass


def marker_jump(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                next: typing.Union[bool, typing.Any] = True):
    ''' Jump to previous/next marker

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param next: Next Marker
    :type next: typing.Union[bool, typing.Any]
    '''

    pass


def new(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None):
    ''' Add a new screen

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def redo_last(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None):
    ''' Display parameters for last action performed

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def region_blend(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Blend in and out overlapping region

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def region_context_menu(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Display region context menu

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def region_flip(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Toggle the region's alignment (left/right or top/bottom)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def region_quadview(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' Split selected area into camera, front, right, and top views

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def region_scale(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Scale selected area

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def region_toggle(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  region_type: typing.Union[str, int] = 'WINDOW'):
    ''' Hide or unhide the region

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param region_type: Region Type, Type of the region to toggle
    :type region_type: typing.Union[str, int]
    '''

    pass


def repeat_history(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   index: typing.Optional[typing.Any] = 0):
    ''' Display menu for previous actions performed

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param index: Index
    :type index: typing.Optional[typing.Any]
    '''

    pass


def repeat_last(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Repeat last action

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def screen_full_area(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     use_hide_panels: typing.Union[bool, typing.Any] = False):
    ''' Toggle display selected area as fullscreen/maximized

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param use_hide_panels: Hide Panels, Hide all the panels
    :type use_hide_panels: typing.Union[bool, typing.Any]
    '''

    pass


def screen_set(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               delta: typing.Optional[typing.Any] = 1):
    ''' Cycle through available screens

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param delta: Delta
    :type delta: typing.Optional[typing.Any]
    '''

    pass


def screenshot(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               filepath: typing.Union[str, typing.Any] = "",
               hide_props_region: typing.Union[bool, typing.Any] = True,
               check_existing: typing.Union[bool, typing.Any] = True,
               filter_blender: typing.Union[bool, typing.Any] = False,
               filter_backup: typing.Union[bool, typing.Any] = False,
               filter_image: typing.Union[bool, typing.Any] = True,
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
               filter_folder: typing.Union[bool, typing.Any] = True,
               filter_blenlib: typing.Union[bool, typing.Any] = False,
               filemode: typing.Optional[typing.Any] = 9,
               show_multiview: typing.Union[bool, typing.Any] = False,
               use_multiview: typing.Union[bool, typing.Any] = False,
               display_type: typing.Optional[typing.Any] = 'DEFAULT',
               sort_method: typing.Union[str, int, typing.Any] = ''):
    ''' Capture a picture of the whole Blender window

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
    :param show_multiview: Enable Multi-View
    :type show_multiview: typing.Union[bool, typing.Any]
    :param use_multiview: Use Multi-View
    :type use_multiview: typing.Union[bool, typing.Any]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int, typing.Any]
    '''

    pass


def screenshot_area(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    filepath: typing.Union[str, typing.Any] = "",
                    hide_props_region: typing.Union[bool, typing.Any] = True,
                    check_existing: typing.Union[bool, typing.Any] = True,
                    filter_blender: typing.Union[bool, typing.Any] = False,
                    filter_backup: typing.Union[bool, typing.Any] = False,
                    filter_image: typing.Union[bool, typing.Any] = True,
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
                    filter_folder: typing.Union[bool, typing.Any] = True,
                    filter_blenlib: typing.Union[bool, typing.Any] = False,
                    filemode: typing.Optional[typing.Any] = 9,
                    show_multiview: typing.Union[bool, typing.Any] = False,
                    use_multiview: typing.Union[bool, typing.Any] = False,
                    display_type: typing.Optional[typing.Any] = 'DEFAULT',
                    sort_method: typing.Union[str, int, typing.Any] = ''):
    ''' Capture a picture of an editor

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
    :param show_multiview: Enable Multi-View
    :type show_multiview: typing.Union[bool, typing.Any]
    :param use_multiview: Use Multi-View
    :type use_multiview: typing.Union[bool, typing.Any]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int, typing.Any]
    '''

    pass


def space_context_cycle(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        direction: typing.Optional[typing.Any] = 'NEXT'):
    ''' Cycle through the editor context by activating the next/previous one

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param direction: Direction, Direction to cycle through
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def space_type_set_or_cycle(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: typing.Optional[bool] = None,
                            *,
                            space_type: typing.Union[str, int] = 'EMPTY'):
    ''' Set the space type or cycle subtype

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param space_type: Type
    :type space_type: typing.Union[str, int]
    '''

    pass


def spacedata_cleanup(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Remove unused settings for invisible editors

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def userpref_show(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  section: typing.Union[str, int] = 'INTERFACE'):
    ''' Edit user preferences and system settings

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param section: Section to activate in the Preferences
    :type section: typing.Union[str, int]
    '''

    pass


def workspace_cycle(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    direction: typing.Optional[typing.Any] = 'NEXT'):
    ''' Cycle through workspaces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param direction: Direction, Direction to cycle through
    :type direction: typing.Optional[typing.Any]
    '''

    pass
