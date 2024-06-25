import typing
import collections.abc
import bl_operators.wm
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def alembic_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = True,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    filter_glob: str | typing.Any = "*.abc",
    start: typing.Any | None = -2147483648,
    end: typing.Any | None = -2147483648,
    xsamples: typing.Any | None = 1,
    gsamples: typing.Any | None = 1,
    sh_open: typing.Any | None = 0.0,
    sh_close: typing.Any | None = 1.0,
    selected: bool | typing.Any | None = False,
    visible_objects_only: bool | typing.Any | None = False,
    flatten: bool | typing.Any | None = False,
    uvs: bool | typing.Any | None = True,
    packuv: bool | typing.Any | None = True,
    normals: bool | typing.Any | None = True,
    vcolors: bool | typing.Any | None = False,
    orcos: bool | typing.Any | None = True,
    face_sets: bool | typing.Any | None = False,
    subdiv_schema: bool | typing.Any | None = False,
    apply_subdiv: bool | typing.Any | None = False,
    curves_as_mesh: bool | typing.Any | None = False,
    use_instancing: bool | typing.Any | None = True,
    global_scale: typing.Any | None = 1.0,
    triangulate: bool | typing.Any | None = False,
    quad_method: str | None = "SHORTEST_DIAGONAL",
    ngon_method: str | None = "BEAUTY",
    export_hair: bool | typing.Any | None = True,
    export_particles: bool | typing.Any | None = True,
    export_custom_properties: bool | typing.Any | None = True,
    as_background_job: bool | typing.Any | None = False,
    evaluation_mode: str | None = "RENDER",
    init_scene_frame_range: bool | typing.Any | None = True,
):
    """Export current scene in an Alembic archive

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :type filter_glob: str | typing.Any
        :param start: Start Frame, Start frame of the export, use the default value to take the start frame of the current scene
        :type start: typing.Any | None
        :param end: End Frame, End frame of the export, use the default value to take the end frame of the current scene
        :type end: typing.Any | None
        :param xsamples: Transform Samples, Number of times per frame transformations are sampled
        :type xsamples: typing.Any | None
        :param gsamples: Geometry Samples, Number of times per frame object data are sampled
        :type gsamples: typing.Any | None
        :param sh_open: Shutter Open, Time at which the shutter is open
        :type sh_open: typing.Any | None
        :param sh_close: Shutter Close, Time at which the shutter is closed
        :type sh_close: typing.Any | None
        :param selected: Selected Objects Only, Export only selected objects
        :type selected: bool | typing.Any | None
        :param visible_objects_only: Visible Objects Only, Export only objects that are visible
        :type visible_objects_only: bool | typing.Any | None
        :param flatten: Flatten Hierarchy, Do not preserve objects' parent/children relationship
        :type flatten: bool | typing.Any | None
        :param uvs: UVs, Export UVs
        :type uvs: bool | typing.Any | None
        :param packuv: Pack UV Islands, Export UVs with packed island
        :type packuv: bool | typing.Any | None
        :param normals: Normals, Export normals
        :type normals: bool | typing.Any | None
        :param vcolors: Color Attributes, Export color attributes
        :type vcolors: bool | typing.Any | None
        :param orcos: Generated Coordinates, Export undeformed mesh vertex coordinates
        :type orcos: bool | typing.Any | None
        :param face_sets: Face Sets, Export per face shading group assignments
        :type face_sets: bool | typing.Any | None
        :param subdiv_schema: Use Subdivision Schema, Export meshes using Alembic's subdivision schema
        :type subdiv_schema: bool | typing.Any | None
        :param apply_subdiv: Apply Subdivision Surface, Export subdivision surfaces as meshes
        :type apply_subdiv: bool | typing.Any | None
        :param curves_as_mesh: Curves as Mesh, Export curves and NURBS surfaces as meshes
        :type curves_as_mesh: bool | typing.Any | None
        :param use_instancing: Use Instancing, Export data of duplicated objects as Alembic instances; speeds up the export and can be disabled for compatibility with other software
        :type use_instancing: bool | typing.Any | None
        :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
        :type global_scale: typing.Any | None
        :param triangulate: Triangulate, Export polygons (quads and n-gons) as triangles
        :type triangulate: bool | typing.Any | None
        :param quad_method: Quad Method, Method for splitting the quads into triangles
        :type quad_method: str | None
        :param ngon_method: N-gon Method, Method for splitting the n-gons into triangles
        :type ngon_method: str | None
        :param export_hair: Export Hair, Exports hair particle systems as animated curves
        :type export_hair: bool | typing.Any | None
        :param export_particles: Export Particles, Exports non-hair particle systems
        :type export_particles: bool | typing.Any | None
        :param export_custom_properties: Export Custom Properties, Export custom properties to Alembic .userProperties
        :type export_custom_properties: bool | typing.Any | None
        :param as_background_job: Run as Background Job, Enable this to run the import in the background, disable to block Blender while importing. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job
        :type as_background_job: bool | typing.Any | None
        :param evaluation_mode: Use Settings for, Determines visibility of objects, modifier settings, and other areas where there are different settings for viewport and rendering

    RENDER
    Render -- Use Render settings for object visibility, modifier settings, etc.

    VIEWPORT
    Viewport -- Use Viewport settings for object visibility, modifier settings, etc.
        :type evaluation_mode: str | None
        :type init_scene_frame_range: bool | typing.Any | None
    """

    ...

def alembic_import(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    check_existing: bool | typing.Any | None = False,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = True,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    relative_path: bool | typing.Any | None = True,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    filter_glob: str | typing.Any = "*.abc",
    scale: typing.Any | None = 1.0,
    set_frame_range: bool | typing.Any | None = True,
    validate_meshes: bool | typing.Any | None = False,
    always_add_cache_reader: bool | typing.Any | None = False,
    is_sequence: bool | typing.Any | None = False,
    as_background_job: bool | typing.Any | None = False,
):
    """Load an Alembic archive

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :type filter_glob: str | typing.Any
        :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
        :type scale: typing.Any | None
        :param set_frame_range: Set Frame Range, If checked, update scene's start and end frame to match those of the Alembic archive
        :type set_frame_range: bool | typing.Any | None
        :param validate_meshes: Validate Meshes, Check imported mesh objects for invalid data (slow)
        :type validate_meshes: bool | typing.Any | None
        :param always_add_cache_reader: Always Add Cache Reader, Add cache modifiers and constraints to imported objects even if they are not animated so that they can be updated when reloading the Alembic archive
        :type always_add_cache_reader: bool | typing.Any | None
        :param is_sequence: Is Sequence, Set to true if the cache is split into separate files
        :type is_sequence: bool | typing.Any | None
        :param as_background_job: Run as Background Job, Enable this to run the export in the background, disable to block Blender while exporting. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job
        :type as_background_job: bool | typing.Any | None
    """

    ...

def append(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    directory: str | typing.Any = "",
    filename: str | typing.Any = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    check_existing: bool | typing.Any | None = False,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = True,
    filemode: typing.Any | None = 1,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    link: bool | typing.Any | None = False,
    do_reuse_local_id: bool | typing.Any | None = False,
    clear_asset_data: bool | typing.Any | None = False,
    autoselect: bool | typing.Any | None = True,
    active_collection: bool | typing.Any | None = True,
    instance_collections: bool | typing.Any | None = False,
    instance_object_data: bool | typing.Any | None = True,
    set_fake: bool | typing.Any | None = False,
    use_recursive: bool | typing.Any | None = True,
):
    """Append from a Library .blend file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param directory: Directory, Directory of the file
        :type directory: str | typing.Any
        :param filename: File Name, Name of the file
        :type filename: str | typing.Any
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param link: Link, Link the objects or data-blocks rather than appending
        :type link: bool | typing.Any | None
        :param do_reuse_local_id: Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy
        :type do_reuse_local_id: bool | typing.Any | None
        :param clear_asset_data: Clear Asset Data, Don't add asset meta-data or tags from the original data-block
        :type clear_asset_data: bool | typing.Any | None
        :param autoselect: Select, Select new objects
        :type autoselect: bool | typing.Any | None
        :param active_collection: Active Collection, Put new objects on the active collection
        :type active_collection: bool | typing.Any | None
        :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
        :type instance_collections: bool | typing.Any | None
        :param instance_object_data: Instance Object Data, Create instances for object data which are not referenced by any objects
        :type instance_object_data: bool | typing.Any | None
        :param set_fake: Fake User, Set "Fake User" for appended items (except objects and collections)
        :type set_fake: bool | typing.Any | None
        :param use_recursive: Localize All, Localize all appended data, including those indirectly linked from other libraries
        :type use_recursive: bool | typing.Any | None
    """

    ...

def batch_rename(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_type: str | None = "OBJECT",
    data_source: str | None = "SELECT",
    actions: bpy.types.bpy_prop_collection[bl_operators.wm.BatchRenameAction]
    | None = None,
):
    """Rename multiple items at once

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_type: Type, Type of data to rename
    :type data_type: str | None
    :param data_source: Source
    :type data_source: str | None
    :param actions: actions
    :type actions: bpy.types.bpy_prop_collection[bl_operators.wm.BatchRenameAction] | None
    """

    ...

def blend_strings_utf8_validate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Check and fix all strings in current .blend file to be valid UTF-8 Unicode (needed for some old, 2.4x area files)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def call_menu(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
):
    """Open a predefined menu

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the menu
    :type name: str | typing.Any
    """

    ...

def call_menu_pie(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
):
    """Open a predefined pie menu

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the pie menu
    :type name: str | typing.Any
    """

    ...

def call_panel(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
    keep_open: bool | typing.Any | None = True,
):
    """Open a predefined panel

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the menu
    :type name: str | typing.Any
    :param keep_open: Keep Open
    :type keep_open: bool | typing.Any | None
    """

    ...

