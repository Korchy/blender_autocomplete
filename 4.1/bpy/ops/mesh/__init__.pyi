import typing
import collections.abc
import bpy.ops.transform
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def attribute_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value_float: typing.Any | None = 0.0,
    value_float_vector_2d: typing.Any | None = (0.0, 0.0),
    value_float_vector_3d: typing.Any | None = (0.0, 0.0, 0.0),
    value_int: typing.Any | None = 0,
    value_color: typing.Any | None = (1.0, 1.0, 1.0, 1.0),
    value_bool: bool | typing.Any | None = False,
):
    """Set values of the active attribute for selected elements

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param value_float: Value
    :type value_float: typing.Any | None
    :param value_float_vector_2d: Value
    :type value_float_vector_2d: typing.Any | None
    :param value_float_vector_3d: Value
    :type value_float_vector_3d: typing.Any | None
    :param value_int: Value
    :type value_int: typing.Any | None
    :param value_color: Value
    :type value_color: typing.Any | None
    :param value_bool: Value
    :type value_bool: bool | typing.Any | None
    """

    ...

def average_normals(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    average_type: str | None = "CUSTOM_NORMAL",
    weight: typing.Any | None = 50,
    threshold: typing.Any | None = 0.01,
):
    """Average custom normals of selected vertices

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param average_type: Type, Averaging method

    CUSTOM_NORMAL
    Custom Normal -- Take average of vertex normals.

    FACE_AREA
    Face Area -- Set all vertex normals by face area.

    CORNER_ANGLE
    Corner Angle -- Set all vertex normals by corner angle.
        :type average_type: str | None
        :param weight: Weight, Weight applied per face
        :type weight: typing.Any | None
        :param threshold: Threshold, Threshold value for different weights to be considered equal
        :type threshold: typing.Any | None
    """

    ...

def beautify_fill(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    angle_limit: typing.Any | None = 3.14159,
):
    """Rearrange some faces to try to get less degenerated geometry

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param angle_limit: Max Angle, Angle limit
    :type angle_limit: typing.Any | None
    """

    ...

def bevel(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    offset_type: str | None = "OFFSET",
    offset: typing.Any | None = 0.0,
    profile_type: str | None = "SUPERELLIPSE",
    offset_pct: typing.Any | None = 0.0,
    segments: typing.Any | None = 1,
    profile: typing.Any | None = 0.5,
    affect: str | None = "EDGES",
    clamp_overlap: bool | typing.Any | None = False,
    loop_slide: bool | typing.Any | None = True,
    mark_seam: bool | typing.Any | None = False,
    mark_sharp: bool | typing.Any | None = False,
    material: typing.Any | None = -1,
    harden_normals: bool | typing.Any | None = False,
    face_strength_mode: str | None = "NONE",
    miter_outer: str | None = "SHARP",
    miter_inner: str | None = "SHARP",
    spread: typing.Any | None = 0.1,
    vmesh_method: str | None = "ADJ",
    release_confirm: bool | typing.Any | None = False,
):
    """Cut into selected items at an angle to create bevel or chamfer

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
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
        :type offset_type: str | None
        :param offset: Width, Bevel amount
        :type offset: typing.Any | None
        :param profile_type: Profile Type, The type of shape used to rebuild a beveled section

    SUPERELLIPSE
    Superellipse -- The profile can be a concave or convex curve.

    CUSTOM
    Custom -- The profile can be any arbitrary path between its endpoints.
        :type profile_type: str | None
        :param offset_pct: Width Percent, Bevel amount for percentage method
        :type offset_pct: typing.Any | None
        :param segments: Segments, Segments for curved edge
        :type segments: typing.Any | None
        :param profile: Profile, Controls profile shape (0.5 = round)
        :type profile: typing.Any | None
        :param affect: Affect, Affect edges or vertices

    VERTICES
    Vertices -- Affect only vertices.

    EDGES
    Edges -- Affect only edges.
        :type affect: str | None
        :param clamp_overlap: Clamp Overlap, Do not allow beveled edges/vertices to overlap each other
        :type clamp_overlap: bool | typing.Any | None
        :param loop_slide: Loop Slide, Prefer sliding along edges to even widths
        :type loop_slide: bool | typing.Any | None
        :param mark_seam: Mark Seams, Mark Seams along beveled edges
        :type mark_seam: bool | typing.Any | None
        :param mark_sharp: Mark Sharp, Mark beveled edges as sharp
        :type mark_sharp: bool | typing.Any | None
        :param material: Material Index, Material for bevel faces (-1 means use adjacent faces)
        :type material: typing.Any | None
        :param harden_normals: Harden Normals, Match normals of new faces to adjacent faces
        :type harden_normals: bool | typing.Any | None
        :param face_strength_mode: Face Strength Mode, Whether to set face strength, and which faces to set face strength on

    NONE
    None -- Do not set face strength.

    NEW
    New -- Set face strength on new faces only.

    AFFECTED
    Affected -- Set face strength on new and modified faces only.

    ALL
    All -- Set face strength on all faces.
        :type face_strength_mode: str | None
        :param miter_outer: Outer Miter, Pattern to use for outside of miters

    SHARP
    Sharp -- Outside of miter is sharp.

    PATCH
    Patch -- Outside of miter is squared-off patch.

    ARC
    Arc -- Outside of miter is arc.
        :type miter_outer: str | None
        :param miter_inner: Inner Miter, Pattern to use for inside of miters

    SHARP
    Sharp -- Inside of miter is sharp.

    ARC
    Arc -- Inside of miter is arc.
        :type miter_inner: str | None
        :param spread: Spread, Amount to spread arcs for arc inner miters
        :type spread: typing.Any | None
        :param vmesh_method: Vertex Mesh Method, The method to use to create meshes at intersections

    ADJ
    Grid Fill -- Default patterned fill.

    CUTOFF
    Cutoff -- A cutoff at each profile's end before the intersection.
        :type vmesh_method: str | None
        :param release_confirm: Confirm on Release
        :type release_confirm: bool | typing.Any | None
    """

    ...

def bisect(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    plane_co: typing.Any | None = (0.0, 0.0, 0.0),
    plane_no: typing.Any | None = (0.0, 0.0, 0.0),
    use_fill: bool | typing.Any | None = False,
    clear_inner: bool | typing.Any | None = False,
    clear_outer: bool | typing.Any | None = False,
    threshold: typing.Any | None = 0.0001,
    xstart: typing.Any | None = 0,
    xend: typing.Any | None = 0,
    ystart: typing.Any | None = 0,
    yend: typing.Any | None = 0,
    flip: bool | typing.Any | None = False,
    cursor: typing.Any | None = 5,
):
    """Cut geometry along a plane (click-drag to define plane)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param plane_co: Plane Point, A point on the plane
    :type plane_co: typing.Any | None
    :param plane_no: Plane Normal, The direction the plane points
    :type plane_no: typing.Any | None
    :param use_fill: Fill, Fill in the cut
    :type use_fill: bool | typing.Any | None
    :param clear_inner: Clear Inner, Remove geometry behind the plane
    :type clear_inner: bool | typing.Any | None
    :param clear_outer: Clear Outer, Remove geometry in front of the plane
    :type clear_outer: bool | typing.Any | None
    :param threshold: Axis Threshold, Preserves the existing geometry along the cut plane
    :type threshold: typing.Any | None
    :param xstart: X Start
    :type xstart: typing.Any | None
    :param xend: X End
    :type xend: typing.Any | None
    :param ystart: Y Start
    :type ystart: typing.Any | None
    :param yend: Y End
    :type yend: typing.Any | None
    :param flip: Flip
    :type flip: bool | typing.Any | None
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: typing.Any | None
    """

    ...

def blend_from_shape(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    shape: str | None = "",
    blend: typing.Any | None = 1.0,
    add: bool | typing.Any | None = True,
):
    """Blend in shape from a shape key

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param shape: Shape, Shape key to use for blending
    :type shape: str | None
    :param blend: Blend, Blending factor
    :type blend: typing.Any | None
    :param add: Add, Add rather than blend between shapes
    :type add: bool | typing.Any | None
    """

    ...

def bridge_edge_loops(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "SINGLE",
    use_merge: bool | typing.Any | None = False,
    merge_factor: typing.Any | None = 0.5,
    twist_offset: typing.Any | None = 0,
    number_cuts: typing.Any | None = 0,
    interpolation: str | None = "PATH",
    smoothness: typing.Any | None = 1.0,
    profile_shape_factor: typing.Any | None = 0.0,
    profile_shape: str | None = "SMOOTH",
):
    """Create a bridge of faces between two or more selected edge loops

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Connect Loops, Method of bridging multiple loops
    :type type: str | None
    :param use_merge: Merge, Merge rather than creating faces
    :type use_merge: bool | typing.Any | None
    :param merge_factor: Merge Factor
    :type merge_factor: typing.Any | None
    :param twist_offset: Twist, Twist offset for closed loops
    :type twist_offset: typing.Any | None
    :param number_cuts: Number of Cuts
    :type number_cuts: typing.Any | None
    :param interpolation: Interpolation, Interpolation method
    :type interpolation: str | None
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: typing.Any | None
    :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded
    :type profile_shape_factor: typing.Any | None
    :param profile_shape: Profile Shape, Shape of the profile
    :type profile_shape: str | None
    """

    ...

