"""
This module gives access to low level bmesh operations.

Most operators take input and return output, they can be chained together
to perform useful operations.


--------------------

This script shows how operators can be used to model a link of a chain.

```__/examples/bmesh.ops.1.py```

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bmesh.types
import bpy.types
import mathutils

def average_vert_facedata(
    bm: bmesh.types.BMesh, verts: list[bmesh.types.BMVert] = []
) -> None:
    """Average Vertices Face-vert Data.Merge uv/vcols associated with the input vertices at
    the bounding box center. (I know, its not averaging but
    the vert_snap_to_bb_center is just too long).

        :param bm: The bmesh to operate on.
        :param verts: Input vertices.
    """

def beautify_fill(
    bm: bmesh.types.BMesh,
    faces: list[bmesh.types.BMFace] = [],
    edges: list[bmesh.types.BMEdge] = [],
    use_restrict_tag: bool = False,
    method: typing.Literal["AREA", "ANGLE"] = "AREA",
) -> dict[str, typing.Any]:
    """Beautify Fill.Rotate edges to create more evenly spaced triangles.

        :param bm: The bmesh to operate on.
        :param faces: Input faces.
        :param edges: Edges that can be flipped.
        :param use_restrict_tag: Restrict edge rotation to mixed tagged vertices.
        :param method: Method to define what is beautiful.
        :return: geom:
    New flipped faces and edges.

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    """

def bevel(
    bm: bmesh.types.BMesh,
    geom: list[bmesh.types.BMEdge]
    | list[bmesh.types.BMFace]
    | list[bmesh.types.BMVert] = [],
    offset: float = 0,
    offset_type: typing.Literal[
        "OFFSET", "WIDTH", "DEPTH", "PERCENT", "ABSOLUTE"
    ] = "OFFSET",
    profile_type: typing.Literal["SUPERELLIPSE", "CUSTOM"] = "SUPERELLIPSE",
    segments: int = 0,
    profile: float = 0,
    affect: typing.Literal["VERTICES", "EDGES"] = "VERTICES",
    clamp_overlap: bool = False,
    material: int = 0,
    loop_slide: bool = False,
    mark_seam: bool = False,
    mark_sharp: bool = False,
    harden_normals: bool = False,
    face_strength_mode: typing.Literal["NONE", "NEW", "AFFECTED", "ALL"] = "NONE",
    miter_outer: typing.Literal["SHARP", "PATCH", "ARC"] = "SHARP",
    miter_inner: typing.Literal["SHARP", "PATCH", "ARC"] = "SHARP",
    spread: float = 0,
    custom_profile: bpy.types.bpy_struct | None = None,
    vmesh_method: typing.Literal["ADJ", "CUTOFF"] = "ADJ",
) -> dict[str, typing.Any]:
    """Bevel.Bevels edges and vertices

        :param bm: The bmesh to operate on.
        :param geom: Input edges and vertices.
        :param offset: Amount to offset beveled edge.
        :param offset_type: How to measure the offset.
        :param profile_type: The profile type to use for bevel.
        :param segments: Number of segments in bevel.
        :param profile: Profile shape, 0->1 (.5=>round).
        :param affect: Whether to bevel vertices or edges.
        :param clamp_overlap: Do not allow beveled edges/vertices to overlap each other.
        :param material: Material for bevel faces, -1 means get from adjacent faces.
        :param loop_slide: Prefer to slide along edges to having even widths.
        :param mark_seam: Extend edge data to allow seams to run across bevels.
        :param mark_sharp: Extend edge data to allow sharp edges to run across bevels.
        :param harden_normals: Harden normals.
        :param face_strength_mode: Whether to set face strength, and which faces to set if so.
        :param miter_outer: Outer miter kind.
        :param miter_inner: Outer miter kind.
        :param spread: Amount to offset beveled edge.
        :param custom_profile: CurveProfile, if None ignored
        :param vmesh_method: The method to use to create meshes at intersections.
        :return: faces:
    Output faces.

    type list of (`bmesh.types.BMFace`)

    edges:
    Output edges.

    type list of (`bmesh.types.BMEdge`)

    verts:
    Output verts.

    type list of (`bmesh.types.BMVert`)
    """

def bisect_edges(
    bm: bmesh.types.BMesh,
    edges: list[bmesh.types.BMEdge] = [],
    cuts: int = 0,
    edge_percents={},
) -> dict[str, typing.Any]:
    """Edge Bisect.Splits input edges (but doesnt do anything else).
    This creates a 2-valence vert.

        :param bm: The bmesh to operate on.
        :param edges: Input edges.
        :param cuts: Number of cuts.
        :param edge_percents: Undocumented.
        :return: geom_split:
    Newly created vertices and edges.

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    """

def bisect_plane(
    bm: bmesh.types.BMesh,
    geom: list[bmesh.types.BMEdge]
    | list[bmesh.types.BMFace]
    | list[bmesh.types.BMVert] = [],
    dist: float = 0,
    plane_co: collections.abc.Sequence[float] | mathutils.Vector = mathutils.Vector(),
    plane_no: collections.abc.Sequence[float] | mathutils.Vector = mathutils.Vector(),
    use_snap_center: bool = False,
    clear_outer: bool = False,
    clear_inner: bool = False,
) -> dict[str, typing.Any]:
    """Bisect Plane.Bisects the mesh by a plane (cut the mesh in half).

        :param bm: The bmesh to operate on.
        :param geom: Input geometry.
        :param dist: Minimum distance when testing if a vert is exactly on the plane.
        :param plane_co: Point on the plane.
        :param plane_no: Direction of the plane.
        :param use_snap_center: Snap axis aligned verts to the center.
        :param clear_outer: When enabled. remove all geometry on the positive side of the plane.
        :param clear_inner: When enabled. remove all geometry on the negative side of the plane.
        :return: geom_cut:
    Output geometry aligned with the plane (new and existing).

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`)

    geom:
    Input and output geometry (result of cut).

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    """

def bmesh_to_mesh(
    bm: bmesh.types.BMesh, mesh: bpy.types.Mesh, object: bpy.types.Object
) -> None:
    """BMesh to Mesh.Converts a bmesh to a Mesh. This is reserved for exiting edit-mode.

    :param bm: The bmesh to operate on.
    :param mesh: Pointer to a mesh structure to fill in.
    :param object: Pointer to an object structure.
    """

def bridge_loops(
    bm: bmesh.types.BMesh,
    edges: list[bmesh.types.BMEdge] = [],
    use_pairs: bool = False,
    use_cyclic: bool = False,
    use_merge: bool = False,
    merge_factor: float = 0,
    twist_offset: int = 0,
) -> dict[str, typing.Any]:
    """Bridge edge loops with faces.

        :param bm: The bmesh to operate on.
        :param edges: Input edges.
        :param use_pairs: Undocumented.
        :param use_cyclic: Undocumented.
        :param use_merge: Merge rather than creating faces.
        :param merge_factor: Merge factor.
        :param twist_offset: Twist offset for closed loops.
        :return: faces:
    New faces.

    type list of (`bmesh.types.BMFace`)

    edges:
    New edges.

    type list of (`bmesh.types.BMEdge`)
    """

def collapse(
    bm: bmesh.types.BMesh, edges: list[bmesh.types.BMEdge] = [], uvs: bool = False
) -> None:
    """Collapse Connected.Collapses connected vertices

    :param bm: The bmesh to operate on.
    :param edges: Input edges.
    :param uvs: Also collapse UVs and such.
    """

def collapse_uvs(bm: bmesh.types.BMesh, edges: list[bmesh.types.BMEdge] = []) -> None:
    """Collapse Connected UVs.Collapses connected UV vertices.

    :param bm: The bmesh to operate on.
    :param edges: Input edges.
    """

def connect_vert_pair(
    bm: bmesh.types.BMesh,
    verts: list[bmesh.types.BMVert] = [],
    verts_exclude: list[bmesh.types.BMVert] = [],
    faces_exclude: list[bmesh.types.BMFace] = [],
) -> dict[str, typing.Any]:
    """Connect Verts.Split faces by adding edges that connect verts.

        :param bm: The bmesh to operate on.
        :param verts: Input vertices.
        :param verts_exclude: Input vertices to explicitly exclude from connecting.
        :param faces_exclude: Input faces to explicitly exclude from connecting.
        :return: edges:

    type list of (`bmesh.types.BMEdge`)
    """

def connect_verts(
    bm: bmesh.types.BMesh,
    verts: list[bmesh.types.BMVert] = [],
    faces_exclude: list[bmesh.types.BMFace] = [],
    check_degenerate: bool = False,
) -> dict[str, typing.Any]:
    """Connect Verts.Split faces by adding edges that connect verts.

        :param bm: The bmesh to operate on.
        :param verts: Input vertices.
        :param faces_exclude: Input faces to explicitly exclude from connecting.
        :param check_degenerate: Prevent splits with overlaps & intersections.
        :return: edges:

    type list of (`bmesh.types.BMEdge`)
    """

def connect_verts_concave(
    bm: bmesh.types.BMesh, faces: list[bmesh.types.BMFace] = []
) -> dict[str, typing.Any]:
    """Connect Verts to form Convex Faces.Ensures all faces are convex faces.

        :param bm: The bmesh to operate on.
        :param faces: Input faces.
        :return: edges:

    type list of (`bmesh.types.BMEdge`)

    faces:

    type list of (`bmesh.types.BMFace`)
    """

def connect_verts_nonplanar(
    bm: bmesh.types.BMesh, angle_limit: float = 0, faces: list[bmesh.types.BMFace] = []
) -> dict[str, typing.Any]:
    """Connect Verts Across non Planer Faces.Split faces by connecting edges along non planer faces.

        :param bm: The bmesh to operate on.
        :param angle_limit: Total rotation angle (radians).
        :param faces: Input faces.
        :return: edges:

    type list of (`bmesh.types.BMEdge`)

    faces:

    type list of (`bmesh.types.BMFace`)
    """

def contextual_create(
    bm: bmesh.types.BMesh,
    geom: list[bmesh.types.BMEdge]
    | list[bmesh.types.BMFace]
    | list[bmesh.types.BMVert] = [],
    mat_nr: int = 0,
    use_smooth: bool = False,
) -> dict[str, typing.Any]:
    """Contextual Create.This is basically F-key, it creates
    new faces from vertices, makes stuff from edge nets,
    makes wire edges, etc. It also dissolves faces.Three verts become a triangle, four become a quad. Two
    become a wire edge.

        :param bm: The bmesh to operate on.
        :param geom: Input geometry.
        :param mat_nr: Material to use.
        :param use_smooth: Smooth to use.
        :return: faces:
    Newly-made face(s).

    type list of (`bmesh.types.BMFace`)

    edges:
    Newly-made edge(s).

    type list of (`bmesh.types.BMEdge`)
    """

def convex_hull(
    bm: bmesh.types.BMesh,
    input: list[bmesh.types.BMEdge]
    | list[bmesh.types.BMFace]
    | list[bmesh.types.BMVert] = [],
    use_existing_faces: bool = False,
) -> dict[str, typing.Any]:
    """Convex HullBuilds a convex hull from the vertices in input.If use_existing_faces is true, the hull will not output triangles
    that are covered by a pre-existing face.All hull vertices, faces, and edges are added to geom.out. Any
    input elements that end up inside the hull (i.e. are not used by an
    output face) are added to the interior_geom slot. The
    unused_geom slot will contain all interior geometry that is
    completely unused. Lastly, holes_geom contains edges and faces
    that were in the input and are part of the hull.

        :param bm: The bmesh to operate on.
        :param input: Input geometry.
        :param use_existing_faces: Skip hull triangles that are covered by a pre-existing face.
        :return: geom:

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)

    geom_interior:

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)

    geom_unused:

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)

    geom_holes:

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    """

def create_circle(
    bm: bmesh.types.BMesh,
    cap_ends: bool = False,
    cap_tris: bool = False,
    segments: int = 0,
    radius: float = 0,
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix = mathutils.Matrix.Identity(4),
    calc_uvs: bool = False,
) -> dict[str, typing.Any]:
    """Creates a Circle.

        :param bm: The bmesh to operate on.
        :param cap_ends: Whether or not to fill in the ends with faces.
        :param cap_tris: Fill ends with triangles instead of ngons.
        :param segments: Number of vertices in the circle.
        :param radius: Radius of the circle.
        :param matrix: Matrix to multiply the new geometry with.
        :param calc_uvs: Calculate default UVs.
        :return: verts:
    Output verts.

    type list of (`bmesh.types.BMVert`)
    """

def create_cone(
    bm: bmesh.types.BMesh,
    cap_ends: bool = False,
    cap_tris: bool = False,
    segments: int = 0,
    radius1: float = 0,
    radius2: float = 0,
    depth: float = 0,
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix = mathutils.Matrix.Identity(4),
    calc_uvs: bool = False,
) -> dict[str, typing.Any]:
    """Create Cone.Creates a cone with variable depth at both ends

        :param bm: The bmesh to operate on.
        :param cap_ends: Whether or not to fill in the ends with faces.
        :param cap_tris: Fill ends with triangles instead of ngons.
        :param segments: Number of vertices in the base circle.
        :param radius1: Radius of one end.
        :param radius2: Radius of the opposite.
        :param depth: Distance between ends.
        :param matrix: Matrix to multiply the new geometry with.
        :param calc_uvs: Calculate default UVs.
        :return: verts:
    Output verts.

    type list of (`bmesh.types.BMVert`)
    """

def create_cube(
    bm: bmesh.types.BMesh,
    size: float = 0,
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix = mathutils.Matrix.Identity(4),
    calc_uvs: bool = False,
) -> dict[str, typing.Any]:
    """Create CubeCreates a cube.

        :param bm: The bmesh to operate on.
        :param size: Size of the cube.
        :param matrix: Matrix to multiply the new geometry with.
        :param calc_uvs: Calculate default UVs.
        :return: verts:
    Output verts.

    type list of (`bmesh.types.BMVert`)
    """

def create_grid(
    bm: bmesh.types.BMesh,
    x_segments: int = 0,
    y_segments: int = 0,
    size: float = 0,
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix = mathutils.Matrix.Identity(4),
    calc_uvs: bool = False,
) -> dict[str, typing.Any]:
    """Create Grid.Creates a grid with a variable number of subdivisions

        :param bm: The bmesh to operate on.
        :param x_segments: Number of x segments.
        :param y_segments: Number of y segments.
        :param size: Size of the grid.
        :param matrix: Matrix to multiply the new geometry with.
        :param calc_uvs: Calculate default UVs.
        :return: verts:
    Output verts.

    type list of (`bmesh.types.BMVert`)
    """

def create_icosphere(
    bm: bmesh.types.BMesh,
    subdivisions: int = 0,
    radius: float = 0,
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix = mathutils.Matrix.Identity(4),
    calc_uvs: bool = False,
) -> dict[str, typing.Any]:
    """Create Ico-Sphere.Creates a grid with a variable number of subdivisions

        :param bm: The bmesh to operate on.
        :param subdivisions: How many times to recursively subdivide the sphere.
        :param radius: Radius.
        :param matrix: Matrix to multiply the new geometry with.
        :param calc_uvs: Calculate default UVs.
        :return: verts:
    Output verts.

    type list of (`bmesh.types.BMVert`)
    """

def create_monkey(
    bm: bmesh.types.BMesh,
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix = mathutils.Matrix.Identity(4),
    calc_uvs: bool = False,
) -> dict[str, typing.Any]:
    """Create Suzanne.Creates a monkey (standard blender primitive).

        :param bm: The bmesh to operate on.
        :param matrix: Matrix to multiply the new geometry with.
        :param calc_uvs: Calculate default UVs.
        :return: verts:
    Output verts.

    type list of (`bmesh.types.BMVert`)
    """

def create_uvsphere(
    bm: bmesh.types.BMesh,
    u_segments: int = 0,
    v_segments: int = 0,
    radius: float = 0,
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix = mathutils.Matrix.Identity(4),
    calc_uvs: bool = False,
) -> dict[str, typing.Any]:
    """Create UV Sphere.Creates a grid with a variable number of subdivisions

        :param bm: The bmesh to operate on.
        :param u_segments: Number of u segments.
        :param v_segments: Number of v segment.
        :param radius: Radius.
        :param matrix: Matrix to multiply the new geometry with.
        :param calc_uvs: Calculate default UVs.
        :return: verts:
    Output verts.

    type list of (`bmesh.types.BMVert`)
    """

def create_vert(
    bm: bmesh.types.BMesh,
    co: collections.abc.Sequence[float] | mathutils.Vector = mathutils.Vector(),
) -> dict[str, typing.Any]:
    """Make Vertex.Creates a single vertex; this BMOP was necessary
    for click-create-vertex.

        :param bm: The bmesh to operate on.
        :param co: The coordinate of the new vert.
        :return: vert:
    The new vert.

    type list of (`bmesh.types.BMVert`)
    """

def delete(
    bm: bmesh.types.BMesh,
    geom: list[bmesh.types.BMEdge]
    | list[bmesh.types.BMFace]
    | list[bmesh.types.BMVert] = [],
    context: typing.Literal[
        "VERTS",
        "EDGES",
        "FACES_ONLY",
        "EDGES_FACES",
        "FACES",
        "FACES_KEEP_BOUNDARY",
        "TAGGED_ONLY",
    ] = "VERTS",
) -> None:
    """Delete Geometry.Utility operator to delete geometry.

    :param bm: The bmesh to operate on.
    :param geom: Input geometry.
    :param context: Geometry types to delete.
    """

def dissolve_degenerate(
    bm: bmesh.types.BMesh, dist: float = 0, edges: list[bmesh.types.BMEdge] = []
) -> None:
    """Degenerate Dissolve.Dissolve edges with no length, faces with no area.

    :param bm: The bmesh to operate on.
    :param dist: Maximum distance to consider degenerate.
    :param edges: Input edges.
    """

def dissolve_edges(
    bm: bmesh.types.BMesh,
    edges: list[bmesh.types.BMEdge] = [],
    use_verts: bool = False,
    use_face_split: bool = False,
    angle_threshold: float = 0,
) -> dict[str, typing.Any]:
    """Dissolve Edges.

        :param bm: The bmesh to operate on.
        :param edges: Input edges.
        :param use_verts: Dissolve verts left between only 2 edges.
        :param use_face_split: Split off face corners to maintain surrounding geometry.
        :param angle_threshold: Do not dissolve verts between 2 edges when their angle exceeds this threshold.
    Disabled by default.
        :return: region:

    type list of (`bmesh.types.BMFace`)
    """

def dissolve_faces(
    bm: bmesh.types.BMesh, faces: list[bmesh.types.BMFace] = [], use_verts: bool = False
) -> dict[str, typing.Any]:
    """Dissolve Faces.

        :param bm: The bmesh to operate on.
        :param faces: Input faces.
        :param use_verts: Dissolve verts left between only 2 edges.
        :return: region:

    type list of (`bmesh.types.BMFace`)
    """

def dissolve_limit(
    bm: bmesh.types.BMesh,
    angle_limit: float = 0,
    use_dissolve_boundaries: bool = False,
    verts: list[bmesh.types.BMVert] = [],
    edges: list[bmesh.types.BMEdge] = [],
    delimit=set(),
) -> dict[str, typing.Any]:
    """Limited Dissolve.Dissolve planar faces and co-linear edges.

        :param bm: The bmesh to operate on.
        :param angle_limit: Total rotation angle (radians).
        :param use_dissolve_boundaries: Dissolve all vertices in between face boundaries.
        :param verts: Input vertices.
        :param edges: Input edges.
        :param delimit: Delimit dissolve operation.
        :return: region:

    type list of (`bmesh.types.BMFace`)
    """

def dissolve_verts(
    bm: bmesh.types.BMesh,
    verts: list[bmesh.types.BMVert] = [],
    use_face_split: bool = False,
    use_boundary_tear: bool = False,
) -> None:
    """Dissolve Verts.

    :param bm: The bmesh to operate on.
    :param verts: Input vertices.
    :param use_face_split: Split off face corners to maintain surrounding geometry.
    :param use_boundary_tear: Split off face corners instead of merging faces.
    """

def duplicate(
    bm: bmesh.types.BMesh,
    geom: list[bmesh.types.BMEdge]
    | list[bmesh.types.BMFace]
    | list[bmesh.types.BMVert] = [],
    dest: bmesh.types.BMesh | None = None,
    use_select_history: bool = False,
    use_edge_flip_from_face: bool = False,
) -> dict[str, typing.Any]:
    """Duplicate Geometry.Utility operator to duplicate geometry,
    optionally into a destination mesh.

        :param bm: The bmesh to operate on.
        :param geom: Input geometry.
        :param dest: Destination bmesh, if None will use current on.
        :param use_select_history: Undocumented.
        :param use_edge_flip_from_face: Undocumented.
        :return: geom_orig:

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)

    geom:

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)

    vert_map:

    type dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace`

    edge_map:

    type dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace`

    face_map:

    type dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace`

    boundary_map:
    Boundary edges from the split geometry that maps edges from the original geometry
    to the destination edges.

    type dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace`

    isovert_map:

    type dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace`
    """

def edgeloop_fill(
    bm: bmesh.types.BMesh,
    edges: list[bmesh.types.BMEdge] = [],
    mat_nr: int = 0,
    use_smooth: bool = False,
) -> dict[str, typing.Any]:
    """Edge Loop Fill.Create faces defined by one or more non overlapping edge loops.

        :param bm: The bmesh to operate on.
        :param edges: Input edges.
        :param mat_nr: Material to use.
        :param use_smooth: Smooth state to use.
        :return: faces:
    New faces.

    type list of (`bmesh.types.BMFace`)
    """

def edgenet_fill(
    bm: bmesh.types.BMesh,
    edges: list[bmesh.types.BMEdge] = [],
    mat_nr: int = 0,
    use_smooth: bool = False,
    sides: int = 0,
) -> dict[str, typing.Any]:
    """Edge Net Fill.Create faces defined by enclosed edges.

        :param bm: The bmesh to operate on.
        :param edges: Input edges.
        :param mat_nr: Material to use.
        :param use_smooth: Smooth state to use.
        :param sides: Number of sides.
        :return: faces:
    New faces.

    type list of (`bmesh.types.BMFace`)
    """

def edgenet_prepare(
    bm: bmesh.types.BMesh, edges: list[bmesh.types.BMEdge] = []
) -> dict[str, typing.Any]:
    """Edge-net Prepare.Identifies several useful edge loop cases and modifies them so
    theyll become a face when edgenet_fill is called. The cases covered are:

        :param bm: The bmesh to operate on.
        :param edges: Input edges.
        :return: edges:
    New edges.

    type list of (`bmesh.types.BMEdge`)
    """

def extrude_discrete_faces(
    bm: bmesh.types.BMesh,
    faces: list[bmesh.types.BMFace] = [],
    use_normal_flip: bool = False,
    use_select_history: bool = False,
) -> dict[str, typing.Any]:
    """Individual Face Extrude.Extrudes faces individually.

        :param bm: The bmesh to operate on.
        :param faces: Input faces.
        :param use_normal_flip: Create faces with reversed direction.
        :param use_select_history: Pass to duplicate.
        :return: faces:
    Output faces.

    type list of (`bmesh.types.BMFace`)
    """

def extrude_edge_only(
    bm: bmesh.types.BMesh,
    edges: list[bmesh.types.BMEdge] = [],
    use_normal_flip: bool = False,
    use_select_history: bool = False,
) -> dict[str, typing.Any]:
    """Extrude Only Edges.Extrudes Edges into faces, note that this is very simple, theres no fancy
    winged extrusion.

        :param bm: The bmesh to operate on.
        :param edges: Input vertices.
        :param use_normal_flip: Create faces with reversed direction.
        :param use_select_history: Pass to duplicate.
        :return: geom:
    Output geometry.

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    """

def extrude_face_region(
    bm: bmesh.types.BMesh,
    geom: list[bmesh.types.BMEdge]
    | list[bmesh.types.BMFace]
    | list[bmesh.types.BMVert] = [],
    edges_exclude=set(),
    use_keep_orig: bool = False,
    use_normal_flip: bool = False,
    use_normal_from_adjacent: bool = False,
    use_dissolve_ortho_edges: bool = False,
    use_select_history: bool = False,
    skip_input_flip: bool = False,
) -> dict[str, typing.Any]:
    """Extrude Faces.Extrude operator (does not transform)

        :param bm: The bmesh to operate on.
        :param geom: Edges and faces.
        :param edges_exclude: Input edges to explicitly exclude from extrusion.
        :param use_keep_orig: Keep original geometry (requires geom to include edges).
        :param use_normal_flip: Create faces with reversed direction.
        :param use_normal_from_adjacent: Use winding from surrounding faces instead of this region.
        :param use_dissolve_ortho_edges: Dissolve edges whose faces form a flat surface.
        :param use_select_history: Pass to duplicate.
        :param skip_input_flip: Skip flipping of input faces to preserve original orientation.
        :return: geom:

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    """

def extrude_vert_indiv(
    bm: bmesh.types.BMesh,
    verts: list[bmesh.types.BMVert] = [],
    use_select_history: bool = False,
) -> dict[str, typing.Any]:
    """Individual Vertex Extrude.Extrudes wire edges from vertices.

        :param bm: The bmesh to operate on.
        :param verts: Input vertices.
        :param use_select_history: Pass to duplicate.
        :return: edges:
    Output wire edges.

    type list of (`bmesh.types.BMEdge`)

    verts:
    Output vertices.

    type list of (`bmesh.types.BMVert`)
    """

def face_attribute_fill(
    bm: bmesh.types.BMesh,
    faces: list[bmesh.types.BMFace] = [],
    use_normals: bool = False,
    use_data: bool = False,
) -> dict[str, typing.Any]:
    """Face Attribute Fill.Fill in faces with data from adjacent faces.

        :param bm: The bmesh to operate on.
        :param faces: Input faces.
        :param use_normals: Copy face winding.
        :param use_data: Copy face data.
        :return: faces_fail:
    Faces that could not be handled.

    type list of (`bmesh.types.BMFace`)
    """

def find_doubles(
    bm: bmesh.types.BMesh,
    verts: list[bmesh.types.BMVert] = [],
    keep_verts: list[bmesh.types.BMVert] = [],
    use_connected: bool = False,
    dist: float = 0,
) -> dict[str, typing.Any]:
    """Find Doubles.Takes input verts and find vertices they should weld to.
    Outputs a mapping slot suitable for use with the weld verts BMOP.If keep_verts is used, vertices outside that set can only be merged
    with vertices in that set.

        :param bm: The bmesh to operate on.
        :param verts: Input vertices.
        :param keep_verts: List of verts to keep.
        :param use_connected: Limit the search for doubles by connected geometry.
        :param dist: Maximum distance.
        :return: targetmap:

    type dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace`
    """

def flip_quad_tessellation(
    bm: bmesh.types.BMesh, faces: list[bmesh.types.BMFace] = []
) -> None:
    """Flip Quad TessellationFlip the tessellation direction of the selected quads.

    :param bm: The bmesh to operate on.
    :param faces: Input faces.
    """

def grid_fill(
    bm: bmesh.types.BMesh,
    edges: list[bmesh.types.BMEdge] = [],
    mat_nr: int = 0,
    use_smooth: bool = False,
    use_interp_simple: bool = False,
) -> dict[str, typing.Any]:
    """Grid Fill.Create faces defined by 2 disconnected edge loops (which share edges).

        :param bm: The bmesh to operate on.
        :param edges: Input edges.
        :param mat_nr: Material to use.
        :param use_smooth: Smooth state to use.
        :param use_interp_simple: Use simple interpolation.
        :return: faces:
    New faces.

    type list of (`bmesh.types.BMFace`)
    """

def holes_fill(
    bm: bmesh.types.BMesh, edges: list[bmesh.types.BMEdge] = [], sides: int = 0
) -> dict[str, typing.Any]:
    """Fill Holes.Fill boundary edges with faces, copying surrounding custom-data.

        :param bm: The bmesh to operate on.
        :param edges: Input edges.
        :param sides: Number of face sides to fill.
        :return: faces:
    New faces.

    type list of (`bmesh.types.BMFace`)
    """

def inset_individual(
    bm: bmesh.types.BMesh,
    faces: list[bmesh.types.BMFace] = [],
    thickness: float = 0,
    depth: float = 0,
    use_even_offset: bool = False,
    use_interpolate: bool = False,
    use_relative_offset: bool = False,
) -> dict[str, typing.Any]:
    """Face Inset (Individual).Insets individual faces.

        :param bm: The bmesh to operate on.
        :param faces: Input faces.
        :param thickness: Thickness.
        :param depth: Depth.
        :param use_even_offset: Scale the offset to give more even thickness.
        :param use_interpolate: Blend face data across the inset.
        :param use_relative_offset: Scale the offset by surrounding geometry.
        :return: faces:
    Output faces.

    type list of (`bmesh.types.BMFace`)
    """

def inset_region(
    bm: bmesh.types.BMesh,
    faces: list[bmesh.types.BMFace] = [],
    faces_exclude: list[bmesh.types.BMFace] = [],
    use_boundary: bool = False,
    use_even_offset: bool = False,
    use_interpolate: bool = False,
    use_relative_offset: bool = False,
    use_edge_rail: bool = False,
    thickness: float = 0,
    depth: float = 0,
    use_outset: bool = False,
) -> dict[str, typing.Any]:
    """Face Inset (Regions).Inset or outset face regions.

        :param bm: The bmesh to operate on.
        :param faces: Input faces.
        :param faces_exclude: Input faces to explicitly exclude from inset.
        :param use_boundary: Inset face boundaries.
        :param use_even_offset: Scale the offset to give more even thickness.
        :param use_interpolate: Blend face data across the inset.
        :param use_relative_offset: Scale the offset by surrounding geometry.
        :param use_edge_rail: Inset the region along existing edges.
        :param thickness: Thickness.
        :param depth: Depth.
        :param use_outset: Outset rather than inset.
        :return: faces:
    Output faces.

    type list of (`bmesh.types.BMFace`)
    """

def join_triangles(
    bm: bmesh.types.BMesh,
    faces: list[bmesh.types.BMFace] = [],
    cmp_seam: bool = False,
    cmp_sharp: bool = False,
    cmp_uvs: bool = False,
    cmp_vcols: bool = False,
    cmp_materials: bool = False,
    angle_face_threshold: float = 0,
    angle_shape_threshold: float = 0,
    topology_influence: float = 0,
    deselect_joined: bool = False,
    merge_limit: int = 0,
    neighbor_debug: int = 0,
) -> dict[str, typing.Any]:
    """Join Triangles.Tries to intelligently join triangles according
    to angle threshold and delimiters.

        :param bm: The bmesh to operate on.
        :param faces: Input geometry.
        :param cmp_seam: Compare seam
        :param cmp_sharp: Compare sharp
        :param cmp_uvs: Compare UVs
        :param cmp_vcols: Compare VCols.
        :param cmp_materials: Compare materials.
        :param angle_face_threshold: Undocumented.
        :param angle_shape_threshold: Undocumented.
        :param topology_influence: Undocumented.
        :param deselect_joined: Undocumented.
        :param merge_limit: Undocumented.
        :param neighbor_debug: Undocumented.
        :return: faces:
    Joined faces.

    type list of (`bmesh.types.BMFace`)
    """

def mesh_to_bmesh(
    bm: bmesh.types.BMesh,
    mesh: bpy.types.Mesh,
    object: bpy.types.Object,
    use_shapekey: bool = False,
) -> None:
    """Mesh to BMesh.Load the contents of a mesh into the bmesh. this BMOP is private, its
    reserved exclusively for entering edit-mode.

        :param bm: The bmesh to operate on.
        :param mesh: Pointer to a Mesh structure.
        :param object: Pointer to an Object structure.
        :param use_shapekey: Load active shapekey coordinates into verts.
    """

def mirror(
    bm: bmesh.types.BMesh,
    geom: list[bmesh.types.BMEdge]
    | list[bmesh.types.BMFace]
    | list[bmesh.types.BMVert] = [],
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix = mathutils.Matrix.Identity(4),
    merge_dist: float = 0,
    axis: typing.Literal["X", "Y", "Z"] = "X",
    mirror_u: bool = False,
    mirror_v: bool = False,
    mirror_udim: bool = False,
    use_shapekey: bool = False,
) -> dict[str, typing.Any]:
    """Mirror.Mirrors geometry along an axis. The resulting geometry is welded on using
    merge_dist. Pairs of original/mirrored vertices are welded using the merge_dist
    parameter (which defines the minimum distance for welding to happen).

        :param bm: The bmesh to operate on.
        :param geom: Input geometry.
        :param matrix: Matrix defining the mirror transformation.
        :param merge_dist: Maximum distance for merging. does no merging if 0.
        :param axis: The axis to use.
        :param mirror_u: Mirror UVs across the u axis.
        :param mirror_v: Mirror UVs across the v axis.
        :param mirror_udim: Mirror UVs in each tile.
        :param use_shapekey: Transform shape keys too.
        :return: geom:
    Output geometry, mirrored.

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    """

def object_load_bmesh(
    bm: bmesh.types.BMesh, scene: bpy.types.Scene, object: bpy.types.Object
) -> None:
    """Object Load BMesh.Loads a bmesh into an object/mesh. This is a "private"
    BMOP.

        :param bm: The bmesh to operate on.
        :param scene: Pointer to an scene structure.
        :param object: Pointer to an object structure.
    """

def offset_edgeloops(
    bm: bmesh.types.BMesh,
    edges: list[bmesh.types.BMEdge] = [],
    use_cap_endpoint: bool = False,
) -> dict[str, typing.Any]:
    """Edge-loop Offset.Creates edge loops based on simple edge-outset method.

        :param bm: The bmesh to operate on.
        :param edges: Input edges.
        :param use_cap_endpoint: Extend loop around end-points.
        :return: edges:
    Output edges.

    type list of (`bmesh.types.BMEdge`)
    """

def planar_faces(
    bm: bmesh.types.BMesh,
    faces: list[bmesh.types.BMFace] = [],
    iterations: int = 0,
    factor: float = 0,
) -> dict[str, typing.Any]:
    """Planar Faces.Iteratively flatten faces.

        :param bm: The bmesh to operate on.
        :param faces: Input geometry.
        :param iterations: Number of times to flatten faces (for when connected faces are used)
        :param factor: Influence for making planar each iteration
        :return: geom:
    Output slot, computed boundary geometry.

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    """

def pointmerge(
    bm: bmesh.types.BMesh,
    verts: list[bmesh.types.BMVert] = [],
    merge_co: collections.abc.Sequence[float] | mathutils.Vector = mathutils.Vector(),
) -> None:
    """Point Merge.Merge verts together at a point.

    :param bm: The bmesh to operate on.
    :param verts: Input vertices (all verts will be merged into the first).
    :param merge_co: Position to merge at.
    """

def pointmerge_facedata(
    bm: bmesh.types.BMesh,
    verts: list[bmesh.types.BMVert] = [],
    vert_snap: bmesh.types.BMVert | None = None,
) -> None:
    """Face-Data Point Merge.Merge uv/vcols at a specific vertex.

    :param bm: The bmesh to operate on.
    :param verts: Input vertices.
    :param vert_snap: Snap vertex.
    """

def poke(
    bm: bmesh.types.BMesh,
    faces: list[bmesh.types.BMFace] = [],
    offset: float = 0,
    center_mode: typing.Literal["MEAN_WEIGHTED", "MEAN", "BOUNDS"] = "MEAN_WEIGHTED",
    use_relative_offset: bool = False,
) -> dict[str, typing.Any]:
    """Pokes a face.Splits a face into a triangle fan.

        :param bm: The bmesh to operate on.
        :param faces: Input faces.
        :param offset: Center vertex offset along normal.
        :param center_mode: Calculation mode for center vertex.
        :param use_relative_offset: Apply offset.
        :return: verts:
    Output verts.

    type list of (`bmesh.types.BMVert`)

    faces:
    Output faces.

    type list of (`bmesh.types.BMFace`)
    """

def recalc_face_normals(
    bm: bmesh.types.BMesh, faces: list[bmesh.types.BMFace] = []
) -> None:
    """Right-Hand Faces.Computes an "outside" normal for the specified input faces.

    :param bm: The bmesh to operate on.
    :param faces: Input faces.
    """

def region_extend(
    bm: bmesh.types.BMesh,
    geom: list[bmesh.types.BMEdge]
    | list[bmesh.types.BMFace]
    | list[bmesh.types.BMVert] = [],
    use_contract: bool = False,
    use_faces: bool = False,
    use_face_step: bool = False,
) -> dict[str, typing.Any]:
    """Region Extend.used to implement the select more/less tools.
    this puts some geometry surrounding regions of
    geometry in geom into geom.out.if use_faces is 0 then geom.out spits out verts and edges,
    otherwise it spits out faces.

        :param bm: The bmesh to operate on.
        :param geom: Input geometry.
        :param use_contract: Find boundary inside the regions, not outside.
        :param use_faces: Extend from faces instead of edges.
        :param use_face_step: Step over connected faces.
        :return: geom:
    Output slot, computed boundary geometry.

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    """

def remove_doubles(
    bm: bmesh.types.BMesh,
    verts: list[bmesh.types.BMVert] = [],
    use_connected: bool = False,
    dist: float = 0,
) -> None:
    """Remove Doubles.Finds groups of vertices closer than dist and merges them together,
    using the weld verts BMOP.

        :param bm: The bmesh to operate on.
        :param verts: Input verts.
        :param use_connected: Limit the search for doubles by connected geometry.
        :param dist: Minimum distance.
    """

def reverse_colors(
    bm: bmesh.types.BMesh, faces: list[bmesh.types.BMFace] = [], color_index: int = 0
) -> None:
    """Color ReverseReverse the loop colors.

    :param bm: The bmesh to operate on.
    :param faces: Input faces.
    :param color_index: Index into color attribute list.
    """

def reverse_faces(
    bm: bmesh.types.BMesh,
    faces: list[bmesh.types.BMFace] = [],
    flip_multires: bool = False,
) -> None:
    """Reverse Faces.Reverses the winding (vertex order) of faces.
    This has the effect of flipping the normal.

        :param bm: The bmesh to operate on.
        :param faces: Input faces.
        :param flip_multires: Maintain multi-res offset.
    """

def reverse_uvs(bm: bmesh.types.BMesh, faces: list[bmesh.types.BMFace] = []) -> None:
    """UV Reverse.Reverse the UVs

    :param bm: The bmesh to operate on.
    :param faces: Input faces.
    """

def rotate(
    bm: bmesh.types.BMesh,
    cent: collections.abc.Sequence[float] | mathutils.Vector = mathutils.Vector(),
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix = mathutils.Matrix.Identity(4),
    verts: list[bmesh.types.BMVert] = [],
    space: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix = mathutils.Matrix.Identity(4),
    use_shapekey: bool = False,
) -> None:
    """Rotate.Rotate vertices around a center, using a 3x3 rotation matrix.

    :param bm: The bmesh to operate on.
    :param cent: Center of rotation.
    :param matrix: Matrix defining rotation.
    :param verts: Input vertices.
    :param space: Matrix to define the space (typically object matrix).
    :param use_shapekey: Transform shape keys too.
    """

def rotate_colors(
    bm: bmesh.types.BMesh,
    faces: list[bmesh.types.BMFace] = [],
    use_ccw: bool = False,
    color_index: int = 0,
) -> None:
    """Color Rotation.Cycle the loop colors

    :param bm: The bmesh to operate on.
    :param faces: Input faces.
    :param use_ccw: Rotate counter-clockwise if true, otherwise clockwise.
    :param color_index: Index into color attribute list.
    """

def rotate_edges(
    bm: bmesh.types.BMesh, edges: list[bmesh.types.BMEdge] = [], use_ccw: bool = False
) -> dict[str, typing.Any]:
    """Edge Rotate.Rotates edges topologically. Also known as "spin edge" to some people.
    Simple example: [/] becomes [|] then [\].

        :param bm: The bmesh to operate on.
        :param edges: Input edges.
        :param use_ccw: Rotate edge counter-clockwise if true, otherwise clockwise.
        :return: edges:
    Newly spun edges.

    type list of (`bmesh.types.BMEdge`)
    """

def rotate_uvs(
    bm: bmesh.types.BMesh, faces: list[bmesh.types.BMFace] = [], use_ccw: bool = False
) -> None:
    """UV Rotation.Cycle the loop UVs

    :param bm: The bmesh to operate on.
    :param faces: Input faces.
    :param use_ccw: Rotate counter-clockwise if true, otherwise clockwise.
    """

def scale(
    bm: bmesh.types.BMesh,
    vec: collections.abc.Sequence[float] | mathutils.Vector = mathutils.Vector(),
    space: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix = mathutils.Matrix.Identity(4),
    verts: list[bmesh.types.BMVert] = [],
    use_shapekey: bool = False,
) -> None:
    """Scale.Scales vertices by an offset.

    :param bm: The bmesh to operate on.
    :param vec: Scale factor.
    :param space: Matrix to define the space (typically object matrix).
    :param verts: Input vertices.
    :param use_shapekey: Transform shape keys too.
    """

def smooth_laplacian_vert(
    bm: bmesh.types.BMesh,
    verts: list[bmesh.types.BMVert] = [],
    lambda_factor: float = 0,
    lambda_border: float = 0,
    use_x: bool = False,
    use_y: bool = False,
    use_z: bool = False,
    preserve_volume: bool = False,
) -> None:
    """Vertex Smooth Laplacian.Smooths vertices by using Laplacian smoothing propose by.
    Desbrun, et al. Implicit Fairing of Irregular Meshes using Diffusion and Curvature Flow.

        :param bm: The bmesh to operate on.
        :param verts: Input vertices.
        :param lambda_factor: Lambda parameter.
        :param lambda_border: Lambda param in border.
        :param use_x: Smooth object along X axis.
        :param use_y: Smooth object along Y axis.
        :param use_z: Smooth object along Z axis.
        :param preserve_volume: Apply volume preservation after smooth.
    """

def smooth_vert(
    bm: bmesh.types.BMesh,
    verts: list[bmesh.types.BMVert] = [],
    factor: float = 0,
    mirror_clip_x: bool = False,
    mirror_clip_y: bool = False,
    mirror_clip_z: bool = False,
    clip_dist: float = 0,
    use_axis_x: bool = False,
    use_axis_y: bool = False,
    use_axis_z: bool = False,
) -> None:
    """Vertex Smooth.Smooths vertices by using a basic vertex averaging scheme.

    :param bm: The bmesh to operate on.
    :param verts: Input vertices.
    :param factor: Smoothing factor.
    :param mirror_clip_x: Set vertices close to the x axis before the operation to 0.
    :param mirror_clip_y: Set vertices close to the y axis before the operation to 0.
    :param mirror_clip_z: Set vertices close to the z axis before the operation to 0.
    :param clip_dist: Clipping threshold for the above three slots.
    :param use_axis_x: Smooth vertices along X axis.
    :param use_axis_y: Smooth vertices along Y axis.
    :param use_axis_z: Smooth vertices along Z axis.
    """

def solidify(
    bm: bmesh.types.BMesh,
    geom: list[bmesh.types.BMEdge]
    | list[bmesh.types.BMFace]
    | list[bmesh.types.BMVert] = [],
    thickness: float = 0,
) -> dict[str, typing.Any]:
    """Solidify.Turns a mesh into a shell with thickness

        :param bm: The bmesh to operate on.
        :param geom: Input geometry.
        :param thickness: Thickness.
        :return: geom:

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    """

def spin(
    bm: bmesh.types.BMesh,
    geom: list[bmesh.types.BMEdge]
    | list[bmesh.types.BMFace]
    | list[bmesh.types.BMVert] = [],
    cent: collections.abc.Sequence[float] | mathutils.Vector = mathutils.Vector(),
    axis: collections.abc.Sequence[float] | mathutils.Vector = mathutils.Vector(),
    dvec: collections.abc.Sequence[float] | mathutils.Vector = mathutils.Vector(),
    angle: float = 0,
    space: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix = mathutils.Matrix.Identity(4),
    steps: int = 0,
    use_merge: bool = False,
    use_normal_flip: bool = False,
    use_duplicate: bool = False,
) -> dict[str, typing.Any]:
    """Spin.Extrude or duplicate geometry a number of times,
    rotating and possibly translating after each step

        :param bm: The bmesh to operate on.
        :param geom: Input geometry.
        :param cent: Rotation center.
        :param axis: Rotation axis.
        :param dvec: Translation delta per step.
        :param angle: Total rotation angle (radians).
        :param space: Matrix to define the space (typically object matrix).
        :param steps: Number of steps.
        :param use_merge: Merge first/last when the angle is a full revolution.
        :param use_normal_flip: Create faces with reversed direction.
        :param use_duplicate: Duplicate or extrude?.
        :return: geom_last:
    Result of last step.

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    """

def split(
    bm: bmesh.types.BMesh,
    geom: list[bmesh.types.BMEdge]
    | list[bmesh.types.BMFace]
    | list[bmesh.types.BMVert] = [],
    dest: bmesh.types.BMesh | None = None,
    use_only_faces: bool = False,
) -> dict[str, typing.Any]:
    """Split Off Geometry.Disconnect geometry from adjacent edges and faces,
    optionally into a destination mesh.

        :param bm: The bmesh to operate on.
        :param geom: Input geometry.
        :param dest: Destination bmesh, if None will use current one.
        :param use_only_faces: When enabled. dont duplicate loose verts/edges.
        :return: geom:

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)

    boundary_map:
    Boundary edges from the split geometry that maps edges from the original geometry
    to the destination edges.

    When the source edges have been deleted, the destination edge will be used
    for both the key and the value.

    type dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace`

    isovert_map:

    type dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace`
    """

def split_edges(
    bm: bmesh.types.BMesh,
    edges: list[bmesh.types.BMEdge] = [],
    verts: list[bmesh.types.BMVert] = [],
    use_verts: bool = False,
) -> dict[str, typing.Any]:
    """Edge Split.Disconnects faces along input edges.

        :param bm: The bmesh to operate on.
        :param edges: Input edges.
        :param verts: Optional tag verts, use to have greater control of splits.
        :param use_verts: Use verts for splitting, else just find verts to split from edges.
        :return: edges:
    Old output disconnected edges.

    type list of (`bmesh.types.BMEdge`)
    """

def subdivide_edgering(
    bm: bmesh.types.BMesh,
    edges: list[bmesh.types.BMEdge] = [],
    interp_mode: typing.Literal["LINEAR", "PATH", "SURFACE"] = "LINEAR",
    smooth: float = 0,
    cuts: int = 0,
    profile_shape: typing.Literal[
        "SMOOTH", "SPHERE", "ROOT", "SHARP", "LINEAR", "INVERSE_SQUARE"
    ] = "SMOOTH",
    profile_shape_factor: float = 0,
) -> dict[str, typing.Any]:
    """Subdivide Edge-Ring.Take an edge-ring, and subdivide with interpolation options.

        :param bm: The bmesh to operate on.
        :param edges: Input vertices.
        :param interp_mode: Interpolation method.
        :param smooth: Smoothness factor.
        :param cuts: Number of cuts.
        :param profile_shape: Profile shape type.
        :param profile_shape_factor: How much intermediary new edges are shrunk/expanded.
        :return: faces:
    Output faces.

    type list of (`bmesh.types.BMFace`)
    """

def subdivide_edges(
    bm: bmesh.types.BMesh,
    edges: list[bmesh.types.BMEdge] = [],
    smooth: float = 0,
    smooth_falloff: typing.Literal[
        "SMOOTH", "SPHERE", "ROOT", "SHARP", "LINEAR", "INVERSE_SQUARE"
    ] = "SMOOTH",
    fractal: float = 0,
    along_normal: float = 0,
    cuts: int = 0,
    seed: int = 0,
    custom_patterns={},
    edge_percents={},
    quad_corner_type: typing.Literal[
        "STRAIGHT_CUT", "INNER_VERT", "PATH", "FAN"
    ] = "STRAIGHT_CUT",
    use_grid_fill: bool = False,
    use_single_edge: bool = False,
    use_only_quads: bool = False,
    use_sphere: bool = False,
    use_smooth_even: bool = False,
) -> dict[str, typing.Any]:
    """Subdivide Edges.Advanced operator for subdividing edges
    with options for face patterns, smoothing and randomization.

        :param bm: The bmesh to operate on.
        :param edges: Input edges.
        :param smooth: Smoothness factor.
        :param smooth_falloff: Smooth falloff type.
        :param fractal: Fractal randomness factor.
        :param along_normal: Apply fractal displacement along normal only.
        :param cuts: Number of cuts.
        :param seed: Seed for the random number generator.
        :param custom_patterns: Uses custom pointers.
        :param edge_percents: Undocumented.
        :param quad_corner_type: Quad corner type.
        :param use_grid_fill: Fill in fully-selected faces with a grid.
        :param use_single_edge: Tessellate the case of one edge selected in a quad or triangle.
        :param use_only_quads: Only subdivide quads (for loop-cut).
        :param use_sphere: For making new primitives only.
        :param use_smooth_even: Maintain even offset when smoothing.
        :return: geom_inner:

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)

    geom_split:

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)

    geom:
    Contains all output geometry.

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    """

def symmetrize(
    bm: bmesh.types.BMesh,
    input: list[bmesh.types.BMEdge]
    | list[bmesh.types.BMFace]
    | list[bmesh.types.BMVert] = [],
    direction: typing.Literal["-X", "-Y", "-Z", "X", "Y", "Z"] = "-X",
    dist: float = 0,
    use_shapekey: bool = False,
) -> dict[str, typing.Any]:
    """Symmetrize.Makes the mesh elements in the "input" slot symmetrical. Unlike
    normal mirroring, it only copies in one direction, as specified by
    the "direction" slot. The edges and faces that cross the plane of
    symmetry are split as needed to enforce symmetry.All new vertices, edges, and faces are added to the "geom.out" slot.

        :param bm: The bmesh to operate on.
        :param input: Input geometry.
        :param direction: Axis to use.
        :param dist: Minimum distance.
        :param use_shapekey: Transform shape keys too.
        :return: geom:

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    """

def transform(
    bm: bmesh.types.BMesh,
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix = mathutils.Matrix.Identity(4),
    space: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix = mathutils.Matrix.Identity(4),
    verts: list[bmesh.types.BMVert] = [],
    use_shapekey: bool = False,
) -> None:
    """Transform.Transforms a set of vertices by a matrix. Multiplies
    the vertex coordinates with the matrix.

        :param bm: The bmesh to operate on.
        :param matrix: Transform matrix.
        :param space: Matrix to define the space (typically object matrix).
        :param verts: Input vertices.
        :param use_shapekey: Transform shape keys too.
    """

def translate(
    bm: bmesh.types.BMesh,
    vec: collections.abc.Sequence[float] | mathutils.Vector = mathutils.Vector(),
    space: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix = mathutils.Matrix.Identity(4),
    verts: list[bmesh.types.BMVert] = [],
    use_shapekey: bool = False,
) -> None:
    """Translate.Translate vertices by an offset.

    :param bm: The bmesh to operate on.
    :param vec: Translation offset.
    :param space: Matrix to define the space (typically object matrix).
    :param verts: Input vertices.
    :param use_shapekey: Transform shape keys too.
    """

def triangle_fill(
    bm: bmesh.types.BMesh,
    use_beauty: bool = False,
    use_dissolve: bool = False,
    edges: list[bmesh.types.BMEdge] = [],
    normal: collections.abc.Sequence[float] | mathutils.Vector = mathutils.Vector(),
) -> dict[str, typing.Any]:
    """Triangle Fill.Fill edges with triangles

        :param bm: The bmesh to operate on.
        :param use_beauty: Use best triangulation division.
        :param use_dissolve: Dissolve resulting faces.
        :param edges: Input edges.
        :param normal: Optionally pass the fill normal to use.
        :return: geom:
    New faces and edges.

    type list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    """

def triangulate(
    bm: bmesh.types.BMesh,
    faces: list[bmesh.types.BMFace] = [],
    quad_method: typing.Literal[
        "BEAUTY", "FIXED", "ALTERNATE", "SHORT_EDGE", "LONG_EDGE"
    ] = "BEAUTY",
    ngon_method: typing.Literal["BEAUTY", "EAR_CLIP"] = "BEAUTY",
) -> dict[str, typing.Any]:
    """Triangulate.

        :param bm: The bmesh to operate on.
        :param faces: Input faces.
        :param quad_method: Method for splitting the quads into triangles.
        :param ngon_method: Method for splitting the polygons into triangles.
        :return: edges:

    type list of (`bmesh.types.BMEdge`)

    faces:

    type list of (`bmesh.types.BMFace`)

    face_map:

    type dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace`

    face_map_double:
    Duplicate faces.

    type dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace`
    """

def unsubdivide(
    bm: bmesh.types.BMesh, verts: list[bmesh.types.BMVert] = [], iterations: int = 0
) -> None:
    """Un-Subdivide.Reduce detail in geometry containing grids.

    :param bm: The bmesh to operate on.
    :param verts: Input vertices.
    :param iterations: Number of times to unsubdivide.
    """

def weld_verts(bm: bmesh.types.BMesh, targetmap={}, use_centroid: bool = False) -> None:
    """Weld Verts.Welds verts together (kind-of like remove doubles, merge, etc, all of which
    use or will use this BMOP). You pass in mappings from vertices to the vertices
    they weld with.

        :param bm: The bmesh to operate on.
        :param targetmap: Maps welded vertices to verts they should weld to.
        :param use_centroid: Merged vertices to their centroid position,
    otherwise the position of the target vertex is used.
    """

def wireframe(
    bm: bmesh.types.BMesh,
    faces: list[bmesh.types.BMFace] = [],
    thickness: float = 0,
    offset: float = 0,
    use_replace: bool = False,
    use_boundary: bool = False,
    use_even_offset: bool = False,
    use_crease: bool = False,
    crease_weight: float = 0,
    use_relative_offset: bool = False,
    material_offset: int = 0,
) -> dict[str, typing.Any]:
    """Wire Frame.Makes a wire-frame copy of faces.

        :param bm: The bmesh to operate on.
        :param faces: Input faces.
        :param thickness: Thickness.
        :param offset: Offset the thickness from the center.
        :param use_replace: Remove original geometry.
        :param use_boundary: Inset face boundaries.
        :param use_even_offset: Scale the offset to give more even thickness.
        :param use_crease: Crease hub edges for improved subdivision surface.
        :param crease_weight: The mean crease weight for resulting edges.
        :param use_relative_offset: Scale the offset by surrounding geometry.
        :param material_offset: Offset material index of generated faces.
        :return: faces:
    Output faces.

    type list of (`bmesh.types.BMFace`)
    """
