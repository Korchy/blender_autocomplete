import sys
import typing
import bmesh
import mathutils
import bpy
from bmesh.types import BMFaceSeq


def automerge(bm: 'bmesh.types.BMesh',
              verts: typing.List['bmesh.types.BMVert'], dist: float):
    '''Finds groups of vertices closer then dist and merges them together, using the weld verts bmop. The merges must go from a vert not in verts to one in verts. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param verts: input verts 
    :type verts: typing.List['bmesh.types.BMVert']
    :param dist: minimum distance 
    :type dist: float
    '''

    pass


def average_vert_facedata(bm: 'bmesh.types.BMesh',
                          verts: typing.List['bmesh.types.BMVert']):
    '''Merge uv/vcols associated with the input vertices at the bounding box center. (I know, it’s not averaging but the vert_snap_to_bb_center is just too long). 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices 
    :type verts: typing.List['bmesh.types.BMVert']
    '''

    pass


def beautify_fill(bm: 'bmesh.types.BMesh',
                  faces: typing.List['bmesh.types.BMFace'],
                  edges: typing.List['bmesh.types.BMEdge'],
                  use_restrict_tag: bool, method: int) -> dict:
    '''Rotate edges to create more evenly spaced triangles. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces 
    :type faces: typing.List['bmesh.types.BMFace']
    :param edges: edges that can be flipped 
    :type edges: typing.List['bmesh.types.BMEdge']
    :param use_restrict_tag: restrict edge rotation to mixed tagged vertices 
    :type use_restrict_tag: bool
    :param method: method to define what is beautiful 
    :type method: int
    :return:  geom: new flipped faces and edgestype list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def bevel(bm: 'bmesh.types.BMesh', geom: typing.List['bmesh.types.BMVert'],
          offset: float, offset_type: int, segments: int, profile: float,
          vertex_only: bool, clamp_overlap: bool, material: int,
          loop_slide: bool) -> dict:
    '''Bevels edges and vertices 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param geom: input edges and vertices 
    :type geom: typing.List['bmesh.types.BMVert']
    :param offset: amount to offset beveled edge 
    :type offset: float
    :param offset_type: how to measure offset (enum) 
    :type offset_type: int
    :param segments: number of segments in bevel 
    :type segments: int
    :param profile: profile shape, 0->1 (.5=>round) 
    :type profile: float
    :param vertex_only: only bevel vertices, not edges 
    :type vertex_only: bool
    :param clamp_overlap: do not allow beveled edges/vertices to overlap each other 
    :type clamp_overlap: bool
    :param material: material for bevel faces, -1 means get from adjacent faces 
    :type material: int
    :param loop_slide: prefer to slide along edges to having even widths 
    :type loop_slide: bool
    :return:  faces: output facestype list of (bmesh.types.BMFace)edges: output edgestype list of (bmesh.types.BMEdge)verts: output vertstype list of (bmesh.types.BMVert) 
    '''

    pass


def bisect_edges(bm: 'bmesh.types.BMesh',
                 edges: typing.List['bmesh.types.BMEdge'], cuts: int,
                 edge_percents: dict = None) -> dict:
    '''Splits input edges (but doesn’t do anything else). This creates a 2-valence vert. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges 
    :type edges: typing.List['bmesh.types.BMEdge']
    :param cuts: number of cuts 
    :type cuts: int
    :param edge_percents: Undocumented. 
    :type edge_percents: dict
    :return:  geom_split: newly created vertices and edgestype list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def bisect_plane(bm: 'bmesh.types.BMesh',
                 geom: typing.List['bmesh.types.BMVert'], dist: float,
                 plane_co: 'mathutils.Vector', plane_no: 'mathutils.Vector',
                 use_snap_center: bool, clear_outer: bool,
                 clear_inner: bool) -> dict:
    '''Bisects the mesh by a plane (cut the mesh in half). 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param geom: Undocumented. 
    :type geom: typing.List['bmesh.types.BMVert']
    :param dist: minimum distance when testing if a vert is exactly on the plane 
    :type dist: float
    :param plane_co: point on the plane 
    :type plane_co: 'mathutils.Vector'
    :param plane_no: direction of the plane 
    :type plane_no: 'mathutils.Vector'
    :param use_snap_center: snap axis aligned verts to the center 
    :type use_snap_center: bool
    :param clear_outer: when enabled. remove all geometry on the positive side of the plane 
    :type clear_outer: bool
    :param clear_inner: when enabled. remove all geometry on the negative side of the plane 
    :type clear_inner: bool
    :return:  geom_cut: output geometry aligned with the plane (new and existing)type list of (bmesh.types.BMVert, bmesh.types.BMEdge)geom: input and output geometry (result of cut)type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def bmesh_to_mesh(bm: 'bmesh.types.BMesh', mesh: 'bpy.types.Mesh',
                  object: 'bpy.types.Object', skip_tessface: bool):
    '''Converts a bmesh to a Mesh. This is reserved for exiting editmode. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param mesh: Undocumented. 
    :type mesh: 'bpy.types.Mesh'
    :param object: Undocumented. 
    :type object: 'bpy.types.Object'
    :param skip_tessface: don’t calculate mfaces 
    :type skip_tessface: bool
    '''

    pass


def bridge_loops(bm: 'bmesh.types.BMesh',
                 edges: typing.List['bmesh.types.BMEdge'], use_pairs: bool,
                 use_cyclic: bool, use_merge: bool, merge_factor: float,
                 twist_offset: int) -> dict:
    '''Bridge edge loops with faces. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges 
    :type edges: typing.List['bmesh.types.BMEdge']
    :param use_pairs: Undocumented. 
    :type use_pairs: bool
    :param use_cyclic: Undocumented. 
    :type use_cyclic: bool
    :param use_merge: Undocumented. 
    :type use_merge: bool
    :param merge_factor: Undocumented. 
    :type merge_factor: float
    :param twist_offset: Undocumented. 
    :type twist_offset: int
    :return:  faces: new facestype list of (bmesh.types.BMFace)edges: new edgestype list of (bmesh.types.BMEdge) 
    '''

    pass


def collapse(bm: 'bmesh.types.BMesh', edges: typing.List['bmesh.types.BMEdge'],
             uvs: bool):
    '''Collapses connected vertices 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges 
    :type edges: typing.List['bmesh.types.BMEdge']
    :param uvs: also collapse UVs and such 
    :type uvs: bool
    '''

    pass


def collapse_uvs(bm: 'bmesh.types.BMesh',
                 edges: typing.List['bmesh.types.BMEdge']):
    '''Collapses connected UV vertices. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges 
    :type edges: typing.List['bmesh.types.BMEdge']
    '''

    pass


def connect_vert_pair(
        bm: 'bmesh.types.BMesh', verts: typing.List['bmesh.types.BMVert'],
        verts_exclude: typing.List['bmesh.types.BMVert'] = [],
        faces_exclude: typing.List['bmesh.types.BMFace'] = []
) -> dict:
    '''Split faces by adding edges that connect verts. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param verts: Undocumented. 
    :type verts: typing.List['bmesh.types.BMVert']
    :param verts_exclude: Undocumented. 
    :type verts_exclude: typing.List['bmesh.types.BMVert']
    :param faces_exclude: Undocumented. 
    :type faces_exclude: typing.List['bmesh.types.BMFace']
    :return:  edges:type list of (bmesh.types.BMEdge) 
    '''

    pass


def connect_verts(bm: 'bmesh.types.BMesh',
                  verts: typing.List['bmesh.types.BMVert'],
                  faces_exclude: typing.List['bmesh.types.BMFace'],
                  check_degenerate: bool) -> dict:
    '''Split faces by adding edges that connect verts. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param verts: Undocumented. 
    :type verts: typing.List['bmesh.types.BMVert']
    :param faces_exclude: Undocumented. 
    :type faces_exclude: typing.List['bmesh.types.BMFace']
    :param check_degenerate: prevent splits with overlaps & intersections 
    :type check_degenerate: bool
    :return:  edges:type list of (bmesh.types.BMEdge) 
    '''

    pass


def connect_verts_concave(bm: 'bmesh.types.BMesh',
                          faces: typing.List['bmesh.types.BMFace']) -> dict:
    '''Ensures all faces are convex faces. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: Undocumented. 
    :type faces: typing.List['bmesh.types.BMFace']
    :return:  edges:type list of (bmesh.types.BMEdge)faces:type list of (bmesh.types.BMFace) 
    '''

    pass


def connect_verts_nonplanar(bm: 'bmesh.types.BMesh', angle_limit: float,
                            faces: typing.List['bmesh.types.BMFace']) -> dict:
    '''Split faces by connecting edges along non planer faces. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param angle_limit: total rotation angle (radians) 
    :type angle_limit: float
    :param faces: Undocumented. 
    :type faces: typing.List['bmesh.types.BMFace']
    :return:  edges:type list of (bmesh.types.BMEdge)faces:type list of (bmesh.types.BMFace) 
    '''

    pass


def contextual_create(bm: 'bmesh.types.BMesh',
                      geom: typing.List['bmesh.types.BMVert'], mat_nr: int,
                      use_smooth: bool) -> dict:
    '''Three verts become a triangle, four become a quad. Two become a wire edge. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param geom: input geometry. 
    :type geom: typing.List['bmesh.types.BMVert']
    :param mat_nr: material to use 
    :type mat_nr: int
    :param use_smooth: smooth to use 
    :type use_smooth: bool
    :return:  faces: newly-made face(s)type list of (bmesh.types.BMFace)edges: newly-made edge(s)type list of (bmesh.types.BMEdge) 
    '''

    pass


def convex_hull(bm: 'bmesh.types.BMesh',
                input: typing.List['bmesh.types.BMVert'],
                use_existing_faces: bool) -> dict:
    '''All hull vertices, faces, and edges are added to ‘geom.out’. Any input elements that end up inside the hull (i.e. are not used by an output face) are added to the ‘interior_geom’ slot. The ‘unused_geom’ slot will contain all interior geometry that is completely unused. Lastly, ‘holes_geom’ contains edges and faces that were in the input and are part of the hull. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param input: Undocumented. 
    :type input: typing.List['bmesh.types.BMVert']
    :param use_existing_faces: Undocumented. 
    :type use_existing_faces: bool
    :return:  geom:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)geom_interior:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)geom_unused:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)geom_holes:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def create_circle(bm: 'bmesh.types.BMesh', cap_ends: bool, cap_tris: bool,
                  segments: int, diameter: float, matrix: 'mathutils.Matrix',
                  calc_uvs: bool) -> dict:
    '''Creates a Circle. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param cap_ends: whether or not to fill in the ends with faces 
    :type cap_ends: bool
    :param cap_tris: fill ends with triangles instead of ngons 
    :type cap_tris: bool
    :param segments: Undocumented. 
    :type segments: int
    :param diameter: diameter of one end 
    :type diameter: float
    :param matrix: matrix to multiply the new geometry with 
    :type matrix: 'mathutils.Matrix'
    :param calc_uvs: calculate default UVs 
    :type calc_uvs: bool
    :return:  verts: output vertstype list of (bmesh.types.BMVert) 
    '''

    pass


