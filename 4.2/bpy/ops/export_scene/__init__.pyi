import typing
import collections.abc
import typing_extensions
import bpy.types

def fbx(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
    filter_glob: str = "*.fbx",
    use_selection: bool | None = False,
    use_visible: bool | None = False,
    use_active_collection: bool | None = False,
    collection: str = "",
    global_scale: float | None = 1.0,
    apply_unit_scale: bool | None = True,
    apply_scale_options: typing.Literal[
        "FBX_SCALE_NONE", "FBX_SCALE_UNITS", "FBX_SCALE_CUSTOM", "FBX_SCALE_ALL"
    ]
    | None = "FBX_SCALE_NONE",
    use_space_transform: bool | None = True,
    bake_space_transform: bool | None = False,
    object_types: set[
        typing.Literal["EMPTY", "CAMERA", "LIGHT", "ARMATURE", "MESH", "OTHER"]
    ]
    | None = {"ARMATURE", "CAMERA", "EMPTY", "LIGHT", "MESH", "OTHER"},
    use_mesh_modifiers: bool | None = True,
    use_mesh_modifiers_render: bool | None = True,
    mesh_smooth_type: typing.Literal["OFF", "FACE", "EDGE"] | None = "OFF",
    colors_type: typing.Literal["NONE", "SRGB", "LINEAR"] | None = "SRGB",
    prioritize_active_color: bool | None = False,
    use_subsurf: bool | None = False,
    use_mesh_edges: bool | None = False,
    use_tspace: bool | None = False,
    use_triangles: bool | None = False,
    use_custom_props: bool | None = False,
    add_leaf_bones: bool | None = True,
    primary_bone_axis: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
    secondary_bone_axis: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "X",
    use_armature_deform_only: bool | None = False,
    armature_nodetype: typing.Literal["NULL", "ROOT", "LIMBNODE"] | None = "NULL",
    bake_anim: bool | None = True,
    bake_anim_use_all_bones: bool | None = True,
    bake_anim_use_nla_strips: bool | None = True,
    bake_anim_use_all_actions: bool | None = True,
    bake_anim_force_startend_keying: bool | None = True,
    bake_anim_step: float | None = 1.0,
    bake_anim_simplify_factor: float | None = 1.0,
    path_mode: typing.Literal["AUTO", "ABSOLUTE", "RELATIVE", "MATCH", "STRIP", "COPY"]
    | None = "AUTO",
    embed_textures: bool | None = False,
    batch_mode: typing.Literal[
        "OFF", "SCENE", "COLLECTION", "SCENE_COLLECTION", "ACTIVE_SCENE_COLLECTION"
    ]
    | None = "OFF",
    use_batch_own_dir: bool | None = True,
    use_metadata: bool | None = True,
    axis_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "-Z",
    axis_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
):
    """Write a FBX file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Filepath used for exporting the file
        :type filepath: str
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_glob: filter_glob
        :type filter_glob: str
        :param use_selection: Selected Objects, Export selected and visible objects only
        :type use_selection: bool | None
        :param use_visible: Visible Objects, Export visible objects only
        :type use_visible: bool | None
        :param use_active_collection: Active Collection, Export only objects from the active collection (and its children)
        :type use_active_collection: bool | None
        :param collection: Source Collection, Export only objects from this collection (and its children)
        :type collection: str
        :param global_scale: Scale, Scale all data (Some importers do not support scaled armatures!)
        :type global_scale: float | None
        :param apply_unit_scale: Apply Unit, Take into account current Blender units settings (if unset, raw Blender Units values are used as-is)
        :type apply_unit_scale: bool | None
        :param apply_scale_options: Apply Scalings, How to apply custom and units scalings in generated FBX file (Blender uses FBX scale to detect units on import, but many other applications do not handle the same way)

    FBX_SCALE_NONE
    All Local -- Apply custom scaling and units scaling to each object transformation, FBX scale remains at 1.0.

    FBX_SCALE_UNITS
    FBX Units Scale -- Apply custom scaling to each object transformation, and units scaling to FBX scale.

    FBX_SCALE_CUSTOM
    FBX Custom Scale -- Apply custom scaling to FBX scale, and units scaling to each object transformation.

    FBX_SCALE_ALL
    FBX All -- Apply custom scaling and units scaling to FBX scale.
        :type apply_scale_options: typing.Literal['FBX_SCALE_NONE','FBX_SCALE_UNITS','FBX_SCALE_CUSTOM','FBX_SCALE_ALL'] | None
        :param use_space_transform: Use Space Transform, Apply global space transform to the object rotations. When disabled only the axis space is written to the file and all object transforms are left as-is
        :type use_space_transform: bool | None
        :param bake_space_transform: Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risk, known to be broken with armatures/animations)
        :type bake_space_transform: bool | None
        :param object_types: Object Types, Which kind of object to export

    EMPTY
    Empty.

    CAMERA
    Camera.

    LIGHT
    Lamp.

    ARMATURE
    Armature -- WARNING: not supported in dupli/group instances.

    MESH
    Mesh.

    OTHER
    Other -- Other geometry types, like curve, metaball, etc. (converted to meshes).
        :type object_types: set[typing.Literal['EMPTY','CAMERA','LIGHT','ARMATURE','MESH','OTHER']] | None
        :param use_mesh_modifiers: Apply Modifiers, Apply modifiers to mesh objects (except Armature ones) - WARNING: prevents exporting shape keys
        :type use_mesh_modifiers: bool | None
        :param use_mesh_modifiers_render: Use Modifiers Render Setting, Use render settings when applying modifiers to mesh objects (DISABLED in Blender 2.8)
        :type use_mesh_modifiers_render: bool | None
        :param mesh_smooth_type: Smoothing, Export smoothing information (prefer 'Normals Only' option if your target importer understand split normals)

    OFF
    Normals Only -- Export only normals instead of writing edge or face smoothing data.

    FACE
    Face -- Write face smoothing.

    EDGE
    Edge -- Write edge smoothing.
        :type mesh_smooth_type: typing.Literal['OFF','FACE','EDGE'] | None
        :param colors_type: Vertex Colors, Export vertex color attributes

    NONE
    None -- Do not export color attributes.

    SRGB
    sRGB -- Export colors in sRGB color space.

    LINEAR
    Linear -- Export colors in linear color space.
        :type colors_type: typing.Literal['NONE','SRGB','LINEAR'] | None
        :param prioritize_active_color: Prioritize Active Color, Make sure active color will be exported first. Could be important since some other software can discard other color attributes besides the first one
        :type prioritize_active_color: bool | None
        :param use_subsurf: Export Subdivision Surface, Export the last Catmull-Rom subdivision modifier as FBX subdivision (does not apply the modifier even if 'Apply Modifiers' is enabled)
        :type use_subsurf: bool | None
        :param use_mesh_edges: Loose Edges, Export loose edges (as two-vertices polygons)
        :type use_mesh_edges: bool | None
        :param use_tspace: Tangent Space, Add binormal and tangent vectors, together with normal they form the tangent space (will only work correctly with tris/quads only meshes!)
        :type use_tspace: bool | None
        :param use_triangles: Triangulate Faces, Convert all faces to triangles
        :type use_triangles: bool | None
        :param use_custom_props: Custom Properties, Export custom properties
        :type use_custom_props: bool | None
        :param add_leaf_bones: Add Leaf Bones, Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data)
        :type add_leaf_bones: bool | None
        :param primary_bone_axis: Primary Bone Axis
        :type primary_bone_axis: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param secondary_bone_axis: Secondary Bone Axis
        :type secondary_bone_axis: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param use_armature_deform_only: Only Deform Bones, Only write deforming bones (and non-deforming ones when they have deforming children)
        :type use_armature_deform_only: bool | None
        :param armature_nodetype: Armature FBXNode Type, FBX type of node (object) used to represent Blender's armatures (use the Null type unless you experience issues with the other app, as other choices may not import back perfectly into Blender...)

    NULL
    Null -- 'Null' FBX node, similar to Blender's Empty (default).

    ROOT
    Root -- 'Root' FBX node, supposed to be the root of chains of bones....

    LIMBNODE
    LimbNode -- 'LimbNode' FBX node, a regular joint between two bones....
        :type armature_nodetype: typing.Literal['NULL','ROOT','LIMBNODE'] | None
        :param bake_anim: Baked Animation, Export baked keyframe animation
        :type bake_anim: bool | None
        :param bake_anim_use_all_bones: Key All Bones, Force exporting at least one key of animation for all bones (needed with some target applications, like UE4)
        :type bake_anim_use_all_bones: bool | None
        :param bake_anim_use_nla_strips: NLA Strips, Export each non-muted NLA strip as a separated FBX's AnimStack, if any, instead of global scene animation
        :type bake_anim_use_nla_strips: bool | None
        :param bake_anim_use_all_actions: All Actions, Export each action as a separated FBX's AnimStack, instead of global scene animation (note that animated objects will get all actions compatible with them, others will get no animation at all)
        :type bake_anim_use_all_actions: bool | None
        :param bake_anim_force_startend_keying: Force Start/End Keying, Always add a keyframe at start and end of actions for animated channels
        :type bake_anim_force_startend_keying: bool | None
        :param bake_anim_step: Sampling Rate, How often to evaluate animated values (in frames)
        :type bake_anim_step: float | None
        :param bake_anim_simplify_factor: Simplify, How much to simplify baked values (0.0 to disable, the higher the more simplified)
        :type bake_anim_simplify_factor: float | None
        :param path_mode: Path Mode, Method used to reference paths

    AUTO
    Auto -- Use relative paths with subdirectories only.

    ABSOLUTE
    Absolute -- Always write absolute paths.

    RELATIVE
    Relative -- Always write relative paths (where possible).

    MATCH
    Match -- Match absolute/relative setting with input path.

    STRIP
    Strip Path -- Filename only.

    COPY
    Copy -- Copy the file to the destination path (or subdirectory).
        :type path_mode: typing.Literal['AUTO','ABSOLUTE','RELATIVE','MATCH','STRIP','COPY'] | None
        :param embed_textures: Embed Textures, Embed textures in FBX binary file (only for "Copy" path mode!)
        :type embed_textures: bool | None
        :param batch_mode: Batch Mode

    OFF
    Off -- Active scene to file.

    SCENE
    Scene -- Each scene as a file.

    COLLECTION
    Collection -- Each collection (data-block ones) as a file, does not include content of children collections.

    SCENE_COLLECTION
    Scene Collections -- Each collection (including master, non-data-block ones) of each scene as a file, including content from children collections.

    ACTIVE_SCENE_COLLECTION
    Active Scene Collections -- Each collection (including master, non-data-block one) of the active scene as a file, including content from children collections.
        :type batch_mode: typing.Literal['OFF','SCENE','COLLECTION','SCENE_COLLECTION','ACTIVE_SCENE_COLLECTION'] | None
        :param use_batch_own_dir: Batch Own Dir, Create a dir for each exported file
        :type use_batch_own_dir: bool | None
        :param use_metadata: Use Metadata
        :type use_metadata: bool | None
        :param axis_forward: Forward
        :type axis_forward: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param axis_up: Up
        :type axis_up: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
    """

