import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def fbx(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    directory: str | typing.Any = "",
    filter_glob: str | typing.Any = "*.fbx",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    ui_tab: str | None = "MAIN",
    use_manual_orientation: bool | typing.Any | None = False,
    global_scale: typing.Any | None = 1.0,
    bake_space_transform: bool | typing.Any | None = False,
    use_custom_normals: bool | typing.Any | None = True,
    colors_type: str | None = "SRGB",
    use_image_search: bool | typing.Any | None = True,
    use_alpha_decals: bool | typing.Any | None = False,
    decal_offset: typing.Any | None = 0.0,
    use_anim: bool | typing.Any | None = True,
    anim_offset: typing.Any | None = 1.0,
    use_subsurf: bool | typing.Any | None = False,
    use_custom_props: bool | typing.Any | None = True,
    use_custom_props_enum_as_string: bool | typing.Any | None = True,
    ignore_leaf_bones: bool | typing.Any | None = False,
    force_connect_children: bool | typing.Any | None = False,
    automatic_bone_orientation: bool | typing.Any | None = False,
    primary_bone_axis: str | None = "Y",
    secondary_bone_axis: str | None = "X",
    use_prepost_rot: bool | typing.Any | None = True,
    axis_forward: str | None = "-Z",
    axis_up: str | None = "Y",
):
    """Load a FBX file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Filepath used for importing the file
        :type filepath: str | typing.Any
        :param directory: directory
        :type directory: str | typing.Any
        :param filter_glob: filter_glob
        :type filter_glob: str | typing.Any
        :param files: File Path
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param ui_tab: ui_tab, Import options categories

    MAIN
    Main -- Main basic settings.

    ARMATURE
    Armatures -- Armature-related settings.
        :type ui_tab: str | None
        :param use_manual_orientation: Manual Orientation, Specify orientation and scale, instead of using embedded data in FBX file
        :type use_manual_orientation: bool | typing.Any | None
        :param global_scale: Scale
        :type global_scale: typing.Any | None
        :param bake_space_transform: Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risk, known to be broken with armatures/animations)
        :type bake_space_transform: bool | typing.Any | None
        :param use_custom_normals: Custom Normals, Import custom normals, if available (otherwise Blender will recompute them)
        :type use_custom_normals: bool | typing.Any | None
        :param colors_type: Vertex Colors, Import vertex color attributes

    NONE
    None -- Do not import color attributes.

    SRGB
    sRGB -- Expect file colors in sRGB color space.

    LINEAR
    Linear -- Expect file colors in linear color space.
        :type colors_type: str | None
        :param use_image_search: Image Search, Search subdirs for any associated images (WARNING: may be slow)
        :type use_image_search: bool | typing.Any | None
        :param use_alpha_decals: Alpha Decals, Treat materials with alpha as decals (no shadow casting)
        :type use_alpha_decals: bool | typing.Any | None
        :param decal_offset: Decal Offset, Displace geometry of alpha meshes
        :type decal_offset: typing.Any | None
        :param use_anim: Import Animation, Import FBX animation
        :type use_anim: bool | typing.Any | None
        :param anim_offset: Animation Offset, Offset to apply to animation during import, in frames
        :type anim_offset: typing.Any | None
        :param use_subsurf: Subdivision Data, Import FBX subdivision information as subdivision surface modifiers
        :type use_subsurf: bool | typing.Any | None
        :param use_custom_props: Custom Properties, Import user properties as custom properties
        :type use_custom_props: bool | typing.Any | None
        :param use_custom_props_enum_as_string: Import Enums As Strings, Store enumeration values as strings
        :type use_custom_props_enum_as_string: bool | typing.Any | None
        :param ignore_leaf_bones: Ignore Leaf Bones, Ignore the last bone at the end of each chain (used to mark the length of the previous bone)
        :type ignore_leaf_bones: bool | typing.Any | None
        :param force_connect_children: Force Connect Children, Force connection of children bones to their parent, even if their computed head/tail positions do not match (can be useful with pure-joints-type armatures)
        :type force_connect_children: bool | typing.Any | None
        :param automatic_bone_orientation: Automatic Bone Orientation, Try to align the major bone axis with the bone children
        :type automatic_bone_orientation: bool | typing.Any | None
        :param primary_bone_axis: Primary Bone Axis
        :type primary_bone_axis: str | None
        :param secondary_bone_axis: Secondary Bone Axis
        :type secondary_bone_axis: str | None
        :param use_prepost_rot: Use Pre/Post Rotation, Use pre/post rotation from FBX transform (you may have to disable that in some cases)
        :type use_prepost_rot: bool | typing.Any | None
        :param axis_forward: Forward
        :type axis_forward: str | None
        :param axis_up: Up
        :type axis_up: str | None
    """

    ...

