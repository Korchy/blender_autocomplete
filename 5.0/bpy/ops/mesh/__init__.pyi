import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops.transform
import bpy.stub_internal.rna_enums
import mathutils

def attribute_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value_float: float | None = 0.0,
    value_float_vector_2d: collections.abc.Iterable[float] | None = (0.0, 0.0),
    value_float_vector_3d: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    value_int: int | None = 0,
    value_int_vector_2d: collections.abc.Iterable[int] | None = (0, 0),
    value_color: collections.abc.Iterable[float] | None = (1.0, 1.0, 1.0, 1.0),
    value_bool: bool | None = False,
) -> None:
    """Set values of the active attribute for selected elements

    :param value_float: Value
    :param value_float_vector_2d: Value
    :param value_float_vector_3d: Value
    :param value_int: Value
    :param value_int_vector_2d: Value
    :param value_color: Value
    :param value_bool: Value
    """

def average_normals(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    average_type: typing.Literal["CUSTOM_NORMAL", "FACE_AREA", "CORNER_ANGLE"]
    | None = "CUSTOM_NORMAL",
    weight: int | None = 50,
    threshold: float | None = 0.01,
) -> None:
    """Average custom normals of selected vertices

        :param average_type: Type, Averaging method

    CUSTOM_NORMAL
    Custom Normal -- Take average of vertex normals.

    FACE_AREA
    Face Area -- Set all vertex normals by face area.

    CORNER_ANGLE
    Corner Angle -- Set all vertex normals by corner angle.
        :param weight: Weight, Weight applied per face
        :param threshold: Threshold, Threshold value for different weights to be considered equal
    """

def beautify_fill(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle_limit: float | None = 3.14159,
) -> None:
    """Rearrange some faces to try to get less degenerated geometry

    :param angle_limit: Max Angle, Angle limit
    """

def bevel(
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
) -> None:
    """Cut into selected items at an angle to create bevel or chamfer

        :param offset_type: Width Type, The method for determining the size of the bevel

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
        :param offset: Width, Bevel amount
        :param profile_type: Profile Type, The type of shape used to rebuild a beveled section

    SUPERELLIPSE
    Superellipse -- The profile can be a concave or convex curve.

    CUSTOM
    Custom -- The profile can be any arbitrary path between its endpoints.
        :param offset_pct: Width Percent, Bevel amount for percentage method
        :param segments: Segments, Segments for curved edge
        :param profile: Profile, Controls profile shape (0.5 = round)
        :param affect: Affect, Affect edges or vertices

    VERTICES
    Vertices -- Affect only vertices.

    EDGES
    Edges -- Affect only edges.
        :param clamp_overlap: Clamp Overlap, Do not allow beveled edges/vertices to overlap each other
        :param loop_slide: Loop Slide, Prefer sliding along edges to even widths
        :param mark_seam: Mark Seams, Preserve seams along beveled edges
        :param mark_sharp: Mark Sharp, Preserve sharp edges along beveled edges
        :param material: Material Index, Material for bevel faces (-1 means use adjacent faces)
        :param harden_normals: Harden Normals, Match normals of new faces to adjacent faces
        :param face_strength_mode: Face Strength Mode, Whether to set face strength, and which faces to set face strength on

    NONE
    None -- Do not set face strength.

    NEW
    New -- Set face strength on new faces only.

    AFFECTED
    Affected -- Set face strength on new and modified faces only.

    ALL
    All -- Set face strength on all faces.
        :param miter_outer: Outer Miter, Pattern to use for outside of miters

    SHARP
    Sharp -- Outside of miter is sharp.

    PATCH
    Patch -- Outside of miter is squared-off patch.

    ARC
    Arc -- Outside of miter is arc.
        :param miter_inner: Inner Miter, Pattern to use for inside of miters

    SHARP
    Sharp -- Inside of miter is sharp.

    ARC
    Arc -- Inside of miter is arc.
        :param spread: Spread, Amount to spread arcs for arc inner miters
        :param vmesh_method: Vertex Mesh Method, The method to use to create meshes at intersections

    ADJ
    Grid Fill -- Default patterned fill.

    CUTOFF
    Cutoff -- A cutoff at each profiles end before the intersection.
        :param release_confirm: Confirm on Release
    """

def bisect(
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
) -> None:
    """Cut geometry along a plane (click-drag to define plane)

    :param plane_co: Plane Point, A point on the plane
    :param plane_no: Plane Normal, The direction the plane points
    :param use_fill: Fill, Fill in the cut
    :param clear_inner: Clear Inner, Remove geometry behind the plane
    :param clear_outer: Clear Outer, Remove geometry in front of the plane
    :param threshold: Axis Threshold, Preserves the existing geometry along the cut plane
    :param xstart: X Start
    :param xend: X End
    :param ystart: Y Start
    :param yend: Y End
    :param flip: Flip
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    """

def blend_from_shape(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    shape: str | None = "",
    blend: float | None = 1.0,
    add: bool | None = True,
) -> None:
    """Blend in shape from a shape key

    :param shape: Shape, Shape key to use for blending
    :param blend: Blend, Blending factor
    :param add: Add, Add rather than blend between shapes
    """

def bridge_edge_loops(
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
    profile_shape: bpy.stub_internal.rna_enums.ProportionalFalloffCurveOnlyItems
    | None = "SMOOTH",
) -> None:
    """Create a bridge of faces between two or more selected edge loops

    :param type: Connect Loops, Method of bridging multiple loops
    :param use_merge: Merge, Merge rather than creating faces
    :param merge_factor: Merge Factor
    :param twist_offset: Twist, Twist offset for closed loops
    :param number_cuts: Number of Cuts
    :param interpolation: Interpolation, Interpolation method
    :param smoothness: Smoothness, Smoothness factor
    :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded
    :param profile_shape: Profile Shape, Shape of the profile
    """