def create_cone(bm: 'bmesh.types.BMesh', cap_ends: bool, cap_tris: bool,
                segments: int, diameter1: float, diameter2: float,
                depth: float, matrix: 'mathutils.Matrix',
                calc_uvs: bool) -> dict:
    '''Creates a cone with variable depth at both ends 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param cap_ends: whether or not to fill in the ends with faces 
    :type cap_ends: bool
    :param cap_tris: fill ends with triangles instead of ngons 
    :type cap_tris: bool
    :param segments: Undocumented. 
    :type segments: int
    :param diameter1: diameter of one end 
    :type diameter1: float
    :param diameter2: diameter of the opposite 
    :type diameter2: float
    :param depth: distance between ends 
    :type depth: float
    :param matrix: matrix to multiply the new geometry with 
    :type matrix: 'mathutils.Matrix'
    :param calc_uvs: calculate default UVs 
    :type calc_uvs: bool
    :return:  verts: output vertstype list of (bmesh.types.BMVert) 
    '''

    pass


def create_cube(bm: 'bmesh.types.BMesh', size: float,
                matrix: 'mathutils.Matrix', calc_uvs: bool) -> dict:
    '''Creates a cube. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param size: size of the cube 
    :type size: float
    :param matrix: matrix to multiply the new geometry with 
    :type matrix: 'mathutils.Matrix'
    :param calc_uvs: calculate default UVs 
    :type calc_uvs: bool
    :return:  verts: output vertstype list of (bmesh.types.BMVert) 
    '''

    pass


