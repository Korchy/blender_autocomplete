import sys
import typing


def autodesk_3ds(filepath: str = "",
                 axis_forward: int = 'Y',
                 axis_up: int = 'Z',
                 filter_glob: str = "*.3ds",
                 constrain_size: float = 10.0,
                 use_image_search: bool = True,
                 use_apply_transform: bool = True):
    '''Import from 3DS file format (.3ds) 

    :param filepath: File Path, Filepath used for importing the file 
    :type filepath: str
    :param axis_forward: Forward 
    :type axis_forward: int
    :param axis_up: Up 
    :type axis_up: int
    :param filter_glob: filter_glob 
    :type filter_glob: str
    :param constrain_size: Size Constraint, Scale the model by 10 until it reaches the size constraint (0 to disable) 
    :type constrain_size: float
    :param use_image_search: Image Search, Search subdirectories for any associated images (Warning, may be slow) 
    :type use_image_search: bool
    :param use_apply_transform: Apply Transform, Workaround for object transformations importing incorrectly 
    :type use_apply_transform: bool
    '''

    pass


def fbx(filepath: str = "",
        axis_forward: int = '-Z',
        axis_up: int = 'Y',
        directory: str = "",
        filter_glob: str = "*.fbx",
        ui_tab: int = 'MAIN',
        use_manual_orientation: bool = False,
        global_scale: float = 1.0,
        bake_space_transform: bool = False,
        use_custom_normals: bool = True,
        use_image_search: bool = True,
        use_alpha_decals: bool = False,
        decal_offset: float = 0.0,
        use_anim: bool = True,
        anim_offset: float = 1.0,
        use_custom_props: bool = True,
        use_custom_props_enum_as_string: bool = True,
        ignore_leaf_bones: bool = False,
        force_connect_children: bool = False,
        automatic_bone_orientation: bool = False,
        primary_bone_axis: int = 'Y',
        secondary_bone_axis: int = 'X',
        use_prepost_rot: bool = True):
    '''Load a FBX file 

    :param filepath: File Path, Filepath used for importing the file 
    :type filepath: str
    :param axis_forward: Forward 
    :type axis_forward: int
    :param axis_up: Up 
    :type axis_up: int
    :param directory: directory 
    :type directory: str
    :param filter_glob: filter_glob 
    :type filter_glob: str
    :param ui_tab: ui_tab, Import options categoriesMAIN Main, Main basic settings.ARMATURE Armatures, Armature-related settings. 
    :type ui_tab: int
    :param use_manual_orientation: Manual Orientation, Specify orientation and scale, instead of using embedded data in FBX file 
    :type use_manual_orientation: bool
    :param global_scale: Scale 
    :type global_scale: float
    :param bake_space_transform: !EXPERIMENTAL! Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender’s space (WARNING! experimental option, use at own risks, known broken with armatures/animations) 
    :type bake_space_transform: bool
    :param use_custom_normals: Import Normals, Import custom normals, if available (otherwise Blender will recompute them) 
    :type use_custom_normals: bool
    :param use_image_search: Image Search, Search subdirs for any associated images (WARNING: may be slow) 
    :type use_image_search: bool
    :param use_alpha_decals: Alpha Decals, Treat materials with alpha as decals (no shadow casting) 
    :type use_alpha_decals: bool
    :param decal_offset: Decal Offset, Displace geometry of alpha meshes 
    :type decal_offset: float
    :param use_anim: Import Animation, Import FBX animation 
    :type use_anim: bool
    :param anim_offset: Animation Offset, Offset to apply to animation during import, in frames 
    :type anim_offset: float
    :param use_custom_props: Import User Properties, Import user properties as custom properties 
    :type use_custom_props: bool
    :param use_custom_props_enum_as_string: Import Enums As Strings, Store enumeration values as strings 
    :type use_custom_props_enum_as_string: bool
    :param ignore_leaf_bones: Ignore Leaf Bones, Ignore the last bone at the end of each chain (used to mark the length of the previous bone) 
    :type ignore_leaf_bones: bool
    :param force_connect_children: Force Connect Children, Force connection of children bones to their parent, even if their computed head/tail positions do not match (can be useful with pure-joints-type armatures) 
    :type force_connect_children: bool
    :param automatic_bone_orientation: Automatic Bone Orientation, Try to align the major bone axis with the bone children 
    :type automatic_bone_orientation: bool
    :param primary_bone_axis: Primary Bone Axis 
    :type primary_bone_axis: int
    :param secondary_bone_axis: Secondary Bone Axis 
    :type secondary_bone_axis: int
    :param use_prepost_rot: Use Pre/Post Rotation, Use pre/post rotation from FBX transform (you may have to disable that in some cases) 
    :type use_prepost_rot: bool
    '''

    pass


def obj(filepath: str = "",
        axis_forward: int = '-Z',
        axis_up: int = 'Y',
        filter_glob: str = "*.obj;*.mtl",
        use_edges: bool = True,
        use_smooth_groups: bool = True,
        use_split_objects: bool = True,
        use_split_groups: bool = True,
        use_groups_as_vgroups: bool = False,
        use_image_search: bool = True,
        split_mode: int = 'ON',
        global_clamp_size: float = 0.0):
    '''Load a Wavefront OBJ File 

    :param filepath: File Path, Filepath used for importing the file 
    :type filepath: str
    :param axis_forward: Forward 
    :type axis_forward: int
    :param axis_up: Up 
    :type axis_up: int
    :param filter_glob: filter_glob 
    :type filter_glob: str
    :param use_edges: Lines, Import lines and faces with 2 verts as edge 
    :type use_edges: bool
    :param use_smooth_groups: Smooth Groups, Surround smooth groups by sharp edges 
    :type use_smooth_groups: bool
    :param use_split_objects: Object, Import OBJ Objects into Blender Objects 
    :type use_split_objects: bool
    :param use_split_groups: Group, Import OBJ Groups into Blender Objects 
    :type use_split_groups: bool
    :param use_groups_as_vgroups: Poly Groups, Import OBJ groups as vertex groups 
    :type use_groups_as_vgroups: bool
    :param use_image_search: Image Search, Search subdirs for any associated images (Warning, may be slow) 
    :type use_image_search: bool
    :param split_mode: SplitON Split, Split geometry, omits unused verts.OFF Keep Vert Order, Keep vertex order from file. 
    :type split_mode: int
    :param global_clamp_size: Clamp Size, Clamp bounds under this value (zero to disable) 
    :type global_clamp_size: float
    '''

    pass


def x3d(filepath: str = "",
        axis_forward: int = 'Z',
        axis_up: int = 'Y',
        filter_glob: str = "*.x3d;*.wrl"):
    '''Import an X3D or VRML2 file 

    :param filepath: File Path, Filepath used for importing the file 
    :type filepath: str
    :param axis_forward: Forward 
    :type axis_forward: int
    :param axis_up: Up 
    :type axis_up: int
    :param filter_glob: filter_glob 
    :type filter_glob: str
    '''

    pass
