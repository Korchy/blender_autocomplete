import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

def fbx(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    directory: str = "",
    filter_glob: str = "*.fbx",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    ui_tab: typing.Literal["MAIN", "ARMATURE"] | None = "MAIN",
    use_manual_orientation: bool | None = False,
    global_scale: float | None = 1.0,
    bake_space_transform: bool | None = False,
    use_custom_normals: bool | None = True,
    colors_type: typing.Literal["NONE", "SRGB", "LINEAR"] | None = "SRGB",
    use_image_search: bool | None = True,
    use_alpha_decals: bool | None = False,
    decal_offset: float | None = 0.0,
    use_anim: bool | None = True,
    anim_offset: float | None = 1.0,
    use_subsurf: bool | None = False,
    use_custom_props: bool | None = True,
    use_custom_props_enum_as_string: bool | None = True,
    ignore_leaf_bones: bool | None = False,
    force_connect_children: bool | None = False,
    automatic_bone_orientation: bool | None = False,
    primary_bone_axis: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
    secondary_bone_axis: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "X",
    use_prepost_rot: bool | None = True,
    mtl_name_collision_mode: typing.Literal["MAKE_UNIQUE", "REFERENCE_EXISTING"]
    | None = "MAKE_UNIQUE",
    axis_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "-Z",
    axis_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
) -> None:
    """Load a FBX file

        :param filepath: File Path, Filepath used for importing the file
        :param directory: directory
        :param filter_glob: filter_glob
        :param files: File Path
        :param ui_tab: ui_tab, Import options categories

    MAIN
    Main -- Main basic settings.

    ARMATURE
    Armatures -- Armature-related settings.
        :param use_manual_orientation: Manual Orientation, Specify orientation and scale, instead of using embedded data in FBX file
        :param global_scale: Scale
        :param bake_space_transform: Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blenders space (WARNING! experimental option, use at own risk, known to be broken with armatures/animations)
        :param use_custom_normals: Custom Normals, Import custom normals, if available (otherwise Blender will recompute them)
        :param colors_type: Vertex Colors, Import vertex color attributes

    NONE
    None -- Do not import color attributes.

    SRGB
    sRGB -- Expect file colors in sRGB color space.

    LINEAR
    Linear -- Expect file colors in linear color space.
        :param use_image_search: Image Search, Search subdirs for any associated images (WARNING: may be slow)
        :param use_alpha_decals: Alpha Decals, Treat materials with alpha as decals (no shadow casting)
        :param decal_offset: Decal Offset, Displace geometry of alpha meshes
        :param use_anim: Import Animation, Import FBX animation
        :param anim_offset: Animation Offset, Offset to apply to animation during import, in frames
        :param use_subsurf: Subdivision Data, Import FBX subdivision information as subdivision surface modifiers
        :param use_custom_props: Custom Properties, Import user properties as custom properties
        :param use_custom_props_enum_as_string: Import Enums As Strings, Store enumeration values as strings
        :param ignore_leaf_bones: Ignore Leaf Bones, Ignore the last bone at the end of each chain (used to mark the length of the previous bone)
        :param force_connect_children: Force Connect Children, Force connection of children bones to their parent, even if their computed head/tail positions do not match (can be useful with pure-joints-type armatures)
        :param automatic_bone_orientation: Automatic Bone Orientation, Try to align the major bone axis with the bone children
        :param primary_bone_axis: Primary Bone Axis
        :param secondary_bone_axis: Secondary Bone Axis
        :param use_prepost_rot: Use Pre/Post Rotation, Use pre/post rotation from FBX transform (you may have to disable that in some cases)
        :param mtl_name_collision_mode: Material Name Collision, Behavior when the name of an imported material conflicts with an existing material

    MAKE_UNIQUE
    Make Unique -- Import each FBX material as a unique Blender material.

    REFERENCE_EXISTING
    Reference Existing -- If a material with the same name already exists, reference that instead of importing.
        :param axis_forward: Forward
        :param axis_up: Up
    """

def gltf(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    export_import_convert_lighting_mode: typing.Literal["SPEC", "COMPAT", "RAW"]
    | None = "SPEC",
    filter_glob: str = "*.glb;*.gltf",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    loglevel: int | None = 0,
    import_pack_images: bool | None = True,
    merge_vertices: bool | None = False,
    import_shading: typing.Literal["NORMALS", "FLAT", "SMOOTH"] | None = "NORMALS",
    bone_heuristic: typing.Literal["BLENDER", "TEMPERANCE", "FORTUNE"]
    | None = "BLENDER",
    disable_bone_shape: bool | None = False,
    bone_shape_scale_factor: float | None = 1.0,
    guess_original_bind_pose: bool | None = True,
    import_webp_texture: bool | None = False,
    import_unused_materials: bool | None = False,
    import_select_created_objects: bool | None = True,
    import_scene_extras: bool | None = True,
    import_scene_as_collection: bool | None = True,
    import_merge_material_slots: bool | None = True,
) -> None:
    """Load a glTF 2.0 file

        :param filepath: File Path, Filepath used for importing the file
        :param export_import_convert_lighting_mode: Lighting Mode, Optional backwards compatibility for non-standard render engines. Applies to lights

    SPEC
    Standard -- Physically-based glTF lighting units (cd, lx, nt).

    COMPAT
    Unitless -- Non-physical, unitless lighting. Useful when exposure controls are not available.

    RAW
    Raw (Deprecated) -- Blender lighting strengths with no conversion.
        :param filter_glob: filter_glob
        :param directory: directory
        :param files: File Path
        :param loglevel: Log Level, Log Level
        :param import_pack_images: Pack Images, Pack all images into .blend file
        :param merge_vertices: Merge Vertices, The glTF format requires discontinuous normals, UVs, and other vertex attributes to be stored as separate vertices, as required for rendering on typical graphics hardware. This option attempts to combine co-located vertices where possible. Currently cannot combine verts with different normals
        :param import_shading: Shading, How normals are computed during import
        :param bone_heuristic: Bone Dir, Heuristic for placing bones. Tries to make bones pretty

    BLENDER
    Blender (best for import/export round trip) -- Good for re-importing glTFs exported from Blender, and re-exporting glTFs to glTFs after Blender editing. Bone tips are placed on their local +Y axis (in glTF space).

    TEMPERANCE
    Temperance (average) -- Decent all-around strategy. A bone with one child has its tip placed on the local axis closest to its child.

    FORTUNE
    Fortune (may look better, less accurate) -- Might look better than Temperance, but also might have errors. A bone with one child has its tip placed at its childs root. Non-uniform scalings may get messed up though, so beware.
        :param disable_bone_shape: Disable Bone Shape, Do not create bone shapes
        :param bone_shape_scale_factor: Bone Shape Scale, Scale factor for bone shapes
        :param guess_original_bind_pose: Guess Original Bind Pose, Try to guess the original bind pose for skinned meshes from the inverse bind matrices. When off, use default/rest pose as bind pose
        :param import_webp_texture: Import WebP Textures, If a texture exists in WebP format, loads the WebP texture instead of the fallback PNG/JPEG one
        :param import_unused_materials: Import Unused Materials & Images, Import materials & Images not assigned to any mesh
        :param import_select_created_objects: Select Imported Objects, Select created objects at the end of the import
        :param import_scene_extras: Import Scene Extras, Import scene extras as custom properties. Existing custom properties will be overwritten
        :param import_scene_as_collection: Import Scene as Collection, Import the scene as a collection
        :param import_merge_material_slots: Merge Material Slot when possible, Merge material slots when possible
    """