def create_grid(bm: 'bmesh.types.BMesh', x_segments: int, y_segments: int,
                size: float, matrix: 'mathutils.Matrix',
                calc_uvs: bool) -> dict:
    '''Creates a grid with a variable number of subdivisions 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param x_segments: number of x segments 
    :type x_segments: int
    :param y_segments: number of y segments 
    :type y_segments: int
    :param size: size of the grid 
    :type size: float
    :param matrix: matrix to multiply the new geometry with 
    :type matrix: 'mathutils.Matrix'
    :param calc_uvs: calculate default UVs 
    :type calc_uvs: bool
    :return:  verts: output vertstype list of (bmesh.types.BMVert) 
    '''

    pass


def create_icosphere(bm: 'bmesh.types.BMesh', subdivisions: int,
                     diameter: float, matrix: 'mathutils.Matrix',
                     calc_uvs: bool) -> dict:
    '''Creates a grid with a variable number of subdivisions 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param subdivisions: how many times to recursively subdivide the sphere 
    :type subdivisions: int
    :param diameter: diameter 
    :type diameter: float
    :param matrix: matrix to multiply the new geometry with 
    :type matrix: 'mathutils.Matrix'
    :param calc_uvs: calculate default UVs 
    :type calc_uvs: bool
    :return:  verts: output vertstype list of (bmesh.types.BMVert) 
    '''

    pass


def create_monkey(bm: 'bmesh.types.BMesh', matrix: 'mathutils.Matrix',
                  calc_uvs: bool) -> dict:
    '''Creates a monkey (standard blender primitive). 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param matrix: matrix to multiply the new geometry with 
    :type matrix: 'mathutils.Matrix'
    :param calc_uvs: calculate default UVs 
    :type calc_uvs: bool
    :return:  verts: output vertstype list of (bmesh.types.BMVert) 
    '''

    pass


def create_uvsphere(bm: 'bmesh.types.BMesh', u_segments: int, v_segments: int,
                    diameter: float, matrix: 'mathutils.Matrix',
                    calc_uvs: bool) -> dict:
    '''Creates a grid with a variable number of subdivisions 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param u_segments: number of u segments 
    :type u_segments: int
    :param v_segments: number of v segment 
    :type v_segments: int
    :param diameter: diameter 
    :type diameter: float
    :param matrix: matrix to multiply the new geometry with 
    :type matrix: 'mathutils.Matrix'
    :param calc_uvs: calculate default UVs 
    :type calc_uvs: bool
    :return:  verts: output vertstype list of (bmesh.types.BMVert) 
    '''

    pass


def create_vert(bm: 'bmesh.types.BMesh', co: 'mathutils.Vector') -> dict:
    '''Creates a single vertex; this bmop was necessary for click-create-vertex. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param co: the coordinate of the new vert 
    :type co: 'mathutils.Vector'
    :return:  vert: the new verttype list of (bmesh.types.BMVert) 
    '''

    pass


def delete(bm: 'bmesh.types.BMesh', geom: typing.List['bmesh.types.BMVert'],
           context: int):
    '''Utility operator to delete geometry. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param geom: Undocumented. 
    :type geom: typing.List['bmesh.types.BMVert']
    :param context: enum DEL_VERTS … 
    :type context: int
    '''

    pass


def dissolve_degenerate(bm: 'bmesh.types.BMesh', dist: float,
                        edges: typing.List['bmesh.types.BMEdge']):
    '''Dissolve edges with no length, faces with no area. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param dist: minimum distance to consider degenerate 
    :type dist: float
    :param edges: Undocumented. 
    :type edges: typing.List['bmesh.types.BMEdge']
    '''

    pass


def dissolve_edges(bm: 'bmesh.types.BMesh',
                   edges: typing.List['bmesh.types.BMEdge'], use_verts: bool = False,
                   use_face_split: bool = False) -> dict:
    '''Dissolve Edges. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param edges: Undocumented. 
    :type edges: typing.List['bmesh.types.BMEdge']
    :param use_verts: dissolve verts left between only 2 edges. 
    :type use_verts: bool
    :param use_face_split: Undocumented. 
    :type use_face_split: bool
    :return:  region
    :type list of (bmesh.types.BMFace)
    '''

    pass


def dissolve_faces(bm: 'bmesh.types.BMesh',
                   faces: typing.List['bmesh.types.BMFace'],
                   use_verts: bool) -> dict:
    '''Dissolve Faces. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: Undocumented. 
    :type faces: typing.List['bmesh.types.BMFace']
    :param use_verts: dissolve verts left between only 2 edges. 
    :type use_verts: bool
    :return:  region:type list of (bmesh.types.BMFace) 
    '''

    pass


def dissolve_limit(bm: 'bmesh.types.BMesh', angle_limit: float,
                   use_dissolve_boundaries: bool,
                   verts: typing.List['bmesh.types.BMVert'],
                   edges: typing.List['bmesh.types.BMEdge'],
                   delimit: int) -> dict:
    '''Dissolve planar faces and co-linear edges. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param angle_limit: total rotation angle (radians) 
    :type angle_limit: float
    :param use_dissolve_boundaries: Undocumented. 
    :type use_dissolve_boundaries: bool
    :param verts: Undocumented. 
    :type verts: typing.List['bmesh.types.BMVert']
    :param edges: Undocumented. 
    :type edges: typing.List['bmesh.types.BMEdge']
    :param delimit: Undocumented. 
    :type delimit: int
    :return:  region:type list of (bmesh.types.BMFace) 
    '''

    pass


def dissolve_verts(bm: 'bmesh.types.BMesh',
                   verts: typing.List['bmesh.types.BMVert'],
                   use_face_split: bool = False,
                   use_boundary_tear: bool = False):
    '''Dissolve Verts. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param verts: Undocumented. 
    :type verts: typing.List['bmesh.types.BMVert']
    :param use_face_split: Undocumented. 
    :type use_face_split: bool
    :param use_boundary_tear: Undocumented. 
    :type use_boundary_tear: bool
    '''

    pass


