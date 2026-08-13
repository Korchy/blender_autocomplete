import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class autopack_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Automatically pack all external files into the .blend file

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class bookmark_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a bookmark for the selected/active directory

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class bookmark_cleanup(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete all invalid bookmarks

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class bookmark_delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        index: int | None = -1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete selected bookmark

        :param execution_context:
        :param undo:
        :param index: Index, (in [-1, 20000], optional)
        :return: Result of the operator call.
        """

class bookmark_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal["TOP", "UP", "DOWN", "BOTTOM"] | None = "TOP",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move the active bookmark up/down in the list

                :param execution_context:
                :param undo:
                :param direction: Direction, Direction to move the active bookmark towards (optional)

        TOP
        Top -- Top of the list.

        UP
        Up.

        DOWN
        Down.

        BOTTOM
        Bottom -- Bottom of the list.
                :return: Result of the operator call.
        """

class cancel(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Cancel file operation

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move selected files to the trash or recycle bin

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class directory_new(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        directory: str = "",
        open: bool | None = False,
        confirm: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a new directory

        :param execution_context:
        :param undo:
        :param directory: Directory, Name of new directory (optional, never None)
        :param open: Open, Open new directory (optional)
        :param confirm: Confirm, Prompt for confirmation (optional)
        :return: Result of the operator call.
        """

class edit_directory_path(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Start editing directory field

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class execute(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Execute selected file

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class external_operation(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Perform external operation on a file or folder

                :param execution_context:
                :param undo:
                :param operation: Operation, Operation to perform on the selected file or path (optional)

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
                :return: Result of the operator call.
        """

class filenum(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        increment: int | None = 1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Increment number in filename

        :param execution_context:
        :param undo:
        :param increment: Increment, (in [-100, 100], optional)
        :return: Result of the operator call.
        """

class filepath_drop(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "Path",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param filepath: (optional, never None)
        :return: Result of the operator call.
        """

class find_missing_files(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Try to find missing external files

                :param execution_context:
                :param undo:
                :param find_all: Find All, Find all files in the search path (not just missing) (optional)
                :param directory: Directory, Directory of the file (optional, never None)
                :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
                :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
                :param filter_blender: Filter .blend files, (optional)
                :param filter_backup: Filter backup .blend files, (optional)
                :param filter_image: Filter image files, (optional)
                :param filter_movie: Filter movie files, (optional)
                :param filter_python: Filter Python files, (optional)
                :param filter_font: Filter font files, (optional)
                :param filter_sound: Filter sound files, (optional)
                :param filter_text: Filter text files, (optional)
                :param filter_archive: Filter archive files, (optional)
                :param filter_btx: Filter btx files, (optional)
                :param filter_alembic: Filter Alembic files, (optional)
                :param filter_usd: Filter USD files, (optional)
                :param filter_obj: Filter OBJ files, (optional)
                :param filter_volume: Filter OpenVDB volume files, (optional)
                :param filter_folder: Filter folders, (optional)
                :param filter_blenlib: Filter Blender IDs, (optional)
                :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
                :param display_type: Display Type, (optional)

        DEFAULT
        Default -- Automatically determine display type for files.

        LIST_VERTICAL
        Short List -- Display files as short list.

        LIST_HORIZONTAL
        Long List -- Display files as a detailed list.

        THUMBNAIL
        Thumbnails -- Display files as thumbnails.
                :param sort_method: File sorting mode, (optional)
                :return: Result of the operator call.
        """

class hidedot(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Toggle hide hidden dot files

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class highlight(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Highlight selected file(s)

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class make_paths_absolute(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make all paths to external files absolute

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class make_paths_relative(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make all paths to external files relative to current .blend

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class mouse_execute(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Perform the current execute action for the file under the cursor (e.g. open the file)

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class next(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move to next folder

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class pack_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Pack all used external files into this .blend

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class pack_libraries(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Store all data-blocks linked from other .blend files in the current .blend file. Library references are preserved so the linked data-blocks can be unpacked again

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class parent(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move to parent directory

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class previous(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move to previous folder

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class refresh(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Refresh the file list

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class rename(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Rename file or file directory

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class report_missing_files(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Report all missing external files

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class reset_recent(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset recent files

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Handle mouse clicks to select and activate items

        :param execution_context:
        :param undo:
        :param wait_to_deselect_others: Wait to Deselect Others, (optional)
        :param use_select_on_click: Act on Click, Instead of selecting on mouse press, wait to see if theres drag event. Otherwise select on mouse release (optional)
        :param mouse_x: Mouse X, (in [-inf, inf], optional)
        :param mouse_y: Mouse Y, (in [-inf, inf], optional)
        :param extend: Extend, Extend selection instead of deselecting everything first (optional)
        :param fill: Fill, Select everything beginning with the last selection (optional)
        :param open: Open, Open a directory when selecting it (optional)
        :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor (optional)
        :param only_activate_if_selected: Only Activate if Selected, Do not change selection if the item under the cursor is already selected, only activate it (optional)
        :param pass_through: Pass Through, Even on successful execution, pass the event on so other operators can execute on it as well (optional)
        :return: Result of the operator call.
        """

class select_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"]
        | None = "TOGGLE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select or deselect all files

                :param execution_context:
                :param undo:
                :param action: Action, Selection action to execute (optional)

        TOGGLE
        Toggle -- Toggle selection for all elements.

        SELECT
        Select -- Select all elements.

        DESELECT
        Deselect -- Deselect all elements.

        INVERT
        Invert -- Invert selection of all elements.
                :return: Result of the operator call.
        """

class select_bookmark(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        dir: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select a bookmarked directory

        :param execution_context:
        :param undo:
        :param dir: Directory, (optional, never None)
        :return: Result of the operator call.
        """

class select_box(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Activate/select the file(s) contained in the border

                :param execution_context:
                :param undo:
                :param xmin: X Min, (in [-inf, inf], optional)
                :param xmax: X Max, (in [-inf, inf], optional)
                :param ymin: Y Min, (in [-inf, inf], optional)
                :param ymax: Y Max, (in [-inf, inf], optional)
                :param wait_for_input: Wait for Input, (optional)
                :param mode: Mode, (optional)

        SET
        Set -- Set a new selection.

        ADD
        Extend -- Extend existing selection.

        SUB
        Subtract -- Subtract existing selection.
                :return: Result of the operator call.
        """

class select_walk(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal["UP", "DOWN", "LEFT", "RIGHT"] | None = "UP",
        extend: bool | None = False,
        fill: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select/Deselect files by walking through them

        :param execution_context:
        :param undo:
        :param direction: Walk Direction, Select/Deselect element in this direction (optional)
        :param extend: Extend, Extend selection instead of deselecting everything first (optional)
        :param fill: Fill, Select everything beginning with the last selection (optional)
        :return: Result of the operator call.
        """

class smoothscroll(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Smooth scroll to make editable file visible

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class sort_column_ui_context(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change sorting to use column under cursor

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class start_filter(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Start entering filter text

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class unpack_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        method: typing.Literal[
            "USE_LOCAL",
            "WRITE_LOCAL",
            "USE_ORIGINAL",
            "WRITE_ORIGINAL",
            "KEEP",
            "REMOVE",
        ]
        | None = "USE_LOCAL",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Unpack all files packed into this .blend to external ones

        :param execution_context:
        :param undo:
        :param method: Method, How to unpack (optional)
        :return: Result of the operator call.
        """

class unpack_item(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        method: typing.Literal[
            "USE_LOCAL", "WRITE_LOCAL", "USE_ORIGINAL", "WRITE_ORIGINAL"
        ]
        | None = "USE_LOCAL",
        id_name: str = "",
        id_type: int | None = 19785,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Unpack this file to an external file

        :param execution_context:
        :param undo:
        :param method: Method, How to unpack (optional)
        :param id_name: ID Name, Name of ID block to unpack (optional, never None)
        :param id_type: ID Type, Identifier type of ID block (in [0, inf], optional)
        :return: Result of the operator call.
        """

class unpack_libraries(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Restore all packed linked data-blocks to their original locations

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_selected(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Scroll the selected files into view

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
