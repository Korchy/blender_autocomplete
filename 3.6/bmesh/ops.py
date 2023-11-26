import sys
import typing
import bmesh.types
import mathutils
import bpy.types

GenericType = typing.TypeVar("GenericType")


def average_vert_facedata(bm: 'bmesh.types.BMesh',
                          verts: typing.List['bmesh.types.BMVert'] = []):
    ''' Average Vertices Facevert Data. Merge uv/vcols associated with the input vertices at the bounding box center. (I know, it's not averaging but the vert_snap_to_bb_center is just too long).

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices
    :type verts: typing.List['bmesh.types.BMVert']
    '''

    pass


def beautify_fill(bm: 'bmesh.types.BMesh',
                  faces: typing.List['bmesh.types.BMFace'] = [],
                  edges: typing.List['bmesh.types.BMEdge'] = [],
                  use_restrict_tag: bool = False,
                  method: typing.Union[str, int] = 'AREA') -> typing.Dict:
    ''' Beautify Fill. Rotate edges to create more evenly spaced triangles.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    :param edges: edges that can be flipped
    :type edges: typing.List['bmesh.types.BMEdge']
    :param use_restrict_tag: restrict edge rotation to mixed tagged vertices
    :type use_restrict_tag: bool
    :param method: method to define what is beautiful
    :type method: typing.Union[str, int]
    :rtype: typing.Dict
    :return: - ``geom``: new flipped faces and edges **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    '''

    pass


def bevel(bm: 'bmesh.types.BMesh',
          geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.
                             List['bmesh.types.BMEdge'], typing.
                             List['bmesh.types.BMFace']] = [],
          offset: float = 0,
          offset_type: typing.Union[str, int] = 'OFFSET',
          profile_type: typing.Union[str, int] = 'SUPERELLIPSE',
          segments: int = 0,
          profile: float = 0,
          affect: typing.Union[str, int] = 'VERTICES',
          clamp_overlap: bool = False,
          material: int = 0,
          loop_slide: bool = False,
          mark_seam: bool = False,
          mark_sharp: bool = False,
          harden_normals: bool = False,
          face_strength_mode: typing.Union[str, int] = 'NONE',
          miter_outer: typing.Union[str, int] = 'SHARP',
          miter_inner: typing.Union[str, int] = 'SHARP',
          spread: float = 0,
          smoothresh: float = 0,
          custom_profile: 'bpy.types.bpy_struct' = None,
          vmesh_method: typing.Union[str, int] = 'ADJ') -> typing.Dict:
    ''' Bevel. Bevels edges and vertices

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param geom: input edges and vertices
    :type geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.List['bmesh.types.BMEdge'], typing.List['bmesh.types.BMFace']]
    :param offset: amount to offset beveled edge
    :type offset: float
    :param offset_type: how to measure the offset
    :type offset_type: typing.Union[str, int]
    :param profile_type: The profile type to use for bevel.
    :type profile_type: typing.Union[str, int]
    :param segments: number of segments in bevel
    :type segments: int
    :param profile: profile shape, 0->1 (.5=>round)
    :type profile: float
    :param affect: Whether to bevel vertices or edges.
    :type affect: typing.Union[str, int]
    :param clamp_overlap: do not allow beveled edges/vertices to overlap each other
    :type clamp_overlap: bool
    :param material: material for bevel faces, -1 means get from adjacent faces
    :type material: int
    :param loop_slide: prefer to slide along edges to having even widths
    :type loop_slide: bool
    :param mark_seam: extend edge data to allow seams to run across bevels
    :type mark_seam: bool
    :param mark_sharp: extend edge data to allow sharp edges to run across bevels
    :type mark_sharp: bool
    :param harden_normals: harden normals
    :type harden_normals: bool
    :param face_strength_mode: whether to set face strength, and which faces to set if so
    :type face_strength_mode: typing.Union[str, int]
    :param miter_outer: outer miter kind
    :type miter_outer: typing.Union[str, int]
    :param miter_inner: outer miter kind
    :type miter_inner: typing.Union[str, int]
    :param spread: amount to offset beveled edge
    :type spread: float
    :param smoothresh: for passing mesh's smoothresh, used in hardening
    :type smoothresh: float
    :param custom_profile: CurveProfile, if None ignored
    :type custom_profile: 'bpy.types.bpy_struct'
    :param vmesh_method: The method to use to create meshes at intersections.
    :type vmesh_method: typing.Union[str, int]
    :rtype: typing.Dict
    :return: - ``faces``: output faces **type** list of (`bmesh.types.BMFace`) - ``edges``: output edges **type** list of (`bmesh.types.BMEdge`) - ``verts``: output verts **type** list of (`bmesh.types.BMVert`)
    '''

    pass


def bisect_edges(bm: 'bmesh.types.BMesh',
                 edges: typing.List['bmesh.types.BMEdge'] = [],
                 cuts: int = 0,
                 edge_percents: typing.Dict = {}) -> typing.Dict:
    ''' Edge Bisect. Splits input edges (but doesn't do anything else). This creates a 2-valence vert.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    :param cuts: number of cuts
    :type cuts: int
    :param edge_percents: Undocumented.
    :type edge_percents: typing.Dict
    :rtype: typing.Dict
    :return: - ``geom_split``: newly created vertices and edges **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    '''

    pass


def bisect_plane(
        bm: 'bmesh.types.BMesh',
        geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.
                           List['bmesh.types.BMEdge'], typing.
                           List['bmesh.types.BMFace']] = [],
        dist: float = 0,
        plane_co: typing.Union[typing.Sequence[float],
                               'mathutils.Vector'] = 'mathutils.Vector()',
        plane_no: typing.Union[typing.Sequence[float],
                               'mathutils.Vector'] = 'mathutils.Vector()',
        use_snap_center: bool = False,
        clear_outer: bool = False,
        clear_inner: bool = False) -> typing.Dict:
    ''' Bisect Plane. Bisects the mesh by a plane (cut the mesh in half).

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param geom: input geometry
    :type geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.List['bmesh.types.BMEdge'], typing.List['bmesh.types.BMFace']]
    :param dist: minimum distance when testing if a vert is exactly on the plane
    :type dist: float
    :param plane_co: point on the plane
    :type plane_co: typing.Union[typing.Sequence[float], 'mathutils.Vector']
    :param plane_no: direction of the plane
    :type plane_no: typing.Union[typing.Sequence[float], 'mathutils.Vector']
    :param use_snap_center: snap axis aligned verts to the center
    :type use_snap_center: bool
    :param clear_outer: when enabled. remove all geometry on the positive side of the plane
    :type clear_outer: bool
    :param clear_inner: when enabled. remove all geometry on the negative side of the plane
    :type clear_inner: bool
    :rtype: typing.Dict
    :return: - ``geom_cut``: output geometry aligned with the plane (new and existing) **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`) - ``geom``: input and output geometry (result of cut). **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    '''

    pass


def bmesh_to_mesh(bm: 'bmesh.types.BMesh', mesh: 'bpy.types.Mesh',
                  object: 'bpy.types.Object'):
    ''' BMesh to Mesh. Converts a bmesh to a Mesh. This is reserved for exiting editmode.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param mesh: pointer to a mesh structure to fill in
    :type mesh: 'bpy.types.Mesh'
    :param object: pointer to an object structure
    :type object: 'bpy.types.Object'
    '''

    pass


def bridge_loops(bm: 'bmesh.types.BMesh',
                 edges: typing.List['bmesh.types.BMEdge'] = [],
                 use_pairs: bool = False,
                 use_cyclic: bool = False,
                 use_merge: bool = False,
                 merge_factor: float = 0,
                 twist_offset: int = 0) -> typing.Dict:
    ''' Bridge edge loops with faces.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    :param use_pairs: Undocumented.
    :type use_pairs: bool
    :param use_cyclic: Undocumented.
    :type use_cyclic: bool
    :param use_merge: merge rather than creating faces
    :type use_merge: bool
    :param merge_factor: merge factor
    :type merge_factor: float
    :param twist_offset: twist offset for closed loops
    :type twist_offset: int
    :rtype: typing.Dict
    :return: - ``faces``: new faces **type** list of (`bmesh.types.BMFace`) - ``edges``: new edges **type** list of (`bmesh.types.BMEdge`)
    '''

    pass


