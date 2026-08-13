import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums
import mathutils

class attribute_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        value_float: float | None = 0.0,
        value_float_vector_2d: collections.abc.Sequence[float] | None = (0.0, 0.0),
        value_float_vector_3d: collections.abc.Sequence[float] | None = (0.0, 0.0, 0.0),
        value_int: int | None = 0,
        value_int_vector_2d: collections.abc.Sequence[int] | None = (0, 0),
        value_color: collections.abc.Sequence[float] | None = (1.0, 1.0, 1.0, 1.0),
        value_bool: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set values of the active attribute for selected elements

        :param execution_context:
        :param undo:
        :param value_float: Value, (in [-inf, inf], optional)
        :param value_float_vector_2d: Value, (array of 2 items, in [-inf, inf], optional)
        :param value_float_vector_3d: Value, (array of 3 items, in [-inf, inf], optional)
        :param value_int: Value, (in [-inf, inf], optional)
        :param value_int_vector_2d: Value, (array of 2 items, in [-inf, inf], optional)
        :param value_color: Value, (array of 4 items, in [-inf, inf], optional)
        :param value_bool: Value, (optional)
        :return: Result of the operator call.
        """

class average_normals(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        average_type: typing.Literal["CUSTOM_NORMAL", "FACE_AREA", "CORNER_ANGLE"]
        | None = "CUSTOM_NORMAL",
        weight: int | None = 50,
        threshold: float | None = 0.01,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Average custom normals of selected vertices

                :param execution_context:
                :param undo:
                :param average_type: Type, Averaging method (optional)

        CUSTOM_NORMAL
        Custom Normal -- Take average of vertex normals.

        FACE_AREA
        Face Area -- Set all vertex normals by face area.

        CORNER_ANGLE
        Corner Angle -- Set all vertex normals by corner angle.
                :param weight: Weight, Weight applied per face (in [1, 100], optional)
                :param threshold: Threshold, Threshold value for different weights to be considered equal (in [0, 10], optional)
                :return: Result of the operator call.
        """