def clear_recent_files(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Clear the recent files list

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def collada_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = True,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    filter_glob: str | typing.Any = "*.dae",
    prop_bc_export_ui_section: str | None = "main",
    apply_modifiers: bool | typing.Any | None = False,
    export_mesh_type: typing.Any | None = 0,
    export_mesh_type_selection: str | None = "view",
    export_global_forward_selection: str | None = "Y",
    export_global_up_selection: str | None = "Z",
    apply_global_orientation: bool | typing.Any | None = False,
    selected: bool | typing.Any | None = False,
    include_children: bool | typing.Any | None = False,
    include_armatures: bool | typing.Any | None = False,
    include_shapekeys: bool | typing.Any | None = False,
    deform_bones_only: bool | typing.Any | None = False,
    include_animations: bool | typing.Any | None = True,
    include_all_actions: bool | typing.Any | None = True,
    export_animation_type_selection: str | None = "sample",
    sampling_rate: typing.Any | None = 1,
    keep_smooth_curves: bool | typing.Any | None = False,
    keep_keyframes: bool | typing.Any | None = False,
    keep_flat_curves: bool | typing.Any | None = False,
    active_uv_only: bool | typing.Any | None = False,
    use_texture_copies: bool | typing.Any | None = True,
    triangulate: bool | typing.Any | None = True,
    use_object_instantiation: bool | typing.Any | None = True,
    use_blender_profile: bool | typing.Any | None = True,
    sort_by_name: bool | typing.Any | None = False,
    export_object_transformation_type: typing.Any | None = 0,
    export_object_transformation_type_selection: str | None = "matrix",
    export_animation_transformation_type: typing.Any | None = 0,
    export_animation_transformation_type_selection: str | None = "matrix",
    open_sim: bool | typing.Any | None = False,
    limit_precision: bool | typing.Any | None = False,
    keep_bind_info: bool | typing.Any | None = False,
):
    """Save a Collada file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :type filter_glob: str | typing.Any
        :param prop_bc_export_ui_section: Export Section, Only for User Interface organization

    main
    Main -- Data export section.

    geometry
    Geom -- Geometry export section.

    armature
    Arm -- Armature export section.

    animation
    Anim -- Animation export section.

    collada
    Extra -- Collada export section.
        :type prop_bc_export_ui_section: str | None
        :param apply_modifiers: Apply Modifiers, Apply modifiers to exported mesh (non destructive)
        :type apply_modifiers: bool | typing.Any | None
        :param export_mesh_type: Resolution, Modifier resolution for export
        :type export_mesh_type: typing.Any | None
        :param export_mesh_type_selection: Resolution, Modifier resolution for export

    view
    Viewport -- Apply modifier's viewport settings.

    render
    Render -- Apply modifier's render settings.
        :type export_mesh_type_selection: str | None
        :param export_global_forward_selection: Global Forward Axis, Global Forward axis for export

    X
    X -- Global Forward is positive X Axis.

    Y
    Y -- Global Forward is positive Y Axis.

    Z
    Z -- Global Forward is positive Z Axis.

    -X
    -X -- Global Forward is negative X Axis.

    -Y
    -Y -- Global Forward is negative Y Axis.

    -Z
    -Z -- Global Forward is negative Z Axis.
        :type export_global_forward_selection: str | None
        :param export_global_up_selection: Global Up Axis, Global Up axis for export

    X
    X -- Global UP is positive X Axis.

    Y
    Y -- Global UP is positive Y Axis.

    Z
    Z -- Global UP is positive Z Axis.

    -X
    -X -- Global UP is negative X Axis.

    -Y
    -Y -- Global UP is negative Y Axis.

    -Z
    -Z -- Global UP is negative Z Axis.
        :type export_global_up_selection: str | None
        :param apply_global_orientation: Apply Global Orientation, Rotate all root objects to match the global orientation settings otherwise set the global orientation per Collada asset
        :type apply_global_orientation: bool | typing.Any | None
        :param selected: Selection Only, Export only selected elements
        :type selected: bool | typing.Any | None
        :param include_children: Include Children, Export all children of selected objects (even if not selected)
        :type include_children: bool | typing.Any | None
        :param include_armatures: Include Armatures, Export related armatures (even if not selected)
        :type include_armatures: bool | typing.Any | None
        :param include_shapekeys: Include Shape Keys, Export all Shape Keys from Mesh Objects
        :type include_shapekeys: bool | typing.Any | None
        :param deform_bones_only: Deform Bones Only, Only export deforming bones with armatures
        :type deform_bones_only: bool | typing.Any | None
        :param include_animations: Include Animations, Export animations if available (exporting animations will enforce the decomposition of node transforms into  <translation> <rotation> and <scale> components)
        :type include_animations: bool | typing.Any | None
        :param include_all_actions: Include all Actions, Export also unassigned actions (this allows you to export entire animation libraries for your character(s))
        :type include_all_actions: bool | typing.Any | None
        :param export_animation_type_selection: Key Type, Type for exported animations (use sample keys or Curve keys)

    sample
    Samples -- Export Sampled points guided by sampling rate.

    keys
    Curves -- Export Curves (note: guided by curve keys).
        :type export_animation_type_selection: str | None
        :param sampling_rate: Sampling Rate, The distance between 2 keyframes (1 to key every frame)
        :type sampling_rate: typing.Any | None
        :param keep_smooth_curves: Keep Smooth curves, Export also the curve handles (if available) (this does only work when the inverse parent matrix is the unity matrix, otherwise you may end up with odd results)
        :type keep_smooth_curves: bool | typing.Any | None
        :param keep_keyframes: Keep Keyframes, Use existing keyframes as additional sample points (this helps when you want to keep manual tweaks)
        :type keep_keyframes: bool | typing.Any | None
        :param keep_flat_curves: All Keyed Curves, Export also curves which have only one key or are totally flat
        :type keep_flat_curves: bool | typing.Any | None
        :param active_uv_only: Only Selected UV Map, Export only the selected UV Map
        :type active_uv_only: bool | typing.Any | None
        :param use_texture_copies: Copy, Copy textures to same folder where the .dae file is exported
        :type use_texture_copies: bool | typing.Any | None
        :param triangulate: Triangulate, Export polygons (quads and n-gons) as triangles
        :type triangulate: bool | typing.Any | None
        :param use_object_instantiation: Use Object Instances, Instantiate multiple Objects from same Data
        :type use_object_instantiation: bool | typing.Any | None
        :param use_blender_profile: Use Blender Profile, Export additional Blender specific information (for material, shaders, bones, etc.)
        :type use_blender_profile: bool | typing.Any | None
        :param sort_by_name: Sort by Object name, Sort exported data by Object name
        :type sort_by_name: bool | typing.Any | None
        :param export_object_transformation_type: Transform, Object Transformation type for translation, scale and rotation
        :type export_object_transformation_type: typing.Any | None
        :param export_object_transformation_type_selection: Transform, Object Transformation type for translation, scale and rotation

    matrix
    Matrix -- Use <matrix> representation for exported transformations.

    decomposed
    Decomposed -- Use <rotate>, <translate> and <scale> representation for exported transformations.
        :type export_object_transformation_type_selection: str | None
        :param export_animation_transformation_type: Transform, Transformation type for translation, scale and rotation. Note: The Animation transformation type in the Anim Tab is always equal to the Object transformation type in the Geom tab
        :type export_animation_transformation_type: typing.Any | None
        :param export_animation_transformation_type_selection: Transform, Transformation type for translation, scale and rotation. Note: The Animation transformation type in the Anim Tab is always equal to the Object transformation type in the Geom tab

    matrix
    Matrix -- Use <matrix> representation for exported transformations.

    decomposed
    Decomposed -- Use <rotate>, <translate> and <scale> representation for exported transformations.
        :type export_animation_transformation_type_selection: str | None
        :param open_sim: Export to SL/OpenSim, Compatibility mode for Second Life, OpenSimulator and other compatible online worlds
        :type open_sim: bool | typing.Any | None
        :param limit_precision: Limit Precision, Reduce the precision of the exported data to 6 digits
        :type limit_precision: bool | typing.Any | None
        :param keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export
        :type keep_bind_info: bool | typing.Any | None
    """

    ...

def collada_import(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    check_existing: bool | typing.Any | None = False,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = True,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    filter_glob: str | typing.Any = "*.dae",
    import_units: bool | typing.Any | None = False,
    custom_normals: bool | typing.Any | None = True,
    fix_orientation: bool | typing.Any | None = False,
    find_chains: bool | typing.Any | None = False,
    auto_connect: bool | typing.Any | None = False,
    min_chain_length: typing.Any | None = 0,
    keep_bind_info: bool | typing.Any | None = False,
):
    """Load a Collada file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :type filter_glob: str | typing.Any
        :param import_units: Import Units, If disabled match import to Blender's current Unit settings, otherwise use the settings from the Imported scene
        :type import_units: bool | typing.Any | None
        :param custom_normals: Custom Normals, Import custom normals, if available (otherwise Blender will compute them)
        :type custom_normals: bool | typing.Any | None
        :param fix_orientation: Fix Leaf Bones, Fix Orientation of Leaf Bones (Collada does only support Joints)
        :type fix_orientation: bool | typing.Any | None
        :param find_chains: Find Bone Chains, Find best matching Bone Chains and ensure bones in chain are connected
        :type find_chains: bool | typing.Any | None
        :param auto_connect: Auto Connect, Set use_connect for parent bones which have exactly one child bone
        :type auto_connect: bool | typing.Any | None
        :param min_chain_length: Minimum Chain Length, When searching Bone Chains disregard chains of length below this value
        :type min_chain_length: typing.Any | None
        :param keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export
        :type keep_bind_info: bool | typing.Any | None
    """

    ...

def context_collection_boolean_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path_iter: str | typing.Any = "",
    data_path_item: str | typing.Any = "",
    type: str | None = "TOGGLE",
):
    """Set boolean values for a collection of items

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
    :type data_path_iter: str | typing.Any
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float)
    :type data_path_item: str | typing.Any
    :param type: Type
    :type type: str | None
    """

    ...

def context_cycle_array(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    reverse: bool | typing.Any | None = False,
):
    """Set a context array value (useful for cycling the active mesh edit mode)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str | typing.Any
    :param reverse: Reverse, Cycle backwards
    :type reverse: bool | typing.Any | None
    """

    ...

def context_cycle_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    reverse: bool | typing.Any | None = False,
    wrap: bool | typing.Any | None = False,
):
    """Toggle a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str | typing.Any
    :param reverse: Reverse, Cycle backwards
    :type reverse: bool | typing.Any | None
    :param wrap: Wrap, Wrap back to the first/last values
    :type wrap: bool | typing.Any | None
    """

    ...

def context_cycle_int(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    reverse: bool | typing.Any | None = False,
    wrap: bool | typing.Any | None = False,
):
    """Set a context value (useful for cycling active material, shape keys, groups, etc.)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str | typing.Any
    :param reverse: Reverse, Cycle backwards
    :type reverse: bool | typing.Any | None
    :param wrap: Wrap, Wrap back to the first/last values
    :type wrap: bool | typing.Any | None
    """

    ...

def context_menu_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str | typing.Any
    """

    ...

def context_modal_mouse(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path_iter: str | typing.Any = "",
    data_path_item: str | typing.Any = "",
    header_text: str | typing.Any = "",
    input_scale: typing.Any | None = 0.01,
    invert: bool | typing.Any | None = False,
    initial_x: typing.Any | None = 0,
):
    """Adjust arbitrary values with mouse input

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
    :type data_path_iter: str | typing.Any
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float)
    :type data_path_item: str | typing.Any
    :param header_text: Header Text, Text to display in header during scale
    :type header_text: str | typing.Any
    :param input_scale: input_scale, Scale the mouse movement by this value before applying the delta
    :type input_scale: typing.Any | None
    :param invert: invert, Invert the mouse input
    :type invert: bool | typing.Any | None
    :param initial_x: initial_x
    :type initial_x: typing.Any | None
    """

    ...

def context_pie_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str | typing.Any
    """

    ...