def collapse(bm: 'bmesh.types.BMesh',
             edges: typing.List['bmesh.types.BMEdge'] = [],
             uvs: bool = False):
    ''' Collapse Connected. Collapses connected vertices

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    :param uvs: also collapse UVs and such
    :type uvs: bool
    '''

    pass


def collapse_uvs(bm: 'bmesh.types.BMesh',
                 edges: typing.List['bmesh.types.BMEdge'] = []):
    ''' Collapse Connected UVs. Collapses connected UV vertices.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    '''

    pass


def connect_vert_pair(
        bm: 'bmesh.types.BMesh',
        verts: typing.List['bmesh.types.BMVert'] = [],
        verts_exclude: typing.List['bmesh.types.BMVert'] = [],
        faces_exclude: typing.List['bmesh.types.BMFace'] = []) -> typing.Dict:
    ''' Connect Verts. Split faces by adding edges that connect **verts**.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices
    :type verts: typing.List['bmesh.types.BMVert']
    :param verts_exclude: input vertices to explicitly exclude from connecting
    :type verts_exclude: typing.List['bmesh.types.BMVert']
    :param faces_exclude: input faces to explicitly exclude from connecting
    :type faces_exclude: typing.List['bmesh.types.BMFace']
    :rtype: typing.Dict
    :return: - ``edges``: **type** list of (`bmesh.types.BMEdge`)
    '''

    pass


def connect_verts(bm: 'bmesh.types.BMesh',
                  verts: typing.List['bmesh.types.BMVert'] = [],
                  faces_exclude: typing.List['bmesh.types.BMFace'] = [],
                  check_degenerate: bool = False) -> typing.Dict:
    ''' Connect Verts. Split faces by adding edges that connect **verts**.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices
    :type verts: typing.List['bmesh.types.BMVert']
    :param faces_exclude: input faces to explicitly exclude from connecting
    :type faces_exclude: typing.List['bmesh.types.BMFace']
    :param check_degenerate: prevent splits with overlaps & intersections
    :type check_degenerate: bool
    :rtype: typing.Dict
    :return: - ``edges``: **type** list of (`bmesh.types.BMEdge`)
    '''

    pass


def connect_verts_concave(bm: 'bmesh.types.BMesh',
                          faces: typing.List['bmesh.types.BMFace'] = []
                          ) -> typing.Dict:
    ''' Connect Verts to form Convex Faces. Ensures all faces are convex **faces**.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    :rtype: typing.Dict
    :return: - ``edges``: **type** list of (`bmesh.types.BMEdge`) - ``faces``: **type** list of (`bmesh.types.BMFace`)
    '''

    pass


def connect_verts_nonplanar(
        bm: 'bmesh.types.BMesh',
        angle_limit: float = 0,
        faces: typing.List['bmesh.types.BMFace'] = []) -> typing.Dict:
    ''' Connect Verts Across non Planer Faces. Split faces by connecting edges along non planer **faces**.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param angle_limit: total rotation angle (radians)
    :type angle_limit: float
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    :rtype: typing.Dict
    :return: - ``edges``: **type** list of (`bmesh.types.BMEdge`) - ``faces``: **type** list of (`bmesh.types.BMFace`)
    '''

    pass


def contextual_create(
        bm: 'bmesh.types.BMesh',
        geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.
                           List['bmesh.types.BMEdge'], typing.
                           List['bmesh.types.BMFace']] = [],
        mat_nr: int = 0,
        use_smooth: bool = False) -> typing.Dict:
    ''' Contextual Create. This is basically F-key, it creates new faces from vertices, makes stuff from edge nets, makes wire edges, etc. It also dissolves faces. Three verts become a triangle, four become a quad. Two become a wire edge.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param geom: input geometry.
    :type geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.List['bmesh.types.BMEdge'], typing.List['bmesh.types.BMFace']]
    :param mat_nr: material to use
    :type mat_nr: int
    :param use_smooth: smooth to use
    :type use_smooth: bool
    :rtype: typing.Dict
    :return: - ``faces``: newly-made face(s) **type** list of (`bmesh.types.BMFace`) - ``edges``: newly-made edge(s) **type** list of (`bmesh.types.BMEdge`)
    '''

    pass


def convex_hull(bm: 'bmesh.types.BMesh',
                input: typing.Union[typing.List['bmesh.types.BMVert'], typing.
                                    List['bmesh.types.BMEdge'], typing.
                                    List['bmesh.types.BMFace']] = [],
                use_existing_faces: bool = False) -> typing.Dict:
    ''' Convex Hull Builds a convex hull from the vertices in 'input'. If 'use_existing_faces' is true, the hull will not output triangles that are covered by a pre-existing face. All hull vertices, faces, and edges are added to 'geom.out'. Any input elements that end up inside the hull (i.e. are not used by an output face) are added to the 'interior_geom' slot. The 'unused_geom' slot will contain all interior geometry that is completely unused. Lastly, 'holes_geom' contains edges and faces that were in the input and are part of the hull.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param input: input geometry
    :type input: typing.Union[typing.List['bmesh.types.BMVert'], typing.List['bmesh.types.BMEdge'], typing.List['bmesh.types.BMFace']]
    :param use_existing_faces: skip hull triangles that are covered by a pre-existing face
    :type use_existing_faces: bool
    :rtype: typing.Dict
    :return: - ``geom``: **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`) - ``geom_interior``: **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`) - ``geom_unused``: **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`) - ``geom_holes``: **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    '''

    pass


def create_circle(bm: 'bmesh.types.BMesh',
                  cap_ends: bool = False,
                  cap_tris: bool = False,
                  segments: int = 0,
                  radius: float = 0,
                  matrix: typing.
                  Union[typing.Sequence[float],
                        'mathutils.Matrix'] = 'mathutils.Matrix.Identity(4)',
                  calc_uvs: bool = False) -> typing.Dict:
    ''' Creates a Circle.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param cap_ends: whether or not to fill in the ends with faces
    :type cap_ends: bool
    :param cap_tris: fill ends with triangles instead of ngons
    :type cap_tris: bool
    :param segments: number of vertices in the circle
    :type segments: int
    :param radius: Radius of the circle.
    :type radius: float
    :param matrix: matrix to multiply the new geometry with
    :type matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    :param calc_uvs: calculate default UVs
    :type calc_uvs: bool
    :rtype: typing.Dict
    :return: - ``verts``: output verts **type** list of (`bmesh.types.BMVert`)
    '''

    pass


def create_cone(bm: 'bmesh.types.BMesh',
                cap_ends: bool = False,
                cap_tris: bool = False,
                segments: int = 0,
                radius1: float = 0,
                radius2: float = 0,
                depth: float = 0,
                matrix: typing.
                Union[typing.Sequence[float],
                      'mathutils.Matrix'] = 'mathutils.Matrix.Identity(4)',
                calc_uvs: bool = False) -> typing.Dict:
    ''' Create Cone. Creates a cone with variable depth at both ends

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param cap_ends: whether or not to fill in the ends with faces
    :type cap_ends: bool
    :param cap_tris: fill ends with triangles instead of ngons
    :type cap_tris: bool
    :param segments: number of vertices in the base circle
    :type segments: int
    :param radius1: radius of one end
    :type radius1: float
    :param radius2: radius of the opposite
    :type radius2: float
    :param depth: distance between ends
    :type depth: float
    :param matrix: matrix to multiply the new geometry with
    :type matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    :param calc_uvs: calculate default UVs
    :type calc_uvs: bool
    :rtype: typing.Dict
    :return: - ``verts``: output verts **type** list of (`bmesh.types.BMVert`)
    '''

    pass