def duplicate(bm: 'bmesh.types.BMesh', geom: typing.List['bmesh.types.BMVert'],
              dest: 'bmesh.types.BMesh', use_select_history: bool) -> dict:
    '''Utility operator to duplicate geometry, optionally into a destination mesh. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param geom: Undocumented. 
    :type geom: typing.List['bmesh.types.BMVert']
    :param dest: Undocumented. 
    :type dest: 'bmesh.types.BMesh'
    :param use_select_history: Undocumented. 
    :type use_select_history: bool
    :return:  geom_orig
    :type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)geom:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)vert_map:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFaceedge_map:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFaceface_map:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFaceboundary_map:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFaceisovert_map:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFace
    '''

    pass


def edgeloop_fill(bm: 'bmesh.types.BMesh',
                  edges: typing.List['bmesh.types.BMEdge'], mat_nr: int,
                  use_smooth: bool) -> dict:
    '''Create faces defined by one or more non overlapping edge loops. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges 
    :type edges: typing.List['bmesh.types.BMEdge']
    :param mat_nr: material to use 
    :type mat_nr: int
    :param use_smooth: smooth state to use 
    :type use_smooth: bool
    :return:  faces: new facestype list of (bmesh.types.BMFace) 
    '''

    pass


def edgenet_fill(bm: 'bmesh.types.BMesh',
                 edges: typing.List['bmesh.types.BMEdge'], mat_nr: int,
                 use_smooth: bool, sides: int) -> dict:
    '''Create faces defined by enclosed edges. 

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
    :return:  faces: new facestype list of (bmesh.types.BMFace) 
    '''

    pass


def edgenet_prepare(bm: 'bmesh.types.BMesh',
                    edges: typing.List['bmesh.types.BMEdge']) -> dict:
    '''Identifies several useful edge loop cases and modifies them so they’ll become a face when edgenet_fill is called. The cases covered are: 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges 
    :type edges: typing.List['bmesh.types.BMEdge']
    :return:  edges: new edgestype list of (bmesh.types.BMEdge) 
    '''

    pass


def extrude_discrete_faces(bm: 'bmesh.types.BMesh',
                           faces: typing.List['bmesh.types.BMFace'],
                           use_select_history: bool) -> dict:
    '''Extrudes faces individually. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces 
    :type faces: typing.List['bmesh.types.BMFace']
    :param use_select_history: pass to duplicate 
    :type use_select_history: bool
    :return:  faces: output facestype list of (bmesh.types.BMFace) 
    '''

    pass


def extrude_edge_only(bm: 'bmesh.types.BMesh',
                      edges: typing.List['bmesh.types.BMEdge'],
                      use_select_history: bool) -> dict:
    '''Extrudes Edges into faces, note that this is very simple, there’s no fancy winged extrusion. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param edges: input vertices 
    :type edges: typing.List['bmesh.types.BMEdge']
    :param use_select_history: pass to duplicate 
    :type use_select_history: bool
    :return:  geom: output geometrytype list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def extrude_face_region(bmesh,
                        geom: typing.List['bmesh.types.BMVert'] = [],
                        edges_exclude: set = {},
                        use_keep_orig: bool = False,
                        use_select_history: bool = False) -> dict:
    '''Extrude operator (does not transform) 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param geom: edges and faces 
    :type geom: typing.List['bmesh.types.BMVert']
    :param edges_exclude: Undocumented. 
    :type edges_exclude: set
    :param use_keep_orig: keep original geometry (requires geom to include edges). 
    :type use_keep_orig: bool
    :param use_select_history: pass to duplicate 
    :type use_select_history: bool
    :return:  geom:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def extrude_vert_indiv(bm: 'bmesh.types.BMesh',
                       verts: typing.List['bmesh.types.BMVert'],
                       use_select_history: bool) -> dict:
    '''Extrudes wire edges from vertices. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices 
    :type verts: typing.List['bmesh.types.BMVert']
    :param use_select_history: pass to duplicate 
    :type use_select_history: bool
    :return:  edges: output wire edgestype list of (bmesh.types.BMEdge)verts: output verticestype list of (bmesh.types.BMVert) 
    '''

    pass


def face_attribute_fill(bm: 'bmesh.types.BMesh',
                        faces: typing.List['bmesh.types.BMFace'],
                        use_normals: bool, use_data: bool) -> dict:
    '''Fill in faces with data from adjacent faces. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces 
    :type faces: typing.List['bmesh.types.BMFace']
    :param use_normals: copy face winding 
    :type use_normals: bool
    :param use_data: copy face data 
    :type use_data: bool
    :return:  faces_fail: faces that could not be handledtype list of (bmesh.types.BMFace) 
    '''

    pass


def find_doubles(
        bm: 'bmesh.types.BMesh', verts: typing.List['bmesh.types.BMVert'],
        keep_verts: typing.List['bmesh.types.BMVert'], dist: float) -> dict:
    '''If keep_verts is used, vertices outside that set can only be merged with vertices in that set. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices 
    :type verts: typing.List['bmesh.types.BMVert']
    :param keep_verts: list of verts to keep 
    :type keep_verts: typing.List['bmesh.types.BMVert']
    :param dist: minimum distance 
    :type dist: float
    :return:  targetmap:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFace 
    '''

    pass


def grid_fill(bm: 'bmesh.types.BMesh',
              edges: typing.List['bmesh.types.BMEdge'], mat_nr: int,
              use_smooth: bool, use_interp_simple: bool) -> dict:
    '''Create faces defined by 2 disconnected edge loops (which share edges). 

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
    :return:  faces: new facestype list of (bmesh.types.BMFace) 
    '''

    pass


def holes_fill(bm: 'bmesh.types.BMesh',
               edges: typing.List['bmesh.types.BMEdge'], sides: int) -> dict:
    '''Fill boundary edges with faces, copying surrounding customdata. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges 
    :type edges: typing.List['bmesh.types.BMEdge']
    :param sides: number of face sides to fill 
    :type sides: int
    :return:  faces: new facestype list of (bmesh.types.BMFace) 
    '''

    pass