def context_scale_float(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: typing.Any | None = 1.0,
):
    """Scale a float context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str | typing.Any
    :param value: Value, Assign value
    :type value: typing.Any | None
    """

    ...

def context_scale_int(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: typing.Any | None = 1.0,
    always_step: bool | typing.Any | None = True,
):
    """Scale an int context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str | typing.Any
    :param value: Value, Assign value
    :type value: typing.Any | None
    :param always_step: Always Step, Always adjust the value by a minimum of 1 when 'value' is not 1.0
    :type always_step: bool | typing.Any | None
    """

    ...

def context_set_boolean(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: bool | typing.Any | None = True,
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str | typing.Any
    :param value: Value, Assignment value
    :type value: bool | typing.Any | None
    """

    ...

def context_set_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: str | typing.Any = "",
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str | typing.Any
    :param value: Value, Assignment value (as a string)
    :type value: str | typing.Any
    """

    ...

def context_set_float(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: typing.Any | None = 0.0,
    relative: bool | typing.Any | None = False,
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str | typing.Any
    :param value: Value, Assignment value
    :type value: typing.Any | None
    :param relative: Relative, Apply relative to the current value (delta)
    :type relative: bool | typing.Any | None
    """

    ...

def context_set_id(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: str | typing.Any = "",
):
    """Set a context value to an ID data-block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str | typing.Any
    :param value: Value, Assign value
    :type value: str | typing.Any
    """

    ...

def context_set_int(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: typing.Any | None = 0,
    relative: bool | typing.Any | None = False,
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str | typing.Any
    :param value: Value, Assign value
    :type value: typing.Any | None
    :param relative: Relative, Apply relative to the current value (delta)
    :type relative: bool | typing.Any | None
    """

    ...

def context_set_string(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: str | typing.Any = "",
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str | typing.Any
    :param value: Value, Assign value
    :type value: str | typing.Any
    """

    ...

def context_set_value(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: str | typing.Any = "",
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str | typing.Any
    :param value: Value, Assignment value (as a string)
    :type value: str | typing.Any
    """

    ...

def context_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    module: str | typing.Any = "",
):
    """Toggle a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str | typing.Any
    :param module: Module, Optionally override the context with a module
    :type module: str | typing.Any
    """

    ...

def context_toggle_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value_1: str | typing.Any = "",
    value_2: str | typing.Any = "",
):
    """Toggle a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str | typing.Any
    :param value_1: Value, Toggle enum
    :type value_1: str | typing.Any
    :param value_2: Value, Toggle enum
    :type value_2: str | typing.Any
    """

    ...

def debug_menu(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    debug_value: typing.Any | None = 0,
):
    """Open a popup to set the debug level

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param debug_value: Debug Value
    :type debug_value: typing.Any | None
    """

    ...

def doc_view(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    doc_id: str | typing.Any = "",
):
    """Open online reference docs in a web browser

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param doc_id: Doc ID
    :type doc_id: str | typing.Any
    """

    ...

def doc_view_manual(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    doc_id: str | typing.Any = "",
):
    """Load online manual

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param doc_id: Doc ID
    :type doc_id: str | typing.Any
    """

    ...

def doc_view_manual_ui_context(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """View a context based online manual in a web browser

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def drop_blend_file(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    """

    ...

def drop_import_file(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    directory: str | typing.Any = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
):
    """Operator that allows file handlers to receive file drops

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param directory: Directory, Directory of the file
    :type directory: str | typing.Any
    :param files: Files
    :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
    """

    ...

def gpencil_export_pdf(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = True,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    use_fill: bool | typing.Any | None = True,
    selected_object_type: str | None = "SELECTED",
    stroke_sample: typing.Any | None = 0.0,
    use_normalized_thickness: bool | typing.Any | None = False,
    frame_mode: str | None = "ACTIVE",
):
    """Export grease pencil to PDF

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param use_fill: Fill, Export strokes with fill enabled
        :type use_fill: bool | typing.Any | None
        :param selected_object_type: Object, Which objects to include in the export

    ACTIVE
    Active -- Include only the active object.

    SELECTED
    Selected -- Include selected objects.

    VISIBLE
    Visible -- Include all visible objects.
        :type selected_object_type: str | None
        :param stroke_sample: Sampling, Precision of stroke sampling. Low values mean a more precise result, and zero disables sampling
        :type stroke_sample: typing.Any | None
        :param use_normalized_thickness: Normalize, Export strokes with constant thickness
        :type use_normalized_thickness: bool | typing.Any | None
        :param frame_mode: Frames, Which frames to include in the export

    ACTIVE
    Active -- Include only active frame.

    SELECTED
    Selected -- Include selected frames.

    SCENE
    Scene -- Include all scene frames.
        :type frame_mode: str | None
    """

    ...

def gpencil_export_svg(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = True,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    use_fill: bool | typing.Any | None = True,
    selected_object_type: str | None = "SELECTED",
    stroke_sample: typing.Any | None = 0.0,
    use_normalized_thickness: bool | typing.Any | None = False,
    use_clip_camera: bool | typing.Any | None = False,
):
    """Export grease pencil to SVG

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param use_fill: Fill, Export strokes with fill enabled
        :type use_fill: bool | typing.Any | None
        :param selected_object_type: Object, Which objects to include in the export

    ACTIVE
    Active -- Include only the active object.

    SELECTED
    Selected -- Include selected objects.

    VISIBLE
    Visible -- Include all visible objects.
        :type selected_object_type: str | None
        :param stroke_sample: Sampling, Precision of stroke sampling. Low values mean a more precise result, and zero disables sampling
        :type stroke_sample: typing.Any | None
        :param use_normalized_thickness: Normalize, Export strokes with constant thickness
        :type use_normalized_thickness: bool | typing.Any | None
        :param use_clip_camera: Clip Camera, Clip drawings to camera size when export in camera view
        :type use_clip_camera: bool | typing.Any | None
    """

    ...

def gpencil_import_svg(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    directory: str | typing.Any = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    check_existing: bool | typing.Any | None = False,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = True,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    relative_path: bool | typing.Any | None = True,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    resolution: typing.Any | None = 10,
    scale: typing.Any | None = 10.0,
):
    """Import SVG into grease pencil

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param directory: Directory, Directory of the file
        :type directory: str | typing.Any
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param resolution: Resolution, Resolution of the generated strokes
        :type resolution: typing.Any | None
        :param scale: Scale, Scale of the final strokes
        :type scale: typing.Any | None
    """

    ...

def interface_theme_preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
    remove_name: bool | typing.Any | None = False,
    remove_active: bool | typing.Any | None = False,
):
    """Add or remove a theme preset

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str | typing.Any
    :param remove_name: remove_name
    :type remove_name: bool | typing.Any | None
    :param remove_active: remove_active
    :type remove_active: bool | typing.Any | None
    """

    ...

def keyconfig_preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
    remove_name: bool | typing.Any | None = False,
    remove_active: bool | typing.Any | None = False,
):
    """Add or remove a Key-config Preset

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str | typing.Any
    :param remove_name: remove_name
    :type remove_name: bool | typing.Any | None
    :param remove_active: remove_active
    :type remove_active: bool | typing.Any | None
    """

    ...

def lib_reload(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    library: str | typing.Any = "",
    filepath: str | typing.Any = "",
    directory: str | typing.Any = "",
    filename: str | typing.Any = "",
    hide_props_region: bool | typing.Any | None = True,
    check_existing: bool | typing.Any | None = False,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    relative_path: bool | typing.Any | None = True,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
):
    """Reload the given library

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param library: Library, Library to reload
        :type library: str | typing.Any
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param directory: Directory, Directory of the file
        :type directory: str | typing.Any
        :param filename: File Name, Name of the file
        :type filename: str | typing.Any
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
    """

    ...

def lib_relocate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    library: str | typing.Any = "",
    filepath: str | typing.Any = "",
    directory: str | typing.Any = "",
    filename: str | typing.Any = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    hide_props_region: bool | typing.Any | None = True,
    check_existing: bool | typing.Any | None = False,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    relative_path: bool | typing.Any | None = True,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
):
    """Relocate the given library to one or several others

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param library: Library, Library to relocate
        :type library: str | typing.Any
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param directory: Directory, Directory of the file
        :type directory: str | typing.Any
        :param filename: File Name, Name of the file
        :type filename: str | typing.Any
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
    """

    ...

def link(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    directory: str | typing.Any = "",
    filename: str | typing.Any = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    check_existing: bool | typing.Any | None = False,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = True,
    filemode: typing.Any | None = 1,
    relative_path: bool | typing.Any | None = True,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    link: bool | typing.Any | None = True,
    do_reuse_local_id: bool | typing.Any | None = False,
    clear_asset_data: bool | typing.Any | None = False,
    autoselect: bool | typing.Any | None = True,
    active_collection: bool | typing.Any | None = True,
    instance_collections: bool | typing.Any | None = True,
    instance_object_data: bool | typing.Any | None = True,
):
    """Link from a Library .blend file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param directory: Directory, Directory of the file
        :type directory: str | typing.Any
        :param filename: File Name, Name of the file
        :type filename: str | typing.Any
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param link: Link, Link the objects or data-blocks rather than appending
        :type link: bool | typing.Any | None
        :param do_reuse_local_id: Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy
        :type do_reuse_local_id: bool | typing.Any | None
        :param clear_asset_data: Clear Asset Data, Don't add asset meta-data or tags from the original data-block
        :type clear_asset_data: bool | typing.Any | None
        :param autoselect: Select, Select new objects
        :type autoselect: bool | typing.Any | None
        :param active_collection: Active Collection, Put new objects on the active collection
        :type active_collection: bool | typing.Any | None
        :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
        :type instance_collections: bool | typing.Any | None
        :param instance_object_data: Instance Object Data, Create instances for object data which are not referenced by any objects
        :type instance_object_data: bool | typing.Any | None
    """

    ...