def create_cube(bm: 'bmesh.types.BMesh',
                size: float = 0,
                matrix: typing.
                Union[typing.Sequence[float],
                      'mathutils.Matrix'] = 'mathutils.Matrix.Identity(4)',
                calc_uvs: bool = False) -> typing.Dict:
    ''' Create Cube Creates a cube.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param size: size of the cube
    :type size: float
    :param matrix: matrix to multiply the new geometry with
    :type matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    :param calc_uvs: calculate default UVs
    :type calc_uvs: bool
    :rtype: typing.Dict
    :return: - ``verts``: output verts **type** list of (`bmesh.types.BMVert`)
    '''

    pass


def create_grid(bm: 'bmesh.types.BMesh',
                x_segments: int = 0,
                y_segments: int = 0,
                size: float = 0,
                matrix: typing.
                Union[typing.Sequence[float],
                      'mathutils.Matrix'] = 'mathutils.Matrix.Identity(4)',
                calc_uvs: bool = False) -> typing.Dict:
    ''' Create Grid. Creates a grid with a variable number of subdivisions

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param x_segments: number of x segments
    :type x_segments: int
    :param y_segments: number of y segments
    :type y_segments: int
    :param size: size of the grid
    :type size: float
    :param matrix: matrix to multiply the new geometry with
    :type matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    :param calc_uvs: calculate default UVs
    :type calc_uvs: bool
    :rtype: typing.Dict
    :return: - ``verts``: output verts **type** list of (`bmesh.types.BMVert`)
    '''

    pass


def create_icosphere(
        bm: 'bmesh.types.BMesh',
        subdivisions: int = 0,
        radius: float = 0,
        matrix: typing.
        Union[typing.Sequence[float],
              'mathutils.Matrix'] = 'mathutils.Matrix.Identity(4)',
        calc_uvs: bool = False) -> typing.Dict:
    ''' Create Ico-Sphere. Creates a grid with a variable number of subdivisions

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param subdivisions: how many times to recursively subdivide the sphere
    :type subdivisions: int
    :param radius: radius
    :type radius: float
    :param matrix: matrix to multiply the new geometry with
    :type matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    :param calc_uvs: calculate default UVs
    :type calc_uvs: bool
    :rtype: typing.Dict
    :return: - ``verts``: output verts **type** list of (`bmesh.types.BMVert`)
    '''

    pass


def create_monkey(bm: 'bmesh.types.BMesh',
                  matrix: typing.
                  Union[typing.Sequence[float],
                        'mathutils.Matrix'] = 'mathutils.Matrix.Identity(4)',
                  calc_uvs: bool = False) -> typing.Dict:
    ''' Create Suzanne. Creates a monkey (standard blender primitive).

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param matrix: matrix to multiply the new geometry with
    :type matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    :param calc_uvs: calculate default UVs
    :type calc_uvs: bool
    :rtype: typing.Dict
    :return: - ``verts``: output verts **type** list of (`bmesh.types.BMVert`)
    '''

    pass


def create_uvsphere(bm: 'bmesh.types.BMesh',
                    u_segments: int = 0,
                    v_segments: int = 0,
                    radius: float = 0,
                    matrix: typing.
                    Union[typing.Sequence[float],
                          'mathutils.Matrix'] = 'mathutils.Matrix.Identity(4)',
                    calc_uvs: bool = False) -> typing.Dict:
    ''' Create UV Sphere. Creates a grid with a variable number of subdivisions

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param u_segments: number of u segments
    :type u_segments: int
    :param v_segments: number of v segment
    :type v_segments: int
    :param radius: radius
    :type radius: float
    :param matrix: matrix to multiply the new geometry with
    :type matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    :param calc_uvs: calculate default UVs
    :type calc_uvs: bool
    :rtype: typing.Dict
    :return: - ``verts``: output verts **type** list of (`bmesh.types.BMVert`)
    '''

    pass


def create_vert(bm: 'bmesh.types.BMesh',
                co: typing.Union[typing.Sequence[float],
                                 'mathutils.Vector'] = 'mathutils.Vector()'
                ) -> typing.Dict:
    ''' Make Vertex. Creates a single vertex; this bmop was necessary for click-create-vertex.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param co: the coordinate of the new vert
    :type co: typing.Union[typing.Sequence[float], 'mathutils.Vector']
    :rtype: typing.Dict
    :return: - ``vert``: the new vert **type** list of (`bmesh.types.BMVert`)
    '''

    pass


def delete(bm: 'bmesh.types.BMesh',
           geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.
                              List['bmesh.types.BMEdge'], typing.
                              List['bmesh.types.BMFace']] = [],
           context: typing.Union[str, int] = 'VERTS'):
    ''' Delete Geometry. Utility operator to delete geometry.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param geom: input geometry
    :type geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.List['bmesh.types.BMEdge'], typing.List['bmesh.types.BMFace']]
    :param context: geometry types to delete
    :type context: typing.Union[str, int]
    '''

    pass


def dissolve_degenerate(bm: 'bmesh.types.BMesh',
                        dist: float = 0,
                        edges: typing.List['bmesh.types.BMEdge'] = []):
    ''' Degenerate Dissolve. Dissolve edges with no length, faces with no area.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param dist: maximum distance to consider degenerate
    :type dist: float
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    '''

    pass


def dissolve_edges(bm: 'bmesh.types.BMesh',
                   edges: typing.List['bmesh.types.BMEdge'] = [],
                   use_verts: bool = False,
                   use_face_split: bool = False) -> typing.Dict:
    ''' Dissolve Edges.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    :param use_verts: dissolve verts left between only 2 edges.
    :type use_verts: bool
    :param use_face_split: split off face corners to maintain surrounding geometry
    :type use_face_split: bool
    :rtype: typing.Dict
    :return: - ``region``: **type** list of (`bmesh.types.BMFace`)
    '''

    pass


def dissolve_faces(bm: 'bmesh.types.BMesh',
                   faces: typing.List['bmesh.types.BMFace'] = [],
                   use_verts: bool = False) -> typing.Dict:
    ''' Dissolve Faces.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    :param use_verts: dissolve verts left between only 2 edges.
    :type use_verts: bool
    :rtype: typing.Dict
    :return: - ``region``: **type** list of (`bmesh.types.BMFace`)
    '''

    pass


def dissolve_limit(bm: 'bmesh.types.BMesh',
                   angle_limit: float = 0,
                   use_dissolve_boundaries: bool = False,
                   verts: typing.List['bmesh.types.BMVert'] = [],
                   edges: typing.List['bmesh.types.BMEdge'] = [],
                   delimit: typing.Set = 'set()') -> typing.Dict:
    ''' Limited Dissolve. Dissolve planar faces and co-linear edges.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param angle_limit: total rotation angle (radians)
    :type angle_limit: float
    :param use_dissolve_boundaries: dissolve all vertices in between face boundaries
    :type use_dissolve_boundaries: bool
    :param verts: input vertices
    :type verts: typing.List['bmesh.types.BMVert']
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    :param delimit: delimit dissolve operation
    :type delimit: typing.Set
    :rtype: typing.Dict
    :return: - ``region``: **type** list of (`bmesh.types.BMFace`)
    '''

    pass


def dissolve_verts(bm: 'bmesh.types.BMesh',
                   verts: typing.List['bmesh.types.BMVert'] = [],
                   use_face_split: bool = False,
                   use_boundary_tear: bool = False):
    ''' Dissolve Verts.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices
    :type verts: typing.List['bmesh.types.BMVert']
    :param use_face_split: split off face corners to maintain surrounding geometry
    :type use_face_split: bool
    :param use_boundary_tear: split off face corners instead of merging faces
    :type use_boundary_tear: bool
    '''

    pass


