import sys
import typing
import bpy


def addon_disable(module: str = ""):
    '''Disable an add-on 

    :param module: Module, Module name of the add-on to disable 
    :type module: str
    '''

    pass


def addon_enable(module: str = ""):
    '''Enable an add-on 

    :param module: Module, Module name of the add-on to enable 
    :type module: str
    '''

    pass


def addon_expand(module: str = ""):
    '''Display information and preferences for this add-on 

    :param module: Module, Module name of the add-on to expand 
    :type module: str
    '''

    pass


def addon_install(overwrite: bool = True,
                  target: int = 'DEFAULT',
                  filepath: str = "",
                  filter_folder: bool = True,
                  filter_python: bool = True,
                  filter_glob: str = "*.py;*.zip"):
    '''Install an add-on 

    :param overwrite: Overwrite, Remove existing add-ons with the same ID 
    :type overwrite: bool
    :param target: Target Path 
    :type target: int
    :param filepath: filepath 
    :type filepath: str
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_python: Filter python 
    :type filter_python: bool
    :param filter_glob: filter_glob 
    :type filter_glob: str
    '''

    pass


def addon_refresh():
    '''Scan add-on directories for new modules 

    '''

    pass


def addon_remove(module: str = ""):
    '''Delete the add-on from the file system 

    :param module: Module, Module name of the add-on to remove 
    :type module: str
    '''

    pass


def addon_userpref_show(module: str = ""):
    '''Show add-on user preferences 

    :param module: Module, Module name of the add-on to expand 
    :type module: str
    '''

    pass


def alembic_export(filepath: str = "",
                   check_existing: bool = True,
                   filter_blender: bool = False,
                   filter_backup: bool = False,
                   filter_image: bool = False,
                   filter_movie: bool = False,
                   filter_python: bool = False,
                   filter_font: bool = False,
                   filter_sound: bool = False,
                   filter_text: bool = False,
                   filter_btx: bool = False,
                   filter_collada: bool = False,
                   filter_alembic: bool = True,
                   filter_folder: bool = True,
                   filter_blenlib: bool = False,
                   filemode: int = 8,
                   display_type: int = 'DEFAULT',
                   sort_method: int = 'FILE_SORT_ALPHA',
                   start: int = -2147483648,
                   end: int = -2147483648,
                   xsamples: int = 1,
                   gsamples: int = 1,
                   sh_open: float = 0.0,
                   sh_close: float = 1.0,
                   selected: bool = False,
                   renderable_only: bool = True,
                   visible_layers_only: bool = False,
                   flatten: bool = False,
                   uvs: bool = True,
                   packuv: bool = True,
                   normals: bool = True,
                   vcolors: bool = False,
                   face_sets: bool = False,
                   subdiv_schema: bool = False,
                   apply_subdiv: bool = False,
                   compression_type: int = 'OGAWA',
                   global_scale: float = 1.0,
                   triangulate: bool = False,
                   quad_method: int = 'SHORTEST_DIAGONAL',
                   ngon_method: int = 'BEAUTY',
                   export_hair: bool = True,
                   export_particles: bool = True,
                   as_background_job: bool = True,
                   init_scene_frame_range=False):
    '''Export current scene in an Alembic archive 

    :param filepath: File Path, Path to file 
    :type filepath: str
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
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    :param start: Start Frame, Start frame of the export, use the default value to take the start frame of the current scene 
    :type start: int
    :param end: End Frame, End frame of the export, use the default value to take the end frame of the current scene 
    :type end: int
    :param xsamples: Transform Samples, Number of times per frame transformations are sampled 
    :type xsamples: int
    :param gsamples: Geometry Samples, Number of times per frame object data are sampled 
    :type gsamples: int
    :param sh_open: Shutter Open, Time at which the shutter is open 
    :type sh_open: float
    :param sh_close: Shutter Close, Time at which the shutter is closed 
    :type sh_close: float
    :param selected: Selected Objects Only, Export only selected objects 
    :type selected: bool
    :param renderable_only: Renderable Objects Only, Export only objects marked renderable in the outliner 
    :type renderable_only: bool
    :param visible_layers_only: Visible Layers Only, Export only objects in visible layers 
    :type visible_layers_only: bool
    :param flatten: Flatten Hierarchy, Do not preserve objects’ parent/children relationship 
    :type flatten: bool
    :param uvs: UVs, Export UVs 
    :type uvs: bool
    :param packuv: Pack UV Islands, Export UVs with packed island 
    :type packuv: bool
    :param normals: Normals, Export normals 
    :type normals: bool
    :param vcolors: Vertex Colors, Export vertex colors 
    :type vcolors: bool
    :param face_sets: Face Sets, Export per face shading group assignments 
    :type face_sets: bool
    :param subdiv_schema: Use Subdivision Schema, Export meshes using Alembic’s subdivision schema 
    :type subdiv_schema: bool
    :param apply_subdiv: Apply Subsurf, Export subdivision surfaces as meshes 
    :type apply_subdiv: bool
    :param compression_type: Compression 
    :type compression_type: int
    :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world’s origin 
    :type global_scale: float
    :param triangulate: Triangulate, Export Polygons (Quads & NGons) as Triangles 
    :type triangulate: bool
    :param quad_method: Quad Method, Method for splitting the quads into trianglesBEAUTY Beauty , Split the quads in nice triangles, slower method.FIXED Fixed, Split the quads on the first and third vertices.FIXED_ALTERNATE Fixed Alternate, Split the quads on the 2nd and 4th vertices.SHORTEST_DIAGONAL Shortest Diagonal, Split the quads based on the distance between the vertices. 
    :type quad_method: int
    :param ngon_method: Polygon Method, Method for splitting the polygons into trianglesBEAUTY Beauty , Split the quads in nice triangles, slower method.FIXED Fixed, Split the quads on the first and third vertices.FIXED_ALTERNATE Fixed Alternate, Split the quads on the 2nd and 4th vertices.SHORTEST_DIAGONAL Shortest Diagonal, Split the quads based on the distance between the vertices. 
    :type ngon_method: int
    :param export_hair: Export Hair, Exports hair particle systems as animated curves 
    :type export_hair: bool
    :param export_particles: Export Particles, Exports non-hair particle systems 
    :type export_particles: bool
    :param as_background_job: Run as Background Job, Enable this to run the import in the background, disable to block Blender while importing 
    :type as_background_job: bool
    '''

    pass