def inset_individual(bm: 'bmesh.types.BMesh',
                     faces: typing.List['bmesh.types.BMFace'],
                     thickness: float, depth: float, use_even_offset: bool,
                     use_interpolate: bool, use_relative_offset: bool) -> dict:
    '''Insets individual faces. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces 
    :type faces: typing.List['bmesh.types.BMFace']
    :param thickness: Undocumented. 
    :type thickness: float
    :param depth: Undocumented. 
    :type depth: float
    :param use_even_offset: Undocumented. 
    :type use_even_offset: bool
    :param use_interpolate: Undocumented. 
    :type use_interpolate: bool
    :param use_relative_offset: Undocumented. 
    :type use_relative_offset: bool
    :return:  faces: output facestype list of (bmesh.types.BMFace) 
    '''

    pass


def inset_region(
        bm: 'bmesh.types.BMesh', faces: typing.List['bmesh.types.BMFace'],
        faces_exclude: typing.List['bmesh.types.BMFace'], use_boundary: bool,
        use_even_offset: bool, use_interpolate: bool,
        use_relative_offset: bool, use_edge_rail: bool, thickness: float,
        depth: float, use_outset: bool) -> dict:
    '''Inset or outset face regions. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces 
    :type faces: typing.List['bmesh.types.BMFace']
    :param faces_exclude: Undocumented. 
    :type faces_exclude: typing.List['bmesh.types.BMFace']
    :param use_boundary: Undocumented. 
    :type use_boundary: bool
    :param use_even_offset: Undocumented. 
    :type use_even_offset: bool
    :param use_interpolate: Undocumented. 
    :type use_interpolate: bool
    :param use_relative_offset: Undocumented. 
    :type use_relative_offset: bool
    :param use_edge_rail: Undocumented. 
    :type use_edge_rail: bool
    :param thickness: Undocumented. 
    :type thickness: float
    :param depth: Undocumented. 
    :type depth: float
    :param use_outset: Undocumented. 
    :type use_outset: bool
    :return:  faces: output facestype list of (bmesh.types.BMFace) 
    '''

    pass


def join_triangles(bm: 'bmesh.types.BMesh',
                   faces: typing.List['bmesh.types.BMFace'], cmp_seam: bool,
                   cmp_sharp: bool, cmp_uvs: bool, cmp_vcols: bool,
                   cmp_materials: bool, angle_face_threshold: float,
                   angle_shape_threshold: float) -> dict:
    '''Tries to intelligently join triangles according to angle threshold and delimiters. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: input geometry. 
    :type faces: typing.List['bmesh.types.BMFace']
    :param cmp_seam: Undocumented. 
    :type cmp_seam: bool
    :param cmp_sharp: Undocumented. 
    :type cmp_sharp: bool
    :param cmp_uvs: Undocumented. 
    :type cmp_uvs: bool
    :param cmp_vcols: Undocumented. 
    :type cmp_vcols: bool
    :param cmp_materials: Undocumented. 
    :type cmp_materials: bool
    :param angle_face_threshold: Undocumented. 
    :type angle_face_threshold: float
    :param angle_shape_threshold: Undocumented. 
    :type angle_shape_threshold: float
    :return:  faces: joined facestype list of (bmesh.types.BMFace) 
    '''

    pass


def mesh_to_bmesh(bm: 'bmesh.types.BMesh', mesh: 'bpy.types.Mesh',
                  object: 'bpy.types.Object', use_shapekey: bool):
    '''Load the contents of a mesh into the bmesh. this bmop is private, it’s reserved exclusively for entering editmode. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param mesh: Undocumented. 
    :type mesh: 'bpy.types.Mesh'
    :param object: Undocumented. 
    :type object: 'bpy.types.Object'
    :param use_shapekey: load active shapekey coordinates into verts 
    :type use_shapekey: bool
    '''

    pass


def mirror(bm: 'bmesh.types.BMesh', geom: typing.List['bmesh.types.BMVert'],
           matrix: 'mathutils.Matrix', merge_dist: float, axis: int,
           mirror_u: bool, mirror_v: bool) -> dict:
    '''Mirrors geometry along an axis. The resulting geometry is welded on using merge_dist. Pairs of original/mirrored vertices are welded using the merge_dist parameter (which defines the minimum distance for welding to happen). 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param geom: input geometry 
    :type geom: typing.List['bmesh.types.BMVert']
    :param matrix: matrix defining the mirror transformation 
    :type matrix: 'mathutils.Matrix'
    :param merge_dist: maximum distance for merging. does no merging if 0. 
    :type merge_dist: float
    :param axis: the axis to use, 0, 1, or 2 for x, y, z 
    :type axis: int
    :param mirror_u: mirror UVs across the u axis 
    :type mirror_u: bool
    :param mirror_v: mirror UVs across the v axis 
    :type mirror_v: bool
    :return:  geom: output geometry, mirroredtype list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def object_load_bmesh(bm: 'bmesh.types.BMesh', scene: 'bpy.types.Scene',
                      object: 'bpy.types.Object'):
    '''Loads a bmesh into an object/mesh. This is a “private” bmop. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param scene: Undocumented. 
    :type scene: 'bpy.types.Scene'
    :param object: Undocumented. 
    :type object: 'bpy.types.Object'
    '''

    pass


def offset_edgeloops(bm: 'bmesh.types.BMesh',
                     edges: typing.List['bmesh.types.BMEdge'],
                     use_cap_endpoint: bool) -> dict:
    '''Creates edge loops based on simple edge-outset method. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param edges: input faces 
    :type edges: typing.List['bmesh.types.BMEdge']
    :param use_cap_endpoint: Undocumented. 
    :type use_cap_endpoint: bool
    :return:  edges: output facestype list of (bmesh.types.BMEdge) 
    '''

    pass


def planar_faces(bm: 'bmesh.types.BMesh',
                 faces: typing.List['bmesh.types.BMFace'], iterations: int,
                 factor: float) -> dict:
    '''Iteratively flatten faces. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: input geometry. 
    :type faces: typing.List['bmesh.types.BMFace']
    :param iterations: Number of times to flatten faces (for when connected faces are used) 
    :type iterations: int
    :param factor: Influence for making planar each iteration 
    :type factor: float
    :return:  geom: output slot, computed boundary geometry.type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def pointmerge(bm: 'bmesh.types.BMesh',
               verts: typing.List['bmesh.types.BMVert'],
               merge_co: 'mathutils.Vector'):
    '''Merge verts together at a point. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices (all verts will be merged into the first). 
    :type verts: typing.List['bmesh.types.BMVert']
    :param merge_co: Position to merge at. 
    :type merge_co: 'mathutils.Vector'
    '''

    pass