class beautify_fill(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        angle_limit: float | None = 3.14159,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Rearrange some faces to try to get less degenerated geometry

        :param execution_context:
        :param undo:
        :param angle_limit: Max Angle, Angle limit (in [0, 3.14159], optional)
        :return: Result of the operator call.
        """

class bevel(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        offset_type: typing.Literal["OFFSET", "WIDTH", "DEPTH", "PERCENT", "ABSOLUTE"]
        | None = "OFFSET",
        offset: float | None = 0.0,
        profile_type: typing.Literal["SUPERELLIPSE", "CUSTOM"] | None = "SUPERELLIPSE",
        offset_pct: float | None = 0.0,
        segments: int | None = 1,
        profile: float | None = 0.5,
        affect: typing.Literal["VERTICES", "EDGES"] | None = "EDGES",
        clamp_overlap: bool | None = False,
        loop_slide: bool | None = True,
        mark_seam: bool | None = False,
        mark_sharp: bool | None = False,
        material: int | None = -1,
        harden_normals: bool | None = False,
        face_strength_mode: typing.Literal["NONE", "NEW", "AFFECTED", "ALL"]
        | None = "NONE",
        miter_outer: typing.Literal["SHARP", "PATCH", "ARC"] | None = "SHARP",
        miter_inner: typing.Literal["SHARP", "ARC"] | None = "SHARP",
        spread: float | None = 0.1,
        vmesh_method: typing.Literal["ADJ", "CUTOFF"] | None = "ADJ",
        release_confirm: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Cut into selected items at an angle to create bevel or chamfer

                :param execution_context:
                :param undo:
                :param offset_type: Width Type, The method for determining the size of the bevel (optional)

        OFFSET
        Offset -- Amount is offset of new edges from original.

        WIDTH
        Width -- Amount is width of new face.

        DEPTH
        Depth -- Amount is perpendicular distance from original edge to bevel face.

        PERCENT
        Percent -- Amount is percent of adjacent edge length.

        ABSOLUTE
        Absolute -- Amount is absolute distance along adjacent edge.
                :param offset: Width, Bevel amount (in [0, 1e+06], optional)
                :param profile_type: Profile Type, The type of shape used to rebuild a beveled section (optional)

        SUPERELLIPSE
        Superellipse -- The profile can be a concave or convex curve.

        CUSTOM
        Custom -- The profile can be any arbitrary path between its endpoints.
                :param offset_pct: Width Percent, Bevel amount for percentage method (in [0, 100], optional)
                :param segments: Segments, Segments for curved edge (in [1, 1000], optional)
                :param profile: Profile, Controls profile shape (0.5 = round) (in [0, 1], optional)
                :param affect: Affect, Affect edges or vertices (optional)

        VERTICES
        Vertices -- Affect only vertices.

        EDGES
        Edges -- Affect only edges.
                :param clamp_overlap: Clamp Overlap, Do not allow beveled edges/vertices to overlap each other (optional)
                :param loop_slide: Loop Slide, Prefer sliding along edges to even widths (optional)
                :param mark_seam: Mark Seams, Preserve seams along beveled edges (optional)
                :param mark_sharp: Mark Sharp, Preserve sharp edges along beveled edges (optional)
                :param material: Material Index, Material for bevel faces (-1 means use adjacent faces) (in [-1, inf], optional)
                :param harden_normals: Harden Normals, Match normals of new faces to adjacent faces (optional)
                :param face_strength_mode: Face Strength Mode, Whether to set face strength, and which faces to set face strength on (optional)

        NONE
        None -- Do not set face strength.

        NEW
        New -- Set face strength on new faces only.

        AFFECTED
        Affected -- Set face strength on new and modified faces only.

        ALL
        All -- Set face strength on all faces.
                :param miter_outer: Outer Miter, Pattern to use for outside of miters (optional)

        SHARP
        Sharp -- Outside of miter is sharp.

        PATCH
        Patch -- Outside of miter is squared-off patch.

        ARC
        Arc -- Outside of miter is arc.
                :param miter_inner: Inner Miter, Pattern to use for inside of miters (optional)

        SHARP
        Sharp -- Inside of miter is sharp.

        ARC
        Arc -- Inside of miter is arc.
                :param spread: Spread, Amount to spread arcs for arc inner miters (in [0, 1e+06], optional)
                :param vmesh_method: Vertex Mesh Method, The method to use to create meshes at intersections (optional)

        ADJ
        Grid Fill -- Default patterned fill.

        CUTOFF
        Cutoff -- A cutoff at each profiles end before the intersection.
                :param release_confirm: Confirm on Release, (optional)
                :return: Result of the operator call.
        """

class bisect(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        plane_co: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
        plane_no: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
        use_fill: bool | None = False,
        clear_inner: bool | None = False,
        clear_outer: bool | None = False,
        threshold: float | None = 0.0001,
        xstart: int | None = 0,
        xend: int | None = 0,
        ystart: int | None = 0,
        yend: int | None = 0,
        flip: bool | None = False,
        cursor: int | None = 5,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Cut geometry along a plane (click-drag to define plane)

        :param execution_context:
        :param undo:
        :param plane_co: Plane Point, A point on the plane (array of 3 items, in [-inf, inf], optional)
        :param plane_no: Plane Normal, The direction the plane points (array of 3 items, in [-1, 1], optional)
        :param use_fill: Fill, Fill in the cut (optional)
        :param clear_inner: Clear Inner, Remove geometry behind the plane (optional)
        :param clear_outer: Clear Outer, Remove geometry in front of the plane (optional)
        :param threshold: Axis Threshold, Preserves the existing geometry along the cut plane (in [0, 10], optional)
        :param xstart: X Start, (in [-inf, inf], optional)
        :param xend: X End, (in [-inf, inf], optional)
        :param ystart: Y Start, (in [-inf, inf], optional)
        :param yend: Y End, (in [-inf, inf], optional)
        :param flip: Flip, (optional)
        :param cursor: Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)
        :return: Result of the operator call.
        """

class blend_from_shape(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        shape: str | None = "",
        blend: float | None = 1.0,
        add: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Blend in shape from a shape key

        :param execution_context:
        :param undo:
        :param shape: Shape, Shape key to use for blending (optional)
        :param blend: Blend, Blending factor (in [-1000, 1000], optional)
        :param add: Add, Add rather than blend between shapes (optional)
        :return: Result of the operator call.
        """

class bridge_edge_loops(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["SINGLE", "CLOSED", "PAIRS"] | None = "SINGLE",
        use_merge: bool | None = False,
        merge_factor: float | None = 0.5,
        twist_offset: int | None = 0,
        number_cuts: int | None = 0,
        interpolation: typing.Literal["LINEAR", "PATH", "SURFACE"] | None = "PATH",
        smoothness: float | None = 1.0,
        profile_shape_factor: float | None = 0.0,
        profile_shape: typing.Literal[
            bpy.stub_internal.rna_enums.ProportionalFalloffCurveOnlyItems
        ]
        | None = "SMOOTH",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a bridge of faces between two or more selected edge loops

        :param execution_context:
        :param undo:
        :param type: Connect Loops, Method of bridging multiple loops (optional)
        :param use_merge: Merge, Merge rather than creating faces (optional)
        :param merge_factor: Merge Factor, (in [0, 1], optional)
        :param twist_offset: Twist, Twist offset for closed loops (in [-1000, 1000], optional)
        :param number_cuts: Number of Cuts, (in [0, 1000], optional)
        :param interpolation: Interpolation, Interpolation method (optional)
        :param smoothness: Smoothness, Smoothness factor (in [0, 1000], optional)
        :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded (in [-1000, 1000], optional)
        :param profile_shape: Profile Shape, Shape of the profile (optional)
        :return: Result of the operator call.
        """

class colors_reverse(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Flip direction of face corner color attribute inside faces

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class colors_rotate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_ccw: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Rotate face corner color attribute inside faces

        :param execution_context:
        :param undo:
        :param use_ccw: Counter Clockwise, (optional)
        :return: Result of the operator call.
        """

class convex_hull(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        delete_unused: bool | None = True,
        use_existing_faces: bool | None = True,
        make_holes: bool | None = False,
        join_triangles: bool | None = True,
        face_threshold: float | None = 0.698132,
        shape_threshold: float | None = 0.698132,
        topology_influence: float | None = 0.0,
        uvs: bool | None = False,
        vcols: bool | None = False,
        seam: bool | None = False,
        sharp: bool | None = False,
        materials: bool | None = False,
        deselect_joined: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Enclose selected vertices in a convex polyhedron

        :param execution_context:
        :param undo:
        :param delete_unused: Delete Unused, Delete selected elements that are not used by the hull (optional)
        :param use_existing_faces: Use Existing Faces, Skip hull triangles that are covered by a pre-existing face (optional)
        :param make_holes: Make Holes, Delete selected faces that are used by the hull (optional)
        :param join_triangles: Join Triangles, Merge adjacent triangles into quads (optional)
        :param face_threshold: Max Face Angle, Face angle limit (in [0, 3.14159], optional)
        :param shape_threshold: Max Shape Angle, Shape angle limit (in [0, 3.14159], optional)
        :param topology_influence: Topology Influence, How much to prioritize regular grids of quads as well as quads that touch existing quads (in [0, 2], optional)
        :param uvs: Compare UVs, (optional)
        :param vcols: Compare Color Attributes, (optional)
        :param seam: Compare Seam, (optional)
        :param sharp: Compare Sharp, (optional)
        :param materials: Compare Materials, (optional)
        :param deselect_joined: Deselect Joined, Only select remaining triangles that were not merged (optional)
        :return: Result of the operator call.
        """

class customdata_custom_splitnormals_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a custom normals layer, if none exists yet

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class customdata_custom_splitnormals_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the custom normals layer, if it exists

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class customdata_mask_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear vertex sculpt masking data from the mesh

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class customdata_skin_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a vertex skin layer

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class customdata_skin_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear vertex skin layer

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class decimate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        ratio: float | None = 1.0,
        use_vertex_group: bool | None = False,
        vertex_group_factor: float | None = 1.0,
        invert_vertex_group: bool | None = False,
        use_symmetry: bool | None = False,
        symmetry_axis: typing.Literal[bpy.stub_internal.rna_enums.AxisXyzItems]
        | None = "Y",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Simplify geometry by collapsing edges

        :param execution_context:
        :param undo:
        :param ratio: Ratio, (in [0, 1], optional)
        :param use_vertex_group: Vertex Group, Use active vertex group as an influence (optional)
        :param vertex_group_factor: Weight, Vertex group strength (in [0, 1000], optional)
        :param invert_vertex_group: Invert, Invert vertex group influence (optional)
        :param use_symmetry: Symmetry, Maintain symmetry on an axis (optional)
        :param symmetry_axis: Axis, Axis of symmetry (optional)
        :return: Result of the operator call.
        """

class delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["VERT", "EDGE", "FACE", "EDGE_FACE", "ONLY_FACE"]
        | None = "VERT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete selected vertices, edges or faces

        :param execution_context:
        :param undo:
        :param type: Type, Method used for deleting mesh data (optional)
        :return: Result of the operator call.
        """

class delete_edgeloop(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_face_split: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete an edge loop by merging the faces on each side

        :param execution_context:
        :param undo:
        :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry (optional)
        :return: Result of the operator call.
        """

class delete_loose(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_verts: bool | None = True,
        use_edges: bool | None = True,
        use_faces: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete loose vertices, edges or faces

        :param execution_context:
        :param undo:
        :param use_verts: Vertices, Remove loose vertices (optional)
        :param use_edges: Edges, Remove loose edges (optional)
        :param use_faces: Faces, Remove loose faces (optional)
        :return: Result of the operator call.
        """

class dissolve_degenerate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        threshold: float | None = 0.0001,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Dissolve zero area faces and zero length edges

        :param execution_context:
        :param undo:
        :param threshold: Merge Distance, Maximum distance between elements to merge (in [1e-06, 50], optional)
        :return: Result of the operator call.
        """

class dissolve_edges(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_verts: bool | None = True,
        angle_threshold: float | None = 3.14159,
        use_face_split: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Dissolve edges, merging faces

        :param execution_context:
        :param undo:
        :param use_verts: Dissolve Vertices, Dissolve remaining vertices which connect to only two edges (optional)
        :param angle_threshold: Angle Threshold, Remaining vertices which separate edge pairs are preserved if their edge angle exceeds this threshold. (in [0, 3.14159], optional)
        :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry (optional)
        :return: Result of the operator call.
        """

class dissolve_faces(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_verts: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Dissolve faces

        :param execution_context:
        :param undo:
        :param use_verts: Dissolve Vertices, Dissolve remaining vertices which connect to only two edges (optional)
        :return: Result of the operator call.
        """

class dissolve_limited(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        angle_limit: float | None = 0.0872665,
        use_dissolve_boundaries: bool | None = False,
        delimit: set[typing.Literal[bpy.stub_internal.rna_enums.MeshDelimitModeItems]]
        | None = {"NORMAL"},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Dissolve selected edges and vertices, limited by the angle of surrounding geometry

        :param execution_context:
        :param undo:
        :param angle_limit: Max Angle, Angle limit (in [0, 3.14159], optional)
        :param use_dissolve_boundaries: All Boundaries, Dissolve all vertices in between face boundaries (optional)
        :param delimit: Delimit, Delimit dissolve operation (optional)
        :return: Result of the operator call.
        """

class dissolve_mode(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_verts: bool | None = False,
        angle_threshold: float | None = 3.14159,
        use_face_split: bool | None = False,
        use_boundary_tear: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Dissolve geometry based on the selection mode

        :param execution_context:
        :param undo:
        :param use_verts: Dissolve Vertices, Dissolve remaining vertices which connect to only two edges (optional)
        :param angle_threshold: Angle Threshold, Remaining vertices which separate edge pairs are preserved if their edge angle exceeds this threshold. (in [0, 3.14159], optional)
        :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry (optional)
        :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces (optional)
        :return: Result of the operator call.
        """

class dissolve_verts(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_face_split: bool | None = False,
        use_boundary_tear: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Dissolve vertices, merge edges and faces

        :param execution_context:
        :param undo:
        :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry (optional)
        :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces (optional)
        :return: Result of the operator call.
        """

class dupli_extrude_cursor(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        rotate_source: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate and extrude selected vertices, edges or faces towards the mouse cursor

        :param execution_context:
        :param undo:
        :param rotate_source: Rotate Source, Rotate initial selection giving better shape (optional)
        :return: Result of the operator call.
        """

class duplicate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: int | None = 1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate selected vertices, edges or faces

        :param execution_context:
        :param undo:
        :param mode: Mode, (in [0, inf], optional)
        :return: Result of the operator call.
        """

class duplicate_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        MESH_OT_duplicate: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate mesh and move

        :param execution_context:
        :param undo:
        :param MESH_OT_duplicate: Duplicate, Duplicate selected vertices, edges or faces (optional, `bpy.ops.mesh.duplicate` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class edge_collapse(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Collapse isolated edge and face regions, merging data such as UVs and color attributes. This can collapse edge-rings as well as regions of connected faces into vertices

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class edge_face_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add an edge or face to selected

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class edge_rotate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_ccw: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Rotate selected edge or adjoining faces

        :param execution_context:
        :param undo:
        :param use_ccw: Counter Clockwise, (optional)
        :return: Result of the operator call.
        """

class edge_split(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["EDGE", "VERT"] | None = "EDGE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Split selected edges so that each neighbor face gets its own copy

                :param execution_context:
                :param undo:
                :param type: Type, Method to use for splitting (optional)

        EDGE
        Faces by Edges -- Split faces along selected edges.

        VERT
        Faces & Edges by Vertices -- Split faces and edges connected to selected vertices.
                :return: Result of the operator call.
        """

class edgering_select(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        delimit_edge_ring: set[
            typing.Literal[bpy.stub_internal.rna_enums.MeshWalkDelimitEdgeRingItems]
        ]
        | None = {"NGONS"},
        extend: bool | None = False,
        deselect: bool | None = False,
        toggle: bool | None = False,
        object_index: int | None = -1,
        edge_index: int | None = -1,
        vert_index: int | None = -1,
        face_index: int | None = -1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select an edge ring

        :param execution_context:
        :param undo:
        :param delimit_edge_ring: Edge Ring Delimit, Delimit edge ring selection (optional)
        :param extend: Extend Select, Extend the selection (optional)
        :param deselect: Deselect, Remove from the selection (optional)
        :param toggle: Toggle Select, Toggle the selection (optional)
        :param object_index: (in [-1, inf], optional)
        :param edge_index: (in [-1, inf], optional)
        :param vert_index: (in [-1, inf], optional)
        :param face_index: (in [-1, inf], optional)
        :return: Result of the operator call.
        """

class edges_select_sharp(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        sharpness: float | None = 0.523599,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all sharp enough edges

        :param execution_context:
        :param undo:
        :param sharpness: Sharpness, (in [0.000174533, 3.14159], optional)
        :return: Result of the operator call.
        """

class extrude_context(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_normal_flip: bool | None = False,
        use_dissolve_ortho_edges: bool | None = False,
        mirror: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude selection

        :param execution_context:
        :param undo:
        :param use_normal_flip: Flip Normals, (optional)
        :param use_dissolve_ortho_edges: Dissolve Orthogonal Edges, (optional)
        :param mirror: Mirror Editing, (optional)
        :return: Result of the operator call.
        """

class extrude_context_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        MESH_OT_extrude_context: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude region together along the average normal

        :param execution_context:
        :param undo:
        :param MESH_OT_extrude_context: Extrude Context, Extrude selection (optional, `bpy.ops.mesh.extrude_context` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class extrude_edges_indiv(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_normal_flip: bool | None = False,
        mirror: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude individual edges only

        :param execution_context:
        :param undo:
        :param use_normal_flip: Flip Normals, (optional)
        :param mirror: Mirror Editing, (optional)
        :return: Result of the operator call.
        """

class extrude_edges_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        MESH_OT_extrude_edges_indiv: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude edges and move result

        :param execution_context:
        :param undo:
        :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only (optional, `bpy.ops.mesh.extrude_edges_indiv` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class extrude_faces_indiv(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mirror: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude individual faces only

        :param execution_context:
        :param undo:
        :param mirror: Mirror Editing, (optional)
        :return: Result of the operator call.
        """

class extrude_faces_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        MESH_OT_extrude_faces_indiv: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_shrink_fatten: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude each individual face separately along local normals

        :param execution_context:
        :param undo:
        :param MESH_OT_extrude_faces_indiv: Extrude Individual Faces, Extrude individual faces only (optional, `bpy.ops.mesh.extrude_faces_indiv` keyword arguments)
        :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals (optional, `bpy.ops.transform.shrink_fatten` keyword arguments)
        :return: Result of the operator call.
        """

class extrude_manifold(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        MESH_OT_extrude_region: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude, dissolves edges whose faces form a flat surface and intersect new edges

        :param execution_context:
        :param undo:
        :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces (optional, `bpy.ops.mesh.extrude_region` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class extrude_region(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_normal_flip: bool | None = False,
        use_dissolve_ortho_edges: bool | None = False,
        mirror: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude region of faces

        :param execution_context:
        :param undo:
        :param use_normal_flip: Flip Normals, (optional)
        :param use_dissolve_ortho_edges: Dissolve Orthogonal Edges, (optional)
        :param mirror: Mirror Editing, (optional)
        :return: Result of the operator call.
        """

class extrude_region_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        MESH_OT_extrude_region: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude region and move result

        :param execution_context:
        :param undo:
        :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces (optional, `bpy.ops.mesh.extrude_region` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class extrude_region_shrink_fatten(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        MESH_OT_extrude_region: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_shrink_fatten: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude region together along local normals

        :param execution_context:
        :param undo:
        :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces (optional, `bpy.ops.mesh.extrude_region` keyword arguments)
        :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals (optional, `bpy.ops.transform.shrink_fatten` keyword arguments)
        :return: Result of the operator call.
        """

class extrude_repeat(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        steps: int | None = 10,
        offset: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
        scale_offset: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude selected vertices, edges or faces repeatedly

        :param execution_context:
        :param undo:
        :param steps: Steps, (in [0, 1000000], optional)
        :param offset: Offset, Offset vector (array of 3 items, in [-100000, 100000], optional)
        :param scale_offset: Scale Offset, (in [0, inf], optional)
        :return: Result of the operator call.
        """

class extrude_vertices_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        MESH_OT_extrude_verts_indiv: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude vertices and move result

        :param execution_context:
        :param undo:
        :param MESH_OT_extrude_verts_indiv: Extrude Only Vertices, Extrude individual vertices only (optional, `bpy.ops.mesh.extrude_verts_indiv` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class extrude_verts_indiv(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mirror: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude individual vertices only

        :param execution_context:
        :param undo:
        :param mirror: Mirror Editing, (optional)
        :return: Result of the operator call.
        """

class face_make_planar(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        factor: float | None = 1.0,
        repeat: int | None = 1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Flatten selected faces

        :param execution_context:
        :param undo:
        :param factor: Factor, (in [-10, 10], optional)
        :param repeat: Iterations, (in [1, 10000], optional)
        :return: Result of the operator call.
        """

class face_split_by_edges(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Weld loose edges into faces (splitting them into new faces)

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class faces_select_linked_flat(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        sharpness: float | None = 0.0174533,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select linked faces by angle

        :param execution_context:
        :param undo:
        :param sharpness: Sharpness, (in [0.000174533, 3.14159], optional)
        :return: Result of the operator call.
        """

class faces_shade_flat(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Display faces flat

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class faces_shade_smooth(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Display faces smooth (using vertex normals)

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class fill(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_beauty: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Fill a selected edge loop with faces

        :param execution_context:
        :param undo:
        :param use_beauty: Beauty, Use best triangulation division (optional)
        :return: Result of the operator call.
        """

class fill_grid(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        span: int | None = 1,
        offset: int | None = 0,
        use_interp_simple: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Fill grid from two loops

        :param execution_context:
        :param undo:
        :param span: Span, Number of grid columns (in [1, 1000], optional)
        :param offset: Offset, Vertex that is the corner of the grid (in [-1000, 1000], optional)
        :param use_interp_simple: Simple Blending, Use simple interpolation of grid vertices (optional)
        :return: Result of the operator call.
        """

class fill_holes(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        sides: int | None = 4,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Fill in holes (boundary edge loops)

        :param execution_context:
        :param undo:
        :param sides: Sides, Number of sides in hole required to fill (zero fills all holes) (in [0, 1000], optional)
        :return: Result of the operator call.
        """

class flip_normals(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        only_clnors: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Flip the direction of selected faces normals (and of their vertices)

        :param execution_context:
        :param undo:
        :param only_clnors: Custom Normals Only, Only flip the custom loop normals of the selected elements (optional)
        :return: Result of the operator call.
        """

class flip_quad_tessellation(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Flips the tessellation of selected quads

        :param execution_context:
        :param undo:
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
        """Hide (un)selected vertices, edges or faces

        :param execution_context:
        :param undo:
        :param unselected: Unselected, Hide unselected rather than selected (optional)
        :return: Result of the operator call.
        """

class inset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_boundary: bool | None = True,
        use_even_offset: bool | None = True,
        use_relative_offset: bool | None = False,
        use_edge_rail: bool | None = False,
        thickness: float | None = 0.0,
        depth: float | None = 0.0,
        use_outset: bool | None = False,
        use_select_inset: bool | None = False,
        use_individual: bool | None = False,
        use_interpolate: bool | None = True,
        release_confirm: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Inset new faces into selected faces

        :param execution_context:
        :param undo:
        :param use_boundary: Boundary, Inset face boundaries (optional)
        :param use_even_offset: Offset Even, Scale the offset to give more even thickness (optional)
        :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry (optional)
        :param use_edge_rail: Edge Rail, Inset the region along existing edges (optional)
        :param thickness: Thickness, (in [0, inf], optional)
        :param depth: Depth, (in [-inf, inf], optional)
        :param use_outset: Outset, Outset rather than inset (optional)
        :param use_select_inset: Select Outer, Select the new inset faces (optional)
        :param use_individual: Individual, Individual face inset (optional)
        :param use_interpolate: Interpolate, Blend face data across the inset (optional)
        :param release_confirm: Confirm on Release, (optional)
        :return: Result of the operator call.
        """

class intersect(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["SELECT", "SELECT_UNSELECT"] | None = "SELECT_UNSELECT",
        separate_mode: typing.Literal["ALL", "CUT", "NONE"] | None = "CUT",
        threshold: float | None = 1e-06,
        solver: typing.Literal["FLOAT", "EXACT"] | None = "EXACT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Cut an intersection into faces

                :param execution_context:
                :param undo:
                :param mode: Source, (optional)

        SELECT
        Self Intersect -- Self intersect selected faces.

        SELECT_UNSELECT
        Selected/Unselected -- Intersect selected with unselected faces.
                :param separate_mode: Separate Mode, (optional)

        ALL
        All -- Separate all geometry from intersections.

        CUT
        Cut -- Cut into geometry keeping each side separate (Selected/Unselected only).

        NONE
        Merge -- Merge all geometry from the intersection.
                :param threshold: Merge Threshold, (in [0, 0.01], optional)
                :param solver: Solver, Which Intersect solver to use (optional)

        FLOAT
        Float -- Simple solver with good performance, without support for overlapping geometry.

        EXACT
        Exact -- Slower solver with the best results for coplanar faces.
                :return: Result of the operator call.
        """

class intersect_boolean(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        operation: typing.Literal["INTERSECT", "UNION", "DIFFERENCE"]
        | None = "DIFFERENCE",
        use_swap: bool | None = False,
        use_self: bool | None = False,
        threshold: float | None = 1e-06,
        solver: typing.Literal["FLOAT", "EXACT"] | None = "EXACT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Cut solid geometry from selected to unselected

                :param execution_context:
                :param undo:
                :param operation: Boolean Operation, Which boolean operation to apply (optional)
                :param use_swap: Swap, Use with difference intersection to swap which side is kept (optional)
                :param use_self: Self Intersection, Do self-union or self-intersection (optional)
                :param threshold: Merge Threshold, (in [0, 0.01], optional)
                :param solver: Solver, Which Boolean solver to use (optional)

        FLOAT
        Float -- Faster solver, some limitations.

        EXACT
        Exact -- Exact solver, slower, handles more cases.
                :return: Result of the operator call.
        """

class knife_project(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        cut_through: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Use other objects outlines and boundaries to project knife cuts

        :param execution_context:
        :param undo:
        :param cut_through: Cut Through, Cut through all faces, not just visible ones (optional)
        :return: Result of the operator call.
        """

class knife_tool(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_occlude_geometry: bool | None = True,
        only_selected: bool | None = False,
        xray: bool | None = True,
        visible_measurements: typing.Literal["NONE", "BOTH", "DISTANCE", "ANGLE"]
        | None = "NONE",
        angle_snapping: typing.Literal["NONE", "SCREEN", "RELATIVE"] | None = "NONE",
        angle_snapping_increment: float | None = 0.523599,
        wait_for_input: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Cut new topology

                :param execution_context:
                :param undo:
                :param use_occlude_geometry: Occlude Geometry, Only cut the front most geometry (optional)
                :param only_selected: Only Selected, Only cut selected geometry (optional)
                :param xray: X-Ray, Show cuts hidden by geometry (optional)
                :param visible_measurements: Measurements, Visible distance and angle measurements (optional)

        NONE
        None -- Show no measurements.

        BOTH
        Both -- Show both distances and angles.

        DISTANCE
        Distance -- Show just distance measurements.

        ANGLE
        Angle -- Show just angle measurements.
                :param angle_snapping: Angle Snapping, Angle snapping mode (optional)

        NONE
        None -- No angle snapping.

        SCREEN
        Screen -- Screen space angle snapping.

        RELATIVE
        Relative -- Angle snapping relative to the previous cut edge.
                :param angle_snapping_increment: Angle Snap Increment, The angle snap increment used when in constrained angle mode (in [0, 3.14159], optional)
                :param wait_for_input: Wait for Input, (optional)
                :return: Result of the operator call.
        """

class loop_select(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        delimit_edge_loop: set[
            typing.Literal[bpy.stub_internal.rna_enums.MeshWalkDelimitEdgeLoopItems]
        ]
        | None = {"NGONS", "OUTER_CORNERS"},
        delimit_face_loop: set[
            typing.Literal[bpy.stub_internal.rna_enums.MeshWalkDelimitFaceLoopItems]
        ]
        | None = set(),
        extend: bool | None = False,
        deselect: bool | None = False,
        toggle: bool | None = False,
        object_index: int | None = -1,
        edge_index: int | None = -1,
        vert_index: int | None = -1,
        face_index: int | None = -1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select a loop of connected edges

        :param execution_context:
        :param undo:
        :param delimit_edge_loop: Delimit, Delimit edge loop selection (optional)
        :param delimit_face_loop: Face Loop Delimit, Delimit face loop selection (optional)
        :param extend: Extend Select, Extend the selection (optional)
        :param deselect: Deselect, Remove from the selection (optional)
        :param toggle: Toggle Select, Toggle the selection (optional)
        :param object_index: (in [-1, inf], optional)
        :param edge_index: (in [-1, inf], optional)
        :param vert_index: (in [-1, inf], optional)
        :param face_index: (in [-1, inf], optional)
        :return: Result of the operator call.
        """

class loop_to_region(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        select_bigger: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select region of faces inside of a selected loop of edges

        :param execution_context:
        :param undo:
        :param select_bigger: Select Bigger, Select bigger regions instead of smaller ones (optional)
        :return: Result of the operator call.
        """

class loopcut(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        number_cuts: int | None = 1,
        smoothness: float | None = 0.0,
        falloff: typing.Literal[
            bpy.stub_internal.rna_enums.ProportionalFalloffCurveOnlyItems
        ]
        | None = "INVERSE_SQUARE",
        object_index: int | None = -1,
        edge_index: int | None = -1,
        mesh_select_mode_init: collections.abc.Sequence[bool] | None = (
            False,
            False,
            False,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a new loop between existing loops

        :param execution_context:
        :param undo:
        :param number_cuts: Number of Cuts, (in [1, 1000000], optional)
        :param smoothness: Smoothness, Smoothness factor (in [-1000, 1000], optional)
        :param falloff: Falloff, Falloff type of the feather (optional)
        :param object_index: Object Index, (in [-1, inf], optional)
        :param edge_index: Edge Index, (in [-1, inf], optional)
        :param mesh_select_mode_init: (array of 3 items, optional)
        :return: Result of the operator call.
        """

class loopcut_slide(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        MESH_OT_loopcut: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_edge_slide: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Cut mesh loop and slide it

        :param execution_context:
        :param undo:
        :param MESH_OT_loopcut: Loop Cut, Add a new loop between existing loops (optional, `bpy.ops.mesh.loopcut` keyword arguments)
        :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh (optional, `bpy.ops.transform.edge_slide` keyword arguments)
        :return: Result of the operator call.
        """

class mark_freestyle_edge(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        clear: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """(Un)mark selected edges as Freestyle feature edges

        :param execution_context:
        :param undo:
        :param clear: Clear, (optional)
        :return: Result of the operator call.
        """

class mark_freestyle_face(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        clear: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """(Un)mark selected faces for exclusion from Freestyle feature edge detection

        :param execution_context:
        :param undo:
        :param clear: Clear, (optional)
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
        """(Un)mark selected edges as a seam

        :param execution_context:
        :param undo:
        :param clear: Clear, (optional)
        :return: Result of the operator call.
        """

class mark_sharp(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        clear: bool | None = False,
        use_verts: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """(Un)mark selected edges as sharp

        :param execution_context:
        :param undo:
        :param clear: Clear, (optional)
        :param use_verts: Vertices, Consider vertices instead of edges to select which edges to (un)tag as sharp (optional)
        :return: Result of the operator call.
        """

class merge(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["CENTER", "CURSOR", "COLLAPSE", "FIRST", "LAST"]
        | None = "CENTER",
        uvs: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Merge selected vertices

        :param execution_context:
        :param undo:
        :param type: Type, Merge method to use (optional)
        :param uvs: UVs, Move UVs according to merge (optional)
        :return: Result of the operator call.
        """

class merge_normals(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Merge custom normals of selected vertices

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class mod_weighted_strength(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        set: bool | None = False,
        face_strength: typing.Literal["WEAK", "MEDIUM", "STRONG"] | None = "MEDIUM",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set/Get strength of face (used in Weighted Normal modifier)

        :param execution_context:
        :param undo:
        :param set: Set Value, Set value of faces (optional)
        :param face_strength: Face Strength, Strength to use for assigning or selecting face influence for weighted normal modifier (optional)
        :return: Result of the operator call.
        """

class normals_make_consistent(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        inside: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make face and vertex normals point either outside or inside the mesh

        :param execution_context:
        :param undo:
        :param inside: Inside, (optional)
        :return: Result of the operator call.
        """

class normals_tools(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["COPY", "PASTE", "ADD", "MULTIPLY", "RESET"]
        | None = "COPY",
        absolute: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Custom normals tools using Normal Vector of UI

                :param execution_context:
                :param undo:
                :param mode: Mode, Mode of tools taking input from interface (optional)

        COPY
        Copy Normal -- Copy normal to the internal clipboard.

        PASTE
        Paste Normal -- Paste normal from the internal clipboard.

        ADD
        Add Normal -- Add normal vector with selection.

        MULTIPLY
        Multiply Normal -- Multiply normal vector with selection.

        RESET
        Reset Normal -- Reset the internal clipboard and/or normal of selected element.
                :param absolute: Absolute Coordinates, Copy Absolute coordinates of Normal vector (optional)
                :return: Result of the operator call.
        """

class offset_edge_loops(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_cap_endpoint: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create offset edge loop from the current selection

        :param execution_context:
        :param undo:
        :param use_cap_endpoint: Cap Endpoint, Extend loop around end-points (optional)
        :return: Result of the operator call.
        """

class offset_edge_loops_slide(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        MESH_OT_offset_edge_loops: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_edge_slide: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Offset edge loop slide

        :param execution_context:
        :param undo:
        :param MESH_OT_offset_edge_loops: Offset Edge Loop, Create offset edge loop from the current selection (optional, `bpy.ops.mesh.offset_edge_loops` keyword arguments)
        :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh (optional, `bpy.ops.transform.edge_slide` keyword arguments)
        :return: Result of the operator call.
        """

class point_normals(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["COORDINATES", "MOUSE"] | None = "COORDINATES",
        invert: bool | None = False,
        align: bool | None = False,
        target_location: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
        spherize: bool | None = False,
        spherize_strength: float | None = 0.1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Point selected custom normals to specified Target

                :param execution_context:
                :param undo:
                :param mode: Mode, How to define coordinates to point custom normals to (optional)

        COORDINATES
        Coordinates -- Use static coordinates (defined by various means).

        MOUSE
        Mouse -- Follow mouse cursor.
                :param invert: Invert, Invert affected normals (optional)
                :param align: Align, Make all affected normals parallel (optional)
                :param target_location: Target, Target location to which normals will point (array of 3 items, in [-inf, inf], optional)
                :param spherize: Spherize, Interpolate between original and new normals (optional)
                :param spherize_strength: Spherize Strength, Ratio of spherized normal to original normal (in [0, 1], optional)
                :return: Result of the operator call.
        """

class poke(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        offset: float | None = 0.0,
        use_relative_offset: bool | None = False,
        center_mode: typing.Literal["MEDIAN_WEIGHTED", "MEDIAN", "BOUNDS"]
        | None = "MEDIAN_WEIGHTED",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Split a face into a fan

                :param execution_context:
                :param undo:
                :param offset: Poke Offset, Poke Offset (in [-1000, 1000], optional)
                :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry (optional)
                :param center_mode: Poke Center, Poke face center calculation (optional)

        MEDIAN_WEIGHTED
        Weighted Median -- Weighted median face center.

        MEDIAN
        Median -- Median face center.

        BOUNDS
        Bounds -- Face bounds center.
                :return: Result of the operator call.
        """

class polybuild_delete_at_cursor(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mirror: bool | None = False,
        use_proportional_edit: bool | None = False,
        proportional_edit_falloff: typing.Literal[
            bpy.stub_internal.rna_enums.ProportionalFalloffItems
        ]
        | None = "SMOOTH",
        proportional_size: float | None = 1.0,
        use_proportional_connected: bool | None = False,
        use_proportional_projected: bool | None = False,
        release_confirm: bool | None = False,
        use_accurate: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param mirror: Mirror Editing, (optional)
        :param use_proportional_edit: Proportional Editing, (optional)
        :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode (optional)
        :param proportional_size: Proportional Size, (in [1e-06, inf], optional)
        :param use_proportional_connected: Connected, (optional)
        :param use_proportional_projected: Projected (2D), (optional)
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button (optional)
        :param use_accurate: Accurate, Use accurate transformation (optional)
        :return: Result of the operator call.
        """

class polybuild_dissolve_at_cursor(bpy.ops._BPyOpsSubModOp):
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

class polybuild_extrude_at_cursor_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        MESH_OT_polybuild_transform_at_cursor: dict[str, typing.Any] | None = {},
        MESH_OT_extrude_edges_indiv: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor, (optional, `bpy.ops.mesh.polybuild_transform_at_cursor` keyword arguments)
        :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only (optional, `bpy.ops.mesh.extrude_edges_indiv` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class polybuild_face_at_cursor(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        create_quads: bool | None = True,
        mirror: bool | None = False,
        use_proportional_edit: bool | None = False,
        proportional_edit_falloff: typing.Literal[
            bpy.stub_internal.rna_enums.ProportionalFalloffItems
        ]
        | None = "SMOOTH",
        proportional_size: float | None = 1.0,
        use_proportional_connected: bool | None = False,
        use_proportional_projected: bool | None = False,
        release_confirm: bool | None = False,
        use_accurate: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param create_quads: Create Quads, Automatically split edges in triangles to maintain quad topology (optional)
        :param mirror: Mirror Editing, (optional)
        :param use_proportional_edit: Proportional Editing, (optional)
        :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode (optional)
        :param proportional_size: Proportional Size, (in [1e-06, inf], optional)
        :param use_proportional_connected: Connected, (optional)
        :param use_proportional_projected: Projected (2D), (optional)
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button (optional)
        :param use_accurate: Accurate, Use accurate transformation (optional)
        :return: Result of the operator call.
        """

class polybuild_face_at_cursor_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        MESH_OT_polybuild_face_at_cursor: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param MESH_OT_polybuild_face_at_cursor: Poly Build Face at Cursor, (optional, `bpy.ops.mesh.polybuild_face_at_cursor` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class polybuild_split_at_cursor(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mirror: bool | None = False,
        use_proportional_edit: bool | None = False,
        proportional_edit_falloff: typing.Literal[
            bpy.stub_internal.rna_enums.ProportionalFalloffItems
        ]
        | None = "SMOOTH",
        proportional_size: float | None = 1.0,
        use_proportional_connected: bool | None = False,
        use_proportional_projected: bool | None = False,
        release_confirm: bool | None = False,
        use_accurate: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param mirror: Mirror Editing, (optional)
        :param use_proportional_edit: Proportional Editing, (optional)
        :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode (optional)
        :param proportional_size: Proportional Size, (in [1e-06, inf], optional)
        :param use_proportional_connected: Connected, (optional)
        :param use_proportional_projected: Projected (2D), (optional)
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button (optional)
        :param use_accurate: Accurate, Use accurate transformation (optional)
        :return: Result of the operator call.
        """

class polybuild_split_at_cursor_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        MESH_OT_polybuild_split_at_cursor: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param MESH_OT_polybuild_split_at_cursor: Poly Build Split at Cursor, (optional, `bpy.ops.mesh.polybuild_split_at_cursor` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class polybuild_transform_at_cursor(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mirror: bool | None = False,
        use_proportional_edit: bool | None = False,
        proportional_edit_falloff: typing.Literal[
            bpy.stub_internal.rna_enums.ProportionalFalloffItems
        ]
        | None = "SMOOTH",
        proportional_size: float | None = 1.0,
        use_proportional_connected: bool | None = False,
        use_proportional_projected: bool | None = False,
        release_confirm: bool | None = False,
        use_accurate: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param mirror: Mirror Editing, (optional)
        :param use_proportional_edit: Proportional Editing, (optional)
        :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode (optional)
        :param proportional_size: Proportional Size, (in [1e-06, inf], optional)
        :param use_proportional_connected: Connected, (optional)
        :param use_proportional_projected: Projected (2D), (optional)
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button (optional)
        :param use_accurate: Accurate, Use accurate transformation (optional)
        :return: Result of the operator call.
        """

class polybuild_transform_at_cursor_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        MESH_OT_polybuild_transform_at_cursor: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor, (optional, `bpy.ops.mesh.polybuild_transform_at_cursor` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class primitive_circle_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        vertices: int | None = 32,
        radius: float | None = 1.0,
        fill_type: typing.Literal["NOTHING", "NGON", "TRIFAN"] | None = "NOTHING",
        calc_uvs: bool | None = True,
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
        """Construct a circle mesh

                :param execution_context:
                :param undo:
                :param vertices: Vertices, (in [3, 10000000], optional)
                :param radius: Radius, (in [0, inf], optional)
                :param fill_type: Fill Type, (optional)

        NOTHING
        Nothing -- Dont fill at all.

        NGON
        N-Gon -- Use n-gons.

        TRIFAN
        Triangle Fan -- Use triangle fans.
                :param calc_uvs: Generate UVs, Generate a default UV map (optional)
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

class primitive_cone_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        vertices: int | None = 32,
        radius1: float | None = 1.0,
        radius2: float | None = 0.0,
        depth: float | None = 2.0,
        end_fill_type: typing.Literal["NOTHING", "NGON", "TRIFAN"] | None = "NGON",
        calc_uvs: bool | None = True,
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
        """Construct a conic mesh

                :param execution_context:
                :param undo:
                :param vertices: Vertices, (in [3, 10000000], optional)
                :param radius1: Radius 1, (in [0, inf], optional)
                :param radius2: Radius 2, (in [0, inf], optional)
                :param depth: Depth, (in [0, inf], optional)
                :param end_fill_type: Base Fill Type, (optional)

        NOTHING
        Nothing -- Dont fill at all.

        NGON
        N-Gon -- Use n-gons.

        TRIFAN
        Triangle Fan -- Use triangle fans.
                :param calc_uvs: Generate UVs, Generate a default UV map (optional)
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

class primitive_cube_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        size: float | None = 2.0,
        calc_uvs: bool | None = True,
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
        """Construct a cube mesh that consists of six square faces

                :param execution_context:
                :param undo:
                :param size: Size, (in [0, inf], optional)
                :param calc_uvs: Generate UVs, Generate a default UV map (optional)
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

class primitive_cube_add_gizmo(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        calc_uvs: bool | None = True,
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
        matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
        | mathutils.Matrix
        | None = (
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Construct a cube mesh

                :param execution_context:
                :param undo:
                :param calc_uvs: Generate UVs, Generate a default UV map (optional)
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
                :param matrix: Matrix, (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class primitive_cylinder_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        vertices: int | None = 32,
        radius: float | None = 1.0,
        depth: float | None = 2.0,
        end_fill_type: typing.Literal["NOTHING", "NGON", "TRIFAN"] | None = "NGON",
        calc_uvs: bool | None = True,
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
        """Construct a cylinder mesh

                :param execution_context:
                :param undo:
                :param vertices: Vertices, (in [3, 10000000], optional)
                :param radius: Radius, (in [0, inf], optional)
                :param depth: Depth, (in [0, inf], optional)
                :param end_fill_type: Cap Fill Type, (optional)

        NOTHING
        Nothing -- Dont fill at all.

        NGON
        N-Gon -- Use n-gons.

        TRIFAN
        Triangle Fan -- Use triangle fans.
                :param calc_uvs: Generate UVs, Generate a default UV map (optional)
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

class primitive_grid_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        x_subdivisions: int | None = 10,
        y_subdivisions: int | None = 10,
        size: float | None = 2.0,
        calc_uvs: bool | None = True,
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
        """Construct a subdivided plane mesh

                :param execution_context:
                :param undo:
                :param x_subdivisions: X Subdivisions, (in [1, 10000000], optional)
                :param y_subdivisions: Y Subdivisions, (in [1, 10000000], optional)
                :param size: Size, (in [0, inf], optional)
                :param calc_uvs: Generate UVs, Generate a default UV map (optional)
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

class primitive_ico_sphere_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        subdivisions: int | None = 2,
        radius: float | None = 1.0,
        calc_uvs: bool | None = True,
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
        """Construct a spherical mesh that consists of equally sized triangles

                :param execution_context:
                :param undo:
                :param subdivisions: Subdivisions, (in [1, 10], optional)
                :param radius: Radius, (in [0, inf], optional)
                :param calc_uvs: Generate UVs, Generate a default UV map (optional)
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

class primitive_monkey_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        size: float | None = 2.0,
        calc_uvs: bool | None = True,
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
        """Construct a Suzanne mesh

                :param execution_context:
                :param undo:
                :param size: Size, (in [0, inf], optional)
                :param calc_uvs: Generate UVs, Generate a default UV map (optional)
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

class primitive_plane_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        size: float | None = 2.0,
        calc_uvs: bool | None = True,
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
        """Construct a filled planar mesh with 4 vertices

                :param execution_context:
                :param undo:
                :param size: Size, (in [0, inf], optional)
                :param calc_uvs: Generate UVs, Generate a default UV map (optional)
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

class primitive_torus_add(bpy.ops._BPyOpsSubModOp):
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
        major_segments: int | None = 48,
        minor_segments: int | None = 12,
        mode: typing.Literal["MAJOR_MINOR", "EXT_INT"] | None = "MAJOR_MINOR",
        major_radius: float | None = 1.0,
        minor_radius: float | None = 0.25,
        abso_major_rad: float | None = 1.25,
        abso_minor_rad: float | None = 0.75,
        generate_uvs: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Construct a torus mesh

                :param execution_context:
                :param undo:
                :param align: Align, (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, (array of 3 items, in [-inf, inf], optional)
                :param major_segments: Major Segments, Number of segments for the main ring of the torus (in [3, 256], optional)
                :param minor_segments: Minor Segments, Number of segments for the minor ring of the torus (in [3, 256], optional)
                :param mode: Dimensions Mode, (optional)

        MAJOR_MINOR
        Major/Minor -- Use the major/minor radii for torus dimensions.

        EXT_INT
        Exterior/Interior -- Use the exterior/interior radii for torus dimensions.
                :param major_radius: Major Radius, Radius from the origin to the center of the cross sections (in [0, 10000], optional)
                :param minor_radius: Minor Radius, Radius of the toruss cross section (in [0, 10000], optional)
                :param abso_major_rad: Exterior Radius, Total Exterior Radius of the torus (in [0, 10000], optional)
                :param abso_minor_rad: Interior Radius, Total Interior Radius of the torus (in [0, 10000], optional)
                :param generate_uvs: Generate UVs, Generate a default UV map (optional)
                :return: Result of the operator call.
        """

class primitive_uv_sphere_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        segments: int | None = 32,
        ring_count: int | None = 16,
        radius: float | None = 1.0,
        calc_uvs: bool | None = True,
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
        """Construct a spherical mesh with quad faces, except for triangle faces at the top and bottom

                :param execution_context:
                :param undo:
                :param segments: Segments, (in [3, 100000], optional)
                :param ring_count: Rings, (in [3, 100000], optional)
                :param radius: Radius, (in [0, inf], optional)
                :param calc_uvs: Generate UVs, Generate a default UV map (optional)
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

class quads_convert_to_tris(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        quad_method: typing.Literal[
            bpy.stub_internal.rna_enums.ModifierTriangulateQuadMethodItems
        ]
        | None = "BEAUTY",
        ngon_method: typing.Literal[
            bpy.stub_internal.rna_enums.ModifierTriangulateNgonMethodItems
        ]
        | None = "BEAUTY",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Triangulate selected faces

        :param execution_context:
        :param undo:
        :param quad_method: Quad Method, Method for splitting the quads into triangles (optional)
        :param ngon_method: N-gon Method, Method for splitting the n-gons into triangles (optional)
        :return: Result of the operator call.
        """

class region_to_loop(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select boundary edges around the selected faces

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class remove_doubles(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        threshold: float | None = 0.0001,
        use_centroid: bool | None = True,
        use_unselected: bool | None = False,
        use_sharp_edge_from_normals: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Merge vertices based on their proximity

        :param execution_context:
        :param undo:
        :param threshold: Merge Distance, Maximum distance between elements to merge (in [1e-06, 50], optional)
        :param use_centroid: Centroid Merge, Move vertices to the centroid of the duplicate cluster, otherwise the vertex closest to the centroid is used. (optional)
        :param use_unselected: Unselected, Merge selected to other unselected vertices (optional)
        :param use_sharp_edge_from_normals: Sharp Edges, Calculate sharp edges using custom normal data (when available) (optional)
        :return: Result of the operator call.
        """

class reorder_vertices_spatial(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reorder mesh faces and vertices based on their spatial position for better BVH building and sculpting performance.

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
        """Reveal all hidden vertices, edges and faces

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
        use_proportional_edit: bool | None = False,
        proportional_edit_falloff: typing.Literal[
            bpy.stub_internal.rna_enums.ProportionalFalloffItems
        ]
        | None = "SMOOTH",
        proportional_size: float | None = 1.0,
        use_proportional_connected: bool | None = False,
        use_proportional_projected: bool | None = False,
        release_confirm: bool | None = False,
        use_accurate: bool | None = False,
        use_fill: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Disconnect vertices or edges from connected geometry

        :param execution_context:
        :param undo:
        :param mirror: Mirror Editing, (optional)
        :param use_proportional_edit: Proportional Editing, (optional)
        :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode (optional)
        :param proportional_size: Proportional Size, (in [1e-06, inf], optional)
        :param use_proportional_connected: Connected, (optional)
        :param use_proportional_projected: Projected (2D), (optional)
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button (optional)
        :param use_accurate: Accurate, Use accurate transformation (optional)
        :param use_fill: Fill, Fill the ripped region (optional)
        :return: Result of the operator call.
        """

class rip_edge(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        location: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
        direction: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extend vertices along the edge closest to the cursor

        :param execution_context:
        :param undo:
        :param location: Location, World-space ray origin for extending vertices (array of 3 items, in [-inf, inf], optional)
        :param direction: Direction, World-space direction vector for extending vertices (array of 3 items, in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class rip_edge_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        MESH_OT_rip_edge: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extend vertices and move the result

        :param execution_context:
        :param undo:
        :param MESH_OT_rip_edge: Extend Vertices, Extend vertices along the edge closest to the cursor (optional, `bpy.ops.mesh.rip_edge` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class rip_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        MESH_OT_rip: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Rip polygons and move the result

        :param execution_context:
        :param undo:
        :param MESH_OT_rip: Rip, Disconnect vertices or edges from connected geometry (optional, `bpy.ops.mesh.rip` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class screw(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        steps: int | None = 9,
        turns: int | None = 1,
        center: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
        axis: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude selected vertices in screw-shaped rotation around the cursor in indicated viewport

        :param execution_context:
        :param undo:
        :param steps: Steps, Steps (in [1, 100000], optional)
        :param turns: Turns, Turns (in [1, 100000], optional)
        :param center: Center, Center in global view space (array of 3 items, in [-inf, inf], optional)
        :param axis: Axis, Axis in global view space (array of 3 items, in [-1, 1], optional)
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
        """(De)select all vertices, edges or faces

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

class select_axis(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        orientation: typing.Literal[
            bpy.stub_internal.rna_enums.TransformOrientationItems
        ]
        | None = "LOCAL",
        sign: typing.Literal["POS", "NEG", "ALIGN"] | None = "POS",
        axis: typing.Literal[bpy.stub_internal.rna_enums.AxisXyzItems] | None = "X",
        threshold: float | None = 0.0001,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all data in the mesh on a single axis

        :param execution_context:
        :param undo:
        :param orientation: Axis Mode, Axis orientation (optional)
        :param sign: Axis Sign, Side to select (optional)
        :param axis: Axis, Select the axis to compare each vertex on (optional)
        :param threshold: Threshold, (in [1e-06, 50], optional)
        :return: Result of the operator call.
        """

class select_by_attribute(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select elements based on the active boolean attribute

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_by_pole_count(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        pole_count: int | None = 4,
        type: typing.Literal["LESS", "EQUAL", "GREATER", "NOTEQUAL"]
        | None = "NOTEQUAL",
        extend: bool | None = False,
        exclude_nonmanifold: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select vertices at poles by the number of connected edges. In edge and face mode the geometry connected to the vertices is selected

        :param execution_context:
        :param undo:
        :param pole_count: Pole Count, (in [0, inf], optional)
        :param type: Type, Type of comparison to make (optional)
        :param extend: Extend, Extend the selection (optional)
        :param exclude_nonmanifold: Exclude Non Manifold, Exclude non-manifold poles (optional)
        :return: Result of the operator call.
        """

class select_edge_loop_multi(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        delimit_edge_loop: set[
            typing.Literal[bpy.stub_internal.rna_enums.MeshWalkDelimitEdgeLoopItems]
        ]
        | None = {"NGONS", "OUTER_CORNERS"},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select loops of connected edges from each selected edge

        :param execution_context:
        :param undo:
        :param delimit_edge_loop: Delimit, Delimit edge loop selection (optional)
        :return: Result of the operator call.
        """

class select_edge_ring_multi(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        delimit_edge_ring: set[
            typing.Literal[bpy.stub_internal.rna_enums.MeshWalkDelimitEdgeRingItems]
        ]
        | None = {"NGONS"},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select rings of connected edges from each selected edge

        :param execution_context:
        :param undo:
        :param delimit_edge_ring: Edge Ring Delimit, Delimit edge ring selection (optional)
        :return: Result of the operator call.
        """

class select_face_by_sides(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        number: int | None = 4,
        type: typing.Literal["LESS", "EQUAL", "GREATER", "NOTEQUAL"] | None = "EQUAL",
        extend: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select vertices or faces by the number of face sides

        :param execution_context:
        :param undo:
        :param number: Number of Vertices, (in [3, inf], optional)
        :param type: Type, Type of comparison to make (optional)
        :param extend: Extend, Extend the selection (optional)
        :return: Result of the operator call.
        """

class select_interior_faces(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select faces where all edges have more than 2 face users

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_less(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_face_step: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Deselect vertices, edges or faces at the boundary of each selection region

        :param execution_context:
        :param undo:
        :param use_face_step: Face Step, Connected faces (instead of edges) (optional)
        :return: Result of the operator call.
        """

class select_linked(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        delimit: set[typing.Literal[bpy.stub_internal.rna_enums.MeshDelimitModeItems]]
        | None = {"SEAM"},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all vertices connected to the current selection

        :param execution_context:
        :param undo:
        :param delimit: Delimit, Delimit selected region (optional)
        :return: Result of the operator call.
        """

class select_linked_pick(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        deselect: bool | None = False,
        delimit: set[typing.Literal[bpy.stub_internal.rna_enums.MeshDelimitModeItems]]
        | None = {"SEAM"},
        object_index: int | None = -1,
        index: int | None = -1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """(De)select all vertices linked to the edge under the mouse cursor

        :param execution_context:
        :param undo:
        :param deselect: Deselect, (optional)
        :param delimit: Delimit, Delimit selected region (optional)
        :param object_index: (in [-1, inf], optional)
        :param index: (in [-1, inf], optional)
        :return: Result of the operator call.
        """

class select_loose(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select loose geometry based on the selection mode

        :param execution_context:
        :param undo:
        :param extend: Extend, Extend the selection (optional)
        :return: Result of the operator call.
        """

class select_mirror(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        axis: set[typing.Literal[bpy.stub_internal.rna_enums.AxisFlagXyzItems]]
        | None = {"X"},
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select mesh items at mirrored locations

        :param execution_context:
        :param undo:
        :param axis: Axis, (optional)
        :param extend: Extend, Extend the existing selection (optional)
        :return: Result of the operator call.
        """

class select_mode(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_extend: bool | None = False,
        use_expand: bool | None = False,
        type: typing.Literal[bpy.stub_internal.rna_enums.MeshSelectModeItems]
        | None = "VERT",
        action: typing.Literal["DISABLE", "ENABLE", "TOGGLE"] | None = "TOGGLE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change selection mode

                :param execution_context:
                :param undo:
                :param use_extend: Extend, (optional)
                :param use_expand: Expand, (optional)
                :param type: Type, (optional)
                :param action: Action, Selection action to execute (optional)

        DISABLE
        Disable -- Disable the selection mode.

        ENABLE
        Enable -- Enable the selection mode.

        TOGGLE
        Toggle -- Toggle the selection mode.
                :return: Result of the operator call.
        """

class select_more(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_face_step: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select more vertices, edges or faces connected to initial selection

        :param execution_context:
        :param undo:
        :param use_face_step: Face Step, Connected faces (instead of edges) (optional)
        :return: Result of the operator call.
        """

class select_next_item(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select the next element (using selection order)

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_non_manifold(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        extend: bool | None = True,
        use_wire: bool | None = True,
        use_boundary: bool | None = True,
        use_multi_face: bool | None = True,
        use_non_contiguous: bool | None = True,
        use_verts: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all non-manifold vertices or edges

        :param execution_context:
        :param undo:
        :param extend: Extend, Extend the selection (optional)
        :param use_wire: Wire, Wire edges (optional)
        :param use_boundary: Boundaries, Boundary edges (optional)
        :param use_multi_face: Multiple Faces, Edges shared by more than two faces (optional)
        :param use_non_contiguous: Non Contiguous, Edges between faces pointing in alternate directions (optional)
        :param use_verts: Vertices, Vertices connecting multiple face regions (optional)
        :return: Result of the operator call.
        """

class select_nth(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        skip: int | None = 1,
        nth: int | None = 1,
        offset: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Deselect every Nth element starting from the active vertex, edge or face

        :param execution_context:
        :param undo:
        :param skip: Deselected, Number of deselected elements in the repetitive sequence (in [1, inf], optional)
        :param nth: Selected, Number of selected elements in the repetitive sequence (in [1, inf], optional)
        :param offset: Offset, Offset from the starting point (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class select_prev_item(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select the previous element (using selection order)

        :param execution_context:
        :param undo:
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
        """Randomly select vertices

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

class select_similar(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            "VERT_NORMAL",
            "VERT_FACES",
            "VERT_GROUPS",
            "VERT_EDGES",
            "VERT_CREASE",
            "EDGE_LENGTH",
            "EDGE_DIR",
            "EDGE_FACES",
            "EDGE_FACE_ANGLE",
            "EDGE_CREASE",
            "EDGE_BEVEL",
            "EDGE_SEAM",
            "EDGE_SHARP",
            "EDGE_FREESTYLE",
            "FACE_MATERIAL",
            "FACE_AREA",
            "FACE_SIDES",
            "FACE_PERIMETER",
            "FACE_NORMAL",
            "FACE_COPLANAR",
            "FACE_SMOOTH",
            "FACE_FREESTYLE",
        ]
        | None = "VERT_NORMAL",
        compare: typing.Literal["EQUAL", "GREATER", "LESS"] | None = "EQUAL",
        threshold: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select similar vertices, edges or faces by property types

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :param compare: Compare, (optional)
        :param threshold: Threshold, (in [0, 100000], optional)
        :return: Result of the operator call.
        """

class select_similar_region(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select similar face regions to the current selection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_ungrouped(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select vertices without a group

        :param execution_context:
        :param undo:
        :param extend: Extend, Extend the selection (optional)
        :return: Result of the operator call.
        """

class separate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["SELECTED", "MATERIAL", "LOOSE"] | None = "SELECTED",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Separate selected geometry into a new mesh

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class set_normals_from_faces(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        keep_sharp: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the custom normals from the selected faces ones

        :param execution_context:
        :param undo:
        :param keep_sharp: Keep Sharp Edges, Do not set sharp edges to face (optional)
        :return: Result of the operator call.
        """

class set_sharpness_by_angle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        angle: float | None = 0.523599,
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set edge sharpness based on the angle between neighboring faces

        :param execution_context:
        :param undo:
        :param angle: Angle, (in [0.000174533, 3.14159], optional)
        :param extend: Extend, Add new sharp edges without clearing existing sharp edges (optional)
        :return: Result of the operator call.
        """

class shape_propagate_to_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Apply selected vertex locations to all other shape keys

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class shortest_path_pick(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        edge_mode: typing.Literal[
            "SELECT", "SEAM", "SHARP", "CREASE", "BEVEL", "FREESTYLE"
        ]
        | None = "SELECT",
        use_face_step: bool | None = False,
        use_topology_distance: bool | None = False,
        use_fill: bool | None = False,
        skip: int | None = 0,
        nth: int | None = 1,
        offset: int | None = 0,
        index: int | None = -1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select shortest path between two selections

        :param execution_context:
        :param undo:
        :param edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path (optional)
        :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings) (optional)
        :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance (optional)
        :param use_fill: Fill Region, Select all paths between the source/destination elements (optional)
        :param skip: Deselected, Number of deselected elements in the repetitive sequence (in [0, inf], optional)
        :param nth: Selected, Number of selected elements in the repetitive sequence (in [1, inf], optional)
        :param offset: Offset, Offset from the starting point (in [-inf, inf], optional)
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
        edge_mode: typing.Literal[
            "SELECT", "SEAM", "SHARP", "CREASE", "BEVEL", "FREESTYLE"
        ]
        | None = "SELECT",
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
        :param edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path (optional)
        :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings) (optional)
        :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance (optional)
        :param use_fill: Fill Region, Select all paths between the source/destination elements (optional)
        :param skip: Deselected, Number of deselected elements in the repetitive sequence (in [0, inf], optional)
        :param nth: Selected, Number of selected elements in the repetitive sequence (in [1, inf], optional)
        :param offset: Offset, Offset from the starting point (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class smooth_normals(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        factor: float | None = 0.5,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Smooth custom normals based on adjacent vertex normals

        :param execution_context:
        :param undo:
        :param factor: Factor, Specifies weight of smooth vs original normal (in [0, 1], optional)
        :return: Result of the operator call.
        """

class solidify(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        thickness: float | None = 0.01,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a solid skin by extruding, compensating for sharp angles

        :param execution_context:
        :param undo:
        :param thickness: Thickness, (in [-10000, 10000], optional)
        :return: Result of the operator call.
        """

class sort_elements(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            "VIEW_ZAXIS",
            "VIEW_XAXIS",
            "CURSOR_DISTANCE",
            "MATERIAL",
            "SELECTED",
            "RANDOMIZE",
            "REVERSE",
        ]
        | None = "VIEW_ZAXIS",
        elements: set[typing.Literal["VERT", "EDGE", "FACE"]] | None = {"VERT"},
        reverse: bool | None = False,
        seed: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """The order of selected vertices/edges/faces is modified, based on a given method

                :param execution_context:
                :param undo:
                :param type: Type, Type of reordering operation to apply (optional)

        VIEW_ZAXIS
        View Z Axis -- Sort selected elements from farthest to nearest one in current view.

        VIEW_XAXIS
        View X Axis -- Sort selected elements from left to right one in current view.

        CURSOR_DISTANCE
        Cursor Distance -- Sort selected elements from nearest to farthest from 3D cursor.

        MATERIAL
        Material -- Sort selected faces from smallest to greatest material index.

        SELECTED
        Selected -- Move all selected elements in first places, preserving their relative order.
        Warning: This will affect unselected elements indices as well.

        RANDOMIZE
        Randomize -- Randomize order of selected elements.

        REVERSE
        Reverse -- Reverse current order of selected elements.
                :param elements: Elements, Which elements to affect (vertices, edges and/or faces) (optional)
                :param reverse: Reverse, Reverse the sorting effect (optional)
                :param seed: Seed, Seed for random-based operations (in [0, inf], optional)
                :return: Result of the operator call.
        """

class spin(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        steps: int | None = 12,
        dupli: bool | None = False,
        angle: float | None = 1.5708,
        use_auto_merge: bool | None = True,
        use_normal_flip: bool | None = False,
        center: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
        axis: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Extrude selected vertices in a circle around the cursor in indicated viewport

        :param execution_context:
        :param undo:
        :param steps: Steps, Steps (in [0, 1000000], optional)
        :param dupli: Use Duplicates, (optional)
        :param angle: Angle, Rotation for each step (in [-inf, inf], optional)
        :param use_auto_merge: Auto Merge, Merge first/last when the angle is a full revolution (optional)
        :param use_normal_flip: Flip Normals, (optional)
        :param center: Center, Center in global view space (array of 3 items, in [-inf, inf], optional)
        :param axis: Axis, Axis in global view space (array of 3 items, in [-1, 1], optional)
        :return: Result of the operator call.
        """

class split(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Split off selected geometry from connected unselected geometry

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class split_normals(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Split custom normals of selected vertices

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class subdivide(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        number_cuts: int | None = 1,
        smoothness: float | None = 0.0,
        ngon: bool | None = True,
        quadcorner: typing.Literal["INNERVERT", "PATH", "STRAIGHT_CUT", "FAN"]
        | None = "STRAIGHT_CUT",
        fractal: float | None = 0.0,
        fractal_along_normal: float | None = 0.0,
        seed: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Subdivide selected edges

        :param execution_context:
        :param undo:
        :param number_cuts: Number of Cuts, (in [1, 100], optional)
        :param smoothness: Smoothness, Smoothness factor (in [0, 1000], optional)
        :param ngon: Create N-Gons, When disabled, newly created faces are limited to 3 and 4 sided faces (optional)
        :param quadcorner: Quad Corner Type, How to subdivide quad corners (anything other than Straight Cut will prevent n-gons) (optional)
        :param fractal: Fractal, Fractal randomness factor (in [0, 1e+06], optional)
        :param fractal_along_normal: Along Normal, Apply fractal displacement along normal only (in [0, 1], optional)
        :param seed: Random Seed, Seed for the random number generator (in [0, inf], optional)
        :return: Result of the operator call.
        """

class subdivide_edgering(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        number_cuts: int | None = 10,
        interpolation: typing.Literal["LINEAR", "PATH", "SURFACE"] | None = "PATH",
        smoothness: float | None = 1.0,
        profile_shape_factor: float | None = 0.0,
        profile_shape: typing.Literal[
            bpy.stub_internal.rna_enums.ProportionalFalloffCurveOnlyItems
        ]
        | None = "SMOOTH",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Subdivide perpendicular edges to the selected edge-ring

        :param execution_context:
        :param undo:
        :param number_cuts: Number of Cuts, (in [0, 1000], optional)
        :param interpolation: Interpolation, Interpolation method (optional)
        :param smoothness: Smoothness, Smoothness factor (in [0, 1000], optional)
        :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded (in [-1000, 1000], optional)
        :param profile_shape: Profile Shape, Shape of the profile (optional)
        :return: Result of the operator call.
        """

class symmetrize(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal[bpy.stub_internal.rna_enums.SymmetrizeDirectionItems]
        | None = "NEGATIVE_X",
        threshold: float | None = 0.0001,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Enforce symmetry (both form and topological) across an axis

        :param execution_context:
        :param undo:
        :param direction: Direction, Which sides to copy from and to (optional)
        :param threshold: Threshold, Limit for snap middle vertices to the axis center (in [0, 10], optional)
        :return: Result of the operator call.
        """

class symmetry_snap(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal[bpy.stub_internal.rna_enums.SymmetrizeDirectionItems]
        | None = "NEGATIVE_X",
        threshold: float | None = 0.05,
        factor: float | None = 0.5,
        use_center: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Snap vertex pairs to their mirrored locations

        :param execution_context:
        :param undo:
        :param direction: Direction, Which sides to copy from and to (optional)
        :param threshold: Threshold, Distance within which matching vertices are searched (in [0, 10], optional)
        :param factor: Factor, Mix factor of the locations of the vertices (in [0, 1], optional)
        :param use_center: Center, Snap middle vertices to the axis center (optional)
        :return: Result of the operator call.
        """

class tris_convert_to_quads(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        face_threshold: float | None = 0.698132,
        shape_threshold: float | None = 0.698132,
        topology_influence: float | None = 0.0,
        uvs: bool | None = False,
        vcols: bool | None = False,
        seam: bool | None = False,
        sharp: bool | None = False,
        materials: bool | None = False,
        deselect_joined: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Merge triangles into four sided polygons where possible

        :param execution_context:
        :param undo:
        :param face_threshold: Max Face Angle, Face angle limit (in [0, 3.14159], optional)
        :param shape_threshold: Max Shape Angle, Shape angle limit (in [0, 3.14159], optional)
        :param topology_influence: Topology Influence, How much to prioritize regular grids of quads as well as quads that touch existing quads (in [0, 2], optional)
        :param uvs: Compare UVs, (optional)
        :param vcols: Compare Color Attributes, (optional)
        :param seam: Compare Seam, (optional)
        :param sharp: Compare Sharp, (optional)
        :param materials: Compare Materials, (optional)
        :param deselect_joined: Deselect Joined, Only select remaining triangles that were not merged (optional)
        :return: Result of the operator call.
        """

class unsubdivide(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        iterations: int | None = 2,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Un-subdivide selected edges and faces

        :param execution_context:
        :param undo:
        :param iterations: Iterations, Number of times to un-subdivide (in [1, 1000], optional)
        :return: Result of the operator call.
        """

class uv_texture_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add UV map

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class uv_texture_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove UV map

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class uvs_reverse(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Flip direction of UV coordinates inside faces

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class uvs_rotate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_ccw: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Rotate UV coordinates inside faces

        :param execution_context:
        :param undo:
        :param use_ccw: Counter Clockwise, (optional)
        :return: Result of the operator call.
        """

class vert_connect(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Connect selected vertices of faces, splitting the face

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vert_connect_concave(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Split concave faces by connecting vertices to make them convex

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vert_connect_nonplanar(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        angle_limit: float | None = 0.0872665,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Split non-planar faces that exceed the angle threshold

        :param execution_context:
        :param undo:
        :param angle_limit: Max Angle, Angle limit (in [0, 3.14159], optional)
        :return: Result of the operator call.
        """

class vert_connect_path(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Connect vertices by their selection order, creating edges, splitting faces

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vertices_smooth(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        factor: float | None = 0.0,
        repeat: int | None = 1,
        xaxis: bool | None = True,
        yaxis: bool | None = True,
        zaxis: bool | None = True,
        wait_for_input: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Flatten angles of selected vertices

        :param execution_context:
        :param undo:
        :param factor: Smoothing, Smoothing factor (in [-10, 10], optional)
        :param repeat: Repeat, Number of times to smooth the mesh (in [1, 1000], optional)
        :param xaxis: X-Axis, Smooth along the X axis (optional)
        :param yaxis: Y-Axis, Smooth along the Y axis (optional)
        :param zaxis: Z-Axis, Smooth along the Z axis (optional)
        :param wait_for_input: Wait for Input, (optional)
        :return: Result of the operator call.
        """

class vertices_smooth_laplacian(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        repeat: int | None = 1,
        lambda_factor: float | None = 1.0,
        lambda_border: float | None = 5e-05,
        use_x: bool | None = True,
        use_y: bool | None = True,
        use_z: bool | None = True,
        preserve_volume: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Laplacian smooth of selected vertices

        :param execution_context:
        :param undo:
        :param repeat: Number of iterations to smooth the mesh, (in [1, 1000], optional)
        :param lambda_factor: Lambda factor, (in [1e-07, 1000], optional)
        :param lambda_border: Lambda factor in border, (in [1e-07, 1000], optional)
        :param use_x: Smooth X Axis, Smooth object along X axis (optional)
        :param use_y: Smooth Y Axis, Smooth object along Y axis (optional)
        :param use_z: Smooth Z Axis, Smooth object along Z axis (optional)
        :param preserve_volume: Preserve Volume, Apply volume preservation after smooth (optional)
        :return: Result of the operator call.
        """

class wireframe(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_boundary: bool | None = True,
        use_even_offset: bool | None = True,
        use_relative_offset: bool | None = False,
        use_replace: bool | None = True,
        thickness: float | None = 0.01,
        offset: float | None = 0.01,
        use_crease: bool | None = False,
        crease_weight: float | None = 0.01,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a solid wireframe from faces

        :param execution_context:
        :param undo:
        :param use_boundary: Boundary, Inset face boundaries (optional)
        :param use_even_offset: Offset Even, Scale the offset to give more even thickness (optional)
        :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry (optional)
        :param use_replace: Replace, Remove original faces (optional)
        :param thickness: Thickness, (in [0, 10000], optional)
        :param offset: Offset, (in [0, 10000], optional)
        :param use_crease: Crease, Crease hub edges for an improved subdivision surface (optional)
        :param crease_weight: Crease Weight, (in [0, 1000], optional)
        :return: Result of the operator call.
        """