def colors_reverse(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Flip direction of face corner color attribute inside faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def colors_rotate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_ccw: bool | typing.Any | None = False,
):
    """Rotate face corner color attribute inside faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_ccw: Counter Clockwise
    :type use_ccw: bool | typing.Any | None
    """

    ...

def convex_hull(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    delete_unused: bool | typing.Any | None = True,
    use_existing_faces: bool | typing.Any | None = True,
    make_holes: bool | typing.Any | None = False,
    join_triangles: bool | typing.Any | None = True,
    face_threshold: typing.Any | None = 0.698132,
    shape_threshold: typing.Any | None = 0.698132,
    uvs: bool | typing.Any | None = False,
    vcols: bool | typing.Any | None = False,
    seam: bool | typing.Any | None = False,
    sharp: bool | typing.Any | None = False,
    materials: bool | typing.Any | None = False,
):
    """Enclose selected vertices in a convex polyhedron

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param delete_unused: Delete Unused, Delete selected elements that are not used by the hull
    :type delete_unused: bool | typing.Any | None
    :param use_existing_faces: Use Existing Faces, Skip hull triangles that are covered by a pre-existing face
    :type use_existing_faces: bool | typing.Any | None
    :param make_holes: Make Holes, Delete selected faces that are used by the hull
    :type make_holes: bool | typing.Any | None
    :param join_triangles: Join Triangles, Merge adjacent triangles into quads
    :type join_triangles: bool | typing.Any | None
    :param face_threshold: Max Face Angle, Face angle limit
    :type face_threshold: typing.Any | None
    :param shape_threshold: Max Shape Angle, Shape angle limit
    :type shape_threshold: typing.Any | None
    :param uvs: Compare UVs
    :type uvs: bool | typing.Any | None
    :param vcols: Compare VCols
    :type vcols: bool | typing.Any | None
    :param seam: Compare Seam
    :type seam: bool | typing.Any | None
    :param sharp: Compare Sharp
    :type sharp: bool | typing.Any | None
    :param materials: Compare Materials
    :type materials: bool | typing.Any | None
    """

    ...

def customdata_custom_splitnormals_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a custom split normals layer, if none exists yet

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def customdata_custom_splitnormals_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove the custom split normals layer, if it exists

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def customdata_mask_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Clear vertex sculpt masking data from the mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def customdata_skin_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a vertex skin layer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def customdata_skin_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Clear vertex skin layer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def decimate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    ratio: typing.Any | None = 1.0,
    use_vertex_group: bool | typing.Any | None = False,
    vertex_group_factor: typing.Any | None = 1.0,
    invert_vertex_group: bool | typing.Any | None = False,
    use_symmetry: bool | typing.Any | None = False,
    symmetry_axis: str | None = "Y",
):
    """Simplify geometry by collapsing edges

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param ratio: Ratio
    :type ratio: typing.Any | None
    :param use_vertex_group: Vertex Group, Use active vertex group as an influence
    :type use_vertex_group: bool | typing.Any | None
    :param vertex_group_factor: Weight, Vertex group strength
    :type vertex_group_factor: typing.Any | None
    :param invert_vertex_group: Invert, Invert vertex group influence
    :type invert_vertex_group: bool | typing.Any | None
    :param use_symmetry: Symmetry, Maintain symmetry on an axis
    :type use_symmetry: bool | typing.Any | None
    :param symmetry_axis: Axis, Axis of symmetry
    :type symmetry_axis: str | None
    """

    ...

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "VERT",
):
    """Delete selected vertices, edges or faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Method used for deleting mesh data
    :type type: str | None
    """

    ...

def delete_edgeloop(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_face_split: bool | typing.Any | None = True,
):
    """Delete an edge loop by merging the faces on each side

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: bool | typing.Any | None
    """

    ...

def delete_loose(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_verts: bool | typing.Any | None = True,
    use_edges: bool | typing.Any | None = True,
    use_faces: bool | typing.Any | None = False,
):
    """Delete loose vertices, edges or faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_verts: Vertices, Remove loose vertices
    :type use_verts: bool | typing.Any | None
    :param use_edges: Edges, Remove loose edges
    :type use_edges: bool | typing.Any | None
    :param use_faces: Faces, Remove loose faces
    :type use_faces: bool | typing.Any | None
    """

    ...

def dissolve_degenerate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    threshold: typing.Any | None = 0.0001,
):
    """Dissolve zero area faces and zero length edges

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Merge Distance, Maximum distance between elements to merge
    :type threshold: typing.Any | None
    """

    ...

def dissolve_edges(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_verts: bool | typing.Any | None = True,
    use_face_split: bool | typing.Any | None = False,
):
    """Dissolve edges, merging faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_verts: Dissolve Vertices, Dissolve remaining vertices
    :type use_verts: bool | typing.Any | None
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: bool | typing.Any | None
    """

    ...

def dissolve_faces(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_verts: bool | typing.Any | None = False,
):
    """Dissolve faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_verts: Dissolve Vertices, Dissolve remaining vertices
    :type use_verts: bool | typing.Any | None
    """

    ...

def dissolve_limited(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    angle_limit: typing.Any | None = 0.0872665,
    use_dissolve_boundaries: bool | typing.Any | None = False,
    delimit: typing.Any | None = {"NORMAL"},
):
    """Dissolve selected edges and vertices, limited by the angle of surrounding geometry

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param angle_limit: Max Angle, Angle limit
    :type angle_limit: typing.Any | None
    :param use_dissolve_boundaries: All Boundaries, Dissolve all vertices in between face boundaries
    :type use_dissolve_boundaries: bool | typing.Any | None
    :param delimit: Delimit, Delimit dissolve operation
    :type delimit: typing.Any | None
    """

    ...

def dissolve_mode(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_verts: bool | typing.Any | None = False,
    use_face_split: bool | typing.Any | None = False,
    use_boundary_tear: bool | typing.Any | None = False,
):
    """Dissolve geometry based on the selection mode

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_verts: Dissolve Vertices, Dissolve remaining vertices
    :type use_verts: bool | typing.Any | None
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: bool | typing.Any | None
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces
    :type use_boundary_tear: bool | typing.Any | None
    """

    ...

def dissolve_verts(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_face_split: bool | typing.Any | None = False,
    use_boundary_tear: bool | typing.Any | None = False,
):
    """Dissolve vertices, merge edges and faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: bool | typing.Any | None
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces
    :type use_boundary_tear: bool | typing.Any | None
    """

    ...

def dupli_extrude_cursor(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    rotate_source: bool | typing.Any | None = True,
):
    """Duplicate and extrude selected vertices, edges or faces towards the mouse cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param rotate_source: Rotate Source, Rotate initial selection giving better shape
    :type rotate_source: bool | typing.Any | None
    """

    ...

def duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: typing.Any | None = 1,
):
    """Duplicate selected vertices, edges or faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Any | None
    """

    ...

def duplicate_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    MESH_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Duplicate mesh and move

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_duplicate: Duplicate, Duplicate selected vertices, edges or faces
    :type MESH_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def edge_collapse(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Collapse isolated edge and face regions, merging data such as UVs and color attributes. This can collapse edge-rings as well as regions of connected faces into vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def edge_face_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add an edge or face to selected

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def edge_rotate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_ccw: bool | typing.Any | None = False,
):
    """Rotate selected edge or adjoining faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_ccw: Counter Clockwise
    :type use_ccw: bool | typing.Any | None
    """

    ...

def edge_split(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "EDGE",
):
    """Split selected edges so that each neighbor face gets its own copy

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Method to use for splitting

    EDGE
    Faces by Edges -- Split faces along selected edges.

    VERT
    Faces & Edges by Vertices -- Split faces and edges connected to selected vertices.
        :type type: str | None
    """

    ...

def edgering_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
    deselect: bool | typing.Any | None = False,
    toggle: bool | typing.Any | None = False,
    ring: bool | typing.Any | None = True,
):
    """Select an edge ring

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | typing.Any | None
    :param deselect: Deselect, Remove from the selection
    :type deselect: bool | typing.Any | None
    :param toggle: Toggle Select, Toggle the selection
    :type toggle: bool | typing.Any | None
    :param ring: Select Ring, Select ring
    :type ring: bool | typing.Any | None
    """

    ...

def edges_select_sharp(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    sharpness: typing.Any | None = 0.523599,
):
    """Select all sharp enough edges

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param sharpness: Sharpness
    :type sharpness: typing.Any | None
    """

    ...

