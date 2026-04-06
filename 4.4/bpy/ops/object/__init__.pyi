import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops.transform
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

def add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
    type: bpy.stub_internal.rna_enums.ObjectTypeItems | None = "EMPTY",
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add an object to the scene

        :param radius: Radius
        :param type: Type
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def add_modifier_menu(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

def add_named(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    linked: bool | None = False,
    name: str = "",
    session_uid: int | None = 0,
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = (
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
    ),
    drop_x: int | None = 0,
    drop_y: int | None = 0,
) -> None:
    """Add named object

    :param linked: Linked, Duplicate object but not object data, linking to the original data
    :param name: Name, Name of the data-block to use by the operator
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :param matrix: Matrix
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    """

def align(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    bb_quality: bool | None = True,
    align_mode: typing.Literal["OPT_1", "OPT_2", "OPT_3"] | None = "OPT_2",
    relative_to: typing.Literal["OPT_1", "OPT_2", "OPT_3", "OPT_4"] | None = "OPT_4",
    align_axis: set[typing.Literal["X", "Y", "Z"]] | None = {},
) -> None:
    """Align objects

        :param bb_quality: High Quality, Enables high quality but slow calculation of the bounding box for perfect results on complex shape meshes with rotation/scale
        :param align_mode: Align Mode, Side of object to use for alignment
        :param relative_to: Relative To, Reference location to align to

    OPT_1
    Scene Origin -- Use the scene origin as the position for the selected objects to align to.

    OPT_2
    3D Cursor -- Use the 3D cursor as the position for the selected objects to align to.

    OPT_3
    Selection -- Use the selected objects as the position for the selected objects to align to.

    OPT_4
    Active -- Use the active object as the position for the selected objects to align to.
        :param align_axis: Align, Align to axis
    """

def anim_transforms_to_deltas(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Convert object animation for normal transforms to delta transforms"""

def armature_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add an armature object to the scene

        :param radius: Radius
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def assign_property_defaults(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    process_data: bool | None = True,
    process_bones: bool | None = True,
) -> None:
    """Assign the current values of custom properties as their defaults, for use as part of the rest pose state in NLA track mixing

    :param process_data: Process data properties
    :param process_bones: Process bone properties
    """

def bake(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.BakePassTypeItems | None = "COMBINED",
    pass_filter: set[bpy.stub_internal.rna_enums.BakePassFilterTypeItems] | None = {},
    filepath: str = "",
    width: int | None = 512,
    height: int | None = 512,
    margin: int | None = 16,
    margin_type: bpy.stub_internal.rna_enums.BakeMarginTypeItems | None = "EXTEND",
    use_selected_to_active: bool | None = False,
    max_ray_distance: float | None = 0.0,
    cage_extrusion: float | None = 0.0,
    cage_object: str = "",
    normal_space: bpy.stub_internal.rna_enums.NormalSpaceItems | None = "TANGENT",
    normal_r: bpy.stub_internal.rna_enums.NormalSwizzleItems | None = "POS_X",
    normal_g: bpy.stub_internal.rna_enums.NormalSwizzleItems | None = "POS_Y",
    normal_b: bpy.stub_internal.rna_enums.NormalSwizzleItems | None = "POS_Z",
    target: bpy.stub_internal.rna_enums.BakeTargetItems | None = "IMAGE_TEXTURES",
    save_mode: bpy.stub_internal.rna_enums.BakeSaveModeItems | None = "INTERNAL",
    use_clear: bool | None = False,
    use_cage: bool | None = False,
    use_split_materials: bool | None = False,
    use_automatic_name: bool | None = False,
    uv_layer: str = "",
) -> None:
    """Bake image textures of selected objects

    :param type: Type, Type of pass to bake, some of them may not be supported by the current render engine
    :param pass_filter: Pass Filter, Filter to combined, diffuse, glossy, transmission and subsurface passes
    :param filepath: File Path, Image filepath to use when saving externally
    :param width: Width, Horizontal dimension of the baking map (external only)
    :param height: Height, Vertical dimension of the baking map (external only)
    :param margin: Margin, Extends the baked result as a post process filter
    :param margin_type: Margin Type, Which algorithm to use to generate the margin
    :param use_selected_to_active: Selected to Active, Bake shading on the surface of selected objects to the active object
    :param max_ray_distance: Max Ray Distance, The maximum ray distance for matching points between the active and selected objects. If zero, there is no limit
    :param cage_extrusion: Cage Extrusion, Inflate the active object by the specified distance for baking. This helps matching to points nearer to the outside of the selected object meshes
    :param cage_object: Cage Object, Object to use as cage, instead of calculating the cage from the active object with cage extrusion
    :param normal_space: Normal Space, Choose normal space for baking
    :param normal_r: R, Axis to bake in red channel
    :param normal_g: G, Axis to bake in green channel
    :param normal_b: B, Axis to bake in blue channel
    :param target: Target, Where to output the baked map
    :param save_mode: Save Mode, Where to save baked image textures
    :param use_clear: Clear, Clear images before baking (only for internal saving)
    :param use_cage: Cage, Cast rays to active object from a cage
    :param use_split_materials: Split Materials, Split baked maps per material, using material name in output file (external only)
    :param use_automatic_name: Automatic Name, Automatically name the output file with the pass type
    :param uv_layer: UV Layer, UV layer to override active
    """

def bake_image(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Bake image textures of selected objects"""

def camera_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add a camera object to the scene

        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def clear_override_library(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete the selected local overrides and relink their usages to the linked data-blocks if possible, else reset them and mark them as non editable"""

def collection_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add an object to a new collection"""

def collection_external_asset_drop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    session_uid: int | None = 0,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
    use_instance: bool | None = True,
    drop_x: int | None = 0,
    drop_y: int | None = 0,
    collection: str | None = "",
) -> None:
    """Add the dragged collection to the scene

        :param session_uid: Session UID, Session UID of the data-block to use by the operator
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
        :param use_instance: Instance, Add the dropped collection as collection instance
        :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
        :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
        :param collection: Collection
    """

def collection_instance_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "Collection",
    collection: str | None = "",
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
    session_uid: int | None = 0,
    drop_x: int | None = 0,
    drop_y: int | None = 0,
) -> None:
    """Add a collection instance

        :param name: Name, Collection name to add
        :param collection: Collection
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
        :param session_uid: Session UID, Session UID of the data-block to use by the operator
        :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
        :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    """

def collection_link(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    collection: str | None = "",
) -> None:
    """Add an object to an existing collection

    :param collection: Collection
    """

def collection_objects_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all objects in collection"""

def collection_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the active object from this collection"""

def collection_unlink(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Unlink the collection from all objects"""

def constraint_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "",
) -> None:
    """Add a constraint to the active object

    :param type: Type
    """

def constraint_add_with_targets(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "",
) -> None:
    """Add a constraint to the active object, with target (where applicable) set to the selected objects/bones

    :param type: Type
    """

def constraints_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear all constraints from the selected objects"""

def constraints_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy constraints to other selected objects"""

def convert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    target: typing.Literal["CURVE", "MESH", "CURVES", "GREASEPENCIL"] | None = "MESH",
    keep_original: bool | None = False,
    merge_customdata: bool | None = True,
    thickness: int | None = 5,
    faces: bool | None = True,
    offset: float | None = 0.01,
) -> None:
    """Convert selected objects to another type

        :param target: Target, Type of object to convert to

    CURVE
    Curve -- Curve from Mesh or Text objects.

    MESH
    Mesh -- Mesh from Curve, Surface, Metaball, or Text objects.

    CURVES
    Curves -- Curves from evaluated curve data.

    GREASEPENCIL
    Grease Pencil -- Grease Pencil from Curve or Mesh objects.
        :param keep_original: Keep Original, Keep original objects instead of replacing them
        :param merge_customdata: Merge UVs, Merge UV coordinates that share a vertex to account for imprecision in some modifiers
        :param thickness: Thickness
        :param faces: Export Faces, Export faces as filled strokes
        :param offset: Stroke Offset, Offset strokes from fill
    """

def correctivesmooth_bind(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Bind base pose in Corrective Smooth modifier

    :param modifier: Modifier, Name of the modifier to edit
    """

def curves_empty_hair_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add an empty curve object to the scene with the selected mesh as surface

        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def curves_random_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add a curves object with random curves to the scene

        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def data_instance_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    session_uid: int | None = 0,
    type: bpy.stub_internal.rna_enums.IdTypeItems | None = "ACTION",
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
    drop_x: int | None = 0,
    drop_y: int | None = 0,
) -> None:
    """Add an object data instance

        :param name: Name, Name of the data-block to use by the operator
        :param session_uid: Session UID, Session UID of the data-block to use by the operator
        :param type: Type
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
        :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
        :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    """

def data_transfer(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_reverse_transfer: bool | None = False,
    use_freeze: bool | None = False,
    data_type: typing.Literal[
        "VGROUP_WEIGHTS",
        "BEVEL_WEIGHT_VERT",
        "COLOR_VERTEX",
        "SHARP_EDGE",
        "SEAM",
        "CREASE",
        "BEVEL_WEIGHT_EDGE",
        "FREESTYLE_EDGE",
        "CUSTOM_NORMAL",
        "COLOR_CORNER",
        "UV",
        "SMOOTH",
        "FREESTYLE_FACE",
    ]
    | None = "",
    use_create: bool | None = True,
    vert_mapping: bpy.stub_internal.rna_enums.DtMethodVertexItems | None = "NEAREST",
    edge_mapping: bpy.stub_internal.rna_enums.DtMethodEdgeItems | None = "NEAREST",
    loop_mapping: bpy.stub_internal.rna_enums.DtMethodLoopItems
    | None = "NEAREST_POLYNOR",
    poly_mapping: bpy.stub_internal.rna_enums.DtMethodPolyItems | None = "NEAREST",
    use_auto_transform: bool | None = False,
    use_object_transform: bool | None = True,
    use_max_distance: bool | None = False,
    max_distance: float | None = 1.0,
    ray_radius: float | None = 0.0,
    islands_precision: float | None = 0.1,
    layers_select_src: bpy.stub_internal.rna_enums.DtLayersSelectSrcItems
    | None = "ACTIVE",
    layers_select_dst: bpy.stub_internal.rna_enums.DtLayersSelectDstItems
    | None = "ACTIVE",
    mix_mode: bpy.stub_internal.rna_enums.DtMixModeItems | None = "REPLACE",
    mix_factor: float | None = 1.0,
) -> None:
    """Transfer data layer(s) (weights, edge sharp, etc.) from active to selected meshes

        :param use_reverse_transfer: Reverse Transfer, Transfer from selected objects to active one
        :param use_freeze: Freeze Operator, Prevent changes to settings to re-run the operator, handy to change several things at once with heavy geometry
        :param data_type: Data Type, Which data to transfer

    VGROUP_WEIGHTS
    Vertex Group(s) -- Transfer active or all vertex groups.

    BEVEL_WEIGHT_VERT
    Bevel Weight -- Transfer bevel weights.

    COLOR_VERTEX
    Colors -- Color Attributes.

    SHARP_EDGE
    Sharp -- Transfer sharp mark.

    SEAM
    UV Seam -- Transfer UV seam mark.

    CREASE
    Subdivision Crease -- Transfer crease values.

    BEVEL_WEIGHT_EDGE
    Bevel Weight -- Transfer bevel weights.

    FREESTYLE_EDGE
    Freestyle Mark -- Transfer Freestyle edge mark.

    CUSTOM_NORMAL
    Custom Normals -- Transfer custom normals.

    COLOR_CORNER
    Colors -- Color Attributes.

    UV
    UVs -- Transfer UV layers.

    SMOOTH
    Smooth -- Transfer flat/smooth mark.

    FREESTYLE_FACE
    Freestyle Mark -- Transfer Freestyle face mark.
        :param use_create: Create Data, Add data layers on destination meshes if needed
        :param vert_mapping: Vertex Mapping, Method used to map source vertices to destination ones
        :param edge_mapping: Edge Mapping, Method used to map source edges to destination ones
        :param loop_mapping: Face Corner Mapping, Method used to map source faces corners to destination ones
        :param poly_mapping: Face Mapping, Method used to map source faces to destination ones
        :param use_auto_transform: Auto Transform, Automatically compute transformation to get the best possible match between source and destination meshes.Warning: Results will never be as good as manual matching of objects
        :param use_object_transform: Object Transform, Evaluate source and destination meshes in global space
        :param use_max_distance: Only Neighbor Geometry, Source elements must be closer than given distance from destination one
        :param max_distance: Max Distance, Maximum allowed distance between source and destination element, for non-topology mappings
        :param ray_radius: Ray Radius, Width of rays (especially useful when raycasting against vertices or edges)
        :param islands_precision: Islands Precision, Factor controlling precision of islands handling (the higher, the better the results)
        :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types
        :param layers_select_dst: Destination Layers Matching, How to match source and destination layers
        :param mix_mode: Mix Mode, How to affect destination elements with source values
        :param mix_factor: Mix Factor, Factor to use when applying data to destination (exact behavior depends on mix mode)
    """

def datalayout_transfer(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
    data_type: typing.Literal[
        "VGROUP_WEIGHTS",
        "BEVEL_WEIGHT_VERT",
        "COLOR_VERTEX",
        "SHARP_EDGE",
        "SEAM",
        "CREASE",
        "BEVEL_WEIGHT_EDGE",
        "FREESTYLE_EDGE",
        "CUSTOM_NORMAL",
        "COLOR_CORNER",
        "UV",
        "SMOOTH",
        "FREESTYLE_FACE",
    ]
    | None = "",
    use_delete: bool | None = False,
    layers_select_src: bpy.stub_internal.rna_enums.DtLayersSelectSrcItems
    | None = "ACTIVE",
    layers_select_dst: bpy.stub_internal.rna_enums.DtLayersSelectDstItems
    | None = "ACTIVE",
) -> None:
    """Transfer layout of data layer(s) from active to selected meshes

        :param modifier: Modifier, Name of the modifier to edit
        :param data_type: Data Type, Which data to transfer

    VGROUP_WEIGHTS
    Vertex Group(s) -- Transfer active or all vertex groups.

    BEVEL_WEIGHT_VERT
    Bevel Weight -- Transfer bevel weights.

    COLOR_VERTEX
    Colors -- Color Attributes.

    SHARP_EDGE
    Sharp -- Transfer sharp mark.

    SEAM
    UV Seam -- Transfer UV seam mark.

    CREASE
    Subdivision Crease -- Transfer crease values.

    BEVEL_WEIGHT_EDGE
    Bevel Weight -- Transfer bevel weights.

    FREESTYLE_EDGE
    Freestyle Mark -- Transfer Freestyle edge mark.

    CUSTOM_NORMAL
    Custom Normals -- Transfer custom normals.

    COLOR_CORNER
    Colors -- Color Attributes.

    UV
    UVs -- Transfer UV layers.

    SMOOTH
    Smooth -- Transfer flat/smooth mark.

    FREESTYLE_FACE
    Freestyle Mark -- Transfer Freestyle face mark.
        :param use_delete: Exact Match, Also delete some data layers from destination if necessary, so that it matches exactly source
        :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types
        :param layers_select_dst: Destination Layers Matching, How to match source and destination layers
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_global: bool | None = False,
    confirm: bool | None = True,
) -> None:
    """Delete selected objects

    :param use_global: Delete Globally, Remove object from all scenes
    :param confirm: Confirm, Prompt for confirmation
    """

def drop_geometry_nodes(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    session_uid: int | None = 0,
    show_datablock_in_modifier: bool | None = True,
) -> None:
    """Undocumented, consider contributing.

    :param session_uid: Session UID, Session UID of the geometry node group being dropped
    :param show_datablock_in_modifier: Show the datablock selector in the modifier
    """

def drop_named_material(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    session_uid: int | None = 0,
) -> None:
    """Undocumented, consider contributing.

    :param name: Name, Name of the data-block to use by the operator
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    """

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    linked: bool | None = False,
    mode: bpy.stub_internal.rna_enums.TransformModeTypeItems | None = "TRANSLATION",
) -> None:
    """Duplicate selected objects

    :param linked: Linked, Duplicate object but not object data, linking to the original data
    :param mode: Mode
    """

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    OBJECT_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Duplicate the selected objects and move them

    :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def duplicate_move_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    OBJECT_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Duplicate the selected objects, but not their object data, and move them

    :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def duplicates_make_real(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_base_parent: bool | None = False,
    use_hierarchy: bool | None = False,
) -> None:
    """Make instanced objects attached to this object real

    :param use_base_parent: Parent, Parent newly created objects to the original instancer
    :param use_hierarchy: Keep Hierarchy, Maintain parent child relationships
    """

def editmode_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle objects edit mode"""

def effector_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "FORCE",
        "WIND",
        "VORTEX",
        "MAGNET",
        "HARMONIC",
        "CHARGE",
        "LENNARDJ",
        "TEXTURE",
        "GUIDE",
        "BOID",
        "TURBULENCE",
        "DRAG",
        "FLUID",
    ]
    | None = "FORCE",
    radius: float | None = 1.0,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add an empty object with a physics effector to the scene

        :param type: Type
        :param radius: Radius
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def empty_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.ObjectEmptyDrawtypeItems | None = "PLAIN_AXES",
    radius: float | None = 1.0,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add an empty object to the scene

        :param type: Type
        :param radius: Radius
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def empty_image_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = True,
    filter_movie: bool | None = True,
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
    filemode: int | None = 9,
    relative_path: bool | None = True,
    show_multiview: bool | None = False,
    use_multiview: bool | None = False,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: typing.Literal[
        "DEFAULT",
        "FILE_SORT_ALPHA",
        "FILE_SORT_EXTENSION",
        "FILE_SORT_TIME",
        "FILE_SORT_SIZE",
        "ASSET_CATALOG",
    ]
    | None = "",
    name: str = "",
    session_uid: int | None = 0,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
    background: bool | None = False,
) -> None:
    """Add an empty image type to scene with data

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
        :param relative_path: Relative Path, Select the file relative to the blend file
        :param show_multiview: Enable Multi-View
        :param use_multiview: Use Multi-View
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

    DEFAULT
    Default -- Automatically determine sort method for files.

    FILE_SORT_ALPHA
    Name -- Sort the file list alphabetically.

    FILE_SORT_EXTENSION
    Extension -- Sort the file list by extension/type.

    FILE_SORT_TIME
    Modified Date -- Sort files by modification time.

    FILE_SORT_SIZE
    Size -- Sort files by size.

    ASSET_CATALOG
    Asset Catalog -- Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..
        :param name: Name, Name of the data-block to use by the operator
        :param session_uid: Session UID, Session UID of the data-block to use by the operator
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
        :param background: Put in Background, Make the image render behind all objects
    """