def gltf(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    export_import_convert_lighting_mode: str | None = "SPEC",
    filter_glob: str | typing.Any = "*.glb;*.gltf",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    loglevel: typing.Any | None = 0,
    import_pack_images: bool | typing.Any | None = True,
    merge_vertices: bool | typing.Any | None = False,
    import_shading: str | None = "NORMALS",
    bone_heuristic: str | None = "BLENDER",
    guess_original_bind_pose: bool | typing.Any | None = True,
    import_webp_texture: bool | typing.Any | None = False,
):
    """Load a glTF 2.0 file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Filepath used for importing the file
        :type filepath: str | typing.Any
        :param export_import_convert_lighting_mode: Lighting Mode, Optional backwards compatibility for non-standard render engines. Applies to lights

    SPEC
    Standard -- Physically-based glTF lighting units (cd, lx, nt).

    COMPAT
    Unitless -- Non-physical, unitless lighting. Useful when exposure controls are not available.

    RAW
    Raw (Deprecated) -- Blender lighting strengths with no conversion.
        :type export_import_convert_lighting_mode: str | None
        :param filter_glob: filter_glob
        :type filter_glob: str | typing.Any
        :param files: File Path
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param loglevel: Log Level, Log Level
        :type loglevel: typing.Any | None
        :param import_pack_images: Pack Images, Pack all images into .blend file
        :type import_pack_images: bool | typing.Any | None
        :param merge_vertices: Merge Vertices, The glTF format requires discontinuous normals, UVs, and other vertex attributes to be stored as separate vertices, as required for rendering on typical graphics hardware. This option attempts to combine co-located vertices where possible. Currently cannot combine verts with different normals
        :type merge_vertices: bool | typing.Any | None
        :param import_shading: Shading, How normals are computed during import
        :type import_shading: str | None
        :param bone_heuristic: Bone Dir, Heuristic for placing bones. Tries to make bones pretty

    BLENDER
    Blender (best for import/export round trip) -- Good for re-importing glTFs exported from Blender, and re-exporting glTFs to glTFs after Blender editing. Bone tips are placed on their local +Y axis (in glTF space).

    TEMPERANCE
    Temperance (average) -- Decent all-around strategy. A bone with one child has its tip placed on the local axis closest to its child.

    FORTUNE
    Fortune (may look better, less accurate) -- Might look better than Temperance, but also might have errors. A bone with one child has its tip placed at its child's root. Non-uniform scalings may get messed up though, so beware.
        :type bone_heuristic: str | None
        :param guess_original_bind_pose: Guess Original Bind Pose, Try to guess the original bind pose for skinned meshes from the inverse bind matrices. When off, use default/rest pose as bind pose
        :type guess_original_bind_pose: bool | typing.Any | None
        :param import_webp_texture: Import WebP textures, If a texture exists in WebP format, loads the WebP texture instead of the fallback PNG/JPEG one
        :type import_webp_texture: bool | typing.Any | None
    """

    ...

def x3d(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    filter_glob: str | typing.Any = "*.x3d;*.wrl",
    axis_forward: str | None = "Z",
    axis_up: str | None = "Y",
):
    """Import an X3D or VRML2 file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: str | typing.Any
    :param filter_glob: filter_glob
    :type filter_glob: str | typing.Any
    :param axis_forward: Forward
    :type axis_forward: str | None
    :param axis_up: Up
    :type axis_up: str | None
    """

    ...