def memory_statistics(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Print memory statistics to the console

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def obj_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    export_animation: bool | typing.Any | None = False,
    start_frame: typing.Any | None = -2147483648,
    end_frame: typing.Any | None = 2147483647,
    forward_axis: str | None = "NEGATIVE_Z",
    up_axis: str | None = "Y",
    global_scale: typing.Any | None = 1.0,
    apply_modifiers: bool | typing.Any | None = True,
    export_eval_mode: str | None = "DAG_EVAL_VIEWPORT",
    export_selected_objects: bool | typing.Any | None = False,
    export_uv: bool | typing.Any | None = True,
    export_normals: bool | typing.Any | None = True,
    export_colors: bool | typing.Any | None = False,
    export_materials: bool | typing.Any | None = True,
    export_pbr_extensions: bool | typing.Any | None = False,
    path_mode: str | None = "AUTO",
    export_triangulated_mesh: bool | typing.Any | None = False,
    export_curves_as_nurbs: bool | typing.Any | None = False,
    export_object_groups: bool | typing.Any | None = False,
    export_material_groups: bool | typing.Any | None = False,
    export_vertex_groups: bool | typing.Any | None = False,
    export_smooth_groups: bool | typing.Any | None = False,
    smooth_group_bitflags: bool | typing.Any | None = False,
    filter_glob: str | typing.Any = "*.obj;*.mtl",
):
    """Save the scene to a Wavefront OBJ file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param export_animation: Export Animation, Export multiple frames instead of the current frame only
        :type export_animation: bool | typing.Any | None
        :param start_frame: Start Frame, The first frame to be exported
        :type start_frame: typing.Any | None
        :param end_frame: End Frame, The last frame to be exported
        :type end_frame: typing.Any | None
        :param forward_axis: Forward Axis

    X
    X -- Positive X axis.

    Y
    Y -- Positive Y axis.

    Z
    Z -- Positive Z axis.

    NEGATIVE_X
    -X -- Negative X axis.

    NEGATIVE_Y
    -Y -- Negative Y axis.

    NEGATIVE_Z
    -Z -- Negative Z axis.
        :type forward_axis: str | None
        :param up_axis: Up Axis

    X
    X -- Positive X axis.

    Y
    Y -- Positive Y axis.

    Z
    Z -- Positive Z axis.

    NEGATIVE_X
    -X -- Negative X axis.

    NEGATIVE_Y
    -Y -- Negative Y axis.

    NEGATIVE_Z
    -Z -- Negative Z axis.
        :type up_axis: str | None
        :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
        :type global_scale: typing.Any | None
        :param apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes
        :type apply_modifiers: bool | typing.Any | None
        :param export_eval_mode: Object Properties, Determines properties like object visibility, modifiers etc., where they differ for Render and Viewport

    DAG_EVAL_RENDER
    Render -- Export objects as they appear in render.

    DAG_EVAL_VIEWPORT
    Viewport -- Export objects as they appear in the viewport.
        :type export_eval_mode: str | None
        :param export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects
        :type export_selected_objects: bool | typing.Any | None
        :param export_uv: Export UVs
        :type export_uv: bool | typing.Any | None
        :param export_normals: Export Normals, Export per-face normals if the face is flat-shaded, per-face-per-loop normals if smooth-shaded
        :type export_normals: bool | typing.Any | None
        :param export_colors: Export Colors, Export per-vertex colors
        :type export_colors: bool | typing.Any | None
        :param export_materials: Export Materials, Export MTL library. There must be a Principled-BSDF node for image textures to be exported to the MTL file
        :type export_materials: bool | typing.Any | None
        :param export_pbr_extensions: Export Materials with PBR Extensions, Export MTL library using PBR extensions (roughness, metallic, sheen, coat, anisotropy, transmission)
        :type export_pbr_extensions: bool | typing.Any | None
        :param path_mode: Path Mode, Method used to reference paths

    AUTO
    Auto -- Use relative paths with subdirectories only.

    ABSOLUTE
    Absolute -- Always write absolute paths.

    RELATIVE
    Relative -- Write relative paths where possible.

    MATCH
    Match -- Match absolute/relative setting with input path.

    STRIP
    Strip -- Write filename only.

    COPY
    Copy -- Copy the file to the destination path.
        :type path_mode: str | None
        :param export_triangulated_mesh: Export Triangulated Mesh, All ngons with four or more vertices will be triangulated. Meshes in the scene will not be affected. Behaves like Triangulate Modifier with ngon-method: "Beauty", quad-method: "Shortest Diagonal", min vertices: 4
        :type export_triangulated_mesh: bool | typing.Any | None
        :param export_curves_as_nurbs: Export Curves as NURBS, Export curves in parametric form instead of exporting as mesh
        :type export_curves_as_nurbs: bool | typing.Any | None
        :param export_object_groups: Export Object Groups, Append mesh name to object name, separated by a '_'
        :type export_object_groups: bool | typing.Any | None
        :param export_material_groups: Export Material Groups, Generate an OBJ group for each part of a geometry using a different material
        :type export_material_groups: bool | typing.Any | None
        :param export_vertex_groups: Export Vertex Groups, Export the name of the vertex group of a face. It is approximated by choosing the vertex group with the most members among the vertices of a face
        :type export_vertex_groups: bool | typing.Any | None
        :param export_smooth_groups: Export Smooth Groups, Every smooth-shaded face is assigned group "1" and every flat-shaded face "off"
        :type export_smooth_groups: bool | typing.Any | None
        :param smooth_group_bitflags: Generate Bitflags for Smooth Groups
        :type smooth_group_bitflags: bool | typing.Any | None
        :param filter_glob: Extension Filter
        :type filter_glob: str | typing.Any
    """

    ...

def obj_import(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    directory: str | typing.Any = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    check_existing: bool | typing.Any | None = False,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    global_scale: typing.Any | None = 1.0,
    clamp_size: typing.Any | None = 0.0,
    forward_axis: str | None = "NEGATIVE_Z",
    up_axis: str | None = "Y",
    use_split_objects: bool | typing.Any | None = True,
    use_split_groups: bool | typing.Any | None = False,
    import_vertex_groups: bool | typing.Any | None = False,
    validate_meshes: bool | typing.Any | None = False,
    collection_separator: str | typing.Any = "",
    filter_glob: str | typing.Any = "*.obj;*.mtl",
):
    """Load a Wavefront OBJ scene

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param directory: Directory, Directory of the file
        :type directory: str | typing.Any
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
        :type global_scale: typing.Any | None
        :param clamp_size: Clamp Bounding Box, Resize the objects to keep bounding box under this value. Value 0 disables clamping
        :type clamp_size: typing.Any | None
        :param forward_axis: Forward Axis

    X
    X -- Positive X axis.

    Y
    Y -- Positive Y axis.

    Z
    Z -- Positive Z axis.

    NEGATIVE_X
    -X -- Negative X axis.

    NEGATIVE_Y
    -Y -- Negative Y axis.

    NEGATIVE_Z
    -Z -- Negative Z axis.
        :type forward_axis: str | None
        :param up_axis: Up Axis

    X
    X -- Positive X axis.

    Y
    Y -- Positive Y axis.

    Z
    Z -- Positive Z axis.

    NEGATIVE_X
    -X -- Negative X axis.

    NEGATIVE_Y
    -Y -- Negative Y axis.

    NEGATIVE_Z
    -Z -- Negative Z axis.
        :type up_axis: str | None
        :param use_split_objects: Split By Object, Import each OBJ 'o' as a separate object
        :type use_split_objects: bool | typing.Any | None
        :param use_split_groups: Split By Group, Import each OBJ 'g' as a separate object
        :type use_split_groups: bool | typing.Any | None
        :param import_vertex_groups: Vertex Groups, Import OBJ groups as vertex groups
        :type import_vertex_groups: bool | typing.Any | None
        :param validate_meshes: Validate Meshes, Check imported mesh objects for invalid data (slow)
        :type validate_meshes: bool | typing.Any | None
        :param collection_separator: Path Separator, Character used to separate objects name into hierarchical structure
        :type collection_separator: str | typing.Any
        :param filter_glob: Extension Filter
        :type filter_glob: str | typing.Any
    """

    ...

def open_mainfile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    hide_props_region: bool | typing.Any | None = True,
    check_existing: bool | typing.Any | None = False,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    load_ui: bool | typing.Any | None = True,
    use_scripts: bool | typing.Any | None = True,
    display_file_selector: bool | typing.Any | None = True,
    state: typing.Any | None = 0,
):
    """Open a Blender file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param load_ui: Load UI, Load user interface setup in the .blend file
        :type load_ui: bool | typing.Any | None
        :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
        :type use_scripts: bool | typing.Any | None
        :param display_file_selector: Display File Selector
        :type display_file_selector: bool | typing.Any | None
        :param state: State
        :type state: typing.Any | None
    """

    ...

def operator_cheat_sheet(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """List all the operators in a text-block, useful for scripting

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def operator_defaults(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Set the active operator to its default values

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def operator_pie_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    prop_string: str | typing.Any = "",
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Operator, Operator name (in Python as string)
    :type data_path: str | typing.Any
    :param prop_string: Property, Property name (as a string)
    :type prop_string: str | typing.Any
    """

    ...

def operator_preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
    remove_name: bool | typing.Any | None = False,
    remove_active: bool | typing.Any | None = False,
    operator: str | typing.Any = "",
):
    """Add or remove an Operator Preset

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str | typing.Any
    :param remove_name: remove_name
    :type remove_name: bool | typing.Any | None
    :param remove_active: remove_active
    :type remove_active: bool | typing.Any | None
    :param operator: Operator
    :type operator: str | typing.Any
    """

    ...

def operator_presets_cleanup(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    operator: str | typing.Any = "",
    properties: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
):
    """Remove outdated operator properties from presets that may cause problems

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param operator: operator
    :type operator: str | typing.Any
    :param properties: properties
    :type properties: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
    """

    ...

def owner_disable(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    owner_id: str | typing.Any = "",
):
    """Disable add-on for workspace

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param owner_id: UI Tag
    :type owner_id: str | typing.Any
    """

    ...

def owner_enable(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    owner_id: str | typing.Any = "",
):
    """Enable add-on for workspace

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param owner_id: UI Tag
    :type owner_id: str | typing.Any
    """

    ...

def path_open(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
):
    """Open a path in a file browser

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    """

    ...

