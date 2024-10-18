import typing
import collections.abc
import typing_extensions
import bl_operators.wm
import bpy.types
import bpy.typing
import mathutils

def alembic_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
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
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    filter_glob: str = "*.abc",
    start: int | None = -2147483648,
    end: int | None = -2147483648,
    xsamples: int | None = 1,
    gsamples: int | None = 1,
    sh_open: float | None = 0.0,
    sh_close: float | None = 1.0,
    selected: bool | None = False,
    visible_objects_only: bool | None = False,
    flatten: bool | None = False,
    collection: str = "",
    uvs: bool | None = True,
    packuv: bool | None = True,
    normals: bool | None = True,
    vcolors: bool | None = False,
    orcos: bool | None = True,
    face_sets: bool | None = False,
    subdiv_schema: bool | None = False,
    apply_subdiv: bool | None = False,
    curves_as_mesh: bool | None = False,
    use_instancing: bool | None = True,
    global_scale: float | None = 1.0,
    triangulate: bool | None = False,
    quad_method: bpy.typing.ModifierTriangulateQuadMethodItems
    | None = "SHORTEST_DIAGONAL",
    ngon_method: bpy.typing.ModifierTriangulateNgonMethodItems | None = "BEAUTY",
    export_hair: bool | None = True,
    export_particles: bool | None = True,
    export_custom_properties: bool | None = True,
    as_background_job: bool | None = False,
    evaluation_mode: typing.Literal["RENDER", "VIEWPORT"] | None = "RENDER",
    init_scene_frame_range: bool | None = True,
):
    """Export current scene in an Alembic archive

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
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
        :type filter_glob: str
        :param start: Start Frame, Start frame of the export, use the default value to take the start frame of the current scene
        :type start: int | None
        :param end: End Frame, End frame of the export, use the default value to take the end frame of the current scene
        :type end: int | None
        :param xsamples: Transform Samples, Number of times per frame transformations are sampled
        :type xsamples: int | None
        :param gsamples: Geometry Samples, Number of times per frame object data are sampled
        :type gsamples: int | None
        :param sh_open: Shutter Open, Time at which the shutter is open
        :type sh_open: float | None
        :param sh_close: Shutter Close, Time at which the shutter is closed
        :type sh_close: float | None
        :param selected: Selected Objects Only, Export only selected objects
        :type selected: bool | None
        :param visible_objects_only: Visible Objects Only, Export only objects that are visible
        :type visible_objects_only: bool | None
        :param flatten: Flatten Hierarchy, Do not preserve objects' parent/children relationship
        :type flatten: bool | None
        :param collection: Collection
        :type collection: str
        :param uvs: UV Coordinates, Export UV coordinates
        :type uvs: bool | None
        :param packuv: Merge UVs
        :type packuv: bool | None
        :param normals: Normals, Export normals
        :type normals: bool | None
        :param vcolors: Color Attributes, Export color attributes
        :type vcolors: bool | None
        :param orcos: Generated Coordinates, Export undeformed mesh vertex coordinates
        :type orcos: bool | None
        :param face_sets: Face Sets, Export per face shading group assignments
        :type face_sets: bool | None
        :param subdiv_schema: Use Subdivision Schema, Export meshes using Alembic's subdivision schema
        :type subdiv_schema: bool | None
        :param apply_subdiv: Apply Subdivision Surface, Export subdivision surfaces as meshes
        :type apply_subdiv: bool | None
        :param curves_as_mesh: Curves as Mesh, Export curves and NURBS surfaces as meshes
        :type curves_as_mesh: bool | None
        :param use_instancing: Use Instancing, Export data of duplicated objects as Alembic instances; speeds up the export and can be disabled for compatibility with other software
        :type use_instancing: bool | None
        :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
        :type global_scale: float | None
        :param triangulate: Triangulate, Export polygons (quads and n-gons) as triangles
        :type triangulate: bool | None
        :param quad_method: Quad Method, Method for splitting the quads into triangles
        :type quad_method: bpy.typing.ModifierTriangulateQuadMethodItems | None
        :param ngon_method: N-gon Method, Method for splitting the n-gons into triangles
        :type ngon_method: bpy.typing.ModifierTriangulateNgonMethodItems | None
        :param export_hair: Export Hair, Exports hair particle systems as animated curves
        :type export_hair: bool | None
        :param export_particles: Export Particles, Exports non-hair particle systems
        :type export_particles: bool | None
        :param export_custom_properties: Export Custom Properties, Export custom properties to Alembic .userProperties
        :type export_custom_properties: bool | None
        :param as_background_job: Run as Background Job, Enable this to run the import in the background, disable to block Blender while importing. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job
        :type as_background_job: bool | None
        :param evaluation_mode: Settings, Determines visibility of objects, modifier settings, and other areas where there are different settings for viewport and rendering

    RENDER
    Render -- Use Render settings for object visibility, modifier settings, etc.

    VIEWPORT
    Viewport -- Use Viewport settings for object visibility, modifier settings, etc.
        :type evaluation_mode: typing.Literal['RENDER','VIEWPORT'] | None
        :type init_scene_frame_range: bool | None
    """

def alembic_import(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
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
    filter_usd: bool | None = False,
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
    filter_glob: str = "*.abc",
    scale: float | None = 1.0,
    set_frame_range: bool | None = True,
    validate_meshes: bool | None = False,
    always_add_cache_reader: bool | None = False,
    is_sequence: bool | None = False,
    as_background_job: bool | None = False,
):
    """Load an Alembic archive

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param directory: Directory, Directory of the file
        :type directory: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
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
        :type filter_glob: str
        :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
        :type scale: float | None
        :param set_frame_range: Set Frame Range, If checked, update scene's start and end frame to match those of the Alembic archive
        :type set_frame_range: bool | None
        :param validate_meshes: Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)
        :type validate_meshes: bool | None
        :param always_add_cache_reader: Always Add Cache Reader, Add cache modifiers and constraints to imported objects even if they are not animated so that they can be updated when reloading the Alembic archive
        :type always_add_cache_reader: bool | None
        :param is_sequence: Is Sequence, Set to true if the cache is split into separate files
        :type is_sequence: bool | None
        :param as_background_job: Run as Background Job, Enable this to run the export in the background, disable to block Blender while exporting. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job
        :type as_background_job: bool | None
    """

def append(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    directory: str = "",
    filename: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    check_existing: bool | None = False,
    filter_blender: bool | None = True,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = True,
    filemode: int | None = 1,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    link: bool | None = False,
    do_reuse_local_id: bool | None = False,
    clear_asset_data: bool | None = False,
    autoselect: bool | None = True,
    active_collection: bool | None = True,
    instance_collections: bool | None = False,
    instance_object_data: bool | None = True,
    set_fake: bool | None = False,
    use_recursive: bool | None = True,
):
    """Append from a Library .blend file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param directory: Directory, Directory of the file
        :type directory: str
        :param filename: File Name, Name of the file
        :type filename: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
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
        :param link: Link, Link the objects or data-blocks rather than appending
        :type link: bool | None
        :param do_reuse_local_id: Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy
        :type do_reuse_local_id: bool | None
        :param clear_asset_data: Clear Asset Data, Don't add asset meta-data or tags from the original data-block
        :type clear_asset_data: bool | None
        :param autoselect: Select, Select new objects
        :type autoselect: bool | None
        :param active_collection: Active Collection, Put new objects on the active collection
        :type active_collection: bool | None
        :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
        :type instance_collections: bool | None
        :param instance_object_data: Instance Object Data, Create instances for object data which are not referenced by any objects
        :type instance_object_data: bool | None
        :param set_fake: Fake User, Set "Fake User" for appended items (except objects and collections)
        :type set_fake: bool | None
        :param use_recursive: Localize All, Localize all appended data, including those indirectly linked from other libraries
        :type use_recursive: bool | None
    """

def batch_rename(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_type: typing.Literal[
        "OBJECT",
        "COLLECTION",
        "MATERIAL",
        "MESH",
        "CURVE",
        "META",
        "VOLUME",
        "GPENCIL",
        "ARMATURE",
        "LATTICE",
        "LIGHT",
        "LIGHT_PROBE",
        "CAMERA",
        "SPEAKER",
        "BONE",
        "NODE",
        "SEQUENCE_STRIP",
        "ACTION_CLIP",
        "SCENE",
        "BRUSH",
    ]
    | None = "OBJECT",
    data_source: typing.Literal["SELECT", "ALL"] | None = "SELECT",
    actions: bpy.types.bpy_prop_collection[bl_operators.wm.BatchRenameAction]
    | None = None,
):
    """Rename multiple items at once

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_type: Type, Type of data to rename
    :type data_type: typing.Literal['OBJECT','COLLECTION','MATERIAL','MESH','CURVE','META','VOLUME','GPENCIL','ARMATURE','LATTICE','LIGHT','LIGHT_PROBE','CAMERA','SPEAKER','BONE','NODE','SEQUENCE_STRIP','ACTION_CLIP','SCENE','BRUSH'] | None
    :param data_source: Source
    :type data_source: typing.Literal['SELECT','ALL'] | None
    :param actions: actions
    :type actions: bpy.types.bpy_prop_collection[bl_operators.wm.BatchRenameAction] | None
    """

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

def call_menu(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str = "",
):
    """Open a predefined menu

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the menu
    :type name: str
    """

def call_menu_pie(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str = "",
):
    """Open a predefined pie menu

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the pie menu
    :type name: str
    """

def call_panel(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str = "",
    keep_open: bool | None = True,
):
    """Open a predefined panel

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the menu
    :type name: str
    :param keep_open: Keep Open
    :type keep_open: bool | None
    """

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