def alembic_import(filepath: str = "",
                   check_existing: bool = True,
                   filter_blender: bool = False,
                   filter_backup: bool = False,
                   filter_image: bool = False,
                   filter_movie: bool = False,
                   filter_python: bool = False,
                   filter_font: bool = False,
                   filter_sound: bool = False,
                   filter_text: bool = False,
                   filter_btx: bool = False,
                   filter_collada: bool = False,
                   filter_alembic: bool = True,
                   filter_folder: bool = True,
                   filter_blenlib: bool = False,
                   filemode: int = 8,
                   display_type: int = 'DEFAULT',
                   sort_method: int = 'FILE_SORT_ALPHA',
                   scale: float = 1.0,
                   set_frame_range: bool = True,
                   validate_meshes: bool = False,
                   is_sequence: bool = False,
                   as_background_job: bool = True):
    '''Load an Alembic archive 

    :param filepath: File Path, Path to file 
    :type filepath: str
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
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the world’s origin 
    :type scale: float
    :param set_frame_range: Set Frame Range, If checked, update scene’s start and end frame to match those of the Alembic archive 
    :type set_frame_range: bool
    :param validate_meshes: Validate Meshes, Check imported mesh objects for invalid data (slow) 
    :type validate_meshes: bool
    :param is_sequence: Is Sequence, Set to true if the cache is split into separate files 
    :type is_sequence: bool
    :param as_background_job: Run as Background Job, Enable this to run the export in the background, disable to block Blender while exporting 
    :type as_background_job: bool
    '''

    pass


def app_template_install(overwrite: bool = True,
                         filepath: str = "",
                         filter_folder: bool = True,
                         filter_glob: str = "*.zip"):
    '''Install an application-template 

    :param overwrite: Overwrite, Remove existing template with the same ID 
    :type overwrite: bool
    :param filepath: filepath 
    :type filepath: str
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_glob: filter_glob 
    :type filter_glob: str
    '''

    pass


def appconfig_activate(filepath: str = ""):
    '''Undocumented 

    :param filepath: filepath 
    :type filepath: str
    '''

    pass


def appconfig_default():
    '''Undocumented 

    '''

    pass


def append(filepath: str = "",
           directory: str = "",
           filename: str = "",
           files: typing.List['bpy.types.OperatorFileListElement'] = None,
           filter_blender: bool = True,
           filter_backup: bool = False,
           filter_image: bool = False,
           filter_movie: bool = False,
           filter_python: bool = False,
           filter_font: bool = False,
           filter_sound: bool = False,
           filter_text: bool = False,
           filter_btx: bool = False,
           filter_collada: bool = False,
           filter_alembic: bool = False,
           filter_folder: bool = True,
           filter_blenlib: bool = True,
           filemode: int = 1,
           display_type: int = 'DEFAULT',
           sort_method: int = 'FILE_SORT_ALPHA',
           link: bool = False,
           autoselect: bool = True,
           active_layer: bool = True,
           instance_groups: bool = False,
           set_fake: bool = False,
           use_recursive: bool = True):
    '''Append from a Library .blend file 

    :param filepath: File Path, Path to file 
    :type filepath: str
    :param directory: Directory, Directory of the file 
    :type directory: str
    :param filename: File Name, Name of the file 
    :type filename: str
    :param files: Files 
    :type files: typing.List['bpy.types.OperatorFileListElement']
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
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    :param link: Link, Link the objects or data-blocks rather than appending 
    :type link: bool
    :param autoselect: Select, Select new objects 
    :type autoselect: bool
    :param active_layer: Active Layer, Put new objects on the active layer 
    :type active_layer: bool
    :param instance_groups: Instance Groups, Create Dupli-Group instances for each group 
    :type instance_groups: bool
    :param set_fake: Fake User, Set Fake User for appended items (except Objects and Groups) 
    :type set_fake: bool
    :param use_recursive: Localize All, Localize all appended data, including those indirectly linked from other libraries 
    :type use_recursive: bool
    '''

    pass


def blenderplayer_start():
    '''Launch the blender-player with the current blend-file 

    '''

    pass


def call_menu(name: str = ""):
    '''Call (draw) a pre-defined menu 

    :param name: Name, Name of the menu 
    :type name: str
    '''

    pass


def call_menu_pie(name: str = ""):
    '''Call (draw) a pre-defined pie menu 

    :param name: Name, Name of the pie menu 
    :type name: str
    '''

    pass