def ply_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    forward_axis: str | None = "Y",
    up_axis: str | None = "Z",
    global_scale: typing.Any | None = 1.0,
    apply_modifiers: bool | typing.Any | None = True,
    export_selected_objects: bool | typing.Any | None = False,
    export_uv: bool | typing.Any | None = True,
    export_normals: bool | typing.Any | None = False,
    export_colors: str | None = "SRGB",
    export_attributes: bool | typing.Any | None = True,
    export_triangulated_mesh: bool | typing.Any | None = False,
    ascii_format: bool | typing.Any | None = False,
    filter_glob: str | typing.Any = "*.ply",
):
    """Save the scene to a PLY file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param forward_axis: Forward Axis

    X
    X -- Positive X axis.

    Y
    Y -- Positive Y axis.

    Z
    Z -- Positive Z axis.

    NEGATIVE_X
    -X -- Negative X axis.

    NEGATIVE_Y
    -Y -- Negative Y axis.

    NEGATIVE_Z
    -Z -- Negative Z axis.
        :type forward_axis: str | None
        :param up_axis: Up Axis

    X
    X -- Positive X axis.

    Y
    Y -- Positive Y axis.

    Z
    Z -- Positive Z axis.

    NEGATIVE_X
    -X -- Negative X axis.

    NEGATIVE_Y
    -Y -- Negative Y axis.

    NEGATIVE_Z
    -Z -- Negative Z axis.
        :type up_axis: str | None
        :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
        :type global_scale: typing.Any | None
        :param apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes
        :type apply_modifiers: bool | typing.Any | None
        :param export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects
        :type export_selected_objects: bool | typing.Any | None
        :param export_uv: Export UVs
        :type export_uv: bool | typing.Any | None
        :param export_normals: Export Vertex Normals, Export specific vertex normals if available, export calculated normals otherwise
        :type export_normals: bool | typing.Any | None
        :param export_colors: Export Vertex Colors, Export vertex color attributes

    NONE
    None -- Do not import/export color attributes.

    SRGB
    sRGB -- Vertex colors in the file are in sRGB color space.

    LINEAR
    Linear -- Vertex colors in the file are in linear color space.
        :type export_colors: str | None
        :param export_attributes: Export Vertex Attributes, Export custom vertex attributes
        :type export_attributes: bool | typing.Any | None
        :param export_triangulated_mesh: Export Triangulated Mesh, All ngons with four or more vertices will be triangulated. Meshes in the scene will not be affected. Behaves like Triangulate Modifier with ngon-method: "Beauty", quad-method: "Shortest Diagonal", min vertices: 4
        :type export_triangulated_mesh: bool | typing.Any | None
        :param ascii_format: ASCII Format, Export file in ASCII format, export as binary otherwise
        :type ascii_format: bool | typing.Any | None
        :param filter_glob: Extension Filter
        :type filter_glob: str | typing.Any
    """

    ...

def ply_import(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    directory: str | typing.Any = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    check_existing: bool | typing.Any | None = False,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    global_scale: typing.Any | None = 1.0,
    use_scene_unit: bool | typing.Any | None = False,
    forward_axis: str | None = "Y",
    up_axis: str | None = "Z",
    merge_verts: bool | typing.Any | None = False,
    import_colors: str | None = "SRGB",
    import_attributes: bool | typing.Any | None = True,
    filter_glob: str | typing.Any = "*.ply",
):
    """Import an PLY file as an object

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param directory: Directory, Directory of the file
        :type directory: str | typing.Any
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param global_scale: Scale
        :type global_scale: typing.Any | None
        :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to imported data
        :type use_scene_unit: bool | typing.Any | None
        :param forward_axis: Forward Axis

    X
    X -- Positive X axis.

    Y
    Y -- Positive Y axis.

    Z
    Z -- Positive Z axis.

    NEGATIVE_X
    -X -- Negative X axis.

    NEGATIVE_Y
    -Y -- Negative Y axis.

    NEGATIVE_Z
    -Z -- Negative Z axis.
        :type forward_axis: str | None
        :param up_axis: Up Axis

    X
    X -- Positive X axis.

    Y
    Y -- Positive Y axis.

    Z
    Z -- Positive Z axis.

    NEGATIVE_X
    -X -- Negative X axis.

    NEGATIVE_Y
    -Y -- Negative Y axis.

    NEGATIVE_Z
    -Z -- Negative Z axis.
        :type up_axis: str | None
        :param merge_verts: Merge Vertices, Merges vertices by distance
        :type merge_verts: bool | typing.Any | None
        :param import_colors: Vertex Colors, Import vertex color attributes

    NONE
    None -- Do not import/export color attributes.

    SRGB
    sRGB -- Vertex colors in the file are in sRGB color space.

    LINEAR
    Linear -- Vertex colors in the file are in linear color space.
        :type import_colors: str | None
        :param import_attributes: Vertex Attributes, Import custom vertex attributes
        :type import_attributes: bool | typing.Any | None
        :param filter_glob: Extension Filter
        :type filter_glob: str | typing.Any
    """

    ...

def previews_batch_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    directory: str | typing.Any = "",
    filter_blender: bool | typing.Any | None = True,
    filter_folder: bool | typing.Any | None = True,
    use_scenes: bool | typing.Any | None = True,
    use_collections: bool | typing.Any | None = True,
    use_objects: bool | typing.Any | None = True,
    use_intern_data: bool | typing.Any | None = True,
    use_trusted: bool | typing.Any | None = False,
    use_backups: bool | typing.Any | None = True,
):
    """Clear selected .blend file's previews

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param files: files
    :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
    :param directory: directory
    :type directory: str | typing.Any
    :param filter_blender: filter_blender
    :type filter_blender: bool | typing.Any | None
    :param filter_folder: filter_folder
    :type filter_folder: bool | typing.Any | None
    :param use_scenes: Scenes, Clear scenes' previews
    :type use_scenes: bool | typing.Any | None
    :param use_collections: Collections, Clear collections' previews
    :type use_collections: bool | typing.Any | None
    :param use_objects: Objects, Clear objects' previews
    :type use_objects: bool | typing.Any | None
    :param use_intern_data: Materials & Textures, Clear 'internal' previews (materials, textures, images, etc.)
    :type use_intern_data: bool | typing.Any | None
    :param use_trusted: Trusted Blend Files, Enable Python evaluation for selected files
    :type use_trusted: bool | typing.Any | None
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with cleared previews
    :type use_backups: bool | typing.Any | None
    """

    ...

def previews_batch_generate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    directory: str | typing.Any = "",
    filter_blender: bool | typing.Any | None = True,
    filter_folder: bool | typing.Any | None = True,
    use_scenes: bool | typing.Any | None = True,
    use_collections: bool | typing.Any | None = True,
    use_objects: bool | typing.Any | None = True,
    use_intern_data: bool | typing.Any | None = True,
    use_trusted: bool | typing.Any | None = False,
    use_backups: bool | typing.Any | None = True,
):
    """Generate selected .blend file's previews

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param files: Collection of file paths with common directory root
    :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
    :param directory: Root path of all files listed in files collection
    :type directory: str | typing.Any
    :param filter_blender: Show Blender files in the File Browser
    :type filter_blender: bool | typing.Any | None
    :param filter_folder: Show folders in the File Browser
    :type filter_folder: bool | typing.Any | None
    :param use_scenes: Scenes, Generate scenes' previews
    :type use_scenes: bool | typing.Any | None
    :param use_collections: Collections, Generate collections' previews
    :type use_collections: bool | typing.Any | None
    :param use_objects: Objects, Generate objects' previews
    :type use_objects: bool | typing.Any | None
    :param use_intern_data: Materials & Textures, Generate 'internal' previews (materials, textures, images, etc.)
    :type use_intern_data: bool | typing.Any | None
    :param use_trusted: Trusted Blend Files, Enable Python evaluation for selected files
    :type use_trusted: bool | typing.Any | None
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with generated previews
    :type use_backups: bool | typing.Any | None
    """

    ...

def previews_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    id_type: set[str] | None = {},
):
    """Clear data-block previews (only for some types like objects, materials, textures, etc.)

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param id_type: Data-Block Type, Which data-block previews to clear

    ALL
    All Types.

    GEOMETRY
    All Geometry Types -- Clear previews for scenes, collections and objects.

    SHADING
    All Shading Types -- Clear previews for materials, lights, worlds, textures and images.

    SCENE
    Scenes.

    COLLECTION
    Collections.

    OBJECT
    Objects.

    MATERIAL
    Materials.

    LIGHT
    Lights.

    WORLD
    Worlds.

    TEXTURE
    Textures.

    IMAGE
    Images.
        :type id_type: set[str] | None
    """

    ...

def previews_ensure(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Ensure data-block previews are available and up-to-date (to be saved in .blend file, only for some types like materials, textures, etc.)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def properties_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
):
    """Add your own property to the data-block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Property Edit, Property data_path edit
    :type data_path: str | typing.Any
    """

    ...

def properties_context_change(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    context: str | typing.Any = "",
):
    """Jump to a different tab inside the properties editor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param context: Context
    :type context: str | typing.Any
    """

    ...

def properties_edit(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    property_name: str | typing.Any = "",
    property_type: str | None = "FLOAT",
    is_overridable_library: bool | typing.Any | None = False,
    description: str | typing.Any = "",
    use_soft_limits: bool | typing.Any | None = False,
    array_length: typing.Any | None = 3,
    default_int: typing.Any | None = (
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ),
    min_int: typing.Any | None = -10000,
    max_int: typing.Any | None = 10000,
    soft_min_int: typing.Any | None = -10000,
    soft_max_int: typing.Any | None = 10000,
    step_int: typing.Any | None = 1,
    default_bool: list[bool] | typing.Any | None = (
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ),
    default_float: typing.Any | None = (
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ),
    min_float: typing.Any | None = -10000.0,
    max_float: typing.Any | None = -10000.0,
    soft_min_float: typing.Any | None = -10000.0,
    soft_max_float: typing.Any | None = -10000.0,
    precision: typing.Any | None = 3,
    step_float: typing.Any | None = 0.1,
    subtype: str | None = "",
    default_string: str | typing.Any = "",
    id_type: str | None = "OBJECT",
    eval_string: str | typing.Any = "",
):
    """Change a custom property's type, or adjust how it is displayed in the interface

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param data_path: Property Edit, Property data_path edit
        :type data_path: str | typing.Any
        :param property_name: Property Name, Property name edit
        :type property_name: str | typing.Any
        :param property_type: Type

    FLOAT
    Float -- A single floating-point value.

    FLOAT_ARRAY
    Float Array -- An array of floating-point values.

    INT
    Integer -- A single integer.

    INT_ARRAY
    Integer Array -- An array of integers.

    BOOL
    Boolean -- A true or false value.

    BOOL_ARRAY
    Boolean Array -- An array of true or false values.

    STRING
    String -- A string value.

    DATA_BLOCK
    Data-Block -- A data-block value.

    PYTHON
    Python -- Edit a Python value directly, for unsupported property types.
        :type property_type: str | None
        :param is_overridable_library: Library Overridable, Allow the property to be overridden when the data-block is linked
        :type is_overridable_library: bool | typing.Any | None
        :param description: Description
        :type description: str | typing.Any
        :param use_soft_limits: Soft Limits, Limits the Property Value slider to a range, values outside the range must be inputted numerically
        :type use_soft_limits: bool | typing.Any | None
        :param array_length: Array Length
        :type array_length: typing.Any | None
        :param default_int: Default Value
        :type default_int: typing.Any | None
        :param min_int: Min
        :type min_int: typing.Any | None
        :param max_int: Max
        :type max_int: typing.Any | None
        :param soft_min_int: Soft Min
        :type soft_min_int: typing.Any | None
        :param soft_max_int: Soft Max
        :type soft_max_int: typing.Any | None
        :param step_int: Step
        :type step_int: typing.Any | None
        :param default_bool: Default Value
        :type default_bool: list[bool] | typing.Any | None
        :param default_float: Default Value
        :type default_float: typing.Any | None
        :param min_float: Min
        :type min_float: typing.Any | None
        :param max_float: Max
        :type max_float: typing.Any | None
        :param soft_min_float: Soft Min
        :type soft_min_float: typing.Any | None
        :param soft_max_float: Soft Max
        :type soft_max_float: typing.Any | None
        :param precision: Precision
        :type precision: typing.Any | None
        :param step_float: Step
        :type step_float: typing.Any | None
        :param subtype: Subtype
        :type subtype: str | None
        :param default_string: Default Value
        :type default_string: str | typing.Any
        :param id_type: ID Type
        :type id_type: str | None
        :param eval_string: Value, Python value for unsupported custom property types
        :type eval_string: str | typing.Any
    """

    ...