def extrude_context(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_normal_flip: bool | typing.Any | None = False,
    use_dissolve_ortho_edges: bool | typing.Any | None = False,
    mirror: bool | typing.Any | None = False,
):
    """Extrude selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: bool | typing.Any | None
    :param use_dissolve_ortho_edges: Dissolve Orthogonal Edges
    :type use_dissolve_ortho_edges: bool | typing.Any | None
    :param mirror: Mirror Editing
    :type mirror: bool | typing.Any | None
    """

    ...

def extrude_context_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    MESH_OT_extrude_context: extrude_context | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Extrude region together along the average normal

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_context: Extrude Context, Extrude selection
    :type MESH_OT_extrude_context: extrude_context | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def extrude_edges_indiv(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_normal_flip: bool | typing.Any | None = False,
    mirror: bool | typing.Any | None = False,
):
    """Extrude individual edges only

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: bool | typing.Any | None
    :param mirror: Mirror Editing
    :type mirror: bool | typing.Any | None
    """

    ...

def extrude_edges_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    MESH_OT_extrude_edges_indiv: extrude_edges_indiv | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Extrude edges and move result

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only
    :type MESH_OT_extrude_edges_indiv: extrude_edges_indiv | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def extrude_faces_indiv(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mirror: bool | typing.Any | None = False,
):
    """Extrude individual faces only

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | typing.Any | None
    """

    ...

def extrude_faces_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    MESH_OT_extrude_faces_indiv: extrude_faces_indiv | None = None,
    TRANSFORM_OT_shrink_fatten: bpy.ops.transform.shrink_fatten | None = None,
):
    """Extrude each individual face separately along local normals

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_faces_indiv: Extrude Individual Faces, Extrude individual faces only
    :type MESH_OT_extrude_faces_indiv: extrude_faces_indiv | None
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals
    :type TRANSFORM_OT_shrink_fatten: bpy.ops.transform.shrink_fatten | None
    """

    ...

def extrude_manifold(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    MESH_OT_extrude_region: extrude_region | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Extrude, dissolves edges whose faces form a flat surface and intersect new edges

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :type MESH_OT_extrude_region: extrude_region | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def extrude_region(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_normal_flip: bool | typing.Any | None = False,
    use_dissolve_ortho_edges: bool | typing.Any | None = False,
    mirror: bool | typing.Any | None = False,
):
    """Extrude region of faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: bool | typing.Any | None
    :param use_dissolve_ortho_edges: Dissolve Orthogonal Edges
    :type use_dissolve_ortho_edges: bool | typing.Any | None
    :param mirror: Mirror Editing
    :type mirror: bool | typing.Any | None
    """

    ...

def extrude_region_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    MESH_OT_extrude_region: extrude_region | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Extrude region and move result

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :type MESH_OT_extrude_region: extrude_region | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def extrude_region_shrink_fatten(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    MESH_OT_extrude_region: extrude_region | None = None,
    TRANSFORM_OT_shrink_fatten: bpy.ops.transform.shrink_fatten | None = None,
):
    """Extrude region together along local normals

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :type MESH_OT_extrude_region: extrude_region | None
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals
    :type TRANSFORM_OT_shrink_fatten: bpy.ops.transform.shrink_fatten | None
    """

    ...

def extrude_repeat(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    steps: typing.Any | None = 10,
    offset: typing.Any | None = (0.0, 0.0, 0.0),
    scale_offset: typing.Any | None = 1.0,
):
    """Extrude selected vertices, edges or faces repeatedly

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param steps: Steps
    :type steps: typing.Any | None
    :param offset: Offset, Offset vector
    :type offset: typing.Any | None
    :param scale_offset: Scale Offset
    :type scale_offset: typing.Any | None
    """

    ...

def extrude_vertices_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    MESH_OT_extrude_verts_indiv: extrude_verts_indiv | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Extrude vertices and move result

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_verts_indiv: Extrude Only Vertices, Extrude individual vertices only
    :type MESH_OT_extrude_verts_indiv: extrude_verts_indiv | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def extrude_verts_indiv(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mirror: bool | typing.Any | None = False,
):
    """Extrude individual vertices only

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | typing.Any | None
    """

    ...

def face_make_planar(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 1.0,
    repeat: typing.Any | None = 1,
):
    """Flatten selected faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor
    :type factor: typing.Any | None
    :param repeat: Iterations
    :type repeat: typing.Any | None
    """

    ...

def face_set_extract(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    add_boundary_loop: bool | typing.Any | None = True,
    smooth_iterations: typing.Any | None = 4,
    apply_shrinkwrap: bool | typing.Any | None = True,
    add_solidify: bool | typing.Any | None = True,
):
    """Create a new mesh object from the selected Face Set

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param add_boundary_loop: Add Boundary Loop, Add an extra edge loop to better preserve the shape when applying a subdivision surface modifier
    :type add_boundary_loop: bool | typing.Any | None
    :param smooth_iterations: Smooth Iterations, Smooth iterations applied to the extracted mesh
    :type smooth_iterations: typing.Any | None
    :param apply_shrinkwrap: Project to Sculpt, Project the extracted mesh into the original sculpt
    :type apply_shrinkwrap: bool | typing.Any | None
    :param add_solidify: Extract as Solid, Extract the mask as a solid object with a solidify modifier
    :type add_solidify: bool | typing.Any | None
    """

    ...

def face_split_by_edges(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Weld loose edges into faces (splitting them into new faces)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def faces_mirror_uv(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    direction: str | None = "POSITIVE",
    precision: typing.Any | None = 3,
):
    """Copy mirror UV coordinates on the X axis based on a mirrored mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Axis Direction
    :type direction: str | None
    :param precision: Precision, Tolerance for finding vertex duplicates
    :type precision: typing.Any | None
    """

    ...

def faces_select_linked_flat(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    sharpness: typing.Any | None = 0.0174533,
):
    """Select linked faces by angle

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param sharpness: Sharpness
    :type sharpness: typing.Any | None
    """

    ...

def faces_shade_flat(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Display faces flat

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def faces_shade_smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Display faces smooth (using vertex normals)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def fill(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_beauty: bool | typing.Any | None = True,
):
    """Fill a selected edge loop with faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_beauty: Beauty, Use best triangulation division
    :type use_beauty: bool | typing.Any | None
    """

    ...

def fill_grid(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    span: typing.Any | None = 1,
    offset: typing.Any | None = 0,
    use_interp_simple: bool | typing.Any | None = False,
):
    """Fill grid from two loops

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param span: Span, Number of grid columns
    :type span: typing.Any | None
    :param offset: Offset, Vertex that is the corner of the grid
    :type offset: typing.Any | None
    :param use_interp_simple: Simple Blending, Use simple interpolation of grid vertices
    :type use_interp_simple: bool | typing.Any | None
    """

    ...

def fill_holes(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    sides: typing.Any | None = 4,
):
    """Fill in holes (boundary edge loops)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param sides: Sides, Number of sides in hole required to fill (zero fills all holes)
    :type sides: typing.Any | None
    """

    ...

def flip_normals(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    only_clnors: bool | typing.Any | None = False,
):
    """Flip the direction of selected faces' normals (and of their vertices)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_clnors: Custom Normals Only, Only flip the custom loop normals of the selected elements
    :type only_clnors: bool | typing.Any | None
    """

    ...

def flip_quad_tessellation(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Flips the tessellation of selected quads

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def hide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselected: bool | typing.Any | None = False,
):
    """Hide (un)selected vertices, edges or faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: bool | typing.Any | None
    """

    ...

def inset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_boundary: bool | typing.Any | None = True,
    use_even_offset: bool | typing.Any | None = True,
    use_relative_offset: bool | typing.Any | None = False,
    use_edge_rail: bool | typing.Any | None = False,
    thickness: typing.Any | None = 0.0,
    depth: typing.Any | None = 0.0,
    use_outset: bool | typing.Any | None = False,
    use_select_inset: bool | typing.Any | None = False,
    use_individual: bool | typing.Any | None = False,
    use_interpolate: bool | typing.Any | None = True,
    release_confirm: bool | typing.Any | None = False,
):
    """Inset new faces into selected faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_boundary: Boundary, Inset face boundaries
    :type use_boundary: bool | typing.Any | None
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :type use_even_offset: bool | typing.Any | None
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
    :type use_relative_offset: bool | typing.Any | None
    :param use_edge_rail: Edge Rail, Inset the region along existing edges
    :type use_edge_rail: bool | typing.Any | None
    :param thickness: Thickness
    :type thickness: typing.Any | None
    :param depth: Depth
    :type depth: typing.Any | None
    :param use_outset: Outset, Outset rather than inset
    :type use_outset: bool | typing.Any | None
    :param use_select_inset: Select Outer, Select the new inset faces
    :type use_select_inset: bool | typing.Any | None
    :param use_individual: Individual, Individual face inset
    :type use_individual: bool | typing.Any | None
    :param use_interpolate: Interpolate, Blend face data across the inset
    :type use_interpolate: bool | typing.Any | None
    :param release_confirm: Confirm on Release
    :type release_confirm: bool | typing.Any | None
    """

    ...

def intersect(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "SELECT_UNSELECT",
    separate_mode: str | None = "CUT",
    threshold: typing.Any | None = 1e-06,
    solver: str | None = "EXACT",
):
    """Cut an intersection into faces

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Source

    SELECT
    Self Intersect -- Self intersect selected faces.

    SELECT_UNSELECT
    Selected/Unselected -- Intersect selected with unselected faces.
        :type mode: str | None
        :param separate_mode: Separate Mode

    ALL
    All -- Separate all geometry from intersections.

    CUT
    Cut -- Cut into geometry keeping each side separate (Selected/Unselected only).

    NONE
    Merge -- Merge all geometry from the intersection.
        :type separate_mode: str | None
        :param threshold: Merge Threshold
        :type threshold: typing.Any | None
        :param solver: Solver, Which Intersect solver to use

    FAST
    Fast -- Faster solver, some limitations.

    EXACT
    Exact -- Exact solver, slower, handles more cases.
        :type solver: str | None
    """

    ...

def intersect_boolean(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    operation: str | None = "DIFFERENCE",
    use_swap: bool | typing.Any | None = False,
    use_self: bool | typing.Any | None = False,
    threshold: typing.Any | None = 1e-06,
    solver: str | None = "EXACT",
):
    """Cut solid geometry from selected to unselected

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param operation: Boolean Operation, Which boolean operation to apply
        :type operation: str | None
        :param use_swap: Swap, Use with difference intersection to swap which side is kept
        :type use_swap: bool | typing.Any | None
        :param use_self: Self Intersection, Do self-union or self-intersection
        :type use_self: bool | typing.Any | None
        :param threshold: Merge Threshold
        :type threshold: typing.Any | None
        :param solver: Solver, Which Boolean solver to use

    FAST
    Fast -- Faster solver, some limitations.

    EXACT
    Exact -- Exact solver, slower, handles more cases.
        :type solver: str | None
    """

    ...

def knife_project(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    cut_through: bool | typing.Any | None = False,
):
    """Use other objects outlines and boundaries to project knife cuts

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param cut_through: Cut Through, Cut through all faces, not just visible ones
    :type cut_through: bool | typing.Any | None
    """

    ...

def knife_tool(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_occlude_geometry: bool | typing.Any | None = True,
    only_selected: bool | typing.Any | None = False,
    xray: bool | typing.Any | None = True,
    visible_measurements: str | None = "NONE",
    angle_snapping: str | None = "NONE",
    angle_snapping_increment: typing.Any | None = 0.523599,
    wait_for_input: bool | typing.Any | None = True,
):
    """Cut new topology

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param use_occlude_geometry: Occlude Geometry, Only cut the front most geometry
        :type use_occlude_geometry: bool | typing.Any | None
        :param only_selected: Only Selected, Only cut selected geometry
        :type only_selected: bool | typing.Any | None
        :param xray: X-Ray, Show cuts hidden by geometry
        :type xray: bool | typing.Any | None
        :param visible_measurements: Measurements, Visible distance and angle measurements

    NONE
    None -- Show no measurements.

    BOTH
    Both -- Show both distances and angles.

    DISTANCE
    Distance -- Show just distance measurements.

    ANGLE
    Angle -- Show just angle measurements.
        :type visible_measurements: str | None
        :param angle_snapping: Angle Snapping, Angle snapping mode

    NONE
    None -- No angle snapping.

    SCREEN
    Screen -- Screen space angle snapping.

    RELATIVE
    Relative -- Angle snapping relative to the previous cut edge.
        :type angle_snapping: str | None
        :param angle_snapping_increment: Angle Snap Increment, The angle snap increment used when in constrained angle mode
        :type angle_snapping_increment: typing.Any | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | typing.Any | None
    """

    ...

def loop_multi_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    ring: bool | typing.Any | None = False,
):
    """Select a loop of connected edges by connection type

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param ring: Ring
    :type ring: bool | typing.Any | None
    """

    ...

def loop_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
    deselect: bool | typing.Any | None = False,
    toggle: bool | typing.Any | None = False,
    ring: bool | typing.Any | None = False,
):
    """Select a loop of connected edges

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend Select, Extend the selection
    :type extend: bool | typing.Any | None
    :param deselect: Deselect, Remove from the selection
    :type deselect: bool | typing.Any | None
    :param toggle: Toggle Select, Toggle the selection
    :type toggle: bool | typing.Any | None
    :param ring: Select Ring, Select ring
    :type ring: bool | typing.Any | None
    """

    ...