def colors_reverse(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Flip direction of face corner color attribute inside faces"""

def colors_rotate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_ccw: bool | None = False,
) -> None:
    """Rotate face corner color attribute inside faces

    :param use_ccw: Counter Clockwise
    """

def convex_hull(
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
) -> None:
    """Enclose selected vertices in a convex polyhedron

    :param delete_unused: Delete Unused, Delete selected elements that are not used by the hull
    :param use_existing_faces: Use Existing Faces, Skip hull triangles that are covered by a pre-existing face
    :param make_holes: Make Holes, Delete selected faces that are used by the hull
    :param join_triangles: Join Triangles, Merge adjacent triangles into quads
    :param face_threshold: Max Face Angle, Face angle limit
    :param shape_threshold: Max Shape Angle, Shape angle limit
    :param topology_influence: Topology Influence, How much to prioritize regular grids of quads as well as quads that touch existing quads
    :param uvs: Compare UVs
    :param vcols: Compare Color Attributes
    :param seam: Compare Seam
    :param sharp: Compare Sharp
    :param materials: Compare Materials
    :param deselect_joined: Deselect Joined, Only select remaining triangles that were not merged
    """

def customdata_custom_splitnormals_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a custom normals layer, if none exists yet"""

def customdata_custom_splitnormals_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the custom normals layer, if it exists"""

def customdata_mask_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear vertex sculpt masking data from the mesh"""

def customdata_skin_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a vertex skin layer"""

def customdata_skin_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear vertex skin layer"""

def decimate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 1.0,
    use_vertex_group: bool | None = False,
    vertex_group_factor: float | None = 1.0,
    invert_vertex_group: bool | None = False,
    use_symmetry: bool | None = False,
    symmetry_axis: bpy.stub_internal.rna_enums.AxisXyzItems | None = "Y",
) -> None:
    """Simplify geometry by collapsing edges

    :param ratio: Ratio
    :param use_vertex_group: Vertex Group, Use active vertex group as an influence
    :param vertex_group_factor: Weight, Vertex group strength
    :param invert_vertex_group: Invert, Invert vertex group influence
    :param use_symmetry: Symmetry, Maintain symmetry on an axis
    :param symmetry_axis: Axis, Axis of symmetry
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["VERT", "EDGE", "FACE", "EDGE_FACE", "ONLY_FACE"]
    | None = "VERT",
) -> None:
    """Delete selected vertices, edges or faces

    :param type: Type, Method used for deleting mesh data
    """

def delete_edgeloop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_face_split: bool | None = True,
) -> None:
    """Delete an edge loop by merging the faces on each side

    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    """

def delete_loose(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_verts: bool | None = True,
    use_edges: bool | None = True,
    use_faces: bool | None = False,
) -> None:
    """Delete loose vertices, edges or faces

    :param use_verts: Vertices, Remove loose vertices
    :param use_edges: Edges, Remove loose edges
    :param use_faces: Faces, Remove loose faces
    """

def dissolve_degenerate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    threshold: float | None = 0.0001,
) -> None:
    """Dissolve zero area faces and zero length edges

    :param threshold: Merge Distance, Maximum distance between elements to merge
    """

def dissolve_edges(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_verts: bool | None = True,
    angle_threshold: float | None = 3.14159,
    use_face_split: bool | None = False,
) -> None:
    """Dissolve edges, merging faces

    :param use_verts: Dissolve Vertices, Dissolve remaining vertices which connect to only two edges
    :param angle_threshold: Angle Threshold, Remaining vertices which separate edge pairs are preserved if their edge angle exceeds this threshold.
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    """

def dissolve_faces(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_verts: bool | None = False,
) -> None:
    """Dissolve faces

    :param use_verts: Dissolve Vertices, Dissolve remaining vertices which connect to only two edges
    """

def dissolve_limited(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle_limit: float | None = 0.0872665,
    use_dissolve_boundaries: bool | None = False,
    delimit: set[bpy.stub_internal.rna_enums.MeshDelimitModeItems] | None = {"NORMAL"},
) -> None:
    """Dissolve selected edges and vertices, limited by the angle of surrounding geometry

    :param angle_limit: Max Angle, Angle limit
    :param use_dissolve_boundaries: All Boundaries, Dissolve all vertices in between face boundaries
    :param delimit: Delimit, Delimit dissolve operation
    """

def dissolve_mode(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_verts: bool | None = False,
    angle_threshold: float | None = 3.14159,
    use_face_split: bool | None = False,
    use_boundary_tear: bool | None = False,
) -> None:
    """Dissolve geometry based on the selection mode

    :param use_verts: Dissolve Vertices, Dissolve remaining vertices which connect to only two edges
    :param angle_threshold: Angle Threshold, Remaining vertices which separate edge pairs are preserved if their edge angle exceeds this threshold.
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces
    """

def dissolve_verts(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_face_split: bool | None = False,
    use_boundary_tear: bool | None = False,
) -> None:
    """Dissolve vertices, merge edges and faces

    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces
    """

def dupli_extrude_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    rotate_source: bool | None = True,
) -> None:
    """Duplicate and extrude selected vertices, edges or faces towards the mouse cursor

    :param rotate_source: Rotate Source, Rotate initial selection giving better shape
    """

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: int | None = 1,
) -> None:
    """Duplicate selected vertices, edges or faces

    :param mode: Mode
    """

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Duplicate mesh and move

    :param MESH_OT_duplicate: Duplicate, Duplicate selected vertices, edges or faces
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def edge_collapse(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Collapse isolated edge and face regions, merging data such as UVs and color attributes. This can collapse edge-rings as well as regions of connected faces into vertices"""