def pointmerge_facedata(bm: 'bmesh.types.BMesh',
                        verts: typing.List['bmesh.types.BMVert'],
                        vert_snap: 'bmesh.types.BMVert'):
    '''Merge uv/vcols at a specific vertex. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices 
    :type verts: typing.List['bmesh.types.BMVert']
    :param vert_snap: snap vertex 
    :type vert_snap: 'bmesh.types.BMVert'
    '''

    pass


def poke(bm: 'bmesh.types.BMesh', faces: typing.List['bmesh.types.BMFace'],
         offset: float, center_mode: int, use_relative_offset: bool) -> dict:
    '''Splits a face into a triangle fan. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces 
    :type faces: typing.List['bmesh.types.BMFace']
    :param offset: center vertex offset along normal 
    :type offset: float
    :param center_mode: calculation mode for center vertex 
    :type center_mode: int
    :param use_relative_offset: apply offset 
    :type use_relative_offset: bool
    :return:  verts: output vertstype list of (bmesh.types.BMVert)faces: output facestype list of (bmesh.types.BMFace) 
    '''

    pass


def recalc_face_normals(bm: 'bmesh.types.BMesh',
                        faces: typing.Union[typing.List['bmesh.types.BMFace'], BMFaceSeq]):
    '''Computes an “outside” normal for the specified input faces. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: Undocumented. 
    :type faces: typing.List['bmesh.types.BMFace']
    '''

    pass