def duplicate(bm: 'bmesh.types.BMesh',
              geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.
                                 List['bmesh.types.BMEdge'], typing.
                                 List['bmesh.types.BMFace']] = [],
              dest: 'bmesh.types.BMesh' = None,
              use_select_history: bool = False,
              use_edge_flip_from_face: bool = False) -> typing.Dict:
    ''' Duplicate Geometry. Utility operator to duplicate geometry, optionally into a destination mesh.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param geom: input geometry
    :type geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.List['bmesh.types.BMEdge'], typing.List['bmesh.types.BMFace']]
    :param dest: destination bmesh, if None will use current on
    :type dest: 'bmesh.types.BMesh'
    :param use_select_history: Undocumented.
    :type use_select_history: bool
    :param use_edge_flip_from_face: Undocumented.
    :type use_edge_flip_from_face: bool
    :rtype: typing.Dict
    :return: - ``geom_orig``: **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`) - ``geom``: **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`) - ``vert_map``: **type** dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace` - ``edge_map``: **type** dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace` - ``face_map``: **type** dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace` - ``boundary_map``: **type** dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace` - ``isovert_map``: **type** dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace`
    '''

    pass


def edgeloop_fill(bm: 'bmesh.types.BMesh',
                  edges: typing.List['bmesh.types.BMEdge'] = [],
                  mat_nr: int = 0,
                  use_smooth: bool = False) -> typing.Dict:
    ''' Edge Loop Fill. Create faces defined by one or more non overlapping edge loops.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    :param mat_nr: material to use
    :type mat_nr: int
    :param use_smooth: smooth state to use
    :type use_smooth: bool
    :rtype: typing.Dict
    :return: - ``faces``: new faces **type** list of (`bmesh.types.BMFace`)
    '''

    pass


def edgenet_fill(bm: 'bmesh.types.BMesh',
                 edges: typing.List['bmesh.types.BMEdge'] = [],
                 mat_nr: int = 0,
                 use_smooth: bool = False,
                 sides: int = 0) -> typing.Dict:
    ''' Edge Net Fill. Create faces defined by enclosed edges.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    :param mat_nr: material to use
    :type mat_nr: int
    :param use_smooth: smooth state to use
    :type use_smooth: bool
    :param sides: number of sides
    :type sides: int
    :rtype: typing.Dict
    :return: - ``faces``: new faces **type** list of (`bmesh.types.BMFace`)
    '''

    pass


def edgenet_prepare(bm: 'bmesh.types.BMesh',
                    edges: typing.List['bmesh.types.BMEdge'] = []
                    ) -> typing.Dict:
    ''' Edge-net Prepare. Identifies several useful edge loop cases and modifies them so they'll become a face when edgenet_fill is called. The cases covered are: - One single loop; an edge is added to connect the ends - Two loops; two edges are added to connect the endpoints (based on the shortest distance between each endpoint).

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    :rtype: typing.Dict
    :return: - ``edges``: new edges **type** list of (`bmesh.types.BMEdge`)
    '''

    pass


def extrude_discrete_faces(bm: 'bmesh.types.BMesh',
                           faces: typing.List['bmesh.types.BMFace'] = [],
                           use_normal_flip: bool = False,
                           use_select_history: bool = False) -> typing.Dict:
    ''' Individual Face Extrude. Extrudes faces individually.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    :param use_normal_flip: Create faces with reversed direction.
    :type use_normal_flip: bool
    :param use_select_history: pass to duplicate
    :type use_select_history: bool
    :rtype: typing.Dict
    :return: - ``faces``: output faces **type** list of (`bmesh.types.BMFace`)
    '''

    pass


def extrude_edge_only(bm: 'bmesh.types.BMesh',
                      edges: typing.List['bmesh.types.BMEdge'] = [],
                      use_normal_flip: bool = False,
                      use_select_history: bool = False) -> typing.Dict:
    ''' Extrude Only Edges. Extrudes Edges into faces, note that this is very simple, there's no fancy winged extrusion.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param edges: input vertices
    :type edges: typing.List['bmesh.types.BMEdge']
    :param use_normal_flip: Create faces with reversed direction.
    :type use_normal_flip: bool
    :param use_select_history: pass to duplicate
    :type use_select_history: bool
    :rtype: typing.Dict
    :return: - ``geom``: output geometry **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    '''

    pass


def extrude_face_region(
        bm: 'bmesh.types.BMesh',
        geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.
                           List['bmesh.types.BMEdge'], typing.
                           List['bmesh.types.BMFace']] = [],
        edges_exclude: typing.Set = 'set()',
        use_keep_orig: bool = False,
        use_normal_flip: bool = False,
        use_normal_from_adjacent: bool = False,
        use_dissolve_ortho_edges: bool = False,
        use_select_history: bool = False) -> typing.Dict:
    ''' Extrude Faces. Extrude operator (does not transform)

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param geom: edges and faces
    :type geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.List['bmesh.types.BMEdge'], typing.List['bmesh.types.BMFace']]
    :param edges_exclude: input edges to explicitly exclude from extrusion
    :type edges_exclude: typing.Set
    :param use_keep_orig: keep original geometry (requires ``geom`` to include edges).
    :type use_keep_orig: bool
    :param use_normal_flip: Create faces with reversed direction.
    :type use_normal_flip: bool
    :param use_normal_from_adjacent: Use winding from surrounding faces instead of this region.
    :type use_normal_from_adjacent: bool
    :param use_dissolve_ortho_edges: Dissolve edges whose faces form a flat surface.
    :type use_dissolve_ortho_edges: bool
    :param use_select_history: pass to duplicate
    :type use_select_history: bool
    :rtype: typing.Dict
    :return: - ``geom``: **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    '''

    pass


def extrude_vert_indiv(bm: 'bmesh.types.BMesh',
                       verts: typing.List['bmesh.types.BMVert'] = [],
                       use_select_history: bool = False) -> typing.Dict:
    ''' Individual Vertex Extrude. Extrudes wire edges from vertices.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices
    :type verts: typing.List['bmesh.types.BMVert']
    :param use_select_history: pass to duplicate
    :type use_select_history: bool
    :rtype: typing.Dict
    :return: - ``edges``: output wire edges **type** list of (`bmesh.types.BMEdge`) - ``verts``: output vertices **type** list of (`bmesh.types.BMVert`)
    '''

    pass


def face_attribute_fill(bm: 'bmesh.types.BMesh',
                        faces: typing.List['bmesh.types.BMFace'] = [],
                        use_normals: bool = False,
                        use_data: bool = False) -> typing.Dict:
    ''' Face Attribute Fill. Fill in faces with data from adjacent faces.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    :param use_normals: copy face winding
    :type use_normals: bool
    :param use_data: copy face data
    :type use_data: bool
    :rtype: typing.Dict
    :return: - ``faces_fail``: faces that could not be handled **type** list of (`bmesh.types.BMFace`)
    '''

    pass


def find_doubles(bm: 'bmesh.types.BMesh',
                 verts: typing.List['bmesh.types.BMVert'] = [],
                 keep_verts: typing.List['bmesh.types.BMVert'] = [],
                 dist: float = 0) -> typing.Dict:
    ''' Find Doubles. Takes input verts and find vertices they should weld to. Outputs a mapping slot suitable for use with the weld verts bmop. If keep_verts is used, vertices outside that set can only be merged with vertices in that set.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices
    :type verts: typing.List['bmesh.types.BMVert']
    :param keep_verts: list of verts to keep
    :type keep_verts: typing.List['bmesh.types.BMVert']
    :param dist: maximum distance
    :type dist: float
    :rtype: typing.Dict
    :return: - ``targetmap``: **type** dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace`
    '''

    pass


def flip_quad_tessellation(bm: 'bmesh.types.BMesh',
                           faces: typing.List['bmesh.types.BMFace'] = []):
    ''' Flip Quad Tessellation Flip the tessellation direction of the selected quads.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: Undocumented.
    :type faces: typing.List['bmesh.types.BMFace']
    '''

    pass


def grid_fill(bm: 'bmesh.types.BMesh',
              edges: typing.List['bmesh.types.BMEdge'] = [],
              mat_nr: int = 0,
              use_smooth: bool = False,
              use_interp_simple: bool = False) -> typing.Dict:
    ''' Grid Fill. Create faces defined by 2 disconnected edge loops (which share edges).

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    :param mat_nr: material to use
    :type mat_nr: int
    :param use_smooth: smooth state to use
    :type use_smooth: bool
    :param use_interp_simple: use simple interpolation
    :type use_interp_simple: bool
    :rtype: typing.Dict
    :return: - ``faces``: new faces **type** list of (`bmesh.types.BMFace`)
    '''

    pass


