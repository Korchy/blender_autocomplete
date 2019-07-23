import sys
import typing


def autodesk_3ds(filepath: str = "",
                 check_existing: bool = True,
                 axis_forward: int = 'Y',
                 axis_up: int = 'Z',
                 filter_glob: str = "*.3ds",
                 use_selection: bool = False):
    '''Export to 3DS file format (.3ds) 

    :param filepath: File Path, Filepath used for exporting the file 
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: bool
    :param axis_forward: Forward 
    :type axis_forward: int
    :param axis_up: Up 
    :type axis_up: int
    :param filter_glob: filter_glob 
    :type filter_glob: str
    :param use_selection: Selection Only, Export selected objects only 
    :type use_selection: bool
    '''

    pass


def fbx(filepath: str = "",
        check_existing: bool = True,
        axis_forward: int = '-Z',
        axis_up: int = 'Y',
        filter_glob: str = "*.fbx",
        version: int = 'BIN7400',
        ui_tab: int = 'MAIN',
        use_selection: bool = False,
        global_scale: float = 1.0,
        apply_unit_scale: bool = True,
        apply_scale_options: int = 'FBX_SCALE_NONE',
        bake_space_transform: bool = False,
        object_types: typing.Set[int] = {
            'ARMATURE', 'CAMERA', 'EMPTY', 'LAMP', 'MESH', 'OTHER'
        },
        use_mesh_modifiers: bool = True,
        use_mesh_modifiers_render: bool = True,
        mesh_smooth_type: int = 'OFF',
        use_mesh_edges: bool = False,
        use_tspace: bool = False,
        use_custom_props: bool = False,
        add_leaf_bones: bool = True,
        primary_bone_axis: int = 'Y',
        secondary_bone_axis: int = 'X',
        use_armature_deform_only: bool = False,
        armature_nodetype: int = 'NULL',
        bake_anim: bool = True,
        bake_anim_use_all_bones: bool = True,
        bake_anim_use_nla_strips: bool = True,
        bake_anim_use_all_actions: bool = True,
        bake_anim_force_startend_keying: bool = True,
        bake_anim_step: float = 1.0,
        bake_anim_simplify_factor: float = 1.0,
        use_anim: bool = True,
        use_anim_action_all: bool = True,
        use_default_take: bool = True,
        use_anim_optimize: bool = True,
        anim_optimize_precision: float = 6.0,
        path_mode: int = 'AUTO',
        embed_textures: bool = False,
        batch_mode: int = 'OFF',
        use_batch_own_dir: bool = True,
        use_metadata: bool = True):
    '''Write a FBX file 

    :param filepath: File Path, Filepath used for exporting the file 
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: bool
    :param axis_forward: Forward 
    :type axis_forward: int
    :param axis_up: Up 
    :type axis_up: int
    :param filter_glob: filter_glob 
    :type filter_glob: str
    :param version: Version, Choose which version of the exporter to useBIN7400 FBX 7.4 binary, Modern 7.4 binary version.ASCII6100 FBX 6.1 ASCII, Legacy 6.1 ascii version - WARNING: Deprecated and no more maintained. 
    :type version: int
    :param ui_tab: ui_tab, Export options categoriesMAIN Main, Main basic settings.GEOMETRY Geometries, Geometry-related settings.ARMATURE Armatures, Armature-related settings.ANIMATION Animation, Animation-related settings. 
    :type ui_tab: int
    :param use_selection: Selected Objects, Export selected objects on visible layers 
    :type use_selection: bool
    :param global_scale: Scale, Scale all data (Some importers do not support scaled armatures!) 
    :type global_scale: float
    :param apply_unit_scale: Apply Unit, Take into account current Blender units settings (if unset, raw Blender Units values are used as-is) 
    :type apply_unit_scale: bool
    :param apply_scale_options: Apply Scalings, How to apply custom and units scalings in generated FBX file (Blender uses FBX scale to detect units on import, but many other applications do not handle the same way)FBX_SCALE_NONE All Local, Apply custom scaling and units scaling to each object transformation, FBX scale remains at 1.0.FBX_SCALE_UNITS FBX Units Scale, Apply custom scaling to each object transformation, and units scaling to FBX scale.FBX_SCALE_CUSTOM FBX Custom Scale, Apply custom scaling to FBX scale, and units scaling to each object transformation.FBX_SCALE_ALL FBX All, Apply custom scaling and units scaling to FBX scale. 
    :type apply_scale_options: int
    :param bake_space_transform: !EXPERIMENTAL! Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender’s space (WARNING! experimental option, use at own risks, known broken with armatures/animations) 
    :type bake_space_transform: bool
    :param object_types: Object Types, Which kind of object to exportEMPTY Empty.CAMERA Camera.LAMP Lamp.ARMATURE Armature, WARNING: not supported in dupli/group instances.MESH Mesh.OTHER Other, Other geometry types, like curve, metaball, etc. (converted to meshes). 
    :type object_types: typing.Set[int]
    :param use_mesh_modifiers: Apply Modifiers, Apply modifiers to mesh objects (except Armature ones) - WARNING: prevents exporting shape keys 
    :type use_mesh_modifiers: bool
    :param use_mesh_modifiers_render: Use Modifiers Render Setting, Use render settings when applying modifiers to mesh objects 
    :type use_mesh_modifiers_render: bool
    :param mesh_smooth_type: Smoothing, Export smoothing information (prefer ‘Normals Only’ option if your target importer understand split normals)OFF Normals Only, Export only normals instead of writing edge or face smoothing data.FACE Face, Write face smoothing.EDGE Edge, Write edge smoothing. 
    :type mesh_smooth_type: int
    :param use_mesh_edges: Loose Edges, Export loose edges (as two-vertices polygons) 
    :type use_mesh_edges: bool
    :param use_tspace: Tangent Space, Add binormal and tangent vectors, together with normal they form the tangent space (will only work correctly with tris/quads only meshes!) 
    :type use_tspace: bool
    :param use_custom_props: Custom Properties, Export custom properties 
    :type use_custom_props: bool
    :param add_leaf_bones: Add Leaf Bones, Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data) 
    :type add_leaf_bones: bool
    :param primary_bone_axis: Primary Bone Axis 
    :type primary_bone_axis: int
    :param secondary_bone_axis: Secondary Bone Axis 
    :type secondary_bone_axis: int
    :param use_armature_deform_only: Only Deform Bones, Only write deforming bones (and non-deforming ones when they have deforming children) 
    :type use_armature_deform_only: bool
    :param armature_nodetype: Armature FBXNode Type, FBX type of node (object) used to represent Blender’s armatures (use Null one unless you experience issues with other app, other choices may no import back perfectly in Blender…)NULL Null, ‘Null’ FBX node, similar to Blender’s Empty (default).ROOT Root, ‘Root’ FBX node, supposed to be the root of chains of bones….LIMBNODE LimbNode, ‘LimbNode’ FBX node, a regular joint between two bones…. 
    :type armature_nodetype: int
    :param bake_anim: Baked Animation, Export baked keyframe animation 
    :type bake_anim: bool
    :param bake_anim_use_all_bones: Key All Bones, Force exporting at least one key of animation for all bones (needed with some target applications, like UE4) 
    :type bake_anim_use_all_bones: bool
    :param bake_anim_use_nla_strips: NLA Strips, Export each non-muted NLA strip as a separated FBX’s AnimStack, if any, instead of global scene animation 
    :type bake_anim_use_nla_strips: bool
    :param bake_anim_use_all_actions: All Actions, Export each action as a separated FBX’s AnimStack, instead of global scene animation (note that animated objects will get all actions compatible with them, others will get no animation at all) 
    :type bake_anim_use_all_actions: bool
    :param bake_anim_force_startend_keying: Force Start/End Keying, Always add a keyframe at start and end of actions for animated channels 
    :type bake_anim_force_startend_keying: bool
    :param bake_anim_step: Sampling Rate, How often to evaluate animated values (in frames) 
    :type bake_anim_step: float
    :param bake_anim_simplify_factor: Simplify, How much to simplify baked values (0.0 to disable, the higher the more simplified) 
    :type bake_anim_simplify_factor: float
    :param use_anim: Animation, Export keyframe animation 
    :type use_anim: bool
    :param use_anim_action_all: All Actions, Export all actions for armatures or just the currently selected action 
    :type use_anim_action_all: bool
    :param use_default_take: Default Take, Export currently assigned object and armature animations into a default take from the scene start/end frames 
    :type use_default_take: bool
    :param use_anim_optimize: Optimize Keyframes, Remove double keyframes 
    :type use_anim_optimize: bool
    :param anim_optimize_precision: Precision, Tolerance for comparing double keyframes (higher for greater accuracy) 
    :type anim_optimize_precision: float
    :param path_mode: Path Mode, Method used to reference pathsAUTO Auto, Use Relative paths with subdirectories only.ABSOLUTE Absolute, Always write absolute paths.RELATIVE Relative, Always write relative paths (where possible).MATCH Match, Match Absolute/Relative setting with input path.STRIP Strip Path, Filename only.COPY Copy, Copy the file to the destination path (or subdirectory). 
    :type path_mode: int
    :param embed_textures: Embed Textures, Embed textures in FBX binary file (only for “Copy” path mode!) 
    :type embed_textures: bool
    :param batch_mode: Batch ModeOFF Off, Active scene to file.SCENE Scene, Each scene as a file.GROUP Group, Each group as a file. 
    :type batch_mode: int
    :param use_batch_own_dir: Batch Own Dir, Create a dir for each exported file 
    :type use_batch_own_dir: bool
    :param use_metadata: Use Metadata 
    :type use_metadata: bool
    '''

    pass