def properties_edit_value(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    property_name: str | typing.Any = "",
    eval_string: str | typing.Any = "",
):
    """Edit the value of a custom property

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Property Edit, Property data_path edit
    :type data_path: str | typing.Any
    :param property_name: Property Name, Property name edit
    :type property_name: str | typing.Any
    :param eval_string: Value, Value for custom property types that can only be edited as a Python expression
    :type eval_string: str | typing.Any
    """

    ...

def properties_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    property_name: str | typing.Any = "",
):
    """Internal use (edit a property data_path)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Property Edit, Property data_path edit
    :type data_path: str | typing.Any
    :param property_name: Property Name, Property name edit
    :type property_name: str | typing.Any
    """

    ...

def quit_blender(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Quit Blender

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def radial_control(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path_primary: str | typing.Any = "",
    data_path_secondary: str | typing.Any = "",
    use_secondary: str | typing.Any = "",
    rotation_path: str | typing.Any = "",
    color_path: str | typing.Any = "",
    fill_color_path: str | typing.Any = "",
    fill_color_override_path: str | typing.Any = "",
    fill_color_override_test_path: str | typing.Any = "",
    zoom_path: str | typing.Any = "",
    image_id: str | typing.Any = "",
    secondary_tex: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
):
    """Set some size property (e.g. brush size) with mouse wheel

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path_primary: Primary Data Path, Primary path of property to be set by the radial control
    :type data_path_primary: str | typing.Any
    :param data_path_secondary: Secondary Data Path, Secondary path of property to be set by the radial control
    :type data_path_secondary: str | typing.Any
    :param use_secondary: Use Secondary, Path of property to select between the primary and secondary data paths
    :type use_secondary: str | typing.Any
    :param rotation_path: Rotation Path, Path of property used to rotate the texture display
    :type rotation_path: str | typing.Any
    :param color_path: Color Path, Path of property used to set the color of the control
    :type color_path: str | typing.Any
    :param fill_color_path: Fill Color Path, Path of property used to set the fill color of the control
    :type fill_color_path: str | typing.Any
    :param fill_color_override_path: Fill Color Override Path
    :type fill_color_override_path: str | typing.Any
    :param fill_color_override_test_path: Fill Color Override Test
    :type fill_color_override_test_path: str | typing.Any
    :param zoom_path: Zoom Path, Path of property used to set the zoom level for the control
    :type zoom_path: str | typing.Any
    :param image_id: Image ID, Path of ID that is used to generate an image for the control
    :type image_id: str | typing.Any
    :param secondary_tex: Secondary Texture, Tweak brush secondary/mask texture
    :type secondary_tex: bool | typing.Any | None
    :param release_confirm: Confirm On Release, Finish operation on key release
    :type release_confirm: bool | typing.Any | None
    """

    ...

def read_factory_settings(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_factory_startup_app_template_only: bool | typing.Any | None = False,
    app_template: str | typing.Any = "Template",
    use_empty: bool | typing.Any | None = False,
):
    """Load factory default startup file and preferences. To make changes permanent, use "Save Startup File" and "Save Preferences"

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_factory_startup_app_template_only: Factory Startup App-Template Only
    :type use_factory_startup_app_template_only: bool | typing.Any | None
    :type app_template: str | typing.Any
    :param use_empty: Empty, After loading, remove everything except scenes, windows, and workspaces. This makes it possible to load the startup file with its scene configuration and window layout intact, but no objects, materials, animations, ...
    :type use_empty: bool | typing.Any | None
    """

    ...

def read_factory_userpref(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_factory_startup_app_template_only: bool | typing.Any | None = False,
):
    """Load factory default preferences. To make changes to preferences permanent, use "Save Preferences"

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_factory_startup_app_template_only: Factory Startup App-Template Only
    :type use_factory_startup_app_template_only: bool | typing.Any | None
    """

    ...

def read_history(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reloads history and bookmarks

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def read_homefile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    load_ui: bool | typing.Any | None = True,
    use_splash: bool | typing.Any | None = False,
    use_factory_startup: bool | typing.Any | None = False,
    use_factory_startup_app_template_only: bool | typing.Any | None = False,
    app_template: str | typing.Any = "Template",
    use_empty: bool | typing.Any | None = False,
):
    """Open the default file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Path to an alternative start-up file
    :type filepath: str | typing.Any
    :param load_ui: Load UI, Load user interface setup from the .blend file
    :type load_ui: bool | typing.Any | None
    :param use_splash: Splash
    :type use_splash: bool | typing.Any | None
    :param use_factory_startup: Factory Startup, Load the default ('factory startup') blend file. This is independent of the normal start-up file that the user can save
    :type use_factory_startup: bool | typing.Any | None
    :param use_factory_startup_app_template_only: Factory Startup App-Template Only
    :type use_factory_startup_app_template_only: bool | typing.Any | None
    :type app_template: str | typing.Any
    :param use_empty: Empty, After loading, remove everything except scenes, windows, and workspaces. This makes it possible to load the startup file with its scene configuration and window layout intact, but no objects, materials, animations, ...
    :type use_empty: bool | typing.Any | None
    """

    ...

def read_userpref(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Load last saved preferences

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def recover_auto_save(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    hide_props_region: bool | typing.Any | None = True,
    check_existing: bool | typing.Any | None = False,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = False,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "LIST_VERTICAL",
    sort_method: str | None = "",
    use_scripts: bool | typing.Any | None = True,
):
    """Open an automatically saved file to recover it

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
        :type use_scripts: bool | typing.Any | None
    """

    ...

def recover_last_session(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_scripts: bool | typing.Any | None = True,
):
    """Open the last closed file ("quit.blend")

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: bool | typing.Any | None
    """

    ...

def redraw_timer(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "DRAW",
    iterations: typing.Any | None = 10,
    time_limit: typing.Any | None = 0.0,
):
    """Simple redraw timer to test the speed of updating the interface

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    DRAW
    Draw Region -- Draw region.

    DRAW_SWAP
    Draw Region & Swap -- Draw region and swap.

    DRAW_WIN
    Draw Window -- Draw window.

    DRAW_WIN_SWAP
    Draw Window & Swap -- Draw window and swap.

    ANIM_STEP
    Animation Step -- Animation steps.

    ANIM_PLAY
    Animation Play -- Animation playback.

    UNDO
    Undo/Redo -- Undo and redo.
        :type type: str | None
        :param iterations: Iterations, Number of times to redraw
        :type iterations: typing.Any | None
        :param time_limit: Time Limit, Seconds to run the test for (override iterations)
        :type time_limit: typing.Any | None
    """

    ...

def revert_mainfile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_scripts: bool | typing.Any | None = True,
):
    """Reload the saved file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: bool | typing.Any | None
    """

    ...

def save_as_mainfile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    hide_props_region: bool | typing.Any | None = True,
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    compress: bool | typing.Any | None = False,
    relative_remap: bool | typing.Any | None = True,
    copy: bool | typing.Any | None = False,
):
    """Save the current file in the desired location

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param compress: Compress, Write compressed .blend file
        :type compress: bool | typing.Any | None
        :param relative_remap: Remap Relative, Remap relative paths when saving to a different directory
        :type relative_remap: bool | typing.Any | None
        :param copy: Save Copy, Save a copy of the actual working state but does not make saved file active
        :type copy: bool | typing.Any | None
    """

    ...

def save_homefile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Make the current file the default .blend file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def save_mainfile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    hide_props_region: bool | typing.Any | None = True,
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    compress: bool | typing.Any | None = False,
    relative_remap: bool | typing.Any | None = False,
    exit: bool | typing.Any | None = False,
    incremental: bool | typing.Any | None = False,
):
    """Save the current Blender file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param compress: Compress, Write compressed .blend file
        :type compress: bool | typing.Any | None
        :param relative_remap: Remap Relative, Remap relative paths when saving to a different directory
        :type relative_remap: bool | typing.Any | None
        :param exit: Exit, Exit Blender after saving
        :type exit: bool | typing.Any | None
        :param incremental: Incremental, Save the current Blender file with a numerically incremented name that does not overwrite any existing files
        :type incremental: bool | typing.Any | None
    """

    ...