def holes_fill(bm: 'bmesh.types.BMesh',
               edges: typing.List['bmesh.types.BMEdge'] = [],
               sides: int = 0) -> typing.Dict:
    ''' Fill Holes. Fill boundary edges with faces, copying surrounding customdata.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    :param sides: number of face sides to fill
    :type sides: int
    :rtype: typing.Dict
    :return: - ``faces``: new faces **type** list of (`bmesh.types.BMFace`)
    '''

    pass


def inset_individual(bm: 'bmesh.types.BMesh',
                     faces: typing.List['bmesh.types.BMFace'] = [],
                     thickness: float = 0,
                     depth: float = 0,
                     use_even_offset: bool = False,
                     use_interpolate: bool = False,
                     use_relative_offset: bool = False) -> typing.Dict:
    ''' Face Inset (Individual). Insets individual faces.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    :param thickness: thickness
    :type thickness: float
    :param depth: depth
    :type depth: float
    :param use_even_offset: scale the offset to give more even thickness
    :type use_even_offset: bool
    :param use_interpolate: blend face data across the inset
    :type use_interpolate: bool
    :param use_relative_offset: scale the offset by surrounding geometry
    :type use_relative_offset: bool
    :rtype: typing.Dict
    :return: - ``faces``: output faces **type** list of (`bmesh.types.BMFace`)
    '''

    pass


def inset_region(bm: 'bmesh.types.BMesh',
                 faces: typing.List['bmesh.types.BMFace'] = [],
                 faces_exclude: typing.List['bmesh.types.BMFace'] = [],
                 use_boundary: bool = False,
                 use_even_offset: bool = False,
                 use_interpolate: bool = False,
                 use_relative_offset: bool = False,
                 use_edge_rail: bool = False,
                 thickness: float = 0,
                 depth: float = 0,
                 use_outset: bool = False) -> typing.Dict:
    ''' Face Inset (Regions). Inset or outset face regions.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    :param faces_exclude: input faces to explicitly exclude from inset
    :type faces_exclude: typing.List['bmesh.types.BMFace']
    :param use_boundary: inset face boundaries
    :type use_boundary: bool
    :param use_even_offset: scale the offset to give more even thickness
    :type use_even_offset: bool
    :param use_interpolate: blend face data across the inset
    :type use_interpolate: bool
    :param use_relative_offset: scale the offset by surrounding geometry
    :type use_relative_offset: bool
    :param use_edge_rail: inset the region along existing edges
    :type use_edge_rail: bool
    :param thickness: thickness
    :type thickness: float
    :param depth: depth
    :type depth: float
    :param use_outset: outset rather than inset
    :type use_outset: bool
    :rtype: typing.Dict
    :return: - ``faces``: output faces **type** list of (`bmesh.types.BMFace`)
    '''

    pass


def join_triangles(bm: 'bmesh.types.BMesh',
                   faces: typing.List['bmesh.types.BMFace'] = [],
                   cmp_seam: bool = False,
                   cmp_sharp: bool = False,
                   cmp_uvs: bool = False,
                   cmp_vcols: bool = False,
                   cmp_materials: bool = False,
                   angle_face_threshold: float = 0,
                   angle_shape_threshold: float = 0) -> typing.Dict:
    ''' Join Triangles. Tries to intelligently join triangles according to angle threshold and delimiters.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input geometry.
    :type faces: typing.List['bmesh.types.BMFace']
    :param cmp_seam: Compare seam
    :type cmp_seam: bool
    :param cmp_sharp: Compare sharp
    :type cmp_sharp: bool
    :param cmp_uvs: Compare UVs
    :type cmp_uvs: bool
    :param cmp_vcols: compare VCols
    :type cmp_vcols: bool
    :param cmp_materials: compare materials
    :type cmp_materials: bool
    :param angle_face_threshold: Undocumented.
    :type angle_face_threshold: float
    :param angle_shape_threshold: Undocumented.
    :type angle_shape_threshold: float
    :rtype: typing.Dict
    :return: - ``faces``: joined faces **type** list of (`bmesh.types.BMFace`)
    '''

    pass


def mesh_to_bmesh(bm: 'bmesh.types.BMesh',
                  mesh: 'bpy.types.Mesh',
                  object: 'bpy.types.Object',
                  use_shapekey: bool = False):
    ''' Mesh to BMesh. Load the contents of a mesh into the bmesh. this bmop is private, it's reserved exclusively for entering editmode.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param mesh: pointer to a Mesh structure
    :type mesh: 'bpy.types.Mesh'
    :param object: pointer to an Object structure
    :type object: 'bpy.types.Object'
    :param use_shapekey: load active shapekey coordinates into verts
    :type use_shapekey: bool
    '''

    pass


def mirror(bm: 'bmesh.types.BMesh',
           geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.
                              List['bmesh.types.BMEdge'], typing.
                              List['bmesh.types.BMFace']] = [],
           matrix: typing.
           Union[typing.Sequence[float],
                 'mathutils.Matrix'] = 'mathutils.Matrix.Identity(4)',
           merge_dist: float = 0,
           axis: typing.Union[str, int] = 'X',
           mirror_u: bool = False,
           mirror_v: bool = False,
           mirror_udim: bool = False,
           use_shapekey: bool = False) -> typing.Dict:
    ''' Mirror. Mirrors geometry along an axis. The resulting geometry is welded on using merge_dist. Pairs of original/mirrored vertices are welded using the merge_dist parameter (which defines the minimum distance for welding to happen).

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param geom: input geometry
    :type geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.List['bmesh.types.BMEdge'], typing.List['bmesh.types.BMFace']]
    :param matrix: matrix defining the mirror transformation
    :type matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    :param merge_dist: maximum distance for merging. does no merging if 0.
    :type merge_dist: float
    :param axis: the axis to use.
    :type axis: typing.Union[str, int]
    :param mirror_u: mirror UVs across the u axis
    :type mirror_u: bool
    :param mirror_v: mirror UVs across the v axis
    :type mirror_v: bool
    :param mirror_udim: mirror UVs in each tile
    :type mirror_udim: bool
    :param use_shapekey: Transform shape keys too.
    :type use_shapekey: bool
    :rtype: typing.Dict
    :return: - ``geom``: output geometry, mirrored **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    '''

    pass


def object_load_bmesh(bm: 'bmesh.types.BMesh', scene: 'bpy.types.Scene',
                      object: 'bpy.types.Object'):
    ''' Object Load BMesh. Loads a bmesh into an object/mesh. This is a "private" bmop.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param scene: pointer to an scene structure
    :type scene: 'bpy.types.Scene'
    :param object: pointer to an object structure
    :type object: 'bpy.types.Object'
    '''

    pass


def offset_edgeloops(bm: 'bmesh.types.BMesh',
                     edges: typing.List['bmesh.types.BMEdge'] = [],
                     use_cap_endpoint: bool = False) -> typing.Dict:
    ''' Edge-loop Offset. Creates edge loops based on simple edge-outset method.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    :param use_cap_endpoint: extend loop around end-points
    :type use_cap_endpoint: bool
    :rtype: typing.Dict
    :return: - ``edges``: output edges **type** list of (`bmesh.types.BMEdge`)
    '''

    pass


def planar_faces(bm: 'bmesh.types.BMesh',
                 faces: typing.List['bmesh.types.BMFace'] = [],
                 iterations: int = 0,
                 factor: float = 0) -> typing.Dict:
    ''' Planar Faces. Iteratively flatten faces.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input geometry.
    :type faces: typing.List['bmesh.types.BMFace']
    :param iterations: Number of times to flatten faces (for when connected faces are used)
    :type iterations: int
    :param factor: Influence for making planar each iteration
    :type factor: float
    :rtype: typing.Dict
    :return: - ``geom``: output slot, computed boundary geometry. **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    '''

    pass