def obj(filepath: str = "",
        check_existing: bool = True,
        axis_forward: int = '-Z',
        axis_up: int = 'Y',
        filter_glob: str = "*.obj;*.mtl",
        use_selection: bool = False,
        use_animation: bool = False,
        use_mesh_modifiers: bool = True,
        use_mesh_modifiers_render: bool = False,
        use_edges: bool = True,
        use_smooth_groups: bool = False,
        use_smooth_groups_bitflags: bool = False,
        use_normals: bool = True,
        use_uvs: bool = True,
        use_materials: bool = True,
        use_triangles: bool = False,
        use_nurbs: bool = False,
        use_vertex_groups: bool = False,
        use_blen_objects: bool = True,
        group_by_object: bool = False,
        group_by_material: bool = False,
        keep_vertex_order: bool = False,
        global_scale: float = 1.0,
        path_mode: int = 'AUTO'):
    '''Save a Wavefront OBJ File 

    :param filepath: File Path, Filepath used for exporting the file 
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: bool
    :param axis_forward: Forward 
    :type axis_forward: int
    :param axis_up: Up 
    :type axis_up: int
    :param filter_glob: filter_glob 
    :type filter_glob: str
    :param use_selection: Selection Only, Export selected objects only 
    :type use_selection: bool
    :param use_animation: Animation, Write out an OBJ for each frame 
    :type use_animation: bool
    :param use_mesh_modifiers: Apply Modifiers, Apply modifiers 
    :type use_mesh_modifiers: bool
    :param use_mesh_modifiers_render: Use Modifiers Render Settings, Use render settings when applying modifiers to mesh objects 
    :type use_mesh_modifiers_render: bool
    :param use_edges: Include Edges 
    :type use_edges: bool
    :param use_smooth_groups: Smooth Groups, Write sharp edges as smooth groups 
    :type use_smooth_groups: bool
    :param use_smooth_groups_bitflags: Bitflag Smooth Groups, Same as ‘Smooth Groups’, but generate smooth groups IDs as bitflags (produces at most 32 different smooth groups, usually much less) 
    :type use_smooth_groups_bitflags: bool
    :param use_normals: Write Normals, Export one normal per vertex and per face, to represent flat faces and sharp edges 
    :type use_normals: bool
    :param use_uvs: Include UVs, Write out the active UV coordinates 
    :type use_uvs: bool
    :param use_materials: Write Materials, Write out the MTL file 
    :type use_materials: bool
    :param use_triangles: Triangulate Faces, Convert all faces to triangles 
    :type use_triangles: bool
    :param use_nurbs: Write Nurbs, Write nurbs curves as OBJ nurbs rather than converting to geometry 
    :type use_nurbs: bool
    :param use_vertex_groups: Polygroups 
    :type use_vertex_groups: bool
    :param use_blen_objects: Objects as OBJ Objects 
    :type use_blen_objects: bool
    :param group_by_object: Objects as OBJ Groups 
    :type group_by_object: bool
    :param group_by_material: Material Groups 
    :type group_by_material: bool
    :param keep_vertex_order: Keep Vertex Order 
    :type keep_vertex_order: bool
    :param global_scale: Scale 
    :type global_scale: float
    :param path_mode: Path Mode, Method used to reference pathsAUTO Auto, Use Relative paths with subdirectories only.ABSOLUTE Absolute, Always write absolute paths.RELATIVE Relative, Always write relative paths (where possible).MATCH Match, Match Absolute/Relative setting with input path.STRIP Strip Path, Filename only.COPY Copy, Copy the file to the destination path (or subdirectory). 
    :type path_mode: int
    '''

    pass