def explode_refresh(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Refresh data in the Explode modifier

    :param modifier: Modifier, Name of the modifier to edit
    """

def forcefield_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle objects force field"""

def geometry_node_bake_delete_single(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    session_uid: int | None = 0,
    modifier_name: str = "",
    bake_id: int | None = 0,
) -> None:
    """Delete baked data of a single bake node or simulation

    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :param modifier_name: Modifier Name, Name of the modifier that contains the node
    :param bake_id: Bake ID, Nested node id of the node
    """

def geometry_node_bake_pack_single(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    session_uid: int | None = 0,
    modifier_name: str = "",
    bake_id: int | None = 0,
) -> None:
    """Pack baked data from disk into the .blend file

    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :param modifier_name: Modifier Name, Name of the modifier that contains the node
    :param bake_id: Bake ID, Nested node id of the node
    """

def geometry_node_bake_single(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    session_uid: int | None = 0,
    modifier_name: str = "",
    bake_id: int | None = 0,
) -> None:
    """Bake a single bake node or simulation

    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :param modifier_name: Modifier Name, Name of the modifier that contains the node
    :param bake_id: Bake ID, Nested node id of the node
    """

def geometry_node_bake_unpack_single(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    session_uid: int | None = 0,
    modifier_name: str = "",
    bake_id: int | None = 0,
    method: typing.Literal["USE_LOCAL", "WRITE_LOCAL", "USE_ORIGINAL", "WRITE_ORIGINAL"]
    | None = "USE_LOCAL",
) -> None:
    """Unpack baked data from the .blend file to disk

    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :param modifier_name: Modifier Name, Name of the modifier that contains the node
    :param bake_id: Bake ID, Nested node id of the node
    :param method: Method, How to unpack
    """

def geometry_node_tree_copy_assign(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the active geometry node group and assign it to the active modifier"""

def geometry_nodes_input_attribute_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    input_name: str = "",
    modifier_name: str = "",
) -> None:
    """Switch between an attribute and a single value to define the data for every element

    :param input_name: Input Name
    :param modifier_name: Modifier Name
    """

def geometry_nodes_move_to_nodes(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_selected_objects: bool | None = False,
) -> None:
    """Move inputs and outputs from in the modifier to a new node group

    :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object
    """

def grease_pencil_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.ObjectGpencilTypeItems | None = "EMPTY",
    use_in_front: bool | None = True,
    stroke_depth_offset: float | None = 0.05,
    use_lights: bool | None = False,
    stroke_depth_order: typing.Literal["2D", "3D"] | None = "3D",
    radius: float | None = 1.0,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add a Grease Pencil object to the scene

        :param type: Type
        :param use_in_front: Show In Front, Show Line Art Grease Pencil in front of everything
        :param stroke_depth_offset: Stroke Offset, Stroke offset for the Line Art modifier
        :param use_lights: Use Lights, Use lights for this Grease Pencil object
        :param stroke_depth_order: Stroke Depth Order, Defines how the strokes are ordered in 3D space (for objects not displayed In Front)

    2D
    2D Layers -- Display strokes using Grease Pencil layers to define order.

    3D
    3D Location -- Display strokes using real 3D position in 3D space.
        :param radius: Radius
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def grease_pencil_dash_modifier_segment_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Add a segment to the dash modifier

    :param modifier: Modifier, Name of the modifier to edit
    """

def grease_pencil_dash_modifier_segment_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
    type: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move the active dash segment up or down

    :param modifier: Modifier, Name of the modifier to edit
    :param type: Type
    """

def grease_pencil_dash_modifier_segment_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
    index: int | None = 0,
) -> None:
    """Remove the active segment from the dash modifier

    :param modifier: Modifier, Name of the modifier to edit
    :param index: Index, Index of the segment to remove
    """

def grease_pencil_time_modifier_segment_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Add a segment to the time modifier

    :param modifier: Modifier, Name of the modifier to edit
    """

def grease_pencil_time_modifier_segment_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
    type: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move the active time segment up or down

    :param modifier: Modifier, Name of the modifier to edit
    :param type: Type
    """

def grease_pencil_time_modifier_segment_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
    index: int | None = 0,
) -> None:
    """Remove the active segment from the time modifier

    :param modifier: Modifier, Name of the modifier to edit
    :param index: Index, Index of the segment to remove
    """

def hide_collection(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    collection_index: int | None = -1,
    toggle: bool | None = False,
    extend: bool | None = False,
) -> None:
    """Show only objects in collection (Shift to extend)

    :param collection_index: Collection Index, Index of the collection to change visibility
    :param toggle: Toggle, Toggle visibility
    :param extend: Extend, Extend visibility
    """

def hide_render_clear_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reveal all render objects by setting the hide render flag"""

def hide_view_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
) -> None:
    """Reveal temporarily hidden objects

    :param select: Select, Select revealed objects
    """

def hide_view_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Temporarily hide objects from the viewport

    :param unselected: Unselected, Hide unselected rather than selected objects
    """

def hook_add_newob(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Hook selected vertices to a newly created object"""

def hook_add_selob(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_bone: bool | None = False,
) -> None:
    """Hook selected vertices to the first selected object

    :param use_bone: Active Bone, Assign the hook to the hook objects active bone
    """

def hook_assign(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str | None = "",
) -> None:
    """Assign the selected vertices to a hook

    :param modifier: Modifier, Modifier number to assign to
    """

def hook_recenter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str | None = "",
) -> None:
    """Set hook center to cursor position

    :param modifier: Modifier, Modifier number to assign to
    """