def gltf(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
    export_import_convert_lighting_mode: typing.Literal["SPEC", "COMPAT", "RAW"]
    | None = "SPEC",
    gltf_export_id: str = "",
    export_use_gltfpack: bool | None = False,
    export_gltfpack_tc: bool | None = True,
    export_gltfpack_tq: int | None = 8,
    export_gltfpack_si: float | None = 1.0,
    export_gltfpack_sa: bool | None = False,
    export_gltfpack_slb: bool | None = False,
    export_gltfpack_vp: int | None = 14,
    export_gltfpack_vt: int | None = 12,
    export_gltfpack_vn: int | None = 8,
    export_gltfpack_vc: int | None = 8,
    export_gltfpack_vpi: typing.Literal["Integer", "Normalized", "Floating-point"]
    | None = "Integer",
    export_gltfpack_noq: bool | None = True,
    export_format: str | None = "",
    ui_tab: typing.Literal["GENERAL", "MESHES", "OBJECTS", "ANIMATION"]
    | None = "GENERAL",
    export_copyright: str = "",
    export_image_format: typing.Literal["AUTO", "JPEG", "WEBP", "NONE"] | None = "AUTO",
    export_image_add_webp: bool | None = False,
    export_image_webp_fallback: bool | None = False,
    export_texture_dir: str = "",
    export_jpeg_quality: int | None = 75,
    export_image_quality: int | None = 75,
    export_keep_originals: bool | None = False,
    export_texcoords: bool | None = True,
    export_normals: bool | None = True,
    export_gn_mesh: bool | None = False,
    export_draco_mesh_compression_enable: bool | None = False,
    export_draco_mesh_compression_level: int | None = 6,
    export_draco_position_quantization: int | None = 14,
    export_draco_normal_quantization: int | None = 10,
    export_draco_texcoord_quantization: int | None = 12,
    export_draco_color_quantization: int | None = 10,
    export_draco_generic_quantization: int | None = 12,
    export_tangents: bool | None = False,
    export_materials: typing.Literal["EXPORT", "PLACEHOLDER", "NONE"] | None = "EXPORT",
    export_unused_images: bool | None = False,
    export_unused_textures: bool | None = False,
    export_vertex_color: typing.Literal["MATERIAL", "ACTIVE", "NONE"]
    | None = "MATERIAL",
    export_all_vertex_colors: bool | None = True,
    export_active_vertex_color_when_no_material: bool | None = True,
    export_attributes: bool | None = False,
    use_mesh_edges: bool | None = False,
    use_mesh_vertices: bool | None = False,
    export_cameras: bool | None = False,
    use_selection: bool | None = False,
    use_visible: bool | None = False,
    use_renderable: bool | None = False,
    use_active_collection_with_nested: bool | None = True,
    use_active_collection: bool | None = False,
    use_active_scene: bool | None = False,
    collection: str = "",
    at_collection_center: bool | None = False,
    export_extras: bool | None = False,
    export_yup: bool | None = True,
    export_apply: bool | None = False,
    export_shared_accessors: bool | None = False,
    export_animations: bool | None = True,
    export_frame_range: bool | None = False,
    export_frame_step: int | None = 1,
    export_force_sampling: bool | None = True,
    export_pointer_animation: bool | None = False,
    export_animation_mode: typing.Literal[
        "ACTIONS", "ACTIVE_ACTIONS", "BROADCAST", "NLA_TRACKS", "SCENE"
    ]
    | None = "ACTIONS",
    export_nla_strips_merged_animation_name: str = "Animation",
    export_def_bones: bool | None = False,
    export_hierarchy_flatten_bones: bool | None = False,
    export_hierarchy_flatten_objs: bool | None = False,
    export_armature_object_remove: bool | None = False,
    export_leaf_bone: bool | None = False,
    export_optimize_animation_size: bool | None = True,
    export_optimize_animation_keep_anim_armature: bool | None = True,
    export_optimize_animation_keep_anim_object: bool | None = False,
    export_optimize_disable_viewport: bool | None = False,
    export_negative_frame: typing.Literal["SLIDE", "CROP"] | None = "SLIDE",
    export_anim_slide_to_zero: bool | None = False,
    export_bake_animation: bool | None = False,
    export_anim_single_armature: bool | None = True,
    export_reset_pose_bones: bool | None = True,
    export_current_frame: bool | None = False,
    export_rest_position_armature: bool | None = True,
    export_anim_scene_split_object: bool | None = True,
    export_skins: bool | None = True,
    export_influence_nb: int | None = 4,
    export_all_influences: bool | None = False,
    export_morph: bool | None = True,
    export_morph_normal: bool | None = True,
    export_morph_tangent: bool | None = False,
    export_morph_animation: bool | None = True,
    export_morph_reset_sk_data: bool | None = True,
    export_lights: bool | None = False,
    export_try_sparse_sk: bool | None = True,
    export_try_omit_sparse_sk: bool | None = False,
    export_gpu_instances: bool | None = False,
    export_action_filter: bool | None = False,
    export_convert_animation_pointer: bool | None = False,
    export_nla_strips: bool | None = True,
    export_original_specular: bool | None = False,
    will_save_settings: bool | None = False,
    export_hierarchy_full_collections: bool | None = False,
    export_extra_animations: bool | None = False,
    filter_glob: str = "*.glb",
):
    """Export scene as glTF 2.0 file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Filepath used for exporting the file
        :type filepath: str
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param export_import_convert_lighting_mode: Lighting Mode, Optional backwards compatibility for non-standard render engines. Applies to lights

    SPEC
    Standard -- Physically-based glTF lighting units (cd, lx, nt).

    COMPAT
    Unitless -- Non-physical, unitless lighting. Useful when exposure controls are not available.

    RAW
    Raw (Deprecated) -- Blender lighting strengths with no conversion.
        :type export_import_convert_lighting_mode: typing.Literal['SPEC','COMPAT','RAW'] | None
        :param gltf_export_id: Identifier, Identifier of caller (in case of add-on calling this exporter). Can be useful in case of Extension added by other add-ons
        :type gltf_export_id: str
        :param export_use_gltfpack: Use Gltfpack, Use gltfpack to simplify the mesh and/or compress its textures
        :type export_use_gltfpack: bool | None
        :param export_gltfpack_tc: KTX2 Compression, Convert all textures to KTX2 with BasisU supercompression
        :type export_gltfpack_tc: bool | None
        :param export_gltfpack_tq: Texture Encoding Quality, Texture encoding quality
        :type export_gltfpack_tq: int | None
        :param export_gltfpack_si: Mesh Simplification Ratio, Simplify meshes targeting triangle count ratio
        :type export_gltfpack_si: float | None
        :param export_gltfpack_sa: Aggressive Mesh Simplification, Aggressively simplify to the target ratio disregarding quality
        :type export_gltfpack_sa: bool | None
        :param export_gltfpack_slb: Lock Mesh Border Vertices, Lock border vertices during simplification to avoid gaps on connected meshes
        :type export_gltfpack_slb: bool | None
        :param export_gltfpack_vp: Position Quantization, Use N-bit quantization for positions
        :type export_gltfpack_vp: int | None
        :param export_gltfpack_vt: Texture Coordinate Quantization, Use N-bit quantization for texture coordinates
        :type export_gltfpack_vt: int | None
        :param export_gltfpack_vn: Normal/Tangent Quantization, Use N-bit quantization for normals and tangents
        :type export_gltfpack_vn: int | None
        :param export_gltfpack_vc: Vertex Color Quantization, Use N-bit quantization for colors
        :type export_gltfpack_vc: int | None
        :param export_gltfpack_vpi: Vertex Position Attributes, Type to use for vertex position attributes

    Integer
    Integer -- Use integer attributes for positions.

    Normalized
    Normalized -- Use normalized attributes for positions.

    Floating-point
    Floating-point -- Use floating-point attributes for positions.
        :type export_gltfpack_vpi: typing.Literal['Integer','Normalized','Floating-point'] | None
        :param export_gltfpack_noq: Disable Quantization, Disable quantization; produces much larger glTF files with no extensions
        :type export_gltfpack_noq: bool | None
        :param export_format: Format, Output format. Binary is most efficient, but JSON may be easier to edit later
        :type export_format: str | None
        :param ui_tab: ui_tab, Export setting categories

    GENERAL
    General -- General settings.

    MESHES
    Meshes -- Mesh settings.

    OBJECTS
    Objects -- Object settings.

    ANIMATION
    Animation -- Animation settings.
        :type ui_tab: typing.Literal['GENERAL','MESHES','OBJECTS','ANIMATION'] | None
        :param export_copyright: Copyright, Legal rights and conditions for the model
        :type export_copyright: str
        :param export_image_format: Images, Output format for images. PNG is lossless and generally preferred, but JPEG might be preferable for web applications due to the smaller file size. Alternatively they can be omitted if they are not needed

    AUTO
    Automatic -- Save PNGs as PNGs, JPEGs as JPEGs, WebPs as WebPs. For other formats, use PNG.

    JPEG
    JPEG Format (.jpg) -- Save images as JPEGs. (Images that need alpha are saved as PNGs though.) Be aware of a possible loss in quality.

    WEBP
    WebP Format -- Save images as WebPs as main image (no fallback).

    NONE
    None -- Don't export images.
        :type export_image_format: typing.Literal['AUTO','JPEG','WEBP','NONE'] | None
        :param export_image_add_webp: Create WebP, Creates WebP textures for every texture. For already WebP textures, nothing happens
        :type export_image_add_webp: bool | None
        :param export_image_webp_fallback: WebP fallback, For all WebP textures, create a PNG fallback texture
        :type export_image_webp_fallback: bool | None
        :param export_texture_dir: Textures, Folder to place texture files in. Relative to the .gltf file
        :type export_texture_dir: str
        :param export_jpeg_quality: JPEG quality, Quality of JPEG export
        :type export_jpeg_quality: int | None
        :param export_image_quality: Image quality, Quality of image export
        :type export_image_quality: int | None
        :param export_keep_originals: Keep original, Keep original textures files if possible. WARNING: if you use more than one texture, where pbr standard requires only one, only one texture will be used. This can lead to unexpected results
        :type export_keep_originals: bool | None
        :param export_texcoords: UVs, Export UVs (texture coordinates) with meshes
        :type export_texcoords: bool | None
        :param export_normals: Normals, Export vertex normals with meshes
        :type export_normals: bool | None
        :param export_gn_mesh: Geometry Nodes Instances (Experimental), Export Geometry nodes instance meshes
        :type export_gn_mesh: bool | None
        :param export_draco_mesh_compression_enable: Draco mesh compression, Compress mesh using Draco
        :type export_draco_mesh_compression_enable: bool | None
        :param export_draco_mesh_compression_level: Compression level, Compression level (0 = most speed, 6 = most compression, higher values currently not supported)
        :type export_draco_mesh_compression_level: int | None
        :param export_draco_position_quantization: Position quantization bits, Quantization bits for position values (0 = no quantization)
        :type export_draco_position_quantization: int | None
        :param export_draco_normal_quantization: Normal quantization bits, Quantization bits for normal values (0 = no quantization)
        :type export_draco_normal_quantization: int | None
        :param export_draco_texcoord_quantization: Texcoord quantization bits, Quantization bits for texture coordinate values (0 = no quantization)
        :type export_draco_texcoord_quantization: int | None
        :param export_draco_color_quantization: Color quantization bits, Quantization bits for color values (0 = no quantization)
        :type export_draco_color_quantization: int | None
        :param export_draco_generic_quantization: Generic quantization bits, Quantization bits for generic values like weights or joints (0 = no quantization)
        :type export_draco_generic_quantization: int | None
        :param export_tangents: Tangents, Export vertex tangents with meshes
        :type export_tangents: bool | None
        :param export_materials: Materials, Export materials

    EXPORT
    Export -- Export all materials used by included objects.

    PLACEHOLDER
    Placeholder -- Do not export materials, but write multiple primitive groups per mesh, keeping material slot information.

    NONE
    No export -- Do not export materials, and combine mesh primitive groups, losing material slot information.
        :type export_materials: typing.Literal['EXPORT','PLACEHOLDER','NONE'] | None
        :param export_unused_images: Unused images, Export images not assigned to any material
        :type export_unused_images: bool | None
        :param export_unused_textures: Prepare Unused textures, Export image texture nodes not assigned to any material. This feature is not standard and needs an external extension to be included in the glTF file
        :type export_unused_textures: bool | None
        :param export_vertex_color: Use Vertex Color, How to export vertex color

    MATERIAL
    Material -- Export vertex color when used by material.

    ACTIVE
    Active -- Export active vertex color.

    NONE
    None -- Do not export vertex color.
        :type export_vertex_color: typing.Literal['MATERIAL','ACTIVE','NONE'] | None
        :param export_all_vertex_colors: Export all vertex colors, Export all vertex colors, even if not used by any material. If no Vertex Color is used in the mesh materials, a fake COLOR_0 will be created, in order to keep material unchanged
        :type export_all_vertex_colors: bool | None
        :param export_active_vertex_color_when_no_material: Export active vertex color when no material, When there is no material on object, export active vertex color
        :type export_active_vertex_color_when_no_material: bool | None
        :param export_attributes: Attributes, Export Attributes (when starting with underscore)
        :type export_attributes: bool | None
        :param use_mesh_edges: Loose Edges, Export loose edges as lines, using the material from the first material slot
        :type use_mesh_edges: bool | None
        :param use_mesh_vertices: Loose Points, Export loose points as glTF points, using the material from the first material slot
        :type use_mesh_vertices: bool | None
        :param export_cameras: Cameras, Export cameras
        :type export_cameras: bool | None
        :param use_selection: Selected Objects, Export selected objects only
        :type use_selection: bool | None
        :param use_visible: Visible Objects, Export visible objects only
        :type use_visible: bool | None
        :param use_renderable: Renderable Objects, Export renderable objects only
        :type use_renderable: bool | None
        :param use_active_collection_with_nested: Include Nested Collections, Include active collection and nested collections
        :type use_active_collection_with_nested: bool | None
        :param use_active_collection: Active Collection, Export objects in the active collection only
        :type use_active_collection: bool | None
        :param use_active_scene: Active Scene, Export active scene only
        :type use_active_scene: bool | None
        :param collection: Source Collection, Export only objects from this collection (and its children)
        :type collection: str
        :param at_collection_center: Export at Collection Center, Export at Collection center of mass of root objects of the collection
        :type at_collection_center: bool | None
        :param export_extras: Custom Properties, Export custom properties as glTF extras
        :type export_extras: bool | None
        :param export_yup: +Y Up, Export using glTF convention, +Y up
        :type export_yup: bool | None
        :param export_apply: Apply Modifiers, Apply modifiers (excluding Armatures) to mesh objects -WARNING: prevents exporting shape keys
        :type export_apply: bool | None
        :param export_shared_accessors: Shared Accessors, Export Primitives using shared accessors for attributes
        :type export_shared_accessors: bool | None
        :param export_animations: Animations, Exports active actions and NLA tracks as glTF animations
        :type export_animations: bool | None
        :param export_frame_range: Limit to Playback Range, Clips animations to selected playback range
        :type export_frame_range: bool | None
        :param export_frame_step: Sampling Rate, How often to evaluate animated values (in frames)
        :type export_frame_step: int | None
        :param export_force_sampling: Always Sample Animations, Apply sampling to all animations
        :type export_force_sampling: bool | None
        :param export_pointer_animation: Export Animation Pointer (Experimental), Export material, Light & Camera animation as Animation Pointer
        :type export_pointer_animation: bool | None
        :param export_animation_mode: Animation mode, Export Animation mode

    ACTIONS
    Actions -- Export actions (actives and on NLA tracks) as separate animations.

    ACTIVE_ACTIONS
    Active actions merged -- All the currently assigned actions become one glTF animation.

    BROADCAST
    Broadcast actions -- Broadcast all compatible actions to all objects. Animated objects will get all actions compatible with them, others will get no animation at all.

    NLA_TRACKS
    NLA Tracks -- Export individual NLA Tracks as separate animation.

    SCENE
    Scene -- Export baked scene as a single animation.
        :type export_animation_mode: typing.Literal['ACTIONS','ACTIVE_ACTIONS','BROADCAST','NLA_TRACKS','SCENE'] | None
        :param export_nla_strips_merged_animation_name: Merged Animation Name, Name of single glTF animation to be exported
        :type export_nla_strips_merged_animation_name: str
        :param export_def_bones: Export Deformation Bones Only, Export Deformation bones only
        :type export_def_bones: bool | None
        :param export_hierarchy_flatten_bones: Flatten Bone Hierarchy, Flatten Bone Hierarchy. Useful in case of non decomposable transformation matrix
        :type export_hierarchy_flatten_bones: bool | None
        :param export_hierarchy_flatten_objs: Flatten Object Hierarchy, Flatten Object Hierarchy. Useful in case of non decomposable transformation matrix
        :type export_hierarchy_flatten_objs: bool | None
        :param export_armature_object_remove: Remove Armature Object, Remove Armature object if possible. If Armature has multiple root bones, object will not be removed
        :type export_armature_object_remove: bool | None
        :param export_leaf_bone: Add Leaf Bones, Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data)
        :type export_leaf_bone: bool | None
        :param export_optimize_animation_size: Optimize Animation Size, Reduce exported file size by removing duplicate keyframes
        :type export_optimize_animation_size: bool | None
        :param export_optimize_animation_keep_anim_armature: Force keeping channels for bones, If all keyframes are identical in a rig, force keeping the minimal animation. When off, all possible channels for the bones will be exported, even if empty (minimal animation, 2 keyframes)
        :type export_optimize_animation_keep_anim_armature: bool | None
        :param export_optimize_animation_keep_anim_object: Force keeping channel for objects, If all keyframes are identical for object transformations, force keeping the minimal animation
        :type export_optimize_animation_keep_anim_object: bool | None
        :param export_optimize_disable_viewport: Disable viewport for other objects, When exporting animations, disable viewport for other objects, for performance
        :type export_optimize_disable_viewport: bool | None
        :param export_negative_frame: Negative Frames, Negative Frames are slid or cropped

    SLIDE
    Slide -- Slide animation to start at frame 0.

    CROP
    Crop -- Keep only frames above frame 0.
        :type export_negative_frame: typing.Literal['SLIDE','CROP'] | None
        :param export_anim_slide_to_zero: Set all glTF Animation starting at 0, Set all glTF animation starting at 0.0s. Can be useful for looping animations
        :type export_anim_slide_to_zero: bool | None
        :param export_bake_animation: Bake All Objects Animations, Force exporting animation on every object. Can be useful when using constraints or driver. Also useful when exporting only selection
        :type export_bake_animation: bool | None
        :param export_anim_single_armature: Export all Armature Actions, Export all actions, bound to a single armature. WARNING: Option does not support exports including multiple armatures
        :type export_anim_single_armature: bool | None
        :param export_reset_pose_bones: Reset pose bones between actions, Reset pose bones between each action exported. This is needed when some bones are not keyed on some animations
        :type export_reset_pose_bones: bool | None
        :param export_current_frame: Use Current Frame as Object Rest Transformations, Export the scene in the current animation frame. When off, frame 0 is used as rest transformations for objects
        :type export_current_frame: bool | None
        :param export_rest_position_armature: Use Rest Position Armature, Export armatures using rest position as joints' rest pose. When off, current frame pose is used as rest pose
        :type export_rest_position_armature: bool | None
        :param export_anim_scene_split_object: Split Animation by Object, Export Scene as seen in Viewport, But split animation by Object
        :type export_anim_scene_split_object: bool | None
        :param export_skins: Skinning, Export skinning (armature) data
        :type export_skins: bool | None
        :param export_influence_nb: Bone Influences, Choose how many Bone influences to export
        :type export_influence_nb: int | None
        :param export_all_influences: Include All Bone Influences, Allow export of all joint vertex influences. Models may appear incorrectly in many viewers
        :type export_all_influences: bool | None
        :param export_morph: Shape Keys, Export shape keys (morph targets)
        :type export_morph: bool | None
        :param export_morph_normal: Shape Key Normals, Export vertex normals with shape keys (morph targets)
        :type export_morph_normal: bool | None
        :param export_morph_tangent: Shape Key Tangents, Export vertex tangents with shape keys (morph targets)
        :type export_morph_tangent: bool | None
        :param export_morph_animation: Shape Key Animations, Export shape keys animations (morph targets)
        :type export_morph_animation: bool | None
        :param export_morph_reset_sk_data: Reset shape keys between actions, Reset shape keys between each action exported. This is needed when some SK channels are not keyed on some animations
        :type export_morph_reset_sk_data: bool | None
        :param export_lights: Punctual Lights, Export directional, point, and spot lights. Uses "KHR_lights_punctual" glTF extension
        :type export_lights: bool | None
        :param export_try_sparse_sk: Use Sparse Accessor if better, Try using Sparse Accessor if it saves space
        :type export_try_sparse_sk: bool | None
        :param export_try_omit_sparse_sk: Omitting Sparse Accessor if data is empty, Omitting Sparse Accessor if data is empty
        :type export_try_omit_sparse_sk: bool | None
        :param export_gpu_instances: GPU Instances, Export using EXT_mesh_gpu_instancing. Limited to children of a given Empty. Multiple materials might be omitted
        :type export_gpu_instances: bool | None
        :param export_action_filter: Filter Actions, Filter Actions to be exported
        :type export_action_filter: bool | None
        :param export_convert_animation_pointer: Convert TRS/weights to Animation Pointer, Export TRS and weights as Animation Pointer. Using KHR_animation_pointer extension
        :type export_convert_animation_pointer: bool | None
        :param export_nla_strips: Group by NLA Track, When on, multiple actions become part of the same glTF animation if they're pushed onto NLA tracks with the same name. When off, all the currently assigned actions become one glTF animation
        :type export_nla_strips: bool | None
        :param export_original_specular: Export original PBR Specular, Export original glTF PBR Specular, instead of Blender Principled Shader Specular
        :type export_original_specular: bool | None
        :param will_save_settings: Remember Export Settings, Store glTF export settings in the Blender project
        :type will_save_settings: bool | None
        :param export_hierarchy_full_collections: Full Collection Hierarchy, Export full hierarchy, including intermediate collections
        :type export_hierarchy_full_collections: bool | None
        :param export_extra_animations: Prepare extra animations, Export additional animationsThis feature is not standard and needs an external extension to be included in the glTF file
        :type export_extra_animations: bool | None
        :param filter_glob: filter_glob
        :type filter_glob: str
    """