def x3d(filepath: str = "",
        check_existing: bool = True,
        axis_forward: int = 'Z',
        axis_up: int = 'Y',
        filter_glob: str = "*.x3d",
        use_selection: bool = False,
        use_mesh_modifiers: bool = True,
        use_triangulate: bool = False,
        use_normals: bool = False,
        use_compress: bool = False,
        use_hierarchy: bool = True,
        name_decorations: bool = True,
        use_h3d: bool = False,
        global_scale: float = 1.0,
        path_mode: int = 'AUTO'):
    '''Export selection to Extensible 3D file (.x3d) 

    :param filepath: File Path, Filepath used for exporting the file 
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: bool
    :param axis_forward: Forward 
    :type axis_forward: int
    :param axis_up: Up 
    :type axis_up: int
    :param filter_glob: filter_glob 
    :type filter_glob: str
    :param use_selection: Selection Only, Export selected objects only 
    :type use_selection: bool
    :param use_mesh_modifiers: Apply Modifiers, Use transformed mesh data from each object 
    :type use_mesh_modifiers: bool
    :param use_triangulate: Triangulate, Write quads into ‘IndexedTriangleSet’ 
    :type use_triangulate: bool
    :param use_normals: Normals, Write normals with geometry 
    :type use_normals: bool
    :param use_compress: Compress, Compress the exported file 
    :type use_compress: bool
    :param use_hierarchy: Hierarchy, Export parent child relationships 
    :type use_hierarchy: bool
    :param name_decorations: Name decorations, Add prefixes to the names of exported nodes to indicate their type 
    :type name_decorations: bool
    :param use_h3d: H3D Extensions, Export shaders for H3D 
    :type use_h3d: bool
    :param global_scale: Scale 
    :type global_scale: float
    :param path_mode: Path Mode, Method used to reference pathsAUTO Auto, Use Relative paths with subdirectories only.ABSOLUTE Absolute, Always write absolute paths.RELATIVE Relative, Always write relative paths (where possible).MATCH Match, Match Absolute/Relative setting with input path.STRIP Strip Path, Filename only.COPY Copy, Copy the file to the destination path (or subdirectory). 
    :type path_mode: int
    '''

    pass