def hook_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str | None = "",
) -> None:
    """Remove a hook from the active object

    :param modifier: Modifier, Modifier number to remove
    """

def hook_reset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str | None = "",
) -> None:
    """Recalculate and clear offset transformation

    :param modifier: Modifier, Modifier number to assign to
    """

def hook_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str | None = "",
) -> None:
    """Select affected vertices on mesh

    :param modifier: Modifier, Modifier number to remove
    """

def instance_offset_from_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set offset used for collection instances based on cursor position"""

def instance_offset_from_object(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set offset used for collection instances based on the active object position"""

def instance_offset_to_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set cursor position to the offset used for collection instances"""

def isolate_type_render(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Hide unselected render objects of same type as active by setting the hide render flag"""

def join(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Join selected objects into active object"""

def join_shapes(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the current resulting shape of another selected object to this one"""

def join_uvs(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Transfer UV Maps from active to selected objects (needs matching geometry)"""

def laplaciandeform_bind(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Bind mesh to system in laplacian deform modifier

    :param modifier: Modifier, Name of the modifier to edit
    """

def light_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.LightTypeItems | None = "POINT",
    radius: float | None = 1.0,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add a light object to the scene

        :param type: Type
        :param radius: Radius
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def light_linking_blocker_collection_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create new light linking collection used by the active emitter"""

def light_linking_blockers_link(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    link_state: typing.Literal["INCLUDE", "EXCLUDE"] | None = "INCLUDE",
) -> None:
    """Light link selected blockers to the active emitter object

        :param link_state: Link State, State of the shadow linking

    INCLUDE
    Include -- Include selected blockers to cast shadows from the active emitter.

    EXCLUDE
    Exclude -- Exclude selected blockers from casting shadows from the active emitter.
    """

def light_linking_blockers_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all objects which block light from this emitter"""

def light_linking_receiver_collection_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create new light linking collection used by the active emitter"""

def light_linking_receivers_link(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    link_state: typing.Literal["INCLUDE", "EXCLUDE"] | None = "INCLUDE",
) -> None:
    """Light link selected receivers to the active emitter object

        :param link_state: Link State, State of the light linking

    INCLUDE
    Include -- Include selected receivers to receive light from the active emitter.

    EXCLUDE
    Exclude -- Exclude selected receivers from receiving light from the active emitter.
    """

def light_linking_receivers_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all objects which receive light from this emitter"""

def light_linking_unlink_from_collection(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove this object or collection from the light linking collection"""

def lightprobe_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["SPHERE", "PLANE", "VOLUME"] | None = "SPHERE",
    radius: float | None = 1.0,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add a light probe object

        :param type: Type

    SPHERE
    Sphere -- Light probe that captures precise lighting from all directions at a single point in space.

    PLANE
    Plane -- Light probe that captures incoming light from a single direction on a plane.

    VOLUME
    Volume -- Light probe that captures low frequency lighting inside a volume.
        :param radius: Radius
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def lightprobe_cache_bake(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    subset: typing.Literal["ALL", "SELECTED", "ACTIVE"] | None = "ALL",
) -> None:
    """Bake irradiance volume light cache

        :param subset: Subset, Subset of probes to update

    ALL
    All Volumes -- Bake all light probe volumes.

    SELECTED
    Selected Only -- Only bake selected light probe volumes.

    ACTIVE
    Active Only -- Only bake the active light probe volume.
    """

def lightprobe_cache_free(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    subset: typing.Literal["ALL", "SELECTED", "ACTIVE"] | None = "SELECTED",
) -> None:
    """Delete cached indirect lighting

        :param subset: Subset, Subset of probes to update

    ALL
    All Light Probes -- Delete all light probes baked lighting data.

    SELECTED
    Selected Only -- Only delete selected light probes baked lighting data.

    ACTIVE
    Active Only -- Only delete the active light probes baked lighting data.
    """

def lineart_bake_strokes(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    bake_all: bool | None = False,
) -> None:
    """Bake Line Art for current Grease Pencil object

    :param bake_all: Bake All, Bake all Line Art modifiers
    """

def lineart_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear_all: bool | None = False,
) -> None:
    """Clear all strokes in current Grease Pencil object

    :param clear_all: Clear All, Clear all Line Art modifier bakes
    """

def link_to_collection(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    collection_index: int | None = -1,
    is_new: bool | None = False,
    new_collection_name: str = "",
) -> None:
    """Link objects to a collection

    :param collection_index: Collection Index, Index of the collection to move to
    :param is_new: New, Move objects to a new collection
    :param new_collection_name: Name, Name of the newly added collection
    """

def location_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear_delta: bool | None = False,
) -> None:
    """Clear the objects location

    :param clear_delta: Clear Delta, Clear delta location in addition to clearing the normal location transform
    """

def make_dupli_face(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Convert objects into instanced faces"""

def make_links_data(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "OBDATA",
        "MATERIAL",
        "ANIMATION",
        "GROUPS",
        "DUPLICOLLECTION",
        "FONTS",
        "MODIFIERS",
        "EFFECTS",
    ]
    | None = "OBDATA",
) -> None:
    """Transfer data from active object to selected objects

        :param type: Type

    OBDATA
    Link Object Data -- Replace assigned Object Data.

    MATERIAL
    Link Materials -- Replace assigned Materials.

    ANIMATION
    Link Animation Data -- Replace assigned Animation Data.

    GROUPS
    Link Collections -- Replace assigned Collections.

    DUPLICOLLECTION
    Link Instance Collection -- Replace assigned Collection Instance.

    FONTS
    Link Fonts to Text -- Replace Text object Fonts.

    MODIFIERS
    Copy Modifiers -- Replace Modifiers.

    EFFECTS
    Copy Grease Pencil Effects -- Replace Grease Pencil Effects.
    """

def make_links_scene(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    scene: str | None = "",
) -> None:
    """Link selection to another scene

    :param scene: Scene
    """

def make_local(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "SELECT_OBJECT", "SELECT_OBDATA", "SELECT_OBDATA_MATERIAL", "ALL"
    ]
    | None = "SELECT_OBJECT",
) -> None:
    """Make library linked data-blocks local to this file

    :param type: Type
    """

def make_override_library(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    collection: int | None = 0,
) -> None:
    """Create a local override of the selected linked objects, and their hierarchy of dependencies

    :param collection: Override Collection, Session UID of the directly linked collection containing the selected object, to make an override from
    """

def make_single_user(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["SELECTED_OBJECTS", "ALL"] | None = "SELECTED_OBJECTS",
    object: bool | None = False,
    obdata: bool | None = False,
    material: bool | None = False,
    animation: bool | None = False,
    obdata_animation: bool | None = False,
) -> None:
    """Make linked data local to each object

    :param type: Type
    :param object: Object, Make single user objects
    :param obdata: Object Data, Make single user object data
    :param material: Materials, Make materials local to each data-block
    :param animation: Object Animation, Make object animation data local to each object
    :param obdata_animation: Object Data Animation, Make object data (mesh, curve etc.) animation data local to each object
    """

def material_slot_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a new material slot"""

def material_slot_assign(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Assign active material slot to selection"""

def material_slot_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy material to selected objects"""

def material_slot_deselect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Deselect by active material slot"""

def material_slot_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move the active material up/down in the list

    :param direction: Direction, Direction to move the active material towards
    """

def material_slot_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the selected material slot"""

def material_slot_remove_unused(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove unused material slots"""

def material_slot_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select by active material slot"""

def meshdeform_bind(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Bind mesh to cage in mesh deform modifier

    :param modifier: Modifier, Name of the modifier to edit
    """

def metaball_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.MetaelemTypeItems | None = "BALL",
    radius: float | None = 2.0,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add an metaball object to the scene

        :param type: Primitive
        :param radius: Radius
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def mode_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: bpy.stub_internal.rna_enums.ObjectModeItems | None = "OBJECT",
    toggle: bool | None = False,
) -> None:
    """Sets the object interaction mode

    :param mode: Mode
    :param toggle: Toggle
    """

def mode_set_with_submode(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: bpy.stub_internal.rna_enums.ObjectModeItems | None = "OBJECT",
    toggle: bool | None = False,
    mesh_select_mode: set[bpy.stub_internal.rna_enums.MeshSelectModeItems] | None = {},
) -> None:
    """Sets the object interaction mode

    :param mode: Mode
    :param toggle: Toggle
    :param mesh_select_mode: Mesh Mode
    """

def modifier_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.ObjectModifierTypeItems | None = "SUBSURF",
    use_selected_objects: bool | None = False,
) -> None:
    """Add a procedural operation/effect to the active object

    :param type: Type
    :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object
    """

def modifier_add_node_group(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    asset_library_type: bpy.stub_internal.rna_enums.AssetLibraryTypeItems
    | None = "LOCAL",
    asset_library_identifier: str = "",
    relative_asset_identifier: str = "",
    session_uid: int | None = 0,
    use_selected_objects: bool | None = False,
) -> None:
    """Add a procedural operation/effect to the active object

    :param asset_library_type: Asset Library Type
    :param asset_library_identifier: Asset Library Identifier
    :param relative_asset_identifier: Relative Asset Identifier
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object
    """

def modifier_apply(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
    report: bool | None = False,
    merge_customdata: bool | None = True,
    single_user: bool | None = False,
    all_keyframes: bool | None = False,
    use_selected_objects: bool | None = False,
) -> None:
    """Apply modifier and remove from the stack

    :param modifier: Modifier, Name of the modifier to edit
    :param report: Report, Create a notification after the operation
    :param merge_customdata: Merge UVs, For mesh objects, merge UV coordinates that share a vertex to account for imprecision in some modifiers
    :param single_user: Make Data Single User, Make the objects data single user if needed
    :param all_keyframes: Apply to all keyframes, For Grease Pencil objects, apply the modifier to all the keyframes
    :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object
    """

def modifier_apply_as_shapekey(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keep_modifier: bool | None = False,
    modifier: str = "",
    report: bool | None = False,
    use_selected_objects: bool | None = False,
) -> None:
    """Apply modifier as a new shape key and remove from the stack

    :param keep_modifier: Keep Modifier, Do not remove the modifier from stack
    :param modifier: Modifier, Name of the modifier to edit
    :param report: Report, Create a notification after the operation
    :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object
    """

def modifier_convert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Convert particles to a mesh object

    :param modifier: Modifier, Name of the modifier to edit
    """

def modifier_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
    use_selected_objects: bool | None = False,
) -> None:
    """Duplicate modifier at the same position in the stack

    :param modifier: Modifier, Name of the modifier to edit
    :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object
    """

def modifier_copy_to_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Copy the modifier from the active object to all selected objects

    :param modifier: Modifier, Name of the modifier to edit
    """

def modifier_move_down(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Move modifier down in the stack

    :param modifier: Modifier, Name of the modifier to edit
    """

def modifier_move_to_index(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
    index: int | None = 0,
    use_selected_objects: bool | None = False,
) -> None:
    """Change the modifiers index in the stack so it evaluates after the set number of others

    :param modifier: Modifier, Name of the modifier to edit
    :param index: Index, The index to move the modifier to
    :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object
    """

def modifier_move_up(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Move modifier up in the stack

    :param modifier: Modifier, Name of the modifier to edit
    """

def modifier_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
    report: bool | None = False,
    use_selected_objects: bool | None = False,
) -> None:
    """Remove a modifier from the active object

    :param modifier: Modifier, Name of the modifier to edit
    :param report: Report, Create a notification after the operation
    :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object
    """

def modifier_set_active(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Activate the modifier to use as the context

    :param modifier: Modifier, Name of the modifier to edit
    """

def modifiers_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear all modifiers from the selected objects"""

def modifiers_copy_to_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy modifiers to other selected objects"""

def move_to_collection(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    collection_index: int | None = -1,
    is_new: bool | None = False,
    new_collection_name: str = "",
) -> None:
    """Move objects to a collection

    :param collection_index: Collection Index, Index of the collection to move to
    :param is_new: New, Move objects to a new collection
    :param new_collection_name: Name, Name of the newly added collection
    """

def multires_base_apply(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Modify the base mesh to conform to the displaced mesh

    :param modifier: Modifier, Name of the modifier to edit
    """

def multires_external_pack(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Pack displacements from an external file"""

def multires_external_save(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
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
    filter_btx: bool | None = True,
    filter_collada: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    relative_path: bool | None = True,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    modifier: str = "",
) -> None:
    """Save displacements to an external file

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
        :param modifier: Modifier, Name of the modifier to edit
    """

def multires_higher_levels_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Deletes the higher resolution mesh, potential loss of detail

    :param modifier: Modifier, Name of the modifier to edit
    """

def multires_rebuild_subdiv(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Rebuilds all possible subdivisions levels to generate a lower resolution base mesh

    :param modifier: Modifier, Name of the modifier to edit
    """

def multires_reshape(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Copy vertex coordinates from other object

    :param modifier: Modifier, Name of the modifier to edit
    """

def multires_subdivide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
    mode: typing.Literal["CATMULL_CLARK", "SIMPLE", "LINEAR"] | None = "CATMULL_CLARK",
) -> None:
    """Add a new level of subdivision

        :param modifier: Modifier, Name of the modifier to edit
        :param mode: Subdivision Mode, How the mesh is going to be subdivided to create a new level

    CATMULL_CLARK
    Catmull-Clark -- Create a new level using Catmull-Clark subdivisions.

    SIMPLE
    Simple -- Create a new level using simple subdivisions.

    LINEAR
    Linear -- Create a new level using linear interpolation of the sculpted displacement.
    """

def multires_unsubdivide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Rebuild a lower subdivision level of the current base mesh

    :param modifier: Modifier, Name of the modifier to edit
    """

def ocean_bake(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
    free: bool | None = False,
) -> None:
    """Bake an image sequence of ocean data

    :param modifier: Modifier, Name of the modifier to edit
    :param free: Free, Free the bake, rather than generating it
    """

def origin_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear the objects origin"""

def origin_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "GEOMETRY_ORIGIN",
        "ORIGIN_GEOMETRY",
        "ORIGIN_CURSOR",
        "ORIGIN_CENTER_OF_MASS",
        "ORIGIN_CENTER_OF_VOLUME",
    ]
    | None = "GEOMETRY_ORIGIN",
    center: typing.Literal["MEDIAN", "BOUNDS"] | None = "MEDIAN",
) -> None:
    """Set the objects origin, by either moving the data, or set to center of data, or use 3D cursor

        :param type: Type

    GEOMETRY_ORIGIN
    Geometry to Origin -- Move object geometry to object origin.

    ORIGIN_GEOMETRY
    Origin to Geometry -- Calculate the center of geometry based on the current pivot point (median, otherwise bounding box).

    ORIGIN_CURSOR
    Origin to 3D Cursor -- Move object origin to position of the 3D cursor.

    ORIGIN_CENTER_OF_MASS
    Origin to Center of Mass (Surface) -- Calculate the center of mass from the surface area.

    ORIGIN_CENTER_OF_VOLUME
    Origin to Center of Mass (Volume) -- Calculate the center of mass from the volume (must be manifold geometry with consistent normals).
        :param center: Center
    """

def parent_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CLEAR", "CLEAR_KEEP_TRANSFORM", "CLEAR_INVERSE"]
    | None = "CLEAR",
) -> None:
    """Clear the objects parenting

        :param type: Type

    CLEAR
    Clear Parent -- Completely clear the parenting relationship, including involved modifiers if any.

    CLEAR_KEEP_TRANSFORM
    Clear and Keep Transformation -- As Clear Parent, but keep the current visual transformations of the object.

    CLEAR_INVERSE
    Clear Parent Inverse -- Reset the transform corrections applied to the parenting relationship, does not remove parenting itself.
    """

def parent_inverse_apply(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Apply the objects parent inverse to its data"""

def parent_no_inverse_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keep_transform: bool | None = False,
) -> None:
    """Set the objects parenting without setting the inverse parent correction

    :param keep_transform: Keep Transform, Preserve the world transform throughout parenting
    """

def parent_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "OBJECT",
        "ARMATURE",
        "ARMATURE_NAME",
        "ARMATURE_AUTO",
        "ARMATURE_ENVELOPE",
        "BONE",
        "BONE_RELATIVE",
        "CURVE",
        "FOLLOW",
        "PATH_CONST",
        "LATTICE",
        "VERTEX",
        "VERTEX_TRI",
    ]
    | None = "OBJECT",
    xmirror: bool | None = False,
    keep_transform: bool | None = False,
) -> None:
    """Set the objects parenting

    :param type: Type
    :param xmirror: X Mirror, Apply weights symmetrically along X axis, for Envelope/Automatic vertex groups creation
    :param keep_transform: Keep Transform, Apply transformation before parenting
    """

def particle_system_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a particle system"""

def particle_system_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the selected particle system"""

def paths_calculate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    display_type: bpy.stub_internal.rna_enums.MotionpathDisplayTypeItems
    | None = "RANGE",
    range: bpy.stub_internal.rna_enums.MotionpathRangeItems | None = "SCENE",
) -> None:
    """Generate motion paths for the selected objects

    :param display_type: Display type
    :param range: Computation Range
    """

def paths_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_selected: bool | None = False,
) -> None:
    """Undocumented, consider contributing.

    :param only_selected: Only Selected, Only clear motion paths of selected objects
    """

