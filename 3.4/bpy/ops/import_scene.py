import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def fbx(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        directory: typing.Union[str, typing.Any] = "",
        filter_glob: typing.Union[str, typing.Any] = "*.fbx",
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
        ui_tab: typing.Optional[typing.Any] = 'MAIN',
        use_manual_orientation: typing.Union[bool, typing.Any] = False,
        global_scale: typing.Optional[typing.Any] = 1.0,
        bake_space_transform: typing.Union[bool, typing.Any] = False,
        use_custom_normals: typing.Union[bool, typing.Any] = True,
        colors_type: typing.Optional[typing.Any] = 'SRGB',
        use_image_search: typing.Union[bool, typing.Any] = True,
        use_alpha_decals: typing.Union[bool, typing.Any] = False,
        decal_offset: typing.Optional[typing.Any] = 0.0,
        use_anim: typing.Union[bool, typing.Any] = True,
        anim_offset: typing.Optional[typing.Any] = 1.0,
        use_subsurf: typing.Union[bool, typing.Any] = False,
        use_custom_props: typing.Union[bool, typing.Any] = True,
        use_custom_props_enum_as_string: typing.Union[bool, typing.Any] = True,
        ignore_leaf_bones: typing.Union[bool, typing.Any] = False,
        force_connect_children: typing.Union[bool, typing.Any] = False,
        automatic_bone_orientation: typing.Union[bool, typing.Any] = False,
        primary_bone_axis: typing.Optional[typing.Any] = 'Y',
        secondary_bone_axis: typing.Optional[typing.Any] = 'X',
        use_prepost_rot: typing.Union[bool, typing.Any] = True,
        axis_forward: typing.Optional[typing.Any] = '-Z',
        axis_up: typing.Optional[typing.Any] = 'Y'):
    ''' Load a FBX file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: typing.Union[str, typing.Any]
    :param directory: directory
    :type directory: typing.Union[str, typing.Any]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    :param files: File Path
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
    :param ui_tab: ui_tab, Import options categories * ``MAIN`` Main -- Main basic settings. * ``ARMATURE`` Armatures -- Armature-related settings.
    :type ui_tab: typing.Optional[typing.Any]
    :param use_manual_orientation: Manual Orientation, Specify orientation and scale, instead of using embedded data in FBX file
    :type use_manual_orientation: typing.Union[bool, typing.Any]
    :param global_scale: Scale
    :type global_scale: typing.Optional[typing.Any]
    :param bake_space_transform: Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risks, known broken with armatures/animations)
    :type bake_space_transform: typing.Union[bool, typing.Any]
    :param use_custom_normals: Custom Normals, Import custom normals, if available (otherwise Blender will recompute them)
    :type use_custom_normals: typing.Union[bool, typing.Any]
    :param colors_type: Vertex Colors, Import vertex color attributes * ``NONE`` None -- Do not import color attributes. * ``SRGB`` sRGB -- Expect file colors in sRGB color space. * ``LINEAR`` Linear -- Expect file colors in linear color space.
    :type colors_type: typing.Optional[typing.Any]
    :param use_image_search: may be slow)
    :type use_image_search: typing.Union[bool, typing.Any]
    :param use_alpha_decals: Alpha Decals, Treat materials with alpha as decals (no shadow casting)
    :type use_alpha_decals: typing.Union[bool, typing.Any]
    :param decal_offset: Decal Offset, Displace geometry of alpha meshes
    :type decal_offset: typing.Optional[typing.Any]
    :param use_anim: Import Animation, Import FBX animation
    :type use_anim: typing.Union[bool, typing.Any]
    :param anim_offset: Animation Offset, Offset to apply to animation during import, in frames
    :type anim_offset: typing.Optional[typing.Any]
    :param use_subsurf: Subdivision Data, Import FBX subdivision information as subdivision surface modifiers
    :type use_subsurf: typing.Union[bool, typing.Any]
    :param use_custom_props: Custom Properties, Import user properties as custom properties
    :type use_custom_props: typing.Union[bool, typing.Any]
    :param use_custom_props_enum_as_string: Import Enums As Strings, Store enumeration values as strings
    :type use_custom_props_enum_as_string: typing.Union[bool, typing.Any]
    :param ignore_leaf_bones: Ignore Leaf Bones, Ignore the last bone at the end of each chain (used to mark the length of the previous bone)
    :type ignore_leaf_bones: typing.Union[bool, typing.Any]
    :param force_connect_children: Force Connect Children, Force connection of children bones to their parent, even if their computed head/tail positions do not match (can be useful with pure-joints-type armatures)
    :type force_connect_children: typing.Union[bool, typing.Any]
    :param automatic_bone_orientation: Automatic Bone Orientation, Try to align the major bone axis with the bone children
    :type automatic_bone_orientation: typing.Union[bool, typing.Any]
    :param primary_bone_axis: Primary Bone Axis
    :type primary_bone_axis: typing.Optional[typing.Any]
    :param secondary_bone_axis: Secondary Bone Axis
    :type secondary_bone_axis: typing.Optional[typing.Any]
    :param use_prepost_rot: Use Pre/Post Rotation, Use pre/post rotation from FBX transform (you may have to disable that in some cases)
    :type use_prepost_rot: typing.Union[bool, typing.Any]
    :param axis_forward: Forward
    :type axis_forward: typing.Optional[typing.Any]
    :param axis_up: Up
    :type axis_up: typing.Optional[typing.Any]
    '''

    pass


