import typing
import collections.abc
import typing_extensions

def layer_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
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
    filter_collada: bool | None = False,
    filter_alembic: bool | None = True,
    filter_usd: bool | None = True,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    relative_path: bool | None = True,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
):
    """Add an override layer to the archive

        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
    """

def layer_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move layer in the list, layers further down the list will overwrite data from the layers higher up

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to move the active vertex group towards
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def layer_remove(execution_context: int | str | None = None, undo: bool | None = None):
    """Remove an override layer from the archive

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def open(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
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
    filter_collada: bool | None = False,
    filter_alembic: bool | None = True,
    filter_usd: bool | None = True,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    relative_path: bool | None = True,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
):
    """Load a cache file

        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
    """

def reload(execution_context: int | str | None = None, undo: bool | None = None):
    """Update objects paths list with new data from the archive

    :type execution_context: int | str | None
    :type undo: bool | None
    """