def paths_update(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Recalculate motion paths for selected objects"""

def paths_update_visible(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Recalculate all visible motion paths for objects and poses"""

def pointcloud_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add a point cloud object to the scene

        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def posemode_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Enable or disable posing/selecting bones"""

def quadriflow_remesh(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_mesh_symmetry: bool | None = True,
    use_preserve_sharp: bool | None = False,
    use_preserve_boundary: bool | None = False,
    preserve_attributes: bool | None = False,
    smooth_normals: bool | None = False,
    mode: typing.Literal["RATIO", "EDGE", "FACES"] | None = "FACES",
    target_ratio: float | None = 1.0,
    target_edge_length: float | None = 0.1,
    target_faces: int | None = 4000,
    mesh_area: float | None = -1.0,
    seed: int | None = 0,
) -> None:
    """Create a new quad based mesh using the surface data of the current mesh. All data layers will be lost

        :param use_mesh_symmetry: Use Mesh Symmetry, Generates a symmetrical mesh using the mesh symmetry configuration
        :param use_preserve_sharp: Preserve Sharp, Try to preserve sharp features on the mesh
        :param use_preserve_boundary: Preserve Mesh Boundary, Try to preserve mesh boundary on the mesh
        :param preserve_attributes: Preserve Attributes, Reproject attributes onto the new mesh
        :param smooth_normals: Smooth Normals, Set the output mesh normals to smooth
        :param mode: Mode, How to specify the amount of detail for the new mesh

    RATIO
    Ratio -- Specify target number of faces relative to the current mesh.

    EDGE
    Edge Length -- Input target edge length in the new mesh.

    FACES
    Faces -- Input target number of faces in the new mesh.
        :param target_ratio: Ratio, Relative number of faces compared to the current mesh
        :param target_edge_length: Edge Length, Target edge length in the new mesh
        :param target_faces: Number of Faces, Approximate number of faces (quads) in the new mesh
        :param mesh_area: Old Object Face Area, This property is only used to cache the object area for later calculations
        :param seed: Seed, Random seed to use with the solver. Different seeds will cause the remesher to come up with different quad layouts on the mesh
    """

def quick_explode(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    style: typing.Literal["EXPLODE", "BLEND"] | None = "EXPLODE",
    amount: int | None = 100,
    frame_duration: int | None = 50,
    frame_start: int | None = 1,
    frame_end: int | None = 10,
    velocity: float | None = 1.0,
    fade: bool | None = True,
) -> None:
    """Make selected objects explode

    :param style: Explode Style
    :param amount: Number of Pieces
    :param frame_duration: Duration
    :param frame_start: Start Frame
    :param frame_end: End Frame
    :param velocity: Outwards Velocity
    :param fade: Fade, Fade the pieces over time
    """

def quick_fur(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    density: typing.Literal["LOW", "MEDIUM", "HIGH"] | None = "MEDIUM",
    length: float | None = 0.1,
    radius: float | None = 0.001,
    view_percentage: float | None = 1.0,
    apply_hair_guides: bool | None = True,
    use_noise: bool | None = True,
    use_frizz: bool | None = True,
) -> None:
    """Add a fur setup to the selected objects

    :param density: Density
    :param length: Length
    :param radius: Hair Radius
    :param view_percentage: View Percentage
    :param apply_hair_guides: Apply Hair Guides
    :param use_noise: Noise
    :param use_frizz: Frizz
    """

def quick_liquid(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    show_flows: bool | None = False,
) -> None:
    """Make selected objects liquid

    :param show_flows: Render Liquid Objects, Keep the liquid objects visible during rendering
    """

def quick_smoke(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    style: typing.Literal["SMOKE", "FIRE", "BOTH"] | None = "SMOKE",
    show_flows: bool | None = False,
) -> None:
    """Use selected objects as smoke emitters

    :param style: Smoke Style
    :param show_flows: Render Smoke Objects, Keep the smoke objects visible during rendering
    """

def randomize_transform(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    random_seed: int | None = 0,
    use_delta: bool | None = False,
    use_loc: bool | None = True,
    loc: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
    use_rot: bool | None = True,
    rot: collections.abc.Sequence[float] | mathutils.Euler | None = (0.0, 0.0, 0.0),
    use_scale: bool | None = True,
    scale_even: bool | None = False,
    scale: collections.abc.Iterable[float] | None = (1.0, 1.0, 1.0),
) -> None:
    """Randomize objects location, rotation, and scale

    :param random_seed: Random Seed, Seed value for the random generator
    :param use_delta: Transform Delta, Randomize delta transform values instead of regular transform
    :param use_loc: Randomize Location, Randomize the location values
    :param loc: Location, Maximum distance the objects can spread over each axis
    :param use_rot: Randomize Rotation, Randomize the rotation values
    :param rot: Rotation, Maximum rotation over each axis
    :param use_scale: Randomize Scale, Randomize the scale values
    :param scale_even: Scale Even, Use the same scale value for all axis
    :param scale: Scale, Maximum scale randomization over each axis
    """

def reset_override_library(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset the selected local overrides to their linked references values"""

def rotation_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear_delta: bool | None = False,
) -> None:
    """Clear the objects rotation

    :param clear_delta: Clear Delta, Clear delta rotation in addition to clearing the normal rotation transform
    """