def collada_export(filepath: str = "",
                   check_existing: bool = True,
                   filter_blender: bool = False,
                   filter_backup: bool = False,
                   filter_image: bool = False,
                   filter_movie: bool = False,
                   filter_python: bool = False,
                   filter_font: bool = False,
                   filter_sound: bool = False,
                   filter_text: bool = False,
                   filter_btx: bool = False,
                   filter_collada: bool = True,
                   filter_alembic: bool = False,
                   filter_folder: bool = True,
                   filter_blenlib: bool = False,
                   filemode: int = 8,
                   display_type: int = 'DEFAULT',
                   sort_method: int = 'FILE_SORT_ALPHA',
                   apply_modifiers: bool = False,
                   export_mesh_type: int = 0,
                   export_mesh_type_selection: int = 'view',
                   selected: bool = False,
                   include_children: bool = False,
                   include_armatures: bool = False,
                   include_shapekeys: bool = True,
                   deform_bones_only: bool = False,
                   active_uv_only: bool = False,
                   use_texture_copies: bool = True,
                   triangulate: bool = True,
                   use_object_instantiation: bool = True,
                   use_blender_profile: bool = True,
                   sort_by_name: bool = False,
                   export_transformation_type: int = 0,
                   export_transformation_type_selection: int = 'matrix',
                   export_texture_type: int = 0,
                   export_texture_type_selection: int = 'mat',
                   open_sim: bool = False,
                   limit_precision: bool = False,
                   keep_bind_info: bool = False):
    '''Save a Collada file 

    :param filepath: File Path, Path to file 
    :type filepath: str
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
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    :param apply_modifiers: Apply Modifiers, Apply modifiers to exported mesh (non destructive)) 
    :type apply_modifiers: bool
    :param export_mesh_type: Resolution, Modifier resolution for export 
    :type export_mesh_type: int
    :param export_mesh_type_selection: Resolution, Modifier resolution for exportview View, Apply modifier’s view settings.render Render, Apply modifier’s render settings. 
    :type export_mesh_type_selection: int
    :param selected: Selection Only, Export only selected elements 
    :type selected: bool
    :param include_children: Include Children, Export all children of selected objects (even if not selected) 
    :type include_children: bool
    :param include_armatures: Include Armatures, Export related armatures (even if not selected) 
    :type include_armatures: bool
    :param include_shapekeys: Include Shape Keys, Export all Shape Keys from Mesh Objects 
    :type include_shapekeys: bool
    :param deform_bones_only: Deform Bones only, Only export deforming bones with armatures 
    :type deform_bones_only: bool
    :param active_uv_only: Only Selected UV Map, Export only the selected UV Map 
    :type active_uv_only: bool
    :param use_texture_copies: Copy, Copy textures to same folder where the .dae file is exported 
    :type use_texture_copies: bool
    :param triangulate: Triangulate, Export Polygons (Quads & NGons) as Triangles 
    :type triangulate: bool
    :param use_object_instantiation: Use Object Instances, Instantiate multiple Objects from same Data 
    :type use_object_instantiation: bool
    :param use_blender_profile: Use Blender Profile, Export additional Blender specific information (for material, shaders, bones, etc.) 
    :type use_blender_profile: bool
    :param sort_by_name: Sort by Object name, Sort exported data by Object name 
    :type sort_by_name: bool
    :param export_transformation_type: Transform, Transformation type for translation, scale and rotation 
    :type export_transformation_type: int
    :param export_transformation_type_selection: Transform, Transformation type for translation, scale and rotationmatrix Matrix, Use <matrix> to specify transformations.transrotloc TransRotLoc, Use <translate>, <rotate>, <scale> to specify transformations. 
    :type export_transformation_type_selection: int
    :param export_texture_type: Texture Type, Type for exported Textures (UV or MAT) 
    :type export_texture_type: int
    :param export_texture_type_selection: Texture Type, Type for exported Textures (UV or MAT)mat Materials, Export Materials.uv UV Textures, Export UV Textures (Face textures) as materials. 
    :type export_texture_type_selection: int
    :param open_sim: Export to SL/OpenSim, Compatibility mode for SL, OpenSim and other compatible online worlds 
    :type open_sim: bool
    :param limit_precision: Limit Precision, Reduce the precision of the exported data to 6 digits 
    :type limit_precision: bool
    :param keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export 
    :type keep_bind_info: bool
    '''

    pass


def collada_import(filepath: str = "",
                   filter_blender: bool = False,
                   filter_backup: bool = False,
                   filter_image: bool = False,
                   filter_movie: bool = False,
                   filter_python: bool = False,
                   filter_font: bool = False,
                   filter_sound: bool = False,
                   filter_text: bool = False,
                   filter_btx: bool = False,
                   filter_collada: bool = True,
                   filter_alembic: bool = False,
                   filter_folder: bool = True,
                   filter_blenlib: bool = False,
                   filemode: int = 8,
                   display_type: int = 'DEFAULT',
                   sort_method: int = 'FILE_SORT_ALPHA',
                   import_units: bool = False,
                   fix_orientation: bool = False,
                   find_chains: bool = False,
                   auto_connect: bool = False,
                   min_chain_length: int = 0,
                   keep_bind_info: bool = False):
    '''Load a Collada file 

    :param filepath: File Path, Path to file 
    :type filepath: str
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
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    :param import_units: Import Units, If disabled match import to Blender’s current Unit settings, otherwise use the settings from the Imported scene 
    :type import_units: bool
    :param fix_orientation: Fix Leaf Bones, Fix Orientation of Leaf Bones (Collada does only support Joints) 
    :type fix_orientation: bool
    :param find_chains: Find Bone Chains, Find best matching Bone Chains and ensure bones in chain are connected 
    :type find_chains: bool
    :param auto_connect: Auto Connect, Set use_connect for parent bones which have exactly one child bone 
    :type auto_connect: bool
    :param min_chain_length: Minimum Chain Length, When searching Bone Chains disregard chains of length below this value 
    :type min_chain_length: int
    :param keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export 
    :type keep_bind_info: bool
    '''

    pass


