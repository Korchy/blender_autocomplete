import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def autopack_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Automatically pack all external files into the .blend file"""

def bookmark_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a bookmark for the selected/active directory"""

def bookmark_cleanup(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete all invalid bookmarks"""

def bookmark_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = -1,
) -> None:
    """Delete selected bookmark

    :param index: Index
    """

def bookmark_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["TOP", "UP", "DOWN", "BOTTOM"] | None = "TOP",
) -> None:
    """Move the active bookmark up/down in the list

        :param direction: Direction, Direction to move the active bookmark towards

    TOP
    Top -- Top of the list.

    UP
    Up.

    DOWN
    Down.

    BOTTOM
    Bottom -- Bottom of the list.
    """

def cancel(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Cancel file operation"""

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move selected files to the trash or recycle bin"""

def directory_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    directory: str = "",
    open: bool | None = False,
    confirm: bool | None = True,
) -> None:
    """Create a new directory

    :param directory: Directory, Name of new directory
    :param open: Open, Open new directory
    :param confirm: Confirm, Prompt for confirmation
    """

def edit_directory_path(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Start editing directory field"""

def execute(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Execute selected file"""

def external_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    operation: typing.Literal[
        "OPEN",
        "FOLDER_OPEN",
        "EDIT",
        "NEW",
        "FIND",
        "SHOW",
        "PLAY",
        "BROWSE",
        "PREVIEW",
        "PRINT",
        "INSTALL",
        "RUNAS",
        "PROPERTIES",
        "FOLDER_FIND",
        "CMD",
    ]
    | None = "OPEN",
) -> None:
    """Perform external operation on a file or folder

        :param operation: Operation, Operation to perform on the selected file or path

    OPEN
    Open -- Open the file.

    FOLDER_OPEN
    Open Folder -- Open the folder.

    EDIT
    Edit -- Edit the file.

    NEW
    New -- Create a new file of this type.

    FIND
    Find File -- Search for files of this type.

    SHOW
    Show -- Show this file.

    PLAY
    Play -- Play this file.

    BROWSE
    Browse -- Browse this file.

    PREVIEW
    Preview -- Preview this file.

    PRINT
    Print -- Print this file.

    INSTALL
    Install -- Install this file.

    RUNAS
    Run As User -- Run as specific user.

    PROPERTIES
    Properties -- Show OS Properties for this item.

    FOLDER_FIND
    Find in Folder -- Search for items in this folder.

    CMD
    Command Prompt Here -- Open a command prompt here.
    """

def filenum(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    increment: int | None = 1,
) -> None:
    """Increment number in filename

    :param increment: Increment
    """

def filepath_drop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "Path",
) -> None:
    """Undocumented, consider contributing."""

def find_missing_files(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    find_all: bool | None = False,
    directory: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = False,
    filter_movie: bool | None = False,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = False,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
) -> None:
    """Try to find missing external files

        :param find_all: Find All, Find all files in the search path (not just missing)
        :param directory: Directory, Directory of the file
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
        :param filter_alembic: Filter Alembic files
        :param filter_usd: Filter USD files
        :param filter_obj: Filter OBJ files
        :param filter_volume: Filter OpenVDB volume files
        :param filter_folder: Filter folders
        :param filter_blenlib: Filter Blender IDs
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
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

def hidedot(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle hide hidden dot files"""

def highlight(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Highlight selected file(s)"""

def make_paths_absolute(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Make all paths to external files absolute"""

def make_paths_relative(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Make all paths to external files relative to current .blend"""

def mouse_execute(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Perform the current execute action for the file under the cursor (e.g. open the file)"""

def next(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move to next folder"""

def pack_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Pack all used external files into this .blend"""

def pack_libraries(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Store all data-blocks linked from other .blend files in the current .blend file. Library references are preserved so the linked data-blocks can be unpacked again"""

def parent(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move to parent directory"""

def previous(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move to previous folder"""

def refresh(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Refresh the file list"""

def rename(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Rename file or file directory"""

def report_missing_files(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Report all missing external files"""

def reset_recent(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset recent files"""

def select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    wait_to_deselect_others: bool | None = False,
    use_select_on_click: bool | None = False,
    mouse_x: int | None = 0,
    mouse_y: int | None = 0,
    extend: bool | None = False,
    fill: bool | None = False,
    open: bool | None = True,
    deselect_all: bool | None = False,
    only_activate_if_selected: bool | None = False,
    pass_through: bool | None = False,
) -> None:
    """Handle mouse clicks to select and activate items

    :param wait_to_deselect_others: Wait to Deselect Others
    :param use_select_on_click: Act on Click, Instead of selecting on mouse press, wait to see if theres drag event. Otherwise select on mouse release
    :param mouse_x: Mouse X
    :param mouse_y: Mouse Y
    :param extend: Extend, Extend selection instead of deselecting everything first
    :param fill: Fill, Select everything beginning with the last selection
    :param open: Open, Open a directory when selecting it
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :param only_activate_if_selected: Only Activate if Selected, Do not change selection if the item under the cursor is already selected, only activate it
    :param pass_through: Pass Through, Even on successful execution, pass the event on so other operators can execute on it as well
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Select or deselect all files

        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
    """

def select_bookmark(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    dir: str = "",
) -> None:
    """Select a bookmarked directory

    :param dir: Directory
    """

def select_box(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
) -> None:
    """Activate/select the file(s) contained in the border

        :param xmin: X Min
        :param xmax: X Max
        :param ymin: Y Min
        :param ymax: Y Max
        :param wait_for_input: Wait for Input
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
    """

def select_walk(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN", "LEFT", "RIGHT"] | None = "UP",
    extend: bool | None = False,
    fill: bool | None = False,
) -> None:
    """Select/Deselect files by walking through them

    :param direction: Walk Direction, Select/Deselect element in this direction
    :param extend: Extend, Extend selection instead of deselecting everything first
    :param fill: Fill, Select everything beginning with the last selection
    """

def smoothscroll(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Smooth scroll to make editable file visible"""

def sort_column_ui_context(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Change sorting to use column under cursor"""

def start_filter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Start entering filter text"""

def unpack_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    method: typing.Literal[
        "USE_LOCAL", "WRITE_LOCAL", "USE_ORIGINAL", "WRITE_ORIGINAL", "KEEP", "REMOVE"
    ]
    | None = "USE_LOCAL",
) -> None:
    """Unpack all files packed into this .blend to external ones

    :param method: Method, How to unpack
    """

def unpack_item(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    method: typing.Literal["USE_LOCAL", "WRITE_LOCAL", "USE_ORIGINAL", "WRITE_ORIGINAL"]
    | None = "USE_LOCAL",
    id_name: str = "",
    id_type: int | None = 19785,
) -> None:
    """Unpack this file to an external file

    :param method: Method, How to unpack
    :param id_name: ID Name, Name of ID block to unpack
    :param id_type: ID Type, Identifier type of ID block
    """

def unpack_libraries(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Restore all packed linked data-blocks to their original locations"""

def view_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Scroll the selected files into view"""