def collada_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
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
    filter_collada: bool | None = True,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    filter_glob: str = "*.dae",
    prop_bc_export_ui_section: typing.Literal[
        "main", "geometry", "armature", "animation", "collada"
    ]
    | None = "main",
    apply_modifiers: bool | None = False,
    export_mesh_type: int | None = 0,
    export_mesh_type_selection: typing.Literal["view", "render"] | None = "view",
    export_global_forward_selection: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"]
    | None = "Y",
    export_global_up_selection: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"]
    | None = "Z",
    apply_global_orientation: bool | None = False,
    selected: bool | None = False,
    include_children: bool | None = False,
    include_armatures: bool | None = False,
    include_shapekeys: bool | None = False,
    deform_bones_only: bool | None = False,
    include_animations: bool | None = True,
    include_all_actions: bool | None = True,
    export_animation_type_selection: typing.Literal["sample", "keys"] | None = "sample",
    sampling_rate: int | None = 1,
    keep_smooth_curves: bool | None = False,
    keep_keyframes: bool | None = False,
    keep_flat_curves: bool | None = False,
    active_uv_only: bool | None = False,
    use_texture_copies: bool | None = True,
    triangulate: bool | None = True,
    use_object_instantiation: bool | None = True,
    use_blender_profile: bool | None = True,
    sort_by_name: bool | None = False,
    export_object_transformation_type: int | None = 0,
    export_object_transformation_type_selection: typing.Literal["matrix", "decomposed"]
    | None = "matrix",
    export_animation_transformation_type: int | None = 0,
    export_animation_transformation_type_selection: typing.Literal[
        "matrix", "decomposed"
    ]
    | None = "matrix",
    open_sim: bool | None = False,
    limit_precision: bool | None = False,
    keep_bind_info: bool | None = False,
):
    """Save a Collada file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
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
        :type filter_glob: str
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
        :type prop_bc_export_ui_section: typing.Literal['main','geometry','armature','animation','collada'] | None
        :param apply_modifiers: Apply Modifiers, Apply modifiers to exported mesh (non destructive)
        :type apply_modifiers: bool | None
        :param export_mesh_type: Resolution, Modifier resolution for export
        :type export_mesh_type: int | None
        :param export_mesh_type_selection: Resolution, Modifier resolution for export

    view
    Viewport -- Apply modifier's viewport settings.

    render
    Render -- Apply modifier's render settings.
        :type export_mesh_type_selection: typing.Literal['view','render'] | None
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
        :type export_global_forward_selection: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
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
        :type export_global_up_selection: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param apply_global_orientation: Apply Global Orientation, Rotate all root objects to match the global orientation settings otherwise set the global orientation per Collada asset
        :type apply_global_orientation: bool | None
        :param selected: Selection Only, Export only selected elements
        :type selected: bool | None
        :param include_children: Include Children, Export all children of selected objects (even if not selected)
        :type include_children: bool | None
        :param include_armatures: Include Armatures, Export related armatures (even if not selected)
        :type include_armatures: bool | None
        :param include_shapekeys: Include Shape Keys, Export all Shape Keys from Mesh Objects
        :type include_shapekeys: bool | None
        :param deform_bones_only: Deform Bones Only, Only export deforming bones with armatures
        :type deform_bones_only: bool | None
        :param include_animations: Include Animations, Export animations if available (exporting animations will enforce the decomposition of node transforms into <translation> <rotation> and <scale> components)
        :type include_animations: bool | None
        :param include_all_actions: Include all Actions, Export also unassigned actions (this allows you to export entire animation libraries for your character(s))
        :type include_all_actions: bool | None
        :param export_animation_type_selection: Key Type, Type for exported animations (use sample keys or Curve keys)

    sample
    Samples -- Export Sampled points guided by sampling rate.

    keys
    Curves -- Export Curves (note: guided by curve keys).
        :type export_animation_type_selection: typing.Literal['sample','keys'] | None
        :param sampling_rate: Sampling Rate, The distance between 2 keyframes (1 to key every frame)
        :type sampling_rate: int | None
        :param keep_smooth_curves: Keep Smooth curves, Export also the curve handles (if available) (this does only work when the inverse parent matrix is the unity matrix, otherwise you may end up with odd results)
        :type keep_smooth_curves: bool | None
        :param keep_keyframes: Keep Keyframes, Use existing keyframes as additional sample points (this helps when you want to keep manual tweaks)
        :type keep_keyframes: bool | None
        :param keep_flat_curves: All Keyed Curves, Export also curves which have only one key or are totally flat
        :type keep_flat_curves: bool | None
        :param active_uv_only: Only Selected UV Map, Export only the selected UV Map
        :type active_uv_only: bool | None
        :param use_texture_copies: Copy, Copy textures to same folder where the .dae file is exported
        :type use_texture_copies: bool | None
        :param triangulate: Triangulate, Export polygons (quads and n-gons) as triangles
        :type triangulate: bool | None
        :param use_object_instantiation: Use Object Instances, Instantiate multiple Objects from same Data
        :type use_object_instantiation: bool | None
        :param use_blender_profile: Use Blender Profile, Export additional Blender specific information (for material, shaders, bones, etc.)
        :type use_blender_profile: bool | None
        :param sort_by_name: Sort by Object name, Sort exported data by Object name
        :type sort_by_name: bool | None
        :param export_object_transformation_type: Transform, Object Transformation type for translation, scale and rotation
        :type export_object_transformation_type: int | None
        :param export_object_transformation_type_selection: Transform, Object Transformation type for translation, scale and rotation

    matrix
    Matrix -- Use <matrix> representation for exported transformations.

    decomposed
    Decomposed -- Use <rotate>, <translate> and <scale> representation for exported transformations.
        :type export_object_transformation_type_selection: typing.Literal['matrix','decomposed'] | None
        :param export_animation_transformation_type: Transform, Transformation type for translation, scale and rotation. Note: The Animation transformation type in the Anim Tab is always equal to the Object transformation type in the Geom tab
        :type export_animation_transformation_type: int | None
        :param export_animation_transformation_type_selection: Transform, Transformation type for translation, scale and rotation. Note: The Animation transformation type in the Anim Tab is always equal to the Object transformation type in the Geom tab

    matrix
    Matrix -- Use <matrix> representation for exported transformations.

    decomposed
    Decomposed -- Use <rotate>, <translate> and <scale> representation for exported transformations.
        :type export_animation_transformation_type_selection: typing.Literal['matrix','decomposed'] | None
        :param open_sim: Export to SL/OpenSim, Compatibility mode for Second Life, OpenSimulator and other compatible online worlds
        :type open_sim: bool | None
        :param limit_precision: Limit Precision, Reduce the precision of the exported data to 6 digits
        :type limit_precision: bool | None
        :param keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export
        :type keep_bind_info: bool | None
    """

def collada_import(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
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
    filter_collada: bool | None = True,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    filter_glob: str = "*.dae",
    import_units: bool | None = False,
    custom_normals: bool | None = True,
    fix_orientation: bool | None = False,
    find_chains: bool | None = False,
    auto_connect: bool | None = False,
    min_chain_length: int | None = 0,
    keep_bind_info: bool | None = False,
):
    """Load a Collada file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
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
        :type filter_glob: str
        :param import_units: Import Units, If disabled match import to Blender's current Unit settings, otherwise use the settings from the Imported scene
        :type import_units: bool | None
        :param custom_normals: Custom Normals, Import custom normals, if available (otherwise Blender will compute them)
        :type custom_normals: bool | None
        :param fix_orientation: Fix Leaf Bones, Fix Orientation of Leaf Bones (Collada does only support Joints)
        :type fix_orientation: bool | None
        :param find_chains: Find Bone Chains, Find best matching Bone Chains and ensure bones in chain are connected
        :type find_chains: bool | None
        :param auto_connect: Auto Connect, Set use_connect for parent bones which have exactly one child bone
        :type auto_connect: bool | None
        :param min_chain_length: Minimum Chain Length, When searching Bone Chains disregard chains of length below this value
        :type min_chain_length: int | None
        :param keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export
        :type keep_bind_info: bool | None
    """

def collection_export_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Invoke all configured exporters for all collections

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def context_collection_boolean_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path_iter: str = "",
    data_path_item: str = "",
    type: typing.Literal["TOGGLE", "ENABLE", "DISABLE"] | None = "TOGGLE",
):
    """Set boolean values for a collection of items

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
    :type data_path_iter: str
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float)
    :type data_path_item: str
    :param type: Type
    :type type: typing.Literal['TOGGLE','ENABLE','DISABLE'] | None
    """

def context_cycle_array(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    reverse: bool | None = False,
):
    """Set a context array value (useful for cycling the active mesh edit mode)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param reverse: Reverse, Cycle backwards
    :type reverse: bool | None
    """

def context_cycle_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    reverse: bool | None = False,
    wrap: bool | None = False,
):
    """Toggle a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param reverse: Reverse, Cycle backwards
    :type reverse: bool | None
    :param wrap: Wrap, Wrap back to the first/last values
    :type wrap: bool | None
    """

def context_cycle_int(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    reverse: bool | None = False,
    wrap: bool | None = False,
):
    """Set a context value (useful for cycling active material, shape keys, groups, etc.)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param reverse: Reverse, Cycle backwards
    :type reverse: bool | None
    :param wrap: Wrap, Wrap back to the first/last values
    :type wrap: bool | None
    """

def context_menu_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    """

def context_modal_mouse(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path_iter: str = "",
    data_path_item: str = "",
    header_text: str = "",
    input_scale: float | None = 0.01,
    invert: bool | None = False,
    initial_x: int | None = 0,
):
    """Adjust arbitrary values with mouse input

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
    :type data_path_iter: str
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float)
    :type data_path_item: str
    :param header_text: Header Text, Text to display in header during scale
    :type header_text: str
    :param input_scale: input_scale, Scale the mouse movement by this value before applying the delta
    :type input_scale: float | None
    :param invert: invert, Invert the mouse input
    :type invert: bool | None
    :param initial_x: initial_x
    :type initial_x: int | None
    """

def context_pie_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    """

def context_scale_float(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    value: float | None = 1.0,
):
    """Scale a float context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assign value
    :type value: float | None
    """

def context_scale_int(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    value: float | None = 1.0,
    always_step: bool | None = True,
):
    """Scale an int context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assign value
    :type value: float | None
    :param always_step: Always Step, Always adjust the value by a minimum of 1 when 'value' is not 1.0
    :type always_step: bool | None
    """