def context_collection_boolean_set(data_path_iter: str = "",
                                   data_path_item: str = "",
                                   type: int = 'TOGGLE'):
    '''Set boolean values for a collection of items 

    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable 
    :type data_path_iter: str
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float) 
    :type data_path_item: str
    :param type: Type 
    :type type: int
    '''

    pass


def context_cycle_array(data_path: str = "", reverse: bool = False):
    '''Set a context array value (useful for cycling the active mesh edit mode) 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: str
    :param reverse: Reverse, Cycle backwards 
    :type reverse: bool
    '''

    pass


def context_cycle_enum(data_path: str = "",
                       reverse: bool = False,
                       wrap: bool = False):
    '''Toggle a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: str
    :param reverse: Reverse, Cycle backwards 
    :type reverse: bool
    :param wrap: Wrap, Wrap back to the first/last values 
    :type wrap: bool
    '''

    pass


def context_cycle_int(data_path: str = "",
                      reverse: bool = False,
                      wrap: bool = False):
    '''Set a context value (useful for cycling active material, vertex keys, groups, etc.) 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: str
    :param reverse: Reverse, Cycle backwards 
    :type reverse: bool
    :param wrap: Wrap, Wrap back to the first/last values 
    :type wrap: bool
    '''

    pass


def context_menu_enum(data_path: str = ""):
    '''Undocumented 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: str
    '''

    pass


def context_modal_mouse(data_path_iter: str = "",
                        data_path_item: str = "",
                        header_text: str = "",
                        input_scale: float = 0.01,
                        invert: bool = False,
                        initial_x: int = 0):
    '''Adjust arbitrary values with mouse input 

    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable 
    :type data_path_iter: str
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float) 
    :type data_path_item: str
    :param header_text: Header Text, Text to display in header during scale 
    :type header_text: str
    :param input_scale: input_scale, Scale the mouse movement by this value before applying the delta 
    :type input_scale: float
    :param invert: invert, Invert the mouse input 
    :type invert: bool
    :param initial_x: initial_x 
    :type initial_x: int
    '''

    pass


def context_pie_enum(data_path: str = ""):
    '''Undocumented 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: str
    '''

    pass


def context_scale_float(data_path: str = "", value: float = 1.0):
    '''Scale a float context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: str
    :param value: Value, Assign value 
    :type value: float
    '''

    pass


def context_scale_int(data_path: str = "",
                      value: float = 1.0,
                      always_step: bool = True):
    '''Scale an int context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: str
    :param value: Value, Assign value 
    :type value: float
    :param always_step: Always Step, Always adjust the value by a minimum of 1 when ‘value’ is not 1.0 
    :type always_step: bool
    '''

    pass


def context_set_boolean(data_path: str = "", value: bool = True):
    '''Set a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: str
    :param value: Value, Assignment value 
    :type value: bool
    '''

    pass


def context_set_enum(data_path: str = "", value: str = ""):
    '''Set a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: str
    :param value: Value, Assignment value (as a string) 
    :type value: str
    '''

    pass


def context_set_float(data_path: str = "",
                      value: float = 0.0,
                      relative: bool = False):
    '''Set a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: str
    :param value: Value, Assignment value 
    :type value: float
    :param relative: Relative, Apply relative to the current value (delta) 
    :type relative: bool
    '''

    pass


def context_set_id(data_path: str = "", value: str = ""):
    '''Set a context value to an ID data-block 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: str
    :param value: Value, Assign value 
    :type value: str
    '''

    pass


def context_set_int(data_path: str = "",
                    value: int = 0,
                    relative: bool = False):
    '''Set a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: str
    :param value: Value, Assign value 
    :type value: int
    :param relative: Relative, Apply relative to the current value (delta) 
    :type relative: bool
    '''

    pass


def context_set_string(data_path: str = "", value: str = ""):
    '''Set a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: str
    :param value: Value, Assign value 
    :type value: str
    '''

    pass


def context_set_value(data_path: str = "", value: str = ""):
    '''Set a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: str
    :param value: Value, Assignment value (as a string) 
    :type value: str
    '''

    pass


def context_toggle(data_path: str = ""):
    '''Toggle a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: str
    '''

    pass


def context_toggle_enum(data_path: str = "",
                        value_1: str = "",
                        value_2: str = ""):
    '''Toggle a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: str
    :param value_1: Value, Toggle enum 
    :type value_1: str
    :param value_2: Value, Toggle enum 
    :type value_2: str
    '''

    pass


def copy_prev_settings():
    '''Copy settings from previous version 

    '''

    pass


def debug_menu(debug_value: int = 0):
    '''Open a popup to set the debug level 

    :param debug_value: Debug Value 
    :type debug_value: int
    '''

    pass


def dependency_relations():
    '''Print dependency graph relations to the console 

    '''

    pass


