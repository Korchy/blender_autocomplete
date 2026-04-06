import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums

def actionzone(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: int | None = 0,
) -> None:
    """Handle area action zones for mouse actions/gestures

    :param modifier: Modifier, Modifier state
    """

def animation_cancel(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    restore_frame: bool | None = True,
) -> None:
    """Cancel animation, returning to the original frame

    :param restore_frame: Restore Frame, Restore the frame when animation was initialized
    """

def animation_play(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    reverse: bool | None = False,
    sync: bool | None = False,
) -> None:
    """Play animation

    :param reverse: Play in Reverse, Animation is played backwards
    :param sync: Sync, Drop frames to maintain framerate
    """

def animation_step(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Step through animation by position"""

def area_close(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Close selected area"""

def area_dupli(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Duplicate selected area into new window"""

def area_join(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    source_xy: collections.abc.Iterable[int] | None = (0, 0),
    target_xy: collections.abc.Iterable[int] | None = (0, 0),
) -> None:
    """Join selected areas into new window

    :param source_xy: Source location
    :param target_xy: Target location
    """

def area_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    x: int | None = 0,
    y: int | None = 0,
    delta: int | None = 0,
) -> None:
    """Move selected area edges

    :param x: X
    :param y: Y
    :param delta: Delta
    """

def area_options(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Operations for splitting and merging"""

def area_split(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["HORIZONTAL", "VERTICAL"] | None = "HORIZONTAL",
    factor: float | None = 0.5,
    cursor: collections.abc.Iterable[int] | None = (0, 0),
) -> None:
    """Split selected area into new windows

    :param direction: Direction
    :param factor: Factor
    :param cursor: Cursor
    """

def area_swap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    cursor: collections.abc.Iterable[int] | None = (0, 0),
) -> None:
    """Swap selected areas screen positions

    :param cursor: Cursor
    """

def back_to_previous(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Revert back to the original screen layout, before fullscreen area overlay"""

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete active screen"""

def drivers_editor_show(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Show drivers editor in a separate window"""

def frame_jump(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    end: bool | None = False,
) -> None:
    """Jump to first/last frame in frame range

    :param end: Last Frame, Jump to the last frame of the frame range
    """

def frame_offset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delta: int | None = 0,
) -> None:
    """Move current frame forward/backward by a given number

    :param delta: Delta
    """

def header_toggle_menus(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Expand or collapse the header pulldown menus"""

def info_log_show(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Show info log in a separate window"""

def keyframe_jump(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    next: bool | None = True,
) -> None:
    """Jump to previous/next keyframe

    :param next: Next Keyframe
    """

def marker_jump(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    next: bool | None = True,
) -> None:
    """Jump to previous/next marker

    :param next: Next Marker
    """

def new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a new screen"""

def redo_last(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Display parameters for last action performed"""

def region_blend(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Blend in and out overlapping region"""

def region_context_menu(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Display region context menu"""

def region_flip(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle the regions alignment (left/right or top/bottom)"""

def region_quadview(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Split selected area into camera, front, right, and top views"""

def region_scale(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Scale selected area"""

def region_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    region_type: bpy.stub_internal.rna_enums.RegionTypeItems | None = "WINDOW",
) -> None:
    """Hide or unhide the region

    :param region_type: Region Type, Type of the region to toggle
    """

def repeat_history(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
) -> None:
    """Display menu for previous actions performed

    :param index: Index
    """

def repeat_last(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Repeat last action"""

def screen_full_area(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_hide_panels: bool | None = False,
) -> None:
    """Toggle display selected area as fullscreen/maximized

    :param use_hide_panels: Hide Panels, Hide all the panels
    """

def screen_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delta: int | None = 1,
) -> None:
    """Cycle through available screens

    :param delta: Delta
    """

def screenshot(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = True,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = True,
    filter_movie: bool | None = False,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_collada: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    show_multiview: bool | None = False,
    use_multiview: bool | None = False,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
) -> None:
    """Capture a picture of the whole Blender window

        :param filepath: File Path, Path to file
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :param filter_blender: Filter .blend files
        :param filter_backup: Filter .blend files
        :param filter_image: Filter image files
        :param filter_movie: Filter movie files
        :param filter_python: Filter Python files
        :param filter_font: Filter font files
        :param filter_sound: Filter sound files
        :param filter_text: Filter text files
        :param filter_archive: Filter archive files
        :param filter_btx: Filter btx files
        :param filter_collada: Filter COLLADA files
        :param filter_alembic: Filter Alembic files
        :param filter_usd: Filter USD files
        :param filter_obj: Filter OBJ files
        :param filter_volume: Filter OpenVDB volume files
        :param filter_folder: Filter folders
        :param filter_blenlib: Filter Blender IDs
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :param show_multiview: Enable Multi-View
        :param use_multiview: Use Multi-View
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :param sort_method: File sorting mode
    """

def screenshot_area(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = True,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = True,
    filter_movie: bool | None = False,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_collada: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    show_multiview: bool | None = False,
    use_multiview: bool | None = False,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
) -> None:
    """Capture a picture of an editor

        :param filepath: File Path, Path to file
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :param filter_blender: Filter .blend files
        :param filter_backup: Filter .blend files
        :param filter_image: Filter image files
        :param filter_movie: Filter movie files
        :param filter_python: Filter Python files
        :param filter_font: Filter font files
        :param filter_sound: Filter sound files
        :param filter_text: Filter text files
        :param filter_archive: Filter archive files
        :param filter_btx: Filter btx files
        :param filter_collada: Filter COLLADA files
        :param filter_alembic: Filter Alembic files
        :param filter_usd: Filter USD files
        :param filter_obj: Filter OBJ files
        :param filter_volume: Filter OpenVDB volume files
        :param filter_folder: Filter folders
        :param filter_blenlib: Filter Blender IDs
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :param show_multiview: Enable Multi-View
        :param use_multiview: Use Multi-View
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :param sort_method: File sorting mode
    """

def space_context_cycle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["PREV", "NEXT"] | None = "NEXT",
) -> None:
    """Cycle through the editor context by activating the next/previous one

    :param direction: Direction, Direction to cycle through
    """

def space_type_set_or_cycle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    space_type: bpy.stub_internal.rna_enums.SpaceTypeItems | None = "EMPTY",
) -> None:
    """Set the space type or cycle subtype

    :param space_type: Type
    """

def spacedata_cleanup(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove unused settings for invisible editors"""

def userpref_show(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    section: bpy.stub_internal.rna_enums.PreferenceSectionItems | None = "INTERFACE",
) -> None:
    """Edit user preferences and system settings

    :param section: Section to activate in the Preferences
    """

def workspace_cycle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["PREV", "NEXT"] | None = "NEXT",
) -> None:
    """Cycle through workspaces

    :param direction: Direction, Direction to cycle through
    """
