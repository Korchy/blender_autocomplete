import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def fbx(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        directory: typing.Union[str, typing.Any] = "",
        filter_glob: typing.Union[str, typing.Any] = "*.fbx",
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
        ui_tab: typing.Optional[typing.Any] = 'MAIN',
        use_manual_orientation: typing.Optional[typing.Union[bool, typing.
                                                             Any]] = False,
        global_scale: typing.Optional[typing.Any] = 1.0,
        bake_space_transform: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        use_custom_normals: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = True,
        colors_type: typing.Optional[typing.Any] = 'SRGB',
        use_image_search: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        use_alpha_decals: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        decal_offset: typing.Optional[typing.Any] = 0.0,
        use_anim: typing.Optional[typing.Union[bool, typing.Any]] = True,
        anim_offset: typing.Optional[typing.Any] = 1.0,
        use_subsurf: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_custom_props: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        use_custom_props_enum_as_string: typing.Optional[
            typing.Union[bool, typing.Any]] = True,
        ignore_leaf_bones: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False,
        force_connect_children: typing.Optional[typing.Union[bool, typing.
                                                             Any]] = False,
        automatic_bone_orientation: typing.Optional[typing.Union[bool, typing.
                                                                 Any]] = False,
        primary_bone_axis: typing.Optional[typing.Any] = 'Y',
        secondary_bone_axis: typing.Optional[typing.Any] = 'X',
        use_prepost_rot: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True,
        axis_forward: typing.Optional[typing.Any] = '-Z',
        axis_up: typing.Optional[typing.Any] = 'Y'):
    ''' Load a FBX file :File: `addons/io_scene_fbx/__init__.py\:198 <https://projects.blender.org/blender/blender-addons/addons/io_scene_fbx/__init__.py#L198>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
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
    :type use_manual_orientation: typing.Optional[typing.Union[bool, typing.Any]]
    :param global_scale: Scale
    :type global_scale: typing.Optional[typing.Any]
    :param bake_space_transform: Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risk, known to be broken with armatures/animations)
    :type bake_space_transform: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_custom_normals: Custom Normals, Import custom normals, if available (otherwise Blender will recompute them)
    :type use_custom_normals: typing.Optional[typing.Union[bool, typing.Any]]
    :param colors_type: Vertex Colors, Import vertex color attributes * ``NONE`` None -- Do not import color attributes. * ``SRGB`` sRGB -- Expect file colors in sRGB color space. * ``LINEAR`` Linear -- Expect file colors in linear color space.
    :type colors_type: typing.Optional[typing.Any]
    :param use_image_search: may be slow)
    :type use_image_search: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_alpha_decals: Alpha Decals, Treat materials with alpha as decals (no shadow casting)
    :type use_alpha_decals: typing.Optional[typing.Union[bool, typing.Any]]
    :param decal_offset: Decal Offset, Displace geometry of alpha meshes
    :type decal_offset: typing.Optional[typing.Any]
    :param use_anim: Import Animation, Import FBX animation
    :type use_anim: typing.Optional[typing.Union[bool, typing.Any]]
    :param anim_offset: Animation Offset, Offset to apply to animation during import, in frames
    :type anim_offset: typing.Optional[typing.Any]
    :param use_subsurf: Subdivision Data, Import FBX subdivision information as subdivision surface modifiers
    :type use_subsurf: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_custom_props: Custom Properties, Import user properties as custom properties
    :type use_custom_props: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_custom_props_enum_as_string: Import Enums As Strings, Store enumeration values as strings
    :type use_custom_props_enum_as_string: typing.Optional[typing.Union[bool, typing.Any]]
    :param ignore_leaf_bones: Ignore Leaf Bones, Ignore the last bone at the end of each chain (used to mark the length of the previous bone)
    :type ignore_leaf_bones: typing.Optional[typing.Union[bool, typing.Any]]
    :param force_connect_children: Force Connect Children, Force connection of children bones to their parent, even if their computed head/tail positions do not match (can be useful with pure-joints-type armatures)
    :type force_connect_children: typing.Optional[typing.Union[bool, typing.Any]]
    :param automatic_bone_orientation: Automatic Bone Orientation, Try to align the major bone axis with the bone children
    :type automatic_bone_orientation: typing.Optional[typing.Union[bool, typing.Any]]
    :param primary_bone_axis: Primary Bone Axis
    :type primary_bone_axis: typing.Optional[typing.Any]
    :param secondary_bone_axis: Secondary Bone Axis
    :type secondary_bone_axis: typing.Optional[typing.Any]
    :param use_prepost_rot: Use Pre/Post Rotation, Use pre/post rotation from FBX transform (you may have to disable that in some cases)
    :type use_prepost_rot: typing.Optional[typing.Union[bool, typing.Any]]
    :param axis_forward: Forward
    :type axis_forward: typing.Optional[typing.Any]
    :param axis_up: Up
    :type axis_up: typing.Optional[typing.Any]
    '''

    pass