def context_set_boolean(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    value: bool | None = True,
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assignment value
    :type value: bool | None
    """

def context_set_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    value: str = "",
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assignment value (as a string)
    :type value: str
    """

def context_set_float(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    value: float | None = 0.0,
    relative: bool | None = False,
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assignment value
    :type value: float | None
    :param relative: Relative, Apply relative to the current value (delta)
    :type relative: bool | None
    """

def context_set_id(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    value: str = "",
):
    """Set a context value to an ID data-block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assign value
    :type value: str
    """

def context_set_int(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    value: int | None = 0,
    relative: bool | None = False,
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assign value
    :type value: int | None
    :param relative: Relative, Apply relative to the current value (delta)
    :type relative: bool | None
    """

def context_set_string(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    value: str = "",
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assign value
    :type value: str
    """

def context_set_value(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    value: str = "",
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assignment value (as a string)
    :type value: str
    """

def context_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    module: str = "",
):
    """Toggle a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param module: Module, Optionally override the context with a module
    :type module: str
    """

def context_toggle_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    value_1: str = "",
    value_2: str = "",
):
    """Toggle a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value_1: Value, Toggle enum
    :type value_1: str
    :param value_2: Value, Toggle enum
    :type value_2: str
    """

def debug_menu(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    debug_value: int | None = 0,
):
    """Open a popup to set the debug level

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param debug_value: Debug Value
    :type debug_value: int | None
    """

def doc_view(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    doc_id: str = "",
):
    """Open online reference docs in a web browser

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param doc_id: Doc ID
    :type doc_id: str
    """

def doc_view_manual(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    doc_id: str = "",
):
    """Load online manual

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param doc_id: Doc ID
    :type doc_id: str
    """

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

def drop_blend_file(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str
    """

def drop_import_file(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
):
    """Operator that allows file handlers to receive file drops

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param directory: Directory, Directory of the file
    :type directory: str
    :param files: Files
    :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
    """

def gpencil_export_pdf(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = True,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    use_fill: bool | None = True,
    selected_object_type: typing.Literal["ACTIVE", "SELECTED", "VISIBLE"]
    | None = "SELECTED",
    stroke_sample: float | None = 0.0,
    use_normalized_thickness: bool | None = False,
    frame_mode: typing.Literal["ACTIVE", "SELECTED", "SCENE"] | None = "ACTIVE",
):
    """Export grease pencil to PDF

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
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
        :param use_fill: Fill, Export strokes with fill enabled
        :type use_fill: bool | None
        :param selected_object_type: Object, Which objects to include in the export

    ACTIVE
    Active -- Include only the active object.

    SELECTED
    Selected -- Include selected objects.

    VISIBLE
    Visible -- Include all visible objects.
        :type selected_object_type: typing.Literal['ACTIVE','SELECTED','VISIBLE'] | None
        :param stroke_sample: Sampling, Precision of stroke sampling. Low values mean a more precise result, and zero disables sampling
        :type stroke_sample: float | None
        :param use_normalized_thickness: Normalize, Export strokes with constant thickness
        :type use_normalized_thickness: bool | None
        :param frame_mode: Frames, Which frames to include in the export

    ACTIVE
    Active -- Include only active frame.

    SELECTED
    Selected -- Include selected frames.

    SCENE
    Scene -- Include all scene frames.
        :type frame_mode: typing.Literal['ACTIVE','SELECTED','SCENE'] | None
    """

def gpencil_export_svg(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = True,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    use_fill: bool | None = True,
    selected_object_type: typing.Literal["ACTIVE", "SELECTED", "VISIBLE"]
    | None = "SELECTED",
    stroke_sample: float | None = 0.0,
    use_normalized_thickness: bool | None = False,
    use_clip_camera: bool | None = False,
):
    """Export grease pencil to SVG

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
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
        :param use_fill: Fill, Export strokes with fill enabled
        :type use_fill: bool | None
        :param selected_object_type: Object, Which objects to include in the export

    ACTIVE
    Active -- Include only the active object.

    SELECTED
    Selected -- Include selected objects.

    VISIBLE
    Visible -- Include all visible objects.
        :type selected_object_type: typing.Literal['ACTIVE','SELECTED','VISIBLE'] | None
        :param stroke_sample: Sampling, Precision of stroke sampling. Low values mean a more precise result, and zero disables sampling
        :type stroke_sample: float | None
        :param use_normalized_thickness: Normalize, Export strokes with constant thickness
        :type use_normalized_thickness: bool | None
        :param use_clip_camera: Clip Camera, Clip drawings to camera size when export in camera view
        :type use_clip_camera: bool | None
    """

def gpencil_import_svg(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = True,
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
    resolution: int | None = 10,
    scale: float | None = 10.0,
):
    """Import SVG into grease pencil

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param directory: Directory, Directory of the file
        :type directory: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
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
        :param resolution: Resolution, Resolution of the generated strokes
        :type resolution: int | None
        :param scale: Scale, Scale of the final strokes
        :type scale: float | None
    """

def interface_theme_preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
):
    """Add a custom theme to the preset list

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def interface_theme_preset_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = True,
):
    """Remove a custom theme from the preset list

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def interface_theme_preset_save(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = True,
):
    """Save a custom theme in the preset list

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def keyconfig_preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
):
    """Add a custom keymap configuration to the preset list

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def keyconfig_preset_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = True,
):
    """Remove a custom keymap configuration from the preset list

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def lib_reload(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    library: str = "",
    filepath: str = "",
    directory: str = "",
    filename: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = True,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
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
    """Reload the given library

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param library: Library, Library to reload
        :type library: str
        :param filepath: File Path, Path to file
        :type filepath: str
        :param directory: Directory, Directory of the file
        :type directory: str
        :param filename: File Name, Name of the file
        :type filename: str
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

def lib_relocate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    library: str = "",
    filepath: str = "",
    directory: str = "",
    filename: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = True,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
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
    """Relocate the given library to one or several others

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param library: Library, Library to relocate
        :type library: str
        :param filepath: File Path, Path to file
        :type filepath: str
        :param directory: Directory, Directory of the file
        :type directory: str
        :param filename: File Name, Name of the file
        :type filename: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
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

def link(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    directory: str = "",
    filename: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    check_existing: bool | None = False,
    filter_blender: bool | None = True,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = True,
    filemode: int | None = 1,
    relative_path: bool | None = True,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    link: bool | None = True,
    do_reuse_local_id: bool | None = False,
    clear_asset_data: bool | None = False,
    autoselect: bool | None = True,
    active_collection: bool | None = True,
    instance_collections: bool | None = True,
    instance_object_data: bool | None = True,
):
    """Link from a Library .blend file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param directory: Directory, Directory of the file
        :type directory: str
        :param filename: File Name, Name of the file
        :type filename: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
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
        :param link: Link, Link the objects or data-blocks rather than appending
        :type link: bool | None
        :param do_reuse_local_id: Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy
        :type do_reuse_local_id: bool | None
        :param clear_asset_data: Clear Asset Data, Don't add asset meta-data or tags from the original data-block
        :type clear_asset_data: bool | None
        :param autoselect: Select, Select new objects
        :type autoselect: bool | None
        :param active_collection: Active Collection, Put new objects on the active collection
        :type active_collection: bool | None
        :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
        :type instance_collections: bool | None
        :param instance_object_data: Instance Object Data, Create instances for object data which are not referenced by any objects
        :type instance_object_data: bool | None
    """

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

def obj_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    export_animation: bool | None = False,
    start_frame: int | None = -2147483648,
    end_frame: int | None = 2147483647,
    forward_axis: typing.Literal[
        "X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"
    ]
    | None = "NEGATIVE_Z",
    up_axis: typing.Literal["X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"]
    | None = "Y",
    global_scale: float | None = 1.0,
    apply_modifiers: bool | None = True,
    export_eval_mode: typing.Literal["DAG_EVAL_RENDER", "DAG_EVAL_VIEWPORT"]
    | None = "DAG_EVAL_VIEWPORT",
    export_selected_objects: bool | None = False,
    export_uv: bool | None = True,
    export_normals: bool | None = True,
    export_colors: bool | None = False,
    export_materials: bool | None = True,
    export_pbr_extensions: bool | None = False,
    path_mode: typing.Literal["AUTO", "ABSOLUTE", "RELATIVE", "MATCH", "STRIP", "COPY"]
    | None = "AUTO",
    export_triangulated_mesh: bool | None = False,
    export_curves_as_nurbs: bool | None = False,
    export_object_groups: bool | None = False,
    export_material_groups: bool | None = False,
    export_vertex_groups: bool | None = False,
    export_smooth_groups: bool | None = False,
    smooth_group_bitflags: bool | None = False,
    filter_glob: str = "*.obj;*.mtl",
    collection: str = "",
):
    """Save the scene to a Wavefront OBJ file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
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
        :param export_animation: Export Animation, Export multiple frames instead of the current frame only
        :type export_animation: bool | None
        :param start_frame: Start Frame, The first frame to be exported
        :type start_frame: int | None
        :param end_frame: End Frame, The last frame to be exported
        :type end_frame: int | None
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
        :type forward_axis: typing.Literal['X','Y','Z','NEGATIVE_X','NEGATIVE_Y','NEGATIVE_Z'] | None
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
        :type up_axis: typing.Literal['X','Y','Z','NEGATIVE_X','NEGATIVE_Y','NEGATIVE_Z'] | None
        :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
        :type global_scale: float | None
        :param apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes
        :type apply_modifiers: bool | None
        :param export_eval_mode: Object Properties, Determines properties like object visibility, modifiers etc., where they differ for Render and Viewport

    DAG_EVAL_RENDER
    Render -- Export objects as they appear in render.

    DAG_EVAL_VIEWPORT
    Viewport -- Export objects as they appear in the viewport.
        :type export_eval_mode: typing.Literal['DAG_EVAL_RENDER','DAG_EVAL_VIEWPORT'] | None
        :param export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects
        :type export_selected_objects: bool | None
        :param export_uv: Export UVs
        :type export_uv: bool | None
        :param export_normals: Export Normals, Export per-face normals if the face is flat-shaded, per-face-per-loop normals if smooth-shaded
        :type export_normals: bool | None
        :param export_colors: Export Colors, Export per-vertex colors
        :type export_colors: bool | None
        :param export_materials: Export Materials, Export MTL library. There must be a Principled-BSDF node for image textures to be exported to the MTL file
        :type export_materials: bool | None
        :param export_pbr_extensions: Export Materials with PBR Extensions, Export MTL library using PBR extensions (roughness, metallic, sheen, coat, anisotropy, transmission)
        :type export_pbr_extensions: bool | None
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
        :type path_mode: typing.Literal['AUTO','ABSOLUTE','RELATIVE','MATCH','STRIP','COPY'] | None
        :param export_triangulated_mesh: Export Triangulated Mesh, All ngons with four or more vertices will be triangulated. Meshes in the scene will not be affected. Behaves like Triangulate Modifier with ngon-method: "Beauty", quad-method: "Shortest Diagonal", min vertices: 4
        :type export_triangulated_mesh: bool | None
        :param export_curves_as_nurbs: Export Curves as NURBS, Export curves in parametric form instead of exporting as mesh
        :type export_curves_as_nurbs: bool | None
        :param export_object_groups: Export Object Groups, Append mesh name to object name, separated by a '_'
        :type export_object_groups: bool | None
        :param export_material_groups: Export Material Groups, Generate an OBJ group for each part of a geometry using a different material
        :type export_material_groups: bool | None
        :param export_vertex_groups: Export Vertex Groups, Export the name of the vertex group of a face. It is approximated by choosing the vertex group with the most members among the vertices of a face
        :type export_vertex_groups: bool | None
        :param export_smooth_groups: Export Smooth Groups, Every smooth-shaded face is assigned group "1" and every flat-shaded face "off"
        :type export_smooth_groups: bool | None
        :param smooth_group_bitflags: Generate Bitflags for Smooth Groups
        :type smooth_group_bitflags: bool | None
        :param filter_glob: Extension Filter
        :type filter_glob: str
        :param collection: Collection
        :type collection: str
    """