def gltf(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         filepath: typing.Union[str, typing.Any] = "",
         convert_lighting_mode: typing.Optional[typing.Any] = 'SPEC',
         filter_glob: typing.Union[str, typing.Any] = "*.glb;*.gltf",
         files: typing.Optional[bpy.types.bpy_prop_collection[
             'bpy.types.OperatorFileListElement']] = None,
         loglevel: typing.Optional[typing.Any] = 0,
         import_pack_images: typing.Union[bool, typing.Any] = True,
         merge_vertices: typing.Union[bool, typing.Any] = False,
         import_shading: typing.Optional[typing.Any] = 'NORMALS',
         bone_heuristic: typing.Optional[typing.Any] = 'TEMPERANCE',
         guess_original_bind_pose: typing.Union[bool, typing.Any] = True):
    ''' Load a glTF 2.0 file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: typing.Union[str, typing.Any]
    :param convert_lighting_mode: Lighting Mode, Optional backwards compatibility for non-standard render engines. Applies to lights * ``SPEC`` Standard -- Physically-based glTF lighting units (cd, lx, nt). * ``COMPAT`` Unitless -- Non-physical, unitless lighting. Useful when exposure controls are not available. * ``RAW`` Raw (Deprecated) -- Blender lighting strengths with no conversion.
    :type convert_lighting_mode: typing.Optional[typing.Any]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    :param files: File Path
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
    :param loglevel: Log Level, Log Level
    :type loglevel: typing.Optional[typing.Any]
    :param import_pack_images: Pack Images, Pack all images into .blend file
    :type import_pack_images: typing.Union[bool, typing.Any]
    :param merge_vertices: Merge Vertices, The glTF format requires discontinuous normals, UVs, and other vertex attributes to be stored as separate vertices, as required for rendering on typical graphics hardware. This option attempts to combine co-located vertices where possible. Currently cannot combine verts with different normals
    :type merge_vertices: typing.Union[bool, typing.Any]
    :param import_shading: Shading, How normals are computed during import
    :type import_shading: typing.Optional[typing.Any]
    :param bone_heuristic: Bone Dir, Heuristic for placing bones. Tries to make bones pretty * ``BLENDER`` Blender (best for re-importing) -- Good for re-importing glTFs exported from Blender. Bone tips are placed on their local +Y axis (in glTF space). * ``TEMPERANCE`` Temperance (average) -- Decent all-around strategy. A bone with one child has its tip placed on the local axis closest to its child. * ``FORTUNE`` Fortune (may look better, less accurate) -- Might look better than Temperance, but also might have errors. A bone with one child has its tip placed at its child's root. Non-uniform scalings may get messed up though, so beware.
    :type bone_heuristic: typing.Optional[typing.Any]
    :param guess_original_bind_pose: Guess Original Bind Pose, Try to guess the original bind pose for skinned meshes from the inverse bind matrices. When off, use default/rest pose as bind pose
    :type guess_original_bind_pose: typing.Union[bool, typing.Any]
    '''

    pass


def obj(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        filter_glob: typing.Union[str, typing.Any] = "*.obj;*.mtl",
        use_edges: typing.Union[bool, typing.Any] = True,
        use_smooth_groups: typing.Union[bool, typing.Any] = True,
        use_split_objects: typing.Union[bool, typing.Any] = True,
        use_split_groups: typing.Union[bool, typing.Any] = False,
        use_groups_as_vgroups: typing.Union[bool, typing.Any] = False,
        use_image_search: typing.Union[bool, typing.Any] = True,
        split_mode: typing.Optional[typing.Any] = 'ON',
        global_clamp_size: typing.Optional[typing.Any] = 0.0,
        axis_forward: typing.Optional[typing.Any] = '-Z',
        axis_up: typing.Optional[typing.Any] = 'Y'):
    ''' Load a Wavefront OBJ File

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: typing.Union[str, typing.Any]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    :param use_edges: Lines, Import lines and faces with 2 verts as edge
    :type use_edges: typing.Union[bool, typing.Any]
    :param use_smooth_groups: Smooth Groups, Surround smooth groups by sharp edges
    :type use_smooth_groups: typing.Union[bool, typing.Any]
    :param use_split_objects: Object, Import OBJ Objects into Blender Objects
    :type use_split_objects: typing.Union[bool, typing.Any]
    :param use_split_groups: Group, Import OBJ Groups into Blender Objects
    :type use_split_groups: typing.Union[bool, typing.Any]
    :param use_groups_as_vgroups: Poly Groups, Import OBJ groups as vertex groups
    :type use_groups_as_vgroups: typing.Union[bool, typing.Any]
    :param use_image_search: Image Search, Search subdirs for any associated images (Warning, may be slow)
    :type use_image_search: typing.Union[bool, typing.Any]
    :param split_mode: Split * ``ON`` Split -- Split geometry, omits vertices unused by edges or faces. * ``OFF`` Keep Vert Order -- Keep vertex order from file.
    :type split_mode: typing.Optional[typing.Any]
    :param global_clamp_size: Clamp Size, Clamp bounds under this value (zero to disable)
    :type global_clamp_size: typing.Optional[typing.Any]
    :param axis_forward: Forward
    :type axis_forward: typing.Optional[typing.Any]
    :param axis_up: Up
    :type axis_up: typing.Optional[typing.Any]
    '''

    pass


def x3d(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        filter_glob: typing.Union[str, typing.Any] = "*.x3d;*.wrl",
        axis_forward: typing.Optional[typing.Any] = 'Z',
        axis_up: typing.Optional[typing.Any] = 'Y'):
    ''' Import an X3D or VRML2 file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: typing.Union[str, typing.Any]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    :param axis_forward: Forward
    :type axis_forward: typing.Optional[typing.Any]
    :param axis_up: Up
    :type axis_up: typing.Optional[typing.Any]
    '''

    pass
