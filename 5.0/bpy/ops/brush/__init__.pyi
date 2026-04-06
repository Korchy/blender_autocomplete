import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums

def asset_activate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    asset_library_type: bpy.stub_internal.rna_enums.AssetLibraryTypeItems
    | None = "LOCAL",
    asset_library_identifier: str = "",
    relative_asset_identifier: str = "",
    use_toggle: bool | None = False,
) -> None:
    """Activate a brush asset as current sculpt and paint tool

    :param asset_library_type: Asset Library Type
    :param asset_library_identifier: Asset Library Identifier
    :param relative_asset_identifier: Relative Asset Identifier
    :param use_toggle: Toggle, Switch between the current and assigned brushes on consecutive uses.
    """

def asset_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete the active brush asset"""

def asset_edit_metadata(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    catalog_path: str = "",
    author: str = "",
    description: str = "",
) -> None:
    """Edit asset information like the catalog, preview image, tags, or author

    :param catalog_path: Catalog, The assets catalog path
    :param author: Author
    :param description: Description
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
    """Choose a preview image for the brush

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

def asset_revert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Revert the active brush settings to the default values from the asset library"""

def asset_save(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Update the active brush asset in the asset library with current settings"""

def asset_save_as(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    asset_library_reference: str | None = "",
    catalog_path: str = "",
) -> None:
    """Save a copy of the active brush asset into the default asset library, and make it the active brush

    :param name: Name, Name for the new brush asset
    :param asset_library_reference: Library, Asset library used to store the new brush
    :param catalog_path: Catalog, Catalog to use for the new asset
    """

def scale_size(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    scalar: float | None = 1.0,
) -> None:
    """Change brush size by a scalar

    :param scalar: Scalar, Factor to scale brush size by
    """

def stencil_control(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["TRANSLATION", "SCALE", "ROTATION"] | None = "TRANSLATION",
    texmode: typing.Literal["PRIMARY", "SECONDARY"] | None = "PRIMARY",
) -> None:
    """Control the stencil brush

    :param mode: Tool
    :param texmode: Tool
    """

def stencil_fit_image_aspect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_repeat: bool | None = True,
    use_scale: bool | None = True,
    mask: bool | None = False,
) -> None:
    """When using an image texture, adjust the stencil size to fit the image aspect ratio

    :param use_repeat: Use Repeat, Use repeat mapping values
    :param use_scale: Use Scale, Use texture scale values
    :param mask: Modify Mask Stencil, Modify either the primary or mask stencil
    """

def stencil_reset_transform(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mask: bool | None = False,
) -> None:
    """Reset the stencil transformation to the default

    :param mask: Modify Mask Stencil, Modify either the primary or mask stencil
    """
