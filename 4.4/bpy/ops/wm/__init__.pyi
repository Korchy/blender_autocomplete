import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bl_operators.wm
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

def alembic_export(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
    quad_method: bpy.stub_internal.rna_enums.ModifierTriangulateQuadMethodItems
    | None = "SHORTEST_DIAGONAL",
    ngon_method: bpy.stub_internal.rna_enums.ModifierTriangulateNgonMethodItems
    | None = "BEAUTY",
    export_hair: bool | None = True,
    export_particles: bool | None = True,
    export_custom_properties: bool | None = True,
    as_background_job: bool | None = False,
    evaluation_mode: typing.Literal["RENDER", "VIEWPORT"] | None = "RENDER",
    init_scene_frame_range: bool | None = True,
) -> None:
    """Export current scene in an Alembic archive

        :param filepath: File Path, Path to file
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
        :param filter_collada: Filter COLLADA files
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
        :param start: Start Frame, Start frame of the export, use the default value to take the start frame of the current scene
        :param end: End Frame, End frame of the export, use the default value to take the end frame of the current scene
        :param xsamples: Transform Samples, Number of times per frame transformations are sampled
        :param gsamples: Geometry Samples, Number of times per frame object data are sampled
        :param sh_open: Shutter Open, Time at which the shutter is open
        :param sh_close: Shutter Close, Time at which the shutter is closed
        :param selected: Selected Objects Only, Export only selected objects
        :param visible_objects_only: Visible Objects Only, Export only objects that are visible
        :param flatten: Flatten Hierarchy, Do not preserve objects parent/children relationship
        :param collection: Collection
        :param uvs: UV Coordinates, Export UV coordinates
        :param packuv: Merge UVs
        :param normals: Normals, Export normals
        :param vcolors: Color Attributes, Export color attributes
        :param orcos: Generated Coordinates, Export undeformed mesh vertex coordinates
        :param face_sets: Face Sets, Export per face shading group assignments
        :param subdiv_schema: Use Subdivision Schema, Export meshes using Alembics subdivision schema
        :param apply_subdiv: Apply Subdivision Surface, Export subdivision surfaces as meshes
        :param curves_as_mesh: Curves as Mesh, Export curves and NURBS surfaces as meshes
        :param use_instancing: Use Instancing, Export data of duplicated objects as Alembic instances; speeds up the export and can be disabled for compatibility with other software
        :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the worlds origin
        :param triangulate: Triangulate, Export polygons (quads and n-gons) as triangles
        :param quad_method: Quad Method, Method for splitting the quads into triangles
        :param ngon_method: N-gon Method, Method for splitting the n-gons into triangles
        :param export_hair: Export Hair, Exports hair particle systems as animated curves
        :param export_particles: Export Particles, Exports non-hair particle systems
        :param export_custom_properties: Export Custom Properties, Export custom properties to Alembic .userProperties
        :param as_background_job: Run as Background Job, Enable this to run the import in the background, disable to block Blender while importing. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job
        :param evaluation_mode: Settings, Determines visibility of objects, modifier settings, and other areas where there are different settings for viewport and rendering

    RENDER
    Render -- Use Render settings for object visibility, modifier settings, etc.

    VIEWPORT
    Viewport -- Use Viewport settings for object visibility, modifier settings, etc.
    """

def alembic_import(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Load an Alembic archive

        :param filepath: File Path, Path to file
        :param directory: Directory, Directory of the file
        :param files: Files
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
        :param filter_collada: Filter COLLADA files
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
        :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the worlds origin
        :param set_frame_range: Set Frame Range, If checked, update scenes start and end frame to match those of the Alembic archive
        :param validate_meshes: Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)
        :param always_add_cache_reader: Always Add Cache Reader, Add cache modifiers and constraints to imported objects even if they are not animated so that they can be updated when reloading the Alembic archive
        :param is_sequence: Is Sequence, Set to true if the cache is split into separate files
        :param as_background_job: Run as Background Job, Enable this to run the export in the background, disable to block Blender while exporting. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job
    """

def append(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Append from a Library .blend file

        :param filepath: File Path, Path to file
        :param directory: Directory, Directory of the file
        :param filename: File Name, Name of the file
        :param files: Files
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
        :param filter_collada: Filter COLLADA files
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
        :param link: Link, Link the objects or data-blocks rather than appending
        :param do_reuse_local_id: Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy
        :param clear_asset_data: Clear Asset Data, Dont add asset meta-data or tags from the original data-block
        :param autoselect: Select, Select new objects
        :param active_collection: Active Collection, Put new objects on the active collection
        :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
        :param instance_object_data: Instance Object Data, Create instances for object data which are not referenced by any objects
        :param set_fake: Fake User, Set "Fake User" for appended items (except objects and collections)
        :param use_recursive: Localize All, Localize all appended data, including those indirectly linked from other libraries
    """