def region_extend(bm: 'bmesh.types.BMesh',
                  geom: typing.List['bmesh.types.BMVert'], use_contract: bool,
                  use_faces: bool, use_face_step: bool) -> dict:
    '''if use_faces is 0 then geom.out spits out verts and edges, otherwise it spits out faces. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param geom: input geometry 
    :type geom: typing.List['bmesh.types.BMVert']
    :param use_contract: find boundary inside the regions, not outside. 
    :type use_contract: bool
    :param use_faces: extend from faces instead of edges 
    :type use_faces: bool
    :param use_face_step: step over connected faces 
    :type use_face_step: bool
    :return:  geom: output slot, computed boundary geometry.type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def remove_doubles(bm: 'bmesh.types.BMesh',
                   verts: typing.List['bmesh.types.BMVert'], dist: float):
    '''Finds groups of vertices closer then dist and merges them together, using the weld verts bmop. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param verts: input verts 
    :type verts: typing.List['bmesh.types.BMVert']
    :param dist: minimum distance 
    :type dist: float
    '''

    pass


def reverse_colors(bm: 'bmesh.types.BMesh',
                   faces: typing.List['bmesh.types.BMFace']):
    '''Reverse the loop colors. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces 
    :type faces: typing.List['bmesh.types.BMFace']
    '''

    pass


def reverse_faces(bm: 'bmesh.types.BMesh',
                  faces: typing.List['bmesh.types.BMFace'],
                  flip_multires: bool):
    '''Reverses the winding (vertex order) of faces. This has the effect of flipping the normal. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces 
    :type faces: typing.List['bmesh.types.BMFace']
    :param flip_multires: maintain multi-res offset 
    :type flip_multires: bool
    '''

    pass


def reverse_uvs(bm: 'bmesh.types.BMesh',
                faces: typing.List['bmesh.types.BMFace']):
    '''Reverse the UV’s 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces 
    :type faces: typing.List['bmesh.types.BMFace']
    '''

    pass


def rotate(bm: 'bmesh.types.BMesh', cent: 'mathutils.Vector',
           matrix: 'mathutils.Matrix',
           verts: typing.List['bmesh.types.BMVert'],
           space: 'mathutils.Matrix'):
    '''Rotate vertices around a center, using a 3x3 rotation matrix. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param cent: center of rotation 
    :type cent: 'mathutils.Vector'
    :param matrix: matrix defining rotation 
    :type matrix: 'mathutils.Matrix'
    :param verts: input vertices 
    :type verts: typing.List['bmesh.types.BMVert']
    :param space: matrix to define the space (typically object matrix) 
    :type space: 'mathutils.Matrix'
    '''

    pass


def rotate_colors(bm: 'bmesh.types.BMesh',
                  faces: typing.List['bmesh.types.BMFace'], use_ccw: bool):
    '''Cycle the loop colors 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces 
    :type faces: typing.List['bmesh.types.BMFace']
    :param use_ccw: rotate counter-clockwise if true, otherwise clockwise 
    :type use_ccw: bool
    '''

    pass


def rotate_edges(bm: 'bmesh.types.BMesh',
                 edges: typing.List['bmesh.types.BMEdge'],
                 use_ccw: bool) -> dict:
    '''Rotates edges topologically. Also known as “spin edge” to some people. Simple example: [/] becomes [|] then [\]. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges 
    :type edges: typing.List['bmesh.types.BMEdge']
    :param use_ccw: rotate edge counter-clockwise if true, otherwise clockwise 
    :type use_ccw: bool
    :return:  edges: newly spun edgestype list of (bmesh.types.BMEdge) 
    '''

    pass


def rotate_uvs(bm: 'bmesh.types.BMesh',
               faces: typing.List['bmesh.types.BMFace'], use_ccw: bool):
    '''Cycle the loop UV’s 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces 
    :type faces: typing.List['bmesh.types.BMFace']
    :param use_ccw: rotate counter-clockwise if true, otherwise clockwise 
    :type use_ccw: bool
    '''

    pass


def scale(bm: 'bmesh.types.BMesh', vec: 'mathutils.Vector',
          space: 'mathutils.Matrix', verts: typing.List['bmesh.types.BMVert']):
    '''Scales vertices by an offset. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param vec: scale factor 
    :type vec: 'mathutils.Vector'
    :param space: matrix to define the space (typically object matrix) 
    :type space: 'mathutils.Matrix'
    :param verts: input vertices 
    :type verts: typing.List['bmesh.types.BMVert']
    '''

    pass


def similar_edges(bm: 'bmesh.types.BMesh',
                  edges: typing.List['bmesh.types.BMEdge'], type: int,
                  thresh: float, compare: int) -> dict:
    '''Similar Edges Search. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges 
    :type edges: typing.List['bmesh.types.BMEdge']
    :param type: type of selection 
    :type type: int
    :param thresh: threshold of selection 
    :type thresh: float
    :param compare: comparison method 
    :type compare: int
    :return:  edges: output edgestype list of (bmesh.types.BMEdge) 
    '''

    pass


def similar_faces(bm: 'bmesh.types.BMesh',
                  faces: typing.List['bmesh.types.BMFace'], type: int,
                  thresh: float, compare: int) -> dict:
    '''Find similar faces (area/material/perimeter, …). 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces 
    :type faces: typing.List['bmesh.types.BMFace']
    :param type: type of selection 
    :type type: int
    :param thresh: threshold of selection 
    :type thresh: float
    :param compare: comparison method 
    :type compare: int
    :return:  faces: output facestype list of (bmesh.types.BMFace) 
    '''

    pass


def similar_verts(bm: 'bmesh.types.BMesh',
                  verts: typing.List['bmesh.types.BMVert'], type: int,
                  thresh: float, compare: int) -> dict:
    '''Find similar vertices (normal, face, vertex group, …). 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices 
    :type verts: typing.List['bmesh.types.BMVert']
    :param type: type of selection 
    :type type: int
    :param thresh: threshold of selection 
    :type thresh: float
    :param compare: comparison method 
    :type compare: int
    :return:  verts: output verticestype list of (bmesh.types.BMVert) 
    '''

    pass


def smooth_laplacian_vert(
        bm: 'bmesh.types.BMesh', verts: typing.List['bmesh.types.BMVert'],
        lambda_factor: float, lambda_border: float, use_x: bool, use_y: bool,
        use_z: bool, preserve_volume: bool):
    '''Smooths vertices by using Laplacian smoothing propose by. Desbrun, et al. Implicit Fairing of Irregular Meshes using Diffusion and Curvature Flow. 

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
                verts: typing.List['bmesh.types.BMVert'], factor: float,
                mirror_clip_x: bool, mirror_clip_y: bool, mirror_clip_z: bool,
                clip_dist: float, use_axis_x: bool, use_axis_y: bool,
                use_axis_z: bool):
    '''Smooths vertices by using a basic vertex averaging scheme. 

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


def solidify(bm: 'bmesh.types.BMesh', geom: typing.List['bmesh.types.BMVert'],
             thickness: float) -> dict:
    '''Turns a mesh into a shell with thickness 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param geom: Undocumented. 
    :type geom: typing.List['bmesh.types.BMVert']
    :param thickness: Undocumented. 
    :type thickness: float
    :return:  geom:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def spin(bm: 'bmesh.types.BMesh', geom: typing.List['bmesh.types.BMVert'],
         cent: 'mathutils.Vector', axis: 'mathutils.Vector',
         dvec: 'mathutils.Vector', angle: float, space: 'mathutils.Matrix',
         steps: int, use_duplicate: bool) -> dict:
    '''Extrude or duplicate geometry a number of times, rotating and possibly translating after each step 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param geom: Undocumented. 
    :type geom: typing.List['bmesh.types.BMVert']
    :param cent: rotation center 
    :type cent: 'mathutils.Vector'
    :param axis: rotation axis 
    :type axis: 'mathutils.Vector'
    :param dvec: translation delta per step 
    :type dvec: 'mathutils.Vector'
    :param angle: total rotation angle (radians) 
    :type angle: float
    :param space: matrix to define the space (typically object matrix) 
    :type space: 'mathutils.Matrix'
    :param steps: number of steps 
    :type steps: int
    :param use_duplicate: duplicate or extrude? 
    :type use_duplicate: bool
    :return:  geom_last: result of last steptype list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def split(bm: 'bmesh.types.BMesh', geom: typing.List['bmesh.types.BMVert'],
          dest: 'bmesh.types.BMesh', use_only_faces: bool) -> dict:
    '''Disconnect geometry from adjacent edges and faces, optionally into a destination mesh. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param geom: Undocumented. 
    :type geom: typing.List['bmesh.types.BMVert']
    :param dest: Undocumented. 
    :type dest: 'bmesh.types.BMesh'
    :param use_only_faces: when enabled. don’t duplicate loose verts/edges 
    :type use_only_faces: bool
    :return:  geom:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)boundary_map:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFaceisovert_map:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFace 
    '''

    pass


def split_edges(
        bm: 'bmesh.types.BMesh', edges: typing.List['bmesh.types.BMEdge'],
        verts: typing.List['bmesh.types.BMVert'], use_verts: bool) -> dict:
    '''Disconnects faces along input edges. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param edges: input edges 
    :type edges: typing.List['bmesh.types.BMEdge']
    :param verts: optional tag verts, use to have greater control of splits 
    :type verts: typing.List['bmesh.types.BMVert']
    :param use_verts: use ‘verts’ for splitting, else just find verts to split from edges 
    :type use_verts: bool
    :return:  edges: old output disconnected edgestype list of (bmesh.types.BMEdge) 
    '''

    pass


def subdivide_edgering(
        bm: 'bmesh.types.BMesh', edges: typing.List['bmesh.types.BMEdge'],
        interp_mode: int, smooth: float, cuts: int, profile_shape: int,
        profile_shape_factor: float) -> dict:
    '''Take an edge-ring, and subdivide with interpolation options. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param edges: input vertices 
    :type edges: typing.List['bmesh.types.BMEdge']
    :param interp_mode: Undocumented. 
    :type interp_mode: int
    :param smooth: Undocumented. 
    :type smooth: float
    :param cuts: Undocumented. 
    :type cuts: int
    :param profile_shape: Undocumented. 
    :type profile_shape: int
    :param profile_shape_factor: Undocumented. 
    :type profile_shape_factor: float
    :return:  faces: output facestype list of (bmesh.types.BMFace) 
    '''

    pass


def subdivide_edges(
        bm: 'bmesh.types.BMesh', edges: typing.List['bmesh.types.BMEdge'],
        smooth: float, smooth_falloff: int, fractal: float,
        along_normal: float, cuts: int, seed: int, custom_patterns: dict,
        edge_percents: dict, quad_corner_type: int, use_grid_fill: bool,
        use_single_edge: bool, use_only_quads: bool, use_sphere: bool,
        use_smooth_even: bool) -> dict:
    '''Advanced operator for subdividing edges with options for face patterns, smoothing and randomization. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param edges: Undocumented. 
    :type edges: typing.List['bmesh.types.BMEdge']
    :param smooth: Undocumented. 
    :type smooth: float
    :param smooth_falloff: SUBD_FALLOFF_ROOT and friends 
    :type smooth_falloff: int
    :param fractal: Undocumented. 
    :type fractal: float
    :param along_normal: Undocumented. 
    :type along_normal: float
    :param cuts: Undocumented. 
    :type cuts: int
    :param seed: Undocumented. 
    :type seed: int
    :param custom_patterns: uses custom pointers 
    :type custom_patterns: dict
    :param edge_percents: Undocumented. 
    :type edge_percents: dict
    :param quad_corner_type: quad corner type, see bmesh_operators.h 
    :type quad_corner_type: int
    :param use_grid_fill: fill in fully-selected faces with a grid 
    :type use_grid_fill: bool
    :param use_single_edge: tessellate the case of one edge selected in a quad or triangle 
    :type use_single_edge: bool
    :param use_only_quads: only subdivide quads (for loopcut) 
    :type use_only_quads: bool
    :param use_sphere: for making new primitives only 
    :type use_sphere: bool
    :param use_smooth_even: maintain even offset when smoothing 
    :type use_smooth_even: bool
    :return:  geom_inner:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)geom_split:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)geom: contains all output geometrytype list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def symmetrize(bm: 'bmesh.types.BMesh',
               input: typing.List['bmesh.types.BMVert'], direction: int,
               dist: float) -> dict:
    '''All new vertices, edges, and faces are added to the “geom.out” slot. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param input: Undocumented. 
    :type input: typing.List['bmesh.types.BMVert']
    :param direction: Undocumented. 
    :type direction: int
    :param dist: minimum distance 
    :type dist: float
    :return:  geom:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def transform(bm: 'bmesh.types.BMesh', matrix: 'mathutils.Matrix',
              space: 'mathutils.Matrix',
              verts: typing.List['bmesh.types.BMVert']):
    '''Transforms a set of vertices by a matrix. Multiplies the vertex coordinates with the matrix. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param matrix: transform matrix 
    :type matrix: 'mathutils.Matrix'
    :param space: matrix to define the space (typically object matrix) 
    :type space: 'mathutils.Matrix'
    :param verts: input vertices 
    :type verts: typing.List['bmesh.types.BMVert']
    '''

    pass


def translate(bmesh,
              vec: 'mathutils.Vector',
              space: 'mathutils.Matrix',
              verts: typing.List['bmesh.types.BMVert'] = []):
    '''Translate vertices by an offset. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param vec: translation offset 
    :type vec: 'mathutils.Vector'
    :param space: matrix to define the space (typically object matrix) 
    :type space: 'mathutils.Matrix'
    :param verts: input vertices 
    :type verts: typing.List['bmesh.types.BMVert']
    '''

    pass


def triangle_fill(bm: 'bmesh.types.BMesh', use_beauty: bool,
                  use_dissolve: bool, edges: typing.List['bmesh.types.BMEdge'],
                  normal: 'mathutils.Vector') -> dict:
    '''Fill edges with triangles 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param use_beauty: Undocumented. 
    :type use_beauty: bool
    :param use_dissolve: dissolve resulting faces 
    :type use_dissolve: bool
    :param edges: input edges 
    :type edges: typing.List['bmesh.types.BMEdge']
    :param normal: optionally pass the fill normal to use 
    :type normal: 'mathutils.Vector'
    :return:  geom: new faces and edgestype list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def triangulate(bm: 'bmesh.types.BMesh',
                faces: typing.List['bmesh.types.BMFace'], quad_method: int,
                ngon_method: int) -> dict:
    '''Triangulate. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: Undocumented. 
    :type faces: typing.List['bmesh.types.BMFace']
    :param quad_method: Undocumented. 
    :type quad_method: int
    :param ngon_method: Undocumented. 
    :type ngon_method: int
    :return:  edges:type list of (bmesh.types.BMEdge)faces:type list of (bmesh.types.BMFace)face_map:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFaceface_map_double: duplicate facestype dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFace 
    '''

    pass