def pointmerge(
        bm: 'bmesh.types.BMesh',
        verts: typing.List['bmesh.types.BMVert'] = [],
        merge_co: typing.Union[typing.Sequence[float],
                               'mathutils.Vector'] = 'mathutils.Vector()'):
    ''' Point Merge. Merge verts together at a point.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices (all verts will be merged into the first).
    :type verts: typing.List['bmesh.types.BMVert']
    :param merge_co: Position to merge at.
    :type merge_co: typing.Union[typing.Sequence[float], 'mathutils.Vector']
    '''

    pass


def pointmerge_facedata(bm: 'bmesh.types.BMesh',
                        verts: typing.List['bmesh.types.BMVert'] = [],
                        *,
                        vert_snap: 'bmesh.types.BMVert'):
    ''' Face-Data Point Merge. Merge uv/vcols at a specific vertex.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices
    :type verts: typing.List['bmesh.types.BMVert']
    :param vert_snap: snap vertex
    :type vert_snap: 'bmesh.types.BMVert'
    '''

    pass


def poke(bm: 'bmesh.types.BMesh',
         faces: typing.List['bmesh.types.BMFace'] = [],
         offset: float = 0,
         center_mode: typing.Union[str, int] = 'MEAN_WEIGHTED',
         use_relative_offset: bool = False) -> typing.Dict:
    ''' Pokes a face. Splits a face into a triangle fan.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    :param offset: center vertex offset along normal
    :type offset: float
    :param center_mode: calculation mode for center vertex
    :type center_mode: typing.Union[str, int]
    :param use_relative_offset: apply offset
    :type use_relative_offset: bool
    :rtype: typing.Dict
    :return: - ``verts``: output verts **type** list of (`bmesh.types.BMVert`) - ``faces``: output faces **type** list of (`bmesh.types.BMFace`)
    '''

    pass


def recalc_face_normals(bm: 'bmesh.types.BMesh',
                        faces: typing.List['bmesh.types.BMFace'] = []):
    ''' Right-Hand Faces. Computes an "outside" normal for the specified input faces.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    '''

    pass


def region_extend(bm: 'bmesh.types.BMesh',
                  geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.
                                     List['bmesh.types.BMEdge'], typing.
                                     List['bmesh.types.BMFace']] = [],
                  use_contract: bool = False,
                  use_faces: bool = False,
                  use_face_step: bool = False) -> typing.Dict:
    ''' Region Extend. used to implement the select more/less tools. this puts some geometry surrounding regions of geometry in geom into geom.out. if use_faces is 0 then geom.out spits out verts and edges, otherwise it spits out faces.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param geom: input geometry
    :type geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.List['bmesh.types.BMEdge'], typing.List['bmesh.types.BMFace']]
    :param use_contract: find boundary inside the regions, not outside.
    :type use_contract: bool
    :param use_faces: extend from faces instead of edges
    :type use_faces: bool
    :param use_face_step: step over connected faces
    :type use_face_step: bool
    :rtype: typing.Dict
    :return: - ``geom``: output slot, computed boundary geometry. **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    '''

    pass


def remove_doubles(bm: 'bmesh.types.BMesh',
                   verts: typing.List['bmesh.types.BMVert'] = [],
                   dist: float = 0):
    ''' Remove Doubles. Finds groups of vertices closer than dist and merges them together, using the weld verts bmop.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param verts: input verts
    :type verts: typing.List['bmesh.types.BMVert']
    :param dist: minimum distance
    :type dist: float
    '''

    pass


def reverse_colors(bm: 'bmesh.types.BMesh',
                   faces: typing.List['bmesh.types.BMFace'] = [],
                   color_index: int = 0):
    ''' Color Reverse Reverse the loop colors.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    :param color_index: index into color attribute list
    :type color_index: int
    '''

    pass


def reverse_faces(bm: 'bmesh.types.BMesh',
                  faces: typing.List['bmesh.types.BMFace'] = [],
                  flip_multires: bool = False):
    ''' Reverse Faces. Reverses the winding (vertex order) of faces. This has the effect of flipping the normal.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    :param flip_multires: maintain multi-res offset
    :type flip_multires: bool
    '''

    pass


def reverse_uvs(bm: 'bmesh.types.BMesh',
                faces: typing.List['bmesh.types.BMFace'] = []):
    ''' UV Reverse. Reverse the UVs

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    '''

    pass


def rotate(bm: 'bmesh.types.BMesh',
           cent: typing.Union[typing.Sequence[float],
                              'mathutils.Vector'] = 'mathutils.Vector()',
           matrix: typing.
           Union[typing.Sequence[float],
                 'mathutils.Matrix'] = 'mathutils.Matrix.Identity(4)',
           verts: typing.List['bmesh.types.BMVert'] = [],
           space: typing.
           Union[typing.Sequence[float],
                 'mathutils.Matrix'] = 'mathutils.Matrix.Identity(4)',
           use_shapekey: bool = False):
    ''' Rotate. Rotate vertices around a center, using a 3x3 rotation matrix.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param cent: center of rotation
    :type cent: typing.Union[typing.Sequence[float], 'mathutils.Vector']
    :param matrix: matrix defining rotation
    :type matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    :param verts: input vertices
    :type verts: typing.List['bmesh.types.BMVert']
    :param space: matrix to define the space (typically object matrix)
    :type space: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    :param use_shapekey: Transform shape keys too.
    :type use_shapekey: bool
    '''

    pass


def rotate_colors(bm: 'bmesh.types.BMesh',
                  faces: typing.List['bmesh.types.BMFace'] = [],
                  use_ccw: bool = False,
                  color_index: int = 0):
    ''' Color Rotation. Cycle the loop colors

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    :param use_ccw: rotate counter-clockwise if true, otherwise clockwise
    :type use_ccw: bool
    :param color_index: index into color attribute list
    :type color_index: int
    '''

    pass


def rotate_edges(bm: 'bmesh.types.BMesh',
                 edges: typing.List['bmesh.types.BMEdge'] = [],
                 use_ccw: bool = False) -> typing.Dict:
    ''' Edge Rotate. Rotates edges topologically. Also known as "spin edge" to some people. Simple example: `[/] becomes [|] then [\]`.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    :param use_ccw: rotate edge counter-clockwise if true, otherwise clockwise
    :type use_ccw: bool
    :rtype: typing.Dict
    :return: - ``edges``: newly spun edges **type** list of (`bmesh.types.BMEdge`)
    '''

    pass


def rotate_uvs(bm: 'bmesh.types.BMesh',
               faces: typing.List['bmesh.types.BMFace'] = [],
               use_ccw: bool = False):
    ''' UV Rotation. Cycle the loop UVs

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    :param use_ccw: rotate counter-clockwise if true, otherwise clockwise
    :type use_ccw: bool
    '''

    pass


def scale(bm: 'bmesh.types.BMesh',
          vec: typing.Union[typing.Sequence[float],
                            'mathutils.Vector'] = 'mathutils.Vector()',
          space: typing.
          Union[typing.Sequence[float],
                'mathutils.Matrix'] = 'mathutils.Matrix.Identity(4)',
          verts: typing.List['bmesh.types.BMVert'] = [],
          use_shapekey: bool = False):
    ''' Scale. Scales vertices by an offset.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param vec: scale factor
    :type vec: typing.Union[typing.Sequence[float], 'mathutils.Vector']
    :param space: matrix to define the space (typically object matrix)
    :type space: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    :param verts: input vertices
    :type verts: typing.List['bmesh.types.BMVert']
    :param use_shapekey: Transform shape keys too.
    :type use_shapekey: bool
    '''

    pass


def smooth_laplacian_vert(bm: 'bmesh.types.BMesh',
                          verts: typing.List['bmesh.types.BMVert'] = [],
                          lambda_factor: float = 0,
                          lambda_border: float = 0,
                          use_x: bool = False,
                          use_y: bool = False,
                          use_z: bool = False,
                          preserve_volume: bool = False):
    ''' Vertex Smooth Laplacian. Smooths vertices by using Laplacian smoothing propose by. Desbrun, et al. Implicit Fairing of Irregular Meshes using Diffusion and Curvature Flow.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices
    :type verts: typing.List['bmesh.types.BMVert']
    :param lambda_factor: lambda param
    :type lambda_factor: float
    :param lambda_border: lambda param in border
    :type lambda_border: float
    :param use_x: Smooth object along X axis
    :type use_x: bool
    :param use_y: Smooth object along Y axis
    :type use_y: bool
    :param use_z: Smooth object along Z axis
    :type use_z: bool
    :param preserve_volume: Apply volume preservation after smooth
    :type preserve_volume: bool
    '''

    pass


