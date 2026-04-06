import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def clear_filter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear the search filter"""

def context_menu(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Display properties editor context_menu"""

def directory_browse(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
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
    relative_path: bool | None = True,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
) -> None:
    """Open a directory browser, hold Shift to open the file, Alt to browse containing directory

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
        :param relative_path: Relative Path, Select the file relative to the blend file
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

def file_browse(
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = False,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    relative_path: bool | None = True,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    filter_glob: str = "",
) -> None:
    """Open a file browser, hold Shift to open the file, Alt to browse containing directory

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
        :param filter_alembic: Filter Alembic files
        :param filter_usd: Filter USD files
        :param filter_obj: Filter OBJ files
        :param filter_volume: Filter OpenVDB volume files
        :param filter_folder: Filter folders
        :param filter_blenlib: Filter Blender IDs
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :param relative_path: Relative Path, Select the file relative to the blend file
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
        :param filter_glob: Glob Filter, Custom filter
    """

def start_filter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Start entering filter text"""

def toggle_pin(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Keep the current data-block displayed"""