def scale_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear_delta: bool | None = False,
) -> None:
    """Clear the objects scale

    :param clear_delta: Clear Delta, Clear delta scale in addition to clearing the normal scale transform
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Change selection of all visible objects in scene

        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
    """

def select_by_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    type: bpy.stub_internal.rna_enums.ObjectTypeItems | None = "MESH",
) -> None:
    """Select all visible objects that are of a type

    :param extend: Extend, Extend selection instead of deselecting everything first
    :param type: Type
    """

def select_camera(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
) -> None:
    """Select the active camera

    :param extend: Extend, Extend the selection
    """

def select_grouped(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    type: typing.Literal[
        "CHILDREN_RECURSIVE",
        "CHILDREN",
        "PARENT",
        "SIBLINGS",
        "TYPE",
        "COLLECTION",
        "HOOK",
        "PASS",
        "COLOR",
        "KEYINGSET",
        "LIGHT_TYPE",
    ]
    | None = "CHILDREN_RECURSIVE",
) -> None:
    """Select all visible objects grouped by various properties

        :param extend: Extend, Extend selection instead of deselecting everything first
        :param type: Type

    CHILDREN_RECURSIVE
    Children.

    CHILDREN
    Immediate Children.

    PARENT
    Parent.

    SIBLINGS
    Siblings -- Shared parent.

    TYPE
    Type -- Shared object type.

    COLLECTION
    Collection -- Shared collection.

    HOOK
    Hook.

    PASS
    Pass -- Render pass index.

    COLOR
    Color -- Object color.

    KEYINGSET
    Keying Set -- Objects included in active Keying Set.

    LIGHT_TYPE
    Light Type -- Matching light types.
    """

def select_hierarchy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["PARENT", "CHILD"] | None = "PARENT",
    extend: bool | None = False,
) -> None:
    """Select object relative to the active objects position in the hierarchy

    :param direction: Direction, Direction to select in the hierarchy
    :param extend: Extend, Extend the existing selection
    """

def select_less(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Deselect objects at the boundaries of parent/child relationships"""

def select_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    type: typing.Literal[
        "OBDATA", "MATERIAL", "DUPGROUP", "PARTICLE", "LIBRARY", "LIBRARY_OBDATA"
    ]
    | None = "OBDATA",
) -> None:
    """Select all visible objects that are linked

    :param extend: Extend, Extend selection instead of deselecting everything first
    :param type: Type
    """

def select_mirror(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
) -> None:
    """Select the mirror objects of the selected object e.g. "L.sword" and "R.sword"

    :param extend: Extend, Extend selection instead of deselecting everything first
    """

def select_more(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select connected parent/child objects"""

def select_pattern(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pattern: str = "*",
    case_sensitive: bool | None = False,
    extend: bool | None = True,
) -> None:
    """Select objects matching a naming pattern

    :param pattern: Pattern, Name filter using *, ? and [abc] unix style wildcards
    :param case_sensitive: Case Sensitive, Do a case sensitive compare
    :param extend: Extend, Extend the existing selection
    """

def select_random(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 0.5,
    seed: int | None = 0,
    action: typing.Literal["SELECT", "DESELECT"] | None = "SELECT",
) -> None:
    """Select or deselect random visible objects

        :param ratio: Ratio, Portion of items to select randomly
        :param seed: Random Seed, Seed for the random number generator
        :param action: Action, Selection action to execute

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.
    """

def select_same_collection(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    collection: str = "",
) -> None:
    """Select object in the same collection

    :param collection: Collection, Name of the collection to select
    """

def shade_auto_smooth(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_auto_smooth: bool | None = True,
    angle: float | None = 0.523599,
) -> None:
    """Add modifier to automatically set the sharpness of mesh edges based on the angle between the neighboring faces

    :param use_auto_smooth: Auto Smooth, Add modifier to set edge sharpness automatically
    :param angle: Angle, Maximum angle between face normals that will be considered as smooth
    """

def shade_flat(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keep_sharp_edges: bool | None = True,
) -> None:
    """Render and display faces uniform, using face normals

    :param keep_sharp_edges: Keep Sharp Edges, Dont remove sharp edges, which are redundant with faces shaded smooth
    """

def shade_smooth(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keep_sharp_edges: bool | None = True,
) -> None:
    """Render and display faces smooth, using interpolated vertex normals

    :param keep_sharp_edges: Keep Sharp Edges, Dont remove sharp edges. Tagged edges will remain sharp
    """

def shade_smooth_by_angle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle: float | None = 0.523599,
    keep_sharp_edges: bool | None = True,
) -> None:
    """Set the sharpness of mesh edges based on the angle between the neighboring faces

    :param angle: Angle, Maximum angle between face normals that will be considered as smooth
    :param keep_sharp_edges: Keep Sharp Edges, Only add sharp edges instead of clearing existing tags first
    """

def shaderfx_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.ObjectShaderfxTypeItems | None = "FX_BLUR",
) -> None:
    """Add a visual effect to the active object

    :param type: Type
    """

def shaderfx_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    shaderfx: str = "",
) -> None:
    """Duplicate effect at the same position in the stack

    :param shaderfx: Shader, Name of the shaderfx to edit
    """

def shaderfx_move_down(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    shaderfx: str = "",
) -> None:
    """Move effect down in the stack

    :param shaderfx: Shader, Name of the shaderfx to edit
    """

def shaderfx_move_to_index(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    shaderfx: str = "",
    index: int | None = 0,
) -> None:
    """Change the effects position in the list so it evaluates after the set number of others

    :param shaderfx: Shader, Name of the shaderfx to edit
    :param index: Index, The index to move the effect to
    """

def shaderfx_move_up(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    shaderfx: str = "",
) -> None:
    """Move effect up in the stack

    :param shaderfx: Shader, Name of the shaderfx to edit
    """

def shaderfx_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    shaderfx: str = "",
    report: bool | None = False,
) -> None:
    """Remove a effect from the active Grease Pencil object

    :param shaderfx: Shader, Name of the shaderfx to edit
    :param report: Report, Create a notification after the operation
    """

def shape_key_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    from_mix: bool | None = True,
) -> None:
    """Add shape key to the object

    :param from_mix: From Mix, Create the new shape key from the existing mix of keys
    """

def shape_key_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset the weights of all shape keys to 0 or to the closest value respecting the limits"""

def shape_key_lock(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["LOCK", "UNLOCK"] | None = "LOCK",
) -> None:
    """Change the lock state of all shape keys of active object

        :param action: Action, Lock action to execute on vertex groups

    LOCK
    Lock -- Lock all shape keys.

    UNLOCK
    Unlock -- Unlock all shape keys.
    """

def shape_key_mirror(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_topology: bool | None = False,
) -> None:
    """Mirror the current shape key along the local X axis

    :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)
    """

def shape_key_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["TOP", "UP", "DOWN", "BOTTOM"] | None = "TOP",
) -> None:
    """Move the active shape key up/down in the list

        :param type: Type

    TOP
    Top -- Top of the list.

    UP
    Up.

    DOWN
    Down.

    BOTTOM
    Bottom -- Bottom of the list.
    """

def shape_key_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
    apply_mix: bool | None = False,
) -> None:
    """Remove shape key from the object

    :param all: All, Remove all shape keys
    :param apply_mix: Apply Mix, Apply current mix of shape keys to the geometry before removing them
    """

def shape_key_retime(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Resets the timing for absolute shape keys"""

def shape_key_transfer(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["OFFSET", "RELATIVE_FACE", "RELATIVE_EDGE"] | None = "OFFSET",
    use_clamp: bool | None = False,
) -> None:
    """Copy the active shape key of another selected object to this one

        :param mode: Transformation Mode, Relative shape positions to the new shape method

    OFFSET
    Offset -- Apply the relative positional offset.

    RELATIVE_FACE
    Relative Face -- Calculate relative position (using faces).

    RELATIVE_EDGE
    Relative Edge -- Calculate relative position (using edges).
        :param use_clamp: Clamp Offset, Clamp the transformation to the distance each vertex moves in the original shape
    """

def simulation_nodes_cache_bake(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    selected: bool | None = False,
) -> None:
    """Bake simulations in geometry nodes modifiers

    :param selected: Selected, Bake cache on all selected objects
    """

def simulation_nodes_cache_calculate_to_frame(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    selected: bool | None = False,
) -> None:
    """Calculate simulations in geometry nodes modifiers from the start to current frame

    :param selected: Selected, Calculate all selected objects instead of just the active object
    """

def simulation_nodes_cache_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    selected: bool | None = False,
) -> None:
    """Delete cached/baked simulations in geometry nodes modifiers

    :param selected: Selected, Delete cache on all selected objects
    """

def skin_armature_create(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Create an armature that parallels the skin layout

    :param modifier: Modifier, Name of the modifier to edit
    """

def skin_loose_mark_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["MARK", "CLEAR"] | None = "MARK",
) -> None:
    """Mark/clear selected vertices as loose

        :param action: Action

    MARK
    Mark -- Mark selected vertices as loose.

    CLEAR
    Clear -- Set selected vertices as not loose.
    """

def skin_radii_equalize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Make skin radii of selected vertices equal on each axis"""

def skin_root_mark(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Mark selected vertices as roots"""

def speaker_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add a speaker object to the scene

        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def subdivision_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    level: int | None = 1,
    relative: bool | None = False,
) -> None:
    """Sets a Subdivision Surface level (1 to 5)

    :param level: Level
    :param relative: Relative, Apply the subdivision surface level as an offset relative to the current level
    """

def surfacedeform_bind(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Bind mesh to target in surface deform modifier

    :param modifier: Modifier, Name of the modifier to edit
    """

def text_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add a text object to the scene

        :param radius: Radius
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def track_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CLEAR", "CLEAR_KEEP_TRANSFORM"] | None = "CLEAR",
) -> None:
    """Clear tracking constraint or flag from object

    :param type: Type
    """

def track_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["DAMPTRACK", "TRACKTO", "LOCKTRACK"] | None = "DAMPTRACK",
) -> None:
    """Make the object track another object, using various methods/constraints

    :param type: Type
    """

def transfer_mode(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_flash_on_transfer: bool | None = True,
) -> None:
    """Switches the active object and assigns the same mode to a new one under the mouse cursor, leaving the active mode in the current one

    :param use_flash_on_transfer: Flash On Transfer, Flash the target object when transferring the mode
    """

def transform_apply(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: bool | None = True,
    rotation: bool | None = True,
    scale: bool | None = True,
    properties: bool | None = True,
    isolate_users: bool | None = False,
) -> None:
    """Apply the objects transformation to its data

    :param location: Location
    :param rotation: Rotation
    :param scale: Scale
    :param properties: Apply Properties, Modify properties such as curve vertex radius, font size and bone envelope
    :param isolate_users: Isolate Multi User Data, Create new object-data users if needed
    """

def transform_axis_target(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Interactively point cameras and lights to a location (Ctrl translates)"""

def transform_to_mouse(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    session_uid: int | None = 0,
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = (
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
    ),
    drop_x: int | None = 0,
    drop_y: int | None = 0,
) -> None:
    """Snap selected item(s) to the mouse location

    :param name: Name, Object name to place (uses the active object when this and session_uid are unset)
    :param session_uid: Session UUID, Session UUID of the object to place (uses the active object when this and name are unset)
    :param matrix: Matrix
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    """

def transforms_to_deltas(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["ALL", "LOC", "ROT", "SCALE"] | None = "ALL",
    reset_values: bool | None = True,
) -> None:
    """Convert normal object transforms to delta transforms, any existing delta transforms will be included as well

        :param mode: Mode, Which transforms to transfer

    ALL
    All Transforms -- Transfer location, rotation, and scale transforms.

    LOC
    Location -- Transfer location transforms only.

    ROT
    Rotation -- Transfer rotation transforms only.

    SCALE
    Scale -- Transfer scale transforms only.
        :param reset_values: Reset Values, Clear transform values after transferring to deltas
    """

def unlink_data(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

def vertex_group_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a new vertex group to the active object"""

def vertex_group_assign(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Assign the selected vertices to the active vertex group"""

def vertex_group_assign_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Assign the selected vertices to a new vertex group"""

def vertex_group_clean(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    group_select_mode: str | None = "",
    limit: float | None = 0.0,
    keep_single: bool | None = False,
) -> None:
    """Remove vertex group assignments which are not required

    :param group_select_mode: Subset, Define which subset of groups shall be used
    :param limit: Limit, Remove vertices which weight is below or equal to this limit
    :param keep_single: Keep Single, Keep verts assigned to at least one group when cleaning
    """

def vertex_group_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Make a copy of the active vertex group"""

def vertex_group_copy_to_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Replace vertex groups of selected objects by vertex groups of active object"""

def vertex_group_deselect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Deselect all selected vertices assigned to the active vertex group"""

def vertex_group_invert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    group_select_mode: str | None = "",
    auto_assign: bool | None = True,
    auto_remove: bool | None = True,
) -> None:
    """Invert active vertex groups weights

    :param group_select_mode: Subset, Define which subset of groups shall be used
    :param auto_assign: Add Weights, Add vertices from groups that have zero weight before inverting
    :param auto_remove: Remove Weights, Remove vertices from groups that have zero weight after inverting
    """

def vertex_group_levels(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    group_select_mode: str | None = "",
    offset: float | None = 0.0,
    gain: float | None = 1.0,
) -> None:
    """Add some offset and multiply with some gain the weights of the active vertex group

    :param group_select_mode: Subset, Define which subset of groups shall be used
    :param offset: Offset, Value to add to weights
    :param gain: Gain, Value to multiply weights by
    """

def vertex_group_limit_total(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    group_select_mode: str | None = "",
    limit: int | None = 4,
) -> None:
    """Limit deform weights associated with a vertex to a specified number by removing lowest weights

    :param group_select_mode: Subset, Define which subset of groups shall be used
    :param limit: Limit, Maximum number of deform weights
    """

def vertex_group_lock(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "LOCK", "UNLOCK", "INVERT"] | None = "TOGGLE",
    mask: typing.Literal["ALL", "SELECTED", "UNSELECTED", "INVERT_UNSELECTED"]
    | None = "ALL",
) -> None:
    """Change the lock state of all or some vertex groups of active object

        :param action: Action, Lock action to execute on vertex groups

    TOGGLE
    Toggle -- Unlock all vertex groups if there is at least one locked group, lock all in other case.

    LOCK
    Lock -- Lock all vertex groups.

    UNLOCK
    Unlock -- Unlock all vertex groups.

    INVERT
    Invert -- Invert the lock state of all vertex groups.
        :param mask: Mask, Apply the action based on vertex group selection

    ALL
    All -- Apply action to all vertex groups.

    SELECTED
    Selected -- Apply to selected vertex groups.

    UNSELECTED
    Unselected -- Apply to unselected vertex groups.

    INVERT_UNSELECTED
    Invert Unselected -- Apply the opposite of Lock/Unlock to unselected vertex groups.
    """

def vertex_group_mirror(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror_weights: bool | None = True,
    flip_group_names: bool | None = True,
    all_groups: bool | None = False,
    use_topology: bool | None = False,
) -> None:
    """Mirror vertex group, flip weights and/or names, editing only selected vertices, flipping when both sides are selected otherwise copy from unselected

    :param mirror_weights: Mirror Weights, Mirror weights
    :param flip_group_names: Flip Group Names, Flip vertex group names
    :param all_groups: All Groups, Mirror all vertex groups weights
    :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)
    """

def vertex_group_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move the active vertex group up/down in the list

    :param direction: Direction, Direction to move the active vertex group towards
    """

def vertex_group_normalize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Normalize weights of the active vertex group, so that the highest ones are now 1.0"""

def vertex_group_normalize_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    group_select_mode: str | None = "",
    lock_active: bool | None = True,
) -> None:
    """Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0

    :param group_select_mode: Subset, Define which subset of groups shall be used
    :param lock_active: Lock Active, Keep the values of the active group while normalizing others
    """

def vertex_group_quantize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    group_select_mode: str | None = "",
    steps: int | None = 4,
) -> None:
    """Set weights to a fixed number of steps

    :param group_select_mode: Subset, Define which subset of groups shall be used
    :param steps: Steps, Number of steps between 0 and 1
    """

def vertex_group_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
    all_unlocked: bool | None = False,
) -> None:
    """Delete the active or all vertex groups from the active object

    :param all: All, Remove all vertex groups
    :param all_unlocked: All Unlocked, Remove all unlocked vertex groups
    """

def vertex_group_remove_from(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_all_groups: bool | None = False,
    use_all_verts: bool | None = False,
) -> None:
    """Remove the selected vertices from active or all vertex group(s)

    :param use_all_groups: All Groups, Remove from all groups
    :param use_all_verts: All Vertices, Clear the active group
    """

def vertex_group_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all the vertices assigned to the active vertex group"""

def vertex_group_set_active(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    group: str | None = "",
) -> None:
    """Set the active vertex group

    :param group: Group, Vertex group to set as active
    """

def vertex_group_smooth(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    group_select_mode: str | None = "",
    factor: float | None = 0.5,
    repeat: int | None = 1,
    expand: float | None = 0.0,
) -> None:
    """Smooth weights for selected vertices

    :param group_select_mode: Subset, Define which subset of groups shall be used
    :param factor: Factor
    :param repeat: Iterations
    :param expand: Expand/Contract, Expand/contract weights
    """

def vertex_group_sort(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    sort_type: typing.Literal["NAME", "BONE_HIERARCHY"] | None = "NAME",
) -> None:
    """Sort vertex groups

    :param sort_type: Sort Type, Sort type
    """

def vertex_parent_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Parent selected objects to the selected vertices"""

def vertex_weight_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy weights from active to selected"""

def vertex_weight_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    weight_group: int | None = -1,
) -> None:
    """Delete this weight from the vertex (disabled if vertex group is locked)

    :param weight_group: Weight Index, Index of source weight in active vertex group
    """

def vertex_weight_normalize_active_vertex(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Normalize active vertexs weights"""

def vertex_weight_paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    weight_group: int | None = -1,
) -> None:
    """Copy this groups weight to other selected vertices (disabled if vertex group is locked)

    :param weight_group: Weight Index, Index of source weight in active vertex group
    """

def vertex_weight_set_active(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    weight_group: int | None = -1,
) -> None:
    """Set as active vertex group

    :param weight_group: Weight Index, Index of source weight in active vertex group
    """

def visual_transform_apply(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Apply the objects visual transformation to its data"""

def volume_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Add a volume object to the scene

        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def volume_import(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    hide_props_region: bool | None = True,
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
    filter_volume: bool | None = True,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    relative_path: bool | None = True,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    use_sequence_detection: bool | None = True,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Import OpenVDB volume file

        :param filepath: File Path, Path to file
        :param directory: Directory, Directory of the file
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
        :param use_sequence_detection: Detect Sequences, Automatically detect animated sequences in selected volume files (based on file names)
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location, Location for the newly added object
        :param rotation: Rotation, Rotation for the newly added object
        :param scale: Scale, Scale for the newly added object
    """

def voxel_remesh(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Calculates a new manifold mesh based on the volume of the current mesh. All data layers will be lost"""

def voxel_size_edit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Modify the mesh voxel size interactively used in the voxel remesher"""