def edge_face_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add an edge or face to selected"""

def edge_rotate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_ccw: bool | None = False,
) -> None:
    """Rotate selected edge or adjoining faces

    :param use_ccw: Counter Clockwise
    """

def edge_split(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["EDGE", "VERT"] | None = "EDGE",
) -> None:
    """Split selected edges so that each neighbor face gets its own copy

        :param type: Type, Method to use for splitting

    EDGE
    Faces by Edges -- Split faces along selected edges.

    VERT
    Faces & Edges by Vertices -- Split faces and edges connected to selected vertices.
    """

def edgering_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect: bool | None = False,
    toggle: bool | None = False,
    ring: bool | None = True,
) -> None:
    """Select an edge ring

    :param extend: Extend, Extend the selection
    :param deselect: Deselect, Remove from the selection
    :param toggle: Toggle Select, Toggle the selection
    :param ring: Select Ring, Select ring
    """

def edges_select_sharp(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    sharpness: float | None = 0.523599,
) -> None:
    """Select all sharp enough edges

    :param sharpness: Sharpness
    """

def extrude_context(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_normal_flip: bool | None = False,
    use_dissolve_ortho_edges: bool | None = False,
    mirror: bool | None = False,
) -> None:
    """Extrude selection

    :param use_normal_flip: Flip Normals
    :param use_dissolve_ortho_edges: Dissolve Orthogonal Edges
    :param mirror: Mirror Editing
    """

def extrude_context_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_context: extrude_context | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Extrude region together along the average normal

    :param MESH_OT_extrude_context: Extrude Context, Extrude selection
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def extrude_edges_indiv(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_normal_flip: bool | None = False,
    mirror: bool | None = False,
) -> None:
    """Extrude individual edges only

    :param use_normal_flip: Flip Normals
    :param mirror: Mirror Editing
    """

def extrude_edges_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_edges_indiv: extrude_edges_indiv | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Extrude edges and move result

    :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def extrude_faces_indiv(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
) -> None:
    """Extrude individual faces only

    :param mirror: Mirror Editing
    """

def extrude_faces_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_faces_indiv: extrude_faces_indiv | None = None,
    TRANSFORM_OT_shrink_fatten: bpy.ops.transform.shrink_fatten | None = None,
) -> None:
    """Extrude each individual face separately along local normals

    :param MESH_OT_extrude_faces_indiv: Extrude Individual Faces, Extrude individual faces only
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals
    """

def extrude_manifold(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_region: extrude_region | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Extrude, dissolves edges whose faces form a flat surface and intersect new edges

    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def extrude_region(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_normal_flip: bool | None = False,
    use_dissolve_ortho_edges: bool | None = False,
    mirror: bool | None = False,
) -> None:
    """Extrude region of faces

    :param use_normal_flip: Flip Normals
    :param use_dissolve_ortho_edges: Dissolve Orthogonal Edges
    :param mirror: Mirror Editing
    """

def extrude_region_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_region: extrude_region | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Extrude region and move result

    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def extrude_region_shrink_fatten(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_region: extrude_region | None = None,
    TRANSFORM_OT_shrink_fatten: bpy.ops.transform.shrink_fatten | None = None,
) -> None:
    """Extrude region together along local normals

    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals
    """

def extrude_repeat(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    steps: int | None = 10,
    offset: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
    scale_offset: float | None = 1.0,
) -> None:
    """Extrude selected vertices, edges or faces repeatedly

    :param steps: Steps
    :param offset: Offset, Offset vector
    :param scale_offset: Scale Offset
    """

def extrude_vertices_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_verts_indiv: extrude_verts_indiv | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Extrude vertices and move result

    :param MESH_OT_extrude_verts_indiv: Extrude Only Vertices, Extrude individual vertices only
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def extrude_verts_indiv(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
) -> None:
    """Extrude individual vertices only

    :param mirror: Mirror Editing
    """

def face_make_planar(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 1.0,
    repeat: int | None = 1,
) -> None:
    """Flatten selected faces

    :param factor: Factor
    :param repeat: Iterations
    """

def face_split_by_edges(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Weld loose edges into faces (splitting them into new faces)"""

def faces_select_linked_flat(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    sharpness: float | None = 0.0174533,
) -> None:
    """Select linked faces by angle

    :param sharpness: Sharpness
    """

def faces_shade_flat(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Display faces flat"""

def faces_shade_smooth(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Display faces smooth (using vertex normals)"""

def fill(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_beauty: bool | None = True,
) -> None:
    """Fill a selected edge loop with faces

    :param use_beauty: Beauty, Use best triangulation division
    """

def fill_grid(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    span: int | None = 1,
    offset: int | None = 0,
    use_interp_simple: bool | None = False,
) -> None:
    """Fill grid from two loops

    :param span: Span, Number of grid columns
    :param offset: Offset, Vertex that is the corner of the grid
    :param use_interp_simple: Simple Blending, Use simple interpolation of grid vertices
    """

def fill_holes(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    sides: int | None = 4,
) -> None:
    """Fill in holes (boundary edge loops)

    :param sides: Sides, Number of sides in hole required to fill (zero fills all holes)
    """

def flip_normals(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_clnors: bool | None = False,
) -> None:
    """Flip the direction of selected faces normals (and of their vertices)

    :param only_clnors: Custom Normals Only, Only flip the custom loop normals of the selected elements
    """

def flip_quad_tessellation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Flips the tessellation of selected quads"""

def hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Hide (un)selected vertices, edges or faces

    :param unselected: Unselected, Hide unselected rather than selected
    """

def inset(
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
) -> None:
    """Inset new faces into selected faces

    :param use_boundary: Boundary, Inset face boundaries
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
    :param use_edge_rail: Edge Rail, Inset the region along existing edges
    :param thickness: Thickness
    :param depth: Depth
    :param use_outset: Outset, Outset rather than inset
    :param use_select_inset: Select Outer, Select the new inset faces
    :param use_individual: Individual, Individual face inset
    :param use_interpolate: Interpolate, Blend face data across the inset
    :param release_confirm: Confirm on Release
    """

def intersect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["SELECT", "SELECT_UNSELECT"] | None = "SELECT_UNSELECT",
    separate_mode: typing.Literal["ALL", "CUT", "NONE"] | None = "CUT",
    threshold: float | None = 1e-06,
    solver: typing.Literal["FLOAT", "EXACT"] | None = "EXACT",
) -> None:
    """Cut an intersection into faces

        :param mode: Source

    SELECT
    Self Intersect -- Self intersect selected faces.

    SELECT_UNSELECT
    Selected/Unselected -- Intersect selected with unselected faces.
        :param separate_mode: Separate Mode

    ALL
    All -- Separate all geometry from intersections.

    CUT
    Cut -- Cut into geometry keeping each side separate (Selected/Unselected only).

    NONE
    Merge -- Merge all geometry from the intersection.
        :param threshold: Merge Threshold
        :param solver: Solver, Which Intersect solver to use

    FLOAT
    Float -- Simple solver with good performance, without support for overlapping geometry.

    EXACT
    Exact -- Slower solver with the best results for coplanar faces.
    """