def batch_rename(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Rename multiple items at once

    :param data_type: Type, Type of data to rename
    :param data_source: Source
    :param actions: actions
    """

def blend_strings_utf8_validate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Check and fix all strings in current .blend file to be valid UTF-8 Unicode (needed for some old, 2.4x area files)"""

def call_asset_shelf_popover(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
) -> None:
    """Open a predefined asset shelf in a popup

    :param name: Asset Shelf Name, Identifier of the asset shelf to display
    """

def call_menu(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
) -> None:
    """Open a predefined menu

    :param name: Name, Name of the menu
    """

def call_menu_pie(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
) -> None:
    """Open a predefined pie menu

    :param name: Name, Name of the pie menu
    """

def call_panel(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    keep_open: bool | None = True,
) -> None:
    """Open a predefined panel

    :param name: Name, Name of the menu
    :param keep_open: Keep Open
    """

def clear_recent_files(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    remove: typing.Literal["ALL", "MISSING"] | None = "ALL",
) -> None:
    """Clear the recent files list

    :param remove: Remove
    """

def collada_export(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Save a Collada file

        :param filepath: File Path, Path to file
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
        :param filter_collada: Filter COLLADA files
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
        :param apply_modifiers: Apply Modifiers, Apply modifiers to exported mesh (non destructive)
        :param export_mesh_type: Resolution, Modifier resolution for export
        :param export_mesh_type_selection: Resolution, Modifier resolution for export

    view
    Viewport -- Apply modifiers viewport settings.

    render
    Render -- Apply modifiers render settings.
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
        :param apply_global_orientation: Apply Global Orientation, Rotate all root objects to match the global orientation settings otherwise set the global orientation per Collada asset
        :param selected: Selection Only, Export only selected elements
        :param include_children: Include Children, Export all children of selected objects (even if not selected)
        :param include_armatures: Include Armatures, Export related armatures (even if not selected)
        :param include_shapekeys: Include Shape Keys, Export all Shape Keys from Mesh Objects
        :param deform_bones_only: Deform Bones Only, Only export deforming bones with armatures
        :param include_animations: Include Animations, Export animations if available (exporting animations will enforce the decomposition of node transforms into <translation> <rotation> and <scale> components)
        :param include_all_actions: Include all Actions, Export also unassigned actions (this allows you to export entire animation libraries for your character(s))
        :param export_animation_type_selection: Key Type, Type for exported animations (use sample keys or Curve keys)

    sample
    Samples -- Export Sampled points guided by sampling rate.

    keys
    Curves -- Export Curves (note: guided by curve keys).
        :param sampling_rate: Sampling Rate, The distance between 2 keyframes (1 to key every frame)
        :param keep_smooth_curves: Keep Smooth curves, Export also the curve handles (if available) (this does only work when the inverse parent matrix is the unity matrix, otherwise you may end up with odd results)
        :param keep_keyframes: Keep Keyframes, Use existing keyframes as additional sample points (this helps when you want to keep manual tweaks)
        :param keep_flat_curves: All Keyed Curves, Export also curves which have only one key or are totally flat
        :param active_uv_only: Only Selected UV Map, Export only the selected UV Map
        :param use_texture_copies: Copy, Copy textures to same folder where the .dae file is exported
        :param triangulate: Triangulate, Export polygons (quads and n-gons) as triangles
        :param use_object_instantiation: Use Object Instances, Instantiate multiple Objects from same Data
        :param use_blender_profile: Use Blender Profile, Export additional Blender specific information (for material, shaders, bones, etc.)
        :param sort_by_name: Sort by Object name, Sort exported data by Object name
        :param export_object_transformation_type: Transform, Object Transformation type for translation, scale and rotation
        :param export_object_transformation_type_selection: Transform, Object Transformation type for translation, scale and rotation

    matrix
    Matrix -- Use <matrix> representation for exported transformations.

    decomposed
    Decomposed -- Use <rotate>, <translate> and <scale> representation for exported transformations.
        :param export_animation_transformation_type: Transform, Transformation type for translation, scale and rotation. Note: The Animation transformation type in the Anim Tab is always equal to the Object transformation type in the Geom tab
        :param export_animation_transformation_type_selection: Transform, Transformation type for translation, scale and rotation. Note: The Animation transformation type in the Anim Tab is always equal to the Object transformation type in the Geom tab

    matrix
    Matrix -- Use <matrix> representation for exported transformations.

    decomposed
    Decomposed -- Use <rotate>, <translate> and <scale> representation for exported transformations.
        :param open_sim: Export to SL/OpenSim, Compatibility mode for Second Life, OpenSimulator and other compatible online worlds
        :param limit_precision: Limit Precision, Reduce the precision of the exported data to 6 digits
        :param keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export
    """

def collada_import(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Load a Collada file

        :param filepath: File Path, Path to file
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
        :param filter_collada: Filter COLLADA files
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
        :param import_units: Import Units, If disabled match import to Blenders current Unit settings, otherwise use the settings from the Imported scene
        :param custom_normals: Custom Normals, Import custom normals, if available (otherwise Blender will compute them)
        :param fix_orientation: Fix Leaf Bones, Fix Orientation of Leaf Bones (Collada does only support Joints)
        :param find_chains: Find Bone Chains, Find best matching Bone Chains and ensure bones in chain are connected
        :param auto_connect: Auto Connect, Set use_connect for parent bones which have exactly one child bone
        :param min_chain_length: Minimum Chain Length, When searching Bone Chains disregard chains of length below this value
        :param keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export
    """

def collection_export_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Invoke all configured exporters for all collections"""

def context_collection_boolean_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path_iter: str = "",
    data_path_item: str = "",
    type: typing.Literal["TOGGLE", "ENABLE", "DISABLE"] | None = "TOGGLE",
) -> None:
    """Set boolean values for a collection of items

    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float)
    :param type: Type
    """

def context_cycle_array(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    reverse: bool | None = False,
) -> None:
    """Set a context array value (useful for cycling the active mesh edit mode)

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :param reverse: Reverse, Cycle backwards
    """

def context_cycle_enum(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    reverse: bool | None = False,
    wrap: bool | None = False,
) -> None:
    """Toggle a context value

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :param reverse: Reverse, Cycle backwards
    :param wrap: Wrap, Wrap back to the first/last values
    """

def context_cycle_int(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    reverse: bool | None = False,
    wrap: bool | None = False,
) -> None:
    """Set a context value (useful for cycling active material, shape keys, groups, etc.)

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :param reverse: Reverse, Cycle backwards
    :param wrap: Wrap, Wrap back to the first/last values
    """

def context_menu_enum(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
) -> None:
    """Undocumented, consider contributing.

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    """

def context_modal_mouse(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path_iter: str = "",
    data_path_item: str = "",
    header_text: str = "",
    input_scale: float | None = 0.01,
    invert: bool | None = False,
    initial_x: int | None = 0,
) -> None:
    """Adjust arbitrary values with mouse input

    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float)
    :param header_text: Header Text, Text to display in header during scale
    :param input_scale: input_scale, Scale the mouse movement by this value before applying the delta
    :param invert: invert, Invert the mouse input
    :param initial_x: initial_x
    """

def context_pie_enum(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
) -> None:
    """Undocumented, consider contributing.

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    """

def context_scale_float(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    value: float | None = 1.0,
) -> None:
    """Scale a float context value

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :param value: Value, Assign value
    """

def context_scale_int(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    value: float | None = 1.0,
    always_step: bool | None = True,
) -> None:
    """Scale an int context value

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :param value: Value, Assign value
    :param always_step: Always Step, Always adjust the value by a minimum of 1 when value is not 1.0
    """

def context_set_boolean(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    value: bool | None = True,
) -> None:
    """Set a context value

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :param value: Value, Assignment value
    """

def context_set_enum(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    value: str = "",
) -> None:
    """Set a context value

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :param value: Value, Assignment value (as a string)
    """

def context_set_float(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    value: float | None = 0.0,
    relative: bool | None = False,
) -> None:
    """Set a context value

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :param value: Value, Assignment value
    :param relative: Relative, Apply relative to the current value (delta)
    """

def context_set_id(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    value: str = "",
) -> None:
    """Set a context value to an ID data-block

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :param value: Value, Assign value
    """

def context_set_int(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    value: int | None = 0,
    relative: bool | None = False,
) -> None:
    """Set a context value

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :param value: Value, Assign value
    :param relative: Relative, Apply relative to the current value (delta)
    """

def context_set_string(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    value: str = "",
) -> None:
    """Set a context value

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :param value: Value, Assign value
    """

def context_set_value(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    value: str = "",
) -> None:
    """Set a context value

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :param value: Value, Assignment value (as a string)
    """

def context_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    module: str = "",
) -> None:
    """Toggle a context value

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :param module: Module, Optionally override the context with a module
    """

def context_toggle_enum(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    value_1: str = "",
    value_2: str = "",
) -> None:
    """Toggle a context value

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :param value_1: Value, Toggle enum
    :param value_2: Value, Toggle enum
    """

def debug_menu(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    debug_value: int | None = 0,
) -> None:
    """Open a popup to set the debug level

    :param debug_value: Debug Value
    """

def doc_view(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    doc_id: str = "",
) -> None:
    """Open online reference docs in a web browser

    :param doc_id: Doc ID
    """

def doc_view_manual(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    doc_id: str = "",
) -> None:
    """Load online manual

    :param doc_id: Doc ID
    """

def doc_view_manual_ui_context(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """View a context based online manual in a web browser"""

def drop_blend_file(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
) -> None:
    """Undocumented, consider contributing.

    :param filepath: filepath
    """

def drop_import_file(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
) -> None:
    """Operator that allows file handlers to receive file drops

    :param directory: Directory, Directory of the file
    :param files: Files
    """

def grease_pencil_export_pdf(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
    | None = "ACTIVE",
    stroke_sample: float | None = 0.0,
    use_uniform_width: bool | None = False,
    frame_mode: typing.Literal["ACTIVE", "SELECTED", "SCENE"] | None = "ACTIVE",
) -> None:
    """Export Grease Pencil to PDF

        :param filepath: File Path, Path to file
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
        :param filter_collada: Filter COLLADA files
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
        :param use_fill: Fill, Export strokes with fill enabled
        :param selected_object_type: Object, Which objects to include in the export

    ACTIVE
    Active -- Include only the active object.

    SELECTED
    Selected -- Include selected objects.

    VISIBLE
    Visible -- Include all visible objects.
        :param stroke_sample: Sampling, Precision of stroke sampling. Low values mean a more precise result, and zero disables sampling
        :param use_uniform_width: Uniform Width, Export strokes with uniform width
        :param frame_mode: Frames, Which frames to include in the export

    ACTIVE
    Active -- Include only active frame.

    SELECTED
    Selected -- Include selected frames.

    SCENE
    Scene -- Include all scene frames.
    """

def grease_pencil_export_svg(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
    | None = "ACTIVE",
    stroke_sample: float | None = 0.0,
    use_uniform_width: bool | None = False,
    use_clip_camera: bool | None = False,
) -> None:
    """Export Grease Pencil to SVG

        :param filepath: File Path, Path to file
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
        :param filter_collada: Filter COLLADA files
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
        :param use_fill: Fill, Export strokes with fill enabled
        :param selected_object_type: Object, Which objects to include in the export

    ACTIVE
    Active -- Include only the active object.

    SELECTED
    Selected -- Include selected objects.

    VISIBLE
    Visible -- Include all visible objects.
        :param stroke_sample: Sampling, Precision of stroke sampling. Low values mean a more precise result, and zero disables sampling
        :param use_uniform_width: Uniform Width, Export strokes with uniform width
        :param use_clip_camera: Clip Camera, Clip drawings to camera size when exporting in camera view
    """

def grease_pencil_import_svg(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
    use_scene_unit: bool | None = False,
) -> None:
    """Import SVG into Grease Pencil

        :param filepath: File Path, Path to file
        :param directory: Directory, Directory of the file
        :param files: Files
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
        :param filter_collada: Filter COLLADA files
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
        :param resolution: Resolution, Resolution of the generated strokes
        :param scale: Scale, Scale of the final strokes
        :param use_scene_unit: Scene Unit, Apply current scenes unit (as defined by unit scale) to imported data
    """

def interface_theme_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add a custom theme to the preset list

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def interface_theme_preset_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = True,
) -> None:
    """Remove a custom theme from the preset list

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def interface_theme_preset_save(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = True,
) -> None:
    """Save a custom theme in the preset list

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def keyconfig_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add a custom keymap configuration to the preset list

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def keyconfig_preset_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = True,
) -> None:
    """Remove a custom keymap configuration from the preset list

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def lib_reload(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Reload the given library

        :param library: Library, Library to reload
        :param filepath: File Path, Path to file
        :param directory: Directory, Directory of the file
        :param filename: File Name, Name of the file
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
        :param filter_collada: Filter COLLADA files
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

def lib_relocate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Relocate the given library to one or several others

        :param library: Library, Library to relocate
        :param filepath: File Path, Path to file
        :param directory: Directory, Directory of the file
        :param filename: File Name, Name of the file
        :param files: Files
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
        :param filter_collada: Filter COLLADA files
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

def link(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Link from a Library .blend file

        :param filepath: File Path, Path to file
        :param directory: Directory, Directory of the file
        :param filename: File Name, Name of the file
        :param files: Files
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
        :param filter_collada: Filter COLLADA files
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
        :param link: Link, Link the objects or data-blocks rather than appending
        :param do_reuse_local_id: Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy
        :param clear_asset_data: Clear Asset Data, Dont add asset meta-data or tags from the original data-block
        :param autoselect: Select, Select new objects
        :param active_collection: Active Collection, Put new objects on the active collection
        :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
        :param instance_object_data: Instance Object Data, Create instances for object data which are not referenced by any objects
    """

def memory_statistics(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Print memory statistics to the console"""

def obj_export(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Save the scene to a Wavefront OBJ file

        :param filepath: File Path, Path to file
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
        :param filter_collada: Filter COLLADA files
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
        :param export_animation: Export Animation, Export multiple frames instead of the current frame only
        :param start_frame: Start Frame, The first frame to be exported
        :param end_frame: End Frame, The last frame to be exported
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
        :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the worlds origin
        :param apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes
        :param export_eval_mode: Object Properties, Determines properties like object visibility, modifiers etc., where they differ for Render and Viewport

    DAG_EVAL_RENDER
    Render -- Export objects as they appear in render.

    DAG_EVAL_VIEWPORT
    Viewport -- Export objects as they appear in the viewport.
        :param export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects
        :param export_uv: Export UVs
        :param export_normals: Export Normals, Export per-face normals if the face is flat-shaded, per-face-per-loop normals if smooth-shaded
        :param export_colors: Export Colors, Export per-vertex colors
        :param export_materials: Export Materials, Export MTL library. There must be a Principled-BSDF node for image textures to be exported to the MTL file
        :param export_pbr_extensions: Export Materials with PBR Extensions, Export MTL library using PBR extensions (roughness, metallic, sheen, coat, anisotropy, transmission)
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
        :param export_triangulated_mesh: Export Triangulated Mesh, All ngons with four or more vertices will be triangulated. Meshes in the scene will not be affected. Behaves like Triangulate Modifier with ngon-method: "Beauty", quad-method: "Shortest Diagonal", min vertices: 4
        :param export_curves_as_nurbs: Export Curves as NURBS, Export curves in parametric form instead of exporting as mesh
        :param export_object_groups: Export Object Groups, Append mesh name to object name, separated by a _
        :param export_material_groups: Export Material Groups, Generate an OBJ group for each part of a geometry using a different material
        :param export_vertex_groups: Export Vertex Groups, Export the name of the vertex group of a face. It is approximated by choosing the vertex group with the most members among the vertices of a face
        :param export_smooth_groups: Export Smooth Groups, Every smooth-shaded face is assigned group "1" and every flat-shaded face "off"
        :param smooth_group_bitflags: Generate Bitflags for Smooth Groups
        :param filter_glob: Extension Filter
        :param collection: Collection
    """

def obj_import(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
    close_spline_loops: bool | None = True,
    collection_separator: str = "",
    filter_glob: str = "*.obj;*.mtl",
) -> None:
    """Load a Wavefront OBJ scene

        :param filepath: File Path, Path to file
        :param directory: Directory, Directory of the file
        :param files: Files
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
        :param filter_collada: Filter COLLADA files
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
        :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the worlds origin
        :param clamp_size: Clamp Bounding Box, Resize the objects to keep bounding box under this value. Value 0 disables clamping
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
        :param use_split_objects: Split By Object, Import each OBJ o as a separate object
        :param use_split_groups: Split By Group, Import each OBJ g as a separate object
        :param import_vertex_groups: Vertex Groups, Import OBJ groups as vertex groups
        :param validate_meshes: Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)
        :param close_spline_loops: Detect Cyclic Curves, Join curve endpoints if overlapping control points are detected(if disabled, no curves will be cyclic)
        :param collection_separator: Path Separator, Character used to separate objects name into hierarchical structure
        :param filter_glob: Extension Filter
    """

def open_mainfile(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Open a Blender file

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
        :param filter_collada: Filter COLLADA files
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
        :param load_ui: Load UI, Load user interface setup in the .blend file
        :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
        :param display_file_selector: Display File Selector
        :param state: State
    """

def operator_cheat_sheet(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """List all the operators in a text-block, useful for scripting"""

def operator_defaults(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set the active operator to its default values"""

def operator_pie_enum(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    prop_string: str = "",
) -> None:
    """Undocumented, consider contributing.

    :param data_path: Operator, Operator name (in Python as string)
    :param prop_string: Property, Property name (as a string)
    """

def operator_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
    operator: str = "",
) -> None:
    """Add or remove an Operator Preset

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    :param operator: Operator
    """

def operator_presets_cleanup(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    operator: str = "",
    properties: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
) -> None:
    """Remove outdated operator properties from presets that may cause problems

    :param operator: operator
    :param properties: properties
    """

def owner_disable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    owner_id: str = "",
) -> None:
    """Disable add-on for workspace

    :param owner_id: UI Tag
    """

def owner_enable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    owner_id: str = "",
) -> None:
    """Enable add-on for workspace

    :param owner_id: UI Tag
    """

def path_open(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
) -> None:
    """Open a path in a file browser

    :param filepath: filepath
    """

def ply_export(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Save the scene to a PLY file

        :param filepath: File Path, Path to file
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
        :param filter_collada: Filter COLLADA files
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
        :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the worlds origin
        :param apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes
        :param export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects
        :param collection: Source Collection, Export only objects from this collection (and its children)
        :param export_uv: Export UVs
        :param export_normals: Export Vertex Normals, Export specific vertex normals if available, export calculated normals otherwise
        :param export_colors: Export Vertex Colors, Export vertex color attributes

    NONE
    None -- Do not import/export color attributes.

    SRGB
    sRGB -- Vertex colors in the file are in sRGB color space.

    LINEAR
    Linear -- Vertex colors in the file are in linear color space.
        :param export_attributes: Export Vertex Attributes, Export custom vertex attributes
        :param export_triangulated_mesh: Export Triangulated Mesh, All ngons with four or more vertices will be triangulated. Meshes in the scene will not be affected. Behaves like Triangulate Modifier with ngon-method: "Beauty", quad-method: "Shortest Diagonal", min vertices: 4
        :param ascii_format: ASCII Format, Export file in ASCII format, export as binary otherwise
        :param filter_glob: Extension Filter
    """

def ply_import(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Import an PLY file as an object

        :param filepath: File Path, Path to file
        :param directory: Directory, Directory of the file
        :param files: Files
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
        :param filter_collada: Filter COLLADA files
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
        :param global_scale: Scale
        :param use_scene_unit: Scene Unit, Apply current scenes unit (as defined by unit scale) to imported data
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
        :param merge_verts: Merge Vertices, Merges vertices by distance
        :param import_colors: Vertex Colors, Import vertex color attributes

    NONE
    None -- Do not import/export color attributes.

    SRGB
    sRGB -- Vertex colors in the file are in sRGB color space.

    LINEAR
    Linear -- Vertex colors in the file are in linear color space.
        :param import_attributes: Vertex Attributes, Import custom vertex attributes
        :param filter_glob: Extension Filter
    """

def previews_batch_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Clear selected .blend files previews

    :param files: files
    :param directory: directory
    :param filter_blender: filter_blender
    :param filter_folder: filter_folder
    :param use_scenes: Scenes, Clear scenes previews
    :param use_collections: Collections, Clear collections previews
    :param use_objects: Objects, Clear objects previews
    :param use_intern_data: Materials & Textures, Clear internal previews (materials, textures, images, etc.)
    :param use_trusted: Trusted Blend Files, Enable Python evaluation for selected files
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with cleared previews
    """

def previews_batch_generate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Generate selected .blend files previews

    :param files: Collection of file paths with common directory root
    :param directory: Root path of all files listed in files collection
    :param filter_blender: Show Blender files in the File Browser
    :param filter_folder: Show folders in the File Browser
    :param use_scenes: Scenes, Generate scenes previews
    :param use_collections: Collections, Generate collections previews
    :param use_objects: Objects, Generate objects previews
    :param use_intern_data: Materials & Textures, Generate internal previews (materials, textures, images, etc.)
    :param use_trusted: Trusted Blend Files, Enable Python evaluation for selected files
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with generated previews
    """

def previews_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Clear data-block previews (only for some types like objects, materials, textures, etc.)

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
    """

def previews_ensure(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Ensure data-block previews are available and up-to-date (to be saved in .blend file, only for some types like materials, textures, etc.)"""

def properties_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
) -> None:
    """Add your own property to the data-block

    :param data_path: Property Edit, Property data_path edit
    """

def properties_context_change(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    context: str = "",
) -> None:
    """Jump to a different tab inside the properties editor

    :param context: Context
    """

def properties_edit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Change a custom propertys type, or adjust how it is displayed in the interface

        :param data_path: Property Edit, Property data_path edit
        :param property_name: Property Name, Property name edit
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
        :param is_overridable_library: Library Overridable, Allow the property to be overridden when the data-block is linked
        :param description: Description
        :param use_soft_limits: Soft Limits, Limits the Property Value slider to a range, values outside the range must be inputted numerically
        :param array_length: Array Length
        :param default_int: Default Value
        :param min_int: Min
        :param max_int: Max
        :param soft_min_int: Soft Min
        :param soft_max_int: Soft Max
        :param step_int: Step
        :param default_bool: Default Value
        :param default_float: Default Value
        :param min_float: Min
        :param max_float: Max
        :param soft_min_float: Soft Min
        :param soft_max_float: Soft Max
        :param precision: Precision
        :param step_float: Step
        :param subtype: Subtype
        :param default_string: Default Value
        :param id_type: ID Type
        :param eval_string: Value, Python value for unsupported custom property types
    """

def properties_edit_value(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    property_name: str = "",
    eval_string: str = "",
) -> None:
    """Edit the value of a custom property

    :param data_path: Property Edit, Property data_path edit
    :param property_name: Property Name, Property name edit
    :param eval_string: Value, Value for custom property types that can only be edited as a Python expression
    """

def properties_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    data_path: str = "",
    property_name: str = "",
) -> None:
    """Internal use (edit a property data_path)

    :param data_path: Property Edit, Property data_path edit
    :param property_name: Property Name, Property name edit
    """

def quit_blender(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Quit Blender"""

def radial_control(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Set some size property (e.g. brush size) with mouse wheel

    :param data_path_primary: Primary Data Path, Primary path of property to be set by the radial control
    :param data_path_secondary: Secondary Data Path, Secondary path of property to be set by the radial control
    :param use_secondary: Use Secondary, Path of property to select between the primary and secondary data paths
    :param rotation_path: Rotation Path, Path of property used to rotate the texture display
    :param color_path: Color Path, Path of property used to set the color of the control
    :param fill_color_path: Fill Color Path, Path of property used to set the fill color of the control
    :param fill_color_override_path: Fill Color Override Path
    :param fill_color_override_test_path: Fill Color Override Test
    :param zoom_path: Zoom Path, Path of property used to set the zoom level for the control
    :param image_id: Image ID, Path of ID that is used to generate an image for the control
    :param secondary_tex: Secondary Texture, Tweak brush secondary/mask texture
    :param release_confirm: Confirm On Release, Finish operation on key release
    """

def read_factory_settings(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_factory_startup_app_template_only: bool | None = False,
    app_template: str = "Template",
    use_empty: bool | None = False,
) -> None:
    """Load factory default startup file and preferences. To make changes permanent, use "Save Startup File" and "Save Preferences"

    :param use_factory_startup_app_template_only: Factory Startup App-Template Only
    :param use_empty: Empty, After loading, remove everything except scenes, windows, and workspaces. This makes it possible to load the startup file with its scene configuration and window layout intact, but no objects, materials, animations, ...
    """

def read_factory_userpref(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_factory_startup_app_template_only: bool | None = False,
) -> None:
    """Load factory default preferences. To make changes to preferences permanent, use "Save Preferences"

    :param use_factory_startup_app_template_only: Factory Startup App-Template Only
    """

def read_history(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reloads history and bookmarks"""

def read_homefile(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    load_ui: bool | None = True,
    use_splash: bool | None = False,
    use_factory_startup: bool | None = False,
    use_factory_startup_app_template_only: bool | None = False,
    app_template: str = "Template",
    use_empty: bool | None = False,
) -> None:
    """Open the default file

    :param filepath: File Path, Path to an alternative start-up file
    :param load_ui: Load UI, Load user interface setup from the .blend file
    :param use_splash: Splash
    :param use_factory_startup: Factory Startup, Load the default (factory startup) blend file. This is independent of the normal start-up file that the user can save
    :param use_factory_startup_app_template_only: Factory Startup App-Template Only
    :param use_empty: Empty, After loading, remove everything except scenes, windows, and workspaces. This makes it possible to load the startup file with its scene configuration and window layout intact, but no objects, materials, animations, ...
    """

def read_userpref(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Load last saved preferences"""

def recover_auto_save(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Open an automatically saved file to recover it

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
        :param filter_collada: Filter COLLADA files
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
        :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    """

def recover_last_session(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_scripts: bool | None = True,
) -> None:
    """Open the last closed file ("quit.blend")

    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    """

def redraw_timer(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Simple redraw timer to test the speed of updating the interface

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
        :param iterations: Iterations, Number of times to redraw
        :param time_limit: Time Limit, Seconds to run the test for (override iterations)
    """

def revert_mainfile(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_scripts: bool | None = True,
) -> None:
    """Reload the saved file

    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    """

def save_as_mainfile(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Save the current file in the desired location

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
        :param filter_collada: Filter COLLADA files
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
        :param compress: Compress, Write compressed .blend file
        :param relative_remap: Remap Relative, Remap relative paths when saving to a different directory
        :param copy: Save Copy, Save a copy of the actual working state but does not make saved file active
    """

def save_homefile(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Make the current file the default startup file"""

def save_mainfile(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Save the current Blender file

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
        :param filter_collada: Filter COLLADA files
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
        :param compress: Compress, Write compressed .blend file
        :param relative_remap: Remap Relative, Remap relative paths when saving to a different directory
        :param exit: Exit, Exit Blender after saving
        :param incremental: Incremental, Save the current Blender file with a numerically incremented name that does not overwrite any existing files
    """

def save_userpref(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Make the current preferences default"""

def search_menu(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Pop-up a search over all menus in the current context"""

def search_operator(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Pop-up a search over all available operators in current context"""

def search_single_menu(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    menu_idname: str = "",
    initial_query: str = "",
) -> None:
    """Pop-up a search for a menu in current context

    :param menu_idname: Menu Name, Menu to search in
    :param initial_query: Initial Query, Query to insert into the search box
    """

def set_stereo_3d(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    display_mode: bpy.stub_internal.rna_enums.Stereo3DDisplayItems | None = "ANAGLYPH",
    anaglyph_type: bpy.stub_internal.rna_enums.Stereo3DAnaglyphTypeItems
    | None = "RED_CYAN",
    interlace_type: bpy.stub_internal.rna_enums.Stereo3DInterlaceTypeItems
    | None = "ROW_INTERLEAVED",
    use_interlace_swap: bool | None = False,
    use_sidebyside_crosseyed: bool | None = False,
) -> None:
    """Toggle 3D stereo support for current window (or change the display mode)

    :param display_mode: Display Mode
    :param anaglyph_type: Anaglyph Type
    :param interlace_type: Interlace Type
    :param use_interlace_swap: Swap Left/Right, Swap left and right stereo channels
    :param use_sidebyside_crosseyed: Cross-Eyed, Right eye should see left image and vice versa
    """

def splash(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Open the splash screen with release info"""

def splash_about(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Open a window with information about Blender"""

def stl_export(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Save the scene to an STL file

        :param filepath: File Path, Path to file
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
        :param filter_collada: Filter COLLADA files
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
        :param ascii_format: ASCII Format, Export file in ASCII format, export as binary otherwise
        :param use_batch: Batch Export, Export each object to a separate file
        :param export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects
        :param collection: Source Collection, Export only objects from this collection (and its children)
        :param global_scale: Scale
        :param use_scene_unit: Scene Unit, Apply current scenes unit (as defined by unit scale) to exported data
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
        :param apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes
        :param filter_glob: Extension Filter
    """

def stl_import(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Import an STL file as an object

        :param filepath: File Path, Path to file
        :param directory: Directory, Directory of the file
        :param files: Files
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
        :param filter_collada: Filter COLLADA files
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
        :param global_scale: Scale
        :param use_scene_unit: Scene Unit, Apply current scenes unit (as defined by unit scale) to imported data
        :param use_facet_normal: Facet Normals, Use (import) facet normals (note that this will still give flat shading)
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
        :param use_mesh_validate: Validate Mesh, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)
        :param filter_glob: Extension Filter
    """

def sysinfo(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
) -> None:
    """Generate system information, saved into a text file

    :param filepath: filepath
    """

def tool_set_by_brush_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    brush_type: str = "",
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
) -> None:
    """Look up the most appropriate tool for the given brush type and activate that

    :param brush_type: Brush Type, Brush type identifier for which the most appropriate tool will be looked up
    :param space_type: Type
    """

def tool_set_by_id(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Set the tool by name (for key-maps)

    :param name: Identifier, Identifier of the tool
    :param cycle: Cycle, Cycle through tools in this group
    :param as_fallback: Set Fallback, Set the fallback tool instead of the primary tool
    :param space_type: Type
    """

def tool_set_by_index(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Set the tool by index (for key-maps)

    :param index: Index in Toolbar
    :param cycle: Cycle, Cycle through tools in this group
    :param expand: expand, Include tool subgroups
    :param as_fallback: Set Fallback, Set the fallback tool instead of the primary
    :param space_type: Type
    """

def toolbar(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

def toolbar_fallback_pie(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

def toolbar_prompt(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Leader key like functionality for accessing tools"""

def url_open(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    url: str = "",
) -> None:
    """Open a website in the web browser

    :param url: URL, URL to open
    """

def url_open_preset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "",
) -> None:
    """Open a preset website in the web browser

    :param type: Site
    """

def usd_export(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
    export_textures: bool | None = False,
    export_textures_mode: typing.Literal["KEEP", "PRESERVE", "NEW"] | None = "NEW",
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
    export_points: bool | None = True,
    export_volumes: bool | None = True,
    triangulate_meshes: bool | None = False,
    quad_method: bpy.stub_internal.rna_enums.ModifierTriangulateQuadMethodItems
    | None = "SHORTEST_DIAGONAL",
    ngon_method: bpy.stub_internal.rna_enums.ModifierTriangulateNgonMethodItems
    | None = "BEAUTY",
    usdz_downscale_size: typing.Literal[
        "KEEP", "256", "512", "1024", "2048", "4096", "CUSTOM"
    ]
    | None = "KEEP",
    usdz_downscale_custom_size: int | None = 128,
    merge_parent_xform: bool | None = False,
    convert_scene_units: typing.Literal[
        "METERS",
        "KILOMETERS",
        "CENTIMETERS",
        "MILLIMETERS",
        "INCHES",
        "FEET",
        "YARDS",
        "CUSTOM",
    ]
    | None = "METERS",
    meters_per_unit: float | None = 1.0,
) -> None:
    """Export current scene in a USD archive

        :param filepath: File Path, Path to file
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
        :param filter_collada: Filter COLLADA files
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
        :param selected_objects_only: Selection Only, Only export selected objects. Unselected parents of selected objects are exported as empty transform
        :param visible_objects_only: Visible Only, Only export visible objects. Invisible parents of exported objects are exported as empty transforms
        :param collection: Collection
        :param export_animation: Animation, Export all frames in the render frame range, rather than only the current frame
        :param export_hair: Hair, Export hair particle systems as USD curves
        :param export_uvmaps: UV Maps, Include all mesh UV maps in the export
        :param rename_uvmaps: Rename UV Maps, Rename active render UV map to "st" to match USD conventions
        :param export_mesh_colors: Color Attributes, Include mesh color attributes in the export
        :param export_normals: Normals, Include normals of exported meshes in the export
        :param export_materials: Materials, Export viewport settings of materials as USD preview materials, and export material assignments as geometry subsets
        :param export_subdivision: Subdivision, Choose how subdivision modifiers will be mapped to the USD subdivision scheme during export

    IGNORE
    Ignore -- Scheme = None. Export base mesh without subdivision.

    TESSELLATE
    Tessellate -- Scheme = None. Export subdivided mesh.

    BEST_MATCH
    Best Match -- Scheme = Catmull-Clark, when possible. Reverts to exporting the subdivided mesh for the Simple subdivision type.
        :param export_armatures: Armatures, Export armatures and meshes with armature modifiers as USD skeletons and skinned meshes
        :param only_deform_bones: Only Deform Bones, Only export deform bones and their parents
        :param export_shapekeys: Shape Keys, Export shape keys as USD blend shapes
        :param use_instancing: Instancing, Export instanced objects as references in USD rather than real objects
        :param evaluation_mode: Use Settings for, Determines visibility of objects, modifier settings, and other areas where there are different settings for viewport and rendering

    RENDER
    Render -- Use Render settings for object visibility, modifier settings, etc.

    VIEWPORT
    Viewport -- Use Viewport settings for object visibility, modifier settings, etc.
        :param generate_preview_surface: USD Preview Surface Network, Generate an approximate USD Preview Surface shader representation of a Principled BSDF node network
        :param generate_materialx_network: MaterialX Network, Generate a MaterialX network representation of the materials
        :param convert_orientation: Convert Orientation, Convert orientation axis to a different convention to match other applications
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
        :param export_textures: Export Textures, If exporting materials, export textures referenced by material nodes to a textures directory in the same directory as the USD file
        :param export_textures_mode: Export Textures, Texture export method

    KEEP
    Keep -- Use original location of textures.

    PRESERVE
    Preserve -- Preserve file paths of textures from already imported USD files.
    Export remaining textures to a textures folder next to the USD file.

    NEW
    New Path -- Export textures to a textures folder next to the USD file.
        :param overwrite_textures: Overwrite Textures, Overwrite existing files when exporting textures
        :param relative_paths: Relative Paths, Use relative paths to reference external files (i.e. textures, volumes) in USD, otherwise use absolute paths
        :param xform_op_mode: Xform Ops, The type of transform operators to write

    TRS
    Translate, Rotate, Scale -- Export with translate, rotate, and scale Xform operators.

    TOS
    Translate, Orient, Scale -- Export with translate, orient quaternion, and scale Xform operators.

    MAT
    Matrix -- Export matrix operator.
        :param root_prim_path: Root Prim, If set, add a transform primitive with the given path to the stage as the parent of all exported data
        :param export_custom_properties: Custom Properties, Export custom properties as USD attributes
        :param custom_properties_namespace: Namespace, If set, add the given namespace as a prefix to exported custom property names. This only applies to property names that do not already have a prefix (e.g., it would apply to name bar but not foo:bar) and does not apply to blender object and data names which are always exported in the userProperties:blender namespace
        :param author_blender_name: Blender Names, Author USD custom attributes containing the original Blender object and object data names
        :param convert_world_material: World Dome Light, Convert the world material to a USD dome light. Currently works for simple materials, consisting of an environment texture connected to a background shader, with an optional vector multiply of the texture color
        :param allow_unicode: Allow Unicode, Preserve UTF-8 encoded characters when writing USD prim and property names (requires software utilizing USD 24.03 or greater when opening the resulting files)
        :param export_meshes: Meshes, Export all meshes
        :param export_lights: Lights, Export all lights
        :param export_cameras: Cameras, Export all cameras
        :param export_curves: Curves, Export all curves
        :param export_points: Point Clouds, Export all point clouds
        :param export_volumes: Volumes, Export all volumes
        :param triangulate_meshes: Triangulate Meshes, Triangulate meshes during export
        :param quad_method: Quad Method, Method for splitting the quads into triangles
        :param ngon_method: N-gon Method, Method for splitting the n-gons into triangles
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
        :param usdz_downscale_custom_size: USDZ Custom Downscale Size, Custom size for downscaling exported textures
        :param merge_parent_xform: Merge parent Xform, Merge USD primitives with their Xform parent if possible. USD does not allow nested UsdGeomGprims, intermediary Xform prims will be defined to keep the USD file valid when encountering object hierarchies.
        :param convert_scene_units: Units, Set the USD Stage meters per unit to the chosen measurement, or a custom value

    METERS
    Meters -- Scene meters per unit to 1.0.

    KILOMETERS
    Kilometers -- Scene meters per unit to 1000.0.

    CENTIMETERS
    Centimeters -- Scene meters per unit to 0.01.

    MILLIMETERS
    Millimeters -- Scene meters per unit to 0.001.

    INCHES
    Inches -- Scene meters per unit to 0.0254.

    FEET
    Feet -- Scene meters per unit to 0.3048.

    YARDS
    Yards -- Scene meters per unit to 0.9144.

    CUSTOM
    Custom -- Specify a custom scene meters per unit value.
        :param meters_per_unit: Meters Per Unit, Custom value for meters per unit in the USD Stage
    """

def usd_import(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
    mtl_purpose: typing.Literal["MTL_ALL_PURPOSE", "MTL_PREVIEW", "MTL_FULL"]
    | None = "MTL_FULL",
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
    merge_parent_xform: bool | None = True,
    apply_unit_conversion_scale: bool | None = True,
) -> None:
    """Import USD stage into current scene

        :param filepath: File Path, Path to file
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
        :param filter_collada: Filter COLLADA files
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
        :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the worlds origin
        :param set_frame_range: Set Frame Range, Update the scenes start and end frame to match those of the USD archive
        :param import_cameras: Cameras
        :param import_curves: Curves
        :param import_lights: Lights
        :param import_materials: Materials
        :param import_meshes: Meshes
        :param import_volumes: Volumes
        :param import_shapes: USD Shapes
        :param import_skeletons: Armatures
        :param import_blendshapes: Shape Keys
        :param import_points: Point Clouds
        :param import_subdiv: Import Subdivision Scheme, Create subdivision surface modifiers based on the USD SubdivisionScheme attribute
        :param support_scene_instancing: Scene Instancing, Import USD scene graph instances as collection instances
        :param import_visible_only: Visible Primitives Only, Do not import invisible USD primitives. Only applies to primitives with a non-animated visibility attribute. Primitives with animated visibility will always be imported
        :param create_collection: Create Collection, Add all imported objects to a new collection
        :param read_mesh_uvs: UV Coordinates, Read mesh UV coordinates
        :param read_mesh_colors: Color Attributes, Read mesh color attributes
        :param read_mesh_attributes: Mesh Attributes, Read USD Primvars as mesh attributes
        :param prim_path_mask: Path Mask, Import only the primitive at the given path and its descendants. Multiple paths may be specified in a list delimited by commas or semicolons
        :param import_guide: Guide, Import guide geometry
        :param import_proxy: Proxy, Import proxy geometry
        :param import_render: Render, Import final render geometry
        :param import_all_materials: Import All Materials, Also import materials that are not used by any geometry. Note that when this option is false, materials referenced by geometry will still be imported
        :param import_usd_preview: Import USD Preview, Convert UsdPreviewSurface shaders to Principled BSDF shader networks
        :param set_material_blend: Set Material Blend, If the Import USD Preview option is enabled, the material blend method will automatically be set based on the shaders opacity and opacityThreshold inputs
        :param light_intensity_scale: Light Intensity Scale, Scale for the intensity of imported lights
        :param mtl_purpose: Material Purpose, Attempt to import materials with the given purpose. If no material with this purpose is bound to the primitive, fall back on loading any other bound material

    MTL_ALL_PURPOSE
    All Purpose -- Attempt to import allPurpose materials..

    MTL_PREVIEW
    Preview -- Attempt to import preview materials. Load allPurpose materials as a fallback.

    MTL_FULL
    Full -- Attempt to import full materials. Load allPurpose or preview materials, in that order, as a fallback.
        :param mtl_name_collision_mode: Material Name Collision, Behavior when the name of an imported material conflicts with an existing material

    MAKE_UNIQUE
    Make Unique -- Import each USD material as a unique Blender material.

    REFERENCE_EXISTING
    Reference Existing -- If a material with the same name already exists, reference that instead of importing.
        :param import_textures_mode: Import Textures, Behavior when importing textures from a USDZ archive

    IMPORT_NONE
    None -- Dont import textures.

    IMPORT_PACK
    Packed -- Import textures as packed data.

    IMPORT_COPY
    Copy -- Copy files to textures directory.
        :param import_textures_dir: Textures Directory, Path to the directory where imported textures will be copied
        :param tex_name_collision_mode: File Name Collision, Behavior when the name of an imported texture file conflicts with an existing file

    USE_EXISTING
    Use Existing -- If a file with the same name already exists, use that instead of copying.

    OVERWRITE
    Overwrite -- Overwrite existing files.
        :param attr_import_mode: Custom Properties, Behavior when importing USD attributes as Blender custom properties

    NONE
    None -- Do not import USD custom attributes.

    USER
    User -- Import USD attributes in the userProperties namespace as Blender custom properties. The namespace will be stripped from the property names.

    ALL
    All Custom -- Import all USD custom attributes as Blender custom properties. Namespaces will be retained in the property names.
        :param validate_meshes: Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)
        :param create_world_material: World Dome Light, Convert the first discovered USD dome light to a world background shader
        :param import_defined_only: Defined Primitives Only, Import only defined USD primitives. When disabled this allows importing USD primitives which are not defined, such as those with an override specifier
        :param merge_parent_xform: Merge parent Xform, Allow USD primitives to merge with their Xform parent if they are the only child in the hierarchy
        :param apply_unit_conversion_scale: Apply Unit Conversion Scale, Scale the scene objects by the USD stages meters per unit value. This scaling is applied in addition to the value specified in the Scale option
    """

def window_close(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Close the current window"""

def window_fullscreen_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle the current window full-screen"""

def window_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create a new window"""

def window_new_main(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create a new main window with its own workspace and scene selection"""

def xr_navigation_fly(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Move/turn relative to the VR viewer or controller

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
    Viewer Forward -- Move along viewers forward axis.

    VIEWER_BACK
    Viewer Back -- Move along viewers back axis.

    VIEWER_LEFT
    Viewer Left -- Move along viewers left axis.

    VIEWER_RIGHT
    Viewer Right -- Move along viewers right axis.

    CONTROLLER_FORWARD
    Controller Forward -- Move along controllers forward axis.
        :param lock_location_z: Lock Elevation, Prevent changes to viewer elevation
        :param lock_direction: Lock Direction, Limit movement to viewers initial direction
        :param speed_frame_based: Frame Based Speed, Apply fixed movement deltas every update
        :param speed_min: Minimum Speed, Minimum move (turn) speed in meters (radians) per second or frame
        :param speed_max: Maximum Speed, Maximum move (turn) speed in meters (radians) per second or frame
        :param speed_interpolation0: Speed Interpolation 0, First cubic spline control point between min/max speeds
        :param speed_interpolation1: Speed Interpolation 1, Second cubic spline control point between min/max speeds
    """

def xr_navigation_grab(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    lock_location: bool | None = False,
    lock_location_z: bool | None = False,
    lock_rotation: bool | None = False,
    lock_rotation_z: bool | None = False,
    lock_scale: bool | None = False,
) -> None:
    """Navigate the VR scene by grabbing with controllers

    :param lock_location: Lock Location, Prevent changes to viewer location
    :param lock_location_z: Lock Elevation, Prevent changes to viewer elevation
    :param lock_rotation: Lock Rotation, Prevent changes to viewer rotation
    :param lock_rotation_z: Lock Up Orientation, Prevent changes to viewer up orientation
    :param lock_scale: Lock Scale, Prevent changes to viewer scale
    """

def xr_navigation_reset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: bool | None = True,
    rotation: bool | None = True,
    scale: bool | None = True,
) -> None:
    """Reset VR navigation deltas relative to session base pose

    :param location: Location, Reset location deltas
    :param rotation: Rotation, Reset rotation deltas
    :param scale: Scale, Reset scale deltas
    """

def xr_navigation_teleport(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    teleport_axes: collections.abc.Iterable[bool] | None = (True, True, True),
    interpolation: float | None = 1.0,
    offset: float | None = 0.0,
    selectable_only: bool | None = True,
    distance: float | None = 1.70141e38,
    from_viewer: bool | None = False,
    axis: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, -1.0),
    color: collections.abc.Iterable[float] | None = (0.35, 0.35, 1.0, 1.0),
) -> None:
    """Set VR viewer location to controller raycast hit location

    :param teleport_axes: Teleport Axes, Enabled teleport axes in navigation space
    :param interpolation: Interpolation, Interpolation factor between viewer and hit locations
    :param offset: Offset, Offset along hit normal to subtract from final location
    :param selectable_only: Selectable Only, Only allow selectable objects to influence raycast result
    :param distance: Maximum raycast distance
    :param from_viewer: From Viewer, Use viewer pose as raycast origin
    :param axis: Axis, Raycast axis in controller/viewer space
    :param color: Color, Raycast color
    """

def xr_session_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Open a view for use with virtual reality headsets, or close it if already opened"""