def doc_view(doc_id: str = ""):
    '''Load online reference docs 

    :param doc_id: Doc ID 
    :type doc_id: str
    '''

    pass


def doc_view_manual(doc_id: str = ""):
    '''Load online manual 

    :param doc_id: Doc ID 
    :type doc_id: str
    '''

    pass


def doc_view_manual_ui_context():
    '''View a context based online manual in a web browser 

    '''

    pass


def interaction_preset_add(name: str = "", remove_active: bool = False):
    '''Add or remove an Application Interaction Preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: str
    :param remove_active: remove_active 
    :type remove_active: bool
    '''

    pass


def interface_theme_preset_add(name: str = "", remove_active: bool = False):
    '''Add or remove a theme preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: str
    :param remove_active: remove_active 
    :type remove_active: bool
    '''

    pass


def keyconfig_activate(filepath: str = ""):
    '''Undocumented 

    :param filepath: filepath 
    :type filepath: str
    '''

    pass


def keyconfig_export(filepath: str = "keymap.py",
                     filter_folder: bool = True,
                     filter_text: bool = True,
                     filter_python: bool = True):
    '''Export key configuration to a python script 

    :param filepath: filepath 
    :type filepath: str
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_text: Filter text 
    :type filter_text: bool
    :param filter_python: Filter python 
    :type filter_python: bool
    '''

    pass


def keyconfig_import(filepath: str = "keymap.py",
                     filter_folder: bool = True,
                     filter_text: bool = True,
                     filter_python: bool = True,
                     keep_original: bool = True):
    '''Import key configuration from a python script 

    :param filepath: filepath 
    :type filepath: str
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_text: Filter text 
    :type filter_text: bool
    :param filter_python: Filter python 
    :type filter_python: bool
    :param keep_original: Keep original, Keep original file after copying to configuration folder 
    :type keep_original: bool
    '''

    pass


def keyconfig_preset_add(name: str = "", remove_active: bool = False):
    '''Add or remove a Key-config Preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: str
    :param remove_active: remove_active 
    :type remove_active: bool
    '''

    pass


def keyconfig_remove():
    '''Remove key config 

    '''

    pass


def keyconfig_test():
    '''Test key-config for conflicts 

    '''

    pass


def keyitem_add():
    '''Add key map item 

    '''

    pass


def keyitem_remove(item_id: int = 0):
    '''Remove key map item 

    :param item_id: Item Identifier, Identifier of the item to remove 
    :type item_id: int
    '''

    pass


def keyitem_restore(item_id: int = 0):
    '''Restore key map item 

    :param item_id: Item Identifier, Identifier of the item to remove 
    :type item_id: int
    '''

    pass


def keymap_restore(all: bool = False):
    '''Restore key map(s) 

    :param all: All Keymaps, Restore all keymaps to default 
    :type all: bool
    '''

    pass


def lib_reload(library: str = "",
               filepath: str = "",
               directory: str = "",
               filename: str = "",
               filter_blender: bool = True,
               filter_backup: bool = False,
               filter_image: bool = False,
               filter_movie: bool = False,
               filter_python: bool = False,
               filter_font: bool = False,
               filter_sound: bool = False,
               filter_text: bool = False,
               filter_btx: bool = False,
               filter_collada: bool = False,
               filter_alembic: bool = False,
               filter_folder: bool = True,
               filter_blenlib: bool = False,
               filemode: int = 8,
               relative_path: bool = True,
               display_type: int = 'DEFAULT',
               sort_method: int = 'FILE_SORT_ALPHA'):
    '''Reload the given library 

    :param library: Library, Library to reload 
    :type library: str
    :param filepath: File Path, Path to file 
    :type filepath: str
    :param directory: Directory, Directory of the file 
    :type directory: str
    :param filename: File Name, Name of the file 
    :type filename: str
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
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file 
    :type relative_path: bool
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    '''

    pass


def lib_relocate(
        library: str = "",
        filepath: str = "",
        directory: str = "",
        filename: str = "",
        files: typing.List['bpy.types.OperatorFileListElement'] = None,
        filter_blender: bool = True,
        filter_backup: bool = False,
        filter_image: bool = False,
        filter_movie: bool = False,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = False,
        filter_text: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 8,
        relative_path: bool = True,
        display_type: int = 'DEFAULT',
        sort_method: int = 'FILE_SORT_ALPHA'):
    '''Relocate the given library to one or several others 

    :param library: Library, Library to relocate 
    :type library: str
    :param filepath: File Path, Path to file 
    :type filepath: str
    :param directory: Directory, Directory of the file 
    :type directory: str
    :param filename: File Name, Name of the file 
    :type filename: str
    :param files: Files 
    :type files: typing.List['bpy.types.OperatorFileListElement']
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
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file 
    :type relative_path: bool
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    '''

    pass