def obj_import(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    global_scale: float | None = 1.0,
    clamp_size: float | None = 0.0,
    forward_axis: typing.Literal[
        "X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"
    ]
    | None = "NEGATIVE_Z",
    up_axis: typing.Literal["X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"]
    | None = "Y",
    use_split_objects: bool | None = True,
    use_split_groups: bool | None = False,
    import_vertex_groups: bool | None = False,
    validate_meshes: bool | None = True,
    collection_separator: str = "",
    filter_glob: str = "*.obj;*.mtl",
):
    """Load a Wavefront OBJ scene

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param directory: Directory, Directory of the file
        :type directory: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
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
        :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
        :type global_scale: float | None
        :param clamp_size: Clamp Bounding Box, Resize the objects to keep bounding box under this value. Value 0 disables clamping
        :type clamp_size: float | None
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
        :type forward_axis: typing.Literal['X','Y','Z','NEGATIVE_X','NEGATIVE_Y','NEGATIVE_Z'] | None
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
        :type up_axis: typing.Literal['X','Y','Z','NEGATIVE_X','NEGATIVE_Y','NEGATIVE_Z'] | None
        :param use_split_objects: Split By Object, Import each OBJ 'o' as a separate object
        :type use_split_objects: bool | None
        :param use_split_groups: Split By Group, Import each OBJ 'g' as a separate object
        :type use_split_groups: bool | None
        :param import_vertex_groups: Vertex Groups, Import OBJ groups as vertex groups
        :type import_vertex_groups: bool | None
        :param validate_meshes: Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)
        :type validate_meshes: bool | None
        :param collection_separator: Path Separator, Character used to separate objects name into hierarchical structure
        :type collection_separator: str
        :param filter_glob: Extension Filter
        :type filter_glob: str
    """

def open_mainfile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = True,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    load_ui: bool | None = True,
    use_scripts: bool | None = True,
    display_file_selector: bool | None = True,
    state: int | None = 0,
):
    """Open a Blender file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
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
        :param load_ui: Load UI, Load user interface setup in the .blend file
        :type load_ui: bool | None
        :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
        :type use_scripts: bool | None
        :param display_file_selector: Display File Selector
        :type display_file_selector: bool | None
        :param state: State
        :type state: int | None
    """

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

def operator_pie_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    prop_string: str = "",
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Operator, Operator name (in Python as string)
    :type data_path: str
    :param prop_string: Property, Property name (as a string)
    :type prop_string: str
    """

def operator_preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
    operator: str = "",
):
    """Add or remove an Operator Preset

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    :param operator: Operator
    :type operator: str
    """

def operator_presets_cleanup(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    operator: str = "",
    properties: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
):
    """Remove outdated operator properties from presets that may cause problems

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param operator: operator
    :type operator: str
    :param properties: properties
    :type properties: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
    """

def owner_disable(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    owner_id: str = "",
):
    """Disable add-on for workspace

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param owner_id: UI Tag
    :type owner_id: str
    """

def owner_enable(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    owner_id: str = "",
):
    """Enable add-on for workspace

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param owner_id: UI Tag
    :type owner_id: str
    """

def path_open(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
):
    """Open a path in a file browser

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str
    """

def ply_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    forward_axis: typing.Literal[
        "X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"
    ]
    | None = "Y",
    up_axis: typing.Literal["X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"]
    | None = "Z",
    global_scale: float | None = 1.0,
    apply_modifiers: bool | None = True,
    export_selected_objects: bool | None = False,
    collection: str = "",
    export_uv: bool | None = True,
    export_normals: bool | None = False,
    export_colors: typing.Literal["NONE", "SRGB", "LINEAR"] | None = "SRGB",
    export_attributes: bool | None = True,
    export_triangulated_mesh: bool | None = False,
    ascii_format: bool | None = False,
    filter_glob: str = "*.ply",
):
    """Save the scene to a PLY file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
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
        :type forward_axis: typing.Literal['X','Y','Z','NEGATIVE_X','NEGATIVE_Y','NEGATIVE_Z'] | None
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
        :type up_axis: typing.Literal['X','Y','Z','NEGATIVE_X','NEGATIVE_Y','NEGATIVE_Z'] | None
        :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
        :type global_scale: float | None
        :param apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes
        :type apply_modifiers: bool | None
        :param export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects
        :type export_selected_objects: bool | None
        :param collection: Source Collection, Export only objects from this collection (and its children)
        :type collection: str
        :param export_uv: Export UVs
        :type export_uv: bool | None
        :param export_normals: Export Vertex Normals, Export specific vertex normals if available, export calculated normals otherwise
        :type export_normals: bool | None
        :param export_colors: Export Vertex Colors, Export vertex color attributes

    NONE
    None -- Do not import/export color attributes.

    SRGB
    sRGB -- Vertex colors in the file are in sRGB color space.

    LINEAR
    Linear -- Vertex colors in the file are in linear color space.
        :type export_colors: typing.Literal['NONE','SRGB','LINEAR'] | None
        :param export_attributes: Export Vertex Attributes, Export custom vertex attributes
        :type export_attributes: bool | None
        :param export_triangulated_mesh: Export Triangulated Mesh, All ngons with four or more vertices will be triangulated. Meshes in the scene will not be affected. Behaves like Triangulate Modifier with ngon-method: "Beauty", quad-method: "Shortest Diagonal", min vertices: 4
        :type export_triangulated_mesh: bool | None
        :param ascii_format: ASCII Format, Export file in ASCII format, export as binary otherwise
        :type ascii_format: bool | None
        :param filter_glob: Extension Filter
        :type filter_glob: str
    """

def ply_import(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    global_scale: float | None = 1.0,
    use_scene_unit: bool | None = False,
    forward_axis: typing.Literal[
        "X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"
    ]
    | None = "Y",
    up_axis: typing.Literal["X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"]
    | None = "Z",
    merge_verts: bool | None = False,
    import_colors: typing.Literal["NONE", "SRGB", "LINEAR"] | None = "SRGB",
    import_attributes: bool | None = True,
    filter_glob: str = "*.ply",
):
    """Import an PLY file as an object

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param directory: Directory, Directory of the file
        :type directory: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
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
        :param global_scale: Scale
        :type global_scale: float | None
        :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to imported data
        :type use_scene_unit: bool | None
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
        :type forward_axis: typing.Literal['X','Y','Z','NEGATIVE_X','NEGATIVE_Y','NEGATIVE_Z'] | None
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
        :type up_axis: typing.Literal['X','Y','Z','NEGATIVE_X','NEGATIVE_Y','NEGATIVE_Z'] | None
        :param merge_verts: Merge Vertices, Merges vertices by distance
        :type merge_verts: bool | None
        :param import_colors: Vertex Colors, Import vertex color attributes

    NONE
    None -- Do not import/export color attributes.

    SRGB
    sRGB -- Vertex colors in the file are in sRGB color space.

    LINEAR
    Linear -- Vertex colors in the file are in linear color space.
        :type import_colors: typing.Literal['NONE','SRGB','LINEAR'] | None
        :param import_attributes: Vertex Attributes, Import custom vertex attributes
        :type import_attributes: bool | None
        :param filter_glob: Extension Filter
        :type filter_glob: str
    """

def previews_batch_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    directory: str = "",
    filter_blender: bool | None = True,
    filter_folder: bool | None = True,
    use_scenes: bool | None = True,
    use_collections: bool | None = True,
    use_objects: bool | None = True,
    use_intern_data: bool | None = True,
    use_trusted: bool | None = False,
    use_backups: bool | None = True,
):
    """Clear selected .blend file's previews

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param files: files
    :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
    :param directory: directory
    :type directory: str
    :param filter_blender: filter_blender
    :type filter_blender: bool | None
    :param filter_folder: filter_folder
    :type filter_folder: bool | None
    :param use_scenes: Scenes, Clear scenes' previews
    :type use_scenes: bool | None
    :param use_collections: Collections, Clear collections' previews
    :type use_collections: bool | None
    :param use_objects: Objects, Clear objects' previews
    :type use_objects: bool | None
    :param use_intern_data: Materials & Textures, Clear 'internal' previews (materials, textures, images, etc.)
    :type use_intern_data: bool | None
    :param use_trusted: Trusted Blend Files, Enable Python evaluation for selected files
    :type use_trusted: bool | None
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with cleared previews
    :type use_backups: bool | None
    """

def previews_batch_generate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    directory: str = "",
    filter_blender: bool | None = True,
    filter_folder: bool | None = True,
    use_scenes: bool | None = True,
    use_collections: bool | None = True,
    use_objects: bool | None = True,
    use_intern_data: bool | None = True,
    use_trusted: bool | None = False,
    use_backups: bool | None = True,
):
    """Generate selected .blend file's previews

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param files: Collection of file paths with common directory root
    :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
    :param directory: Root path of all files listed in files collection
    :type directory: str
    :param filter_blender: Show Blender files in the File Browser
    :type filter_blender: bool | None
    :param filter_folder: Show folders in the File Browser
    :type filter_folder: bool | None
    :param use_scenes: Scenes, Generate scenes' previews
    :type use_scenes: bool | None
    :param use_collections: Collections, Generate collections' previews
    :type use_collections: bool | None
    :param use_objects: Objects, Generate objects' previews
    :type use_objects: bool | None
    :param use_intern_data: Materials & Textures, Generate 'internal' previews (materials, textures, images, etc.)
    :type use_intern_data: bool | None
    :param use_trusted: Trusted Blend Files, Enable Python evaluation for selected files
    :type use_trusted: bool | None
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with generated previews
    :type use_backups: bool | None
    """

def previews_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    id_type: set[
        typing.Literal[
            "ALL",
            "GEOMETRY",
            "SHADING",
            "SCENE",
            "COLLECTION",
            "OBJECT",
            "MATERIAL",
            "LIGHT",
            "WORLD",
            "TEXTURE",
            "IMAGE",
        ]
    ]
    | None = {},
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
        :type id_type: set[typing.Literal['ALL','GEOMETRY','SHADING','SCENE','COLLECTION','OBJECT','MATERIAL','LIGHT','WORLD','TEXTURE','IMAGE']] | None
    """

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