def gltf(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         filepath: typing.Union[str, typing.Any] = "",
         export_import_convert_lighting_mode: typing.Optional[typing.
                                                              Any] = 'SPEC',
         filter_glob: typing.Union[str, typing.Any] = "*.glb;*.gltf",
         files: typing.Optional[bpy.types.bpy_prop_collection[
             'bpy.types.OperatorFileListElement']] = None,
         loglevel: typing.Optional[typing.Any] = 0,
         import_pack_images: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = True,
         merge_vertices: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
         import_shading: typing.Optional[typing.Any] = 'NORMALS',
         bone_heuristic: typing.Optional[typing.Any] = 'BLENDER',
         guess_original_bind_pose: typing.Optional[typing.Union[bool, typing.
                                                                Any]] = True,
         import_webp_texture: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False):
    ''' Load a glTF 2.0 file :File: `addons/io_scene_gltf2/__init__.py\:1709 <https://projects.blender.org/blender/blender-addons/addons/io_scene_gltf2/__init__.py#L1709>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: typing.Union[str, typing.Any]
    :param export_import_convert_lighting_mode: Lighting Mode, Optional backwards compatibility for non-standard render engines. Applies to lights * ``SPEC`` Standard -- Physically-based glTF lighting units (cd, lx, nt). * ``COMPAT`` Unitless -- Non-physical, unitless lighting. Useful when exposure controls are not available. * ``RAW`` Raw (Deprecated) -- Blender lighting strengths with no conversion.
    :type export_import_convert_lighting_mode: typing.Optional[typing.Any]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    :param files: File Path
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
    :param loglevel: Log Level, Log Level
    :type loglevel: typing.Optional[typing.Any]
    :param import_pack_images: Pack Images, Pack all images into .blend file
    :type import_pack_images: typing.Optional[typing.Union[bool, typing.Any]]
    :param merge_vertices: Merge Vertices, The glTF format requires discontinuous normals, UVs, and other vertex attributes to be stored as separate vertices, as required for rendering on typical graphics hardware. This option attempts to combine co-located vertices where possible. Currently cannot combine verts with different normals
    :type merge_vertices: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_shading: Shading, How normals are computed during import
    :type import_shading: typing.Optional[typing.Any]
    :param bone_heuristic: Bone Dir, Heuristic for placing bones. Tries to make bones pretty * ``BLENDER`` Blender (best for import/export round trip) -- Good for re-importing glTFs exported from Blender, and re-exporting glTFs to glTFs after Blender editing. Bone tips are placed on their local +Y axis (in glTF space). * ``TEMPERANCE`` Temperance (average) -- Decent all-around strategy. A bone with one child has its tip placed on the local axis closest to its child. * ``FORTUNE`` Fortune (may look better, less accurate) -- Might look better than Temperance, but also might have errors. A bone with one child has its tip placed at its child's root. Non-uniform scalings may get messed up though, so beware.
    :type bone_heuristic: typing.Optional[typing.Any]
    :param guess_original_bind_pose: Guess Original Bind Pose, Try to guess the original bind pose for skinned meshes from the inverse bind matrices. When off, use default/rest pose as bind pose
    :type guess_original_bind_pose: typing.Optional[typing.Union[bool, typing.Any]]
    :param import_webp_texture: Import WebP textures, If a texture exists in WebP format, loads the WebP texture instead of the fallback PNG/JPEG one
    :type import_webp_texture: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def x3d(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        filter_glob: typing.Union[str, typing.Any] = "*.x3d;*.wrl",
        axis_forward: typing.Optional[typing.Any] = 'Z',
        axis_up: typing.Optional[typing.Any] = 'Y'):
    ''' Import an X3D or VRML2 file :File: `addons/io_scene_x3d/__init__.py\:50 <https://projects.blender.org/blender/blender-addons/addons/io_scene_x3d/__init__.py#L50>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
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