def link(filepath: str = "",
         directory: str = "",
         filename: str = "",
         files: typing.List['bpy.types.OperatorFileListElement'] = None,
         filter_blender: bool = True,
         filter_backup: bool = False,
         filter_image: bool = False,
         filter_movie: bool = False,
         filter_python: bool = False,
         filter_font: bool = False,
         filter_sound: bool = False,
         filter_text: bool = False,
         filter_btx: bool = False,
         filter_collada: bool = False,
         filter_alembic: bool = False,
         filter_folder: bool = True,
         filter_blenlib: bool = True,
         filemode: int = 1,
         relative_path: bool = True,
         display_type: int = 'DEFAULT',
         sort_method: int = 'FILE_SORT_ALPHA',
         link: bool = True,
         autoselect: bool = True,
         active_layer: bool = True,
         instance_groups: bool = True):
    '''Link from a Library .blend file 

    :param filepath: File Path, Path to file 
    :type filepath: str
    :param directory: Directory, Directory of the file 
    :type directory: str
    :param filename: File Name, Name of the file 
    :type filename: str
    :param files: Files 
    :type files: typing.List['bpy.types.OperatorFileListElement']
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
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file 
    :type relative_path: bool
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    :param link: Link, Link the objects or data-blocks rather than appending 
    :type link: bool
    :param autoselect: Select, Select new objects 
    :type autoselect: bool
    :param active_layer: Active Layer, Put new objects on the active layer 
    :type active_layer: bool
    :param instance_groups: Instance Groups, Create Dupli-Group instances for each group 
    :type instance_groups: bool
    '''

    pass


def memory_statistics():
    '''Print memory statistics to the console 

    '''

    pass


def open_mainfile(filepath: str = "",
                  filter_blender: bool = True,
                  filter_backup: bool = False,
                  filter_image: bool = False,
                  filter_movie: bool = False,
                  filter_python: bool = False,
                  filter_font: bool = False,
                  filter_sound: bool = False,
                  filter_text: bool = False,
                  filter_btx: bool = False,
                  filter_collada: bool = False,
                  filter_alembic: bool = False,
                  filter_folder: bool = True,
                  filter_blenlib: bool = False,
                  filemode: int = 8,
                  display_type: int = 'DEFAULT',
                  sort_method: int = 'FILE_SORT_ALPHA',
                  load_ui: bool = True,
                  use_scripts: bool = True):
    '''Open a Blender file 

    :param filepath: File Path, Path to file 
    :type filepath: str
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
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    :param load_ui: Load UI, Load user interface setup in the .blend file 
    :type load_ui: bool
    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences 
    :type use_scripts: bool
    '''

    pass


def operator_cheat_sheet():
    '''List all the Operators in a text-block, useful for scripting 

    '''

    pass


def operator_defaults():
    '''Set the active operator to its default values 

    '''

    pass


def operator_pie_enum(data_path: str = "", prop_string: str = ""):
    '''Undocumented 

    :param data_path: Operator, Operator name (in python as string) 
    :type data_path: str
    :param prop_string: Property, Property name (as a string) 
    :type prop_string: str
    '''

    pass


def operator_preset_add(name: str = "",
                        remove_active: bool = False,
                        operator: str = ""):
    '''Add or remove an Operator Preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: str
    :param remove_active: remove_active 
    :type remove_active: bool
    :param operator: Operator 
    :type operator: str
    '''

    pass


def path_open(filepath: str = ""):
    '''Open a path in a file browser 

    :param filepath: filepath 
    :type filepath: str
    '''

    pass


def previews_batch_clear(
        files: typing.List['bpy.types.OperatorFileListElement'] = None,
        directory: str = "",
        filter_blender: bool = True,
        filter_folder: bool = True,
        use_scenes: bool = True,
        use_groups: bool = True,
        use_objects: bool = True,
        use_intern_data: bool = True,
        use_trusted: bool = False,
        use_backups: bool = True):
    '''Clear selected .blend file’s previews 

    :param files: files 
    :type files: typing.List['bpy.types.OperatorFileListElement']
    :param directory: directory 
    :type directory: str
    :param filter_blender: filter_blender 
    :type filter_blender: bool
    :param filter_folder: filter_folder 
    :type filter_folder: bool
    :param use_scenes: Scenes, Clear scenes’ previews 
    :type use_scenes: bool
    :param use_groups: Groups, Clear groups’ previews 
    :type use_groups: bool
    :param use_objects: Objects, Clear objects’ previews 
    :type use_objects: bool
    :param use_intern_data: Mat/Tex/…, Clear ‘internal’ previews (materials, textures, images, etc.) 
    :type use_intern_data: bool
    :param use_trusted: Trusted Blend Files, Enable python evaluation for selected files 
    :type use_trusted: bool
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with cleared previews 
    :type use_backups: bool
    '''

    pass


def previews_batch_generate(
        files: typing.List['bpy.types.OperatorFileListElement'] = None,
        directory: str = "",
        filter_blender: bool = True,
        filter_folder: bool = True,
        use_scenes: bool = True,
        use_groups: bool = True,
        use_objects: bool = True,
        use_intern_data: bool = True,
        use_trusted: bool = False,
        use_backups: bool = True):
    '''Generate selected .blend file’s previews 

    :param files: files 
    :type files: typing.List['bpy.types.OperatorFileListElement']
    :param directory: directory 
    :type directory: str
    :param filter_blender: filter_blender 
    :type filter_blender: bool
    :param filter_folder: filter_folder 
    :type filter_folder: bool
    :param use_scenes: Scenes, Generate scenes’ previews 
    :type use_scenes: bool
    :param use_groups: Groups, Generate groups’ previews 
    :type use_groups: bool
    :param use_objects: Objects, Generate objects’ previews 
    :type use_objects: bool
    :param use_intern_data: Mat/Tex/…, Generate ‘internal’ previews (materials, textures, images, etc.) 
    :type use_intern_data: bool
    :param use_trusted: Trusted Blend Files, Enable python evaluation for selected files 
    :type use_trusted: bool
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with generated previews 
    :type use_backups: bool
    '''

    pass