def intersect_boolean(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    operation: typing.Literal["INTERSECT", "UNION", "DIFFERENCE"] | None = "DIFFERENCE",
    use_swap: bool | None = False,
    use_self: bool | None = False,
    threshold: float | None = 1e-06,
    solver: typing.Literal["FLOAT", "EXACT"] | None = "EXACT",
) -> None:
    """Cut solid geometry from selected to unselected

        :param operation: Boolean Operation, Which boolean operation to apply
        :param use_swap: Swap, Use with difference intersection to swap which side is kept
        :param use_self: Self Intersection, Do self-union or self-intersection
        :param threshold: Merge Threshold
        :param solver: Solver, Which Boolean solver to use

    FLOAT
    Float -- Faster solver, some limitations.

    EXACT
    Exact -- Exact solver, slower, handles more cases.
    """

def knife_project(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    cut_through: bool | None = False,
) -> None:
    """Use other objects outlines and boundaries to project knife cuts

    :param cut_through: Cut Through, Cut through all faces, not just visible ones
    """

def knife_tool(
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
) -> None:
    """Cut new topology

        :param use_occlude_geometry: Occlude Geometry, Only cut the front most geometry
        :param only_selected: Only Selected, Only cut selected geometry
        :param xray: X-Ray, Show cuts hidden by geometry
        :param visible_measurements: Measurements, Visible distance and angle measurements

    NONE
    None -- Show no measurements.

    BOTH
    Both -- Show both distances and angles.

    DISTANCE
    Distance -- Show just distance measurements.

    ANGLE
    Angle -- Show just angle measurements.
        :param angle_snapping: Angle Snapping, Angle snapping mode

    NONE
    None -- No angle snapping.

    SCREEN
    Screen -- Screen space angle snapping.

    RELATIVE
    Relative -- Angle snapping relative to the previous cut edge.
        :param angle_snapping_increment: Angle Snap Increment, The angle snap increment used when in constrained angle mode
        :param wait_for_input: Wait for Input
    """

def loop_multi_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ring: bool | None = False,
) -> None:
    """Select a loop of connected edges by connection type

    :param ring: Ring
    """

def loop_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect: bool | None = False,
    toggle: bool | None = False,
    ring: bool | None = False,
) -> None:
    """Select a loop of connected edges

    :param extend: Extend Select, Extend the selection
    :param deselect: Deselect, Remove from the selection
    :param toggle: Toggle Select, Toggle the selection
    :param ring: Select Ring, Select ring
    """

def loop_to_region(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select_bigger: bool | None = False,
) -> None:
    """Select region of faces inside of a selected loop of edges

    :param select_bigger: Select Bigger, Select bigger regions instead of smaller ones
    """

def loopcut(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    number_cuts: int | None = 1,
    smoothness: float | None = 0.0,
    falloff: bpy.stub_internal.rna_enums.ProportionalFalloffCurveOnlyItems
    | None = "INVERSE_SQUARE",
    object_index: int | None = -1,
    edge_index: int | None = -1,
    mesh_select_mode_init: collections.abc.Iterable[bool] | None = (
        False,
        False,
        False,
    ),
) -> None:
    """Add a new loop between existing loops

    :param number_cuts: Number of Cuts
    :param smoothness: Smoothness, Smoothness factor
    :param falloff: Falloff, Falloff type of the feather
    :param object_index: Object Index
    :param edge_index: Edge Index
    """

def loopcut_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_loopcut: loopcut | None = None,
    TRANSFORM_OT_edge_slide: bpy.ops.transform.edge_slide | None = None,
) -> None:
    """Cut mesh loop and slide it

    :param MESH_OT_loopcut: Loop Cut, Add a new loop between existing loops
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh
    """

def mark_freestyle_edge(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
) -> None:
    """(Un)mark selected edges as Freestyle feature edges

    :param clear: Clear
    """

def mark_freestyle_face(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
) -> None:
    """(Un)mark selected faces for exclusion from Freestyle feature edge detection

    :param clear: Clear
    """

def mark_seam(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
) -> None:
    """(Un)mark selected edges as a seam

    :param clear: Clear
    """

def mark_sharp(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
    use_verts: bool | None = False,
) -> None:
    """(Un)mark selected edges as sharp

    :param clear: Clear
    :param use_verts: Vertices, Consider vertices instead of edges to select which edges to (un)tag as sharp
    """

def merge(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CENTER", "CURSOR", "COLLAPSE", "FIRST", "LAST"]
    | None = "CENTER",
    uvs: bool | None = False,
) -> None:
    """Merge selected vertices

    :param type: Type, Merge method to use
    :param uvs: UVs, Move UVs according to merge
    """