def unsubdivide(bm: 'bmesh.types.BMesh',
                verts: typing.List['bmesh.types.BMVert'], iterations: int):
    '''Reduce detail in geometry containing grids. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param verts: input vertices 
    :type verts: typing.List['bmesh.types.BMVert']
    :param iterations: Undocumented. 
    :type iterations: int
    '''

    pass


def weld_verts(bm: 'bmesh.types.BMesh', targetmap: dict):
    '''Welds verts together (kind-of like remove doubles, merge, etc, all of which use or will use this bmop). You pass in mappings from vertices to the vertices they weld with. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param targetmap: Undocumented. 
    :type targetmap: dict
    '''

    pass


def wireframe(bm: 'bmesh.types.BMesh',
              faces: typing.List['bmesh.types.BMFace'], thickness: float,
              offset: float, use_replace: bool, use_boundary: bool,
              use_even_offset: bool, use_crease: bool, crease_weight: float,
              use_relative_offset: bool, material_offset: int) -> dict:
    '''Makes a wire-frame copy of faces. 

    :param bm: The bmesh to operate on. 
    :type bm: 'bmesh.types.BMesh'
    :param faces: input faces 
    :type faces: typing.List['bmesh.types.BMFace']
    :param thickness: Undocumented. 
    :type thickness: float
    :param offset: Undocumented. 
    :type offset: float
    :param use_replace: Undocumented. 
    :type use_replace: bool
    :param use_boundary: Undocumented. 
    :type use_boundary: bool
    :param use_even_offset: Undocumented. 
    :type use_even_offset: bool
    :param use_crease: Undocumented. 
    :type use_crease: bool
    :param crease_weight: Undocumented. 
    :type crease_weight: float
    :param use_relative_offset: Undocumented. 
    :type use_relative_offset: bool
    :param material_offset: Undocumented. 
    :type material_offset: int
    :return:  faces: output facestype list of (bmesh.types.BMFace) 
    '''

    pass