def loop_to_region(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    select_bigger: bool | typing.Any | None = False,
):
    """Select region of faces inside of a selected loop of edges

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select_bigger: Select Bigger, Select bigger regions instead of smaller ones
    :type select_bigger: bool | typing.Any | None
    """

    ...

def loopcut(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    number_cuts: typing.Any | None = 1,
    smoothness: typing.Any | None = 0.0,
    falloff: str | None = "INVERSE_SQUARE",
    object_index: typing.Any | None = -1,
    edge_index: typing.Any | None = -1,
    mesh_select_mode_init: list[bool] | typing.Any | None = (False, False, False),
):
    """Add a new loop between existing loops

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param number_cuts: Number of Cuts
    :type number_cuts: typing.Any | None
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: typing.Any | None
    :param falloff: Falloff, Falloff type of the feather
    :type falloff: str | None
    :param object_index: Object Index
    :type object_index: typing.Any | None
    :param edge_index: Edge Index
    :type edge_index: typing.Any | None
    :type mesh_select_mode_init: list[bool] | typing.Any | None
    """

    ...

def loopcut_slide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    MESH_OT_loopcut: loopcut | None = None,
    TRANSFORM_OT_edge_slide: bpy.ops.transform.edge_slide | None = None,
):
    """Cut mesh loop and slide it

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_loopcut: Loop Cut, Add a new loop between existing loops
    :type MESH_OT_loopcut: loopcut | None
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh
    :type TRANSFORM_OT_edge_slide: bpy.ops.transform.edge_slide | None
    """

    ...

def mark_freestyle_edge(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    clear: bool | typing.Any | None = False,
):
    """(Un)mark selected edges as Freestyle feature edges

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear
    :type clear: bool | typing.Any | None
    """

    ...

def mark_freestyle_face(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    clear: bool | typing.Any | None = False,
):
    """(Un)mark selected faces for exclusion from Freestyle feature edge detection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear
    :type clear: bool | typing.Any | None
    """

    ...

def mark_seam(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    clear: bool | typing.Any | None = False,
):
    """(Un)mark selected edges as a seam

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear
    :type clear: bool | typing.Any | None
    """

    ...

def mark_sharp(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    clear: bool | typing.Any | None = False,
    use_verts: bool | typing.Any | None = False,
):
    """(Un)mark selected edges as sharp

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear
    :type clear: bool | typing.Any | None
    :param use_verts: Vertices, Consider vertices instead of edges to select which edges to (un)tag as sharp
    :type use_verts: bool | typing.Any | None
    """

    ...

def merge(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "CENTER",
    uvs: bool | typing.Any | None = False,
):
    """Merge selected vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Merge method to use
    :type type: str | None
    :param uvs: UVs, Move UVs according to merge
    :type uvs: bool | typing.Any | None
    """

    ...

def merge_normals(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Merge custom normals of selected vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def mod_weighted_strength(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    set: bool | typing.Any | None = False,
    face_strength: str | None = "MEDIUM",
):
    """Set/Get strength of face (used in Weighted Normal modifier)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param set: Set Value, Set value of faces
    :type set: bool | typing.Any | None
    :param face_strength: Face Strength, Strength to use for assigning or selecting face influence for weighted normal modifier
    :type face_strength: str | None
    """

    ...

def normals_make_consistent(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    inside: bool | typing.Any | None = False,
):
    """Make face and vertex normals point either outside or inside the mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param inside: Inside
    :type inside: bool | typing.Any | None
    """

    ...

def normals_tools(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "COPY",
    absolute: bool | typing.Any | None = False,
):
    """Custom normals tools using Normal Vector of UI

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
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
        :type mode: str | None
        :param absolute: Absolute Coordinates, Copy Absolute coordinates or Normal vector
        :type absolute: bool | typing.Any | None
    """

    ...

def offset_edge_loops(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_cap_endpoint: bool | typing.Any | None = False,
):
    """Create offset edge loop from the current selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_cap_endpoint: Cap Endpoint, Extend loop around end-points
    :type use_cap_endpoint: bool | typing.Any | None
    """

    ...

def offset_edge_loops_slide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    MESH_OT_offset_edge_loops: offset_edge_loops | None = None,
    TRANSFORM_OT_edge_slide: bpy.ops.transform.edge_slide | None = None,
):
    """Offset edge loop slide

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_offset_edge_loops: Offset Edge Loop, Create offset edge loop from the current selection
    :type MESH_OT_offset_edge_loops: offset_edge_loops | None
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh
    :type TRANSFORM_OT_edge_slide: bpy.ops.transform.edge_slide | None
    """

    ...