def previews_clear(id_type: typing.Set[int] = {
        'GROUP', 'IMAGE', 'LAMP', 'MATERIAL', 'OBJECT', 'SCENE', 'TEXTURE',
        'WORLD'
}):
    '''Clear data-block previews (only for some types like objects, materials, textures, etc.) 

    :param id_type: Data-Block Type, Which data-block previews to clear 
    :type id_type: typing.Set[int]
    '''

    pass


def previews_ensure():
    '''Ensure data-block previews are available and up-to-date (to be saved in .blend file, only for some types like materials, textures, etc.) 

    '''

    pass


def properties_add(data_path: str = ""):
    '''Undocumented 

    :param data_path: Property Edit, Property data_path edit 
    :type data_path: str
    '''

    pass


def properties_context_change(context: str = ""):
    '''Jump to a different tab inside the properties editor 

    :param context: Context 
    :type context: str
    '''

    pass


def properties_edit(data_path: str = "",
                    property: str = "",
                    value: str = "",
                    min: float = -10000,
                    max: float = 10000.0,
                    use_soft_limits: bool = False,
                    soft_min: float = -10000,
                    soft_max: float = 10000.0,
                    description: str = ""):
    '''Undocumented 

    :param data_path: Property Edit, Property data_path edit 
    :type data_path: str
    :param property: Property Name, Property name edit 
    :type property: str
    :param value: Property Value, Property value edit 
    :type value: str
    :param min: Min 
    :type min: float
    :param max: Max 
    :type max: float
    :param use_soft_limits: Use Soft Limits 
    :type use_soft_limits: bool
    :param soft_min: Min 
    :type soft_min: float
    :param soft_max: Max 
    :type soft_max: float
    :param description: Tooltip 
    :type description: str
    '''

    pass


def properties_remove(data_path: str = "", property: str = ""):
    '''Internal use (edit a property data_path) 

    :param data_path: Property Edit, Property data_path edit 
    :type data_path: str
    :param property: Property Name, Property name edit 
    :type property: str
    '''

    pass


def quit_blender():
    '''Quit Blender 

    '''

    pass


def radial_control(data_path_primary: str = "",
                   data_path_secondary: str = "",
                   use_secondary: str = "",
                   rotation_path: str = "",
                   color_path: str = "",
                   fill_color_path: str = "",
                   fill_color_override_path: str = "",
                   fill_color_override_test_path: str = "",
                   zoom_path: str = "",
                   image_id: str = "",
                   secondary_tex: bool = False):
    '''Set some size property (like e.g. brush size) with mouse wheel 

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
    :type secondary_tex: bool
    '''

    pass


def read_factory_settings(app_template="Template", use_empty: bool = False):
    '''Load default file and user preferences 

    :param use_empty: Empty 
    :type use_empty: bool
    '''

    pass


def read_history():
    '''Reloads history and bookmarks 

    '''

    pass


def read_homefile(filepath: str = "",
                  load_ui: bool = True,
                  use_empty: bool = False,
                  use_splash: bool = False,
                  app_template="Template"):
    '''Open the default file (doesn’t save the current file) 

    :param filepath: File Path, Path to an alternative start-up file 
    :type filepath: str
    :param load_ui: Load UI, Load user interface setup from the .blend file 
    :type load_ui: bool
    :param use_empty: Empty 
    :type use_empty: bool
    :param use_splash: Splash 
    :type use_splash: bool
    '''

    pass


def recover_auto_save(filepath: str = "",
                      filter_blender: bool = True,
                      filter_backup: bool = False,
                      filter_image: bool = False,
                      filter_movie: bool = False,
                      filter_python: bool = False,
                      filter_font: bool = False,
                      filter_sound: bool = False,
                      filter_text: bool = False,
                      filter_btx: bool = False,
                      filter_collada: bool = False,
                      filter_alembic: bool = False,
                      filter_folder: bool = False,
                      filter_blenlib: bool = False,
                      filemode: int = 8,
                      display_type: int = 'LIST_LONG',
                      sort_method: int = 'FILE_SORT_TIME'):
    '''Open an automatically saved file to recover it 

    :param filepath: File Path, Path to file 
    :type filepath: str
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
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    '''

    pass


def recover_last_session():
    '''Open the last closed file (“quit.blend”) 

    '''

    pass


def redraw_timer(type: int = 'DRAW',
                 iterations: int = 10,
                 time_limit: float = 0.0):
    '''Simple redraw timer to test the speed of updating the interface 

    :param type: TypeDRAW Draw Region, Draw Region.DRAW_SWAP Draw Region + Swap, Draw Region and Swap.DRAW_WIN Draw Window, Draw Window.DRAW_WIN_SWAP Draw Window + Swap, Draw Window and Swap.ANIM_STEP Anim Step, Animation Steps.ANIM_PLAY Anim Play, Animation Playback.UNDO Undo/Redo, Undo/Redo. 
    :type type: int
    :param iterations: Iterations, Number of times to redraw 
    :type iterations: int
    :param time_limit: Time Limit, Seconds to run the test for (override iterations) 
    :type time_limit: float
    '''

    pass


def revert_mainfile(use_scripts: bool = True):
    '''Reload the saved file 

    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences 
    :type use_scripts: bool
    '''

    pass


