import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

class align(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        axis: typing.Literal[
            "ALIGN_S", "ALIGN_T", "ALIGN_U", "ALIGN_AUTO", "ALIGN_X", "ALIGN_Y"
        ]
        | None = "ALIGN_AUTO",
        position_mode: typing.Literal["MEAN", "MIN", "MAX"] | None = "MEAN",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Aligns selected UV vertices on a line

                :param execution_context:
                :param undo:
                :param axis: Axis, Axis to align UV locations on (optional)

        ALIGN_S
        Straighten -- Align UV vertices along the line defined by the endpoints.

        ALIGN_T
        Straighten X -- Align UV vertices, moving them horizontally to the line defined by the endpoints.

        ALIGN_U
        Straighten Y -- Align UV vertices, moving them vertically to the line defined by the endpoints.

        ALIGN_AUTO
        Align Auto -- Automatically choose the direction on which there is most alignment already.

        ALIGN_X
        Align Vertically -- Align UV vertices on a vertical line.

        ALIGN_Y
        Align Horizontally -- Align UV vertices on a horizontal line.
                :param position_mode: Position Mode, Method of calculating the alignment position (optional)

        MEAN
        Mean -- Align UVs along the mean position.

        MIN
        Minimum -- Align UVs along the minimum position.

        MAX
        Maximum -- Align UVs along the maximum position.
                :return: Result of the operator call.
        """

class align_rotation(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        method: typing.Literal["AUTO", "EDGE", "GEOMETRY"] | None = "AUTO",
        axis: typing.Literal["X", "Y", "Z"] | None = "X",
        correct_aspect: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Align the UV islands rotation

                :param execution_context:
                :param undo:
                :param method: Method, Method to calculate rotation angle (optional)

        AUTO
        Auto -- Align from all edges.

        EDGE
        Edge -- Only selected edges.

        GEOMETRY
        Geometry -- Align to Geometry axis.
                :param axis: Axis, Axis to align to (optional)

        X
        X -- X axis.

        Y
        Y -- Y axis.

        Z
        Z -- Z axis.
                :param correct_aspect: Correct Aspect, Take image aspect ratio into account (optional)
                :return: Result of the operator call.
        """

class arrange_islands(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        initial_position: typing.Literal[
            "BOUNDING_BOX", "UV_GRID", "ACTIVE_UDIM", "CURSOR"
        ]
        | None = "BOUNDING_BOX",
        axis: typing.Literal["X", "Y"] | None = "Y",
        align: typing.Literal["MIN", "MAX", "CENTER", "NONE"] | None = "MIN",
        order: typing.Literal["LARGE_TO_SMALL", "SMALL_TO_LARGE", "Fixed"]
        | None = "LARGE_TO_SMALL",
        margin: float | None = 0.05,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Arrange selected UV islands on a line

                :param execution_context:
                :param undo:
                :param initial_position: Initial Position, Initial position to arrange islands from (optional)

        BOUNDING_BOX
        Bounding Box -- Initial alignment based on the islands bounding box.

        UV_GRID
        UV Grid -- Initial alignment based on UV Tile Grid.

        ACTIVE_UDIM
        Active UDIM -- Initial alignment based on Active UDIM.

        CURSOR
        2D Cursor -- Initial alignment based on 2D cursor.
                :param axis: Axis, Axis to arrange UV islands on (optional)

        X
        X -- Align UV islands along the X axis.

        Y
        Y -- Align UV islands along the Y axis.
                :param align: Align, Location to align islands on (optional)

        MIN
        Min -- Align the islands to the min of the island.

        MAX
        Max -- Align the islands to the max side of the island.

        CENTER
        Center -- Align the islands to the center of the largest island.

        NONE
        None -- Preserve island alignment.
                :param order: Order, Order of islands (optional)

        LARGE_TO_SMALL
        Largest to Smallest -- Sort islands from largest to smallest.

        SMALL_TO_LARGE
        Smallest to Largest -- Sort islands from smallest to largest.

        Fixed
        Fixed -- Preserve island order.
                :param margin: Margin, Space between islands (in [0, 1], optional)
                :return: Result of the operator call.
        """

class average_islands_scale(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        scale_uv: bool | None = False,
        shear: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Average the size of separate UV islands, based on their area in 3D space

        :param execution_context:
        :param undo:
        :param scale_uv: Non-Uniform, Scale U and V independently (optional)
        :param shear: Shear, Reduce shear within islands (optional)
        :return: Result of the operator call.
        """

class copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy selected UV vertices

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class copy_mirrored_faces(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mesh_axis: typing.Literal[bpy.stub_internal.rna_enums.ObjectAxisFlipItems]
        | None = "POS_X",
        uv_axis: typing.Literal[bpy.stub_internal.rna_enums.AxisXyItems] | None = "X",
        precision: int | None = 3,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy mirror UV coordinates based on a mirrored mesh

        :param execution_context:
        :param undo:
        :param mesh_axis: Mesh Axis, Mirror vertices based on mesh axis (optional)
        :param uv_axis: UV Axis, Axis to mirror UV coordinates (optional)
        :param precision: Precision, Tolerance for finding vertex duplicates (in [1, 16], optional)
        :return: Result of the operator call.
        """

class cube_project(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        cube_size: float | None = 1.0,
        correct_aspect: bool | None = True,
        clip_to_bounds: bool | None = False,
        scale_to_bounds: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Project the UV vertices of the mesh over the six faces of a cube

        :param execution_context:
        :param undo:
        :param cube_size: Cube Size, Size of the cube to project on (in [0, inf], optional)
        :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)
        :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping (optional)
        :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping (optional)
        :return: Result of the operator call.
        """

class cursor_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        location: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set 2D cursor location

        :param execution_context:
        :param undo:
        :param location: Location, Cursor location in normalized (0.0 to 1.0) coordinates (array of 2 items, in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class custom_region_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        xmin: int | None = 0,
        xmax: int | None = 0,
        ymin: int | None = 0,
        ymax: int | None = 0,
        wait_for_input: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the boundaries of the user region

        :param execution_context:
        :param undo:
        :param xmin: X Min, (in [-inf, inf], optional)
        :param xmax: X Max, (in [-inf, inf], optional)
        :param ymin: Y Min, (in [-inf, inf], optional)
        :param ymax: Y Max, (in [-inf, inf], optional)
        :param wait_for_input: Wait for Input, (optional)
        :return: Result of the operator call.
        """

class cylinder_project(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal["VIEW_ON_EQUATOR", "VIEW_ON_POLES", "ALIGN_TO_OBJECT"]
        | None = "VIEW_ON_EQUATOR",
        align: typing.Literal["POLAR_ZX", "POLAR_ZY"] | None = "POLAR_ZX",
        pole: typing.Literal["PINCH", "FAN"] | None = "PINCH",
        seam: bool | None = False,
        radius: float | None = 1.0,
        correct_aspect: bool | None = True,
        clip_to_bounds: bool | None = False,
        scale_to_bounds: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Project the UV vertices of the mesh over the curved wall of a cylinder

                :param execution_context:
                :param undo:
                :param direction: Direction, Direction of the sphere or cylinder (optional)

        VIEW_ON_EQUATOR
        View on Equator -- 3D view is on the equator.

        VIEW_ON_POLES
        View on Poles -- 3D view is on the poles.

        ALIGN_TO_OBJECT
        Align to Object -- Align according to object transform.
                :param align: Align, How to determine rotation around the pole (optional)

        POLAR_ZX
        Polar ZX -- Polar 0 is X.

        POLAR_ZY
        Polar ZY -- Polar 0 is Y.
                :param pole: Pole, How to handle faces at the poles (optional)

        PINCH
        Pinch -- UVs are pinched at the poles.

        FAN
        Fan -- UVs are fanned at the poles.
                :param seam: Preserve Seams, Separate projections by islands isolated by seams (optional)
                :param radius: Radius, Radius of the sphere or cylinder (in [0, inf], optional)
                :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)
                :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping (optional)
                :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping (optional)
                :return: Result of the operator call.
        """

class export_layout(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        export_all: bool | None = False,
        export_tiles: typing.Literal["NONE", "UDIM", "UV"] | None = "NONE",
        modified: bool | None = False,
        mode: typing.Literal["SVG", "EPS", "PNG"] | None = "PNG",
        size: collections.abc.Sequence[int] | None = (1024, 1024),
        opacity: float | None = 0.25,
        check_existing: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Export UV layout to file

                :param execution_context:
                :param undo:
                :param filepath: filepath, (optional, never None)
                :param export_all: All UVs, Export all UVs in this mesh (not just visible ones) (optional)
                :param export_tiles: Export Tiles, Choose whether to export only the [0, 1] range, or all UV tiles (optional)

        NONE
        None -- Export only UVs in the [0, 1] range.

        UDIM
        UDIM -- Export tiles in the UDIM numbering scheme: 1001 + u_tile + 10*v_tile.

        UV
        UVTILE -- Export tiles in the UVTILE numbering scheme: u(u_tile + 1)_v(v_tile + 1).
                :param modified: Modified, Exports UVs from the modified mesh (optional)
                :param mode: Format, File format to export the UV layout to (optional)

        SVG
        Scalable Vector Graphic (.svg) -- Export the UV layout to a vector SVG file.

        EPS
        Encapsulated PostScript (.eps) -- Export the UV layout to a vector EPS file.

        PNG
        PNG Image (.png) -- Export the UV layout to a bitmap image.
                :param size: Size, Dimensions of the exported file (array of 2 items, in [8, 32768], optional)
                :param opacity: Fill Opacity, Set amount of opacity for exported UV layout (in [0, 1], optional)
                :param check_existing: check_existing, (optional)
                :return: Result of the operator call.
        """

class follow_active_quads(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["EVEN", "LENGTH", "LENGTH_AVERAGE"]
        | None = "LENGTH_AVERAGE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Follow UVs from active quads along continuous face loops

                :param execution_context:
                :param undo:
                :param mode: Edge Length Mode, Method to space UV edge loops (optional)

        EVEN
        Even -- Space all UVs evenly.

        LENGTH
        Length -- Average space UVs edge length of each loop.

        LENGTH_AVERAGE
        Length Average -- Average space UVs edge length of each loop.
                :return: Result of the operator call.
        """

class hide(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        unselected: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Hide (un)selected UV vertices

        :param execution_context:
        :param undo:
        :param unselected: Unselected, Hide unselected rather than selected (optional)
        :return: Result of the operator call.
        """

class lightmap_pack(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        PREF_CONTEXT: typing.Literal["SEL_FACES", "ALL_FACES"] | None = "SEL_FACES",
        PREF_PACK_IN_ONE: bool | None = True,
        PREF_NEW_UVLAYER: bool | None = False,
        PREF_BOX_DIV: int | None = 12,
        PREF_MARGIN_DIV: float | None = 0.1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Pack each faces UVs into the UV bounds

                :param execution_context:
                :param undo:
                :param PREF_CONTEXT: Selection, (optional)

        SEL_FACES
        Selected Faces -- Pack only selected faces.

        ALL_FACES
        All Faces -- Pack all faces in the mesh.
                :param PREF_PACK_IN_ONE: Share Texture Space, Objects share texture space, map all objects into a single UV map (optional)
                :param PREF_NEW_UVLAYER: New UV Map, Create a new UV map for every mesh packed (optional)
                :param PREF_BOX_DIV: Pack Quality, Quality of the packing. Higher values will be slower but waste less space (in [1, 48], optional)
                :param PREF_MARGIN_DIV: Margin, Size of the margin as a division of the UV (in [0.001, 1], optional)
                :return: Result of the operator call.
        """

class mark_seam(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        clear: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Mark selected UV edges as seams

        :param execution_context:
        :param undo:
        :param clear: Clear Seams, Clear instead of marking seams (optional)
        :return: Result of the operator call.
        """

class minimize_stretch(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        fill_holes: bool | None = True,
        blend: float | None = 0.0,
        iterations: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reduce UV stretching by relaxing angles

        :param execution_context:
        :param undo:
        :param fill_holes: Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry (optional)
        :param blend: Blend, Blend factor between stretch minimized and original (in [0, 1], optional)
        :param iterations: Iterations, Number of iterations to run, 0 is unlimited when run interactively (in [0, inf], optional)
        :return: Result of the operator call.
        """

class move_on_axis(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["DYNAMIC", "PIXEL", "UDIM"] | None = "UDIM",
        axis: typing.Literal["X", "Y"] | None = "X",
        distance: int | None = 1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move UVs on an axis

                :param execution_context:
                :param undo:
                :param type: Type, Move Type (optional)

        DYNAMIC
        Dynamic -- Move by dynamic grid.

        PIXEL
        Pixel -- Move by pixel.

        UDIM
        UDIM -- Move by UDIM.
                :param axis: Axis, Axis to move UVs on (optional)

        X
        X axis -- Move vertices on the X axis.

        Y
        Y axis -- Move vertices on the Y axis.
                :param distance: Distance, Distance to move UVs (in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class pack_islands(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        udim_source: typing.Literal[
            "CLOSEST_UDIM", "ACTIVE_UDIM", "ORIGINAL_AABB", "CUSTOM_REGION"
        ]
        | None = "CLOSEST_UDIM",
        rotate: bool | None = True,
        rotate_method: typing.Literal[
            "ANY", "CARDINAL", "AXIS_ALIGNED", "AXIS_ALIGNED_X", "AXIS_ALIGNED_Y"
        ]
        | None = "ANY",
        scale: bool | None = True,
        merge_overlap: bool | None = False,
        margin_method: typing.Literal["SCALED", "ADD", "FRACTION"] | None = "SCALED",
        margin: float | None = 0.001,
        pin: bool | None = False,
        pin_method: typing.Literal["SCALE", "ROTATION", "ROTATION_SCALE", "LOCKED"]
        | None = "LOCKED",
        shape_method: typing.Literal["CONCAVE", "CONVEX", "AABB"] | None = "CONCAVE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Transform all islands so that they fill up the UV/UDIM space as much as possible

                :param execution_context:
                :param undo:
                :param udim_source: Pack to, (optional)

        CLOSEST_UDIM
        Closest UDIM -- Pack islands to closest UDIM.

        ACTIVE_UDIM
        Active UDIM -- Pack islands to active UDIM image tile or UDIM grid tile where 2D cursor is located.

        ORIGINAL_AABB
        Original bounding box -- Pack to starting bounding box of islands.

        CUSTOM_REGION
        Custom Region -- Pack islands to custom region.
                :param rotate: Rotate, Rotate islands to improve layout (optional)
                :param rotate_method: Rotation Method, (optional)

        ANY
        Any -- Any angle is allowed for rotation.

        CARDINAL
        Cardinal -- Only 90 degree rotations are allowed.

        AXIS_ALIGNED
        Axis-aligned -- Rotated to a minimal rectangle, either vertical or horizontal.

        AXIS_ALIGNED_X
        Axis-aligned (Horizontal) -- Rotate islands to be aligned horizontally.

        AXIS_ALIGNED_Y
        Axis-aligned (Vertical) -- Rotate islands to be aligned vertically.
                :param scale: Scale, Scale islands to fill unit square (optional)
                :param merge_overlap: Merge Overlapping, Overlapping islands stick together (optional)
                :param margin_method: Margin Method, (optional)

        SCALED
        Scaled -- Use scale of existing UVs to multiply margin.

        ADD
        Add -- Just add the margin, ignoring any UV scale.

        FRACTION
        Fraction -- Specify a precise fraction of final UV output.
                :param margin: Margin, Space between islands (in [0, 1], optional)
                :param pin: Lock Pinned Islands, Constrain islands containing any pinned UVs (optional)
                :param pin_method: Pin Method, (optional)

        SCALE
        Scale -- Pinned islands wont rescale.

        ROTATION
        Rotation -- Pinned islands wont rotate.

        ROTATION_SCALE
        Rotation and Scale -- Pinned islands will translate only.

        LOCKED
        All -- Pinned islands are locked in place.
                :param shape_method: Shape Method, (optional)

        CONCAVE
        Exact Shape (Concave) -- Uses exact geometry.

        CONVEX
        Boundary Shape (Convex) -- Uses convex hull.

        AABB
        Bounding Box -- Uses bounding boxes.
                :return: Result of the operator call.
        """

class paste(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Paste selected UV vertices

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class pin(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        clear: bool | None = False,
        invert: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set/clear selected UV vertices as anchored between multiple unwrap operations

        :param execution_context:
        :param undo:
        :param clear: Clear, Clear pinning for the selection instead of setting it (optional)
        :param invert: Invert, Invert pinning for the selection instead of setting it (optional)
        :return: Result of the operator call.
        """

class project_from_view(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        orthographic: bool | None = False,
        camera_bounds: bool | None = True,
        correct_aspect: bool | None = True,
        clip_to_bounds: bool | None = False,
        scale_to_bounds: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Project the UV vertices of the mesh as seen in current 3D view

        :param execution_context:
        :param undo:
        :param orthographic: Orthographic, Use orthographic projection (optional)
        :param camera_bounds: Camera Bounds, Map UVs to the camera region taking resolution and aspect into account (optional)
        :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)
        :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping (optional)
        :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping (optional)
        :return: Result of the operator call.
        """

class randomize_uv_transform(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        random_seed: int | None = 0,
        use_loc: bool | None = True,
        loc: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
        use_rot: bool | None = True,
        rot: float | None = 0.0,
        use_scale: bool | None = True,
        scale_even: bool | None = False,
        scale: collections.abc.Sequence[float] | None = (1.0, 1.0),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Randomize the UV islands location, rotation, and scale

        :param execution_context:
        :param undo:
        :param random_seed: Random Seed, Seed value for the random generator (in [0, 10000], optional)
        :param use_loc: Randomize Location, Randomize the location values (optional)
        :param loc: Location, Maximum distance the objects can spread over each axis (array of 2 items, in [-100, 100], optional)
        :param use_rot: Randomize Rotation, Randomize the rotation value (optional)
        :param rot: Rotation, Maximum rotation (in [-6.28319, 6.28319], optional)
        :param use_scale: Randomize Scale, Randomize the scale values (optional)
        :param scale_even: Scale Even, Use the same scale value for both axes (optional)
        :param scale: Scale, Maximum scale randomization over each axis (array of 2 items, in [-100, 100], optional)
        :return: Result of the operator call.
        """

class remove_doubles(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        threshold: float | None = 0.02,
        use_unselected: bool | None = False,
        use_shared_vertex: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Selected UV vertices that are within a radius of each other are welded together

        :param execution_context:
        :param undo:
        :param threshold: Merge Distance, Maximum distance between welded vertices (in [0, 10], optional)
        :param use_unselected: Unselected, Merge selected to other unselected vertices (optional)
        :param use_shared_vertex: Shared Vertex, Weld UVs based on shared vertices (optional)
        :return: Result of the operator call.
        """

class reset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset UV projection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class reveal(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        select: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reveal all hidden UV vertices

        :param execution_context:
        :param undo:
        :param select: Select, (optional)
        :return: Result of the operator call.
        """

class rip(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mirror: bool | None = False,
        release_confirm: bool | None = False,
        use_accurate: bool | None = False,
        location: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Rip selected vertices or a selected region

        :param execution_context:
        :param undo:
        :param mirror: Mirror Editing, (optional)
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button (optional)
        :param use_accurate: Accurate, Use accurate transformation (optional)
        :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds (array of 2 items, in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class rip_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        UV_OT_rip: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Unstitch UVs and move the result

        :param execution_context:
        :param undo:
        :param UV_OT_rip: Rip UVs, Rip selected vertices or a selected region (optional, `bpy.ops.uv.rip` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class seams_from_islands(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mark_seams: bool | None = True,
        mark_sharp: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set mesh seams according to island setup in the UV editor

        :param execution_context:
        :param undo:
        :param mark_seams: Mark Seams, Mark boundary edges as seams (optional)
        :param mark_sharp: Mark Sharp, Mark boundary edges as sharp (optional)
        :return: Result of the operator call.
        """

class select(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        extend: bool | None = False,
        deselect: bool | None = False,
        toggle: bool | None = False,
        deselect_all: bool | None = False,
        select_passthrough: bool | None = False,
        location: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select UV vertices

        :param execution_context:
        :param undo:
        :param extend: Extend, Extend selection instead of deselecting everything first (optional)
        :param deselect: Deselect, Remove from selection (optional)
        :param toggle: Toggle Selection, Toggle the selection (optional)
        :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor (optional)
        :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected (optional)
        :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds (array of 2 items, in [-inf, inf], optional)
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
        """Change selection of all UV vertices

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

class select_box(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        pinned: bool | None = False,
        xmin: int | None = 0,
        xmax: int | None = 0,
        ymin: int | None = 0,
        ymax: int | None = 0,
        wait_for_input: bool | None = True,
        mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select UV vertices using box selection

                :param execution_context:
                :param undo:
                :param pinned: Pinned, Border select pinned UVs only (optional)
                :param xmin: X Min, (in [-inf, inf], optional)
                :param xmax: X Max, (in [-inf, inf], optional)
                :param ymin: Y Min, (in [-inf, inf], optional)
                :param ymax: Y Max, (in [-inf, inf], optional)
                :param wait_for_input: Wait for Input, (optional)
                :param mode: Mode, (optional)

        SET
        Set -- Set a new selection.

        ADD
        Extend -- Extend existing selection.

        SUB
        Subtract -- Subtract existing selection.
                :return: Result of the operator call.
        """

class select_by_winding(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        winding: typing.Literal["POSITIVE", "NEGATIVE"] | None = "NEGATIVE",
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select UV faces by their winding

        :param execution_context:
        :param undo:
        :param winding: Winding, Select faces with positive or negative winding (optional)
        :param extend: Extend, Extend selection rather than clearing the existing selection (optional)
        :return: Result of the operator call.
        """

class select_circle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        x: int | None = 0,
        y: int | None = 0,
        radius: int | None = 25,
        wait_for_input: bool | None = True,
        mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select UV vertices using circle selection

                :param execution_context:
                :param undo:
                :param x: X, (in [-inf, inf], optional)
                :param y: Y, (in [-inf, inf], optional)
                :param radius: Radius, (in [1, inf], optional)
                :param wait_for_input: Wait for Input, (optional)
                :param mode: Mode, (optional)

        SET
        Set -- Set a new selection.

        ADD
        Extend -- Extend existing selection.

        SUB
        Subtract -- Subtract existing selection.
                :return: Result of the operator call.
        """

class select_edge_ring(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        extend: bool | None = False,
        location: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select an edge ring of connected UV vertices

        :param execution_context:
        :param undo:
        :param extend: Extend, Extend selection rather than clearing the existing selection (optional)
        :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds (array of 2 items, in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class select_lasso(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        path: None
        | bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath]
        | None = None,
        use_smooth_stroke: bool | None = False,
        smooth_stroke_factor: float | None = 0.75,
        smooth_stroke_radius: int | None = 35,
        mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select UVs using lasso selection

                :param execution_context:
                :param undo:
                :param path: Path, (optional)
                :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path (optional)
                :param smooth_stroke_factor: Smooth Stroke Factor, Higher values give a smoother stroke (in [0.5, 0.99], optional)
                :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues (in [10, 200], optional)
                :param mode: Mode, (optional)

        SET
        Set -- Set a new selection.

        ADD
        Extend -- Extend existing selection.

        SUB
        Subtract -- Subtract existing selection.
                :return: Result of the operator call.
        """

class select_less(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Deselect UV vertices at the boundary of each selection region

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
        delimit: set[typing.Literal["SEAM", "SHARP", "MATERIAL"]] | None = set(),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all UV vertices linked to the active UV map

                :param execution_context:
                :param undo:
                :param delimit: Delimit, Delimit selection when selecting linked UVs (optional)

        SEAM
        Seam -- Delimit by edge seams.

        SHARP
        Sharp -- Delimit by sharp edges.

        MATERIAL
        Material -- Delimit by face material.
                :return: Result of the operator call.
        """

class select_linked_pick(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        extend: bool | None = False,
        deselect: bool | None = False,
        delimit: set[typing.Literal["SEAM", "SHARP", "MATERIAL"]] | None = set(),
        location: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all UV vertices linked under the mouse

                :param execution_context:
                :param undo:
                :param extend: Extend, Extend selection rather than clearing the existing selection (optional)
                :param deselect: Deselect, Deselect linked UV vertices rather than selecting them (optional)
                :param delimit: Delimit, Delimit selection when selecting linked UVs (optional)

        SEAM
        Seam -- Delimit by edge seams.

        SHARP
        Sharp -- Delimit by sharp edges.

        MATERIAL
        Material -- Delimit by face material.
                :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds (array of 2 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class select_loop(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        extend: bool | None = False,
        location: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select a loop of connected UV vertices

        :param execution_context:
        :param undo:
        :param extend: Extend, Extend selection rather than clearing the existing selection (optional)
        :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds (array of 2 items, in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class select_mode(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[bpy.stub_internal.rna_enums.MeshSelectModeUvItems]
        | None = "VERTEX",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change UV selection mode

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class select_more(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select more UV vertices connected to initial selection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_overlap(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all UV faces which overlap each other

        :param execution_context:
        :param undo:
        :param extend: Extend, Extend selection rather than clearing the existing selection (optional)
        :return: Result of the operator call.
        """

class select_pinned(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all pinned UV vertices

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_similar(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            "PIN",
            "LENGTH",
            "LENGTH_3D",
            "AREA",
            "AREA_3D",
            "MATERIAL",
            "OBJECT",
            "SIDES",
            "WINDING",
            "FACE",
        ]
        | None = "PIN",
        compare: typing.Literal["EQUAL", "GREATER", "LESS"] | None = "EQUAL",
        threshold: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select similar UVs by property types

                :param execution_context:
                :param undo:
                :param type: Type, (optional)

        PIN
        Pinned.

        LENGTH
        Length -- Edge length in UV space.

        LENGTH_3D
        Length 3D -- Length of edge in 3D space.

        AREA
        Area -- Face area in UV space.

        AREA_3D
        Area 3D -- Area of face in 3D space.

        MATERIAL
        Material.

        OBJECT
        Object.

        SIDES
        Polygon Sides.

        WINDING
        Winding -- Face direction defined by clockwise or anti-clockwise winding (facing up or facing down).

        FACE
        Amount of Faces in Island.
                :param compare: Compare, (optional)
                :param threshold: Threshold, (in [0, 1], optional)
                :return: Result of the operator call.
        """

class select_split(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select only entirely selected faces

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_tile(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        extend: bool | None = False,
        tile: collections.abc.Sequence[int] | None = (0, 0),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select UVs in specified tile

        :param execution_context:
        :param undo:
        :param extend: Extend, Extend the selection (optional)
        :param tile: Tile, Tile location to select UVs (array of 2 items, in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class shortest_path_pick(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_face_step: bool | None = False,
        use_topology_distance: bool | None = False,
        use_fill: bool | None = False,
        skip: int | None = 0,
        nth: int | None = 1,
        offset: int | None = 0,
        object_index: int | None = -1,
        index: int | None = -1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select shortest path between two selections

        :param execution_context:
        :param undo:
        :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings) (optional)
        :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance (optional)
        :param use_fill: Fill Region, Select all paths between the source/destination elements (optional)
        :param skip: Deselected, Number of deselected elements in the repetitive sequence (in [0, inf], optional)
        :param nth: Selected, Number of selected elements in the repetitive sequence (in [1, inf], optional)
        :param offset: Offset, Offset from the starting point (in [-inf, inf], optional)
        :param object_index: (in [-1, inf], optional)
        :param index: (in [-1, inf], optional)
        :return: Result of the operator call.
        """

class shortest_path_select(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_face_step: bool | None = False,
        use_topology_distance: bool | None = False,
        use_fill: bool | None = False,
        skip: int | None = 0,
        nth: int | None = 1,
        offset: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select shortest path between two vertices/edges/faces

        :param execution_context:
        :param undo:
        :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings) (optional)
        :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance (optional)
        :param use_fill: Fill Region, Select all paths between the source/destination elements (optional)
        :param skip: Deselected, Number of deselected elements in the repetitive sequence (in [0, inf], optional)
        :param nth: Selected, Number of selected elements in the repetitive sequence (in [1, inf], optional)
        :param offset: Offset, Offset from the starting point (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class smart_project(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        angle_limit: float | None = 1.15192,
        margin_method: typing.Literal["SCALED", "ADD", "FRACTION"] | None = "SCALED",
        rotate_method: typing.Literal[
            "AXIS_ALIGNED", "AXIS_ALIGNED_X", "AXIS_ALIGNED_Y"
        ]
        | None = "AXIS_ALIGNED_Y",
        island_margin: float | None = 0.0,
        area_weight: float | None = 0.0,
        correct_aspect: bool | None = True,
        scale_to_bounds: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Projection unwraps the selected faces of mesh objects

                :param execution_context:
                :param undo:
                :param angle_limit: Angle Limit, Lower for more projection groups, higher for less distortion (in [0, 1.5708], optional)
                :param margin_method: Margin Method, (optional)

        SCALED
        Scaled -- Use scale of existing UVs to multiply margin.

        ADD
        Add -- Just add the margin, ignoring any UV scale.

        FRACTION
        Fraction -- Specify a precise fraction of final UV output.
                :param rotate_method: Rotation Method, (optional)

        AXIS_ALIGNED
        Axis-aligned -- Rotated to a minimal rectangle, either vertical or horizontal.

        AXIS_ALIGNED_X
        Axis-aligned (Horizontal) -- Rotate islands to be aligned horizontally.

        AXIS_ALIGNED_Y
        Axis-aligned (Vertical) -- Rotate islands to be aligned vertically.
                :param island_margin: Island Margin, Margin to reduce bleed from adjacent islands (in [0, 1], optional)
                :param area_weight: Area Weight, Weight projections vector by faces with larger areas (in [0, 1], optional)
                :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)
                :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping (optional)
                :return: Result of the operator call.
        """

class snap_cursor(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        target: typing.Literal["PIXELS", "SELECTED", "ORIGIN"] | None = "PIXELS",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Snap cursor to target type

        :param execution_context:
        :param undo:
        :param target: Target, Target to snap the selected UVs to (optional)
        :return: Result of the operator call.
        """

class snap_selected(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        target: typing.Literal[
            "PIXELS", "CURSOR", "CURSOR_OFFSET", "ADJACENT_UNSELECTED"
        ]
        | None = "PIXELS",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Snap selected UV vertices to target type

        :param execution_context:
        :param undo:
        :param target: Target, Target to snap the selected UVs to (optional)
        :return: Result of the operator call.
        """

class sphere_project(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal["VIEW_ON_EQUATOR", "VIEW_ON_POLES", "ALIGN_TO_OBJECT"]
        | None = "VIEW_ON_EQUATOR",
        align: typing.Literal["POLAR_ZX", "POLAR_ZY"] | None = "POLAR_ZX",
        pole: typing.Literal["PINCH", "FAN"] | None = "PINCH",
        seam: bool | None = False,
        correct_aspect: bool | None = True,
        clip_to_bounds: bool | None = False,
        scale_to_bounds: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Project the UV vertices of the mesh over the curved surface of a sphere

                :param execution_context:
                :param undo:
                :param direction: Direction, Direction of the sphere or cylinder (optional)

        VIEW_ON_EQUATOR
        View on Equator -- 3D view is on the equator.

        VIEW_ON_POLES
        View on Poles -- 3D view is on the poles.

        ALIGN_TO_OBJECT
        Align to Object -- Align according to object transform.
                :param align: Align, How to determine rotation around the pole (optional)

        POLAR_ZX
        Polar ZX -- Polar 0 is X.

        POLAR_ZY
        Polar ZY -- Polar 0 is Y.
                :param pole: Pole, How to handle faces at the poles (optional)

        PINCH
        Pinch -- UVs are pinched at the poles.

        FAN
        Fan -- UVs are fanned at the poles.
                :param seam: Preserve Seams, Separate projections by islands isolated by seams (optional)
                :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)
                :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping (optional)
                :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping (optional)
                :return: Result of the operator call.
        """

class stitch(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_limit: bool | None = False,
        snap_islands: bool | None = True,
        limit: float | None = 0.01,
        static_island: int | None = 0,
        active_object_index: int | None = 0,
        midpoint_snap: bool | None = False,
        clear_seams: bool | None = True,
        mode: typing.Literal["VERTEX", "EDGE"] | None = "VERTEX",
        stored_mode: typing.Literal["VERTEX", "EDGE"] | None = "VERTEX",
        selection: None
        | bpy.types.bpy_prop_collection[bpy.types.SelectedUvElement]
        | None = None,
        objects_selection_count: collections.abc.Sequence[int] | None = (
            0,
            0,
            0,
            0,
            0,
            0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Stitch selected UV vertices by proximity

        :param execution_context:
        :param undo:
        :param use_limit: Use Limit, Stitch UVs within a specified limit distance (optional)
        :param snap_islands: Snap Islands, Snap islands together (on edge stitch mode, rotates the islands too) (optional)
        :param limit: Limit, Limit distance in normalized coordinates (in [0, inf], optional)
        :param static_island: Static Island, Island that stays in place when stitching islands (in [0, inf], optional)
        :param active_object_index: Active Object, Index of the active object (in [0, inf], optional)
        :param midpoint_snap: Snap at Midpoint, UVs are stitched at midpoint instead of at static island (optional)
        :param clear_seams: Clear Seams, Clear seams of stitched edges (optional)
        :param mode: Operation Mode, Use vertex or edge stitching (optional)
        :param stored_mode: Stored Operation Mode, Use vertex or edge stitching (optional)
        :param selection: Selection, (optional)
        :param objects_selection_count: Objects Selection Count, (array of 6 items, in [0, inf], optional)
        :return: Result of the operator call.
        """

class unwrap(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        method: typing.Literal["ANGLE_BASED", "CONFORMAL", "MINIMUM_STRETCH"]
        | None = "CONFORMAL",
        fill_holes: bool | None = False,
        correct_aspect: bool | None = True,
        use_subsurf_data: bool | None = False,
        use_original_bounds: bool | None = False,
        margin_method: typing.Literal["SCALED", "ADD", "FRACTION"] | None = "SCALED",
        margin: float | None = 0.001,
        no_flip: bool | None = False,
        iterations: int | None = 10,
        use_weights: bool | None = False,
        weight_group: str = "uv_importance",
        weight_factor: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Unwrap the mesh of the object being edited

                :param execution_context:
                :param undo:
                :param method: Method, Unwrapping method (Angle Based usually gives better results than Conformal, while being somewhat slower) (optional)
                :param fill_holes: Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry (optional)
                :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)
                :param use_subsurf_data: Use Subdivision Surface, Map UVs taking vertex position after Subdivision Surface modifier has been applied (optional)
                :param use_original_bounds: Original Bounds, Unwrap islands into their original bounds, instead of re-packing (optional)
                :param margin_method: Margin Method, (optional)

        SCALED
        Scaled -- Use scale of existing UVs to multiply margin.

        ADD
        Add -- Just add the margin, ignoring any UV scale.

        FRACTION
        Fraction -- Specify a precise fraction of final UV output.
                :param margin: Margin, Space between islands (in [0, 1], optional)
                :param no_flip: No Flip, Prevent flipping UVs, flipping may lower distortion depending on the position of pins (optional)
                :param iterations: Iterations, Number of iterations when "Minimum Stretch" method is used (in [0, 10000], optional)
                :param use_weights: Importance Weights, Whether to take into account per-vertex importance weights (optional)
                :param weight_group: Weight Group, Vertex group name for importance weights (modulating the deform) (optional, never None)
                :param weight_factor: Weight Factor, How much influence the weightmap has for weighted parameterization, 0 being no influence (in [-10000, 10000], optional)
                :return: Result of the operator call.
        """

class weld(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Weld selected UV vertices together

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