def paint_mask_extract(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mask_threshold: typing.Any | None = 0.5,
    add_boundary_loop: bool | typing.Any | None = True,
    smooth_iterations: typing.Any | None = 4,
    apply_shrinkwrap: bool | typing.Any | None = True,
    add_solidify: bool | typing.Any | None = True,
):
    """Create a new mesh object from the current paint mask

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mask_threshold: Threshold, Minimum mask value to consider the vertex valid to extract a face from the original mesh
    :type mask_threshold: typing.Any | None
    :param add_boundary_loop: Add Boundary Loop, Add an extra edge loop to better preserve the shape when applying a subdivision surface modifier
    :type add_boundary_loop: bool | typing.Any | None
    :param smooth_iterations: Smooth Iterations, Smooth iterations applied to the extracted mesh
    :type smooth_iterations: typing.Any | None
    :param apply_shrinkwrap: Project to Sculpt, Project the extracted mesh into the original sculpt
    :type apply_shrinkwrap: bool | typing.Any | None
    :param add_solidify: Extract as Solid, Extract the mask as a solid object with a solidify modifier
    :type add_solidify: bool | typing.Any | None
    """

    ...

def paint_mask_slice(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mask_threshold: typing.Any | None = 0.5,
    fill_holes: bool | typing.Any | None = True,
    new_object: bool | typing.Any | None = True,
):
    """Slices the paint mask from the mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mask_threshold: Threshold, Minimum mask value to consider the vertex valid to extract a face from the original mesh
    :type mask_threshold: typing.Any | None
    :param fill_holes: Fill Holes, Fill holes after slicing the mask
    :type fill_holes: bool | typing.Any | None
    :param new_object: Slice to New Object, Create a new object from the sliced mask
    :type new_object: bool | typing.Any | None
    """

    ...

def point_normals(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "COORDINATES",
    invert: bool | typing.Any | None = False,
    align: bool | typing.Any | None = False,
    target_location: typing.Any | None = (0.0, 0.0, 0.0),
    spherize: bool | typing.Any | None = False,
    spherize_strength: typing.Any | None = 0.1,
):
    """Point selected custom normals to specified Target

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode, How to define coordinates to point custom normals to

    COORDINATES
    Coordinates -- Use static coordinates (defined by various means).

    MOUSE
    Mouse -- Follow mouse cursor.
        :type mode: str | None
        :param invert: Invert, Invert affected normals
        :type invert: bool | typing.Any | None
        :param align: Align, Make all affected normals parallel
        :type align: bool | typing.Any | None
        :param target_location: Target, Target location to which normals will point
        :type target_location: typing.Any | None
        :param spherize: Spherize, Interpolate between original and new normals
        :type spherize: bool | typing.Any | None
        :param spherize_strength: Spherize Strength, Ratio of spherized normal to original normal
        :type spherize_strength: typing.Any | None
    """

    ...

def poke(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    offset: typing.Any | None = 0.0,
    use_relative_offset: bool | typing.Any | None = False,
    center_mode: str | None = "MEDIAN_WEIGHTED",
):
    """Split a face into a fan

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param offset: Poke Offset, Poke Offset
        :type offset: typing.Any | None
        :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
        :type use_relative_offset: bool | typing.Any | None
        :param center_mode: Poke Center, Poke face center calculation

    MEDIAN_WEIGHTED
    Weighted Median -- Weighted median face center.

    MEDIAN
    Median -- Median face center.

    BOUNDS
    Bounds -- Face bounds center.
        :type center_mode: str | None
    """

    ...