def merge_normals(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Merge custom normals of selected vertices"""

def mod_weighted_strength(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    set: bool | None = False,
    face_strength: typing.Literal["WEAK", "MEDIUM", "STRONG"] | None = "MEDIUM",
) -> None:
    """Set/Get strength of face (used in Weighted Normal modifier)

    :param set: Set Value, Set value of faces
    :param face_strength: Face Strength, Strength to use for assigning or selecting face influence for weighted normal modifier
    """

def normals_make_consistent(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    inside: bool | None = False,
) -> None:
    """Make face and vertex normals point either outside or inside the mesh

    :param inside: Inside
    """

def normals_tools(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["COPY", "PASTE", "ADD", "MULTIPLY", "RESET"] | None = "COPY",
    absolute: bool | None = False,
) -> None:
    """Custom normals tools using Normal Vector of UI

        :param mode: Mode, Mode of tools taking input from interface

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
        :param absolute: Absolute Coordinates, Copy Absolute coordinates of Normal vector
    """

def offset_edge_loops(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_cap_endpoint: bool | None = False,
) -> None:
    """Create offset edge loop from the current selection

    :param use_cap_endpoint: Cap Endpoint, Extend loop around end-points
    """

def offset_edge_loops_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_offset_edge_loops: offset_edge_loops | None = None,
    TRANSFORM_OT_edge_slide: bpy.ops.transform.edge_slide | None = None,
) -> None:
    """Offset edge loop slide

    :param MESH_OT_offset_edge_loops: Offset Edge Loop, Create offset edge loop from the current selection
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh
    """

def point_normals(
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
) -> None:
    """Point selected custom normals to specified Target

        :param mode: Mode, How to define coordinates to point custom normals to

    COORDINATES
    Coordinates -- Use static coordinates (defined by various means).

    MOUSE
    Mouse -- Follow mouse cursor.
        :param invert: Invert, Invert affected normals
        :param align: Align, Make all affected normals parallel
        :param target_location: Target, Target location to which normals will point
        :param spherize: Spherize, Interpolate between original and new normals
        :param spherize_strength: Spherize Strength, Ratio of spherized normal to original normal
    """

def poke(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: float | None = 0.0,
    use_relative_offset: bool | None = False,
    center_mode: typing.Literal["MEDIAN_WEIGHTED", "MEDIAN", "BOUNDS"]
    | None = "MEDIAN_WEIGHTED",
) -> None:
    """Split a face into a fan

        :param offset: Poke Offset, Poke Offset
        :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
        :param center_mode: Poke Center, Poke face center calculation

    MEDIAN_WEIGHTED
    Weighted Median -- Weighted median face center.

    MEDIAN
    Median -- Median face center.

    BOUNDS
    Bounds -- Face bounds center.
    """

def polybuild_delete_at_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Undocumented, consider contributing.

    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def polybuild_dissolve_at_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing."""

def polybuild_extrude_at_cursor_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_polybuild_transform_at_cursor: polybuild_transform_at_cursor | None = None,
    MESH_OT_extrude_edges_indiv: extrude_edges_indiv | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Undocumented, consider contributing.

    :param MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor
    :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def polybuild_face_at_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    create_quads: bool | None = True,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Undocumented, consider contributing.

    :param create_quads: Create Quads, Automatically split edges in triangles to maintain quad topology
    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def polybuild_face_at_cursor_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_polybuild_face_at_cursor: polybuild_face_at_cursor | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Undocumented, consider contributing.

    :param MESH_OT_polybuild_face_at_cursor: Poly Build Face at Cursor
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def polybuild_split_at_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Undocumented, consider contributing.

    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def polybuild_split_at_cursor_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_polybuild_split_at_cursor: polybuild_split_at_cursor | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Undocumented, consider contributing.

    :param MESH_OT_polybuild_split_at_cursor: Poly Build Split at Cursor
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def polybuild_transform_at_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Undocumented, consider contributing.

    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def polybuild_transform_at_cursor_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_polybuild_transform_at_cursor: polybuild_transform_at_cursor | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Undocumented, consider contributing.

    :param MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def primitive_circle_add(
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
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a circle mesh

        :param vertices: Vertices
        :param radius: Radius
        :param fill_type: Fill Type

    NOTHING
    Nothing -- Dont fill at all.

    NGON
    N-Gon -- Use n-gons.

    TRIFAN
    Triangle Fan -- Use triangle fans.
        :param calc_uvs: Generate UVs, Generate a default UV map
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

def primitive_cone_add(
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
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a conic mesh

        :param vertices: Vertices
        :param radius1: Radius 1
        :param radius2: Radius 2
        :param depth: Depth
        :param end_fill_type: Base Fill Type

    NOTHING
    Nothing -- Dont fill at all.

    NGON
    N-Gon -- Use n-gons.

    TRIFAN
    Triangle Fan -- Use triangle fans.
        :param calc_uvs: Generate UVs, Generate a default UV map
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

def primitive_cube_add(
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
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a cube mesh that consists of six square faces

        :param size: Size
        :param calc_uvs: Generate UVs, Generate a default UV map
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

def primitive_cube_add_gizmo(
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
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = (
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
    ),
) -> None:
    """Construct a cube mesh

        :param calc_uvs: Generate UVs, Generate a default UV map
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
        :param matrix: Matrix
    """

def primitive_cylinder_add(
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
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a cylinder mesh

        :param vertices: Vertices
        :param radius: Radius
        :param depth: Depth
        :param end_fill_type: Cap Fill Type

    NOTHING
    Nothing -- Dont fill at all.

    NGON
    N-Gon -- Use n-gons.

    TRIFAN
    Triangle Fan -- Use triangle fans.
        :param calc_uvs: Generate UVs, Generate a default UV map
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

def primitive_grid_add(
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
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a subdivided plane mesh

        :param x_subdivisions: X Subdivisions
        :param y_subdivisions: Y Subdivisions
        :param size: Size
        :param calc_uvs: Generate UVs, Generate a default UV map
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

def primitive_ico_sphere_add(
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
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a spherical mesh that consists of equally sized triangles

        :param subdivisions: Subdivisions
        :param radius: Radius
        :param calc_uvs: Generate UVs, Generate a default UV map
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

def primitive_monkey_add(
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
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a Suzanne mesh

        :param size: Size
        :param calc_uvs: Generate UVs, Generate a default UV map
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

def primitive_plane_add(
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
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a filled planar mesh with 4 vertices

        :param size: Size
        :param calc_uvs: Generate UVs, Generate a default UV map
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

def primitive_torus_add(
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
) -> None:
    """Construct a torus mesh

        :param align: Align

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location
        :param rotation: Rotation
        :param major_segments: Major Segments, Number of segments for the main ring of the torus
        :param minor_segments: Minor Segments, Number of segments for the minor ring of the torus
        :param mode: Dimensions Mode

    MAJOR_MINOR
    Major/Minor -- Use the major/minor radii for torus dimensions.

    EXT_INT
    Exterior/Interior -- Use the exterior/interior radii for torus dimensions.
        :param major_radius: Major Radius, Radius from the origin to the center of the cross sections
        :param minor_radius: Minor Radius, Radius of the torus cross section
        :param abso_major_rad: Exterior Radius, Total Exterior Radius of the torus
        :param abso_minor_rad: Interior Radius, Total Interior Radius of the torus
        :param generate_uvs: Generate UVs, Generate a default UV map
    """

def primitive_uv_sphere_add(
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
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a spherical mesh with quad faces, except for triangle faces at the top and bottom

        :param segments: Segments
        :param ring_count: Rings
        :param radius: Radius
        :param calc_uvs: Generate UVs, Generate a default UV map
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

def quads_convert_to_tris(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    quad_method: bpy.stub_internal.rna_enums.ModifierTriangulateQuadMethodItems
    | None = "BEAUTY",
    ngon_method: bpy.stub_internal.rna_enums.ModifierTriangulateNgonMethodItems
    | None = "BEAUTY",
) -> None:
    """Triangulate selected faces

    :param quad_method: Quad Method, Method for splitting the quads into triangles
    :param ngon_method: N-gon Method, Method for splitting the n-gons into triangles
    """

def region_to_loop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select boundary edges around the selected faces"""

def remove_doubles(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    threshold: float | None = 0.0001,
    use_centroid: bool | None = True,
    use_unselected: bool | None = False,
    use_sharp_edge_from_normals: bool | None = False,
) -> None:
    """Merge vertices based on their proximity

    :param threshold: Merge Distance, Maximum distance between elements to merge
    :param use_centroid: Centroid Merge, Move vertices to the centroid of the duplicate cluster, otherwise the vertex closest to the centroid is used.
    :param use_unselected: Unselected, Merge selected to other unselected vertices
    :param use_sharp_edge_from_normals: Sharp Edges, Calculate sharp edges using custom normal data (when available)
    """

def reorder_vertices_spatial(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reorder mesh faces and vertices based on their spatial position for better BVH building and sculpting performance."""

def reveal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
) -> None:
    """Reveal all hidden vertices, edges and faces

    :param select: Select
    """

def rip(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
    use_fill: bool | None = False,
) -> None:
    """Disconnect vertex or edges from connected geometry

    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    :param use_fill: Fill, Fill the ripped region
    """

def rip_edge(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Extend vertices along the edge closest to the cursor

    :param mirror: Mirror Editing
    :param use_proportional_edit: Proportional Editing
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :param proportional_size: Proportional Size
    :param use_proportional_connected: Connected
    :param use_proportional_projected: Projected (2D)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    """

def rip_edge_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_rip_edge: rip_edge | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Extend vertices and move the result

    :param MESH_OT_rip_edge: Extend Vertices, Extend vertices along the edge closest to the cursor
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def rip_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_rip: rip | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Rip polygons and move the result

    :param MESH_OT_rip: Rip, Disconnect vertex or edges from connected geometry
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def screw(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    steps: int | None = 9,
    turns: int | None = 1,
    center: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
    axis: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Extrude selected vertices in screw-shaped rotation around the cursor in indicated viewport

    :param steps: Steps, Steps
    :param turns: Turns, Turns
    :param center: Center, Center in global view space
    :param axis: Axis, Axis in global view space
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """(De)select all vertices, edges or faces

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

def select_axis(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    orientation: bpy.stub_internal.rna_enums.TransformOrientationItems | None = "LOCAL",
    sign: typing.Literal["POS", "NEG", "ALIGN"] | None = "POS",
    axis: bpy.stub_internal.rna_enums.AxisXyzItems | None = "X",
    threshold: float | None = 0.0001,
) -> None:
    """Select all data in the mesh on a single axis

    :param orientation: Axis Mode, Axis orientation
    :param sign: Axis Sign, Side to select
    :param axis: Axis, Select the axis to compare each vertex on
    :param threshold: Threshold
    """

def select_by_attribute(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select elements based on the active boolean attribute"""

def select_by_pole_count(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pole_count: int | None = 4,
    type: typing.Literal["LESS", "EQUAL", "GREATER", "NOTEQUAL"] | None = "NOTEQUAL",
    extend: bool | None = False,
    exclude_nonmanifold: bool | None = True,
) -> None:
    """Select vertices at poles by the number of connected edges. In edge and face mode the geometry connected to the vertices is selected

    :param pole_count: Pole Count
    :param type: Type, Type of comparison to make
    :param extend: Extend, Extend the selection
    :param exclude_nonmanifold: Exclude Non Manifold, Exclude non-manifold poles
    """

def select_face_by_sides(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    number: int | None = 4,
    type: typing.Literal["LESS", "EQUAL", "GREATER", "NOTEQUAL"] | None = "EQUAL",
    extend: bool | None = True,
) -> None:
    """Select vertices or faces by the number of face sides

    :param number: Number of Vertices
    :param type: Type, Type of comparison to make
    :param extend: Extend, Extend the selection
    """

def select_interior_faces(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select faces where all edges have more than 2 face users"""

def select_less(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_face_step: bool | None = True,
) -> None:
    """Deselect vertices, edges or faces at the boundary of each selection region

    :param use_face_step: Face Step, Connected faces (instead of edges)
    """

def select_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delimit: set[bpy.stub_internal.rna_enums.MeshDelimitModeItems] | None = {"SEAM"},
) -> None:
    """Select all vertices connected to the current selection

    :param delimit: Delimit, Delimit selected region
    """

def select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deselect: bool | None = False,
    delimit: set[bpy.stub_internal.rna_enums.MeshDelimitModeItems] | None = {"SEAM"},
    object_index: int | None = -1,
    index: int | None = -1,
) -> None:
    """(De)select all vertices linked to the edge under the mouse cursor

    :param deselect: Deselect
    :param delimit: Delimit, Delimit selected region
    """

def select_loose(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
) -> None:
    """Select loose geometry based on the selection mode

    :param extend: Extend, Extend the selection
    """

def select_mirror(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    axis: set[bpy.stub_internal.rna_enums.AxisFlagXyzItems] | None = {"X"},
    extend: bool | None = False,
) -> None:
    """Select mesh items at mirrored locations

    :param axis: Axis
    :param extend: Extend, Extend the existing selection
    """

def select_mode(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_extend: bool | None = False,
    use_expand: bool | None = False,
    type: bpy.stub_internal.rna_enums.MeshSelectModeItems | None = "VERT",
    action: typing.Literal["DISABLE", "ENABLE", "TOGGLE"] | None = "TOGGLE",
) -> None:
    """Change selection mode

        :param use_extend: Extend
        :param use_expand: Expand
        :param type: Type
        :param action: Action, Selection action to execute

    DISABLE
    Disable -- Disable selected markers.

    ENABLE
    Enable -- Enable selected markers.

    TOGGLE
    Toggle -- Toggle disabled flag for selected markers.
    """

def select_more(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_face_step: bool | None = True,
) -> None:
    """Select more vertices, edges or faces connected to initial selection

    :param use_face_step: Face Step, Connected faces (instead of edges)
    """

def select_next_item(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select the next element (using selection order)"""

def select_non_manifold(
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
) -> None:
    """Select all non-manifold vertices or edges

    :param extend: Extend, Extend the selection
    :param use_wire: Wire, Wire edges
    :param use_boundary: Boundaries, Boundary edges
    :param use_multi_face: Multiple Faces, Edges shared by more than two faces
    :param use_non_contiguous: Non Contiguous, Edges between faces pointing in alternate directions
    :param use_verts: Vertices, Vertices connecting multiple face regions
    """

def select_nth(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    skip: int | None = 1,
    nth: int | None = 1,
    offset: int | None = 0,
) -> None:
    """Deselect every Nth element starting from the active vertex, edge or face

    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :param offset: Offset, Offset from the starting point
    """

def select_prev_item(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select the previous element (using selection order)"""

def select_random(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 0.5,
    seed: int | None = 0,
    action: typing.Literal["SELECT", "DESELECT"] | None = "SELECT",
) -> None:
    """Randomly select vertices

        :param ratio: Ratio, Portion of items to select randomly
        :param seed: Random Seed, Seed for the random number generator
        :param action: Action, Selection action to execute

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.
    """

def select_similar(
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
) -> None:
    """Select similar vertices, edges or faces by property types

    :param type: Type
    :param compare: Compare
    :param threshold: Threshold
    """

def select_similar_region(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select similar face regions to the current selection"""

def select_ungrouped(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
) -> None:
    """Select vertices without a group

    :param extend: Extend, Extend the selection
    """

def separate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["SELECTED", "MATERIAL", "LOOSE"] | None = "SELECTED",
) -> None:
    """Separate selected geometry into a new mesh

    :param type: Type
    """

def set_normals_from_faces(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keep_sharp: bool | None = False,
) -> None:
    """Set the custom normals from the selected faces ones

    :param keep_sharp: Keep Sharp Edges, Do not set sharp edges to face
    """

def set_sharpness_by_angle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle: float | None = 0.523599,
    extend: bool | None = False,
) -> None:
    """Set edge sharpness based on the angle between neighboring faces

    :param angle: Angle
    :param extend: Extend, Add new sharp edges without clearing existing sharp edges
    """

def shape_propagate_to_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Apply selected vertex locations to all other shape keys"""

def shortest_path_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    edge_mode: typing.Literal["SELECT", "SEAM", "SHARP", "CREASE", "BEVEL", "FREESTYLE"]
    | None = "SELECT",
    use_face_step: bool | None = False,
    use_topology_distance: bool | None = False,
    use_fill: bool | None = False,
    skip: int | None = 0,
    nth: int | None = 1,
    offset: int | None = 0,
    index: int | None = -1,
) -> None:
    """Select shortest path between two selections

    :param edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :param offset: Offset, Offset from the starting point
    """

def shortest_path_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    edge_mode: typing.Literal["SELECT", "SEAM", "SHARP", "CREASE", "BEVEL", "FREESTYLE"]
    | None = "SELECT",
    use_face_step: bool | None = False,
    use_topology_distance: bool | None = False,
    use_fill: bool | None = False,
    skip: int | None = 0,
    nth: int | None = 1,
    offset: int | None = 0,
) -> None:
    """Selected shortest path between two vertices/edges/faces

    :param edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :param offset: Offset, Offset from the starting point
    """

def smooth_normals(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.5,
) -> None:
    """Smooth custom normals based on adjacent vertex normals

    :param factor: Factor, Specifies weight of smooth vs original normal
    """

def solidify(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    thickness: float | None = 0.01,
) -> None:
    """Create a solid skin by extruding, compensating for sharp angles

    :param thickness: Thickness
    """

def sort_elements(
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
) -> None:
    """The order of selected vertices/edges/faces is modified, based on a given method

        :param type: Type, Type of reordering operation to apply

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
        :param elements: Elements, Which elements to affect (vertices, edges and/or faces)
        :param reverse: Reverse, Reverse the sorting effect
        :param seed: Seed, Seed for random-based operations
    """

def spin(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    steps: int | None = 12,
    dupli: bool | None = False,
    angle: float | None = 1.5708,
    use_auto_merge: bool | None = True,
    use_normal_flip: bool | None = False,
    center: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
    axis: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Extrude selected vertices in a circle around the cursor in indicated viewport

    :param steps: Steps, Steps
    :param dupli: Use Duplicates
    :param angle: Angle, Rotation for each step
    :param use_auto_merge: Auto Merge, Merge first/last when the angle is a full revolution
    :param use_normal_flip: Flip Normals
    :param center: Center, Center in global view space
    :param axis: Axis, Axis in global view space
    """

def split(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Split off selected geometry from connected unselected geometry"""

def split_normals(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Split custom normals of selected vertices"""

def subdivide(
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
) -> None:
    """Subdivide selected edges

    :param number_cuts: Number of Cuts
    :param smoothness: Smoothness, Smoothness factor
    :param ngon: Create N-Gons, When disabled, newly created faces are limited to 3 and 4 sided faces
    :param quadcorner: Quad Corner Type, How to subdivide quad corners (anything other than Straight Cut will prevent n-gons)
    :param fractal: Fractal, Fractal randomness factor
    :param fractal_along_normal: Along Normal, Apply fractal displacement along normal only
    :param seed: Random Seed, Seed for the random number generator
    """

def subdivide_edgering(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    number_cuts: int | None = 10,
    interpolation: typing.Literal["LINEAR", "PATH", "SURFACE"] | None = "PATH",
    smoothness: float | None = 1.0,
    profile_shape_factor: float | None = 0.0,
    profile_shape: bpy.stub_internal.rna_enums.ProportionalFalloffCurveOnlyItems
    | None = "SMOOTH",
) -> None:
    """Subdivide perpendicular edges to the selected edge-ring

    :param number_cuts: Number of Cuts
    :param interpolation: Interpolation, Interpolation method
    :param smoothness: Smoothness, Smoothness factor
    :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded
    :param profile_shape: Profile Shape, Shape of the profile
    """

def symmetrize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: bpy.stub_internal.rna_enums.SymmetrizeDirectionItems
    | None = "NEGATIVE_X",
    threshold: float | None = 0.0001,
) -> None:
    """Enforce symmetry (both form and topological) across an axis

    :param direction: Direction, Which sides to copy from and to
    :param threshold: Threshold, Limit for snap middle vertices to the axis center
    """

def symmetry_snap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: bpy.stub_internal.rna_enums.SymmetrizeDirectionItems
    | None = "NEGATIVE_X",
    threshold: float | None = 0.05,
    factor: float | None = 0.5,
    use_center: bool | None = True,
) -> None:
    """Snap vertex pairs to their mirrored locations

    :param direction: Direction, Which sides to copy from and to
    :param threshold: Threshold, Distance within which matching vertices are searched
    :param factor: Factor, Mix factor of the locations of the vertices
    :param use_center: Center, Snap middle vertices to the axis center
    """

def tris_convert_to_quads(
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
) -> None:
    """Merge triangles into four sided polygons where possible

    :param face_threshold: Max Face Angle, Face angle limit
    :param shape_threshold: Max Shape Angle, Shape angle limit
    :param topology_influence: Topology Influence, How much to prioritize regular grids of quads as well as quads that touch existing quads
    :param uvs: Compare UVs
    :param vcols: Compare Color Attributes
    :param seam: Compare Seam
    :param sharp: Compare Sharp
    :param materials: Compare Materials
    :param deselect_joined: Deselect Joined, Only select remaining triangles that were not merged
    """

def unsubdivide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    iterations: int | None = 2,
) -> None:
    """Un-subdivide selected edges and faces

    :param iterations: Iterations, Number of times to un-subdivide
    """

def uv_texture_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add UV map"""

def uv_texture_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove UV map"""

def uvs_reverse(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Flip direction of UV coordinates inside faces"""

def uvs_rotate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_ccw: bool | None = False,
) -> None:
    """Rotate UV coordinates inside faces

    :param use_ccw: Counter Clockwise
    """

def vert_connect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Connect selected vertices of faces, splitting the face"""

def vert_connect_concave(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Make all faces convex"""

def vert_connect_nonplanar(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle_limit: float | None = 0.0872665,
) -> None:
    """Split non-planar faces that exceed the angle threshold

    :param angle_limit: Max Angle, Angle limit
    """

def vert_connect_path(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Connect vertices by their selection order, creating edges, splitting faces"""

def vertices_smooth(
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
) -> None:
    """Flatten angles of selected vertices

    :param factor: Smoothing, Smoothing factor
    :param repeat: Repeat, Number of times to smooth the mesh
    :param xaxis: X-Axis, Smooth along the X axis
    :param yaxis: Y-Axis, Smooth along the Y axis
    :param zaxis: Z-Axis, Smooth along the Z axis
    :param wait_for_input: Wait for Input
    """

def vertices_smooth_laplacian(
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
) -> None:
    """Laplacian smooth of selected vertices

    :param repeat: Number of iterations to smooth the mesh
    :param lambda_factor: Lambda factor
    :param lambda_border: Lambda factor in border
    :param use_x: Smooth X Axis, Smooth object along X axis
    :param use_y: Smooth Y Axis, Smooth object along Y axis
    :param use_z: Smooth Z Axis, Smooth object along Z axis
    :param preserve_volume: Preserve Volume, Apply volume preservation after smooth
    """

def wireframe(
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
) -> None:
    """Create a solid wireframe from faces

    :param use_boundary: Boundary, Inset face boundaries
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
    :param use_replace: Replace, Remove original faces
    :param thickness: Thickness
    :param offset: Offset
    :param use_crease: Crease, Crease hub edges for an improved subdivision surface
    :param crease_weight: Crease Weight
    """