def save_userpref(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Make the current preferences default

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def search_menu(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Pop-up a search over all menus in the current context

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def search_operator(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Pop-up a search over all available operators in current context

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def search_single_menu(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    menu_idname: str | typing.Any = "",
    initial_query: str | typing.Any = "",
):
    """Pop-up a search for a menu in current context

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param menu_idname: Menu Name, Menu to search in
    :type menu_idname: str | typing.Any
    :param initial_query: Initial Query, Query to insert into the search box
    :type initial_query: str | typing.Any
    """

    ...

def set_stereo_3d(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    display_mode: str | None = "ANAGLYPH",
    anaglyph_type: str | None = "RED_CYAN",
    interlace_type: str | None = "ROW_INTERLEAVED",
    use_interlace_swap: bool | typing.Any | None = False,
    use_sidebyside_crosseyed: bool | typing.Any | None = False,
):
    """Toggle 3D stereo support for current window (or change the display mode)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param display_mode: Display Mode
    :type display_mode: str | None
    :param anaglyph_type: Anaglyph Type
    :type anaglyph_type: str | None
    :param interlace_type: Interlace Type
    :type interlace_type: str | None
    :param use_interlace_swap: Swap Left/Right, Swap left and right stereo channels
    :type use_interlace_swap: bool | typing.Any | None
    :param use_sidebyside_crosseyed: Cross-Eyed, Right eye should see left image and vice versa
    :type use_sidebyside_crosseyed: bool | typing.Any | None
    """

    ...

def splash(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Open the splash screen with release info

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def splash_about(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Open a window with information about Blender

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def stl_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    ascii_format: bool | typing.Any | None = False,
    use_batch: bool | typing.Any | None = False,
    export_selected_objects: bool | typing.Any | None = False,
    global_scale: typing.Any | None = 1.0,
    use_scene_unit: bool | typing.Any | None = False,
    forward_axis: str | None = "Y",
    up_axis: str | None = "Z",
    apply_modifiers: bool | typing.Any | None = True,
    filter_glob: str | typing.Any = "*.stl",
):
    """Save the scene to an STL file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param ascii_format: ASCII Format, Export file in ASCII format, export as binary otherwise
        :type ascii_format: bool | typing.Any | None
        :param use_batch: Batch Export, Export each object to a separate file
        :type use_batch: bool | typing.Any | None
        :param export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects
        :type export_selected_objects: bool | typing.Any | None
        :param global_scale: Scale
        :type global_scale: typing.Any | None
        :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to exported data
        :type use_scene_unit: bool | typing.Any | None
        :param forward_axis: Forward Axis

    X
    X -- Positive X axis.

    Y
    Y -- Positive Y axis.

    Z
    Z -- Positive Z axis.

    NEGATIVE_X
    -X -- Negative X axis.

    NEGATIVE_Y
    -Y -- Negative Y axis.

    NEGATIVE_Z
    -Z -- Negative Z axis.
        :type forward_axis: str | None
        :param up_axis: Up Axis

    X
    X -- Positive X axis.

    Y
    Y -- Positive Y axis.

    Z
    Z -- Positive Z axis.

    NEGATIVE_X
    -X -- Negative X axis.

    NEGATIVE_Y
    -Y -- Negative Y axis.

    NEGATIVE_Z
    -Z -- Negative Z axis.
        :type up_axis: str | None
        :param apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes
        :type apply_modifiers: bool | typing.Any | None
        :param filter_glob: Extension Filter
        :type filter_glob: str | typing.Any
    """

    ...

def stl_import(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    directory: str | typing.Any = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    check_existing: bool | typing.Any | None = False,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    global_scale: typing.Any | None = 1.0,
    use_scene_unit: bool | typing.Any | None = False,
    use_facet_normal: bool | typing.Any | None = False,
    forward_axis: str | None = "Y",
    up_axis: str | None = "Z",
    use_mesh_validate: bool | typing.Any | None = False,
    filter_glob: str | typing.Any = "*.stl",
):
    """Import an STL file as an object

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param directory: Directory, Directory of the file
        :type directory: str | typing.Any
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param global_scale: Scale
        :type global_scale: typing.Any | None
        :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to imported data
        :type use_scene_unit: bool | typing.Any | None
        :param use_facet_normal: Facet Normals, Use (import) facet normals (note that this will still give flat shading)
        :type use_facet_normal: bool | typing.Any | None
        :param forward_axis: Forward Axis

    X
    X -- Positive X axis.

    Y
    Y -- Positive Y axis.

    Z
    Z -- Positive Z axis.

    NEGATIVE_X
    -X -- Negative X axis.

    NEGATIVE_Y
    -Y -- Negative Y axis.

    NEGATIVE_Z
    -Z -- Negative Z axis.
        :type forward_axis: str | None
        :param up_axis: Up Axis

    X
    X -- Positive X axis.

    Y
    Y -- Positive Y axis.

    Z
    Z -- Positive Z axis.

    NEGATIVE_X
    -X -- Negative X axis.

    NEGATIVE_Y
    -Y -- Negative Y axis.

    NEGATIVE_Z
    -Z -- Negative Z axis.
        :type up_axis: str | None
        :param use_mesh_validate: Validate Mesh, Validate and correct imported mesh (slow)
        :type use_mesh_validate: bool | typing.Any | None
        :param filter_glob: Extension Filter
        :type filter_glob: str | typing.Any
    """

    ...

def sysinfo(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
):
    """Generate system information, saved into a text file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    """

    ...

def tool_set_by_id(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
    cycle: bool | typing.Any | None = False,
    as_fallback: bool | typing.Any | None = False,
    space_type: str | None = "EMPTY",
):
    """Set the tool by name (for key-maps)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Identifier, Identifier of the tool
    :type name: str | typing.Any
    :param cycle: Cycle, Cycle through tools in this group
    :type cycle: bool | typing.Any | None
    :param as_fallback: Set Fallback, Set the fallback tool instead of the primary tool
    :type as_fallback: bool | typing.Any | None
    :param space_type: Type
    :type space_type: str | None
    """

    ...

def tool_set_by_index(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    index: typing.Any | None = 0,
    cycle: bool | typing.Any | None = False,
    expand: bool | typing.Any | None = True,
    as_fallback: bool | typing.Any | None = False,
    space_type: str | None = "EMPTY",
):
    """Set the tool by index (for key-maps)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: Index in Toolbar
    :type index: typing.Any | None
    :param cycle: Cycle, Cycle through tools in this group
    :type cycle: bool | typing.Any | None
    :param expand: expand, Include tool subgroups
    :type expand: bool | typing.Any | None
    :param as_fallback: Set Fallback, Set the fallback tool instead of the primary
    :type as_fallback: bool | typing.Any | None
    :param space_type: Type
    :type space_type: str | None
    """

    ...

def toolbar(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def toolbar_fallback_pie(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def toolbar_prompt(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Leader key like functionality for accessing tools

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def url_open(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    url: str | typing.Any = "",
):
    """Open a website in the web browser

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param url: URL, URL to open
    :type url: str | typing.Any
    """

    ...

def url_open_preset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "",
    id: str | typing.Any = "",
):
    """Open a preset website in the web browser

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Site
    :type type: str | None
    :param id: Identifier, Optional identifier
    :type id: str | typing.Any
    """

    ...

def usd_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = True,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    filter_glob: str | typing.Any = "*.usd",
    selected_objects_only: bool | typing.Any | None = False,
    visible_objects_only: bool | typing.Any | None = True,
    export_animation: bool | typing.Any | None = False,
    export_hair: bool | typing.Any | None = False,
    export_uvmaps: bool | typing.Any | None = True,
    export_mesh_colors: bool | typing.Any | None = True,
    export_normals: bool | typing.Any | None = True,
    export_materials: bool | typing.Any | None = True,
    export_subdivision: str | None = "BEST_MATCH",
    export_armatures: bool | typing.Any | None = True,
    only_deform_bones: bool | typing.Any | None = False,
    export_shapekeys: bool | typing.Any | None = True,
    use_instancing: bool | typing.Any | None = False,
    evaluation_mode: str | None = "RENDER",
    generate_preview_surface: bool | typing.Any | None = True,
    export_textures: bool | typing.Any | None = True,
    overwrite_textures: bool | typing.Any | None = False,
    relative_paths: bool | typing.Any | None = True,
    root_prim_path: str | typing.Any = "/root",
):
    """Export current scene in a USD archive

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :type filter_glob: str | typing.Any
        :param selected_objects_only: Selection Only, Only export selected objects. Unselected parents of selected objects are exported as empty transform
        :type selected_objects_only: bool | typing.Any | None
        :param visible_objects_only: Visible Only, Only export visible objects. Invisible parents of exported objects are exported as empty transforms
        :type visible_objects_only: bool | typing.Any | None
        :param export_animation: Animation, Export all frames in the render frame range, rather than only the current frame
        :type export_animation: bool | typing.Any | None
        :param export_hair: Hair, Export hair particle systems as USD curves
        :type export_hair: bool | typing.Any | None
        :param export_uvmaps: UV Maps, Include all mesh UV maps in the export
        :type export_uvmaps: bool | typing.Any | None
        :param export_mesh_colors: Color Attributes, Include mesh color attributes in the export
        :type export_mesh_colors: bool | typing.Any | None
        :param export_normals: Normals, Include normals of exported meshes in the export
        :type export_normals: bool | typing.Any | None
        :param export_materials: Materials, Export viewport settings of materials as USD preview materials, and export material assignments as geometry subsets
        :type export_materials: bool | typing.Any | None
        :param export_subdivision: Subdivision Scheme, Choose how subdivision modifiers will be mapped to the USD subdivision scheme during export

    IGNORE
    Ignore -- Subdivision scheme = None, export base mesh without subdivision.

    TESSELLATE
    Tessellate -- Subdivision scheme = None, export subdivided mesh.

    BEST_MATCH
    Best Match -- Subdivision scheme = Catmull-Clark, when possible. Reverts to exporting the subdivided mesh for the Simple subdivision type.
        :type export_subdivision: str | None
        :param export_armatures: Armatures, Export armatures and meshes with armature modifiers as USD skeletons and skinned meshes
        :type export_armatures: bool | typing.Any | None
        :param only_deform_bones: Only Deform Bones, Only export deform bones and their parents
        :type only_deform_bones: bool | typing.Any | None
        :param export_shapekeys: Shape Keys, Export shape keys as USD blend shapes
        :type export_shapekeys: bool | typing.Any | None
        :param use_instancing: Instancing, Export instanced objects as references in USD rather than real objects
        :type use_instancing: bool | typing.Any | None
        :param evaluation_mode: Use Settings for, Determines visibility of objects, modifier settings, and other areas where there are different settings for viewport and rendering

    RENDER
    Render -- Use Render settings for object visibility, modifier settings, etc.

    VIEWPORT
    Viewport -- Use Viewport settings for object visibility, modifier settings, etc.
        :type evaluation_mode: str | None
        :param generate_preview_surface: To USD Preview Surface, Generate an approximate USD Preview Surface shader representation of a Principled BSDF node network
        :type generate_preview_surface: bool | typing.Any | None
        :param export_textures: Export Textures, If exporting materials, export textures referenced by material nodes to a 'textures' directory in the same directory as the USD file
        :type export_textures: bool | typing.Any | None
        :param overwrite_textures: Overwrite Textures, Overwrite existing files when exporting textures
        :type overwrite_textures: bool | typing.Any | None
        :param relative_paths: Relative Paths, Use relative paths to reference external files (i.e. textures, volumes) in USD, otherwise use absolute paths
        :type relative_paths: bool | typing.Any | None
        :param root_prim_path: Root Prim, If set, add a transform primitive with the given path to the stage as the parent of all exported data
        :type root_prim_path: str | typing.Any
    """

    ...

def usd_import(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    check_existing: bool | typing.Any | None = False,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = True,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    relative_path: bool | typing.Any | None = True,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    filter_glob: str | typing.Any = "*.usd",
    scale: typing.Any | None = 1.0,
    set_frame_range: bool | typing.Any | None = True,
    import_cameras: bool | typing.Any | None = True,
    import_curves: bool | typing.Any | None = True,
    import_lights: bool | typing.Any | None = True,
    import_materials: bool | typing.Any | None = True,
    import_meshes: bool | typing.Any | None = True,
    import_volumes: bool | typing.Any | None = True,
    import_shapes: bool | typing.Any | None = True,
    import_skeletons: bool | typing.Any | None = True,
    import_blendshapes: bool | typing.Any | None = True,
    import_subdiv: bool | typing.Any | None = False,
    support_scene_instancing: bool | typing.Any | None = True,
    import_visible_only: bool | typing.Any | None = True,
    create_collection: bool | typing.Any | None = False,
    read_mesh_uvs: bool | typing.Any | None = True,
    read_mesh_colors: bool | typing.Any | None = True,
    read_mesh_attributes: bool | typing.Any | None = True,
    prim_path_mask: str | typing.Any = "",
    import_guide: bool | typing.Any | None = False,
    import_proxy: bool | typing.Any | None = True,
    import_render: bool | typing.Any | None = True,
    import_all_materials: bool | typing.Any | None = False,
    import_usd_preview: bool | typing.Any | None = True,
    set_material_blend: bool | typing.Any | None = True,
    light_intensity_scale: typing.Any | None = 1.0,
    mtl_name_collision_mode: str | None = "MAKE_UNIQUE",
    import_textures_mode: str | None = "IMPORT_PACK",
    import_textures_dir: str | typing.Any = "//textures/",
    tex_name_collision_mode: str | None = "USE_EXISTING",
):
    """Import USD stage into current scene

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :type filter_glob: str | typing.Any
        :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
        :type scale: typing.Any | None
        :param set_frame_range: Set Frame Range, Update the scene's start and end frame to match those of the USD archive
        :type set_frame_range: bool | typing.Any | None
        :param import_cameras: Cameras
        :type import_cameras: bool | typing.Any | None
        :param import_curves: Curves
        :type import_curves: bool | typing.Any | None
        :param import_lights: Lights
        :type import_lights: bool | typing.Any | None
        :param import_materials: Materials
        :type import_materials: bool | typing.Any | None
        :param import_meshes: Meshes
        :type import_meshes: bool | typing.Any | None
        :param import_volumes: Volumes
        :type import_volumes: bool | typing.Any | None
        :param import_shapes: Shapes
        :type import_shapes: bool | typing.Any | None
        :param import_skeletons: Skeletons
        :type import_skeletons: bool | typing.Any | None
        :param import_blendshapes: Blend Shapes
        :type import_blendshapes: bool | typing.Any | None
        :param import_subdiv: Import Subdivision Scheme, Create subdivision surface modifiers based on the USD SubdivisionScheme attribute
        :type import_subdiv: bool | typing.Any | None
        :param support_scene_instancing: Scene Instancing, Import USD scene graph instances as collection instances
        :type support_scene_instancing: bool | typing.Any | None
        :param import_visible_only: Visible Primitives Only, Do not import invisible USD primitives. Only applies to primitives with a non-animated visibility attribute. Primitives with animated visibility will always be imported
        :type import_visible_only: bool | typing.Any | None
        :param create_collection: Create Collection, Add all imported objects to a new collection
        :type create_collection: bool | typing.Any | None
        :param read_mesh_uvs: UV Coordinates, Read mesh UV coordinates
        :type read_mesh_uvs: bool | typing.Any | None
        :param read_mesh_colors: Color Attributes, Read mesh color attributes
        :type read_mesh_colors: bool | typing.Any | None
        :param read_mesh_attributes: Mesh Attributes, Read USD Primvars as mesh attributes
        :type read_mesh_attributes: bool | typing.Any | None
        :param prim_path_mask: Path Mask, Import only the primitive at the given path and its descendants. Multiple paths may be specified in a list delimited by commas or semicolons
        :type prim_path_mask: str | typing.Any
        :param import_guide: Guide, Import guide geometry
        :type import_guide: bool | typing.Any | None
        :param import_proxy: Proxy, Import proxy geometry
        :type import_proxy: bool | typing.Any | None
        :param import_render: Render, Import final render geometry
        :type import_render: bool | typing.Any | None
        :param import_all_materials: Import All Materials, Also import materials that are not used by any geometry. Note that when this option is false, materials referenced by geometry will still be imported
        :type import_all_materials: bool | typing.Any | None
        :param import_usd_preview: Import USD Preview, Convert UsdPreviewSurface shaders to Principled BSDF shader networks
        :type import_usd_preview: bool | typing.Any | None
        :param set_material_blend: Set Material Blend, If the Import USD Preview option is enabled, the material blend method will automatically be set based on the shader's opacity and opacityThreshold inputs
        :type set_material_blend: bool | typing.Any | None
        :param light_intensity_scale: Light Intensity Scale, Scale for the intensity of imported lights
        :type light_intensity_scale: typing.Any | None
        :param mtl_name_collision_mode: Material Name Collision, Behavior when the name of an imported material conflicts with an existing material

    MAKE_UNIQUE
    Make Unique -- Import each USD material as a unique Blender material.

    REFERENCE_EXISTING
    Reference Existing -- If a material with the same name already exists, reference that instead of importing.
        :type mtl_name_collision_mode: str | None
        :param import_textures_mode: Import Textures, Behavior when importing textures from a USDZ archive

    IMPORT_NONE
    None -- Don't import textures.

    IMPORT_PACK
    Packed -- Import textures as packed data.

    IMPORT_COPY
    Copy -- Copy files to textures directory.
        :type import_textures_mode: str | None
        :param import_textures_dir: Textures Directory, Path to the directory where imported textures will be copied
        :type import_textures_dir: str | typing.Any
        :param tex_name_collision_mode: File Name Collision, Behavior when the name of an imported texture file conflicts with an existing file

    USE_EXISTING
    Use Existing -- If a file with the same name already exists, use that instead of copying.

    OVERWRITE
    Overwrite -- Overwrite existing files.
        :type tex_name_collision_mode: str | None
    """

    ...

def window_close(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Close the current window

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def window_fullscreen_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle the current window full-screen

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def window_new(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create a new window

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def window_new_main(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create a new main window with its own workspace and scene selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def xr_navigation_fly(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "VIEWER_FORWARD",
    lock_location_z: bool | typing.Any | None = False,
    lock_direction: bool | typing.Any | None = False,
    speed_frame_based: bool | typing.Any | None = True,
    speed_min: typing.Any | None = 0.018,
    speed_max: typing.Any | None = 0.054,
    speed_interpolation0: typing.Any | None = (0.0, 0.0),
    speed_interpolation1: typing.Any | None = (1.0, 1.0),
):
    """Move/turn relative to the VR viewer or controller

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode, Fly mode

    FORWARD
    Forward -- Move along navigation forward axis.

    BACK
    Back -- Move along navigation back axis.

    LEFT
    Left -- Move along navigation left axis.

    RIGHT
    Right -- Move along navigation right axis.

    UP
    Up -- Move along navigation up axis.

    DOWN
    Down -- Move along navigation down axis.

    TURNLEFT
    Turn Left -- Turn counter-clockwise around navigation up axis.

    TURNRIGHT
    Turn Right -- Turn clockwise around navigation up axis.

    VIEWER_FORWARD
    Viewer Forward -- Move along viewer's forward axis.

    VIEWER_BACK
    Viewer Back -- Move along viewer's back axis.

    VIEWER_LEFT
    Viewer Left -- Move along viewer's left axis.

    VIEWER_RIGHT
    Viewer Right -- Move along viewer's right axis.

    CONTROLLER_FORWARD
    Controller Forward -- Move along controller's forward axis.
        :type mode: str | None
        :param lock_location_z: Lock Elevation, Prevent changes to viewer elevation
        :type lock_location_z: bool | typing.Any | None
        :param lock_direction: Lock Direction, Limit movement to viewer's initial direction
        :type lock_direction: bool | typing.Any | None
        :param speed_frame_based: Frame Based Speed, Apply fixed movement deltas every update
        :type speed_frame_based: bool | typing.Any | None
        :param speed_min: Minimum Speed, Minimum move (turn) speed in meters (radians) per second or frame
        :type speed_min: typing.Any | None
        :param speed_max: Maximum Speed, Maximum move (turn) speed in meters (radians) per second or frame
        :type speed_max: typing.Any | None
        :param speed_interpolation0: Speed Interpolation 0, First cubic spline control point between min/max speeds
        :type speed_interpolation0: typing.Any | None
        :param speed_interpolation1: Speed Interpolation 1, Second cubic spline control point between min/max speeds
        :type speed_interpolation1: typing.Any | None
    """

    ...

def xr_navigation_grab(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    lock_location: bool | typing.Any | None = False,
    lock_location_z: bool | typing.Any | None = False,
    lock_rotation: bool | typing.Any | None = False,
    lock_rotation_z: bool | typing.Any | None = False,
    lock_scale: bool | typing.Any | None = False,
):
    """Navigate the VR scene by grabbing with controllers

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param lock_location: Lock Location, Prevent changes to viewer location
    :type lock_location: bool | typing.Any | None
    :param lock_location_z: Lock Elevation, Prevent changes to viewer elevation
    :type lock_location_z: bool | typing.Any | None
    :param lock_rotation: Lock Rotation, Prevent changes to viewer rotation
    :type lock_rotation: bool | typing.Any | None
    :param lock_rotation_z: Lock Up Orientation, Prevent changes to viewer up orientation
    :type lock_rotation_z: bool | typing.Any | None
    :param lock_scale: Lock Scale, Prevent changes to viewer scale
    :type lock_scale: bool | typing.Any | None
    """

    ...

def xr_navigation_reset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    location: bool | typing.Any | None = True,
    rotation: bool | typing.Any | None = True,
    scale: bool | typing.Any | None = True,
):
    """Reset VR navigation deltas relative to session base pose

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Reset location deltas
    :type location: bool | typing.Any | None
    :param rotation: Rotation, Reset rotation deltas
    :type rotation: bool | typing.Any | None
    :param scale: Scale, Reset scale deltas
    :type scale: bool | typing.Any | None
    """

    ...

def xr_navigation_teleport(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    teleport_axes: list[bool] | typing.Any | None = (True, True, True),
    interpolation: typing.Any | None = 1.0,
    offset: typing.Any | None = 0.0,
    selectable_only: bool | typing.Any | None = True,
    distance: typing.Any | None = 1.70141e38,
    from_viewer: bool | typing.Any | None = False,
    axis: typing.Any | None = (0.0, 0.0, -1.0),
    color: typing.Any | None = (0.35, 0.35, 1.0, 1.0),
):
    """Set VR viewer location to controller raycast hit location

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param teleport_axes: Teleport Axes, Enabled teleport axes in navigation space
    :type teleport_axes: list[bool] | typing.Any | None
    :param interpolation: Interpolation, Interpolation factor between viewer and hit locations
    :type interpolation: typing.Any | None
    :param offset: Offset, Offset along hit normal to subtract from final location
    :type offset: typing.Any | None
    :param selectable_only: Selectable Only, Only allow selectable objects to influence raycast result
    :type selectable_only: bool | typing.Any | None
    :param distance: Maximum raycast distance
    :type distance: typing.Any | None
    :param from_viewer: From Viewer, Use viewer pose as raycast origin
    :type from_viewer: bool | typing.Any | None
    :param axis: Axis, Raycast axis in controller/viewer space
    :type axis: typing.Any | None
    :param color: Color, Raycast color
    :type color: typing.Any | None
    """

    ...

def xr_session_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Open a view for use with virtual reality headsets, or close it if already opened

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...