def polybuild_delete_at_cursor(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mirror: bool | typing.Any | None = False,
    use_proportional_edit: bool | typing.Any | None = False,
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    use_proportional_connected: bool | typing.Any | None = False,
    use_proportional_projected: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
    use_accurate: bool | typing.Any | None = False,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | typing.Any | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | typing.Any | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: str | None
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Any | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | typing.Any | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | typing.Any | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | typing.Any | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | typing.Any | None
    """

    ...

def polybuild_dissolve_at_cursor(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def polybuild_extrude_at_cursor_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    MESH_OT_polybuild_transform_at_cursor: polybuild_transform_at_cursor | None = None,
    MESH_OT_extrude_edges_indiv: extrude_edges_indiv | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor
    :type MESH_OT_polybuild_transform_at_cursor: polybuild_transform_at_cursor | None
    :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only
    :type MESH_OT_extrude_edges_indiv: extrude_edges_indiv | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def polybuild_face_at_cursor(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    create_quads: bool | typing.Any | None = True,
    mirror: bool | typing.Any | None = False,
    use_proportional_edit: bool | typing.Any | None = False,
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    use_proportional_connected: bool | typing.Any | None = False,
    use_proportional_projected: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
    use_accurate: bool | typing.Any | None = False,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param create_quads: Create Quads, Automatically split edges in triangles to maintain quad topology
    :type create_quads: bool | typing.Any | None
    :param mirror: Mirror Editing
    :type mirror: bool | typing.Any | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | typing.Any | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: str | None
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Any | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | typing.Any | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | typing.Any | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | typing.Any | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | typing.Any | None
    """

    ...

def polybuild_face_at_cursor_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    MESH_OT_polybuild_face_at_cursor: polybuild_face_at_cursor | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_polybuild_face_at_cursor: Poly Build Face at Cursor
    :type MESH_OT_polybuild_face_at_cursor: polybuild_face_at_cursor | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def polybuild_split_at_cursor(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mirror: bool | typing.Any | None = False,
    use_proportional_edit: bool | typing.Any | None = False,
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    use_proportional_connected: bool | typing.Any | None = False,
    use_proportional_projected: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
    use_accurate: bool | typing.Any | None = False,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | typing.Any | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | typing.Any | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: str | None
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Any | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | typing.Any | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | typing.Any | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | typing.Any | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | typing.Any | None
    """

    ...

def polybuild_split_at_cursor_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    MESH_OT_polybuild_split_at_cursor: polybuild_split_at_cursor | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_polybuild_split_at_cursor: Poly Build Split at Cursor
    :type MESH_OT_polybuild_split_at_cursor: polybuild_split_at_cursor | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def polybuild_transform_at_cursor(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mirror: bool | typing.Any | None = False,
    use_proportional_edit: bool | typing.Any | None = False,
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    use_proportional_connected: bool | typing.Any | None = False,
    use_proportional_projected: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
    use_accurate: bool | typing.Any | None = False,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | typing.Any | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | typing.Any | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: str | None
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Any | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | typing.Any | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | typing.Any | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | typing.Any | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | typing.Any | None
    """

    ...

def polybuild_transform_at_cursor_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    MESH_OT_polybuild_transform_at_cursor: polybuild_transform_at_cursor | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor
    :type MESH_OT_polybuild_transform_at_cursor: polybuild_transform_at_cursor | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def primitive_circle_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    vertices: typing.Any | None = 32,
    radius: typing.Any | None = 1.0,
    fill_type: str | None = "NOTHING",
    calc_uvs: bool | typing.Any | None = True,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    scale: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Construct a circle mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param vertices: Vertices
        :type vertices: typing.Any | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param fill_type: Fill Type

    NOTHING
    Nothing -- Don't fill at all.

    NGON
    N-Gon -- Use n-gons.

    TRIFAN
    Triangle Fan -- Use triangle fans.
        :type fill_type: str | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | typing.Any | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
        :param scale: Scale, Scale for the newly added object
        :type scale: typing.Any | None
    """

    ...

def primitive_cone_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    vertices: typing.Any | None = 32,
    radius1: typing.Any | None = 1.0,
    radius2: typing.Any | None = 0.0,
    depth: typing.Any | None = 2.0,
    end_fill_type: str | None = "NGON",
    calc_uvs: bool | typing.Any | None = True,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    scale: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Construct a conic mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param vertices: Vertices
        :type vertices: typing.Any | None
        :param radius1: Radius 1
        :type radius1: typing.Any | None
        :param radius2: Radius 2
        :type radius2: typing.Any | None
        :param depth: Depth
        :type depth: typing.Any | None
        :param end_fill_type: Base Fill Type

    NOTHING
    Nothing -- Don't fill at all.

    NGON
    N-Gon -- Use n-gons.

    TRIFAN
    Triangle Fan -- Use triangle fans.
        :type end_fill_type: str | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | typing.Any | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
        :param scale: Scale, Scale for the newly added object
        :type scale: typing.Any | None
    """

    ...

def primitive_cube_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    size: typing.Any | None = 2.0,
    calc_uvs: bool | typing.Any | None = True,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    scale: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Construct a cube mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param size: Size
        :type size: typing.Any | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | typing.Any | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
        :param scale: Scale, Scale for the newly added object
        :type scale: typing.Any | None
    """

    ...

def primitive_cube_add_gizmo(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    calc_uvs: bool | typing.Any | None = True,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    scale: typing.Any | None = (0.0, 0.0, 0.0),
    matrix: typing.Any | None = (
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
    ),
):
    """Construct a cube mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | typing.Any | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
        :param scale: Scale, Scale for the newly added object
        :type scale: typing.Any | None
        :param matrix: Matrix
        :type matrix: typing.Any | None
    """

    ...

def primitive_cylinder_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    vertices: typing.Any | None = 32,
    radius: typing.Any | None = 1.0,
    depth: typing.Any | None = 2.0,
    end_fill_type: str | None = "NGON",
    calc_uvs: bool | typing.Any | None = True,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    scale: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Construct a cylinder mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param vertices: Vertices
        :type vertices: typing.Any | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param depth: Depth
        :type depth: typing.Any | None
        :param end_fill_type: Cap Fill Type

    NOTHING
    Nothing -- Don't fill at all.

    NGON
    N-Gon -- Use n-gons.

    TRIFAN
    Triangle Fan -- Use triangle fans.
        :type end_fill_type: str | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | typing.Any | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
        :param scale: Scale, Scale for the newly added object
        :type scale: typing.Any | None
    """

    ...

def primitive_grid_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    x_subdivisions: typing.Any | None = 10,
    y_subdivisions: typing.Any | None = 10,
    size: typing.Any | None = 2.0,
    calc_uvs: bool | typing.Any | None = True,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    scale: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Construct a grid mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param x_subdivisions: X Subdivisions
        :type x_subdivisions: typing.Any | None
        :param y_subdivisions: Y Subdivisions
        :type y_subdivisions: typing.Any | None
        :param size: Size
        :type size: typing.Any | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | typing.Any | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
        :param scale: Scale, Scale for the newly added object
        :type scale: typing.Any | None
    """

    ...

def primitive_ico_sphere_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    subdivisions: typing.Any | None = 2,
    radius: typing.Any | None = 1.0,
    calc_uvs: bool | typing.Any | None = True,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    scale: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Construct an Icosphere mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param subdivisions: Subdivisions
        :type subdivisions: typing.Any | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | typing.Any | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
        :param scale: Scale, Scale for the newly added object
        :type scale: typing.Any | None
    """

    ...

def primitive_monkey_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    size: typing.Any | None = 2.0,
    calc_uvs: bool | typing.Any | None = True,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    scale: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Construct a Suzanne mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param size: Size
        :type size: typing.Any | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | typing.Any | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
        :param scale: Scale, Scale for the newly added object
        :type scale: typing.Any | None
    """

    ...

def primitive_plane_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    size: typing.Any | None = 2.0,
    calc_uvs: bool | typing.Any | None = True,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    scale: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Construct a filled planar mesh with 4 vertices

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param size: Size
        :type size: typing.Any | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | typing.Any | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
        :param scale: Scale, Scale for the newly added object
        :type scale: typing.Any | None
    """

    ...

def primitive_torus_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    major_segments: typing.Any | None = 48,
    minor_segments: typing.Any | None = 12,
    mode: str | None = "MAJOR_MINOR",
    major_radius: typing.Any | None = 1.0,
    minor_radius: typing.Any | None = 0.25,
    abso_major_rad: typing.Any | None = 1.25,
    abso_minor_rad: typing.Any | None = 0.75,
    generate_uvs: bool | typing.Any | None = True,
):
    """Construct a torus mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param align: Align

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location
        :type location: typing.Any | None
        :param rotation: Rotation
        :type rotation: typing.Any | None
        :param major_segments: Major Segments, Number of segments for the main ring of the torus
        :type major_segments: typing.Any | None
        :param minor_segments: Minor Segments, Number of segments for the minor ring of the torus
        :type minor_segments: typing.Any | None
        :param mode: Dimensions Mode

    MAJOR_MINOR
    Major/Minor -- Use the major/minor radii for torus dimensions.

    EXT_INT
    Exterior/Interior -- Use the exterior/interior radii for torus dimensions.
        :type mode: str | None
        :param major_radius: Major Radius, Radius from the origin to the center of the cross sections
        :type major_radius: typing.Any | None
        :param minor_radius: Minor Radius, Radius of the torus' cross section
        :type minor_radius: typing.Any | None
        :param abso_major_rad: Exterior Radius, Total Exterior Radius of the torus
        :type abso_major_rad: typing.Any | None
        :param abso_minor_rad: Interior Radius, Total Interior Radius of the torus
        :type abso_minor_rad: typing.Any | None
        :param generate_uvs: Generate UVs, Generate a default UV map
        :type generate_uvs: bool | typing.Any | None
    """

    ...

def primitive_uv_sphere_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    segments: typing.Any | None = 32,
    ring_count: typing.Any | None = 16,
    radius: typing.Any | None = 1.0,
    calc_uvs: bool | typing.Any | None = True,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    scale: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Construct a UV sphere mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param segments: Segments
        :type segments: typing.Any | None
        :param ring_count: Rings
        :type ring_count: typing.Any | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | typing.Any | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
        :param scale: Scale, Scale for the newly added object
        :type scale: typing.Any | None
    """

    ...

def quads_convert_to_tris(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    quad_method: str | None = "BEAUTY",
    ngon_method: str | None = "BEAUTY",
):
    """Triangulate selected faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param quad_method: Quad Method, Method for splitting the quads into triangles
    :type quad_method: str | None
    :param ngon_method: N-gon Method, Method for splitting the n-gons into triangles
    :type ngon_method: str | None
    """

    ...

def region_to_loop(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select boundary edges around the selected faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def remove_doubles(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    threshold: typing.Any | None = 0.0001,
    use_unselected: bool | typing.Any | None = False,
    use_sharp_edge_from_normals: bool | typing.Any | None = False,
):
    """Merge vertices based on their proximity

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Merge Distance, Maximum distance between elements to merge
    :type threshold: typing.Any | None
    :param use_unselected: Unselected, Merge selected to other unselected vertices
    :type use_unselected: bool | typing.Any | None
    :param use_sharp_edge_from_normals: Sharp Edges, Calculate sharp edges using custom normal data (when available)
    :type use_sharp_edge_from_normals: bool | typing.Any | None
    """

    ...

def reveal(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    select: bool | typing.Any | None = True,
):
    """Reveal all hidden vertices, edges and faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | typing.Any | None
    """

    ...

def rip(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mirror: bool | typing.Any | None = False,
    use_proportional_edit: bool | typing.Any | None = False,
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    use_proportional_connected: bool | typing.Any | None = False,
    use_proportional_projected: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
    use_accurate: bool | typing.Any | None = False,
    use_fill: bool | typing.Any | None = False,
):
    """Disconnect vertex or edges from connected geometry

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | typing.Any | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | typing.Any | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: str | None
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Any | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | typing.Any | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | typing.Any | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | typing.Any | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | typing.Any | None
    :param use_fill: Fill, Fill the ripped region
    :type use_fill: bool | typing.Any | None
    """

    ...

def rip_edge(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mirror: bool | typing.Any | None = False,
    use_proportional_edit: bool | typing.Any | None = False,
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    use_proportional_connected: bool | typing.Any | None = False,
    use_proportional_projected: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
    use_accurate: bool | typing.Any | None = False,
):
    """Extend vertices along the edge closest to the cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | typing.Any | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | typing.Any | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: str | None
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Any | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | typing.Any | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | typing.Any | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | typing.Any | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | typing.Any | None
    """

    ...

def rip_edge_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    MESH_OT_rip_edge: rip_edge | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Extend vertices and move the result

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_rip_edge: Extend Vertices, Extend vertices along the edge closest to the cursor
    :type MESH_OT_rip_edge: rip_edge | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def rip_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    MESH_OT_rip: rip | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Rip polygons and move the result

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_rip: Rip, Disconnect vertex or edges from connected geometry
    :type MESH_OT_rip: rip | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def screw(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    steps: typing.Any | None = 9,
    turns: typing.Any | None = 1,
    center: typing.Any | None = (0.0, 0.0, 0.0),
    axis: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Extrude selected vertices in screw-shaped rotation around the cursor in indicated viewport

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param steps: Steps, Steps
    :type steps: typing.Any | None
    :param turns: Turns, Turns
    :type turns: typing.Any | None
    :param center: Center, Center in global view space
    :type center: typing.Any | None
    :param axis: Axis, Axis in global view space
    :type axis: typing.Any | None
    """

    ...

def select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: str | None = "TOGGLE",
):
    """(De)select all vertices, edges or faces

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
        :type action: str | None
    """

    ...

def select_axis(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    orientation: str | None = "LOCAL",
    sign: str | None = "POS",
    axis: str | None = "X",
    threshold: typing.Any | None = 0.0001,
):
    """Select all data in the mesh on a single axis

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param orientation: Axis Mode, Axis orientation
    :type orientation: str | None
    :param sign: Axis Sign, Side to select
    :type sign: str | None
    :param axis: Axis, Select the axis to compare each vertex on
    :type axis: str | None
    :param threshold: Threshold
    :type threshold: typing.Any | None
    """

    ...