def smooth_vert(bm: 'bmesh.types.BMesh',
                verts: typing.List['bmesh.types.BMVert'] = [],
                factor: float = 0,
                mirror_clip_x: bool = False,
                mirror_clip_y: bool = False,
                mirror_clip_z: bool = False,
                clip_dist: float = 0,
                use_axis_x: bool = False,
                use_axis_y: bool = False,
                use_axis_z: bool = False):
    ''' Vertex Smooth. Smooths vertices by using a basic vertex averaging scheme.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices
    :type verts: typing.List['bmesh.types.BMVert']
    :param factor: smoothing factor
    :type factor: float
    :param mirror_clip_x: set vertices close to the x axis before the operation to 0
    :type mirror_clip_x: bool
    :param mirror_clip_y: set vertices close to the y axis before the operation to 0
    :type mirror_clip_y: bool
    :param mirror_clip_z: set vertices close to the z axis before the operation to 0
    :type mirror_clip_z: bool
    :param clip_dist: clipping threshold for the above three slots
    :type clip_dist: float
    :param use_axis_x: smooth vertices along X axis
    :type use_axis_x: bool
    :param use_axis_y: smooth vertices along Y axis
    :type use_axis_y: bool
    :param use_axis_z: smooth vertices along Z axis
    :type use_axis_z: bool
    '''

    pass


def solidify(bm: 'bmesh.types.BMesh',
             geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.
                                List['bmesh.types.BMEdge'], typing.
                                List['bmesh.types.BMFace']] = [],
             thickness: float = 0) -> typing.Dict:
    ''' Solidify. Turns a mesh into a shell with thickness

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param geom: input geometry
    :type geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.List['bmesh.types.BMEdge'], typing.List['bmesh.types.BMFace']]
    :param thickness: thickness
    :type thickness: float
    :rtype: typing.Dict
    :return: - ``geom``: **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    '''

    pass


def spin(bm: 'bmesh.types.BMesh',
         geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.
                            List['bmesh.types.BMEdge'], typing.
                            List['bmesh.types.BMFace']] = [],
         cent: typing.Union[typing.Sequence[float],
                            'mathutils.Vector'] = 'mathutils.Vector()',
         axis: typing.Union[typing.Sequence[float],
                            'mathutils.Vector'] = 'mathutils.Vector()',
         dvec: typing.Union[typing.Sequence[float],
                            'mathutils.Vector'] = 'mathutils.Vector()',
         angle: float = 0,
         space: typing.
         Union[typing.Sequence[float],
               'mathutils.Matrix'] = 'mathutils.Matrix.Identity(4)',
         steps: int = 0,
         use_merge: bool = False,
         use_normal_flip: bool = False,
         use_duplicate: bool = False) -> typing.Dict:
    ''' Spin. Extrude or duplicate geometry a number of times, rotating and possibly translating after each step

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param geom: input geometry
    :type geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.List['bmesh.types.BMEdge'], typing.List['bmesh.types.BMFace']]
    :param cent: rotation center
    :type cent: typing.Union[typing.Sequence[float], 'mathutils.Vector']
    :param axis: rotation axis
    :type axis: typing.Union[typing.Sequence[float], 'mathutils.Vector']
    :param dvec: translation delta per step
    :type dvec: typing.Union[typing.Sequence[float], 'mathutils.Vector']
    :param angle: total rotation angle (radians)
    :type angle: float
    :param space: matrix to define the space (typically object matrix)
    :type space: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    :param steps: number of steps
    :type steps: int
    :param use_merge: Merge first/last when the angle is a full revolution.
    :type use_merge: bool
    :param use_normal_flip: Create faces with reversed direction.
    :type use_normal_flip: bool
    :param use_duplicate: duplicate or extrude?
    :type use_duplicate: bool
    :rtype: typing.Dict
    :return: - ``geom_last``: result of last step **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    '''

    pass


def split(bm: 'bmesh.types.BMesh',
          geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.
                             List['bmesh.types.BMEdge'], typing.
                             List['bmesh.types.BMFace']] = [],
          dest: 'bmesh.types.BMesh' = None,
          use_only_faces: bool = False) -> typing.Dict:
    ''' Split Off Geometry. Disconnect geometry from adjacent edges and faces, optionally into a destination mesh.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param geom: input geometry
    :type geom: typing.Union[typing.List['bmesh.types.BMVert'], typing.List['bmesh.types.BMEdge'], typing.List['bmesh.types.BMFace']]
    :param dest: destination bmesh, if None will use current one
    :type dest: 'bmesh.types.BMesh'
    :param use_only_faces: when enabled. don't duplicate loose verts/edges
    :type use_only_faces: bool
    :rtype: typing.Dict
    :return: - ``geom``: **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`) - ``boundary_map``: **type** dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace` - ``isovert_map``: **type** dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace`
    '''

    pass


def split_edges(bm: 'bmesh.types.BMesh',
                edges: typing.List['bmesh.types.BMEdge'] = [],
                verts: typing.List['bmesh.types.BMVert'] = [],
                use_verts: bool = False) -> typing.Dict:
    ''' Edge Split. Disconnects faces along input edges.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    :param verts: optional tag verts, use to have greater control of splits
    :type verts: typing.List['bmesh.types.BMVert']
    :param use_verts: use 'verts' for splitting, else just find verts to split from edges
    :type use_verts: bool
    :rtype: typing.Dict
    :return: - ``edges``: old output disconnected edges **type** list of (`bmesh.types.BMEdge`)
    '''

    pass


def subdivide_edgering(bm: 'bmesh.types.BMesh',
                       edges: typing.List['bmesh.types.BMEdge'] = [],
                       interp_mode: typing.Union[str, int] = 'LINEAR',
                       smooth: float = 0,
                       cuts: int = 0,
                       profile_shape: typing.Union[str, int] = 'SMOOTH',
                       profile_shape_factor: float = 0) -> typing.Dict:
    ''' Subdivide Edge-Ring. Take an edge-ring, and subdivide with interpolation options.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param edges: input vertices
    :type edges: typing.List['bmesh.types.BMEdge']
    :param interp_mode: interpolation method
    :type interp_mode: typing.Union[str, int]
    :param smooth: smoothness factor
    :type smooth: float
    :param cuts: number of cuts
    :type cuts: int
    :param profile_shape: profile shape type
    :type profile_shape: typing.Union[str, int]
    :param profile_shape_factor: how much intermediary new edges are shrunk/expanded
    :type profile_shape_factor: float
    :rtype: typing.Dict
    :return: - ``faces``: output faces **type** list of (`bmesh.types.BMFace`)
    '''

    pass


