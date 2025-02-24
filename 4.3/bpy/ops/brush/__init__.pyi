import typing
import collections.abc
import typing_extensions
import bpy._typing.rna_enums

def asset_activate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    asset_library_type: bpy._typing.rna_enums.AssetLibraryTypeItems | None = "LOCAL",
    asset_library_identifier: str = "",
    relative_asset_identifier: str = "",
):
    """Activate a brush asset as current sculpt and paint tool

    :type execution_context: int | str | None
    :type undo: bool | None
    :param asset_library_type: Asset Library Type
    :type asset_library_type: bpy._typing.rna_enums.AssetLibraryTypeItems | None
    :param asset_library_identifier: Asset Library Identifier
    :type asset_library_identifier: str
    :param relative_asset_identifier: Relative Asset Identifier
    :type relative_asset_identifier: str
    """

def asset_delete(execution_context: int | str | None = None, undo: bool | None = None):
    """Delete the active brush asset

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def asset_edit_metadata(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    catalog_path: str = "",
    author: str = "",
    description: str = "",
):
    """Edit asset information like the catalog, preview image, tags, or author

    :type execution_context: int | str | None
    :type undo: bool | None
    :param catalog_path: Catalog, The asset's catalog path
    :type catalog_path: str
    :param author: Author
    :type author: str
    :param description: Description
    :type description: str
    """

def asset_load_preview(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
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
):
    """Choose a preview image for the brush

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
        :param show_multiview: Enable Multi-View
        :type show_multiview: bool | None
        :param use_multiview: Use Multi-View
        :type use_multiview: bool | None
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

def asset_revert(execution_context: int | str | None = None, undo: bool | None = None):
    """Revert the active brush settings to the default values from the asset library

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def asset_save(execution_context: int | str | None = None, undo: bool | None = None):
    """Update the active brush asset in the asset library with current settings

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def asset_save_as(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    asset_library_reference: str | None = "",
    catalog_path: str = "",
):
    """Save a copy of the active brush asset into the default asset library, and make it the active brush

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name for the new brush asset
    :type name: str
    :param asset_library_reference: Library, Asset library used to store the new brush
    :type asset_library_reference: str | None
    :param catalog_path: Catalog, Catalog to use for the new asset
    :type catalog_path: str
    """

def curve_preset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    shape: typing.Literal["SHARP", "SMOOTH", "MAX", "LINE", "ROUND", "ROOT"]
    | None = "SMOOTH",
):
    """Set brush shape

    :type execution_context: int | str | None
    :type undo: bool | None
    :param shape: Mode
    :type shape: typing.Literal['SHARP','SMOOTH','MAX','LINE','ROUND','ROOT'] | None
    """

def scale_size(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    scalar: float | None = 1.0,
):
    """Change brush size by a scalar

    :type execution_context: int | str | None
    :type undo: bool | None
    :param scalar: Scalar, Factor to scale brush size by
    :type scalar: float | None
    """

def sculpt_curves_falloff_preset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    shape: typing.Literal["SHARP", "SMOOTH", "MAX", "LINE", "ROUND", "ROOT"]
    | None = "SMOOTH",
):
    """Set Curve Falloff Preset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param shape: Mode
    :type shape: typing.Literal['SHARP','SMOOTH','MAX','LINE','ROUND','ROOT'] | None
    """

def stencil_control(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["TRANSLATION", "SCALE", "ROTATION"] | None = "TRANSLATION",
    texmode: typing.Literal["PRIMARY", "SECONDARY"] | None = "PRIMARY",
):
    """Control the stencil brush

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Tool
    :type mode: typing.Literal['TRANSLATION','SCALE','ROTATION'] | None
    :param texmode: Tool
    :type texmode: typing.Literal['PRIMARY','SECONDARY'] | None
    """

def stencil_fit_image_aspect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_repeat: bool | None = True,
    use_scale: bool | None = True,
    mask: bool | None = False,
):
    """When using an image texture, adjust the stencil size to fit the image aspect ratio

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_repeat: Use Repeat, Use repeat mapping values
    :type use_repeat: bool | None
    :param use_scale: Use Scale, Use texture scale values
    :type use_scale: bool | None
    :param mask: Modify Mask Stencil, Modify either the primary or mask stencil
    :type mask: bool | None
    """

def stencil_reset_transform(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mask: bool | None = False,
):
    """Reset the stencil transformation to the default

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mask: Modify Mask Stencil, Modify either the primary or mask stencil
    :type mask: bool | None
    """