def select_by_attribute(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select elements based on the active boolean attribute

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_face_by_sides(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    number: typing.Any | None = 4,
    type: str | None = "EQUAL",
    extend: bool | typing.Any | None = True,
):
    """Select vertices or faces by the number of face sides

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param number: Number of Vertices
    :type number: typing.Any | None
    :param type: Type, Type of comparison to make
    :type type: str | None
    :param extend: Extend, Extend the selection
    :type extend: bool | typing.Any | None
    """

    ...

def select_interior_faces(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select faces where all edges have more than 2 face users

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_less(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_face_step: bool | typing.Any | None = True,
):
    """Deselect vertices, edges or faces at the boundary of each selection region

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_step: Face Step, Connected faces (instead of edges)
    :type use_face_step: bool | typing.Any | None
    """

    ...

def select_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    delimit: typing.Any | None = {"SEAM"},
):
    """Select all vertices connected to the current selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param delimit: Delimit, Delimit selected region
    :type delimit: typing.Any | None
    """

    ...

def select_linked_pick(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    deselect: bool | typing.Any | None = False,
    delimit: typing.Any | None = {"SEAM"},
    object_index: typing.Any | None = -1,
    index: typing.Any | None = -1,
):
    """(De)select all vertices linked to the edge under the mouse cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param deselect: Deselect
    :type deselect: bool | typing.Any | None
    :param delimit: Delimit, Delimit selected region
    :type delimit: typing.Any | None
    :type object_index: typing.Any | None
    :type index: typing.Any | None
    """

    ...

def select_loose(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
):
    """Select loose geometry based on the selection mode

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | typing.Any | None
    """

    ...

def select_mirror(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    axis: typing.Any | None = {"X"},
    extend: bool | typing.Any | None = False,
):
    """Select mesh items at mirrored locations

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param axis: Axis
    :type axis: typing.Any | None
    :param extend: Extend, Extend the existing selection
    :type extend: bool | typing.Any | None
    """

    ...

def select_mode(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_extend: bool | typing.Any | None = False,
    use_expand: bool | typing.Any | None = False,
    type: str | None = "VERT",
    action: str | None = "TOGGLE",
):
    """Change selection mode

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param use_extend: Extend
        :type use_extend: bool | typing.Any | None
        :param use_expand: Expand
        :type use_expand: bool | typing.Any | None
        :param type: Type
        :type type: str | None
        :param action: Action, Selection action to execute

    DISABLE
    Disable -- Disable selected markers.

    ENABLE
    Enable -- Enable selected markers.

    TOGGLE
    Toggle -- Toggle disabled flag for selected markers.
        :type action: str | None
    """

    ...

def select_more(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_face_step: bool | typing.Any | None = True,
):
    """Select more vertices, edges or faces connected to initial selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_step: Face Step, Connected faces (instead of edges)
    :type use_face_step: bool | typing.Any | None
    """

    ...

def select_next_item(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select the next element (using selection order)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_non_manifold(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = True,
    use_wire: bool | typing.Any | None = True,
    use_boundary: bool | typing.Any | None = True,
    use_multi_face: bool | typing.Any | None = True,
    use_non_contiguous: bool | typing.Any | None = True,
    use_verts: bool | typing.Any | None = True,
):
    """Select all non-manifold vertices or edges

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | typing.Any | None
    :param use_wire: Wire, Wire edges
    :type use_wire: bool | typing.Any | None
    :param use_boundary: Boundaries, Boundary edges
    :type use_boundary: bool | typing.Any | None
    :param use_multi_face: Multiple Faces, Edges shared by more than two faces
    :type use_multi_face: bool | typing.Any | None
    :param use_non_contiguous: Non Contiguous, Edges between faces pointing in alternate directions
    :type use_non_contiguous: bool | typing.Any | None
    :param use_verts: Vertices, Vertices connecting multiple face regions
    :type use_verts: bool | typing.Any | None
    """

    ...

def select_nth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    skip: typing.Any | None = 1,
    nth: typing.Any | None = 1,
    offset: typing.Any | None = 0,
):
    """Deselect every Nth element starting from the active vertex, edge or face

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: typing.Any | None
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: typing.Any | None
    :param offset: Offset, Offset from the starting point
    :type offset: typing.Any | None
    """

    ...

def select_prev_item(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select the previous element (using selection order)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_random(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    ratio: typing.Any | None = 0.5,
    seed: typing.Any | None = 0,
    action: str | None = "SELECT",
):
    """Randomly select vertices

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param ratio: Ratio, Portion of items to select randomly
        :type ratio: typing.Any | None
        :param seed: Random Seed, Seed for the random number generator
        :type seed: typing.Any | None
        :param action: Action, Selection action to execute

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.
        :type action: str | None
    """

    ...

def select_similar(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "VERT_NORMAL",
    compare: str | None = "EQUAL",
    threshold: typing.Any | None = 0.0,
):
    """Select similar vertices, edges or faces by property types

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    :param compare: Compare
    :type compare: str | None
    :param threshold: Threshold
    :type threshold: typing.Any | None
    """

    ...

def select_similar_region(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select similar face regions to the current selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_ungrouped(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
):
    """Select vertices without a group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | typing.Any | None
    """

    ...

def separate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "SELECTED",
):
    """Separate selected geometry into a new mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

def set_normals_from_faces(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    keep_sharp: bool | typing.Any | None = False,
):
    """Set the custom normals from the selected faces ones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param keep_sharp: Keep Sharp Edges, Do not set sharp edges to face
    :type keep_sharp: bool | typing.Any | None
    """

    ...

def set_sharpness_by_angle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    angle: typing.Any | None = 0.523599,
    extend: bool | typing.Any | None = False,
):
    """Set edge sharpness based on the angle between neighboring faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param angle: Angle
    :type angle: typing.Any | None
    :param extend: Extend, Add new sharp edges without clearing existing sharp edges
    :type extend: bool | typing.Any | None
    """

    ...

def shape_propagate_to_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Apply selected vertex locations to all other shape keys

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def shortest_path_pick(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    edge_mode: str | None = "SELECT",
    use_face_step: bool | typing.Any | None = False,
    use_topology_distance: bool | typing.Any | None = False,
    use_fill: bool | typing.Any | None = False,
    skip: typing.Any | None = 0,
    nth: typing.Any | None = 1,
    offset: typing.Any | None = 0,
    index: typing.Any | None = -1,
):
    """Select shortest path between two selections

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path
    :type edge_mode: str | None
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :type use_face_step: bool | typing.Any | None
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :type use_topology_distance: bool | typing.Any | None
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :type use_fill: bool | typing.Any | None
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: typing.Any | None
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: typing.Any | None
    :param offset: Offset, Offset from the starting point
    :type offset: typing.Any | None
    :type index: typing.Any | None
    """

    ...

def shortest_path_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    edge_mode: str | None = "SELECT",
    use_face_step: bool | typing.Any | None = False,
    use_topology_distance: bool | typing.Any | None = False,
    use_fill: bool | typing.Any | None = False,
    skip: typing.Any | None = 0,
    nth: typing.Any | None = 1,
    offset: typing.Any | None = 0,
):
    """Selected shortest path between two vertices/edges/faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path
    :type edge_mode: str | None
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :type use_face_step: bool | typing.Any | None
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :type use_topology_distance: bool | typing.Any | None
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :type use_fill: bool | typing.Any | None
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: typing.Any | None
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: typing.Any | None
    :param offset: Offset, Offset from the starting point
    :type offset: typing.Any | None
    """

    ...

def smooth_normals(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.5,
):
    """Smooth custom normals based on adjacent vertex normals

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, Specifies weight of smooth vs original normal
    :type factor: typing.Any | None
    """

    ...

def solidify(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    thickness: typing.Any | None = 0.01,
):
    """Create a solid skin by extruding, compensating for sharp angles

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param thickness: Thickness
    :type thickness: typing.Any | None
    """

    ...

def sort_elements(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "VIEW_ZAXIS",
    elements: set[str] | None = {"VERT"},
    reverse: bool | typing.Any | None = False,
    seed: typing.Any | None = 0,
):
    """The order of selected vertices/edges/faces is modified, based on a given method

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
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
    Warning: This will affect unselected elements' indices as well.

    RANDOMIZE
    Randomize -- Randomize order of selected elements.

    REVERSE
    Reverse -- Reverse current order of selected elements.
        :type type: str | None
        :param elements: Elements, Which elements to affect (vertices, edges and/or faces)
        :type elements: set[str] | None
        :param reverse: Reverse, Reverse the sorting effect
        :type reverse: bool | typing.Any | None
        :param seed: Seed, Seed for random-based operations
        :type seed: typing.Any | None
    """

    ...

def spin(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    steps: typing.Any | None = 12,
    dupli: bool | typing.Any | None = False,
    angle: typing.Any | None = 1.5708,
    use_auto_merge: bool | typing.Any | None = True,
    use_normal_flip: bool | typing.Any | None = False,
    center: typing.Any | None = (0.0, 0.0, 0.0),
    axis: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Extrude selected vertices in a circle around the cursor in indicated viewport

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param steps: Steps, Steps
    :type steps: typing.Any | None
    :param dupli: Use Duplicates
    :type dupli: bool | typing.Any | None
    :param angle: Angle, Rotation for each step
    :type angle: typing.Any | None
    :param use_auto_merge: Auto Merge, Merge first/last when the angle is a full revolution
    :type use_auto_merge: bool | typing.Any | None
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: bool | typing.Any | None
    :param center: Center, Center in global view space
    :type center: typing.Any | None
    :param axis: Axis, Axis in global view space
    :type axis: typing.Any | None
    """

    ...

def split(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Split off selected geometry from connected unselected geometry

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def split_normals(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Split custom normals of selected vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def subdivide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    number_cuts: typing.Any | None = 1,
    smoothness: typing.Any | None = 0.0,
    ngon: bool | typing.Any | None = True,
    quadcorner: str | None = "STRAIGHT_CUT",
    fractal: typing.Any | None = 0.0,
    fractal_along_normal: typing.Any | None = 0.0,
    seed: typing.Any | None = 0,
):
    """Subdivide selected edges

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param number_cuts: Number of Cuts
    :type number_cuts: typing.Any | None
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: typing.Any | None
    :param ngon: Create N-Gons, When disabled, newly created faces are limited to 3 and 4 sided faces
    :type ngon: bool | typing.Any | None
    :param quadcorner: Quad Corner Type, How to subdivide quad corners (anything other than Straight Cut will prevent n-gons)
    :type quadcorner: str | None
    :param fractal: Fractal, Fractal randomness factor
    :type fractal: typing.Any | None
    :param fractal_along_normal: Along Normal, Apply fractal displacement along normal only
    :type fractal_along_normal: typing.Any | None
    :param seed: Random Seed, Seed for the random number generator
    :type seed: typing.Any | None
    """

    ...

def subdivide_edgering(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    number_cuts: typing.Any | None = 10,
    interpolation: str | None = "PATH",
    smoothness: typing.Any | None = 1.0,
    profile_shape_factor: typing.Any | None = 0.0,
    profile_shape: str | None = "SMOOTH",
):
    """Subdivide perpendicular edges to the selected edge-ring

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param number_cuts: Number of Cuts
    :type number_cuts: typing.Any | None
    :param interpolation: Interpolation, Interpolation method
    :type interpolation: str | None
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: typing.Any | None
    :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded
    :type profile_shape_factor: typing.Any | None
    :param profile_shape: Profile Shape, Shape of the profile
    :type profile_shape: str | None
    """

    ...

def symmetrize(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    direction: str | None = "NEGATIVE_X",
    threshold: typing.Any | None = 0.0001,
):
    """Enforce symmetry (both form and topological) across an axis

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Which sides to copy from and to
    :type direction: str | None
    :param threshold: Threshold, Limit for snap middle vertices to the axis center
    :type threshold: typing.Any | None
    """

    ...

def symmetry_snap(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    direction: str | None = "NEGATIVE_X",
    threshold: typing.Any | None = 0.05,
    factor: typing.Any | None = 0.5,
    use_center: bool | typing.Any | None = True,
):
    """Snap vertex pairs to their mirrored locations

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Which sides to copy from and to
    :type direction: str | None
    :param threshold: Threshold, Distance within which matching vertices are searched
    :type threshold: typing.Any | None
    :param factor: Factor, Mix factor of the locations of the vertices
    :type factor: typing.Any | None
    :param use_center: Center, Snap middle vertices to the axis center
    :type use_center: bool | typing.Any | None
    """

    ...

def tris_convert_to_quads(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    face_threshold: typing.Any | None = 0.698132,
    shape_threshold: typing.Any | None = 0.698132,
    uvs: bool | typing.Any | None = False,
    vcols: bool | typing.Any | None = False,
    seam: bool | typing.Any | None = False,
    sharp: bool | typing.Any | None = False,
    materials: bool | typing.Any | None = False,
):
    """Join triangles into quads

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param face_threshold: Max Face Angle, Face angle limit
    :type face_threshold: typing.Any | None
    :param shape_threshold: Max Shape Angle, Shape angle limit
    :type shape_threshold: typing.Any | None
    :param uvs: Compare UVs
    :type uvs: bool | typing.Any | None
    :param vcols: Compare VCols
    :type vcols: bool | typing.Any | None
    :param seam: Compare Seam
    :type seam: bool | typing.Any | None
    :param sharp: Compare Sharp
    :type sharp: bool | typing.Any | None
    :param materials: Compare Materials
    :type materials: bool | typing.Any | None
    """

    ...

def unsubdivide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    iterations: typing.Any | None = 2,
):
    """Un-subdivide selected edges and faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param iterations: Iterations, Number of times to un-subdivide
    :type iterations: typing.Any | None
    """

    ...

def uv_texture_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add UV map

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def uv_texture_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove UV map

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def uvs_reverse(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Flip direction of UV coordinates inside faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def uvs_rotate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_ccw: bool | typing.Any | None = False,
):
    """Rotate UV coordinates inside faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_ccw: Counter Clockwise
    :type use_ccw: bool | typing.Any | None
    """

    ...

def vert_connect(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Connect selected vertices of faces, splitting the face

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vert_connect_concave(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Make all faces convex

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vert_connect_nonplanar(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    angle_limit: typing.Any | None = 0.0872665,
):
    """Split non-planar faces that exceed the angle threshold

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param angle_limit: Max Angle, Angle limit
    :type angle_limit: typing.Any | None
    """

    ...

def vert_connect_path(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Connect vertices by their selection order, creating edges, splitting faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertices_smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.0,
    repeat: typing.Any | None = 1,
    xaxis: bool | typing.Any | None = True,
    yaxis: bool | typing.Any | None = True,
    zaxis: bool | typing.Any | None = True,
    wait_for_input: bool | typing.Any | None = True,
):
    """Flatten angles of selected vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Smoothing, Smoothing factor
    :type factor: typing.Any | None
    :param repeat: Repeat, Number of times to smooth the mesh
    :type repeat: typing.Any | None
    :param xaxis: X-Axis, Smooth along the X axis
    :type xaxis: bool | typing.Any | None
    :param yaxis: Y-Axis, Smooth along the Y axis
    :type yaxis: bool | typing.Any | None
    :param zaxis: Z-Axis, Smooth along the Z axis
    :type zaxis: bool | typing.Any | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | typing.Any | None
    """

    ...

def vertices_smooth_laplacian(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    repeat: typing.Any | None = 1,
    lambda_factor: typing.Any | None = 1.0,
    lambda_border: typing.Any | None = 5e-05,
    use_x: bool | typing.Any | None = True,
    use_y: bool | typing.Any | None = True,
    use_z: bool | typing.Any | None = True,
    preserve_volume: bool | typing.Any | None = True,
):
    """Laplacian smooth of selected vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param repeat: Number of iterations to smooth the mesh
    :type repeat: typing.Any | None
    :param lambda_factor: Lambda factor
    :type lambda_factor: typing.Any | None
    :param lambda_border: Lambda factor in border
    :type lambda_border: typing.Any | None
    :param use_x: Smooth X Axis, Smooth object along X axis
    :type use_x: bool | typing.Any | None
    :param use_y: Smooth Y Axis, Smooth object along Y axis
    :type use_y: bool | typing.Any | None
    :param use_z: Smooth Z Axis, Smooth object along Z axis
    :type use_z: bool | typing.Any | None
    :param preserve_volume: Preserve Volume, Apply volume preservation after smooth
    :type preserve_volume: bool | typing.Any | None
    """

    ...

def wireframe(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_boundary: bool | typing.Any | None = True,
    use_even_offset: bool | typing.Any | None = True,
    use_relative_offset: bool | typing.Any | None = False,
    use_replace: bool | typing.Any | None = True,
    thickness: typing.Any | None = 0.01,
    offset: typing.Any | None = 0.01,
    use_crease: bool | typing.Any | None = False,
    crease_weight: typing.Any | None = 0.01,
):
    """Create a solid wireframe from faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_boundary: Boundary, Inset face boundaries
    :type use_boundary: bool | typing.Any | None
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :type use_even_offset: bool | typing.Any | None
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
    :type use_relative_offset: bool | typing.Any | None
    :param use_replace: Replace, Remove original faces
    :type use_replace: bool | typing.Any | None
    :param thickness: Thickness
    :type thickness: typing.Any | None
    :param offset: Offset
    :type offset: typing.Any | None
    :param use_crease: Crease, Crease hub edges for an improved subdivision surface
    :type use_crease: bool | typing.Any | None
    :param crease_weight: Crease Weight
    :type crease_weight: typing.Any | None
    """

    ...
