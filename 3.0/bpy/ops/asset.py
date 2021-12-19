import sys
import typing


def assign_action():
    ''' Set this pose Action as active Action on the active Object :file: addons/pose_library/operators.py\:213 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$213> _

    '''

    pass


def bundle_install(asset_library_ref: typing.Union[int, str] = '',
                   filepath: str = "",
                   hide_props_region: bool = True,
                   check_existing: bool = True,
                   filter_blender: bool = True,
                   filter_backup: bool = False,
                   filter_image: bool = False,
                   filter_movie: bool = False,
                   filter_python: bool = False,
                   filter_font: bool = False,
                   filter_sound: bool = False,
                   filter_text: bool = False,
                   filter_archive: bool = False,
                   filter_btx: bool = False,
                   filter_collada: bool = False,
                   filter_alembic: bool = False,
                   filter_usd: bool = False,
                   filter_volume: bool = False,
                   filter_folder: bool = True,
                   filter_blenlib: bool = False,
                   filemode: int = 8,
                   display_type: typing.Union[int, str] = 'DEFAULT',
                   sort_method: typing.Union[int, str] = ''):
    ''' Copy the current .blend file into an Asset Library. Only works on standalone .blend files (i.e. when no other files are referenced)

    :param asset_library_ref: asset_library_ref
    :type asset_library_ref: typing.Union[int, str]
    :param filepath: File Path, Path to file
    :type filepath: str
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: bool
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[int, str]
    '''

    pass


def catalog_delete(catalog_id: str = ""):
    ''' Remove an asset catalog from the asset library (contained assets will not be affected and show up as unassigned)

    :param catalog_id: Catalog ID, ID of the catalog to delete
    :type catalog_id: str
    '''

    pass


def catalog_new(parent_path: str = ""):
    ''' Create a new catalog to put assets in

    :param parent_path: Parent Path, Optional path defining the location to put the new catalog under
    :type parent_path: str
    '''

    pass


def catalog_redo():
    ''' Redo the last undone edit to the asset catalogs

    '''

    pass


def catalog_undo():
    ''' Undo the last edit to the asset catalogs

    '''

    pass


def catalog_undo_push():
    ''' Store the current state of the asset catalogs in the undo buffer

    '''

    pass


def catalogs_save():
    ''' Make any edits to any catalogs permanent by writing the current set up to the asset library

    '''

    pass


def clear(set_fake_user: bool = False):
    ''' Delete all asset metadata and turn the selected asset data-blocks back into normal data-blocks

    :param set_fake_user: Set Fake User, Ensure the data-block is saved, even when it is no longer marked as asset
    :type set_fake_user: bool
    '''

    pass


def library_refresh():
    ''' Reread assets and asset catalogs from the asset library on disk

    '''

    pass


def mark():
    ''' Enable easier reuse of selected data-blocks through the Asset Browser, with the help of customizable metadata (like previews, descriptions and tags)

    '''

    pass


def open_containing_blend_file():
    ''' Open the blend file that contains the active asset :file: startup/bl_operators/assets.py\:111 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/assets.py$111> _

    '''

    pass


def tag_add():
    ''' Add a new keyword tag to the active asset :file: startup/bl_operators/assets.py\:52 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/assets.py$52> _

    '''

    pass


def tag_remove():
    ''' Remove an existing keyword tag from the active asset :file: startup/bl_operators/assets.py\:75 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/assets.py$75> _

    '''

    pass
