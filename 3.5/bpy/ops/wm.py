import sys
import typing
import bpy.types
import bl_operators.wm

GenericType = typing.TypeVar("GenericType")


def alembic_export(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        check_existing: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blender: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_sound: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_collada: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_alembic: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        start: typing.Optional[typing.Any] = -2147483648,
        end: typing.Optional[typing.Any] = -2147483648,
        xsamples: typing.Optional[typing.Any] = 1,
        gsamples: typing.Optional[typing.Any] = 1,
        sh_open: typing.Optional[typing.Any] = 0.0,
        sh_close: typing.Optional[typing.Any] = 1.0,
        selected: typing.Optional[typing.Union[bool, typing.Any]] = False,
        visible_objects_only: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        flatten: typing.Optional[typing.Union[bool, typing.Any]] = False,
        uvs: typing.Optional[typing.Union[bool, typing.Any]] = True,
        packuv: typing.Optional[typing.Union[bool, typing.Any]] = True,
        normals: typing.Optional[typing.Union[bool, typing.Any]] = True,
        vcolors: typing.Optional[typing.Union[bool, typing.Any]] = False,
        orcos: typing.Optional[typing.Union[bool, typing.Any]] = True,
        face_sets: typing.Optional[typing.Union[bool, typing.Any]] = False,
        subdiv_schema: typing.Optional[typing.Union[bool, typing.Any]] = False,
        apply_subdiv: typing.Optional[typing.Union[bool, typing.Any]] = False,
        curves_as_mesh: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        use_instancing: typing.Optional[typing.Union[bool, typing.Any]] = True,
        global_scale: typing.Optional[typing.Any] = 1.0,
        triangulate: typing.Optional[typing.Union[bool, typing.Any]] = False,
        quad_method: typing.Optional[typing.
                                     Union[str, int]] = 'SHORTEST_DIAGONAL',
        ngon_method: typing.Optional[typing.Union[str, int]] = 'BEAUTY',
        export_hair: typing.Optional[typing.Union[bool, typing.Any]] = True,
        export_particles: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        export_custom_properties: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = True,
        as_background_job: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False,
        evaluation_mode: typing.Optional[typing.Any] = 'RENDER',
        init_scene_frame_range: typing.Optional[typing.Union[bool, typing.
                                                             Any]] = True):
    ''' Export current scene in an Alembic archive

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
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
    :param filter_python: Filter python files
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
    :param start: Start Frame, Start frame of the export, use the default value to take the start frame of the current scene
    :type start: typing.Optional[typing.Any]
    :param end: End Frame, End frame of the export, use the default value to take the end frame of the current scene
    :type end: typing.Optional[typing.Any]
    :param xsamples: Transform Samples, Number of times per frame transformations are sampled
    :type xsamples: typing.Optional[typing.Any]
    :param gsamples: Geometry Samples, Number of times per frame object data are sampled
    :type gsamples: typing.Optional[typing.Any]
    :param sh_open: Shutter Open, Time at which the shutter is open
    :type sh_open: typing.Optional[typing.Any]
    :param sh_close: Shutter Close, Time at which the shutter is closed
    :type sh_close: typing.Optional[typing.Any]
    :param selected: Selected Objects Only, Export only selected objects
    :type selected: typing.Optional[typing.Union[bool, typing.Any]]
    :param visible_objects_only: Visible Objects Only, Export only objects that are visible
    :type visible_objects_only: typing.Optional[typing.Union[bool, typing.Any]]
    :param flatten: Flatten Hierarchy, Do not preserve objects' parent/children relationship
    :type flatten: typing.Optional[typing.Union[bool, typing.Any]]
    :param uvs: UVs, Export UVs
    :type uvs: typing.Optional[typing.Union[bool, typing.Any]]
    :param packuv: Pack UV Islands, Export UVs with packed island
    :type packuv: typing.Optional[typing.Union[bool, typing.Any]]
    :param normals: Normals, Export normals
    :type normals: typing.Optional[typing.Union[bool, typing.Any]]
    :param vcolors: Color Attributes, Export color attributes
    :type vcolors: typing.Optional[typing.Union[bool, typing.Any]]
    :param orcos: Generated Coordinates, Export undeformed mesh vertex coordinates
    :type orcos: typing.Optional[typing.Union[bool, typing.Any]]
    :param face_sets: Face Sets, Export per face shading group assignments
    :type face_sets: typing.Optional[typing.Union[bool, typing.Any]]
    :param subdiv_schema: Use Subdivision Schema, Export meshes using Alembic's subdivision schema
    :type subdiv_schema: typing.Optional[typing.Union[bool, typing.Any]]
    :param apply_subdiv: Apply Subdivision Surface, Export subdivision surfaces as meshes
    :type apply_subdiv: typing.Optional[typing.Union[bool, typing.Any]]
    :param curves_as_mesh: Curves as Mesh, Export curves and NURBS surfaces as meshes
    :type curves_as_mesh: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_instancing: Use Instancing, Export data of duplicated objects as Alembic instances; speeds up the export and can be disabled for compatibility with other software
    :type use_instancing: typing.Optional[typing.Union[bool, typing.Any]]
    :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
    :type global_scale: typing.Optional[typing.Any]
    :param triangulate: Triangulate, Export polygons (quads and n-gons) as triangles
    :type triangulate: typing.Optional[typing.Union[bool, typing.Any]]
    :param quad_method: Quad Method, Method for splitting the quads into triangles
    :type quad_method: typing.Optional[typing.Union[str, int]]
    :param ngon_method: N-gon Method, Method for splitting the n-gons into triangles
    :type ngon_method: typing.Optional[typing.Union[str, int]]
    :param export_hair: Export Hair, Exports hair particle systems as animated curves
    :type export_hair: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_particles: Export Particles, Exports non-hair particle systems
    :type export_particles: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_custom_properties: Export Custom Properties, Export custom properties to Alembic .userProperties
    :type export_custom_properties: typing.Optional[typing.Union[bool, typing.Any]]
    :param as_background_job: Run as Background Job, Enable this to run the import in the background, disable to block Blender while importing. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job
    :type as_background_job: typing.Optional[typing.Union[bool, typing.Any]]
    :param evaluation_mode: Use Settings for, Determines visibility of objects, modifier settings, and other areas where there are different settings for viewport and rendering * ``RENDER`` Render -- Use Render settings for object visibility, modifier settings, etc. * ``VIEWPORT`` Viewport -- Use Viewport settings for object visibility, modifier settings, etc.
    :type evaluation_mode: typing.Optional[typing.Any]
    :type init_scene_frame_range: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def alembic_import(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
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
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_collada: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_alembic: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 8,
        relative_path: typing.Optional[typing.Union[bool, typing.Any]] = True,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        scale: typing.Optional[typing.Any] = 1.0,
        set_frame_range: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True,
        validate_meshes: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        always_add_cache_reader: typing.Optional[typing.Union[bool, typing.
                                                              Any]] = False,
        is_sequence: typing.Optional[typing.Union[bool, typing.Any]] = False,
        as_background_job: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False):
    ''' Load an Alembic archive

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
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
    :param filter_python: Filter python files
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
    :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
    :type scale: typing.Optional[typing.Any]
    :param set_frame_range: Set Frame Range, If checked, update scene's start and end frame to match those of the Alembic archive
    :type set_frame_range: typing.Optional[typing.Union[bool, typing.Any]]
    :param validate_meshes: Validate Meshes, Check imported mesh objects for invalid data (slow)
    :type validate_meshes: typing.Optional[typing.Union[bool, typing.Any]]
    :param always_add_cache_reader: Always Add Cache Reader, Add cache modifiers and constraints to imported objects even if they are not animated so that they can be updated when reloading the Alembic archive
    :type always_add_cache_reader: typing.Optional[typing.Union[bool, typing.Any]]
    :param is_sequence: Is Sequence, Set to true if the cache is split into separate files
    :type is_sequence: typing.Optional[typing.Union[bool, typing.Any]]
    :param as_background_job: Run as Background Job, Enable this to run the export in the background, disable to block Blender while exporting. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job
    :type as_background_job: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def append(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        directory: typing.Union[str, typing.Any] = "",
        filename: typing.Union[str, typing.Any] = "",
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
        check_existing: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_blender: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
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
        filter_blenlib: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filemode: typing.Optional[typing.Any] = 1,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        link: typing.Optional[typing.Union[bool, typing.Any]] = False,
        do_reuse_local_id: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False,
        clear_asset_data: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        autoselect: typing.Optional[typing.Union[bool, typing.Any]] = True,
        active_collection: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        instance_collections: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        instance_object_data: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = True,
        set_fake: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_recursive: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Append from a Library .blend file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param filename: File Name, Name of the file
    :type filename: typing.Union[str, typing.Any]
    :param files: Files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
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
    :param filter_python: Filter python files
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
    :param link: Link, Link the objects or data-blocks rather than appending
    :type link: typing.Optional[typing.Union[bool, typing.Any]]
    :param do_reuse_local_id: Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy
    :type do_reuse_local_id: typing.Optional[typing.Union[bool, typing.Any]]
    :param clear_asset_data: Clear Asset Data, Don't add asset meta-data or tags from the original data-block
    :type clear_asset_data: typing.Optional[typing.Union[bool, typing.Any]]
    :param autoselect: Select, Select new objects
    :type autoselect: typing.Optional[typing.Union[bool, typing.Any]]
    :param active_collection: Active Collection, Put new objects on the active collection
    :type active_collection: typing.Optional[typing.Union[bool, typing.Any]]
    :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
    :type instance_collections: typing.Optional[typing.Union[bool, typing.Any]]
    :param instance_object_data: Instance Object Data, Create instances for object data which are not referenced by any objects
    :type instance_object_data: typing.Optional[typing.Union[bool, typing.Any]]
    :param set_fake: Fake User, Set "Fake User" for appended items (except objects and collections)
    :type set_fake: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_recursive: Localize All, Localize all appended data, including those indirectly linked from other libraries
    :type use_recursive: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def batch_rename(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_type: typing.Optional[typing.Any] = 'OBJECT',
        data_source: typing.Optional[typing.Any] = 'SELECT',
        actions: typing.Optional[bpy.types.bpy_prop_collection[
            'bl_operators.wm.BatchRenameAction']] = None):
    ''' Rename multiple items at once

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_type: Type, Type of data to rename
    :type data_type: typing.Optional[typing.Any]
    :param data_source: Source
    :type data_source: typing.Optional[typing.Any]
    :param actions: actions
    :type actions: typing.Optional[bpy.types.bpy_prop_collection['bl_operators.wm.BatchRenameAction']]
    '''

    pass


def blend_strings_utf8_validate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Check and fix all strings in current .blend file to be valid UTF-8 Unicode (needed for some old, 2.4x area files) :file:`startup/bl_operators/file.py\:288 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/file.py#L288>`_

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def call_menu(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = ""):
    ''' Open a predefined menu

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the menu
    :type name: typing.Union[str, typing.Any]
    '''

    pass


def call_menu_pie(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = ""):
    ''' Open a predefined pie menu

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the pie menu
    :type name: typing.Union[str, typing.Any]
    '''

    pass


def call_panel(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "",
        keep_open: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Open a predefined panel

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the menu
    :type name: typing.Union[str, typing.Any]
    :param keep_open: Keep Open
    :type keep_open: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def collada_export(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        check_existing: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blender: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_sound: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_collada: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_alembic: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        prop_bc_export_ui_section: typing.Optional[typing.Any] = 'main',
        apply_modifiers: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        export_mesh_type: typing.Optional[typing.Any] = 0,
        export_mesh_type_selection: typing.Optional[typing.Any] = 'view',
        export_global_forward_selection: typing.Optional[typing.Any] = 'Y',
        export_global_up_selection: typing.Optional[typing.Any] = 'Z',
        apply_global_orientation: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = False,
        selected: typing.Optional[typing.Union[bool, typing.Any]] = False,
        include_children: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        include_armatures: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False,
        include_shapekeys: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False,
        deform_bones_only: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False,
        include_animations: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = True,
        include_all_actions: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = True,
        export_animation_type_selection: typing.Optional[typing.
                                                         Any] = 'sample',
        sampling_rate: typing.Optional[typing.Any] = 1,
        keep_smooth_curves: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = False,
        keep_keyframes: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        keep_flat_curves: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        active_uv_only: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        use_texture_copies: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = True,
        triangulate: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_object_instantiation: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = True,
        use_blender_profile: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = True,
        sort_by_name: typing.Optional[typing.Union[bool, typing.Any]] = False,
        export_object_transformation_type: typing.Optional[typing.Any] = 0,
        export_object_transformation_type_selection: typing.Optional[
            typing.Any] = 'matrix',
        export_animation_transformation_type: typing.Optional[typing.Any] = 0,
        export_animation_transformation_type_selection: typing.Optional[
            typing.Any] = 'matrix',
        open_sim: typing.Optional[typing.Union[bool, typing.Any]] = False,
        limit_precision: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        keep_bind_info: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False):
    ''' Save a Collada file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
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
    :param filter_python: Filter python files
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
    :param prop_bc_export_ui_section: Export Section, Only for User Interface organization * ``main`` Main -- Data export section. * ``geometry`` Geom -- Geometry export section. * ``armature`` Arm -- Armature export section. * ``animation`` Anim -- Animation export section. * ``collada`` Extra -- Collada export section.
    :type prop_bc_export_ui_section: typing.Optional[typing.Any]
    :param apply_modifiers: Apply Modifiers, Apply modifiers to exported mesh (non destructive))
    :type apply_modifiers: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_mesh_type: Resolution, Modifier resolution for export
    :type export_mesh_type: typing.Optional[typing.Any]
    :param export_mesh_type_selection: Resolution, Modifier resolution for export * ``view`` Viewport -- Apply modifier's viewport settings. * ``render`` Render -- Apply modifier's render settings.
    :type export_mesh_type_selection: typing.Optional[typing.Any]
    :param export_global_forward_selection: Global Forward Axis, Global Forward axis for export * ``X`` X -- Global Forward is positive X Axis. * ``Y`` Y -- Global Forward is positive Y Axis. * ``Z`` Z -- Global Forward is positive Z Axis. * ``-X`` -X -- Global Forward is negative X Axis. * ``-Y`` -Y -- Global Forward is negative Y Axis. * ``-Z`` -Z -- Global Forward is negative Z Axis.
    :type export_global_forward_selection: typing.Optional[typing.Any]
    :param export_global_up_selection: Global Up Axis, Global Up axis for export * ``X`` X -- Global UP is positive X Axis. * ``Y`` Y -- Global UP is positive Y Axis. * ``Z`` Z -- Global UP is positive Z Axis. * ``-X`` -X -- Global UP is negative X Axis. * ``-Y`` -Y -- Global UP is negative Y Axis. * ``-Z`` -Z -- Global UP is negative Z Axis.
    :type export_global_up_selection: typing.Optional[typing.Any]
    :param apply_global_orientation: Apply Global Orientation, Rotate all root objects to match the global orientation settings otherwise set the global orientation per Collada asset
    :type apply_global_orientation: typing.Optional[typing.Union[bool, typing.Any]]
    :param selected: Selection Only, Export only selected elements
    :type selected: typing.Optional[typing.Union[bool, typing.Any]]
    :param include_children: Include Children, Export all children of selected objects (even if not selected)
    :type include_children: typing.Optional[typing.Union[bool, typing.Any]]
    :param include_armatures: Include Armatures, Export related armatures (even if not selected)
    :type include_armatures: typing.Optional[typing.Union[bool, typing.Any]]
    :param include_shapekeys: Include Shape Keys, Export all Shape Keys from Mesh Objects
    :type include_shapekeys: typing.Optional[typing.Union[bool, typing.Any]]
    :param deform_bones_only: Deform Bones Only, Only export deforming bones with armatures
    :type deform_bones_only: typing.Optional[typing.Union[bool, typing.Any]]
    :param include_animations: Include Animations, Export animations if available (exporting animations will enforce the decomposition of node transforms into <translation> <rotation> and <scale> components)
    :type include_animations: typing.Optional[typing.Union[bool, typing.Any]]
    :param include_all_actions: Include all Actions, Export also unassigned actions (this allows you to export entire animation libraries for your character(s))
    :type include_all_actions: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_animation_type_selection: Key Type, Type for exported animations (use sample keys or Curve keys) * ``sample`` Samples -- Export Sampled points guided by sampling rate. * ``keys`` Curves -- Export Curves (note: guided by curve keys).
    :type export_animation_type_selection: typing.Optional[typing.Any]
    :param sampling_rate: Sampling Rate, The distance between 2 keyframes (1 to key every frame)
    :type sampling_rate: typing.Optional[typing.Any]
    :param keep_smooth_curves: Keep Smooth curves, Export also the curve handles (if available) (this does only work when the inverse parent matrix is the unity matrix, otherwise you may end up with odd results)
    :type keep_smooth_curves: typing.Optional[typing.Union[bool, typing.Any]]
    :param keep_keyframes: Keep Keyframes, Use existing keyframes as additional sample points (this helps when you want to keep manual tweaks)
    :type keep_keyframes: typing.Optional[typing.Union[bool, typing.Any]]
    :param keep_flat_curves: All Keyed Curves, Export also curves which have only one key or are totally flat
    :type keep_flat_curves: typing.Optional[typing.Union[bool, typing.Any]]
    :param active_uv_only: Only Selected UV Map, Export only the selected UV Map
    :type active_uv_only: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_texture_copies: Copy, Copy textures to same folder where the .dae file is exported
    :type use_texture_copies: typing.Optional[typing.Union[bool, typing.Any]]
    :param triangulate: Triangulate, Export polygons (quads and n-gons) as triangles
    :type triangulate: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_object_instantiation: Use Object Instances, Instantiate multiple Objects from same Data
    :type use_object_instantiation: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_blender_profile: Use Blender Profile, Export additional Blender specific information (for material, shaders, bones, etc.)
    :type use_blender_profile: typing.Optional[typing.Union[bool, typing.Any]]
    :param sort_by_name: Sort by Object name, Sort exported data by Object name
    :type sort_by_name: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_object_transformation_type: Transform, Object Transformation type for translation, scale and rotation
    :type export_object_transformation_type: typing.Optional[typing.Any]
    :param export_object_transformation_type_selection: Transform, Object Transformation type for translation, scale and rotation * ``matrix`` Matrix -- Use <matrix> representation for exported transformations. * ``decomposed`` Decomposed -- Use <rotate>, <translate> and <scale> representation for exported transformations.
    :type export_object_transformation_type_selection: typing.Optional[typing.Any]
    :param export_animation_transformation_type: The Animation transformation type in the Anim Tab is always equal to the Object transformation type in the Geom tab
    :type export_animation_transformation_type: typing.Optional[typing.Any]
    :param export_animation_transformation_type_selection: The Animation transformation type in the Anim Tab is always equal to the Object transformation type in the Geom tab * ``matrix`` Matrix -- Use <matrix> representation for exported transformations. * ``decomposed`` Decomposed -- Use <rotate>, <translate> and <scale> representation for exported transformations.
    :type export_animation_transformation_type_selection: typing.Optional[typing.Any]
    :param open_sim: Export to SL/OpenSim, Compatibility mode for SL, OpenSim and other compatible online worlds
    :type open_sim: typing.Optional[typing.Union[bool, typing.Any]]
    :param limit_precision: Limit Precision, Reduce the precision of the exported data to 6 digits
    :type limit_precision: typing.Optional[typing.Union[bool, typing.Any]]
    :param keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export
    :type keep_bind_info: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def collada_import(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
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
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_collada: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_alembic: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        import_units: typing.Optional[typing.Union[bool, typing.Any]] = False,
        custom_normals: typing.Optional[typing.Union[bool, typing.Any]] = True,
        fix_orientation: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        find_chains: typing.Optional[typing.Union[bool, typing.Any]] = False,
        auto_connect: typing.Optional[typing.Union[bool, typing.Any]] = False,
        min_chain_length: typing.Optional[typing.Any] = 0,
        keep_bind_info: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False):
    ''' Load a Collada file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
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
    :param filter_python: Filter python files
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
    :param import_units: Import Units, If disabled match import to Blender's current Unit settings, otherwise use the settings from the Imported scene
    :type import_units: typing.Optional[typing.Union[bool, typing.Any]]
    :param custom_normals: Custom Normals, Import custom normals, if available (otherwise Blender will compute them)
    :type custom_normals: typing.Optional[typing.Union[bool, typing.Any]]
    :param fix_orientation: Fix Leaf Bones, Fix Orientation of Leaf Bones (Collada does only support Joints)
    :type fix_orientation: typing.Optional[typing.Union[bool, typing.Any]]
    :param find_chains: Find Bone Chains, Find best matching Bone Chains and ensure bones in chain are connected
    :type find_chains: typing.Optional[typing.Union[bool, typing.Any]]
    :param auto_connect: Auto Connect, Set use_connect for parent bones which have exactly one child bone
    :type auto_connect: typing.Optional[typing.Union[bool, typing.Any]]
    :param min_chain_length: Minimum Chain Length, When searching Bone Chains disregard chains of length below this value
    :type min_chain_length: typing.Optional[typing.Any]
    :param keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export
    :type keep_bind_info: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def context_collection_boolean_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path_iter: typing.Union[str, typing.Any] = "",
        data_path_item: typing.Union[str, typing.Any] = "",
        type: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Set boolean values for a collection of items

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
    :type data_path_iter: typing.Union[str, typing.Any]
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float)
    :type data_path_item: typing.Union[str, typing.Any]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def context_cycle_array(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        reverse: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Set a context array value (useful for cycling the active mesh edit mode)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: typing.Union[str, typing.Any]
    :param reverse: Reverse, Cycle backwards
    :type reverse: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def context_cycle_enum(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        reverse: typing.Optional[typing.Union[bool, typing.Any]] = False,
        wrap: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Toggle a context value

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: typing.Union[str, typing.Any]
    :param reverse: Reverse, Cycle backwards
    :type reverse: typing.Optional[typing.Union[bool, typing.Any]]
    :param wrap: Wrap, Wrap back to the first/last values
    :type wrap: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def context_cycle_int(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        reverse: typing.Optional[typing.Union[bool, typing.Any]] = False,
        wrap: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Set a context value (useful for cycling active material, shape keys, groups, etc.)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: typing.Union[str, typing.Any]
    :param reverse: Reverse, Cycle backwards
    :type reverse: typing.Optional[typing.Union[bool, typing.Any]]
    :param wrap: Wrap, Wrap back to the first/last values
    :type wrap: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def context_menu_enum(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = ""):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: typing.Union[str, typing.Any]
    '''

    pass


def context_modal_mouse(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path_iter: typing.Union[str, typing.Any] = "",
        data_path_item: typing.Union[str, typing.Any] = "",
        header_text: typing.Union[str, typing.Any] = "",
        input_scale: typing.Optional[typing.Any] = 0.01,
        invert: typing.Optional[typing.Union[bool, typing.Any]] = False,
        initial_x: typing.Optional[typing.Any] = 0):
    ''' Adjust arbitrary values with mouse input

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
    :type data_path_iter: typing.Union[str, typing.Any]
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float)
    :type data_path_item: typing.Union[str, typing.Any]
    :param header_text: Header Text, Text to display in header during scale
    :type header_text: typing.Union[str, typing.Any]
    :param input_scale: input_scale, Scale the mouse movement by this value before applying the delta
    :type input_scale: typing.Optional[typing.Any]
    :param invert: invert, Invert the mouse input
    :type invert: typing.Optional[typing.Union[bool, typing.Any]]
    :param initial_x: initial_x
    :type initial_x: typing.Optional[typing.Any]
    '''

    pass


def context_pie_enum(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = ""):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: typing.Union[str, typing.Any]
    '''

    pass


def context_scale_float(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        value: typing.Optional[typing.Any] = 1.0):
    ''' Scale a float context value

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assign value
    :type value: typing.Optional[typing.Any]
    '''

    pass


def context_scale_int(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        value: typing.Optional[typing.Any] = 1.0,
        always_step: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Scale an int context value

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assign value
    :type value: typing.Optional[typing.Any]
    :param always_step: Always Step, Always adjust the value by a minimum of 1 when 'value' is not 1.0
    :type always_step: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def context_set_boolean(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        value: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Set a context value

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assignment value
    :type value: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def context_set_enum(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        value: typing.Union[str, typing.Any] = ""):
    ''' Set a context value

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assignment value (as a string)
    :type value: typing.Union[str, typing.Any]
    '''

    pass


def context_set_float(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        value: typing.Optional[typing.Any] = 0.0,
        relative: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Set a context value

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assignment value
    :type value: typing.Optional[typing.Any]
    :param relative: Relative, Apply relative to the current value (delta)
    :type relative: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def context_set_id(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        value: typing.Union[str, typing.Any] = ""):
    ''' Set a context value to an ID data-block

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assign value
    :type value: typing.Union[str, typing.Any]
    '''

    pass


def context_set_int(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        value: typing.Optional[typing.Any] = 0,
        relative: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Set a context value

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assign value
    :type value: typing.Optional[typing.Any]
    :param relative: Relative, Apply relative to the current value (delta)
    :type relative: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def context_set_string(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        value: typing.Union[str, typing.Any] = ""):
    ''' Set a context value

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assign value
    :type value: typing.Union[str, typing.Any]
    '''

    pass


def context_set_value(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        value: typing.Union[str, typing.Any] = ""):
    ''' Set a context value

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assignment value (as a string)
    :type value: typing.Union[str, typing.Any]
    '''

    pass


def context_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        module: typing.Union[str, typing.Any] = ""):
    ''' Toggle a context value

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: typing.Union[str, typing.Any]
    :param module: Module, Optionally override the context with a module
    :type module: typing.Union[str, typing.Any]
    '''

    pass


def context_toggle_enum(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        value_1: typing.Union[str, typing.Any] = "",
        value_2: typing.Union[str, typing.Any] = ""):
    ''' Toggle a context value

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: typing.Union[str, typing.Any]
    :param value_1: Value, Toggle enum
    :type value_1: typing.Union[str, typing.Any]
    :param value_2: Value, Toggle enum
    :type value_2: typing.Union[str, typing.Any]
    '''

    pass


def debug_menu(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        debug_value: typing.Optional[typing.Any] = 0):
    ''' Open a popup to set the debug level

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param debug_value: Debug Value
    :type debug_value: typing.Optional[typing.Any]
    '''

    pass


def doc_view(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None,
             *,
             doc_id: typing.Union[str, typing.Any] = ""):
    ''' Open online reference docs in a web browser

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param doc_id: Doc ID
    :type doc_id: typing.Union[str, typing.Any]
    '''

    pass


def doc_view_manual(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        doc_id: typing.Union[str, typing.Any] = ""):
    ''' Load online manual

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param doc_id: Doc ID
    :type doc_id: typing.Union[str, typing.Any]
    '''

    pass


def doc_view_manual_ui_context(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' View a context based online manual in a web browser

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def drop_blend_file(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = ""):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: filepath
    :type filepath: typing.Union[str, typing.Any]
    '''

    pass


def gpencil_export_pdf(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        check_existing: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blender: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
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
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        use_fill: typing.Optional[typing.Union[bool, typing.Any]] = True,
        selected_object_type: typing.Optional[typing.Any] = 'SELECTED',
        stroke_sample: typing.Optional[typing.Any] = 0.0,
        use_normalized_thickness: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = False,
        frame_mode: typing.Optional[typing.Any] = 'ACTIVE'):
    ''' Export grease pencil to PDF

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
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
    :param filter_python: Filter python files
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
    :param use_fill: Fill, Export strokes with fill enabled
    :type use_fill: typing.Optional[typing.Union[bool, typing.Any]]
    :param selected_object_type: Object, Which objects to include in the export * ``ACTIVE`` Active -- Include only the active object. * ``SELECTED`` Selected -- Include selected objects. * ``VISIBLE`` Visible -- Include all visible objects.
    :type selected_object_type: typing.Optional[typing.Any]
    :param stroke_sample: Sampling, Precision of stroke sampling. Low values mean a more precise result, and zero disables sampling
    :type stroke_sample: typing.Optional[typing.Any]
    :param use_normalized_thickness: Normalize, Export strokes with constant thickness
    :type use_normalized_thickness: typing.Optional[typing.Union[bool, typing.Any]]
    :param frame_mode: Frames, Which frames to include in the export * ``ACTIVE`` Active -- Include only active frame. * ``SELECTED`` Selected -- Include selected frames. * ``SCENE`` Scene -- Include all scene frames.
    :type frame_mode: typing.Optional[typing.Any]
    '''

    pass


def gpencil_export_svg(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        check_existing: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blender: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
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
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        use_fill: typing.Optional[typing.Union[bool, typing.Any]] = True,
        selected_object_type: typing.Optional[typing.Any] = 'SELECTED',
        stroke_sample: typing.Optional[typing.Any] = 0.0,
        use_normalized_thickness: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = False,
        use_clip_camera: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False):
    ''' Export grease pencil to SVG

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
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
    :param filter_python: Filter python files
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
    :param use_fill: Fill, Export strokes with fill enabled
    :type use_fill: typing.Optional[typing.Union[bool, typing.Any]]
    :param selected_object_type: Object, Which objects to include in the export * ``ACTIVE`` Active -- Include only the active object. * ``SELECTED`` Selected -- Include selected objects. * ``VISIBLE`` Visible -- Include all visible objects.
    :type selected_object_type: typing.Optional[typing.Any]
    :param stroke_sample: Sampling, Precision of stroke sampling. Low values mean a more precise result, and zero disables sampling
    :type stroke_sample: typing.Optional[typing.Any]
    :param use_normalized_thickness: Normalize, Export strokes with constant thickness
    :type use_normalized_thickness: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_clip_camera: Clip Camera, Clip drawings to camera size when export in camera view
    :type use_clip_camera: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def gpencil_import_svg(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        directory: typing.Union[str, typing.Any] = "",
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
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
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_collada: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_alembic: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 8,
        relative_path: typing.Optional[typing.Union[bool, typing.Any]] = True,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        resolution: typing.Optional[typing.Any] = 10,
        scale: typing.Optional[typing.Any] = 10.0):
    ''' Import SVG into grease pencil

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param files: Files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
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
    :param filter_python: Filter python files
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
    :param resolution: Resolution, Resolution of the generated strokes
    :type resolution: typing.Optional[typing.Any]
    :param scale: Scale, Scale of the final strokes
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def interface_theme_preset_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "",
        remove_name: typing.Optional[typing.Union[bool, typing.Any]] = False,
        remove_active: typing.Optional[typing.Union[bool, typing.
                                                    Any]] = False):
    ''' Add or remove a theme preset

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the preset, used to make the path name
    :type name: typing.Union[str, typing.Any]
    :param remove_name: remove_name
    :type remove_name: typing.Optional[typing.Union[bool, typing.Any]]
    :param remove_active: remove_active
    :type remove_active: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def keyconfig_preset_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "",
        remove_name: typing.Optional[typing.Union[bool, typing.Any]] = False,
        remove_active: typing.Optional[typing.Union[bool, typing.
                                                    Any]] = False):
    ''' Add or remove a Key-config Preset

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the preset, used to make the path name
    :type name: typing.Union[str, typing.Any]
    :param remove_name: remove_name
    :type remove_name: typing.Optional[typing.Union[bool, typing.Any]]
    :param remove_active: remove_active
    :type remove_active: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def lib_reload(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        library: typing.Union[str, typing.Any] = "",
        filepath: typing.Union[str, typing.Any] = "",
        directory: typing.Union[str, typing.Any] = "",
        filename: typing.Union[str, typing.Any] = "",
        hide_props_region: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        check_existing: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_blender: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
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
        filemode: typing.Optional[typing.Any] = 8,
        relative_path: typing.Optional[typing.Union[bool, typing.Any]] = True,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Reload the given library

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param library: Library, Library to reload
    :type library: typing.Union[str, typing.Any]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param filename: File Name, Name of the file
    :type filename: typing.Union[str, typing.Any]
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
    :param filter_python: Filter python files
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


def lib_relocate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        library: typing.Union[str, typing.Any] = "",
        filepath: typing.Union[str, typing.Any] = "",
        directory: typing.Union[str, typing.Any] = "",
        filename: typing.Union[str, typing.Any] = "",
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
        hide_props_region: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        check_existing: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_blender: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
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
        filemode: typing.Optional[typing.Any] = 8,
        relative_path: typing.Optional[typing.Union[bool, typing.Any]] = True,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Relocate the given library to one or several others

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param library: Library, Library to relocate
    :type library: typing.Union[str, typing.Any]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param filename: File Name, Name of the file
    :type filename: typing.Union[str, typing.Any]
    :param files: Files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
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
    :param filter_python: Filter python files
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


def link(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        directory: typing.Union[str, typing.Any] = "",
        filename: typing.Union[str, typing.Any] = "",
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
        check_existing: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_blender: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
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
        filter_blenlib: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filemode: typing.Optional[typing.Any] = 1,
        relative_path: typing.Optional[typing.Union[bool, typing.Any]] = True,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        link: typing.Optional[typing.Union[bool, typing.Any]] = True,
        do_reuse_local_id: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False,
        clear_asset_data: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        autoselect: typing.Optional[typing.Union[bool, typing.Any]] = True,
        active_collection: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        instance_collections: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = True,
        instance_object_data: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = True):
    ''' Link from a Library .blend file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param filename: File Name, Name of the file
    :type filename: typing.Union[str, typing.Any]
    :param files: Files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
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
    :param filter_python: Filter python files
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
    :param link: Link, Link the objects or data-blocks rather than appending
    :type link: typing.Optional[typing.Union[bool, typing.Any]]
    :param do_reuse_local_id: Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy
    :type do_reuse_local_id: typing.Optional[typing.Union[bool, typing.Any]]
    :param clear_asset_data: Clear Asset Data, Don't add asset meta-data or tags from the original data-block
    :type clear_asset_data: typing.Optional[typing.Union[bool, typing.Any]]
    :param autoselect: Select, Select new objects
    :type autoselect: typing.Optional[typing.Union[bool, typing.Any]]
    :param active_collection: Active Collection, Put new objects on the active collection
    :type active_collection: typing.Optional[typing.Union[bool, typing.Any]]
    :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
    :type instance_collections: typing.Optional[typing.Union[bool, typing.Any]]
    :param instance_object_data: Instance Object Data, Create instances for object data which are not referenced by any objects
    :type instance_object_data: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def memory_statistics(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Print memory statistics to the console

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def obj_export(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        check_existing: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blender: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
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
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        export_animation: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        start_frame: typing.Optional[typing.Any] = -2147483648,
        end_frame: typing.Optional[typing.Any] = 2147483647,
        forward_axis: typing.Optional[typing.Any] = 'NEGATIVE_Z',
        up_axis: typing.Optional[typing.Any] = 'Y',
        global_scale: typing.Optional[typing.Any] = 1.0,
        apply_modifiers: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True,
        export_eval_mode: typing.Optional[typing.Any] = 'DAG_EVAL_VIEWPORT',
        export_selected_objects: typing.Optional[typing.Union[bool, typing.
                                                              Any]] = False,
        export_uv: typing.Optional[typing.Union[bool, typing.Any]] = True,
        export_normals: typing.Optional[typing.Union[bool, typing.Any]] = True,
        export_colors: typing.Optional[typing.Union[bool, typing.Any]] = False,
        export_materials: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        export_pbr_extensions: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
        path_mode: typing.Optional[typing.Any] = 'AUTO',
        export_triangulated_mesh: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = False,
        export_curves_as_nurbs: typing.Optional[typing.Union[bool, typing.
                                                             Any]] = False,
        export_object_groups: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        export_material_groups: typing.Optional[typing.Union[bool, typing.
                                                             Any]] = False,
        export_vertex_groups: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        export_smooth_groups: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        smooth_group_bitflags: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
        filter_glob: typing.Union[str, typing.Any] = "*.obj;*.mtl"):
    ''' Save the scene to a Wavefront OBJ file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
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
    :param filter_python: Filter python files
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
    :param export_animation: Export Animation, Export multiple frames instead of the current frame only
    :type export_animation: typing.Optional[typing.Union[bool, typing.Any]]
    :param start_frame: Start Frame, The first frame to be exported
    :type start_frame: typing.Optional[typing.Any]
    :param end_frame: End Frame, The last frame to be exported
    :type end_frame: typing.Optional[typing.Any]
    :param forward_axis: Forward Axis * ``X`` X -- Positive X axis. * ``Y`` Y -- Positive Y axis. * ``Z`` Z -- Positive Z axis. * ``NEGATIVE_X`` -X -- Negative X axis. * ``NEGATIVE_Y`` -Y -- Negative Y axis. * ``NEGATIVE_Z`` -Z -- Negative Z axis.
    :type forward_axis: typing.Optional[typing.Any]
    :param up_axis: Up Axis * ``X`` X -- Positive X axis. * ``Y`` Y -- Positive Y axis. * ``Z`` Z -- Positive Z axis. * ``NEGATIVE_X`` -X -- Negative X axis. * ``NEGATIVE_Y`` -Y -- Negative Y axis. * ``NEGATIVE_Z`` -Z -- Negative Z axis.
    :type up_axis: typing.Optional[typing.Any]
    :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
    :type global_scale: typing.Optional[typing.Any]
    :param apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes
    :type apply_modifiers: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_eval_mode: Object Properties, Determines properties like object visibility, modifiers etc., where they differ for Render and Viewport * ``DAG_EVAL_RENDER`` Render -- Export objects as they appear in render. * ``DAG_EVAL_VIEWPORT`` Viewport -- Export objects as they appear in the viewport.
    :type export_eval_mode: typing.Optional[typing.Any]
    :param export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects
    :type export_selected_objects: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_uv: Export UVs
    :type export_uv: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_normals: Export Normals, Export per-face normals if the face is flat-shaded, per-face-per-loop normals if smooth-shaded
    :type export_normals: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_colors: Export Colors, Export per-vertex colors
    :type export_colors: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_materials: Export Materials, Export MTL library. There must be a Principled-BSDF node for image textures to be exported to the MTL file
    :type export_materials: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_pbr_extensions: Export Materials with PBR Extensions, Export MTL library using PBR extensions (roughness, metallic, sheen, clearcoat, anisotropy, transmission)
    :type export_pbr_extensions: typing.Optional[typing.Union[bool, typing.Any]]
    :param path_mode: Path Mode, Method used to reference paths * ``AUTO`` Auto -- Use relative paths with subdirectories only. * ``ABSOLUTE`` Absolute -- Always write absolute paths. * ``RELATIVE`` Relative -- Write relative paths where possible. * ``MATCH`` Match -- Match absolute/relative setting with input path. * ``STRIP`` Strip -- Write filename only. * ``COPY`` Copy -- Copy the file to the destination path.
    :type path_mode: typing.Optional[typing.Any]
    :param export_triangulated_mesh: 4
    :type export_triangulated_mesh: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_curves_as_nurbs: Export Curves as NURBS, Export curves in parametric form instead of exporting as mesh
    :type export_curves_as_nurbs: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_object_groups: Export Object Groups, Append mesh name to object name, separated by a '_'
    :type export_object_groups: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_material_groups: Export Material Groups, Generate an OBJ group for each part of a geometry using a different material
    :type export_material_groups: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_vertex_groups: Export Vertex Groups, Export the name of the vertex group of a face. It is approximated by choosing the vertex group with the most members among the vertices of a face
    :type export_vertex_groups: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_smooth_groups: Export Smooth Groups, Every smooth-shaded face is assigned group "1" and every flat-shaded face "off"
    :type export_smooth_groups: typing.Optional[typing.Union[bool, typing.Any]]
    :param smooth_group_bitflags: Generate Bitflags for Smooth Groups
    :type smooth_group_bitflags: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_glob: Extension Filter
    :type filter_glob: typing.Union[str, typing.Any]
    '''

    pass


def obj_import(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        directory: typing.Union[str, typing.Any] = "",
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
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
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        global_scale: typing.Optional[typing.Any] = 1.0,
        clamp_size: typing.Optional[typing.Any] = 0.0,
        forward_axis: typing.Optional[typing.Any] = 'NEGATIVE_Z',
        up_axis: typing.Optional[typing.Any] = 'Y',
        use_split_objects: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        use_split_groups: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        import_vertex_groups: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        validate_meshes: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        filter_glob: typing.Union[str, typing.Any] = "*.obj;*.mtl"):
    ''' Load a Wavefront OBJ scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param files: Files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
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
    :param filter_python: Filter python files
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
    :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
    :type global_scale: typing.Optional[typing.Any]
    :param clamp_size: Clamp Bounding Box, Resize the objects to keep bounding box under this value. Value 0 disables clamping
    :type clamp_size: typing.Optional[typing.Any]
    :param forward_axis: Forward Axis * ``X`` X -- Positive X axis. * ``Y`` Y -- Positive Y axis. * ``Z`` Z -- Positive Z axis. * ``NEGATIVE_X`` -X -- Negative X axis. * ``NEGATIVE_Y`` -Y -- Negative Y axis. * ``NEGATIVE_Z`` -Z -- Negative Z axis.
    :type forward_axis: typing.Optional[typing.Any]
    :param up_axis: Up Axis * ``X`` X -- Positive X axis. * ``Y`` Y -- Positive Y axis. * ``Z`` Z -- Positive Z axis. * ``NEGATIVE_X`` -X -- Negative X axis. * ``NEGATIVE_Y`` -Y -- Negative Y axis. * ``NEGATIVE_Z`` -Z -- Negative Z axis.
    :type up_axis: typing.Optional[typing.Any]
    :param use_split_objects: Split By Object, Import each OBJ 'o' as a separate object
    :type use_split_objects: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_split_groups: Split By Group, Import each OBJ 'g' as a separate object
    :type use_split_groups: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_vertex_groups: Vertex Groups, Import OBJ groups as vertex groups
    :type import_vertex_groups: typing.Optional[typing.Union[bool, typing.Any]]
    :param validate_meshes: Validate Meshes, Check imported mesh objects for invalid data (slow)
    :type validate_meshes: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_glob: Extension Filter
    :type filter_glob: typing.Union[str, typing.Any]
    '''

    pass


def open_mainfile(
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
        filter_blender: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
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
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        load_ui: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_scripts: typing.Optional[typing.Union[bool, typing.Any]] = True,
        display_file_selector: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = True,
        state: typing.Optional[typing.Any] = 0):
    ''' Open a Blender file

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
    :param filter_python: Filter python files
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
    :param load_ui: Load UI, Load user interface setup in the .blend file
    :type load_ui: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: typing.Optional[typing.Union[bool, typing.Any]]
    :param display_file_selector: Display File Selector
    :type display_file_selector: typing.Optional[typing.Union[bool, typing.Any]]
    :param state: State
    :type state: typing.Optional[typing.Any]
    '''

    pass


def operator_cheat_sheet(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' List all the operators in a text-block, useful for scripting :file:`startup/bl_operators/wm.py\:2125 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2125>`_

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def operator_defaults(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Set the active operator to its default values

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def operator_pie_enum(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        prop_string: typing.Union[str, typing.Any] = ""):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Operator, Operator name (in python as string)
    :type data_path: typing.Union[str, typing.Any]
    :param prop_string: Property, Property name (as a string)
    :type prop_string: typing.Union[str, typing.Any]
    '''

    pass


def operator_preset_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "",
        remove_name: typing.Optional[typing.Union[bool, typing.Any]] = False,
        remove_active: typing.Optional[typing.Union[bool, typing.Any]] = False,
        operator: typing.Union[str, typing.Any] = ""):
    ''' Add or remove an Operator Preset

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the preset, used to make the path name
    :type name: typing.Union[str, typing.Any]
    :param remove_name: remove_name
    :type remove_name: typing.Optional[typing.Union[bool, typing.Any]]
    :param remove_active: remove_active
    :type remove_active: typing.Optional[typing.Union[bool, typing.Any]]
    :param operator: Operator
    :type operator: typing.Union[str, typing.Any]
    '''

    pass


def owner_disable(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        owner_id: typing.Union[str, typing.Any] = ""):
    ''' Disable add-on for workspace

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param owner_id: UI Tag
    :type owner_id: typing.Union[str, typing.Any]
    '''

    pass


def owner_enable(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        owner_id: typing.Union[str, typing.Any] = ""):
    ''' Enable add-on for workspace

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param owner_id: UI Tag
    :type owner_id: typing.Union[str, typing.Any]
    '''

    pass


def path_open(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = ""):
    ''' Open a path in a file browser

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: filepath
    :type filepath: typing.Union[str, typing.Any]
    '''

    pass


def previews_batch_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
        directory: typing.Union[str, typing.Any] = "",
        filter_blender: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_scenes: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_collections: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True,
        use_objects: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_intern_data: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True,
        use_trusted: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_backups: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Clear selected .blend file's previews

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param files: files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
    :param directory: directory
    :type directory: typing.Union[str, typing.Any]
    :param filter_blender: filter_blender
    :type filter_blender: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_folder: filter_folder
    :type filter_folder: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_scenes: Scenes, Clear scenes' previews
    :type use_scenes: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_collections: Collections, Clear collections' previews
    :type use_collections: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_objects: Objects, Clear objects' previews
    :type use_objects: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_intern_data: Materials & Textures, Clear 'internal' previews (materials, textures, images, etc.)
    :type use_intern_data: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_trusted: Trusted Blend Files, Enable python evaluation for selected files
    :type use_trusted: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with cleared previews
    :type use_backups: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def previews_batch_generate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
        directory: typing.Union[str, typing.Any] = "",
        filter_blender: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_scenes: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_collections: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True,
        use_objects: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_intern_data: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True,
        use_trusted: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_backups: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Generate selected .blend file's previews

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param files: Collection of file paths with common `directory` root
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
    :param directory: Root path of all files listed in `files` collection
    :type directory: typing.Union[str, typing.Any]
    :param filter_blender: Show Blender files in the File Browser
    :type filter_blender: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_folder: Show folders in the File Browser
    :type filter_folder: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_scenes: Scenes, Generate scenes' previews
    :type use_scenes: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_collections: Collections, Generate collections' previews
    :type use_collections: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_objects: Objects, Generate objects' previews
    :type use_objects: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_intern_data: Materials & Textures, Generate 'internal' previews (materials, textures, images, etc.)
    :type use_intern_data: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_trusted: Trusted Blend Files, Enable python evaluation for selected files
    :type use_trusted: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with generated previews
    :type use_backups: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def previews_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        id_type: typing.Optional[typing.Any] = {}):
    ''' Clear data-block previews (only for some types like objects, materials, textures, etc.)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param id_type: Data-Block Type, Which data-block previews to clear * ``ALL`` All Types. * ``GEOMETRY`` All Geometry Types -- Clear previews for scenes, collections and objects. * ``SHADING`` All Shading Types -- Clear previews for materials, lights, worlds, textures and images. * ``SCENE`` Scenes. * ``COLLECTION`` Collections. * ``OBJECT`` Objects. * ``MATERIAL`` Materials. * ``LIGHT`` Lights. * ``WORLD`` Worlds. * ``TEXTURE`` Textures. * ``IMAGE`` Images.
    :type id_type: typing.Optional[typing.Any]
    '''

    pass


def previews_ensure(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Ensure data-block previews are available and up-to-date (to be saved in .blend file, only for some types like materials, textures, etc.)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def properties_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = ""):
    ''' Add your own property to the data-block

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Property Edit, Property data_path edit
    :type data_path: typing.Union[str, typing.Any]
    '''

    pass


def properties_context_change(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        context: typing.Union[str, typing.Any] = ""):
    ''' Jump to a different tab inside the properties editor

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param context: Context
    :type context: typing.Union[str, typing.Any]
    '''

    pass


def properties_edit(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        property_name: typing.Union[str, typing.Any] = "",
        property_type: typing.Optional[typing.Any] = 'FLOAT',
        is_overridable_library: typing.Optional[typing.Union[bool, typing.
                                                             Any]] = False,
        description: typing.Union[str, typing.Any] = "",
        use_soft_limits: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        array_length: typing.Optional[typing.Any] = 3,
        default_int: typing.Optional[typing.Any] = (0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                    0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                    0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                    0, 0, 0, 0, 0),
        min_int: typing.Optional[typing.Any] = -10000,
        max_int: typing.Optional[typing.Any] = 10000,
        soft_min_int: typing.Optional[typing.Any] = -10000,
        soft_max_int: typing.Optional[typing.Any] = 10000,
        step_int: typing.Optional[typing.Any] = 1,
        default_bool: typing.
        Optional[typing.Union[typing.List[bool], typing.Any]] = (
            False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False),
        default_float: typing.Optional[typing.Any] = (0.0, 0.0, 0.0, 0.0, 0.0,
                                                      0.0, 0.0, 0.0, 0.0, 0.0,
                                                      0.0, 0.0, 0.0, 0.0, 0.0,
                                                      0.0, 0.0, 0.0, 0.0, 0.0,
                                                      0.0, 0.0, 0.0, 0.0, 0.0,
                                                      0.0, 0.0, 0.0, 0.0, 0.0,
                                                      0.0, 0.0),
        min_float: typing.Optional[typing.Any] = -10000.0,
        max_float: typing.Optional[typing.Any] = -10000.0,
        soft_min_float: typing.Optional[typing.Any] = -10000.0,
        soft_max_float: typing.Optional[typing.Any] = -10000.0,
        precision: typing.Optional[typing.Any] = 3,
        step_float: typing.Optional[typing.Any] = 0.1,
        subtype: typing.Optional[typing.Any] = 'NONE',
        default_string: typing.Union[str, typing.Any] = "",
        eval_string: typing.Union[str, typing.Any] = ""):
    ''' Change a custom property's type, or adjust how it is displayed in the interface

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Property Edit, Property data_path edit
    :type data_path: typing.Union[str, typing.Any]
    :param property_name: Property Name, Property name edit
    :type property_name: typing.Union[str, typing.Any]
    :param property_type: Type * ``FLOAT`` Float -- A single floating-point value. * ``FLOAT_ARRAY`` Float Array -- An array of floating-point values. * ``INT`` Integer -- A single integer. * ``INT_ARRAY`` Integer Array -- An array of integers. * ``BOOL`` Boolean -- A true or false value. * ``BOOL_ARRAY`` Boolean Array -- An array of true or false values. * ``STRING`` String -- A string value. * ``PYTHON`` Python -- Edit a python value directly, for unsupported property types.
    :type property_type: typing.Optional[typing.Any]
    :param is_overridable_library: Library Overridable, Allow the property to be overridden when the data-block is linked
    :type is_overridable_library: typing.Optional[typing.Union[bool, typing.Any]]
    :param description: Description
    :type description: typing.Union[str, typing.Any]
    :param use_soft_limits: Soft Limits, Limits the Property Value slider to a range, values outside the range must be inputted numerically
    :type use_soft_limits: typing.Optional[typing.Union[bool, typing.Any]]
    :param array_length: Array Length
    :type array_length: typing.Optional[typing.Any]
    :param default_int: Default Value
    :type default_int: typing.Optional[typing.Any]
    :param min_int: Min
    :type min_int: typing.Optional[typing.Any]
    :param max_int: Max
    :type max_int: typing.Optional[typing.Any]
    :param soft_min_int: Soft Min
    :type soft_min_int: typing.Optional[typing.Any]
    :param soft_max_int: Soft Max
    :type soft_max_int: typing.Optional[typing.Any]
    :param step_int: Step
    :type step_int: typing.Optional[typing.Any]
    :param default_bool: Default Value
    :type default_bool: typing.Optional[typing.Union[typing.List[bool], typing.Any]]
    :param default_float: Default Value
    :type default_float: typing.Optional[typing.Any]
    :param min_float: Min
    :type min_float: typing.Optional[typing.Any]
    :param max_float: Max
    :type max_float: typing.Optional[typing.Any]
    :param soft_min_float: Soft Min
    :type soft_min_float: typing.Optional[typing.Any]
    :param soft_max_float: Soft Max
    :type soft_max_float: typing.Optional[typing.Any]
    :param precision: Precision
    :type precision: typing.Optional[typing.Any]
    :param step_float: Step
    :type step_float: typing.Optional[typing.Any]
    :param subtype: Subtype * ``NONE`` Plain Data -- Data values without special behavior. * ``COLOR`` Linear Color -- Color in the linear space. * ``COLOR_GAMMA`` Gamma-Corrected Color -- Color in the gamma corrected space. * ``EULER`` Euler Angles -- Euler rotation angles in radians. * ``QUATERNION`` Quaternion Rotation -- Quaternion rotation (affects NLA blending).
    :type subtype: typing.Optional[typing.Any]
    :param default_string: Default Value
    :type default_string: typing.Union[str, typing.Any]
    :param eval_string: Value, Python value for unsupported custom property types
    :type eval_string: typing.Union[str, typing.Any]
    '''

    pass


def properties_edit_value(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        property_name: typing.Union[str, typing.Any] = "",
        eval_string: typing.Union[str, typing.Any] = ""):
    ''' Edit the value of a custom property

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Property Edit, Property data_path edit
    :type data_path: typing.Union[str, typing.Any]
    :param property_name: Property Name, Property name edit
    :type property_name: typing.Union[str, typing.Any]
    :param eval_string: Value, Value for custom property types that can only be edited as a Python expression
    :type eval_string: typing.Union[str, typing.Any]
    '''

    pass


def properties_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path: typing.Union[str, typing.Any] = "",
        property_name: typing.Union[str, typing.Any] = ""):
    ''' Internal use (edit a property data_path)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path: Property Edit, Property data_path edit
    :type data_path: typing.Union[str, typing.Any]
    :param property_name: Property Name, Property name edit
    :type property_name: typing.Union[str, typing.Any]
    '''

    pass


def quit_blender(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Quit Blender

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def radial_control(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path_primary: typing.Union[str, typing.Any] = "",
        data_path_secondary: typing.Union[str, typing.Any] = "",
        use_secondary: typing.Union[str, typing.Any] = "",
        rotation_path: typing.Union[str, typing.Any] = "",
        color_path: typing.Union[str, typing.Any] = "",
        fill_color_path: typing.Union[str, typing.Any] = "",
        fill_color_override_path: typing.Union[str, typing.Any] = "",
        fill_color_override_test_path: typing.Union[str, typing.Any] = "",
        zoom_path: typing.Union[str, typing.Any] = "",
        image_id: typing.Union[str, typing.Any] = "",
        secondary_tex: typing.Optional[typing.Union[bool, typing.Any]] = False,
        release_confirm: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False):
    ''' Set some size property (e.g. brush size) with mouse wheel

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param data_path_primary: Primary Data Path, Primary path of property to be set by the radial control
    :type data_path_primary: typing.Union[str, typing.Any]
    :param data_path_secondary: Secondary Data Path, Secondary path of property to be set by the radial control
    :type data_path_secondary: typing.Union[str, typing.Any]
    :param use_secondary: Use Secondary, Path of property to select between the primary and secondary data paths
    :type use_secondary: typing.Union[str, typing.Any]
    :param rotation_path: Rotation Path, Path of property used to rotate the texture display
    :type rotation_path: typing.Union[str, typing.Any]
    :param color_path: Color Path, Path of property used to set the color of the control
    :type color_path: typing.Union[str, typing.Any]
    :param fill_color_path: Fill Color Path, Path of property used to set the fill color of the control
    :type fill_color_path: typing.Union[str, typing.Any]
    :param fill_color_override_path: Fill Color Override Path
    :type fill_color_override_path: typing.Union[str, typing.Any]
    :param fill_color_override_test_path: Fill Color Override Test
    :type fill_color_override_test_path: typing.Union[str, typing.Any]
    :param zoom_path: Zoom Path, Path of property used to set the zoom level for the control
    :type zoom_path: typing.Union[str, typing.Any]
    :param image_id: Image ID, Path of ID that is used to generate an image for the control
    :type image_id: typing.Union[str, typing.Any]
    :param secondary_tex: Secondary Texture, Tweak brush secondary/mask texture
    :type secondary_tex: typing.Optional[typing.Union[bool, typing.Any]]
    :param release_confirm: Confirm On Release, Finish operation on key release
    :type release_confirm: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def read_factory_settings(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_factory_startup_app_template_only: typing.Optional[
            typing.Union[bool, typing.Any]] = False,
        app_template: typing.Union[str, typing.Any] = "Template",
        use_empty: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Load factory default startup file and preferences. To make changes permanent, use "Save Startup File" and "Save Preferences"

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_factory_startup_app_template_only: Factory Startup App-Template Only
    :type use_factory_startup_app_template_only: typing.Optional[typing.Union[bool, typing.Any]]
    :type app_template: typing.Union[str, typing.Any]
    :param use_empty: Empty
    :type use_empty: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def read_factory_userpref(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_factory_startup_app_template_only: typing.Optional[
            typing.Union[bool, typing.Any]] = False):
    ''' Load factory default preferences. To make changes to preferences permanent, use "Save Preferences"

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_factory_startup_app_template_only: Factory Startup App-Template Only
    :type use_factory_startup_app_template_only: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def read_history(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Reloads history and bookmarks

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def read_homefile(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        load_ui: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_splash: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_factory_startup: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = False,
        use_factory_startup_app_template_only: typing.Optional[
            typing.Union[bool, typing.Any]] = False,
        app_template: typing.Union[str, typing.Any] = "Template",
        use_empty: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Open the default file (doesn't save the current file)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to an alternative start-up file
    :type filepath: typing.Union[str, typing.Any]
    :param load_ui: Load UI, Load user interface setup from the .blend file
    :type load_ui: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_splash: Splash
    :type use_splash: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_factory_startup: Factory Startup
    :type use_factory_startup: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_factory_startup_app_template_only: Factory Startup App-Template Only
    :type use_factory_startup_app_template_only: typing.Optional[typing.Union[bool, typing.Any]]
    :type app_template: typing.Union[str, typing.Any]
    :param use_empty: Empty
    :type use_empty: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def read_userpref(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Load last saved preferences

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def recover_auto_save(
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
        filter_blender: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
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
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'LIST_VERTICAL',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        use_scripts: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Open an automatically saved file to recover it

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
    :param filter_python: Filter python files
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
    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def recover_last_session(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_scripts: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Open the last closed file ("quit.blend")

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def redraw_timer(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'DRAW',
        iterations: typing.Optional[typing.Any] = 10,
        time_limit: typing.Optional[typing.Any] = 0.0):
    ''' Simple redraw timer to test the speed of updating the interface

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type * ``DRAW`` Draw Region -- Draw region. * ``DRAW_SWAP`` Draw Region & Swap -- Draw region and swap. * ``DRAW_WIN`` Draw Window -- Draw window. * ``DRAW_WIN_SWAP`` Draw Window & Swap -- Draw window and swap. * ``ANIM_STEP`` Animation Step -- Animation steps. * ``ANIM_PLAY`` Animation Play -- Animation playback. * ``UNDO`` Undo/Redo -- Undo and redo.
    :type type: typing.Optional[typing.Any]
    :param iterations: Iterations, Number of times to redraw
    :type iterations: typing.Optional[typing.Any]
    :param time_limit: Time Limit, Seconds to run the test for (override iterations)
    :type time_limit: typing.Optional[typing.Any]
    '''

    pass


def revert_mainfile(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_scripts: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Reload the saved file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def save_as_mainfile(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        hide_props_region: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        check_existing: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blender: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
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
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        compress: typing.Optional[typing.Union[bool, typing.Any]] = False,
        relative_remap: typing.Optional[typing.Union[bool, typing.Any]] = True,
        copy: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Save the current file in the desired location

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
    :param filter_python: Filter python files
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
    :param compress: Compress, Write compressed .blend file
    :type compress: typing.Optional[typing.Union[bool, typing.Any]]
    :param relative_remap: Remap Relative, Remap relative paths when saving to a different directory
    :type relative_remap: typing.Optional[typing.Union[bool, typing.Any]]
    :param copy: Save Copy, Save a copy of the actual working state but does not make saved file active
    :type copy: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def save_homefile(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Make the current file the default .blend file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def save_mainfile(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        hide_props_region: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        check_existing: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blender: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
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
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        compress: typing.Optional[typing.Union[bool, typing.Any]] = False,
        relative_remap: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        exit: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Save the current Blender file

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
    :param filter_python: Filter python files
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
    :param compress: Compress, Write compressed .blend file
    :type compress: typing.Optional[typing.Union[bool, typing.Any]]
    :param relative_remap: Remap Relative, Remap relative paths when saving to a different directory
    :type relative_remap: typing.Optional[typing.Union[bool, typing.Any]]
    :param exit: Exit, Exit Blender after saving
    :type exit: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def save_userpref(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Make the current preferences default

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def search_menu(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Pop-up a search over all menus in the current context

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def search_operator(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Pop-up a search over all available operators in current context

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def set_stereo_3d(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        display_mode: typing.Optional[typing.Union[str, int]] = 'ANAGLYPH',
        anaglyph_type: typing.Optional[typing.Union[str, int]] = 'RED_CYAN',
        interlace_type: typing.Optional[typing.
                                        Union[str, int]] = 'ROW_INTERLEAVED',
        use_interlace_swap: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = False,
        use_sidebyside_crosseyed: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = False):
    ''' Toggle 3D stereo support for current window (or change the display mode)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param display_mode: Display Mode
    :type display_mode: typing.Optional[typing.Union[str, int]]
    :param anaglyph_type: Anaglyph Type
    :type anaglyph_type: typing.Optional[typing.Union[str, int]]
    :param interlace_type: Interlace Type
    :type interlace_type: typing.Optional[typing.Union[str, int]]
    :param use_interlace_swap: Swap Left/Right, Swap left and right stereo channels
    :type use_interlace_swap: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_sidebyside_crosseyed: Cross-Eyed, Right eye should see left image and vice versa
    :type use_sidebyside_crosseyed: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def splash(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None):
    ''' Open the splash screen with release info

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def splash_about(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Open a window with information about Blender

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def stl_import(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        directory: typing.Union[str, typing.Any] = "",
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
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
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        global_scale: typing.Optional[typing.Any] = 1.0,
        use_scene_unit: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        use_facet_normal: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        forward_axis: typing.Optional[typing.Any] = 'Y',
        up_axis: typing.Optional[typing.Any] = 'Z',
        use_mesh_validate: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False,
        filter_glob: typing.Union[str, typing.Any] = "*.stl"):
    ''' Import an STL file as an object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param files: Files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
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
    :param filter_python: Filter python files
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
    :param global_scale: Scale
    :type global_scale: typing.Optional[typing.Any]
    :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to imported data
    :type use_scene_unit: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_facet_normal: Facet Normals, Use (import) facet normals (note that this will still give flat shading)
    :type use_facet_normal: typing.Optional[typing.Union[bool, typing.Any]]
    :param forward_axis: Forward Axis * ``X`` X -- Positive X axis. * ``Y`` Y -- Positive Y axis. * ``Z`` Z -- Positive Z axis. * ``NEGATIVE_X`` -X -- Negative X axis. * ``NEGATIVE_Y`` -Y -- Negative Y axis. * ``NEGATIVE_Z`` -Z -- Negative Z axis.
    :type forward_axis: typing.Optional[typing.Any]
    :param up_axis: Up Axis * ``X`` X -- Positive X axis. * ``Y`` Y -- Positive Y axis. * ``Z`` Z -- Positive Z axis. * ``NEGATIVE_X`` -X -- Negative X axis. * ``NEGATIVE_Y`` -Y -- Negative Y axis. * ``NEGATIVE_Z`` -Z -- Negative Z axis.
    :type up_axis: typing.Optional[typing.Any]
    :param use_mesh_validate: Validate Mesh, Validate and correct imported mesh (slow)
    :type use_mesh_validate: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_glob: Extension Filter
    :type filter_glob: typing.Union[str, typing.Any]
    '''

    pass


def sysinfo(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
            execution_context: typing.Optional[typing.Union[str, int]] = None,
            undo: typing.Optional[bool] = None,
            *,
            filepath: typing.Union[str, typing.Any] = ""):
    ''' Generate system information, saved into a text file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: filepath
    :type filepath: typing.Union[str, typing.Any]
    '''

    pass


def tool_set_by_id(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "",
        cycle: typing.Optional[typing.Union[bool, typing.Any]] = False,
        as_fallback: typing.Optional[typing.Union[bool, typing.Any]] = False,
        space_type: typing.Optional[typing.Any] = 'EMPTY'):
    ''' Set the tool by name (for keymaps)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Identifier, Identifier of the tool
    :type name: typing.Union[str, typing.Any]
    :param cycle: Cycle, Cycle through tools in this group
    :type cycle: typing.Optional[typing.Union[bool, typing.Any]]
    :param as_fallback: Set Fallback, Set the fallback tool instead of the primary tool
    :type as_fallback: typing.Optional[typing.Union[bool, typing.Any]]
    :param space_type: Type
    :type space_type: typing.Optional[typing.Any]
    '''

    pass


def tool_set_by_index(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        index: typing.Optional[typing.Any] = 0,
        cycle: typing.Optional[typing.Union[bool, typing.Any]] = False,
        expand: typing.Optional[typing.Union[bool, typing.Any]] = True,
        as_fallback: typing.Optional[typing.Union[bool, typing.Any]] = False,
        space_type: typing.Optional[typing.Any] = 'EMPTY'):
    ''' Set the tool by index (for keymaps)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param index: Index in Toolbar
    :type index: typing.Optional[typing.Any]
    :param cycle: Cycle, Cycle through tools in this group
    :type cycle: typing.Optional[typing.Union[bool, typing.Any]]
    :param expand: expand, Include tool subgroups
    :type expand: typing.Optional[typing.Union[bool, typing.Any]]
    :param as_fallback: Set Fallback, Set the fallback tool instead of the primary
    :type as_fallback: typing.Optional[typing.Union[bool, typing.Any]]
    :param space_type: Type
    :type space_type: typing.Optional[typing.Any]
    '''

    pass


def toolbar(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
            execution_context: typing.Optional[typing.Union[str, int]] = None,
            undo: typing.Optional[bool] = None):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__. :file:`startup/bl_operators/wm.py\:2311 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2311>`_

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def toolbar_fallback_pie(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__. :file:`startup/bl_operators/wm.py\:2335 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2335>`_

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def toolbar_prompt(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Leader key like functionality for accessing tools :file:`startup/bl_operators/wm.py\:2435 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2435>`_

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def url_open(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None,
             *,
             url: typing.Union[str, typing.Any] = ""):
    ''' Open a website in the web browser

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param url: URL, URL to open
    :type url: typing.Union[str, typing.Any]
    '''

    pass


def url_open_preset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        id: typing.Union[str, typing.Any] = ""):
    ''' Open a preset website in the web browser

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Site
    :type type: typing.Optional[typing.Union[str, int, typing.Any]]
    :param id: Identifier, Optional identifier
    :type id: typing.Union[str, typing.Any]
    '''

    pass


def usd_export(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        check_existing: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blender: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_sound: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_collada: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_alembic: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        selected_objects_only: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
        visible_objects_only: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = True,
        export_animation: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        export_hair: typing.Optional[typing.Union[bool, typing.Any]] = False,
        export_uvmaps: typing.Optional[typing.Union[bool, typing.Any]] = True,
        export_normals: typing.Optional[typing.Union[bool, typing.Any]] = True,
        export_materials: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        use_instancing: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        evaluation_mode: typing.Optional[typing.Any] = 'RENDER',
        generate_preview_surface: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = True,
        export_textures: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True,
        overwrite_textures: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = False,
        relative_paths: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = True):
    ''' Export current scene in a USD archive

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
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
    :param filter_python: Filter python files
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
    :param selected_objects_only: Selection Only, Only export selected objects. Unselected parents of selected objects are exported as empty transform
    :type selected_objects_only: typing.Optional[typing.Union[bool, typing.Any]]
    :param visible_objects_only: Visible Only, Only export visible objects. Invisible parents of exported objects are exported as empty transforms
    :type visible_objects_only: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_animation: Animation, Export all frames in the render frame range, rather than only the current frame
    :type export_animation: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_hair: Hair, Export hair particle systems as USD curves
    :type export_hair: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_uvmaps: UV Maps, Include all mesh UV maps in the export
    :type export_uvmaps: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_normals: Normals, Include normals of exported meshes in the export
    :type export_normals: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_materials: Materials, Export viewport settings of materials as USD preview materials, and export material assignments as geometry subsets
    :type export_materials: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_instancing: Instancing, Export instanced objects as references in USD rather than real objects
    :type use_instancing: typing.Optional[typing.Union[bool, typing.Any]]
    :param evaluation_mode: Use Settings for, Determines visibility of objects, modifier settings, and other areas where there are different settings for viewport and rendering * ``RENDER`` Render -- Use Render settings for object visibility, modifier settings, etc. * ``VIEWPORT`` Viewport -- Use Viewport settings for object visibility, modifier settings, etc.
    :type evaluation_mode: typing.Optional[typing.Any]
    :param generate_preview_surface: To USD Preview Surface, Generate an approximate USD Preview Surface shader representation of a Principled BSDF node network
    :type generate_preview_surface: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_textures: Export Textures, If exporting materials, export textures referenced by material nodes to a 'textures' directory in the same directory as the USD file
    :type export_textures: typing.Optional[typing.Union[bool, typing.Any]]
    :param overwrite_textures: Overwrite Textures, Allow overwriting existing texture files when exporting textures
    :type overwrite_textures: typing.Optional[typing.Union[bool, typing.Any]]
    :param relative_paths: Relative Paths, Use relative paths to reference external files (i.e. textures, volumes) in USD, otherwise use absolute paths
    :type relative_paths: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def usd_import(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
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
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_collada: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_alembic: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 8,
        relative_path: typing.Optional[typing.Union[bool, typing.Any]] = True,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        scale: typing.Optional[typing.Any] = 1.0,
        set_frame_range: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True,
        import_cameras: typing.Optional[typing.Union[bool, typing.Any]] = True,
        import_curves: typing.Optional[typing.Union[bool, typing.Any]] = True,
        import_lights: typing.Optional[typing.Union[bool, typing.Any]] = True,
        import_materials: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        import_meshes: typing.Optional[typing.Union[bool, typing.Any]] = True,
        import_volumes: typing.Optional[typing.Union[bool, typing.Any]] = True,
        import_shapes: typing.Optional[typing.Union[bool, typing.Any]] = True,
        import_subdiv: typing.Optional[typing.Union[bool, typing.Any]] = False,
        import_instance_proxies: typing.Optional[typing.Union[bool, typing.
                                                              Any]] = True,
        import_visible_only: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = True,
        create_collection: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False,
        read_mesh_uvs: typing.Optional[typing.Union[bool, typing.Any]] = True,
        read_mesh_colors: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        prim_path_mask: typing.Union[str, typing.Any] = "",
        import_guide: typing.Optional[typing.Union[bool, typing.Any]] = False,
        import_proxy: typing.Optional[typing.Union[bool, typing.Any]] = True,
        import_render: typing.Optional[typing.Union[bool, typing.Any]] = True,
        import_all_materials: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        import_usd_preview: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = True,
        set_material_blend: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = True,
        light_intensity_scale: typing.Optional[typing.Any] = 1.0,
        mtl_name_collision_mode: typing.Optional[typing.Any] = 'MAKE_UNIQUE',
        import_textures_mode: typing.Optional[typing.Any] = 'IMPORT_PACK',
        import_textures_dir: typing.Union[str, typing.Any] = "//textures/",
        tex_name_collision_mode: typing.Optional[typing.Any] = 'USE_EXISTING'):
    ''' Import USD stage into current scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
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
    :param filter_python: Filter python files
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
    :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
    :type scale: typing.Optional[typing.Any]
    :param set_frame_range: Set Frame Range, Update the scene's start and end frame to match those of the USD archive
    :type set_frame_range: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_cameras: Cameras
    :type import_cameras: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_curves: Curves
    :type import_curves: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_lights: Lights
    :type import_lights: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_materials: Materials
    :type import_materials: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_meshes: Meshes
    :type import_meshes: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_volumes: Volumes
    :type import_volumes: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_shapes: Shapes
    :type import_shapes: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_subdiv: Import Subdivision Scheme, Create subdivision surface modifiers based on the USD SubdivisionScheme attribute
    :type import_subdiv: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_instance_proxies: Import Instance Proxies, Create unique Blender objects for USD instances
    :type import_instance_proxies: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_visible_only: Visible Primitives Only, Do not import invisible USD primitives. Only applies to primitives with a non-animated visibility attribute. Primitives with animated visibility will always be imported
    :type import_visible_only: typing.Optional[typing.Union[bool, typing.Any]]
    :param create_collection: Create Collection, Add all imported objects to a new collection
    :type create_collection: typing.Optional[typing.Union[bool, typing.Any]]
    :param read_mesh_uvs: UV Coordinates, Read mesh UV coordinates
    :type read_mesh_uvs: typing.Optional[typing.Union[bool, typing.Any]]
    :param read_mesh_colors: Color Attributes, Read mesh color attributes
    :type read_mesh_colors: typing.Optional[typing.Union[bool, typing.Any]]
    :param prim_path_mask: Path Mask, Import only the subset of the USD scene rooted at the given primitive
    :type prim_path_mask: typing.Union[str, typing.Any]
    :param import_guide: Guide, Import guide geometry
    :type import_guide: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_proxy: Proxy, Import proxy geometry
    :type import_proxy: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_render: Render, Import final render geometry
    :type import_render: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_all_materials: Import All Materials, Also import materials that are not used by any geometry. Note that when this option is false, materials referenced by geometry will still be imported
    :type import_all_materials: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_usd_preview: Import USD Preview, Convert UsdPreviewSurface shaders to Principled BSDF shader networks
    :type import_usd_preview: typing.Optional[typing.Union[bool, typing.Any]]
    :param set_material_blend: Set Material Blend, If the Import USD Preview option is enabled, the material blend method will automatically be set based on the shader's opacity and opacityThreshold inputs
    :type set_material_blend: typing.Optional[typing.Union[bool, typing.Any]]
    :param light_intensity_scale: Light Intensity Scale, Scale for the intensity of imported lights
    :type light_intensity_scale: typing.Optional[typing.Any]
    :param mtl_name_collision_mode: Material Name Collision, Behavior when the name of an imported material conflicts with an existing material * ``MAKE_UNIQUE`` Make Unique -- Import each USD material as a unique Blender material. * ``REFERENCE_EXISTING`` Reference Existing -- If a material with the same name already exists, reference that instead of importing.
    :type mtl_name_collision_mode: typing.Optional[typing.Any]
    :param import_textures_mode: Import Textures, Behavior when importing textures from a USDZ archive * ``IMPORT_NONE`` None -- Don't import textures. * ``IMPORT_PACK`` Packed -- Import textures as packed data. * ``IMPORT_COPY`` Copy -- Copy files to textures directory.
    :type import_textures_mode: typing.Optional[typing.Any]
    :param import_textures_dir: Textures Directory, Path to the directory where imported textures will be copied
    :type import_textures_dir: typing.Union[str, typing.Any]
    :param tex_name_collision_mode: File Name Collision, Behavior when the name of an imported texture file conflicts with an existing file * ``USE_EXISTING`` Use Existing -- If a file with the same name already exists, use that instead of copying. * ``OVERWRITE`` Overwrite -- Overwrite existing files.
    :type tex_name_collision_mode: typing.Optional[typing.Any]
    '''

    pass


def window_close(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Close the current window

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def window_fullscreen_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Toggle the current window full-screen

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def window_new(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Create a new window

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def window_new_main(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Create a new main window with its own workspace and scene selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def xr_navigation_fly(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'VIEWER_FORWARD',
        lock_location_z: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        lock_direction: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        speed_frame_based: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        speed_min: typing.Optional[typing.Any] = 0.018,
        speed_max: typing.Optional[typing.Any] = 0.054,
        speed_interpolation0: typing.Optional[typing.Any] = (0.0, 0.0),
        speed_interpolation1: typing.Optional[typing.Any] = (1.0, 1.0)):
    ''' Move/turn relative to the VR viewer or controller

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode, Fly mode * ``FORWARD`` Forward -- Move along navigation forward axis. * ``BACK`` Back -- Move along navigation back axis. * ``LEFT`` Left -- Move along navigation left axis. * ``RIGHT`` Right -- Move along navigation right axis. * ``UP`` Up -- Move along navigation up axis. * ``DOWN`` Down -- Move along navigation down axis. * ``TURNLEFT`` Turn Left -- Turn counter-clockwise around navigation up axis. * ``TURNRIGHT`` Turn Right -- Turn clockwise around navigation up axis. * ``VIEWER_FORWARD`` Viewer Forward -- Move along viewer's forward axis. * ``VIEWER_BACK`` Viewer Back -- Move along viewer's back axis. * ``VIEWER_LEFT`` Viewer Left -- Move along viewer's left axis. * ``VIEWER_RIGHT`` Viewer Right -- Move along viewer's right axis. * ``CONTROLLER_FORWARD`` Controller Forward -- Move along controller's forward axis.
    :type mode: typing.Optional[typing.Any]
    :param lock_location_z: Lock Elevation, Prevent changes to viewer elevation
    :type lock_location_z: typing.Optional[typing.Union[bool, typing.Any]]
    :param lock_direction: Lock Direction, Limit movement to viewer's initial direction
    :type lock_direction: typing.Optional[typing.Union[bool, typing.Any]]
    :param speed_frame_based: Frame Based Speed, Apply fixed movement deltas every update
    :type speed_frame_based: typing.Optional[typing.Union[bool, typing.Any]]
    :param speed_min: Minimum Speed, Minimum move (turn) speed in meters (radians) per second or frame
    :type speed_min: typing.Optional[typing.Any]
    :param speed_max: Maximum Speed, Maximum move (turn) speed in meters (radians) per second or frame
    :type speed_max: typing.Optional[typing.Any]
    :param speed_interpolation0: Speed Interpolation 0, First cubic spline control point between min/max speeds
    :type speed_interpolation0: typing.Optional[typing.Any]
    :param speed_interpolation1: Speed Interpolation 1, Second cubic spline control point between min/max speeds
    :type speed_interpolation1: typing.Optional[typing.Any]
    '''

    pass


def xr_navigation_grab(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        lock_location: typing.Optional[typing.Union[bool, typing.Any]] = False,
        lock_location_z: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        lock_rotation: typing.Optional[typing.Union[bool, typing.Any]] = False,
        lock_rotation_z: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        lock_scale: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Navigate the VR scene by grabbing with controllers

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param lock_location: Lock Location, Prevent changes to viewer location
    :type lock_location: typing.Optional[typing.Union[bool, typing.Any]]
    :param lock_location_z: Lock Elevation, Prevent changes to viewer elevation
    :type lock_location_z: typing.Optional[typing.Union[bool, typing.Any]]
    :param lock_rotation: Lock Rotation, Prevent changes to viewer rotation
    :type lock_rotation: typing.Optional[typing.Union[bool, typing.Any]]
    :param lock_rotation_z: Lock Up Orientation, Prevent changes to viewer up orientation
    :type lock_rotation_z: typing.Optional[typing.Union[bool, typing.Any]]
    :param lock_scale: Lock Scale, Prevent changes to viewer scale
    :type lock_scale: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def xr_navigation_reset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        location: typing.Optional[typing.Union[bool, typing.Any]] = True,
        rotation: typing.Optional[typing.Union[bool, typing.Any]] = True,
        scale: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Reset VR navigation deltas relative to session base pose

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param location: Location, Reset location deltas
    :type location: typing.Optional[typing.Union[bool, typing.Any]]
    :param rotation: Rotation, Reset rotation deltas
    :type rotation: typing.Optional[typing.Union[bool, typing.Any]]
    :param scale: Scale, Reset scale deltas
    :type scale: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def xr_navigation_teleport(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        teleport_axes: typing.Optional[typing.Union[typing.List[bool], typing.
                                                    Any]] = (True, True, True),
        interpolation: typing.Optional[typing.Any] = 1.0,
        offset: typing.Optional[typing.Any] = 0.0,
        selectable_only: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True,
        distance: typing.Optional[typing.Any] = 1.70141e+38,
        from_viewer: typing.Optional[typing.Union[bool, typing.Any]] = False,
        axis: typing.Optional[typing.Any] = (0.0, 0.0, -1.0),
        color: typing.Optional[typing.Any] = (0.35, 0.35, 1.0, 1.0)):
    ''' Set VR viewer location to controller raycast hit location

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param teleport_axes: Teleport Axes, Enabled teleport axes in navigation space
    :type teleport_axes: typing.Optional[typing.Union[typing.List[bool], typing.Any]]
    :param interpolation: Interpolation, Interpolation factor between viewer and hit locations
    :type interpolation: typing.Optional[typing.Any]
    :param offset: Offset, Offset along hit normal to subtract from final location
    :type offset: typing.Optional[typing.Any]
    :param selectable_only: Selectable Only, Only allow selectable objects to influence raycast result
    :type selectable_only: typing.Optional[typing.Union[bool, typing.Any]]
    :param distance: Maximum raycast distance
    :type distance: typing.Optional[typing.Any]
    :param from_viewer: From Viewer, Use viewer pose as raycast origin
    :type from_viewer: typing.Optional[typing.Union[bool, typing.Any]]
    :param axis: Axis, Raycast axis in controller/viewer space
    :type axis: typing.Optional[typing.Any]
    :param color: Color, Raycast color
    :type color: typing.Optional[typing.Any]
    '''

    pass


def xr_session_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Open a view for use with virtual reality headsets, or close it if already opened

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass
