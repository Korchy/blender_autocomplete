import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

class add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        radius: float | None = 1.0,
        type: typing.Literal[bpy.stub_internal.rna_enums.ObjectTypeItems]
        | None = "EMPTY",
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add an object to the scene

                :param execution_context:
                :param undo:
                :param radius: Radius, (in [0, inf], optional)
                :param type: Type, (optional)
                :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class add_modifier_menu(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class add_named(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add named object

        :param execution_context:
        :param undo:
        :param linked: Linked, Duplicate object but not object data, linking to the original data (optional)
        :param name: Name, Name of the data-block to use by the operator (optional, never None)
        :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
        :param matrix: Matrix, (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)
        :param drop_x: Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
        :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class align(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        bb_quality: bool | None = True,
        align_mode: typing.Literal["OPT_1", "OPT_2", "OPT_3"] | None = "OPT_2",
        relative_to: typing.Literal["OPT_1", "OPT_2", "OPT_3", "OPT_4"]
        | None = "OPT_4",
        align_axis: set[typing.Literal["X", "Y", "Z"]] | None = set(),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Align objects

                :param execution_context:
                :param undo:
                :param bb_quality: High Quality, Enables high quality but slow calculation of the bounding box for perfect results on complex shape meshes with rotation/scale (optional)
                :param align_mode: Align Mode, Side of object to use for alignment (optional)
                :param relative_to: Relative To, Reference location to align to (optional)

        OPT_1
        Scene Origin -- Use the scene origin as the position for the selected objects to align to.

        OPT_2
        3D Cursor -- Use the 3D cursor as the position for the selected objects to align to.

        OPT_3
        Selection -- Use the selected objects as the position for the selected objects to align to.

        OPT_4
        Active -- Use the active object as the position for the selected objects to align to.
                :param align_axis: Align, Align to axis (optional)
                :return: Result of the operator call.
        """

class anim_transforms_to_deltas(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Convert object animation for normal transforms to delta transforms

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class armature_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add an armature object to the scene

                :param execution_context:
                :param undo:
                :param radius: Radius, (in [0, inf], optional)
                :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class assign_property_defaults(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        process_data: bool | None = True,
        process_bones: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Assign the current values of custom properties as their defaults, for use as part of the rest pose state in NLA track mixing

        :param execution_context:
        :param undo:
        :param process_data: Process data properties, (optional)
        :param process_bones: Process bone properties, (optional)
        :return: Result of the operator call.
        """

class bake(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[bpy.stub_internal.rna_enums.BakePassTypeItems]
        | None = "COMBINED",
        pass_filter: set[
            typing.Literal[bpy.stub_internal.rna_enums.BakePassFilterTypeItems]
        ]
        | None = set(),
        filepath: str = "",
        width: int | None = 512,
        height: int | None = 512,
        margin: int | None = 16,
        margin_type: typing.Literal[bpy.stub_internal.rna_enums.BakeMarginTypeItems]
        | None = "EXTEND",
        use_selected_to_active: bool | None = False,
        max_ray_distance: float | None = 0.0,
        cage_extrusion: float | None = 0.0,
        cage_object: str = "",
        normal_space: typing.Literal[bpy.stub_internal.rna_enums.NormalSpaceItems]
        | None = "TANGENT",
        normal_r: typing.Literal[bpy.stub_internal.rna_enums.NormalSwizzleItems]
        | None = "POS_X",
        normal_g: typing.Literal[bpy.stub_internal.rna_enums.NormalSwizzleItems]
        | None = "POS_Y",
        normal_b: typing.Literal[bpy.stub_internal.rna_enums.NormalSwizzleItems]
        | None = "POS_Z",
        target: typing.Literal[bpy.stub_internal.rna_enums.BakeTargetItems]
        | None = "IMAGE_TEXTURES",
        save_mode: typing.Literal[bpy.stub_internal.rna_enums.BakeSaveModeItems]
        | None = "INTERNAL",
        use_clear: bool | None = False,
        use_cage: bool | None = False,
        use_split_materials: bool | None = False,
        use_automatic_name: bool | None = False,
        uv_layer: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Bake image textures of selected objects

        :param execution_context:
        :param undo:
        :param type: Type, Type of pass to bake, some of them may not be supported by the current render engine (optional)
        :param pass_filter: Pass Filter, Filter to combined, diffuse, glossy, transmission and subsurface passes (optional)
        :param filepath: File Path, Image filepath to use when saving externally (optional, never None)
        :param width: Width, Horizontal dimension of the baking map (external only) (in [1, inf], optional)
        :param height: Height, Vertical dimension of the baking map (external only) (in [1, inf], optional)
        :param margin: Margin, Extends the baked result as a post process filter (in [0, inf], optional)
        :param margin_type: Margin Type, Which algorithm to use to generate the margin (optional)
        :param use_selected_to_active: Selected to Active, Bake shading on the surface of selected objects to the active object (optional)
        :param max_ray_distance: Max Ray Distance, The maximum ray distance for matching points between the active and selected objects. If zero, there is no limit (in [0, inf], optional)
        :param cage_extrusion: Cage Extrusion, Inflate the active object by the specified distance for baking. This helps matching to points nearer to the outside of the selected object meshes (in [0, inf], optional)
        :param cage_object: Cage Object, Object to use as cage, instead of calculating the cage from the active object with cage extrusion (optional, never None)
        :param normal_space: Normal Space, Choose normal space for baking (optional)
        :param normal_r: R, Axis to bake in red channel (optional)
        :param normal_g: G, Axis to bake in green channel (optional)
        :param normal_b: B, Axis to bake in blue channel (optional)
        :param target: Target, Where to output the baked map (optional)
        :param save_mode: Save Mode, Where to save baked image textures (optional)
        :param use_clear: Clear, Clear images before baking (only for internal saving) (optional)
        :param use_cage: Cage, Cast rays to active object from a cage (optional)
        :param use_split_materials: Split Materials, Split baked maps per material, using material name in output file (external only) (optional)
        :param use_automatic_name: Automatic Name, Automatically name the output file with the pass type (optional)
        :param uv_layer: UV Layer, UV layer to override active (optional, never None)
        :return: Result of the operator call.
        """

class bake_image(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Bake image textures of selected objects

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class camera_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a camera object to the scene

                :param execution_context:
                :param undo:
                :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class camera_custom_update(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Update custom camera with new parameters from the shader

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class clear_override_library(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete the selected local overrides and relink their usages to the linked data-blocks if possible, else reset them and mark them as non editable

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class collection_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add an object to a new collection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class collection_external_asset_drop(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
        use_instance: bool | None = True,
        drop_x: int | None = 0,
        drop_y: int | None = 0,
        collection: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add the dragged collection to the scene

                :param execution_context:
                :param undo:
                :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param use_instance: Instance, Add the dropped collection as collection instance (optional)
                :param drop_x: Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
                :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
                :param collection: Collection, (optional)
                :return: Result of the operator call.
        """

class collection_instance_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
        session_uid: int | None = 0,
        drop_x: int | None = 0,
        drop_y: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a collection instance

                :param execution_context:
                :param undo:
                :param name: Name, Collection name to add (optional, never None)
                :param collection: Collection, (optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
                :param drop_x: Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
                :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class collection_link(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        collection: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add an object to an existing collection

        :param execution_context:
        :param undo:
        :param collection: Collection, (optional)
        :return: Result of the operator call.
        """

class collection_objects_select(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all objects in collection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class collection_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the active object from this collection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class collection_unlink(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Unlink the collection from all objects

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class constraint_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a constraint to the active object

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class constraint_add_with_targets(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a constraint to the active object, with target (where applicable) set to the selected objects/bones

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class constraints_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear all constraints from the selected objects

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class constraints_copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy constraints to other selected objects

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class convert(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        target: typing.Literal["CURVE", "MESH", "POINTCLOUD", "CURVES", "GREASEPENCIL"]
        | None = "MESH",
        keep_original: bool | None = False,
        merge_customdata: bool | None = True,
        thickness: int | None = 5,
        faces: bool | None = True,
        offset: float | None = 0.01,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Convert selected objects to another type

                :param execution_context:
                :param undo:
                :param target: Target, Type of object to convert to (optional)

        CURVE
        Curve -- Curve from Mesh or Text objects.

        MESH
        Mesh -- Mesh from Curve, Surface, Metaball, Text, or Point Cloud objects.

        POINTCLOUD
        Point Cloud -- Point Cloud from Mesh objects.

        CURVES
        Curves -- Curves from evaluated curve data.

        GREASEPENCIL
        Grease Pencil -- Grease Pencil from Curve or Mesh objects.
                :param keep_original: Keep Original, Keep original objects instead of replacing them (optional)
                :param merge_customdata: Merge UVs, Merge UV coordinates that share a vertex to account for imprecision in some modifiers (optional)
                :param thickness: Thickness, (in [1, 100], optional)
                :param faces: Export Faces, Export faces as filled strokes (optional)
                :param offset: Stroke Offset, Offset strokes from fill (in [0, inf], optional)
                :return: Result of the operator call.
        """

class copy_global_transform(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copies the matrix of the currently active object or pose bone to the clipboard. Uses world-space matrices

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class copy_relative_transform(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copies the matrix of the currently active object or pose bone to the clipboard. Uses matrices relative to a specific object or the active scene camera

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class correctivesmooth_bind(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Bind base pose in Corrective Smooth modifier

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class curves_empty_hair_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add an empty curve object to the scene with the selected mesh as surface

                :param execution_context:
                :param undo:
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class curves_random_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a curves object with random curves to the scene

                :param execution_context:
                :param undo:
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class data_instance_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        session_uid: int | None = 0,
        type: typing.Literal[bpy.stub_internal.rna_enums.IdTypeItems] | None = "ACTION",
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
        drop_x: int | None = 0,
        drop_y: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add an object data instance

                :param execution_context:
                :param undo:
                :param name: Name, Name of the data-block to use by the operator (optional, never None)
                :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
                :param type: Type, (optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param drop_x: Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
                :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class data_transfer(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        | None = "VGROUP_WEIGHTS",
        use_create: bool | None = True,
        vert_mapping: typing.Literal[bpy.stub_internal.rna_enums.DtMethodVertexItems]
        | None = "NEAREST",
        edge_mapping: typing.Literal[bpy.stub_internal.rna_enums.DtMethodEdgeItems]
        | None = "NEAREST",
        loop_mapping: typing.Literal[bpy.stub_internal.rna_enums.DtMethodLoopItems]
        | None = "NEAREST_POLYNOR",
        poly_mapping: typing.Literal[bpy.stub_internal.rna_enums.DtMethodPolyItems]
        | None = "NEAREST",
        use_auto_transform: bool | None = False,
        use_object_transform: bool | None = True,
        use_max_distance: bool | None = False,
        max_distance: float | None = 1.0,
        ray_radius: float | None = 0.0,
        islands_precision: float | None = 0.1,
        layers_select_src: typing.Literal[
            bpy.stub_internal.rna_enums.DtLayersSelectSrcItems
        ]
        | None = "ACTIVE",
        layers_select_dst: typing.Literal[
            bpy.stub_internal.rna_enums.DtLayersSelectDstItems
        ]
        | None = "ACTIVE",
        mix_mode: typing.Literal[bpy.stub_internal.rna_enums.DtMixModeItems]
        | None = "REPLACE",
        mix_factor: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Transfer data layer(s) (weights, edge sharp, etc.) from active to selected meshes

                :param execution_context:
                :param undo:
                :param use_reverse_transfer: Reverse Transfer, Transfer from selected objects to active one (optional)
                :param use_freeze: Freeze Operator, Prevent changes to settings to re-run the operator, handy to change several things at once with heavy geometry (optional)
                :param data_type: Data Type, Which data to transfer (optional)

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
                :param use_create: Create Data, Add data layers on destination meshes if needed (optional)
                :param vert_mapping: Vertex Mapping, Method used to map source vertices to destination ones (optional)
                :param edge_mapping: Edge Mapping, Method used to map source edges to destination ones (optional)
                :param loop_mapping: Face Corner Mapping, Method used to map source faces corners to destination ones (optional)
                :param poly_mapping: Face Mapping, Method used to map source faces to destination ones (optional)
                :param use_auto_transform: Auto Transform, Automatically compute transformation to get the best possible match between source and destination meshes.Warning: Results will never be as good as manual matching of objects(optional)
                :param use_object_transform: Object Transform, Evaluate source and destination meshes in global space (optional)
                :param use_max_distance: Only Neighbor Geometry, Source elements must be closer than given distance from destination one (optional)
                :param max_distance: Max Distance, Maximum allowed distance between source and destination element, for non-topology mappings (in [0, inf], optional)
                :param ray_radius: Ray Radius, Width of rays (especially useful when raycasting against vertices or edges) (in [0, inf], optional)
                :param islands_precision: Islands Precision, Factor controlling precision of islands handling (the higher, the better the results) (in [0, 10], optional)
                :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types (optional)
                :param layers_select_dst: Destination Layers Matching, How to match source and destination layers (optional)
                :param mix_mode: Mix Mode, How to affect destination elements with source values (optional)
                :param mix_factor: Mix Factor, Factor to use when applying data to destination (exact behavior depends on mix mode) (in [0, 1], optional)
                :return: Result of the operator call.
        """

class datalayout_transfer(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        layers_select_src: typing.Literal[
            bpy.stub_internal.rna_enums.DtLayersSelectSrcItems
        ]
        | None = "ACTIVE",
        layers_select_dst: typing.Literal[
            bpy.stub_internal.rna_enums.DtLayersSelectDstItems
        ]
        | None = "ACTIVE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Transfer layout of data layer(s) from active to selected meshes

                :param execution_context:
                :param undo:
                :param modifier: Modifier, Name of the modifier to edit (optional, never None)
                :param data_type: Data Type, Which data to transfer (optional)

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
                :param use_delete: Exact Match, Also delete some data layers from destination if necessary, so that it matches exactly source (optional)
                :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types (optional)
                :param layers_select_dst: Destination Layers Matching, How to match source and destination layers (optional)
                :return: Result of the operator call.
        """

class delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_global: bool | None = False,
        confirm: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete selected objects

        :param execution_context:
        :param undo:
        :param use_global: Delete Globally, Remove object from all scenes (optional)
        :param confirm: Confirm, Prompt for confirmation (optional)
        :return: Result of the operator call.
        """

class delete_fix_to_camera_keys(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete all keys that were generated by the Fix to Scene Camera operator

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class drop_geometry_nodes(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        session_uid: int | None = 0,
        show_datablock_in_modifier: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param session_uid: Session UID, Session UID of the geometry node group being dropped (in [-inf, inf], optional)
        :param show_datablock_in_modifier: Show the data-block selector in the modifier, (optional)
        :return: Result of the operator call.
        """

class drop_named_material(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        session_uid: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param name: Name, Name of the data-block to use by the operator (optional, never None)
        :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class duplicate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        linked: bool | None = False,
        mode: typing.Literal[bpy.stub_internal.rna_enums.TransformModeTypeItems]
        | None = "TRANSLATION",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate selected objects

        :param execution_context:
        :param undo:
        :param linked: Linked, Duplicate object but not object data, linking to the original data (optional)
        :param mode: Mode, (optional)
        :return: Result of the operator call.
        """

class duplicate_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        OBJECT_OT_duplicate: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate the selected objects and move them

        :param execution_context:
        :param undo:
        :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects (optional, `bpy.ops.object.duplicate` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class duplicate_move_linked(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        OBJECT_OT_duplicate: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate the selected objects, but not their object data, and move them

        :param execution_context:
        :param undo:
        :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects (optional, `bpy.ops.object.duplicate` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class duplicates_make_real(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_base_parent: bool | None = False,
        use_hierarchy: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make instanced objects attached to this object real

        :param execution_context:
        :param undo:
        :param use_base_parent: Parent, Parent newly created objects to the original instancer (optional)
        :param use_hierarchy: Keep Hierarchy, Maintain parent child relationships (optional)
        :return: Result of the operator call.
        """

class editmode_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Toggle objects edit mode

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class effector_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add an empty object with a physics effector to the scene

                :param execution_context:
                :param undo:
                :param type: Type, (optional)
                :param radius: Radius, (in [0, inf], optional)
                :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class empty_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[bpy.stub_internal.rna_enums.ObjectEmptyDrawtypeItems]
        | None = "PLAIN_AXES",
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add an empty object to the scene

                :param execution_context:
                :param undo:
                :param type: Type, (optional)
                :param radius: Radius, (in [0, inf], optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class empty_image_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
        background: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add an empty image type to scene with data

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
                :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
                :param filter_blender: Filter .blend files, (optional)
                :param filter_backup: Filter backup .blend files, (optional)
                :param filter_image: Filter image files, (optional)
                :param filter_movie: Filter movie files, (optional)
                :param filter_python: Filter Python files, (optional)
                :param filter_font: Filter font files, (optional)
                :param filter_sound: Filter sound files, (optional)
                :param filter_text: Filter text files, (optional)
                :param filter_archive: Filter archive files, (optional)
                :param filter_btx: Filter btx files, (optional)
                :param filter_alembic: Filter Alembic files, (optional)
                :param filter_usd: Filter USD files, (optional)
                :param filter_obj: Filter OBJ files, (optional)
                :param filter_volume: Filter OpenVDB volume files, (optional)
                :param filter_folder: Filter folders, (optional)
                :param filter_blenlib: Filter Blender IDs, (optional)
                :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
                :param relative_path: Relative Path, Select the file relative to the blend file (optional)
                :param show_multiview: Enable Multi-View, (optional)
                :param use_multiview: Use Multi-View, (optional)
                :param display_type: Display Type, (optional)

        DEFAULT
        Default -- Automatically determine display type for files.

        LIST_VERTICAL
        Short List -- Display files as short list.

        LIST_HORIZONTAL
        Long List -- Display files as a detailed list.

        THUMBNAIL
        Thumbnails -- Display files as thumbnails.
                :param sort_method: File sorting mode, (optional)

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
                :param name: Name, Name of the data-block to use by the operator (optional, never None)
                :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param background: Put in Background, Make the image render behind all objects (optional)
                :return: Result of the operator call.
        """

class explode_refresh(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Refresh data in the Explode modifier

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class fix_to_camera(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_location: bool | None = True,
        use_rotation: bool | None = True,
        use_scale: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Generate new keys to fix the selected object/bone to the camera on unkeyed frames

        :param execution_context:
        :param undo:
        :param use_location: Location, Create Location keys when fixing to the scene camera (optional)
        :param use_rotation: Rotation, Create Rotation keys when fixing to the scene camera (optional)
        :param use_scale: Scale, Create Scale keys when fixing to the scene camera (optional)
        :return: Result of the operator call.
        """

class forcefield_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Toggle objects force field

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class geometry_node_bake_delete_single(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        session_uid: int | None = 0,
        modifier_name: str = "",
        bake_id: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete baked data of a single bake node or simulation

        :param execution_context:
        :param undo:
        :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
        :param modifier_name: Modifier Name, Name of the modifier that contains the node (optional, never None)
        :param bake_id: Bake ID, Nested node id of the node (in [0, inf], optional)
        :return: Result of the operator call.
        """

class geometry_node_bake_pack_single(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        session_uid: int | None = 0,
        modifier_name: str = "",
        bake_id: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Pack baked data from disk into the .blend file

        :param execution_context:
        :param undo:
        :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
        :param modifier_name: Modifier Name, Name of the modifier that contains the node (optional, never None)
        :param bake_id: Bake ID, Nested node id of the node (in [0, inf], optional)
        :return: Result of the operator call.
        """

class geometry_node_bake_single(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        session_uid: int | None = 0,
        modifier_name: str = "",
        bake_id: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Bake a single bake node or simulation

        :param execution_context:
        :param undo:
        :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
        :param modifier_name: Modifier Name, Name of the modifier that contains the node (optional, never None)
        :param bake_id: Bake ID, Nested node id of the node (in [0, inf], optional)
        :return: Result of the operator call.
        """

class geometry_node_bake_unpack_single(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        session_uid: int | None = 0,
        modifier_name: str = "",
        bake_id: int | None = 0,
        method: typing.Literal[
            "USE_LOCAL", "WRITE_LOCAL", "USE_ORIGINAL", "WRITE_ORIGINAL"
        ]
        | None = "USE_LOCAL",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Unpack baked data from the .blend file to disk

        :param execution_context:
        :param undo:
        :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
        :param modifier_name: Modifier Name, Name of the modifier that contains the node (optional, never None)
        :param bake_id: Bake ID, Nested node id of the node (in [0, inf], optional)
        :param method: Method, How to unpack (optional)
        :return: Result of the operator call.
        """

class geometry_node_tree_copy_assign(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate the active geometry node group and assign it to the active modifier

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class geometry_nodes_input_attribute_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        input_name: str = "",
        modifier_name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Switch between an attribute and a single value to define the data for every element

        :param execution_context:
        :param undo:
        :param input_name: Input Name, (optional, never None)
        :param modifier_name: Modifier Name, (optional, never None)
        :return: Result of the operator call.
        """

class geometry_nodes_move_to_nodes(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_selected_objects: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move inputs and outputs from in the modifier to a new node group

        :param execution_context:
        :param undo:
        :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object (optional)
        :return: Result of the operator call.
        """

class grease_pencil_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[bpy.stub_internal.rna_enums.ObjectGpencilTypeItems]
        | None = "EMPTY",
        use_in_front: bool | None = True,
        stroke_depth_offset: float | None = 0.05,
        use_lights: bool | None = True,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a Grease Pencil object to the scene

                :param execution_context:
                :param undo:
                :param type: Type, (optional)
                :param use_in_front: Show In Front, Show Line Art Grease Pencil in front of everything (optional)
                :param stroke_depth_offset: Stroke Offset, Stroke offset for the Line Art modifier (in [0, inf], optional)
                :param use_lights: Use Lights, Use lights for this Grease Pencil object (optional)
                :param stroke_depth_order: Stroke Depth Order, Defines how the strokes are ordered in 3D space (for objects not displayed In Front) (optional)

        2D
        2D Layers -- Display strokes using Grease Pencil layers to define order.

        3D
        3D Location -- Display strokes using real 3D position in 3D space.
                :param radius: Radius, (in [0, inf], optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class grease_pencil_dash_modifier_segment_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a segment to the dash modifier

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class grease_pencil_dash_modifier_segment_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
        type: typing.Literal["UP", "DOWN"] | None = "UP",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move the active dash segment up or down

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class grease_pencil_dash_modifier_segment_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
        index: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the active segment from the dash modifier

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :param index: Index, Index of the segment to remove (in [0, inf], optional)
        :return: Result of the operator call.
        """

class grease_pencil_time_modifier_segment_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a segment to the time modifier

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class grease_pencil_time_modifier_segment_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
        type: typing.Literal["UP", "DOWN"] | None = "UP",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move the active time segment up or down

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class grease_pencil_time_modifier_segment_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
        index: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the active segment from the time modifier

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :param index: Index, Index of the segment to remove (in [0, inf], optional)
        :return: Result of the operator call.
        """

class hide_collection(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        collection_index: int | None = -1,
        toggle: bool | None = False,
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Show only objects in collection (Shift to extend)

        :param execution_context:
        :param undo:
        :param collection_index: Collection Index, Index of the collection to change visibility (in [-1, inf], optional)
        :param toggle: Toggle, Toggle visibility (optional)
        :param extend: Extend, Extend visibility (optional)
        :return: Result of the operator call.
        """

class hide_render_clear_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reveal all render objects by setting the hide render flag

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class hide_view_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        select: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reveal temporarily hidden objects

        :param execution_context:
        :param undo:
        :param select: Select, Select revealed objects (optional)
        :return: Result of the operator call.
        """

class hide_view_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        unselected: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Temporarily hide objects from the viewport

        :param execution_context:
        :param undo:
        :param unselected: Unselected, Hide unselected rather than selected objects (optional)
        :return: Result of the operator call.
        """

class hook_add_newob(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Hook selected vertices to a newly created object

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class hook_add_selob(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_bone: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Hook selected vertices to the first selected object

        :param execution_context:
        :param undo:
        :param use_bone: Active Bone, Assign the hook to the hook objects active bone (optional)
        :return: Result of the operator call.
        """

class hook_assign(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Assign the selected vertices to a hook

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Modifier number to assign to (optional)
        :return: Result of the operator call.
        """

class hook_recenter(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set hook center to cursor position

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Modifier number to assign to (optional)
        :return: Result of the operator call.
        """

class hook_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove a hook from the active object

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Modifier number to remove (optional)
        :return: Result of the operator call.
        """

class hook_reset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Recalculate and clear offset transformation

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Modifier number to assign to (optional)
        :return: Result of the operator call.
        """

class hook_select(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select affected vertices on mesh

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Modifier number to remove (optional)
        :return: Result of the operator call.
        """

class instance_offset_from_cursor(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set offset used for collection instances based on cursor position

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class instance_offset_from_object(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set offset used for collection instances based on the active object position

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class instance_offset_to_cursor(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set cursor position to the offset used for collection instances

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class isolate_type_render(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Hide unselected render objects of same type as active by setting the hide render flag

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class join(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Join selected objects into active object

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class join_shapes(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_mirror: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add the vertex positions of selected objects as shape keys or update existing shape keys with matching names

        :param execution_context:
        :param undo:
        :param use_mirror: Mirror, Mirror the new shape key values (optional)
        :return: Result of the operator call.
        """

class join_uvs(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Transfer UV Maps from active to selected objects (needs matching geometry)

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class laplaciandeform_bind(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Bind mesh to system in laplacian deform modifier

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class lattice_add_to_selected(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        fit_to_selected: bool | None = True,
        radius: float | None = 1.0,
        margin: float | None = 0.0,
        add_modifiers: bool | None = True,
        resolution_u: int | None = 2,
        resolution_v: int | None = 2,
        resolution_w: int | None = 2,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a lattice and use it to deform selected objects

                :param execution_context:
                :param undo:
                :param fit_to_selected: Fit to Selected, Resize lattice to fit selected deformable objects (optional)
                :param radius: Radius, (in [0, inf], optional)
                :param margin: Margin, Add margin to lattice dimensions (in [0, inf], optional)
                :param add_modifiers: Add Modifiers, Automatically add lattice modifiers to selected objects (optional)
                :param resolution_u: Resolution U, Lattice resolution in U direction (in [1, 64], optional)
                :param resolution_v: V, Lattice resolution in V direction (in [1, 64], optional)
                :param resolution_w: W, Lattice resolution in W direction (in [1, 64], optional)
                :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class light_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[bpy.stub_internal.rna_enums.LightTypeItems]
        | None = "POINT",
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a light object to the scene

                :param execution_context:
                :param undo:
                :param type: Type, (optional)
                :param radius: Radius, (in [0, inf], optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class light_linking_blocker_collection_new(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create new light linking collection used by the active emitter

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class light_linking_blockers_link(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        link_state: typing.Literal["INCLUDE", "EXCLUDE"] | None = "INCLUDE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Light link selected blockers to the active emitter object

                :param execution_context:
                :param undo:
                :param link_state: Link State, State of the shadow linking (optional)

        INCLUDE
        Include -- Include selected blockers to cast shadows from the active emitter.

        EXCLUDE
        Exclude -- Exclude selected blockers from casting shadows from the active emitter.
                :return: Result of the operator call.
        """

class light_linking_blockers_select(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all objects which block light from this emitter

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class light_linking_receiver_collection_new(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create new light linking collection used by the active emitter

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class light_linking_receivers_link(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        link_state: typing.Literal["INCLUDE", "EXCLUDE"] | None = "INCLUDE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Light link selected receivers to the active emitter object

                :param execution_context:
                :param undo:
                :param link_state: Link State, State of the light linking (optional)

        INCLUDE
        Include -- Include selected receivers to receive light from the active emitter.

        EXCLUDE
        Exclude -- Exclude selected receivers from receiving light from the active emitter.
                :return: Result of the operator call.
        """

class light_linking_receivers_select(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all objects which receive light from this emitter

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class light_linking_unlink_from_collection(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove this object or collection from the light linking collection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class lightprobe_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a light probe object

                :param execution_context:
                :param undo:
                :param type: Type, (optional)

        SPHERE
        Sphere -- Light probe that captures precise lighting from all directions at a single point in space.

        PLANE
        Plane -- Light probe that captures incoming light from a single direction on a plane.

        VOLUME
        Volume -- Light probe that captures low frequency lighting inside a volume.
                :param radius: Radius, (in [0, inf], optional)
                :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class lightprobe_cache_bake(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        subset: typing.Literal["ALL", "SELECTED", "ACTIVE"] | None = "ALL",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Bake irradiance volume light cache

                :param execution_context:
                :param undo:
                :param subset: Subset, Subset of probes to update (optional)

        ALL
        All Volumes -- Bake all light probe volumes.

        SELECTED
        Selected Only -- Only bake selected light probe volumes.

        ACTIVE
        Active Only -- Only bake the active light probe volume.
                :return: Result of the operator call.
        """

class lightprobe_cache_free(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        subset: typing.Literal["ALL", "SELECTED", "ACTIVE"] | None = "SELECTED",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete cached indirect lighting

                :param execution_context:
                :param undo:
                :param subset: Subset, Subset of probes to update (optional)

        ALL
        All Light Probes -- Delete all light probes baked lighting data.

        SELECTED
        Selected Only -- Only delete selected light probes baked lighting data.

        ACTIVE
        Active Only -- Only delete the active light probes baked lighting data.
                :return: Result of the operator call.
        """

class lineart_bake_strokes(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        bake_all: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Bake Line Art for current Grease Pencil object

        :param execution_context:
        :param undo:
        :param bake_all: Bake All, Bake all Line Art modifiers (optional)
        :return: Result of the operator call.
        """

class lineart_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        clear_all: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear all strokes in current Grease Pencil object

        :param execution_context:
        :param undo:
        :param clear_all: Clear All, Clear all Line Art modifier bakes (optional)
        :return: Result of the operator call.
        """

class link_to_collection(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        collection_uid: int | None = -1,
        is_new: bool | None = False,
        new_collection_name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Link objects to a collection

        :param execution_context:
        :param undo:
        :param collection_uid: Collection UID, Session UID of the collection to link to (in [-1, inf], optional)
        :param is_new: New, Link objects to a new collection (optional)
        :param new_collection_name: Name, Name of the newly added collection (optional, never None)
        :return: Result of the operator call.
        """

class location_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        clear_delta: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear the objects location

        :param execution_context:
        :param undo:
        :param clear_delta: Clear Delta, Clear delta location in addition to clearing the normal location transform (optional)
        :return: Result of the operator call.
        """

class make_dupli_face(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Convert objects into instanced faces

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class make_links_data(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Transfer data from active object to selected objects

                :param execution_context:
                :param undo:
                :param type: Type, (optional)

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
                :return: Result of the operator call.
        """

class make_links_scene(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        scene: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Link selection to another scene

        :param execution_context:
        :param undo:
        :param scene: Scene, (optional)
        :return: Result of the operator call.
        """

class make_local(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            "SELECT_OBJECT", "SELECT_OBDATA", "SELECT_OBDATA_MATERIAL", "ALL"
        ]
        | None = "SELECT_OBJECT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make library linked data-blocks local to this file

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class make_override_library(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        collection: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a local override of the selected linked objects, and their hierarchy of dependencies

        :param execution_context:
        :param undo:
        :param collection: Override Collection, Session UID of the directly linked collection containing the selected object, to make an override from (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class make_single_user(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make linked data local to each object

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :param object: Object, Make single user objects (optional)
        :param obdata: Object Data, Make single user object data (optional)
        :param material: Materials, Make materials local to each data-block (optional)
        :param animation: Object Animation, Make object animation data local to each object (optional)
        :param obdata_animation: Object Data Animation, Make object data (mesh, curve etc.) animation data local to each object (optional)
        :return: Result of the operator call.
        """

class material_slot_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a new material slot

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class material_slot_assign(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Assign active material slot to selection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class material_slot_copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy material to selected objects

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class material_slot_deselect(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Deselect by active material slot

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class material_slot_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal["UP", "DOWN"] | None = "UP",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move the active material up/down in the list

        :param execution_context:
        :param undo:
        :param direction: Direction, Direction to move the active material towards (optional)
        :return: Result of the operator call.
        """

class material_slot_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the selected material slot

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class material_slot_remove_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove all materials

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class material_slot_remove_unused(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove unused material slots

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class material_slot_select(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select by active material slot

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class meshdeform_bind(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Bind mesh to cage in mesh deform modifier

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class metaball_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[bpy.stub_internal.rna_enums.MetaelemTypeItems]
        | None = "BALL",
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a metaball object to the scene

                :param execution_context:
                :param undo:
                :param type: Primitive, (optional)
                :param radius: Radius, (in [0, inf], optional)
                :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class mode_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal[bpy.stub_internal.rna_enums.ObjectModeItems]
        | None = "OBJECT",
        toggle: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Sets the object interaction mode

        :param execution_context:
        :param undo:
        :param mode: Mode, (optional)
        :param toggle: Toggle, (optional)
        :return: Result of the operator call.
        """

class mode_set_with_submode(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal[bpy.stub_internal.rna_enums.ObjectModeItems]
        | None = "OBJECT",
        toggle: bool | None = False,
        mesh_select_mode: set[
            typing.Literal[bpy.stub_internal.rna_enums.MeshSelectModeItems]
        ]
        | None = set(),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Sets the object interaction mode

        :param execution_context:
        :param undo:
        :param mode: Mode, (optional)
        :param toggle: Toggle, (optional)
        :param mesh_select_mode: Mesh Mode, (optional)
        :return: Result of the operator call.
        """

class modifier_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[bpy.stub_internal.rna_enums.ObjectModifierTypeItems]
        | None = "SUBSURF",
        use_selected_objects: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a procedural operation/effect to the active object

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object (optional)
        :return: Result of the operator call.
        """

class modifier_add_node_group(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        asset_library_type: typing.Literal[
            bpy.stub_internal.rna_enums.AssetLibraryTypeItems
        ]
        | None = "LOCAL",
        asset_library_identifier: str = "",
        relative_asset_identifier: str = "",
        session_uid: int | None = 0,
        use_selected_objects: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a procedural operation/effect to the active object

        :param execution_context:
        :param undo:
        :param asset_library_type: Asset Library Type, (optional)
        :param asset_library_identifier: Asset Library Identifier, (optional, never None)
        :param relative_asset_identifier: Relative Asset Identifier, (optional, never None)
        :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
        :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object (optional)
        :return: Result of the operator call.
        """

class modifier_apply(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Apply modifier and remove from the stack

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :param report: Report, Create a notification after the operation (optional)
        :param merge_customdata: Merge UVs, For mesh objects, merge UV coordinates that share a vertex to account for imprecision in some modifiers (optional)
        :param single_user: Make Data Single User, Make the objects data single user if needed (optional)
        :param all_keyframes: Apply to all keyframes, For Grease Pencil objects, apply the modifier to all the keyframes (optional)
        :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object (optional)
        :return: Result of the operator call.
        """

class modifier_apply_as_shapekey(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        keep_modifier: bool | None = False,
        modifier: str = "",
        report: bool | None = False,
        use_selected_objects: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Apply modifier as a new shape key and remove from the stack

        :param execution_context:
        :param undo:
        :param keep_modifier: Keep Modifier, Do not remove the modifier from stack (optional)
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :param report: Report, Create a notification after the operation (optional)
        :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object (optional)
        :return: Result of the operator call.
        """

class modifier_convert(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Convert particles to a mesh object

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class modifier_copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
        use_selected_objects: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate modifier at the same position in the stack

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object (optional)
        :return: Result of the operator call.
        """

class modifier_copy_to_selected(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy the modifier from the active object to all selected objects

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class modifier_move_down(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move modifier down in the stack

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class modifier_move_to_index(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
        index: int | None = 0,
        use_selected_objects: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change the modifiers index in the stack so it evaluates after the set number of others

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :param index: Index, The index to move the modifier to (in [0, inf], optional)
        :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object (optional)
        :return: Result of the operator call.
        """

class modifier_move_up(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move modifier up in the stack

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class modifier_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
        report: bool | None = False,
        use_selected_objects: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove a modifier from the active object

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :param report: Report, Create a notification after the operation (optional)
        :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object (optional)
        :return: Result of the operator call.
        """

class modifier_set_active(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Activate the modifier to use as the context

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class modifiers_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear all modifiers from the selected objects

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class modifiers_copy_to_selected(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy modifiers to other selected objects

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class move_to_collection(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        collection_uid: int | None = -1,
        is_new: bool | None = False,
        new_collection_name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move objects to a collection

        :param execution_context:
        :param undo:
        :param collection_uid: Collection UID, Session UID of the collection to move to (in [-1, inf], optional)
        :param is_new: New, Move objects to a new collection (optional)
        :param new_collection_name: Name, Name of the newly added collection (optional, never None)
        :return: Result of the operator call.
        """

class multires_base_apply(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
        apply_heuristic: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Modify the base mesh to conform to the displaced mesh

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :param apply_heuristic: Apply Subdivision Heuristic, Whether or not the final base mesh positions will be slightly altered to account for a new subdivision modifier being added (optional)
        :return: Result of the operator call.
        """

class multires_external_pack(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Pack displacements from an external file

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class multires_external_save(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Save displacements to an external file

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
                :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
                :param filter_blender: Filter .blend files, (optional)
                :param filter_backup: Filter backup .blend files, (optional)
                :param filter_image: Filter image files, (optional)
                :param filter_movie: Filter movie files, (optional)
                :param filter_python: Filter Python files, (optional)
                :param filter_font: Filter font files, (optional)
                :param filter_sound: Filter sound files, (optional)
                :param filter_text: Filter text files, (optional)
                :param filter_archive: Filter archive files, (optional)
                :param filter_btx: Filter btx files, (optional)
                :param filter_alembic: Filter Alembic files, (optional)
                :param filter_usd: Filter USD files, (optional)
                :param filter_obj: Filter OBJ files, (optional)
                :param filter_volume: Filter OpenVDB volume files, (optional)
                :param filter_folder: Filter folders, (optional)
                :param filter_blenlib: Filter Blender IDs, (optional)
                :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
                :param relative_path: Relative Path, Select the file relative to the blend file (optional)
                :param display_type: Display Type, (optional)

        DEFAULT
        Default -- Automatically determine display type for files.

        LIST_VERTICAL
        Short List -- Display files as short list.

        LIST_HORIZONTAL
        Long List -- Display files as a detailed list.

        THUMBNAIL
        Thumbnails -- Display files as thumbnails.
                :param sort_method: File sorting mode, (optional)
                :param modifier: Modifier, Name of the modifier to edit (optional, never None)
                :return: Result of the operator call.
        """

class multires_higher_levels_delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Deletes the higher resolution mesh, potential loss of detail

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class multires_rebuild_subdiv(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Rebuilds all possible subdivisions levels to generate a lower resolution base mesh

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class multires_reshape(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy vertex coordinates from other object

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class multires_subdivide(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
        mode: typing.Literal["CATMULL_CLARK", "SIMPLE", "LINEAR"]
        | None = "CATMULL_CLARK",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a new level of subdivision

                :param execution_context:
                :param undo:
                :param modifier: Modifier, Name of the modifier to edit (optional, never None)
                :param mode: Subdivision Mode, How the mesh is going to be subdivided to create a new level (optional)

        CATMULL_CLARK
        Catmull-Clark -- Create a new level using Catmull-Clark subdivisions.

        SIMPLE
        Simple -- Create a new level using simple subdivisions.

        LINEAR
        Linear -- Create a new level using linear interpolation of the sculpted displacement.
                :return: Result of the operator call.
        """

class multires_unsubdivide(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Rebuild a lower subdivision level of the current base mesh

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class ocean_bake(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
        free: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Bake an image sequence of ocean data

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :param free: Free, Free the bake, rather than generating it (optional)
        :return: Result of the operator call.
        """

class origin_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear the objects origin

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class origin_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the objects origin, by either moving the data, or set to center of data, or use 3D cursor

                :param execution_context:
                :param undo:
                :param type: Type, (optional)

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
                :param center: Center, (optional)
                :return: Result of the operator call.
        """

class parent_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["CLEAR", "CLEAR_KEEP_TRANSFORM", "CLEAR_INVERSE"]
        | None = "CLEAR",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear the objects parenting

                :param execution_context:
                :param undo:
                :param type: Type, (optional)

        CLEAR
        Clear Parent -- Completely clear the parenting relationship, including involved modifiers if any.

        CLEAR_KEEP_TRANSFORM
        Clear and Keep Transformation -- As Clear Parent, but keep the current visual transformations of the object.

        CLEAR_INVERSE
        Clear Parent Inverse -- Reset the transform corrections applied to the parenting relationship, does not remove parenting itself.
                :return: Result of the operator call.
        """

class parent_inverse_apply(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Apply the objects parent inverse to its data

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class parent_no_inverse_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        keep_transform: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the objects parenting without setting the inverse parent correction

        :param execution_context:
        :param undo:
        :param keep_transform: Keep Transform, Preserve the world transform throughout parenting (optional)
        :return: Result of the operator call.
        """

class parent_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the objects parenting

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :param xmirror: X Mirror, Apply weights symmetrically along X axis, for Envelope/Automatic vertex groups creation (optional)
        :param keep_transform: Keep Transform, Apply transformation before parenting (optional)
        :return: Result of the operator call.
        """

class particle_system_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a particle system

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class particle_system_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the selected particle system

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class paste_transform(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        method: typing.Literal["CURRENT", "EXISTING_KEYS", "BAKE"] | None = "CURRENT",
        bake_step: int | None = 0,
        use_mirror: bool | None = False,
        mirror_axis_loc: typing.Literal["x", "y", "z"] | None = "x",
        mirror_axis_rot: typing.Literal["x", "y", "z"] | None = "z",
        use_relative: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Pastes the matrix from the clipboard to the currently active pose bone or object. Uses world-space matrices

                :param execution_context:
                :param undo:
                :param method: Paste Method, Update the current transform, selected keyframes, or even create new keys (optional)

        CURRENT
        Current Transform -- Paste onto the current values only, only manipulating the animation data if auto-keying is enabled.

        EXISTING_KEYS
        Selected Keys -- Paste onto frames that have a selected key, potentially creating new keys on those frames.

        BAKE
        Bake on Key Range -- Paste onto all frames between the first and last selected key, creating new keyframes if necessary.
                :param bake_step: Frame Step, Only used for baking. Step=1 creates a key on every frame, step=2 bakes on 2s, etc (in [1, inf], optional)
                :param use_mirror: Mirror Transform, When pasting, mirror the transform relative to a specific object or bone (optional)
                :param mirror_axis_loc: Location Axis, Coordinate axis used to mirror the location part of the transform (optional)
                :param mirror_axis_rot: Rotation Axis, Coordinate axis used to mirror the rotation part of the transform (optional)
                :param use_relative: Use Relative Paste, When pasting, assume the pasted matrix is relative to another object (set in the user interface) (optional)
                :return: Result of the operator call.
        """

class paths_calculate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        display_type: typing.Literal[
            bpy.stub_internal.rna_enums.MotionpathDisplayTypeItems
        ]
        | None = "RANGE",
        range: typing.Literal[bpy.stub_internal.rna_enums.MotionpathRangeItems]
        | None = "SCENE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Generate motion paths for the selected objects

        :param execution_context:
        :param undo:
        :param display_type: Display Type, (optional)
        :param range: Computation Range, (optional)
        :return: Result of the operator call.
        """

class paths_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        only_selected: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param only_selected: Only Selected, Only clear motion paths of selected objects (optional)
        :return: Result of the operator call.
        """

class paths_update(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Recalculate motion paths for selected objects

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class paths_update_visible(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Recalculate all visible motion paths for objects and poses

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class pointcloud_random_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a point cloud object to the scene

                :param execution_context:
                :param undo:
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class posemode_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Enable or disable posing/selecting bones

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class quadriflow_remesh(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a new quad based mesh using the surface data of the current mesh. All data layers will be lost

                :param execution_context:
                :param undo:
                :param use_mesh_symmetry: Use Mesh Symmetry, Generates a symmetrical mesh using the mesh symmetry configuration (optional)
                :param use_preserve_sharp: Preserve Sharp, Try to preserve sharp features on the mesh (optional)
                :param use_preserve_boundary: Preserve Mesh Boundary, Try to preserve mesh boundary on the mesh (optional)
                :param preserve_attributes: Preserve Attributes, Reproject attributes onto the new mesh (optional)
                :param smooth_normals: Smooth Normals, Set the output mesh normals to smooth (optional)
                :param mode: Mode, How to specify the amount of detail for the new mesh (optional)

        RATIO
        Ratio -- Specify target number of faces relative to the current mesh.

        EDGE
        Edge Length -- Input target edge length in the new mesh.

        FACES
        Faces -- Input target number of faces in the new mesh.
                :param target_ratio: Ratio, Relative number of faces compared to the current mesh (in [0, inf], optional)
                :param target_edge_length: Edge Length, Target edge length in the new mesh (in [1e-07, inf], optional)
                :param target_faces: Number of Faces, Approximate number of faces (quads) in the new mesh (in [1, inf], optional)
                :param mesh_area: Old Object Face Area, This property is only used to cache the object area for later calculations (in [-inf, inf], optional)
                :param seed: Seed, Random seed to use with the solver. Different seeds will cause the remesher to come up with different quad layouts on the mesh (in [0, inf], optional)
                :return: Result of the operator call.
        """

class quick_explode(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make selected objects explode

        :param execution_context:
        :param undo:
        :param style: Explode Style, (optional)
        :param amount: Number of Pieces, (in [2, 10000], optional)
        :param frame_duration: Duration, (in [1, 300000], optional)
        :param frame_start: Start Frame, (in [1, 300000], optional)
        :param frame_end: End Frame, (in [1, 300000], optional)
        :param velocity: Outwards Velocity, (in [0, 300000], optional)
        :param fade: Fade, Fade the pieces over time (optional)
        :return: Result of the operator call.
        """

class quick_fur(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a fur setup to the selected objects

        :param execution_context:
        :param undo:
        :param density: Density, (optional)
        :param length: Length, (in [0.001, 100], optional)
        :param radius: Hair Radius, (in [0, 10], optional)
        :param view_percentage: View Percentage, (in [0, 1], optional)
        :param apply_hair_guides: Apply Hair Guides, (optional)
        :param use_noise: Noise, (optional)
        :param use_frizz: Frizz, (optional)
        :return: Result of the operator call.
        """

class quick_liquid(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        show_flows: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make selected objects liquid

        :param execution_context:
        :param undo:
        :param show_flows: Render Liquid Objects, Keep the liquid objects visible during rendering (optional)
        :return: Result of the operator call.
        """

class quick_smoke(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        style: typing.Literal["SMOKE", "FIRE", "BOTH"] | None = "SMOKE",
        show_flows: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Use selected objects as smoke emitters

        :param execution_context:
        :param undo:
        :param style: Smoke Style, (optional)
        :param show_flows: Render Smoke Objects, Keep the smoke objects visible during rendering (optional)
        :return: Result of the operator call.
        """

class randomize_transform(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        random_seed: int | None = 0,
        use_delta: bool | None = False,
        use_loc: bool | None = True,
        loc: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
        use_rot: bool | None = True,
        rot: collections.abc.Sequence[float] | mathutils.Euler | None = (0.0, 0.0, 0.0),
        use_scale: bool | None = True,
        scale_even: bool | None = False,
        scale: collections.abc.Sequence[float] | None = (1.0, 1.0, 1.0),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Randomize objects location, rotation, and scale

        :param execution_context:
        :param undo:
        :param random_seed: Random Seed, Seed value for the random generator (in [0, 10000], optional)
        :param use_delta: Transform Delta, Randomize delta transform values instead of regular transform (optional)
        :param use_loc: Randomize Location, Randomize the location values (optional)
        :param loc: Location, Maximum distance the objects can spread over each axis (array of 3 items, in [-100, 100], optional)
        :param use_rot: Randomize Rotation, Randomize the rotation values (optional)
        :param rot: Rotation, Maximum rotation over each axis (array of 3 items, in [-3.14159, 3.14159], optional)
        :param use_scale: Randomize Scale, Randomize the scale values (optional)
        :param scale_even: Scale Even, Use the same scale value for all axis (optional)
        :param scale: Scale, Maximum scale randomization over each axis (array of 3 items, in [-100, 100], optional)
        :return: Result of the operator call.
        """

class reset_override_library(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset the selected local overrides to their linked references values

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class rotation_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        clear_delta: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear the objects rotation

        :param execution_context:
        :param undo:
        :param clear_delta: Clear Delta, Clear delta rotation in addition to clearing the normal rotation transform (optional)
        :return: Result of the operator call.
        """

class scale_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        clear_delta: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear the objects scale

        :param execution_context:
        :param undo:
        :param clear_delta: Clear Delta, Clear delta scale in addition to clearing the normal scale transform (optional)
        :return: Result of the operator call.
        """

class select_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"]
        | None = "TOGGLE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change selection of all visible objects in scene

                :param execution_context:
                :param undo:
                :param action: Action, Selection action to execute (optional)

        TOGGLE
        Toggle -- Toggle selection for all elements.

        SELECT
        Select -- Select all elements.

        DESELECT
        Deselect -- Deselect all elements.

        INVERT
        Invert -- Invert selection of all elements.
                :return: Result of the operator call.
        """

class select_by_type(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        extend: bool | None = False,
        type: typing.Literal[bpy.stub_internal.rna_enums.ObjectTypeItems]
        | None = "MESH",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all visible objects that are of a type

        :param execution_context:
        :param undo:
        :param extend: Extend, Extend selection instead of deselecting everything first (optional)
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class select_camera(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select the active camera

        :param execution_context:
        :param undo:
        :param extend: Extend, Extend the selection (optional)
        :return: Result of the operator call.
        """

class select_grouped(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all visible objects grouped by various properties

                :param execution_context:
                :param undo:
                :param extend: Extend, Extend selection instead of deselecting everything first (optional)
                :param type: Type, (optional)

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
                :return: Result of the operator call.
        """

class select_hierarchy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal["PARENT", "CHILD"] | None = "PARENT",
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select object relative to the active objects position in the hierarchy

        :param execution_context:
        :param undo:
        :param direction: Direction, Direction to select in the hierarchy (optional)
        :param extend: Extend, Extend the existing selection (optional)
        :return: Result of the operator call.
        """

class select_less(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Deselect objects at the boundaries of parent/child relationships

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_linked(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        extend: bool | None = False,
        type: typing.Literal[
            "OBDATA", "MATERIAL", "DUPGROUP", "PARTICLE", "LIBRARY", "LIBRARY_OBDATA"
        ]
        | None = "OBDATA",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all visible objects that are linked

        :param execution_context:
        :param undo:
        :param extend: Extend, Extend selection instead of deselecting everything first (optional)
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class select_mirror(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select the mirror objects of the selected object e.g. "L.sword" and "R.sword"

        :param execution_context:
        :param undo:
        :param extend: Extend, Extend selection instead of deselecting everything first (optional)
        :return: Result of the operator call.
        """

class select_more(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select connected parent/child objects

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_pattern(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        pattern: str = "*",
        case_sensitive: bool | None = False,
        extend: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select objects matching a naming pattern

        :param execution_context:
        :param undo:
        :param pattern: Pattern, Name filter using *, ? and [abc] unix style wildcards (optional, never None)
        :param case_sensitive: Case Sensitive, Do a case sensitive compare (optional)
        :param extend: Extend, Extend the existing selection (optional)
        :return: Result of the operator call.
        """

class select_random(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        ratio: float | None = 0.5,
        seed: int | None = 0,
        action: typing.Literal["SELECT", "DESELECT"] | None = "SELECT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select or deselect random visible objects

                :param execution_context:
                :param undo:
                :param ratio: Ratio, Portion of items to select randomly (in [0, 1], optional)
                :param seed: Random Seed, Seed for the random number generator (in [0, inf], optional)
                :param action: Action, Selection action to execute (optional)

        SELECT
        Select -- Select all elements.

        DESELECT
        Deselect -- Deselect all elements.
                :return: Result of the operator call.
        """

class select_same_collection(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        collection: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select object in the same collection

        :param execution_context:
        :param undo:
        :param collection: Collection, Name of the collection to select (optional, never None)
        :return: Result of the operator call.
        """

class shade_auto_smooth(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_auto_smooth: bool | None = True,
        angle: float | None = 0.523599,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add modifier to automatically set the sharpness of mesh edges based on the angle between the neighboring faces

        :param execution_context:
        :param undo:
        :param use_auto_smooth: Auto Smooth, Add modifier to set edge sharpness automatically (optional)
        :param angle: Angle, Maximum angle between face normals that will be considered as smooth (in [0, 3.14159], optional)
        :return: Result of the operator call.
        """

class shade_flat(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        keep_sharp_edges: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Render and display faces uniform, using face normals

        :param execution_context:
        :param undo:
        :param keep_sharp_edges: Keep Sharp Edges, Dont remove sharp edges, which are redundant with faces shaded smooth (optional)
        :return: Result of the operator call.
        """

class shade_smooth(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        keep_sharp_edges: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Render and display faces smooth, using interpolated vertex normals

        :param execution_context:
        :param undo:
        :param keep_sharp_edges: Keep Sharp Edges, Dont remove sharp edges. Tagged edges will remain sharp (optional)
        :return: Result of the operator call.
        """

class shade_smooth_by_angle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        angle: float | None = 0.523599,
        keep_sharp_edges: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the sharpness of mesh edges based on the angle between the neighboring faces

        :param execution_context:
        :param undo:
        :param angle: Angle, Maximum angle between face normals that will be considered as smooth (in [0, 3.14159], optional)
        :param keep_sharp_edges: Keep Sharp Edges, Only add sharp edges instead of clearing existing tags first (optional)
        :return: Result of the operator call.
        """

class shaderfx_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[bpy.stub_internal.rna_enums.ObjectShaderfxTypeItems]
        | None = "FX_BLUR",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a visual effect to the active object

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class shaderfx_copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        shaderfx: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate effect at the same position in the stack

        :param execution_context:
        :param undo:
        :param shaderfx: Shader, Name of the shaderfx to edit (optional, never None)
        :return: Result of the operator call.
        """

class shaderfx_move_down(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        shaderfx: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move effect down in the stack

        :param execution_context:
        :param undo:
        :param shaderfx: Shader, Name of the shaderfx to edit (optional, never None)
        :return: Result of the operator call.
        """

class shaderfx_move_to_index(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        shaderfx: str = "",
        index: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change the effects position in the list so it evaluates after the set number of others

        :param execution_context:
        :param undo:
        :param shaderfx: Shader, Name of the shaderfx to edit (optional, never None)
        :param index: Index, The index to move the effect to (in [0, inf], optional)
        :return: Result of the operator call.
        """

class shaderfx_move_up(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        shaderfx: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move effect up in the stack

        :param execution_context:
        :param undo:
        :param shaderfx: Shader, Name of the shaderfx to edit (optional, never None)
        :return: Result of the operator call.
        """

class shaderfx_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        shaderfx: str = "",
        report: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove a effect from the active Grease Pencil object

        :param execution_context:
        :param undo:
        :param shaderfx: Shader, Name of the shaderfx to edit (optional, never None)
        :param report: Report, Create a notification after the operation (optional)
        :return: Result of the operator call.
        """

class shape_key_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        from_mix: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add shape key to the object

        :param execution_context:
        :param undo:
        :param from_mix: From Mix, Create the new shape key from the existing mix of keys (optional)
        :return: Result of the operator call.
        """

class shape_key_apply_to_basis(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Apply deformations of selected shape keys to the basis key, removing them

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class shape_key_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset the weights of all shape keys to 0 or to the closest value respecting the limits

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class shape_key_copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate the active shape key

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class shape_key_lock(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        action: typing.Literal["LOCK", "UNLOCK"] | None = "LOCK",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change the lock state of all shape keys of active object

                :param execution_context:
                :param undo:
                :param action: Action, Lock action to execute on vertex groups (optional)

        LOCK
        Lock -- Lock all shape keys.

        UNLOCK
        Unlock -- Unlock all shape keys.
                :return: Result of the operator call.
        """

class shape_key_make_basis(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make this shape key the new basis key, effectively applying it to the mesh. Note that this applies the shape key at its 100% value

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class shape_key_mirror(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_topology: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Mirror the current shape key along the local X axis

        :param execution_context:
        :param undo:
        :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology) (optional)
        :return: Result of the operator call.
        """

class shape_key_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["TOP", "UP", "DOWN", "BOTTOM"] | None = "TOP",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move selected shape keys up/down in the list

                :param execution_context:
                :param undo:
                :param type: Type, (optional)

        TOP
        Top -- Top of the list.

        UP
        Up.

        DOWN
        Down.

        BOTTOM
        Bottom -- Bottom of the list.
                :return: Result of the operator call.
        """

class shape_key_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        all: bool | None = False,
        apply_mix: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove shape key from the object

        :param execution_context:
        :param undo:
        :param all: All, Remove all shape keys (optional)
        :param apply_mix: Apply Mix, Apply current mix of shape keys to the geometry before removing them (optional)
        :return: Result of the operator call.
        """

class shape_key_retime(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Resets the timing for absolute shape keys

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class shape_key_transfer(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["OFFSET", "RELATIVE_FACE", "RELATIVE_EDGE"]
        | None = "OFFSET",
        use_clamp: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy the active shape key of another selected object to this one

                :param execution_context:
                :param undo:
                :param mode: Transformation Mode, Relative shape positions to the new shape method (optional)

        OFFSET
        Offset -- Apply the relative positional offset.

        RELATIVE_FACE
        Relative Face -- Calculate relative position (using faces).

        RELATIVE_EDGE
        Relative Edge -- Calculate relative position (using edges).
                :param use_clamp: Clamp Offset, Clamp the transformation to the distance each vertex moves in the original shape (optional)
                :return: Result of the operator call.
        """

class simulation_nodes_cache_bake(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        selected: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Bake simulations in geometry nodes modifiers

        :param execution_context:
        :param undo:
        :param selected: Selected, Bake cache on all selected objects (optional)
        :return: Result of the operator call.
        """

class simulation_nodes_cache_calculate_to_frame(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        selected: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Calculate simulations in geometry nodes modifiers from the start to current frame

        :param execution_context:
        :param undo:
        :param selected: Selected, Calculate all selected objects instead of just the active object (optional)
        :return: Result of the operator call.
        """

class simulation_nodes_cache_delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        selected: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete cached/baked simulations in geometry nodes modifiers

        :param execution_context:
        :param undo:
        :param selected: Selected, Delete cache on all selected objects (optional)
        :return: Result of the operator call.
        """

class skin_armature_create(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create an armature that parallels the skin layout

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class skin_loose_mark_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        action: typing.Literal["MARK", "CLEAR"] | None = "MARK",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Mark/clear selected vertices as loose

                :param execution_context:
                :param undo:
                :param action: Action, (optional)

        MARK
        Mark -- Mark selected vertices as loose.

        CLEAR
        Clear -- Set selected vertices as not loose.
                :return: Result of the operator call.
        """

class skin_radii_equalize(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make skin radii of selected vertices equal on each axis

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class skin_root_mark(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Mark selected vertices as roots

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class speaker_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a speaker object to the scene

                :param execution_context:
                :param undo:
                :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class subdivision_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        level: int | None = 1,
        relative: bool | None = False,
        ensure_modifier: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Sets a Subdivision Surface level (1 to 5)

        :param execution_context:
        :param undo:
        :param level: Level, (in [-100, 100], optional)
        :param relative: Relative, Apply the subdivision surface level as an offset relative to the current level (optional)
        :param ensure_modifier: Ensure Modifier, Create the corresponding modifier if it does not exist (optional)
        :return: Result of the operator call.
        """

class surfacedeform_bind(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        modifier: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Bind mesh to target in surface deform modifier

        :param execution_context:
        :param undo:
        :param modifier: Modifier, Name of the modifier to edit (optional, never None)
        :return: Result of the operator call.
        """

class text_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a text object to the scene

                :param execution_context:
                :param undo:
                :param radius: Radius, (in [0, inf], optional)
                :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class track_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["CLEAR", "CLEAR_KEEP_TRANSFORM"] | None = "CLEAR",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear tracking constraint or flag from object

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class track_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["DAMPTRACK", "TRACKTO", "LOCKTRACK"] | None = "DAMPTRACK",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make the object track another object, using various methods/constraints

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class transfer_mode(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_flash_on_transfer: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Switches the active object and assigns the same mode to a new one under the mouse cursor, leaving the active mode in the current one

        :param execution_context:
        :param undo:
        :param use_flash_on_transfer: Flash On Transfer, Flash the target object when transferring the mode (optional)
        :return: Result of the operator call.
        """

class transform_apply(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        location: bool | None = True,
        rotation: bool | None = True,
        scale: bool | None = True,
        properties: bool | None = True,
        corrective_flip_normals: bool | None = True,
        isolate_users: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Apply the objects transformation to its data

        :param execution_context:
        :param undo:
        :param location: Location, (optional)
        :param rotation: Rotation, (optional)
        :param scale: Scale, (optional)
        :param properties: Apply Properties, Modify properties such as curve vertex radius, font size and bone envelope (optional)
        :param corrective_flip_normals: Corrective Flip Normals, Invert normals for negative scaled objects. (optional)
        :param isolate_users: Isolate Multi User Data, Create new object-data users if needed (optional)
        :return: Result of the operator call.
        """

class transform_axis_target(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Interactively point cameras and lights to a location (Ctrl translates)

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class transform_to_mouse(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Snap selected item(s) to the mouse location

        :param execution_context:
        :param undo:
        :param name: Name, Object name to place (uses the active object when this and session_uid are unset) (optional, never None)
        :param session_uid: Session UUID, Session UUID of the object to place (uses the active object when this and name are unset) (in [-inf, inf], optional)
        :param matrix: Matrix, (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)
        :param drop_x: Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
        :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class transforms_to_deltas(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["ALL", "LOC", "ROT", "SCALE"] | None = "ALL",
        reset_values: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Convert normal object transforms to delta transforms, any existing delta transforms will be included as well

                :param execution_context:
                :param undo:
                :param mode: Mode, Which transforms to transfer (optional)

        ALL
        All Transforms -- Transfer location, rotation, and scale transforms.

        LOC
        Location -- Transfer location transforms only.

        ROT
        Rotation -- Transfer rotation transforms only.

        SCALE
        Scale -- Transfer scale transforms only.
                :param reset_values: Reset Values, Clear transform values after transferring to deltas (optional)
                :return: Result of the operator call.
        """

class unlink_data(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class update_shapes(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_mirror: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Update existing shape keys with the vertex positions of selected objects with matching names

        :param execution_context:
        :param undo:
        :param use_mirror: Mirror, Mirror the new shape key values (optional)
        :return: Result of the operator call.
        """

class vertex_group_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a new vertex group to the active object

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vertex_group_assign(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Assign the selected vertices to the active vertex group

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vertex_group_assign_new(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Assign the selected vertices to a new vertex group

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vertex_group_clean(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        group_select_mode: str | None = "",
        limit: float | None = 0.0,
        keep_single: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove vertex group assignments which are not required

        :param execution_context:
        :param undo:
        :param group_select_mode: Subset, Define which subset of groups shall be used (optional)
        :param limit: Limit, Remove vertices which weight is below or equal to this limit (in [0, 1], optional)
        :param keep_single: Keep Single, Keep verts assigned to at least one group when cleaning (optional)
        :return: Result of the operator call.
        """

class vertex_group_copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make a copy of the active vertex group

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vertex_group_copy_to_selected(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Replace vertex groups of selected objects by vertex groups of active object

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vertex_group_deselect(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Deselect all selected vertices assigned to the active vertex group

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vertex_group_invert(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        group_select_mode: str | None = "",
        auto_assign: bool | None = True,
        auto_remove: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Invert active vertex groups weights

        :param execution_context:
        :param undo:
        :param group_select_mode: Subset, Define which subset of groups shall be used (optional)
        :param auto_assign: Add Weights, Add vertices from groups that have zero weight before inverting (optional)
        :param auto_remove: Remove Weights, Remove vertices from groups that have zero weight after inverting (optional)
        :return: Result of the operator call.
        """

class vertex_group_levels(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        group_select_mode: str | None = "",
        offset: float | None = 0.0,
        gain: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add some offset and multiply with some gain the weights of the active vertex group

        :param execution_context:
        :param undo:
        :param group_select_mode: Subset, Define which subset of groups shall be used (optional)
        :param offset: Offset, Value to add to weights (in [-1, 1], optional)
        :param gain: Gain, Value to multiply weights by (in [0, inf], optional)
        :return: Result of the operator call.
        """

class vertex_group_limit_total(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        group_select_mode: str | None = "",
        limit: int | None = 4,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Limit deform weights associated with a vertex to a specified number by removing lowest weights

        :param execution_context:
        :param undo:
        :param group_select_mode: Subset, Define which subset of groups shall be used (optional)
        :param limit: Limit, Maximum number of deform weights (in [1, 32], optional)
        :return: Result of the operator call.
        """

class vertex_group_lock(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        action: typing.Literal["TOGGLE", "LOCK", "UNLOCK", "INVERT"] | None = "TOGGLE",
        mask: typing.Literal["ALL", "SELECTED", "UNSELECTED", "INVERT_UNSELECTED"]
        | None = "ALL",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change the lock state of all or some vertex groups of active object

                :param execution_context:
                :param undo:
                :param action: Action, Lock action to execute on vertex groups (optional)

        TOGGLE
        Toggle -- Unlock all vertex groups if there is at least one locked group, lock all in other case.

        LOCK
        Lock -- Lock all vertex groups.

        UNLOCK
        Unlock -- Unlock all vertex groups.

        INVERT
        Invert -- Invert the lock state of all vertex groups.
                :param mask: Mask, Apply the action based on vertex group selection (optional)

        ALL
        All -- Apply action to all vertex groups.

        SELECTED
        Selected -- Apply to selected vertex groups.

        UNSELECTED
        Unselected -- Apply to unselected vertex groups.

        INVERT_UNSELECTED
        Invert Unselected -- Apply the opposite of Lock/Unlock to unselected vertex groups.
                :return: Result of the operator call.
        """

class vertex_group_mirror(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mirror_weights: bool | None = True,
        flip_group_names: bool | None = True,
        all_groups: bool | None = False,
        use_topology: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Mirror vertex group, flip weights and/or names, editing only selected vertices, flipping when both sides are selected otherwise copy from unselected

        :param execution_context:
        :param undo:
        :param mirror_weights: Mirror Weights, Mirror weights (optional)
        :param flip_group_names: Flip Group Names, Flip vertex group names (optional)
        :param all_groups: All Groups, Mirror all vertex groups weights (optional)
        :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology) (optional)
        :return: Result of the operator call.
        """

class vertex_group_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal["UP", "DOWN"] | None = "UP",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move the active vertex group up/down in the list

        :param execution_context:
        :param undo:
        :param direction: Direction, Direction to move the active vertex group towards (optional)
        :return: Result of the operator call.
        """

class vertex_group_normalize(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Normalize weights of the active vertex group, so that the highest ones are now 1.0

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vertex_group_normalize_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        group_select_mode: str | None = "",
        lock_active: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0

        :param execution_context:
        :param undo:
        :param group_select_mode: Subset, Define which subset of groups shall be used (optional)
        :param lock_active: Lock Active, Keep the values of the active group while normalizing others (optional)
        :return: Result of the operator call.
        """

class vertex_group_quantize(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        group_select_mode: str | None = "",
        steps: int | None = 4,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set weights to a fixed number of steps

        :param execution_context:
        :param undo:
        :param group_select_mode: Subset, Define which subset of groups shall be used (optional)
        :param steps: Steps, Number of steps between 0 and 1 (in [1, 1000], optional)
        :return: Result of the operator call.
        """

class vertex_group_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        all: bool | None = False,
        all_unlocked: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete the active or all vertex groups from the active object

        :param execution_context:
        :param undo:
        :param all: All, Remove all vertex groups (optional)
        :param all_unlocked: All Unlocked, Remove all unlocked vertex groups (optional)
        :return: Result of the operator call.
        """

class vertex_group_remove_from(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_all_groups: bool | None = False,
        use_all_verts: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the selected vertices from active or all vertex group(s)

        :param execution_context:
        :param undo:
        :param use_all_groups: All Groups, Remove from all groups (optional)
        :param use_all_verts: All Vertices, Clear the active group (optional)
        :return: Result of the operator call.
        """

class vertex_group_select(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all the vertices assigned to the active vertex group

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vertex_group_set_active(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        group: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the active vertex group

        :param execution_context:
        :param undo:
        :param group: Group, Vertex group to set as active (optional)
        :return: Result of the operator call.
        """

class vertex_group_smooth(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        group_select_mode: str | None = "",
        factor: float | None = 0.5,
        repeat: int | None = 1,
        expand: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Smooth weights for selected vertices

        :param execution_context:
        :param undo:
        :param group_select_mode: Subset, Define which subset of groups shall be used (optional)
        :param factor: Factor, (in [0, 1], optional)
        :param repeat: Iterations, (in [1, 10000], optional)
        :param expand: Expand/Contract, Expand/contract weights (in [-1, 1], optional)
        :return: Result of the operator call.
        """

class vertex_group_sort(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        sort_type: typing.Literal["NAME", "BONE_HIERARCHY"] | None = "NAME",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Sort vertex groups

        :param execution_context:
        :param undo:
        :param sort_type: Sort Type, Sort type (optional)
        :return: Result of the operator call.
        """

class vertex_parent_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Parent selected objects to the selected vertices

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vertex_weight_copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy weights from active to selected

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vertex_weight_delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        weight_group: int | None = -1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete this weight from the vertex (disabled if vertex group is locked)

        :param execution_context:
        :param undo:
        :param weight_group: Weight Index, Index of source weight in active vertex group (in [-1, inf], optional)
        :return: Result of the operator call.
        """

class vertex_weight_normalize_active_vertex(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Normalize active vertexs weights

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vertex_weight_paste(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        weight_group: int | None = -1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy this groups weight to other selected vertices (disabled if vertex group is locked)

        :param execution_context:
        :param undo:
        :param weight_group: Weight Index, Index of source weight in active vertex group (in [-1, inf], optional)
        :return: Result of the operator call.
        """

class vertex_weight_set_active(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        weight_group: int | None = -1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set as active vertex group

        :param execution_context:
        :param undo:
        :param weight_group: Weight Index, Index of source weight in active vertex group (in [-1, inf], optional)
        :return: Result of the operator call.
        """

class visual_geometry_to_objects(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Convert geometry and instances into editable objects and collections

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class visual_transform_apply(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Apply the objects visual transformation to its data

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class volume_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a volume object to the scene

                :param execution_context:
                :param undo:
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class volume_import(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
        scale: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Import OpenVDB volume file

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param directory: Directory, Directory of the file (optional, never None)
                :param files: Files, (optional)
                :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
                :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
                :param filter_blender: Filter .blend files, (optional)
                :param filter_backup: Filter backup .blend files, (optional)
                :param filter_image: Filter image files, (optional)
                :param filter_movie: Filter movie files, (optional)
                :param filter_python: Filter Python files, (optional)
                :param filter_font: Filter font files, (optional)
                :param filter_sound: Filter sound files, (optional)
                :param filter_text: Filter text files, (optional)
                :param filter_archive: Filter archive files, (optional)
                :param filter_btx: Filter btx files, (optional)
                :param filter_alembic: Filter Alembic files, (optional)
                :param filter_usd: Filter USD files, (optional)
                :param filter_obj: Filter OBJ files, (optional)
                :param filter_volume: Filter OpenVDB volume files, (optional)
                :param filter_folder: Filter folders, (optional)
                :param filter_blenlib: Filter Blender IDs, (optional)
                :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
                :param relative_path: Relative Path, Select the file relative to the blend file (optional)
                :param display_type: Display Type, (optional)

        DEFAULT
        Default -- Automatically determine display type for files.

        LIST_VERTICAL
        Short List -- Display files as short list.

        LIST_HORIZONTAL
        Long List -- Display files as a detailed list.

        THUMBNAIL
        Thumbnails -- Display files as thumbnails.
                :param sort_method: File sorting mode, (optional)
                :param use_sequence_detection: Detect Sequences, Automatically detect animated sequences in selected volume files (based on file names) (optional)
                :param align: Align, The alignment of the new object (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
                :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class voxel_remesh(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Calculates a new manifold mesh based on the volume of the current mesh. All data layers will be lost

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class voxel_size_edit(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Modify the mesh voxel size interactively used in the voxel remesher

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