def properties_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
):
    """Add your own property to the data-block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Property Edit, Property data_path edit
    :type data_path: str
    """

def properties_context_change(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    context: str = "",
):
    """Jump to a different tab inside the properties editor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param context: Context
    :type context: str
    """

def properties_edit(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    property_name: str = "",
    property_type: typing.Literal[
        "FLOAT",
        "FLOAT_ARRAY",
        "INT",
        "INT_ARRAY",
        "BOOL",
        "BOOL_ARRAY",
        "STRING",
        "DATA_BLOCK",
        "PYTHON",
    ]
    | None = "FLOAT",
    is_overridable_library: bool | None = False,
    description: str = "",
    use_soft_limits: bool | None = False,
    array_length: int | None = 3,
    default_int: collections.abc.Iterable[int] | None = (
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
    min_int: int | None = -10000,
    max_int: int | None = 10000,
    soft_min_int: int | None = -10000,
    soft_max_int: int | None = 10000,
    step_int: int | None = 1,
    default_bool: collections.abc.Iterable[bool] | None = (
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
    default_float: collections.abc.Iterable[float] | None = (
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
    min_float: float | None = -10000.0,
    max_float: float | None = -10000.0,
    soft_min_float: float | None = -10000.0,
    soft_max_float: float | None = -10000.0,
    precision: int | None = 3,
    step_float: float | None = 0.1,
    subtype: str | None = "",
    default_string: str = "",
    id_type: typing.Literal[
        "ACTION",
        "ARMATURE",
        "BRUSH",
        "CACHEFILE",
        "CAMERA",
        "COLLECTION",
        "CURVE",
        "CURVES",
        "FONT",
        "GREASEPENCIL",
        "GREASEPENCIL_V3",
        "IMAGE",
        "KEY",
        "LATTICE",
        "LIBRARY",
        "LIGHT",
        "LIGHT_PROBE",
        "LINESTYLE",
        "MASK",
        "MATERIAL",
        "MESH",
        "META",
        "MOVIECLIP",
        "NODETREE",
        "OBJECT",
        "PAINTCURVE",
        "PALETTE",
        "PARTICLE",
        "POINTCLOUD",
        "SCENE",
        "SCREEN",
        "SOUND",
        "SPEAKER",
        "TEXT",
        "TEXTURE",
        "VOLUME",
        "WINDOWMANAGER",
        "WORKSPACE",
        "WORLD",
    ]
    | None = "OBJECT",
    eval_string: str = "",
):
    """Change a custom property's type, or adjust how it is displayed in the interface

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param data_path: Property Edit, Property data_path edit
        :type data_path: str
        :param property_name: Property Name, Property name edit
        :type property_name: str
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
        :type property_type: typing.Literal['FLOAT','FLOAT_ARRAY','INT','INT_ARRAY','BOOL','BOOL_ARRAY','STRING','DATA_BLOCK','PYTHON'] | None
        :param is_overridable_library: Library Overridable, Allow the property to be overridden when the data-block is linked
        :type is_overridable_library: bool | None
        :param description: Description
        :type description: str
        :param use_soft_limits: Soft Limits, Limits the Property Value slider to a range, values outside the range must be inputted numerically
        :type use_soft_limits: bool | None
        :param array_length: Array Length
        :type array_length: int | None
        :param default_int: Default Value
        :type default_int: collections.abc.Iterable[int] | None
        :param min_int: Min
        :type min_int: int | None
        :param max_int: Max
        :type max_int: int | None
        :param soft_min_int: Soft Min
        :type soft_min_int: int | None
        :param soft_max_int: Soft Max
        :type soft_max_int: int | None
        :param step_int: Step
        :type step_int: int | None
        :param default_bool: Default Value
        :type default_bool: collections.abc.Iterable[bool] | None
        :param default_float: Default Value
        :type default_float: collections.abc.Iterable[float] | None
        :param min_float: Min
        :type min_float: float | None
        :param max_float: Max
        :type max_float: float | None
        :param soft_min_float: Soft Min
        :type soft_min_float: float | None
        :param soft_max_float: Soft Max
        :type soft_max_float: float | None
        :param precision: Precision
        :type precision: int | None
        :param step_float: Step
        :type step_float: float | None
        :param subtype: Subtype
        :type subtype: str | None
        :param default_string: Default Value
        :type default_string: str
        :param id_type: ID Type
        :type id_type: typing.Literal['ACTION','ARMATURE','BRUSH','CACHEFILE','CAMERA','COLLECTION','CURVE','CURVES','FONT','GREASEPENCIL','GREASEPENCIL_V3','IMAGE','KEY','LATTICE','LIBRARY','LIGHT','LIGHT_PROBE','LINESTYLE','MASK','MATERIAL','MESH','META','MOVIECLIP','NODETREE','OBJECT','PAINTCURVE','PALETTE','PARTICLE','POINTCLOUD','SCENE','SCREEN','SOUND','SPEAKER','TEXT','TEXTURE','VOLUME','WINDOWMANAGER','WORKSPACE','WORLD'] | None
        :param eval_string: Value, Python value for unsupported custom property types
        :type eval_string: str
    """

def properties_edit_value(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    property_name: str = "",
    eval_string: str = "",
):
    """Edit the value of a custom property

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Property Edit, Property data_path edit
    :type data_path: str
    :param property_name: Property Name, Property name edit
    :type property_name: str
    :param eval_string: Value, Value for custom property types that can only be edited as a Python expression
    :type eval_string: str
    """

def properties_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str = "",
    property_name: str = "",
):
    """Internal use (edit a property data_path)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Property Edit, Property data_path edit
    :type data_path: str
    :param property_name: Property Name, Property name edit
    :type property_name: str
    """

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

def radial_control(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path_primary: str = "",
    data_path_secondary: str = "",
    use_secondary: str = "",
    rotation_path: str = "",
    color_path: str = "",
    fill_color_path: str = "",
    fill_color_override_path: str = "",
    fill_color_override_test_path: str = "",
    zoom_path: str = "",
    image_id: str = "",
    secondary_tex: bool | None = False,
    release_confirm: bool | None = False,
):
    """Set some size property (e.g. brush size) with mouse wheel

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path_primary: Primary Data Path, Primary path of property to be set by the radial control
    :type data_path_primary: str
    :param data_path_secondary: Secondary Data Path, Secondary path of property to be set by the radial control
    :type data_path_secondary: str
    :param use_secondary: Use Secondary, Path of property to select between the primary and secondary data paths
    :type use_secondary: str
    :param rotation_path: Rotation Path, Path of property used to rotate the texture display
    :type rotation_path: str
    :param color_path: Color Path, Path of property used to set the color of the control
    :type color_path: str
    :param fill_color_path: Fill Color Path, Path of property used to set the fill color of the control
    :type fill_color_path: str
    :param fill_color_override_path: Fill Color Override Path
    :type fill_color_override_path: str
    :param fill_color_override_test_path: Fill Color Override Test
    :type fill_color_override_test_path: str
    :param zoom_path: Zoom Path, Path of property used to set the zoom level for the control
    :type zoom_path: str
    :param image_id: Image ID, Path of ID that is used to generate an image for the control
    :type image_id: str
    :param secondary_tex: Secondary Texture, Tweak brush secondary/mask texture
    :type secondary_tex: bool | None
    :param release_confirm: Confirm On Release, Finish operation on key release
    :type release_confirm: bool | None
    """

def read_factory_settings(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_factory_startup_app_template_only: bool | None = False,
    app_template: str = "Template",
    use_empty: bool | None = False,
):
    """Load factory default startup file and preferences. To make changes permanent, use "Save Startup File" and "Save Preferences"

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_factory_startup_app_template_only: Factory Startup App-Template Only
    :type use_factory_startup_app_template_only: bool | None
    :type app_template: str
    :param use_empty: Empty, After loading, remove everything except scenes, windows, and workspaces. This makes it possible to load the startup file with its scene configuration and window layout intact, but no objects, materials, animations, ...
    :type use_empty: bool | None
    """

def read_factory_userpref(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_factory_startup_app_template_only: bool | None = False,
):
    """Load factory default preferences. To make changes to preferences permanent, use "Save Preferences"

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_factory_startup_app_template_only: Factory Startup App-Template Only
    :type use_factory_startup_app_template_only: bool | None
    """

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

def read_homefile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    load_ui: bool | None = True,
    use_splash: bool | None = False,
    use_factory_startup: bool | None = False,
    use_factory_startup_app_template_only: bool | None = False,
    app_template: str = "Template",
    use_empty: bool | None = False,
):
    """Open the default file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Path to an alternative start-up file
    :type filepath: str
    :param load_ui: Load UI, Load user interface setup from the .blend file
    :type load_ui: bool | None
    :param use_splash: Splash
    :type use_splash: bool | None
    :param use_factory_startup: Factory Startup, Load the default ('factory startup') blend file. This is independent of the normal start-up file that the user can save
    :type use_factory_startup: bool | None
    :param use_factory_startup_app_template_only: Factory Startup App-Template Only
    :type use_factory_startup_app_template_only: bool | None
    :type app_template: str
    :param use_empty: Empty, After loading, remove everything except scenes, windows, and workspaces. This makes it possible to load the startup file with its scene configuration and window layout intact, but no objects, materials, animations, ...
    :type use_empty: bool | None
    """

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

def recover_auto_save(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = True,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = False,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "LIST_VERTICAL",
    sort_method: str | None = "",
    use_scripts: bool | None = True,
):
    """Open an automatically saved file to recover it

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
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
        :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
        :type use_scripts: bool | None
    """

def recover_last_session(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_scripts: bool | None = True,
):
    """Open the last closed file ("quit.blend")

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: bool | None
    """

def redraw_timer(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: typing.Literal[
        "DRAW",
        "DRAW_SWAP",
        "DRAW_WIN",
        "DRAW_WIN_SWAP",
        "ANIM_STEP",
        "ANIM_PLAY",
        "UNDO",
    ]
    | None = "DRAW",
    iterations: int | None = 10,
    time_limit: float | None = 0.0,
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
        :type type: typing.Literal['DRAW','DRAW_SWAP','DRAW_WIN','DRAW_WIN_SWAP','ANIM_STEP','ANIM_PLAY','UNDO'] | None
        :param iterations: Iterations, Number of times to redraw
        :type iterations: int | None
        :param time_limit: Time Limit, Seconds to run the test for (override iterations)
        :type time_limit: float | None
    """

def revert_mainfile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_scripts: bool | None = True,
):
    """Reload the saved file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: bool | None
    """

def save_as_mainfile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = True,
    filter_blender: bool | None = True,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    compress: bool | None = False,
    relative_remap: bool | None = True,
    copy: bool | None = False,
):
    """Save the current file in the desired location

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
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
        :param compress: Compress, Write compressed .blend file
        :type compress: bool | None
        :param relative_remap: Remap Relative, Remap relative paths when saving to a different directory
        :type relative_remap: bool | None
        :param copy: Save Copy, Save a copy of the actual working state but does not make saved file active
        :type copy: bool | None
    """

def save_homefile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Make the current file the default startup file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def save_mainfile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = True,
    filter_blender: bool | None = True,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    compress: bool | None = False,
    relative_remap: bool | None = False,
    exit: bool | None = False,
    incremental: bool | None = False,
):
    """Save the current Blender file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
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
        :param compress: Compress, Write compressed .blend file
        :type compress: bool | None
        :param relative_remap: Remap Relative, Remap relative paths when saving to a different directory
        :type relative_remap: bool | None
        :param exit: Exit, Exit Blender after saving
        :type exit: bool | None
        :param incremental: Incremental, Save the current Blender file with a numerically incremented name that does not overwrite any existing files
        :type incremental: bool | None
    """

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

def search_single_menu(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    menu_idname: str = "",
    initial_query: str = "",
):
    """Pop-up a search for a menu in current context

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param menu_idname: Menu Name, Menu to search in
    :type menu_idname: str
    :param initial_query: Initial Query, Query to insert into the search box
    :type initial_query: str
    """

def set_stereo_3d(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    display_mode: bpy.typing.Stereo3DDisplayItems | None = "ANAGLYPH",
    anaglyph_type: bpy.typing.Stereo3DAnaglyphTypeItems | None = "RED_CYAN",
    interlace_type: bpy.typing.Stereo3DInterlaceTypeItems | None = "ROW_INTERLEAVED",
    use_interlace_swap: bool | None = False,
    use_sidebyside_crosseyed: bool | None = False,
):
    """Toggle 3D stereo support for current window (or change the display mode)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param display_mode: Display Mode
    :type display_mode: bpy.typing.Stereo3DDisplayItems | None
    :param anaglyph_type: Anaglyph Type
    :type anaglyph_type: bpy.typing.Stereo3DAnaglyphTypeItems | None
    :param interlace_type: Interlace Type
    :type interlace_type: bpy.typing.Stereo3DInterlaceTypeItems | None
    :param use_interlace_swap: Swap Left/Right, Swap left and right stereo channels
    :type use_interlace_swap: bool | None
    :param use_sidebyside_crosseyed: Cross-Eyed, Right eye should see left image and vice versa
    :type use_sidebyside_crosseyed: bool | None
    """

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

def stl_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    ascii_format: bool | None = False,
    use_batch: bool | None = False,
    export_selected_objects: bool | None = False,
    collection: str = "",
    global_scale: float | None = 1.0,
    use_scene_unit: bool | None = False,
    forward_axis: typing.Literal[
        "X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"
    ]
    | None = "Y",
    up_axis: typing.Literal["X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"]
    | None = "Z",
    apply_modifiers: bool | None = True,
    filter_glob: str = "*.stl",
):
    """Save the scene to an STL file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
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
        :param ascii_format: ASCII Format, Export file in ASCII format, export as binary otherwise
        :type ascii_format: bool | None
        :param use_batch: Batch Export, Export each object to a separate file
        :type use_batch: bool | None
        :param export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects
        :type export_selected_objects: bool | None
        :param collection: Source Collection, Export only objects from this collection (and its children)
        :type collection: str
        :param global_scale: Scale
        :type global_scale: float | None
        :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to exported data
        :type use_scene_unit: bool | None
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
        :type forward_axis: typing.Literal['X','Y','Z','NEGATIVE_X','NEGATIVE_Y','NEGATIVE_Z'] | None
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
        :type up_axis: typing.Literal['X','Y','Z','NEGATIVE_X','NEGATIVE_Y','NEGATIVE_Z'] | None
        :param apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes
        :type apply_modifiers: bool | None
        :param filter_glob: Extension Filter
        :type filter_glob: str
    """

def stl_import(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    global_scale: float | None = 1.0,
    use_scene_unit: bool | None = False,
    use_facet_normal: bool | None = False,
    forward_axis: typing.Literal[
        "X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"
    ]
    | None = "Y",
    up_axis: typing.Literal["X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"]
    | None = "Z",
    use_mesh_validate: bool | None = True,
    filter_glob: str = "*.stl",
):
    """Import an STL file as an object

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param directory: Directory, Directory of the file
        :type directory: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
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
        :param global_scale: Scale
        :type global_scale: float | None
        :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to imported data
        :type use_scene_unit: bool | None
        :param use_facet_normal: Facet Normals, Use (import) facet normals (note that this will still give flat shading)
        :type use_facet_normal: bool | None
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
        :type forward_axis: typing.Literal['X','Y','Z','NEGATIVE_X','NEGATIVE_Y','NEGATIVE_Z'] | None
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
        :type up_axis: typing.Literal['X','Y','Z','NEGATIVE_X','NEGATIVE_Y','NEGATIVE_Z'] | None
        :param use_mesh_validate: Validate Mesh, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)
        :type use_mesh_validate: bool | None
        :param filter_glob: Extension Filter
        :type filter_glob: str
    """

def sysinfo(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
):
    """Generate system information, saved into a text file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str
    """

def tool_set_by_id(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str = "",
    cycle: bool | None = False,
    as_fallback: bool | None = False,
    space_type: typing.Literal[
        "EMPTY",
        "VIEW_3D",
        "IMAGE_EDITOR",
        "NODE_EDITOR",
        "SEQUENCE_EDITOR",
        "CLIP_EDITOR",
        "DOPESHEET_EDITOR",
        "GRAPH_EDITOR",
        "NLA_EDITOR",
        "TEXT_EDITOR",
        "CONSOLE",
        "INFO",
        "TOPBAR",
        "STATUSBAR",
        "OUTLINER",
        "PROPERTIES",
        "FILE_BROWSER",
        "SPREADSHEET",
        "PREFERENCES",
    ]
    | None = "EMPTY",
):
    """Set the tool by name (for key-maps)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Identifier, Identifier of the tool
    :type name: str
    :param cycle: Cycle, Cycle through tools in this group
    :type cycle: bool | None
    :param as_fallback: Set Fallback, Set the fallback tool instead of the primary tool
    :type as_fallback: bool | None
    :param space_type: Type
    :type space_type: typing.Literal['EMPTY','VIEW_3D','IMAGE_EDITOR','NODE_EDITOR','SEQUENCE_EDITOR','CLIP_EDITOR','DOPESHEET_EDITOR','GRAPH_EDITOR','NLA_EDITOR','TEXT_EDITOR','CONSOLE','INFO','TOPBAR','STATUSBAR','OUTLINER','PROPERTIES','FILE_BROWSER','SPREADSHEET','PREFERENCES'] | None
    """

def tool_set_by_index(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    index: int | None = 0,
    cycle: bool | None = False,
    expand: bool | None = True,
    as_fallback: bool | None = False,
    space_type: typing.Literal[
        "EMPTY",
        "VIEW_3D",
        "IMAGE_EDITOR",
        "NODE_EDITOR",
        "SEQUENCE_EDITOR",
        "CLIP_EDITOR",
        "DOPESHEET_EDITOR",
        "GRAPH_EDITOR",
        "NLA_EDITOR",
        "TEXT_EDITOR",
        "CONSOLE",
        "INFO",
        "TOPBAR",
        "STATUSBAR",
        "OUTLINER",
        "PROPERTIES",
        "FILE_BROWSER",
        "SPREADSHEET",
        "PREFERENCES",
    ]
    | None = "EMPTY",
):
    """Set the tool by index (for key-maps)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: Index in Toolbar
    :type index: int | None
    :param cycle: Cycle, Cycle through tools in this group
    :type cycle: bool | None
    :param expand: expand, Include tool subgroups
    :type expand: bool | None
    :param as_fallback: Set Fallback, Set the fallback tool instead of the primary
    :type as_fallback: bool | None
    :param space_type: Type
    :type space_type: typing.Literal['EMPTY','VIEW_3D','IMAGE_EDITOR','NODE_EDITOR','SEQUENCE_EDITOR','CLIP_EDITOR','DOPESHEET_EDITOR','GRAPH_EDITOR','NLA_EDITOR','TEXT_EDITOR','CONSOLE','INFO','TOPBAR','STATUSBAR','OUTLINER','PROPERTIES','FILE_BROWSER','SPREADSHEET','PREFERENCES'] | None
    """

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

def url_open(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    url: str = "",
):
    """Open a website in the web browser

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param url: URL, URL to open
    :type url: str
    """

def url_open_preset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "",
    id: str = "",
):
    """Open a preset website in the web browser

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Site
    :type type: str | None
    :param id: Identifier, Optional identifier
    :type id: str
    """

def usd_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
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
    filter_alembic: bool | None = False,
    filter_usd: bool | None = True,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    filter_glob: str = "*.usd",
    selected_objects_only: bool | None = False,
    visible_objects_only: bool | None = True,
    collection: str = "",
    export_animation: bool | None = False,
    export_hair: bool | None = False,
    export_uvmaps: bool | None = True,
    rename_uvmaps: bool | None = True,
    export_mesh_colors: bool | None = True,
    export_normals: bool | None = True,
    export_materials: bool | None = True,
    export_subdivision: typing.Literal["IGNORE", "TESSELLATE", "BEST_MATCH"]
    | None = "BEST_MATCH",
    export_armatures: bool | None = True,
    only_deform_bones: bool | None = False,
    export_shapekeys: bool | None = True,
    use_instancing: bool | None = False,
    evaluation_mode: typing.Literal["RENDER", "VIEWPORT"] | None = "RENDER",
    generate_preview_surface: bool | None = True,
    generate_materialx_network: bool | None = False,
    convert_orientation: bool | None = False,
    export_global_forward_selection: typing.Literal[
        "X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"
    ]
    | None = "NEGATIVE_Z",
    export_global_up_selection: typing.Literal[
        "X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"
    ]
    | None = "Y",
    export_textures: bool | None = True,
    overwrite_textures: bool | None = False,
    relative_paths: bool | None = True,
    xform_op_mode: typing.Literal["TRS", "TOS", "MAT"] | None = "TRS",
    root_prim_path: str = "/root",
    export_custom_properties: bool | None = True,
    custom_properties_namespace: str = "userProperties",
    author_blender_name: bool | None = True,
    convert_world_material: bool | None = True,
    allow_unicode: bool | None = False,
    export_meshes: bool | None = True,
    export_lights: bool | None = True,
    export_cameras: bool | None = True,
    export_curves: bool | None = True,
    export_volumes: bool | None = True,
    triangulate_meshes: bool | None = False,
    quad_method: bpy.typing.ModifierTriangulateQuadMethodItems
    | None = "SHORTEST_DIAGONAL",
    ngon_method: bpy.typing.ModifierTriangulateNgonMethodItems | None = "BEAUTY",
    usdz_downscale_size: typing.Literal[
        "KEEP", "256", "512", "1024", "2048", "4096", "CUSTOM"
    ]
    | None = "KEEP",
    usdz_downscale_custom_size: int | None = 128,
):
    """Export current scene in a USD archive

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
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
        :type filter_glob: str
        :param selected_objects_only: Selection Only, Only export selected objects. Unselected parents of selected objects are exported as empty transform
        :type selected_objects_only: bool | None
        :param visible_objects_only: Visible Only, Only export visible objects. Invisible parents of exported objects are exported as empty transforms
        :type visible_objects_only: bool | None
        :param collection: Collection
        :type collection: str
        :param export_animation: Animation, Export all frames in the render frame range, rather than only the current frame
        :type export_animation: bool | None
        :param export_hair: Hair, Export hair particle systems as USD curves
        :type export_hair: bool | None
        :param export_uvmaps: UV Maps, Include all mesh UV maps in the export
        :type export_uvmaps: bool | None
        :param rename_uvmaps: Rename UV Maps, Rename active render UV map to "st" to match USD conventions
        :type rename_uvmaps: bool | None
        :param export_mesh_colors: Color Attributes, Include mesh color attributes in the export
        :type export_mesh_colors: bool | None
        :param export_normals: Normals, Include normals of exported meshes in the export
        :type export_normals: bool | None
        :param export_materials: Materials, Export viewport settings of materials as USD preview materials, and export material assignments as geometry subsets
        :type export_materials: bool | None
        :param export_subdivision: Subdivision, Choose how subdivision modifiers will be mapped to the USD subdivision scheme during export

    IGNORE
    Ignore -- Scheme = None. Export base mesh without subdivision.

    TESSELLATE
    Tessellate -- Scheme = None. Export subdivided mesh.

    BEST_MATCH
    Best Match -- Scheme = Catmull-Clark, when possible. Reverts to exporting the subdivided mesh for the Simple subdivision type.
        :type export_subdivision: typing.Literal['IGNORE','TESSELLATE','BEST_MATCH'] | None
        :param export_armatures: Armatures, Export armatures and meshes with armature modifiers as USD skeletons and skinned meshes
        :type export_armatures: bool | None
        :param only_deform_bones: Only Deform Bones, Only export deform bones and their parents
        :type only_deform_bones: bool | None
        :param export_shapekeys: Shape Keys, Export shape keys as USD blend shapes
        :type export_shapekeys: bool | None
        :param use_instancing: Instancing, Export instanced objects as references in USD rather than real objects
        :type use_instancing: bool | None
        :param evaluation_mode: Use Settings for, Determines visibility of objects, modifier settings, and other areas where there are different settings for viewport and rendering

    RENDER
    Render -- Use Render settings for object visibility, modifier settings, etc.

    VIEWPORT
    Viewport -- Use Viewport settings for object visibility, modifier settings, etc.
        :type evaluation_mode: typing.Literal['RENDER','VIEWPORT'] | None
        :param generate_preview_surface: USD Preview Surface Network, Generate an approximate USD Preview Surface shader representation of a Principled BSDF node network
        :type generate_preview_surface: bool | None
        :param generate_materialx_network: MaterialX Network, Generate a MaterialX network representation of the materials
        :type generate_materialx_network: bool | None
        :param convert_orientation: Convert Orientation, Convert orientation axis to a different convention to match other applications
        :type convert_orientation: bool | None
        :param export_global_forward_selection: Forward Axis

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
        :type export_global_forward_selection: typing.Literal['X','Y','Z','NEGATIVE_X','NEGATIVE_Y','NEGATIVE_Z'] | None
        :param export_global_up_selection: Up Axis

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
        :type export_global_up_selection: typing.Literal['X','Y','Z','NEGATIVE_X','NEGATIVE_Y','NEGATIVE_Z'] | None
        :param export_textures: Export Textures, If exporting materials, export textures referenced by material nodes to a 'textures' directory in the same directory as the USD file
        :type export_textures: bool | None
        :param overwrite_textures: Overwrite Textures, Overwrite existing files when exporting textures
        :type overwrite_textures: bool | None
        :param relative_paths: Relative Paths, Use relative paths to reference external files (i.e. textures, volumes) in USD, otherwise use absolute paths
        :type relative_paths: bool | None
        :param xform_op_mode: Xform Ops, The type of transform operators to write

    TRS
    Translate, Rotate, Scale -- Export with translate, rotate, and scale Xform operators.

    TOS
    Translate, Orient, Scale -- Export with translate, orient quaternion, and scale Xform operators.

    MAT
    Matrix -- Export matrix operator.
        :type xform_op_mode: typing.Literal['TRS','TOS','MAT'] | None
        :param root_prim_path: Root Prim, If set, add a transform primitive with the given path to the stage as the parent of all exported data
        :type root_prim_path: str
        :param export_custom_properties: Custom Properties, Export custom properties as USD attributes
        :type export_custom_properties: bool | None
        :param custom_properties_namespace: Namespace, If set, add the given namespace as a prefix to exported custom property names. This only applies to property names that do not already have a prefix (e.g., it would apply to name 'bar' but not 'foo:bar') and does not apply to blender object and data names which are always exported in the 'userProperties:blender' namespace
        :type custom_properties_namespace: str
        :param author_blender_name: Blender Names, Author USD custom attributes containing the original Blender object and object data names
        :type author_blender_name: bool | None
        :param convert_world_material: Convert World Material, Convert the world material to a USD dome light. Currently works for simple materials, consisting of an environment texture connected to a background shader, with an optional vector multiply of the texture color
        :type convert_world_material: bool | None
        :param allow_unicode: Allow Unicode, Preserve UTF-8 encoded characters when writing USD prim and property names (requires software utilizing USD 24.03 or greater when opening the resulting files)
        :type allow_unicode: bool | None
        :param export_meshes: Meshes, Export all meshes
        :type export_meshes: bool | None
        :param export_lights: Lights, Export all lights
        :type export_lights: bool | None
        :param export_cameras: Cameras, Export all cameras
        :type export_cameras: bool | None
        :param export_curves: Curves, Export all curves
        :type export_curves: bool | None
        :param export_volumes: Volumes, Export all volumes
        :type export_volumes: bool | None
        :param triangulate_meshes: Triangulate Meshes, Triangulate meshes during export
        :type triangulate_meshes: bool | None
        :param quad_method: Quad Method, Method for splitting the quads into triangles
        :type quad_method: bpy.typing.ModifierTriangulateQuadMethodItems | None
        :param ngon_method: N-gon Method, Method for splitting the n-gons into triangles
        :type ngon_method: bpy.typing.ModifierTriangulateNgonMethodItems | None
        :param usdz_downscale_size: USDZ Texture Downsampling, Choose a maximum size for all exported textures

    KEEP
    Keep -- Keep all current texture sizes.

    256
    256 -- Resize to a maximum of 256 pixels.

    512
    512 -- Resize to a maximum of 512 pixels.

    1024
    1024 -- Resize to a maximum of 1024 pixels.

    2048
    2048 -- Resize to a maximum of 2048 pixels.

    4096
    4096 -- Resize to a maximum of 4096 pixels.

    CUSTOM
    Custom -- Specify a custom size.
        :type usdz_downscale_size: typing.Literal['KEEP','256','512','1024','2048','4096','CUSTOM'] | None
        :param usdz_downscale_custom_size: USDZ Custom Downscale Size, Custom size for downscaling exported textures
        :type usdz_downscale_custom_size: int | None
    """

def usd_import(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
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
    filter_alembic: bool | None = False,
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
    filter_glob: str = "*.usd",
    scale: float | None = 1.0,
    set_frame_range: bool | None = True,
    import_cameras: bool | None = True,
    import_curves: bool | None = True,
    import_lights: bool | None = True,
    import_materials: bool | None = True,
    import_meshes: bool | None = True,
    import_volumes: bool | None = True,
    import_shapes: bool | None = True,
    import_skeletons: bool | None = True,
    import_blendshapes: bool | None = True,
    import_points: bool | None = True,
    import_subdiv: bool | None = False,
    support_scene_instancing: bool | None = True,
    import_visible_only: bool | None = True,
    create_collection: bool | None = False,
    read_mesh_uvs: bool | None = True,
    read_mesh_colors: bool | None = True,
    read_mesh_attributes: bool | None = True,
    prim_path_mask: str = "",
    import_guide: bool | None = False,
    import_proxy: bool | None = False,
    import_render: bool | None = True,
    import_all_materials: bool | None = False,
    import_usd_preview: bool | None = True,
    set_material_blend: bool | None = True,
    light_intensity_scale: float | None = 1.0,
    mtl_name_collision_mode: typing.Literal["MAKE_UNIQUE", "REFERENCE_EXISTING"]
    | None = "MAKE_UNIQUE",
    import_textures_mode: typing.Literal["IMPORT_NONE", "IMPORT_PACK", "IMPORT_COPY"]
    | None = "IMPORT_PACK",
    import_textures_dir: str = "//textures/",
    tex_name_collision_mode: typing.Literal["USE_EXISTING", "OVERWRITE"]
    | None = "USE_EXISTING",
    attr_import_mode: typing.Literal["NONE", "USER", "ALL"] | None = "ALL",
    validate_meshes: bool | None = False,
    create_world_material: bool | None = True,
    import_defined_only: bool | None = True,
):
    """Import USD stage into current scene

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
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
        :type filter_glob: str
        :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
        :type scale: float | None
        :param set_frame_range: Set Frame Range, Update the scene's start and end frame to match those of the USD archive
        :type set_frame_range: bool | None
        :param import_cameras: Cameras
        :type import_cameras: bool | None
        :param import_curves: Curves
        :type import_curves: bool | None
        :param import_lights: Lights
        :type import_lights: bool | None
        :param import_materials: Materials
        :type import_materials: bool | None
        :param import_meshes: Meshes
        :type import_meshes: bool | None
        :param import_volumes: Volumes
        :type import_volumes: bool | None
        :param import_shapes: USD Shapes
        :type import_shapes: bool | None
        :param import_skeletons: Armatures
        :type import_skeletons: bool | None
        :param import_blendshapes: Shape Keys
        :type import_blendshapes: bool | None
        :param import_points: Point Clouds
        :type import_points: bool | None
        :param import_subdiv: Import Subdivision Scheme, Create subdivision surface modifiers based on the USD SubdivisionScheme attribute
        :type import_subdiv: bool | None
        :param support_scene_instancing: Scene Instancing, Import USD scene graph instances as collection instances
        :type support_scene_instancing: bool | None
        :param import_visible_only: Visible Primitives Only, Do not import invisible USD primitives. Only applies to primitives with a non-animated visibility attribute. Primitives with animated visibility will always be imported
        :type import_visible_only: bool | None
        :param create_collection: Create Collection, Add all imported objects to a new collection
        :type create_collection: bool | None
        :param read_mesh_uvs: UV Coordinates, Read mesh UV coordinates
        :type read_mesh_uvs: bool | None
        :param read_mesh_colors: Color Attributes, Read mesh color attributes
        :type read_mesh_colors: bool | None
        :param read_mesh_attributes: Mesh Attributes, Read USD Primvars as mesh attributes
        :type read_mesh_attributes: bool | None
        :param prim_path_mask: Path Mask, Import only the primitive at the given path and its descendants. Multiple paths may be specified in a list delimited by commas or semicolons
        :type prim_path_mask: str
        :param import_guide: Guide, Import guide geometry
        :type import_guide: bool | None
        :param import_proxy: Proxy, Import proxy geometry
        :type import_proxy: bool | None
        :param import_render: Render, Import final render geometry
        :type import_render: bool | None
        :param import_all_materials: Import All Materials, Also import materials that are not used by any geometry. Note that when this option is false, materials referenced by geometry will still be imported
        :type import_all_materials: bool | None
        :param import_usd_preview: Import USD Preview, Convert UsdPreviewSurface shaders to Principled BSDF shader networks
        :type import_usd_preview: bool | None
        :param set_material_blend: Set Material Blend, If the Import USD Preview option is enabled, the material blend method will automatically be set based on the shader's opacity and opacityThreshold inputs
        :type set_material_blend: bool | None
        :param light_intensity_scale: Light Intensity Scale, Scale for the intensity of imported lights
        :type light_intensity_scale: float | None
        :param mtl_name_collision_mode: Material Name Collision, Behavior when the name of an imported material conflicts with an existing material

    MAKE_UNIQUE
    Make Unique -- Import each USD material as a unique Blender material.

    REFERENCE_EXISTING
    Reference Existing -- If a material with the same name already exists, reference that instead of importing.
        :type mtl_name_collision_mode: typing.Literal['MAKE_UNIQUE','REFERENCE_EXISTING'] | None
        :param import_textures_mode: Import Textures, Behavior when importing textures from a USDZ archive

    IMPORT_NONE
    None -- Don't import textures.

    IMPORT_PACK
    Packed -- Import textures as packed data.

    IMPORT_COPY
    Copy -- Copy files to textures directory.
        :type import_textures_mode: typing.Literal['IMPORT_NONE','IMPORT_PACK','IMPORT_COPY'] | None
        :param import_textures_dir: Textures Directory, Path to the directory where imported textures will be copied
        :type import_textures_dir: str
        :param tex_name_collision_mode: File Name Collision, Behavior when the name of an imported texture file conflicts with an existing file

    USE_EXISTING
    Use Existing -- If a file with the same name already exists, use that instead of copying.

    OVERWRITE
    Overwrite -- Overwrite existing files.
        :type tex_name_collision_mode: typing.Literal['USE_EXISTING','OVERWRITE'] | None
        :param attr_import_mode: Custom Properties, Behavior when importing USD attributes as Blender custom properties

    NONE
    None -- Do not import USD custom attributes.

    USER
    User -- Import USD attributes in the 'userProperties' namespace as Blender custom properties. The namespace will be stripped from the property names.

    ALL
    All Custom -- Import all USD custom attributes as Blender custom properties. Namespaces will be retained in the property names.
        :type attr_import_mode: typing.Literal['NONE','USER','ALL'] | None
        :param validate_meshes: Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)
        :type validate_meshes: bool | None
        :param create_world_material: Create World Material, Convert the first discovered USD dome light to a world background shader
        :type create_world_material: bool | None
        :param import_defined_only: Defined Primitives Only, Import only defined USD primitives. When disabled this allows importing USD primitives which are not defined, such as those with an override specifier
        :type import_defined_only: bool | None
    """

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

def xr_navigation_fly(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: typing.Literal[
        "FORWARD",
        "BACK",
        "LEFT",
        "RIGHT",
        "UP",
        "DOWN",
        "TURNLEFT",
        "TURNRIGHT",
        "VIEWER_FORWARD",
        "VIEWER_BACK",
        "VIEWER_LEFT",
        "VIEWER_RIGHT",
        "CONTROLLER_FORWARD",
    ]
    | None = "VIEWER_FORWARD",
    lock_location_z: bool | None = False,
    lock_direction: bool | None = False,
    speed_frame_based: bool | None = True,
    speed_min: float | None = 0.018,
    speed_max: float | None = 0.054,
    speed_interpolation0: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
    ),
    speed_interpolation1: collections.abc.Sequence[float] | mathutils.Vector | None = (
        1.0,
        1.0,
    ),
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
        :type mode: typing.Literal['FORWARD','BACK','LEFT','RIGHT','UP','DOWN','TURNLEFT','TURNRIGHT','VIEWER_FORWARD','VIEWER_BACK','VIEWER_LEFT','VIEWER_RIGHT','CONTROLLER_FORWARD'] | None
        :param lock_location_z: Lock Elevation, Prevent changes to viewer elevation
        :type lock_location_z: bool | None
        :param lock_direction: Lock Direction, Limit movement to viewer's initial direction
        :type lock_direction: bool | None
        :param speed_frame_based: Frame Based Speed, Apply fixed movement deltas every update
        :type speed_frame_based: bool | None
        :param speed_min: Minimum Speed, Minimum move (turn) speed in meters (radians) per second or frame
        :type speed_min: float | None
        :param speed_max: Maximum Speed, Maximum move (turn) speed in meters (radians) per second or frame
        :type speed_max: float | None
        :param speed_interpolation0: Speed Interpolation 0, First cubic spline control point between min/max speeds
        :type speed_interpolation0: collections.abc.Sequence[float] | mathutils.Vector | None
        :param speed_interpolation1: Speed Interpolation 1, Second cubic spline control point between min/max speeds
        :type speed_interpolation1: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def xr_navigation_grab(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    lock_location: bool | None = False,
    lock_location_z: bool | None = False,
    lock_rotation: bool | None = False,
    lock_rotation_z: bool | None = False,
    lock_scale: bool | None = False,
):
    """Navigate the VR scene by grabbing with controllers

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param lock_location: Lock Location, Prevent changes to viewer location
    :type lock_location: bool | None
    :param lock_location_z: Lock Elevation, Prevent changes to viewer elevation
    :type lock_location_z: bool | None
    :param lock_rotation: Lock Rotation, Prevent changes to viewer rotation
    :type lock_rotation: bool | None
    :param lock_rotation_z: Lock Up Orientation, Prevent changes to viewer up orientation
    :type lock_rotation_z: bool | None
    :param lock_scale: Lock Scale, Prevent changes to viewer scale
    :type lock_scale: bool | None
    """

def xr_navigation_reset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    location: bool | None = True,
    rotation: bool | None = True,
    scale: bool | None = True,
):
    """Reset VR navigation deltas relative to session base pose

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Reset location deltas
    :type location: bool | None
    :param rotation: Rotation, Reset rotation deltas
    :type rotation: bool | None
    :param scale: Scale, Reset scale deltas
    :type scale: bool | None
    """

def xr_navigation_teleport(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    teleport_axes: collections.abc.Iterable[bool] | None = (True, True, True),
    interpolation: float | None = 1.0,
    offset: float | None = 0.0,
    selectable_only: bool | None = True,
    distance: float | None = 1.70141e38,
    from_viewer: bool | None = False,
    axis: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, -1.0),
    color: collections.abc.Iterable[float] | None = (0.35, 0.35, 1.0, 1.0),
):
    """Set VR viewer location to controller raycast hit location

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param teleport_axes: Teleport Axes, Enabled teleport axes in navigation space
    :type teleport_axes: collections.abc.Iterable[bool] | None
    :param interpolation: Interpolation, Interpolation factor between viewer and hit locations
    :type interpolation: float | None
    :param offset: Offset, Offset along hit normal to subtract from final location
    :type offset: float | None
    :param selectable_only: Selectable Only, Only allow selectable objects to influence raycast result
    :type selectable_only: bool | None
    :param distance: Maximum raycast distance
    :type distance: float | None
    :param from_viewer: From Viewer, Use viewer pose as raycast origin
    :type from_viewer: bool | None
    :param axis: Axis, Raycast axis in controller/viewer space
    :type axis: collections.abc.Sequence[float] | mathutils.Vector | None
    :param color: Color, Raycast color
    :type color: collections.abc.Iterable[float] | None
    """

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