def subdivide_edges(bm: 'bmesh.types.BMesh',
                    edges: typing.List['bmesh.types.BMEdge'] = [],
                    smooth: float = 0,
                    smooth_falloff: typing.Union[str, int] = 'SMOOTH',
                    fractal: float = 0,
                    along_normal: float = 0,
                    cuts: int = 0,
                    seed: int = 0,
                    custom_patterns: typing.Dict = {},
                    edge_percents: typing.Dict = {},
                    quad_corner_type: typing.Union[str, int] = 'STRAIGHT_CUT',
                    use_grid_fill: bool = False,
                    use_single_edge: bool = False,
                    use_only_quads: bool = False,
                    use_sphere: bool = False,
                    use_smooth_even: bool = False) -> typing.Dict:
    ''' Subdivide Edges. Advanced operator for subdividing edges with options for face patterns, smoothing and randomization.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    :param smooth: smoothness factor
    :type smooth: float
    :param smooth_falloff: smooth falloff type
    :type smooth_falloff: typing.Union[str, int]
    :param fractal: fractal randomness factor
    :type fractal: float
    :param along_normal: apply fractal displacement along normal only
    :type along_normal: float
    :param cuts: number of cuts
    :type cuts: int
    :param seed: seed for the random number generator
    :type seed: int
    :param custom_patterns: uses custom pointers
    :type custom_patterns: typing.Dict
    :param edge_percents: Undocumented.
    :type edge_percents: typing.Dict
    :param quad_corner_type: quad corner type
    :type quad_corner_type: typing.Union[str, int]
    :param use_grid_fill: fill in fully-selected faces with a grid
    :type use_grid_fill: bool
    :param use_single_edge: tessellate the case of one edge selected in a quad or triangle
    :type use_single_edge: bool
    :param use_only_quads: Only subdivide quads (for loop-cut).
    :type use_only_quads: bool
    :param use_sphere: for making new primitives only
    :type use_sphere: bool
    :param use_smooth_even: maintain even offset when smoothing
    :type use_smooth_even: bool
    :rtype: typing.Dict
    :return: - ``geom_inner``: **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`) - ``geom_split``: **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`) - ``geom``: contains all output geometry **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    '''

    pass


def symmetrize(bm: 'bmesh.types.BMesh',
               input: typing.Union[typing.List['bmesh.types.BMVert'], typing.
                                   List['bmesh.types.BMEdge'], typing.
                                   List['bmesh.types.BMFace']] = [],
               direction: typing.Union[str, int] = '-X',
               dist: float = 0,
               use_shapekey: bool = False) -> typing.Dict:
    ''' Symmetrize. Makes the mesh elements in the "input" slot symmetrical. Unlike normal mirroring, it only copies in one direction, as specified by the "direction" slot. The edges and faces that cross the plane of symmetry are split as needed to enforce symmetry. All new vertices, edges, and faces are added to the "geom.out" slot.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param input: input geometry
    :type input: typing.Union[typing.List['bmesh.types.BMVert'], typing.List['bmesh.types.BMEdge'], typing.List['bmesh.types.BMFace']]
    :param direction: axis to use
    :type direction: typing.Union[str, int]
    :param dist: minimum distance
    :type dist: float
    :param use_shapekey: Transform shape keys too.
    :type use_shapekey: bool
    :rtype: typing.Dict
    :return: - ``geom``: **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    '''

    pass


def transform(bm: 'bmesh.types.BMesh',
              matrix: typing.
              Union[typing.Sequence[float],
                    'mathutils.Matrix'] = 'mathutils.Matrix.Identity(4)',
              space: typing.
              Union[typing.Sequence[float],
                    'mathutils.Matrix'] = 'mathutils.Matrix.Identity(4)',
              verts: typing.List['bmesh.types.BMVert'] = [],
              use_shapekey: bool = False):
    ''' Transform. Transforms a set of vertices by a matrix. Multiplies the vertex coordinates with the matrix.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param matrix: transform matrix
    :type matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    :param space: matrix to define the space (typically object matrix)
    :type space: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    :param verts: input vertices
    :type verts: typing.List['bmesh.types.BMVert']
    :param use_shapekey: Transform shape keys too.
    :type use_shapekey: bool
    '''

    pass


def translate(bm: 'bmesh.types.BMesh',
              vec: typing.Union[typing.Sequence[float],
                                'mathutils.Vector'] = 'mathutils.Vector()',
              space: typing.
              Union[typing.Sequence[float],
                    'mathutils.Matrix'] = 'mathutils.Matrix.Identity(4)',
              verts: typing.List['bmesh.types.BMVert'] = [],
              use_shapekey: bool = False):
    ''' Translate. Translate vertices by an offset.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param vec: translation offset
    :type vec: typing.Union[typing.Sequence[float], 'mathutils.Vector']
    :param space: matrix to define the space (typically object matrix)
    :type space: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    :param verts: input vertices
    :type verts: typing.List['bmesh.types.BMVert']
    :param use_shapekey: Transform shape keys too.
    :type use_shapekey: bool
    '''

    pass


def triangle_fill(
        bm: 'bmesh.types.BMesh',
        use_beauty: bool = False,
        use_dissolve: bool = False,
        edges: typing.List['bmesh.types.BMEdge'] = [],
        normal: typing.Union[typing.Sequence[float],
                             'mathutils.Vector'] = 'mathutils.Vector()'
) -> typing.Dict:
    ''' Triangle Fill. Fill edges with triangles

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param use_beauty: use best triangulation division
    :type use_beauty: bool
    :param use_dissolve: dissolve resulting faces
    :type use_dissolve: bool
    :param edges: input edges
    :type edges: typing.List['bmesh.types.BMEdge']
    :param normal: optionally pass the fill normal to use
    :type normal: typing.Union[typing.Sequence[float], 'mathutils.Vector']
    :rtype: typing.Dict
    :return: - ``geom``: new faces and edges **type** list of (`bmesh.types.BMVert`, `bmesh.types.BMEdge`, `bmesh.types.BMFace`)
    '''

    pass


def triangulate(bm: 'bmesh.types.BMesh',
                faces: typing.List['bmesh.types.BMFace'] = [],
                quad_method: typing.Union[str, int] = 'BEAUTY',
                ngon_method: typing.Union[str, int] = 'BEAUTY') -> typing.Dict:
    ''' Triangulate.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    :param quad_method: method for splitting the quads into triangles
    :type quad_method: typing.Union[str, int]
    :param ngon_method: method for splitting the polygons into triangles
    :type ngon_method: typing.Union[str, int]
    :rtype: typing.Dict
    :return: - ``edges``: **type** list of (`bmesh.types.BMEdge`) - ``faces``: **type** list of (`bmesh.types.BMFace`) - ``face_map``: **type** dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace` - ``face_map_double``: duplicate faces **type** dict mapping vert/edge/face types to `bmesh.types.BMVert`/`bmesh.types.BMEdge`/`bmesh.types.BMFace`
    '''

    pass


def unsubdivide(bm: 'bmesh.types.BMesh',
                verts: typing.List['bmesh.types.BMVert'] = [],
                iterations: int = 0):
    ''' Un-Subdivide. Reduce detail in geometry containing grids.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices
    :type verts: typing.List['bmesh.types.BMVert']
    :param iterations: number of times to unsubdivide
    :type iterations: int
    '''

    pass


def weld_verts(bm: 'bmesh.types.BMesh', targetmap: typing.Dict = {}):
    ''' Weld Verts. Welds verts together (kind-of like remove doubles, merge, etc, all of which use or will use this bmop). You pass in mappings from vertices to the vertices they weld with.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param targetmap: maps welded vertices to verts they should weld to
    :type targetmap: typing.Dict
    '''

    pass


def wireframe(bm: 'bmesh.types.BMesh',
              faces: typing.List['bmesh.types.BMFace'] = [],
              thickness: float = 0,
              offset: float = 0,
              use_replace: bool = False,
              use_boundary: bool = False,
              use_even_offset: bool = False,
              use_crease: bool = False,
              crease_weight: float = 0,
              use_relative_offset: bool = False,
              material_offset: int = 0) -> typing.Dict:
    ''' Wire Frame. Makes a wire-frame copy of faces.

    :param bm: The bmesh to operate on.
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces
    :type faces: typing.List['bmesh.types.BMFace']
    :param thickness: thickness
    :type thickness: float
    :param offset: offset the thickness from the center
    :type offset: float
    :param use_replace: remove original geometry
    :type use_replace: bool
    :param use_boundary: inset face boundaries
    :type use_boundary: bool
    :param use_even_offset: scale the offset to give more even thickness
    :type use_even_offset: bool
    :param use_crease: crease hub edges for improved subdivision surface
    :type use_crease: bool
    :param crease_weight: the mean crease weight for resulting edges
    :type crease_weight: float
    :param use_relative_offset: scale the offset by surrounding geometry
    :type use_relative_offset: bool
    :param material_offset: offset material index of generated faces
    :type material_offset: int
    :rtype: typing.Dict
    :return: - ``faces``: output faces **type** list of (`bmesh.types.BMFace`)
    '''

    pass