def save_as_mainfile(filepath: str = "",
                     check_existing: bool = True,
                     filter_blender: bool = True,
                     filter_backup: bool = False,
                     filter_image: bool = False,
                     filter_movie: bool = False,
                     filter_python: bool = False,
                     filter_font: bool = False,
                     filter_sound: bool = False,
                     filter_text: bool = False,
                     filter_btx: bool = False,
                     filter_collada: bool = False,
                     filter_alembic: bool = False,
                     filter_folder: bool = True,
                     filter_blenlib: bool = False,
                     filemode: int = 8,
                     display_type: int = 'DEFAULT',
                     sort_method: int = 'FILE_SORT_ALPHA',
                     compress: bool = False,
                     relative_remap: bool = True,
                     copy: bool = False,
                     use_mesh_compat: bool = False):
    '''Save the current file in the desired location 

    :param filepath: File Path, Path to file 
    :type filepath: str
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
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    :param compress: Compress, Write compressed .blend file 
    :type compress: bool
    :param relative_remap: Remap Relative, Remap relative paths when saving in a different directory 
    :type relative_remap: bool
    :param copy: Save Copy, Save a copy of the actual working state but does not make saved file active 
    :type copy: bool
    :param use_mesh_compat: Legacy Mesh Format, Save using legacy mesh format (no ngons) - WARNING: only saves tris and quads, other ngons will be lost (no implicit triangulation) 
    :type use_mesh_compat: bool
    '''

    pass


def save_homefile():
    '''Make the current file the default .blend file, includes preferences 

    '''

    pass


def save_mainfile(filepath: str = "",
                  check_existing: bool = True,
                  filter_blender: bool = True,
                  filter_backup: bool = False,
                  filter_image: bool = False,
                  filter_movie: bool = False,
                  filter_python: bool = False,
                  filter_font: bool = False,
                  filter_sound: bool = False,
                  filter_text: bool = False,
                  filter_btx: bool = False,
                  filter_collada: bool = False,
                  filter_alembic: bool = False,
                  filter_folder: bool = True,
                  filter_blenlib: bool = False,
                  filemode: int = 8,
                  display_type: int = 'DEFAULT',
                  sort_method: int = 'FILE_SORT_ALPHA',
                  compress: bool = False,
                  relative_remap: bool = False):
    '''Save the current Blender file 

    :param filepath: File Path, Path to file 
    :type filepath: str
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
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    :param compress: Compress, Write compressed .blend file 
    :type compress: bool
    :param relative_remap: Remap Relative, Remap relative paths when saving in a different directory 
    :type relative_remap: bool
    '''

    pass


def save_userpref():
    '''Save user preferences separately, overrides startup file preferences 

    '''

    pass


def search_menu():
    '''Pop-up a search menu over all available operators in current context 

    '''

    pass


def set_stereo_3d(display_mode: int = 'ANAGLYPH',
                  anaglyph_type: int = 'RED_CYAN',
                  interlace_type: int = 'ROW_INTERLEAVED',
                  use_interlace_swap: bool = False,
                  use_sidebyside_crosseyed: bool = False):
    '''Toggle 3D stereo support for current window (or change the display mode) 

    :param display_mode: Display ModeANAGLYPH Anaglyph, Render views for left and right eyes as two differently filtered colors in a single image (anaglyph glasses are required).INTERLACE Interlace, Render views for left and right eyes interlaced in a single image (3D-ready monitor is required).TIMESEQUENTIAL Time Sequential, Render alternate eyes (also known as page flip, quad buffer support in the graphic card is required).SIDEBYSIDE Side-by-Side, Render views for left and right eyes side-by-side.TOPBOTTOM Top-Bottom, Render views for left and right eyes one above another. 
    :type display_mode: int
    :param anaglyph_type: Anaglyph Type 
    :type anaglyph_type: int
    :param interlace_type: Interlace Type 
    :type interlace_type: int
    :param use_interlace_swap: Swap Left/Right, Swap left and right stereo channels 
    :type use_interlace_swap: bool
    :param use_sidebyside_crosseyed: Cross-Eyed, Right eye should see left image and vice-versa 
    :type use_sidebyside_crosseyed: bool
    '''

    pass


def splash():
    '''Open the splash screen with release info 

    '''

    pass


def sysinfo(filepath: str = ""):
    '''Generate system information, saved into a text file 

    :param filepath: filepath 
    :type filepath: str
    '''

    pass


def theme_install(overwrite: bool = True,
                  filepath: str = "",
                  filter_folder: bool = True,
                  filter_glob: str = "*.xml"):
    '''Load and apply a Blender XML theme file 

    :param overwrite: Overwrite, Remove existing theme file if exists 
    :type overwrite: bool
    :param filepath: filepath 
    :type filepath: str
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_glob: filter_glob 
    :type filter_glob: str
    '''

    pass


def url_open(url: str = ""):
    '''Open a website in the web-browser 

    :param url: URL, URL to open 
    :type url: str
    '''

    pass


def userpref_autoexec_path_add():
    '''Add path to exclude from autoexecution 

    '''

    pass


def userpref_autoexec_path_remove(index: int = 0):
    '''Remove path to exclude from autoexecution 

    :param index: Index 
    :type index: int
    '''

    pass


def window_close():
    '''Close the current Blender window 

    '''

    pass


def window_duplicate():
    '''Duplicate the current Blender window 

    '''

    pass


def window_fullscreen_toggle():
    '''Toggle the current window fullscreen 

    '''

    pass
