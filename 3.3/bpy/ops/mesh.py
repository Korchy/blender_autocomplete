import sys
import typing
import bpy.types
import mathutils
import bpy.ops.transform

GenericType = typing.TypeVar("GenericType")


def average_normals(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    average_type: typing.Union[str, int] = 'CUSTOM_NORMAL',
                    weight: int = 50,
                    threshold: float = 0.01):
    ''' Average custom normals of selected vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param average_type: Type, Averaging method * CUSTOM_NORMAL Custom Normal -- Take average of vertex normals. * FACE_AREA Face Area -- Set all vertex normals by face area. * CORNER_ANGLE Corner Angle -- Set all vertex normals by corner angle.
    :type average_type: typing.Union[str, int]
    :param weight: Weight, Weight applied per face
    :type weight: int
    :param threshold: Threshold, Threshold value for different weights to be considered equal
    :type threshold: float
    '''

    pass


def beautify_fill(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  angle_limit: float = 3.14159):
    ''' Rearrange some faces to try to get less degenerated geometry

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param angle_limit: Max Angle, Angle limit
    :type angle_limit: float
    '''

    pass


def bevel(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None,
          *,
          offset_type: typing.Union[str, int] = 'OFFSET',
          offset: float = 0.0,
          profile_type: typing.Union[str, int] = 'SUPERELLIPSE',
          offset_pct: float = 0.0,
          segments: int = 1,
          profile: float = 0.5,
          affect: typing.Union[str, int] = 'EDGES',
          clamp_overlap: bool = False,
          loop_slide: bool = True,
          mark_seam: bool = False,
          mark_sharp: bool = False,
          material: int = -1,
          harden_normals: bool = False,
          face_strength_mode: typing.Union[str, int] = 'NONE',
          miter_outer: typing.Union[str, int] = 'SHARP',
          miter_inner: typing.Union[str, int] = 'SHARP',
          spread: float = 0.1,
          vmesh_method: typing.Union[str, int] = 'ADJ',
          release_confirm: bool = False):
    ''' Cut into selected items at an angle to create bevel or chamfer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param offset_type: Width Type, The method for determining the size of the bevel * OFFSET Offset -- Amount is offset of new edges from original. * WIDTH Width -- Amount is width of new face. * DEPTH Depth -- Amount is perpendicular distance from original edge to bevel face. * PERCENT Percent -- Amount is percent of adjacent edge length. * ABSOLUTE Absolute -- Amount is absolute distance along adjacent edge.
    :type offset_type: typing.Union[str, int]
    :param offset: Width, Bevel amount
    :type offset: float
    :param profile_type: Profile Type, The type of shape used to rebuild a beveled section * SUPERELLIPSE Superellipse -- The profile can be a concave or convex curve. * CUSTOM Custom -- The profile can be any arbitrary path between its endpoints.
    :type profile_type: typing.Union[str, int]
    :param offset_pct: Width Percent, Bevel amount for percentage method
    :type offset_pct: float
    :param segments: Segments, Segments for curved edge
    :type segments: int
    :param profile: Profile, Controls profile shape (0.5 = round)
    :type profile: float
    :param affect: Affect, Affect edges or vertices * VERTICES Vertices -- Affect only vertices. * EDGES Edges -- Affect only edges.
    :type affect: typing.Union[str, int]
    :param clamp_overlap: Clamp Overlap, Do not allow beveled edges/vertices to overlap each other
    :type clamp_overlap: bool
    :param loop_slide: Loop Slide, Prefer sliding along edges to even widths
    :type loop_slide: bool
    :param mark_seam: Mark Seams, Mark Seams along beveled edges
    :type mark_seam: bool
    :param mark_sharp: Mark Sharp, Mark beveled edges as sharp
    :type mark_sharp: bool
    :param material: Material Index, Material for bevel faces (-1 means use adjacent faces)
    :type material: int
    :param harden_normals: Harden Normals, Match normals of new faces to adjacent faces
    :type harden_normals: bool
    :param face_strength_mode: Face Strength Mode, Whether to set face strength, and which faces to set face strength on * NONE None -- Do not set face strength. * NEW New -- Set face strength on new faces only. * AFFECTED Affected -- Set face strength on new and modified faces only. * ALL All -- Set face strength on all faces.
    :type face_strength_mode: typing.Union[str, int]
    :param miter_outer: Outer Miter, Pattern to use for outside of miters * SHARP Sharp -- Outside of miter is sharp. * PATCH Patch -- Outside of miter is squared-off patch. * ARC Arc -- Outside of miter is arc.
    :type miter_outer: typing.Union[str, int]
    :param miter_inner: Inner Miter, Pattern to use for inside of miters * SHARP Sharp -- Inside of miter is sharp. * ARC Arc -- Inside of miter is arc.
    :type miter_inner: typing.Union[str, int]
    :param spread: Spread, Amount to spread arcs for arc inner miters
    :type spread: float
    :param vmesh_method: Vertex Mesh Method, The method to use to create meshes at intersections * ADJ Grid Fill -- Default patterned fill. * CUTOFF Cutoff -- A cutoff at each profile's end before the intersection.
    :type vmesh_method: typing.Union[str, int]
    :param release_confirm: Confirm on Release
    :type release_confirm: bool
    '''

    pass


def bisect(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           plane_co: typing.
           Union[typing.List[float], typing.
                 Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                    0.0),
           plane_no: typing.
           Union[typing.List[float], typing.
                 Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                    0.0),
           use_fill: bool = False,
           clear_inner: bool = False,
           clear_outer: bool = False,
           threshold: float = 0.0001,
           xstart: int = 0,
           xend: int = 0,
           ystart: int = 0,
           yend: int = 0,
           flip: bool = False,
           cursor: int = 5):
    ''' Cut geometry along a plane (click-drag to define plane)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param plane_co: Plane Point, A point on the plane
    :type plane_co: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param plane_no: Plane Normal, The direction the plane points
    :type plane_no: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param use_fill: Fill, Fill in the cut
    :type use_fill: bool
    :param clear_inner: Clear Inner, Remove geometry behind the plane
    :type clear_inner: bool
    :param clear_outer: Clear Outer, Remove geometry in front of the plane
    :type clear_outer: bool
    :param threshold: Axis Threshold, Preserves the existing geometry along the cut plane
    :type threshold: float
    :param xstart: X Start
    :type xstart: int
    :param xend: X End
    :type xend: int
    :param ystart: Y Start
    :type ystart: int
    :param yend: Y End
    :type yend: int
    :param flip: Flip
    :type flip: bool
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: int
    '''

    pass


def blend_from_shape(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     shape: typing.Union[str, int] = '',
                     blend: float = 1.0,
                     add: bool = True):
    ''' Blend in shape from a shape key

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param shape: Shape, Shape key to use for blending
    :type shape: typing.Union[str, int]
    :param blend: Blend, Blending factor
    :type blend: float
    :param add: Add, Add rather than blend between shapes
    :type add: bool
    '''

    pass


def bridge_edge_loops(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      type: typing.Union[str, int] = 'SINGLE',
                      use_merge: bool = False,
                      merge_factor: float = 0.5,
                      twist_offset: int = 0,
                      number_cuts: int = 0,
                      interpolation: typing.Union[str, int] = 'PATH',
                      smoothness: float = 1.0,
                      profile_shape_factor: float = 0.0,
                      profile_shape: typing.Union[int, str] = 'SMOOTH'):
    ''' Create a bridge of faces between two or more selected edge loops

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Connect Loops, Method of bridging multiple loops
    :type type: typing.Union[str, int]
    :param use_merge: Merge, Merge rather than creating faces
    :type use_merge: bool
    :param merge_factor: Merge Factor
    :type merge_factor: float
    :param twist_offset: Twist, Twist offset for closed loops
    :type twist_offset: int
    :param number_cuts: Number of Cuts
    :type number_cuts: int
    :param interpolation: Interpolation, Interpolation method
    :type interpolation: typing.Union[str, int]
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: float
    :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded
    :type profile_shape_factor: float
    :param profile_shape: Profile Shape, Shape of the profile
    :type profile_shape: typing.Union[int, str]
    '''

    pass


def colors_reverse(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Flip direction of vertex colors inside faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def colors_rotate(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  use_ccw: bool = False):
    ''' Rotate color attributes inside faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_ccw: Counter Clockwise
    :type use_ccw: bool
    '''

    pass


def convex_hull(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                delete_unused: bool = True,
                use_existing_faces: bool = True,
                make_holes: bool = False,
                join_triangles: bool = True,
                face_threshold: float = 0.698132,
                shape_threshold: float = 0.698132,
                uvs: bool = False,
                vcols: bool = False,
                seam: bool = False,
                sharp: bool = False,
                materials: bool = False):
    ''' Enclose selected vertices in a convex polyhedron

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param delete_unused: Delete Unused, Delete selected elements that are not used by the hull
    :type delete_unused: bool
    :param use_existing_faces: Use Existing Faces, Skip hull triangles that are covered by a pre-existing face
    :type use_existing_faces: bool
    :param make_holes: Make Holes, Delete selected faces that are used by the hull
    :type make_holes: bool
    :param join_triangles: Join Triangles, Merge adjacent triangles into quads
    :type join_triangles: bool
    :param face_threshold: Max Face Angle, Face angle limit
    :type face_threshold: float
    :param shape_threshold: Max Shape Angle, Shape angle limit
    :type shape_threshold: float
    :param uvs: Compare UVs
    :type uvs: bool
    :param vcols: Compare VCols
    :type vcols: bool
    :param seam: Compare Seam
    :type seam: bool
    :param sharp: Compare Sharp
    :type sharp: bool
    :param materials: Compare Materials
    :type materials: bool
    '''

    pass


def customdata_custom_splitnormals_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Add a custom split normals layer, if none exists yet

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def customdata_custom_splitnormals_clear(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Remove the custom split normals layer, if it exists

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def customdata_mask_clear(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Clear vertex sculpt masking data from the mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def customdata_skin_add(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Add a vertex skin layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def customdata_skin_clear(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Clear vertex skin layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def decimate(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             ratio: float = 1.0,
             use_vertex_group: bool = False,
             vertex_group_factor: float = 1.0,
             invert_vertex_group: bool = False,
             use_symmetry: bool = False,
             symmetry_axis: typing.Union[int, str] = 'Y'):
    ''' Simplify geometry by collapsing edges

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param ratio: Ratio
    :type ratio: float
    :param use_vertex_group: Vertex Group, Use active vertex group as an influence
    :type use_vertex_group: bool
    :param vertex_group_factor: Weight, Vertex group strength
    :type vertex_group_factor: float
    :param invert_vertex_group: Invert, Invert vertex group influence
    :type invert_vertex_group: bool
    :param use_symmetry: Symmetry, Maintain symmetry on an axis
    :type use_symmetry: bool
    :param symmetry_axis: Axis, Axis of symmetry
    :type symmetry_axis: typing.Union[int, str]
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           type: typing.Union[str, int] = 'VERT'):
    ''' Delete selected vertices, edges or faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Method used for deleting mesh data
    :type type: typing.Union[str, int]
    '''

    pass


def delete_edgeloop(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    use_face_split: bool = True):
    ''' Delete an edge loop by merging the faces on each side

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: bool
    '''

    pass


def delete_loose(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 use_verts: bool = True,
                 use_edges: bool = True,
                 use_faces: bool = False):
    ''' Delete loose vertices, edges or faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_verts: Vertices, Remove loose vertices
    :type use_verts: bool
    :param use_edges: Edges, Remove loose edges
    :type use_edges: bool
    :param use_faces: Faces, Remove loose faces
    :type use_faces: bool
    '''

    pass


def dissolve_degenerate(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        threshold: float = 0.0001):
    ''' Dissolve zero area faces and zero length edges

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param threshold: Merge Distance, Maximum distance between elements to merge
    :type threshold: float
    '''

    pass


def dissolve_edges(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   use_verts: bool = True,
                   use_face_split: bool = False):
    ''' Dissolve edges, merging faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_verts: Dissolve Vertices, Dissolve remaining vertices
    :type use_verts: bool
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: bool
    '''

    pass


def dissolve_faces(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   use_verts: bool = False):
    ''' Dissolve faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_verts: Dissolve Vertices, Dissolve remaining vertices
    :type use_verts: bool
    '''

    pass


def dissolve_limited(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        angle_limit: float = 0.0872665,
        use_dissolve_boundaries: bool = False,
        delimit: typing.Union[typing.Set[int], typing.Set[str]] = {'NORMAL'}):
    ''' Dissolve selected edges and vertices, limited by the angle of surrounding geometry

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param angle_limit: Max Angle, Angle limit
    :type angle_limit: float
    :param use_dissolve_boundaries: All Boundaries, Dissolve all vertices in between face boundaries
    :type use_dissolve_boundaries: bool
    :param delimit: Delimit, Delimit dissolve operation
    :type delimit: typing.Union[typing.Set[int], typing.Set[str]]
    '''

    pass


def dissolve_mode(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  use_verts: bool = False,
                  use_face_split: bool = False,
                  use_boundary_tear: bool = False):
    ''' Dissolve geometry based on the selection mode

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_verts: Dissolve Vertices, Dissolve remaining vertices
    :type use_verts: bool
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: bool
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces
    :type use_boundary_tear: bool
    '''

    pass


def dissolve_verts(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   use_face_split: bool = False,
                   use_boundary_tear: bool = False):
    ''' Dissolve vertices, merge edges and faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: bool
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces
    :type use_boundary_tear: bool
    '''

    pass


def dupli_extrude_cursor(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         rotate_source: bool = True):
    ''' Duplicate and extrude selected vertices, edges or faces towards the mouse cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param rotate_source: Rotate Source, Rotate initial selection giving better shape
    :type rotate_source: bool
    '''

    pass


def duplicate(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              mode: int = 1):
    ''' Duplicate selected vertices, edges or faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: int
    '''

    pass


def duplicate_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        MESH_OT_duplicate: 'duplicate' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Duplicate mesh and move

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param MESH_OT_duplicate: Duplicate, Duplicate selected vertices, edges or faces
    :type MESH_OT_duplicate: 'duplicate'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def edge_collapse(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Collapse isolated edge and face regions, merging data such as UV's and color attributes. This can collapse edge-rings as well as regions of connected faces into vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def edge_face_add(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Add an edge or face to selected

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def edge_rotate(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                use_ccw: bool = False):
    ''' Rotate selected edge or adjoining faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_ccw: Counter Clockwise
    :type use_ccw: bool
    '''

    pass


def edge_split(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               type: typing.Union[str, int] = 'EDGE'):
    ''' Split selected edges so that each neighbor face gets its own copy

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Method to use for splitting * EDGE Faces by Edges -- Split faces along selected edges. * VERT Faces & Edges by Vertices -- Split faces and edges connected to selected vertices.
    :type type: typing.Union[str, int]
    '''

    pass


def edgering_select(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    extend: bool = False,
                    deselect: bool = False,
                    toggle: bool = False,
                    ring: bool = True):
    ''' Select an edge ring

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend the selection
    :type extend: bool
    :param deselect: Deselect, Remove from the selection
    :type deselect: bool
    :param toggle: Toggle Select, Toggle the selection
    :type toggle: bool
    :param ring: Select Ring, Select ring
    :type ring: bool
    '''

    pass


def edges_select_sharp(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       sharpness: float = 0.523599):
    ''' Select all sharp enough edges

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param sharpness: Sharpness
    :type sharpness: float
    '''

    pass


def extrude_context(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    use_normal_flip: bool = False,
                    use_dissolve_ortho_edges: bool = False,
                    mirror: bool = False):
    ''' Extrude selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: bool
    :param use_dissolve_ortho_edges: Dissolve Orthogonal Edges
    :type use_dissolve_ortho_edges: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    '''

    pass


def extrude_context_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        MESH_OT_extrude_context: 'extrude_context' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Extrude region together along the average normal

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param MESH_OT_extrude_context: Extrude Context, Extrude selection
    :type MESH_OT_extrude_context: 'extrude_context'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def extrude_edges_indiv(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        use_normal_flip: bool = False,
                        mirror: bool = False):
    ''' Extrude individual edges only

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    '''

    pass


def extrude_edges_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        MESH_OT_extrude_edges_indiv: 'extrude_edges_indiv' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Extrude edges and move result

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only
    :type MESH_OT_extrude_edges_indiv: 'extrude_edges_indiv'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def extrude_faces_indiv(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        mirror: bool = False):
    ''' Extrude individual faces only

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    '''

    pass


def extrude_faces_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        MESH_OT_extrude_faces_indiv: 'extrude_faces_indiv' = None,
        TRANSFORM_OT_shrink_fatten: 'bpy.ops.transform.shrink_fatten' = None):
    ''' Extrude each individual face separately along local normals

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param MESH_OT_extrude_faces_indiv: Extrude Individual Faces, Extrude individual faces only
    :type MESH_OT_extrude_faces_indiv: 'extrude_faces_indiv'
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals
    :type TRANSFORM_OT_shrink_fatten: 'bpy.ops.transform.shrink_fatten'
    '''

    pass


def extrude_manifold(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        MESH_OT_extrude_region: 'extrude_region' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Extrude, dissolves edges whose faces form a flat surface and intersect new edges

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :type MESH_OT_extrude_region: 'extrude_region'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def extrude_region(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   use_normal_flip: bool = False,
                   use_dissolve_ortho_edges: bool = False,
                   mirror: bool = False):
    ''' Extrude region of faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: bool
    :param use_dissolve_ortho_edges: Dissolve Orthogonal Edges
    :type use_dissolve_ortho_edges: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    '''

    pass


def extrude_region_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        MESH_OT_extrude_region: 'extrude_region' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Extrude region and move result

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :type MESH_OT_extrude_region: 'extrude_region'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def extrude_region_shrink_fatten(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        MESH_OT_extrude_region: 'extrude_region' = None,
        TRANSFORM_OT_shrink_fatten: 'bpy.ops.transform.shrink_fatten' = None):
    ''' Extrude region together along local normals

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :type MESH_OT_extrude_region: 'extrude_region'
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals
    :type TRANSFORM_OT_shrink_fatten: 'bpy.ops.transform.shrink_fatten'
    '''

    pass


def extrude_repeat(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        steps: int = 10,
        offset: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale_offset: float = 1.0):
    ''' Extrude selected vertices, edges or faces repeatedly

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param steps: Steps
    :type steps: int
    :param offset: Offset, Offset vector
    :type offset: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale_offset: Scale Offset
    :type scale_offset: float
    '''

    pass


def extrude_vertices_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        MESH_OT_extrude_verts_indiv: 'extrude_verts_indiv' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Extrude vertices and move result

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param MESH_OT_extrude_verts_indiv: Extrude Only Vertices, Extrude individual vertices only
    :type MESH_OT_extrude_verts_indiv: 'extrude_verts_indiv'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def extrude_verts_indiv(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        mirror: bool = False):
    ''' Extrude individual vertices only

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    '''

    pass


def face_make_planar(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     factor: float = 1.0,
                     repeat: int = 1):
    ''' Flatten selected faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param factor: Factor
    :type factor: float
    :param repeat: Iterations
    :type repeat: int
    '''

    pass


def face_set_extract(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     add_boundary_loop: bool = True,
                     smooth_iterations: int = 4,
                     apply_shrinkwrap: bool = True,
                     add_solidify: bool = True):
    ''' Create a new mesh object from the selected Face Set

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param add_boundary_loop: Add Boundary Loop, Add an extra edge loop to better preserve the shape when applying a subdivision surface modifier
    :type add_boundary_loop: bool
    :param smooth_iterations: Smooth Iterations, Smooth iterations applied to the extracted mesh
    :type smooth_iterations: int
    :param apply_shrinkwrap: Project to Sculpt, Project the extracted mesh into the original sculpt
    :type apply_shrinkwrap: bool
    :param add_solidify: Extract as Solid, Extract the mask as a solid object with a solidify modifier
    :type add_solidify: bool
    '''

    pass


def face_split_by_edges(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Weld loose edges into faces (splitting them into new faces)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def faces_mirror_uv(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    direction: typing.Union[str, int] = 'POSITIVE',
                    precision: int = 3):
    ''' Copy mirror UV coordinates on the X axis based on a mirrored mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param direction: Axis Direction
    :type direction: typing.Union[str, int]
    :param precision: Precision, Tolerance for finding vertex duplicates
    :type precision: int
    '''

    pass


def faces_select_linked_flat(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None,
                             *,
                             sharpness: float = 0.0174533):
    ''' Select linked faces by angle

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param sharpness: Sharpness
    :type sharpness: float
    '''

    pass


def faces_shade_flat(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Display faces flat

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def faces_shade_smooth(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Display faces smooth (using vertex normals)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def fill(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         use_beauty: bool = True):
    ''' Fill a selected edge loop with faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_beauty: Beauty, Use best triangulation division
    :type use_beauty: bool
    '''

    pass


def fill_grid(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              span: int = 1,
              offset: int = 0,
              use_interp_simple: bool = False):
    ''' Fill grid from two loops

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param span: Span, Number of grid columns
    :type span: int
    :param offset: Offset, Vertex that is the corner of the grid
    :type offset: int
    :param use_interp_simple: Simple Blending, Use simple interpolation of grid vertices
    :type use_interp_simple: bool
    '''

    pass


def fill_holes(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               sides: int = 4):
    ''' Fill in holes (boundary edge loops)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param sides: Sides, Number of sides in hole required to fill (zero fills all holes)
    :type sides: int
    '''

    pass


def flip_normals(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 only_clnors: bool = False):
    ''' Flip the direction of selected faces' normals (and of their vertices)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param only_clnors: Custom Normals Only, Only flip the custom loop normals of the selected elements
    :type only_clnors: bool
    '''

    pass


def hide(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         unselected: bool = False):
    ''' Hide (un)selected vertices, edges or faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: bool
    '''

    pass


def inset(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None,
          *,
          use_boundary: bool = True,
          use_even_offset: bool = True,
          use_relative_offset: bool = False,
          use_edge_rail: bool = False,
          thickness: float = 0.0,
          depth: float = 0.0,
          use_outset: bool = False,
          use_select_inset: bool = False,
          use_individual: bool = False,
          use_interpolate: bool = True,
          release_confirm: bool = False):
    ''' Inset new faces into selected faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_boundary: Boundary, Inset face boundaries
    :type use_boundary: bool
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :type use_even_offset: bool
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
    :type use_relative_offset: bool
    :param use_edge_rail: Edge Rail, Inset the region along existing edges
    :type use_edge_rail: bool
    :param thickness: Thickness
    :type thickness: float
    :param depth: Depth
    :type depth: float
    :param use_outset: Outset, Outset rather than inset
    :type use_outset: bool
    :param use_select_inset: Select Outer, Select the new inset faces
    :type use_select_inset: bool
    :param use_individual: Individual, Individual face inset
    :type use_individual: bool
    :param use_interpolate: Interpolate, Blend face data across the inset
    :type use_interpolate: bool
    :param release_confirm: Confirm on Release
    :type release_confirm: bool
    '''

    pass


def intersect(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              mode: typing.Union[str, int] = 'SELECT_UNSELECT',
              separate_mode: typing.Union[str, int] = 'CUT',
              threshold: float = 1e-06,
              solver: typing.Union[str, int] = 'EXACT'):
    ''' Cut an intersection into faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Source * SELECT Self Intersect -- Self intersect selected faces. * SELECT_UNSELECT Selected/Unselected -- Intersect selected with unselected faces.
    :type mode: typing.Union[str, int]
    :param separate_mode: Separate Mode * ALL All -- Separate all geometry from intersections. * CUT Cut -- Cut into geometry keeping each side separate (Selected/Unselected only). * NONE Merge -- Merge all geometry from the intersection.
    :type separate_mode: typing.Union[str, int]
    :param threshold: Merge Threshold
    :type threshold: float
    :param solver: Solver, Which Intersect solver to use * FAST Fast -- Faster solver, some limitations. * EXACT Exact -- Exact solver, slower, handles more cases.
    :type solver: typing.Union[str, int]
    '''

    pass


def intersect_boolean(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      operation: typing.Union[str, int] = 'DIFFERENCE',
                      use_swap: bool = False,
                      use_self: bool = False,
                      threshold: float = 1e-06,
                      solver: typing.Union[str, int] = 'EXACT'):
    ''' Cut solid geometry from selected to unselected

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param operation: Boolean Operation, Which boolean operation to apply
    :type operation: typing.Union[str, int]
    :param use_swap: Swap, Use with difference intersection to swap which side is kept
    :type use_swap: bool
    :param use_self: Self Intersection, Do self-union or self-intersection
    :type use_self: bool
    :param threshold: Merge Threshold
    :type threshold: float
    :param solver: Solver, Which Boolean solver to use * FAST Fast -- Faster solver, some limitations. * EXACT Exact -- Exact solver, slower, handles more cases.
    :type solver: typing.Union[str, int]
    '''

    pass


def knife_project(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  cut_through: bool = False):
    ''' Use other objects outlines and boundaries to project knife cuts

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param cut_through: Cut Through, Cut through all faces, not just visible ones
    :type cut_through: bool
    '''

    pass


def knife_tool(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               use_occlude_geometry: bool = True,
               only_selected: bool = False,
               xray: bool = True,
               visible_measurements: typing.Union[str, int] = 'NONE',
               angle_snapping: typing.Union[str, int] = 'NONE',
               angle_snapping_increment: float = 0.523599,
               wait_for_input: bool = True):
    ''' Cut new topology

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_occlude_geometry: Occlude Geometry, Only cut the front most geometry
    :type use_occlude_geometry: bool
    :param only_selected: Only Selected, Only cut selected geometry
    :type only_selected: bool
    :param xray: X-Ray, Show cuts hidden by geometry
    :type xray: bool
    :param visible_measurements: Measurements, Visible distance and angle measurements * NONE None -- Show no measurements. * BOTH Both -- Show both distances and angles. * DISTANCE Distance -- Show just distance measurements. * ANGLE Angle -- Show just angle measurements.
    :type visible_measurements: typing.Union[str, int]
    :param angle_snapping: Angle Snapping, Angle snapping mode * NONE None -- No angle snapping. * SCREEN Screen -- Screen space angle snapping. * RELATIVE Relative -- Angle snapping relative to the previous cut edge.
    :type angle_snapping: typing.Union[str, int]
    :param angle_snapping_increment: Angle Snap Increment, The angle snap increment used when in constrained angle mode
    :type angle_snapping_increment: float
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def loop_multi_select(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      ring: bool = False):
    ''' Select a loop of connected edges by connection type

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param ring: Ring
    :type ring: bool
    '''

    pass


def loop_select(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                extend: bool = False,
                deselect: bool = False,
                toggle: bool = False,
                ring: bool = False):
    ''' Select a loop of connected edges

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend Select, Extend the selection
    :type extend: bool
    :param deselect: Deselect, Remove from the selection
    :type deselect: bool
    :param toggle: Toggle Select, Toggle the selection
    :type toggle: bool
    :param ring: Select Ring, Select ring
    :type ring: bool
    '''

    pass


def loop_to_region(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   select_bigger: bool = False):
    ''' Select region of faces inside of a selected loop of edges

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param select_bigger: Select Bigger, Select bigger regions instead of smaller ones
    :type select_bigger: bool
    '''

    pass


def loopcut(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: bool = None,
            *,
            number_cuts: int = 1,
            smoothness: float = 0.0,
            falloff: typing.Union[int, str] = 'INVERSE_SQUARE',
            object_index: int = -1,
            edge_index: int = -1,
            mesh_select_mode_init: typing.List[bool] = (False, False, False)):
    ''' Add a new loop between existing loops

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param number_cuts: Number of Cuts
    :type number_cuts: int
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: float
    :param falloff: Falloff, Falloff type the feather
    :type falloff: typing.Union[int, str]
    :param object_index: Object Index
    :type object_index: int
    :param edge_index: Edge Index
    :type edge_index: int
    :type mesh_select_mode_init: typing.List[bool]
    '''

    pass


def loopcut_slide(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        MESH_OT_loopcut: 'loopcut' = None,
        TRANSFORM_OT_edge_slide: 'bpy.ops.transform.edge_slide' = None):
    ''' Cut mesh loop and slide it

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param MESH_OT_loopcut: Loop Cut, Add a new loop between existing loops
    :type MESH_OT_loopcut: 'loopcut'
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh
    :type TRANSFORM_OT_edge_slide: 'bpy.ops.transform.edge_slide'
    '''

    pass


def mark_freestyle_edge(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        clear: bool = False):
    ''' (Un)mark selected edges as Freestyle feature edges

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param clear: Clear
    :type clear: bool
    '''

    pass


def mark_freestyle_face(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        clear: bool = False):
    ''' (Un)mark selected faces for exclusion from Freestyle feature edge detection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param clear: Clear
    :type clear: bool
    '''

    pass


def mark_seam(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              clear: bool = False):
    ''' (Un)mark selected edges as a seam

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param clear: Clear
    :type clear: bool
    '''

    pass


def mark_sharp(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               clear: bool = False,
               use_verts: bool = False):
    ''' (Un)mark selected edges as sharp

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param clear: Clear
    :type clear: bool
    :param use_verts: Vertices, Consider vertices instead of edges to select which edges to (un)tag as sharp
    :type use_verts: bool
    '''

    pass


def merge(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None,
          *,
          type: typing.Union[str, int] = 'CENTER',
          uvs: bool = False):
    ''' Merge selected vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Merge method to use
    :type type: typing.Union[str, int]
    :param uvs: UVs, Move UVs according to merge
    :type uvs: bool
    '''

    pass


def merge_normals(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Merge custom normals of selected vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def mod_weighted_strength(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          set: bool = False,
                          face_strength: typing.Union[str, int] = 'MEDIUM'):
    ''' Set/Get strength of face (used in Weighted Normal modifier)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param set: Set Value, Set value of faces
    :type set: bool
    :param face_strength: Face Strength, Strength to use for assigning or selecting face influence for weighted normal modifier
    :type face_strength: typing.Union[str, int]
    '''

    pass


def normals_make_consistent(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None,
                            *,
                            inside: bool = False):
    ''' Make face and vertex normals point either outside or inside the mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param inside: Inside
    :type inside: bool
    '''

    pass


def normals_tools(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  mode: typing.Union[str, int] = 'COPY',
                  absolute: bool = False):
    ''' Custom normals tools using Normal Vector of UI

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode, Mode of tools taking input from interface * COPY Copy Normal -- Copy normal to buffer. * PASTE Paste Normal -- Paste normal from buffer. * ADD Add Normal -- Add normal vector with selection. * MULTIPLY Multiply Normal -- Multiply normal vector with selection. * RESET Reset Normal -- Reset buffer and/or normal of selected element.
    :type mode: typing.Union[str, int]
    :param absolute: Absolute Coordinates, Copy Absolute coordinates or Normal vector
    :type absolute: bool
    '''

    pass


def offset_edge_loops(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      use_cap_endpoint: bool = False):
    ''' Create offset edge loop from the current selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_cap_endpoint: Cap Endpoint, Extend loop around end-points
    :type use_cap_endpoint: bool
    '''

    pass


def offset_edge_loops_slide(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        MESH_OT_offset_edge_loops: 'offset_edge_loops' = None,
        TRANSFORM_OT_edge_slide: 'bpy.ops.transform.edge_slide' = None):
    ''' Offset edge loop slide

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param MESH_OT_offset_edge_loops: Offset Edge Loop, Create offset edge loop from the current selection
    :type MESH_OT_offset_edge_loops: 'offset_edge_loops'
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh
    :type TRANSFORM_OT_edge_slide: 'bpy.ops.transform.edge_slide'
    '''

    pass


def paint_mask_extract(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       mask_threshold: float = 0.5,
                       add_boundary_loop: bool = True,
                       smooth_iterations: int = 4,
                       apply_shrinkwrap: bool = True,
                       add_solidify: bool = True):
    ''' Create a new mesh object from the current paint mask

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mask_threshold: Threshold, Minimum mask value to consider the vertex valid to extract a face from the original mesh
    :type mask_threshold: float
    :param add_boundary_loop: Add Boundary Loop, Add an extra edge loop to better preserve the shape when applying a subdivision surface modifier
    :type add_boundary_loop: bool
    :param smooth_iterations: Smooth Iterations, Smooth iterations applied to the extracted mesh
    :type smooth_iterations: int
    :param apply_shrinkwrap: Project to Sculpt, Project the extracted mesh into the original sculpt
    :type apply_shrinkwrap: bool
    :param add_solidify: Extract as Solid, Extract the mask as a solid object with a solidify modifier
    :type add_solidify: bool
    '''

    pass


def paint_mask_slice(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     mask_threshold: float = 0.5,
                     fill_holes: bool = True,
                     new_object: bool = True):
    ''' Slices the paint mask from the mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mask_threshold: Threshold, Minimum mask value to consider the vertex valid to extract a face from the original mesh
    :type mask_threshold: float
    :param fill_holes: Fill Holes, Fill holes after slicing the mask
    :type fill_holes: bool
    :param new_object: Slice to New Object, Create a new object from the sliced mask
    :type new_object: bool
    '''

    pass


def point_normals(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        mode: typing.Union[str, int] = 'COORDINATES',
        invert: bool = False,
        align: bool = False,
        target_location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        spherize: bool = False,
        spherize_strength: float = 0.1):
    ''' Point selected custom normals to specified Target

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode, How to define coordinates to point custom normals to * COORDINATES Coordinates -- Use static coordinates (defined by various means). * MOUSE Mouse -- Follow mouse cursor.
    :type mode: typing.Union[str, int]
    :param invert: Invert, Invert affected normals
    :type invert: bool
    :param align: Align, Make all affected normals parallel
    :type align: bool
    :param target_location: Target, Target location to which normals will point
    :type target_location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param spherize: Spherize, Interpolate between original and new normals
    :type spherize: bool
    :param spherize_strength: Spherize Strength, Ratio of spherized normal to original normal
    :type spherize_strength: float
    '''

    pass


def poke(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         offset: float = 0.0,
         use_relative_offset: bool = False,
         center_mode: typing.Union[str, int] = 'MEDIAN_WEIGHTED'):
    ''' Split a face into a fan

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param offset: Poke Offset, Poke Offset
    :type offset: float
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
    :type use_relative_offset: bool
    :param center_mode: Poke Center, Poke face center calculation * MEDIAN_WEIGHTED Weighted Median -- Weighted median face center. * MEDIAN Median -- Median face center. * BOUNDS Bounds -- Face bounds center.
    :type center_mode: typing.Union[str, int]
    '''

    pass


def polybuild_delete_at_cursor(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        mirror: bool = False,
        use_proportional_edit: bool = False,
        proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
        proportional_size: float = 1.0,
        use_proportional_connected: bool = False,
        use_proportional_projected: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def polybuild_dissolve_at_cursor(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def polybuild_extrude_at_cursor_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        MESH_OT_polybuild_transform_at_cursor:
        'polybuild_transform_at_cursor' = None,
        MESH_OT_extrude_edges_indiv: 'extrude_edges_indiv' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor
    :type MESH_OT_polybuild_transform_at_cursor: 'polybuild_transform_at_cursor'
    :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only
    :type MESH_OT_extrude_edges_indiv: 'extrude_edges_indiv'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def polybuild_face_at_cursor(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        create_quads: bool = True,
        mirror: bool = False,
        use_proportional_edit: bool = False,
        proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
        proportional_size: float = 1.0,
        use_proportional_connected: bool = False,
        use_proportional_projected: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param create_quads: Create Quads, Automatically split edges in triangles to maintain quad topology
    :type create_quads: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def polybuild_face_at_cursor_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        MESH_OT_polybuild_face_at_cursor: 'polybuild_face_at_cursor' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param MESH_OT_polybuild_face_at_cursor: Poly Build Face at Cursor
    :type MESH_OT_polybuild_face_at_cursor: 'polybuild_face_at_cursor'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def polybuild_split_at_cursor(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        mirror: bool = False,
        use_proportional_edit: bool = False,
        proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
        proportional_size: float = 1.0,
        use_proportional_connected: bool = False,
        use_proportional_projected: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def polybuild_split_at_cursor_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        MESH_OT_polybuild_split_at_cursor: 'polybuild_split_at_cursor' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param MESH_OT_polybuild_split_at_cursor: Poly Build Split at Cursor
    :type MESH_OT_polybuild_split_at_cursor: 'polybuild_split_at_cursor'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def polybuild_transform_at_cursor(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        mirror: bool = False,
        use_proportional_edit: bool = False,
        proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
        proportional_size: float = 1.0,
        use_proportional_connected: bool = False,
        use_proportional_projected: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def polybuild_transform_at_cursor_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        MESH_OT_polybuild_transform_at_cursor:
        'polybuild_transform_at_cursor' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor
    :type MESH_OT_polybuild_transform_at_cursor: 'polybuild_transform_at_cursor'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def primitive_circle_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        vertices: int = 32,
        radius: float = 1.0,
        fill_type: typing.Union[str, int] = 'NOTHING',
        calc_uvs: bool = True,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Construct a circle mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param vertices: Vertices
    :type vertices: int
    :param radius: Radius
    :type radius: float
    :param fill_type: Fill Type * NOTHING Nothing -- Don't fill at all. * NGON N-Gon -- Use n-gons. * TRIFAN Triangle Fan -- Use triangle fans.
    :type fill_type: typing.Union[str, int]
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: bool
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def primitive_cone_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        vertices: int = 32,
        radius1: float = 1.0,
        radius2: float = 0.0,
        depth: float = 2.0,
        end_fill_type: typing.Union[str, int] = 'NGON',
        calc_uvs: bool = True,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Construct a conic mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param vertices: Vertices
    :type vertices: int
    :param radius1: Radius 1
    :type radius1: float
    :param radius2: Radius 2
    :type radius2: float
    :param depth: Depth
    :type depth: float
    :param end_fill_type: Base Fill Type * NOTHING Nothing -- Don't fill at all. * NGON N-Gon -- Use n-gons. * TRIFAN Triangle Fan -- Use triangle fans.
    :type end_fill_type: typing.Union[str, int]
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: bool
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def primitive_cube_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        size: float = 2.0,
        calc_uvs: bool = True,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Construct a cube mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param size: Size
    :type size: float
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: bool
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def primitive_cube_add_gizmo(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        calc_uvs: bool = True,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0),
        matrix: typing.
        Union[typing.List[typing.List[float]], typing.
              Tuple[typing.Tuple[float, float, float, float], typing.
                    Tuple[float, float, float, float], typing.
                    Tuple[float, float, float, float], typing.
                    Tuple[float, float, float, float]], 'mathutils.Matrix'] = (
                        (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0),
                        (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))):
    ''' Construct a cube mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: bool
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param matrix: Matrix
    :type matrix: typing.Union[typing.List[typing.List[float]], typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]], 'mathutils.Matrix']
    '''

    pass


def primitive_cylinder_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        vertices: int = 32,
        radius: float = 1.0,
        depth: float = 2.0,
        end_fill_type: typing.Union[str, int] = 'NGON',
        calc_uvs: bool = True,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Construct a cylinder mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param vertices: Vertices
    :type vertices: int
    :param radius: Radius
    :type radius: float
    :param depth: Depth
    :type depth: float
    :param end_fill_type: Cap Fill Type * NOTHING Nothing -- Don't fill at all. * NGON N-Gon -- Use n-gons. * TRIFAN Triangle Fan -- Use triangle fans.
    :type end_fill_type: typing.Union[str, int]
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: bool
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def primitive_grid_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        x_subdivisions: int = 10,
        y_subdivisions: int = 10,
        size: float = 2.0,
        calc_uvs: bool = True,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Construct a grid mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param x_subdivisions: X Subdivisions
    :type x_subdivisions: int
    :param y_subdivisions: Y Subdivisions
    :type y_subdivisions: int
    :param size: Size
    :type size: float
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: bool
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def primitive_ico_sphere_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        subdivisions: int = 2,
        radius: float = 1.0,
        calc_uvs: bool = True,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Construct an Icosphere mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param subdivisions: Subdivisions
    :type subdivisions: int
    :param radius: Radius
    :type radius: float
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: bool
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def primitive_monkey_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        size: float = 2.0,
        calc_uvs: bool = True,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Construct a Suzanne mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param size: Size
    :type size: float
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: bool
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def primitive_plane_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        size: float = 2.0,
        calc_uvs: bool = True,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Construct a filled planar mesh with 4 vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param size: Size
    :type size: float
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: bool
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def primitive_torus_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        major_segments: int = 48,
        minor_segments: int = 12,
        mode: typing.Union[str, int] = 'MAJOR_MINOR',
        major_radius: float = 1.0,
        minor_radius: float = 0.25,
        abso_major_rad: float = 1.25,
        abso_minor_rad: float = 0.75,
        generate_uvs: bool = True):
    ''' Construct a torus mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param align: Align * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param major_segments: Major Segments, Number of segments for the main ring of the torus
    :type major_segments: int
    :param minor_segments: Minor Segments, Number of segments for the minor ring of the torus
    :type minor_segments: int
    :param mode: Dimensions Mode * MAJOR_MINOR Major/Minor -- Use the major/minor radii for torus dimensions. * EXT_INT Exterior/Interior -- Use the exterior/interior radii for torus dimensions.
    :type mode: typing.Union[str, int]
    :param major_radius: Major Radius, Radius from the origin to the center of the cross sections
    :type major_radius: float
    :param minor_radius: Minor Radius, Radius of the torus' cross section
    :type minor_radius: float
    :param abso_major_rad: Exterior Radius, Total Exterior Radius of the torus
    :type abso_major_rad: float
    :param abso_minor_rad: Interior Radius, Total Interior Radius of the torus
    :type abso_minor_rad: float
    :param generate_uvs: Generate UVs, Generate a default UV map
    :type generate_uvs: bool
    '''

    pass


def primitive_uv_sphere_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        segments: int = 32,
        ring_count: int = 16,
        radius: float = 1.0,
        calc_uvs: bool = True,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Construct a UV sphere mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param segments: Segments
    :type segments: int
    :param ring_count: Rings
    :type ring_count: int
    :param radius: Radius
    :type radius: float
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: bool
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def quads_convert_to_tris(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          quad_method: typing.Union[int, str] = 'BEAUTY',
                          ngon_method: typing.Union[int, str] = 'BEAUTY'):
    ''' Triangulate selected faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param quad_method: Quad Method, Method for splitting the quads into triangles
    :type quad_method: typing.Union[int, str]
    :param ngon_method: N-gon Method, Method for splitting the n-gons into triangles
    :type ngon_method: typing.Union[int, str]
    '''

    pass


def region_to_loop(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Select boundary edges around the selected faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def remove_doubles(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   threshold: float = 0.0001,
                   use_unselected: bool = False,
                   use_sharp_edge_from_normals: bool = False):
    ''' Merge vertices based on their proximity

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param threshold: Merge Distance, Maximum distance between elements to merge
    :type threshold: float
    :param use_unselected: Unselected, Merge selected to other unselected vertices
    :type use_unselected: bool
    :param use_sharp_edge_from_normals: Sharp Edges, Calculate sharp edges using custom normal data (when available)
    :type use_sharp_edge_from_normals: bool
    '''

    pass


def reveal(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           select: bool = True):
    ''' Reveal all hidden vertices, edges and faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param select: Select
    :type select: bool
    '''

    pass


def rip(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        mirror: bool = False,
        use_proportional_edit: bool = False,
        proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
        proportional_size: float = 1.0,
        use_proportional_connected: bool = False,
        use_proportional_projected: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False,
        use_fill: bool = False):
    ''' Disconnect vertex or edges from connected geometry

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    :param use_fill: Fill, Fill the ripped region
    :type use_fill: bool
    '''

    pass


def rip_edge(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             mirror: bool = False,
             use_proportional_edit: bool = False,
             proportional_edit_falloff: typing.Union[int, str] = 'SMOOTH',
             proportional_size: float = 1.0,
             use_proportional_connected: bool = False,
             use_proportional_projected: bool = False,
             release_confirm: bool = False,
             use_accurate: bool = False):
    ''' Extend vertices along the edge closest to the cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Union[int, str]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def rip_edge_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        MESH_OT_rip_edge: 'rip_edge' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Extend vertices and move the result

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param MESH_OT_rip_edge: Extend Vertices, Extend vertices along the edge closest to the cursor
    :type MESH_OT_rip_edge: 'rip_edge'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def rip_move(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             MESH_OT_rip: 'rip' = None,
             TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Rip polygons and move the result

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param MESH_OT_rip: Rip, Disconnect vertex or edges from connected geometry
    :type MESH_OT_rip: 'rip'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def screw(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        steps: int = 9,
        turns: int = 1,
        center: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        axis: typing.Union[typing.List[float], typing.
                           Tuple[float, float, float], 'mathutils.Vector'] = (
                               0.0, 0.0, 0.0)):
    ''' Extrude selected vertices in screw-shaped rotation around the cursor in indicated viewport

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param steps: Steps, Steps
    :type steps: int
    :param turns: Turns, Turns
    :type turns: int
    :param center: Center, Center in global view space
    :type center: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param axis: Axis, Axis in global view space
    :type axis: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def sculpt_vertex_color_add(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None):
    ''' Add vertex color layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def sculpt_vertex_color_remove(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Remove vertex color layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               action: typing.Union[str, int] = 'TOGGLE'):
    ''' (De)select all vertices, edges or faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_axis(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                orientation: typing.Union[int, str] = 'LOCAL',
                sign: typing.Union[str, int] = 'POS',
                axis: typing.Union[int, str] = 'X',
                threshold: float = 0.0001):
    ''' Select all data in the mesh on a single axis

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param orientation: Axis Mode, Axis orientation
    :type orientation: typing.Union[int, str]
    :param sign: Axis Sign, Side to select
    :type sign: typing.Union[str, int]
    :param axis: Axis, Select the axis to compare each vertex on
    :type axis: typing.Union[int, str]
    :param threshold: Threshold
    :type threshold: float
    '''

    pass


def select_face_by_sides(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         number: int = 4,
                         type: typing.Union[str, int] = 'EQUAL',
                         extend: bool = True):
    ''' Select vertices or faces by the number of polygon sides

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param number: Number of Vertices
    :type number: int
    :param type: Type, Type of comparison to make
    :type type: typing.Union[str, int]
    :param extend: Extend, Extend the selection
    :type extend: bool
    '''

    pass


def select_interior_faces(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Select faces where all edges have more than 2 face users

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_less(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                use_face_step: bool = True):
    ''' Deselect vertices, edges or faces at the boundary of each selection region

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_face_step: Face Step, Connected faces (instead of edges)
    :type use_face_step: bool
    '''

    pass


def select_linked(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        delimit: typing.Union[typing.Set[int], typing.Set[str]] = {'SEAM'}):
    ''' Select all vertices connected to the current selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param delimit: Delimit, Delimit selected region
    :type delimit: typing.Union[typing.Set[int], typing.Set[str]]
    '''

    pass


def select_linked_pick(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        deselect: bool = False,
        delimit: typing.Union[typing.Set[int], typing.Set[str]] = {'SEAM'},
        object_index: int = -1,
        index: int = -1):
    ''' (De)select all vertices linked to the edge under the mouse cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param deselect: Deselect
    :type deselect: bool
    :param delimit: Delimit, Delimit selected region
    :type delimit: typing.Union[typing.Set[int], typing.Set[str]]
    :type object_index: int
    :type index: int
    '''

    pass


def select_loose(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 extend: bool = False):
    ''' Select loose geometry based on the selection mode

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend the selection
    :type extend: bool
    '''

    pass


def select_mirror(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  axis: typing.Union[typing.Set[int], typing.Set[str]] = {'X'},
                  extend: bool = False):
    ''' Select mesh items at mirrored locations

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param axis: Axis
    :type axis: typing.Union[typing.Set[int], typing.Set[str]]
    :param extend: Extend, Extend the existing selection
    :type extend: bool
    '''

    pass


def select_mode(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                use_extend: bool = False,
                use_expand: bool = False,
                type: typing.Union[int, str] = 'VERT',
                action: typing.Union[str, int] = 'TOGGLE'):
    ''' Change selection mode

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_extend: Extend
    :type use_extend: bool
    :param use_expand: Expand
    :type use_expand: bool
    :param type: Type
    :type type: typing.Union[int, str]
    :param action: Action, Selection action to execute * DISABLE Disable -- Disable selected markers. * ENABLE Enable -- Enable selected markers. * TOGGLE Toggle -- Toggle disabled flag for selected markers.
    :type action: typing.Union[str, int]
    '''

    pass


def select_more(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                use_face_step: bool = True):
    ''' Select more vertices, edges or faces connected to initial selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_face_step: Face Step, Connected faces (instead of edges)
    :type use_face_step: bool
    '''

    pass


def select_next_item(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Select the next element (using selection order) :file: startup/bl_operators/mesh.py\:194 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/mesh.py$194> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_non_manifold(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        extend: bool = True,
                        use_wire: bool = True,
                        use_boundary: bool = True,
                        use_multi_face: bool = True,
                        use_non_contiguous: bool = True,
                        use_verts: bool = True):
    ''' Select all non-manifold vertices or edges

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend the selection
    :type extend: bool
    :param use_wire: Wire, Wire edges
    :type use_wire: bool
    :param use_boundary: Boundaries, Boundary edges
    :type use_boundary: bool
    :param use_multi_face: Multiple Faces, Edges shared by more than two faces
    :type use_multi_face: bool
    :param use_non_contiguous: Non Contiguous, Edges between faces pointing in alternate directions
    :type use_non_contiguous: bool
    :param use_verts: Vertices, Vertices connecting multiple face regions
    :type use_verts: bool
    '''

    pass


def select_nth(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               skip: int = 1,
               nth: int = 1,
               offset: int = 0):
    ''' Deselect every Nth element starting from the active vertex, edge or face

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: int
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: int
    :param offset: Offset, Offset from the starting point
    :type offset: int
    '''

    pass


def select_prev_item(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Select the previous element (using selection order) :file: startup/bl_operators/mesh.py\:219 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/mesh.py$219> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_random(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  ratio: float = 0.5,
                  seed: int = 0,
                  action: typing.Union[str, int] = 'SELECT'):
    ''' Randomly select vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param ratio: Ratio, Portion of items to select randomly
    :type ratio: float
    :param seed: Random Seed, Seed for the random number generator
    :type seed: int
    :param action: Action, Selection action to execute * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_similar(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   type: typing.Union[str, int] = 'NORMAL',
                   compare: typing.Union[str, int] = 'EQUAL',
                   threshold: float = 0.0):
    ''' Select similar vertices, edges or faces by property types

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    :param compare: Compare
    :type compare: typing.Union[str, int]
    :param threshold: Threshold
    :type threshold: float
    '''

    pass


def select_similar_region(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Select similar face regions to the current selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_ungrouped(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     extend: bool = False):
    ''' Select vertices without a group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend the selection
    :type extend: bool
    '''

    pass


def separate(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             type: typing.Union[str, int] = 'SELECTED'):
    ''' Separate selected geometry into a new mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def set_normals_from_faces(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None,
                           *,
                           keep_sharp: bool = False):
    ''' Set the custom normals from the selected faces ones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param keep_sharp: Keep Sharp Edges, Do not set sharp edges to face
    :type keep_sharp: bool
    '''

    pass


def shape_propagate_to_all(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None):
    ''' Apply selected vertex locations to all other shape keys

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def shortest_path_pick(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       edge_mode: typing.Union[str, int] = 'SELECT',
                       use_face_step: bool = False,
                       use_topology_distance: bool = False,
                       use_fill: bool = False,
                       skip: int = 0,
                       nth: int = 1,
                       offset: int = 0,
                       index: int = -1):
    ''' Select shortest path between two selections

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path
    :type edge_mode: typing.Union[str, int]
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :type use_face_step: bool
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :type use_topology_distance: bool
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :type use_fill: bool
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: int
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: int
    :param offset: Offset, Offset from the starting point
    :type offset: int
    :type index: int
    '''

    pass


def shortest_path_select(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         edge_mode: typing.Union[str, int] = 'SELECT',
                         use_face_step: bool = False,
                         use_topology_distance: bool = False,
                         use_fill: bool = False,
                         skip: int = 0,
                         nth: int = 1,
                         offset: int = 0):
    ''' Selected shortest path between two vertices/edges/faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path
    :type edge_mode: typing.Union[str, int]
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :type use_face_step: bool
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :type use_topology_distance: bool
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :type use_fill: bool
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: int
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: int
    :param offset: Offset, Offset from the starting point
    :type offset: int
    '''

    pass


def smooth_normals(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   factor: float = 0.5):
    ''' Smooth custom normals based on adjacent vertex normals

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param factor: Factor, Specifies weight of smooth vs original normal
    :type factor: float
    '''

    pass


def solidify(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             thickness: float = 0.01):
    ''' Create a solid skin by extruding, compensating for sharp angles

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param thickness: Thickness
    :type thickness: float
    '''

    pass


def sort_elements(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        type: typing.Union[str, int] = 'VIEW_ZAXIS',
        elements: typing.Union[typing.Set[str], typing.Set[int]] = {'VERT'},
        reverse: bool = False,
        seed: int = 0):
    ''' The order of selected vertices/edges/faces is modified, based on a given method

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Type of reordering operation to apply * VIEW_ZAXIS View Z Axis -- Sort selected elements from farthest to nearest one in current view. * VIEW_XAXIS View X Axis -- Sort selected elements from left to right one in current view. * CURSOR_DISTANCE Cursor Distance -- Sort selected elements from nearest to farthest from 3D cursor. * MATERIAL Material -- Sort selected faces from smallest to greatest material index. * SELECTED Selected -- Move all selected elements in first places, preserving their relative order. Warning: This will affect unselected elements' indices as well. * RANDOMIZE Randomize -- Randomize order of selected elements. * REVERSE Reverse -- Reverse current order of selected elements.
    :type type: typing.Union[str, int]
    :param elements: Elements, Which elements to affect (vertices, edges and/or faces)
    :type elements: typing.Union[typing.Set[str], typing.Set[int]]
    :param reverse: Reverse, Reverse the sorting effect
    :type reverse: bool
    :param seed: Seed, Seed for random-based operations
    :type seed: int
    '''

    pass


def spin(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         steps: int = 12,
         dupli: bool = False,
         angle: float = 1.5708,
         use_auto_merge: bool = True,
         use_normal_flip: bool = False,
         center: typing.
         Union[typing.List[float], typing.
               Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                  0.0),
         axis: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Extrude selected vertices in a circle around the cursor in indicated viewport

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param steps: Steps, Steps
    :type steps: int
    :param dupli: Use Duplicates
    :type dupli: bool
    :param angle: Angle, Rotation for each step
    :type angle: float
    :param use_auto_merge: Auto Merge, Merge first/last when the angle is a full revolution
    :type use_auto_merge: bool
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: bool
    :param center: Center, Center in global view space
    :type center: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param axis: Axis, Axis in global view space
    :type axis: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def split(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None):
    ''' Split off selected geometry from connected unselected geometry

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def split_normals(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Split custom normals of selected vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def subdivide(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              number_cuts: int = 1,
              smoothness: float = 0.0,
              ngon: bool = True,
              quadcorner: typing.Union[str, int] = 'STRAIGHT_CUT',
              fractal: float = 0.0,
              fractal_along_normal: float = 0.0,
              seed: int = 0):
    ''' Subdivide selected edges

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param number_cuts: Number of Cuts
    :type number_cuts: int
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: float
    :param ngon: Create N-Gons, When disabled, newly created faces are limited to 3 and 4 sided faces
    :type ngon: bool
    :param quadcorner: Quad Corner Type, How to subdivide quad corners (anything other than Straight Cut will prevent n-gons)
    :type quadcorner: typing.Union[str, int]
    :param fractal: Fractal, Fractal randomness factor
    :type fractal: float
    :param fractal_along_normal: Along Normal, Apply fractal displacement along normal only
    :type fractal_along_normal: float
    :param seed: Random Seed, Seed for the random number generator
    :type seed: int
    '''

    pass


def subdivide_edgering(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       number_cuts: int = 10,
                       interpolation: typing.Union[str, int] = 'PATH',
                       smoothness: float = 1.0,
                       profile_shape_factor: float = 0.0,
                       profile_shape: typing.Union[int, str] = 'SMOOTH'):
    ''' Subdivide perpendicular edges to the selected edge-ring

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param number_cuts: Number of Cuts
    :type number_cuts: int
    :param interpolation: Interpolation, Interpolation method
    :type interpolation: typing.Union[str, int]
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: float
    :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded
    :type profile_shape_factor: float
    :param profile_shape: Profile Shape, Shape of the profile
    :type profile_shape: typing.Union[int, str]
    '''

    pass


def symmetrize(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               direction: typing.Union[int, str] = 'NEGATIVE_X',
               threshold: float = 0.0001):
    ''' Enforce symmetry (both form and topological) across an axis

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param direction: Direction, Which sides to copy from and to
    :type direction: typing.Union[int, str]
    :param threshold: Threshold, Limit for snap middle vertices to the axis center
    :type threshold: float
    '''

    pass


def symmetry_snap(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  direction: typing.Union[int, str] = 'NEGATIVE_X',
                  threshold: float = 0.05,
                  factor: float = 0.5,
                  use_center: bool = True):
    ''' Snap vertex pairs to their mirrored locations

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param direction: Direction, Which sides to copy from and to
    :type direction: typing.Union[int, str]
    :param threshold: Threshold, Distance within which matching vertices are searched
    :type threshold: float
    :param factor: Factor, Mix factor of the locations of the vertices
    :type factor: float
    :param use_center: Center, Snap middle vertices to the axis center
    :type use_center: bool
    '''

    pass


def tris_convert_to_quads(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          face_threshold: float = 0.698132,
                          shape_threshold: float = 0.698132,
                          uvs: bool = False,
                          vcols: bool = False,
                          seam: bool = False,
                          sharp: bool = False,
                          materials: bool = False):
    ''' Join triangles into quads

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param face_threshold: Max Face Angle, Face angle limit
    :type face_threshold: float
    :param shape_threshold: Max Shape Angle, Shape angle limit
    :type shape_threshold: float
    :param uvs: Compare UVs
    :type uvs: bool
    :param vcols: Compare VCols
    :type vcols: bool
    :param seam: Compare Seam
    :type seam: bool
    :param sharp: Compare Sharp
    :type sharp: bool
    :param materials: Compare Materials
    :type materials: bool
    '''

    pass


def unsubdivide(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                iterations: int = 2):
    ''' Un-subdivide selected edges and faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param iterations: Iterations, Number of times to un-subdivide
    :type iterations: int
    '''

    pass


def uv_texture_add(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Add UV map

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def uv_texture_remove(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Remove UV map

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def uvs_reverse(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Flip direction of UV coordinates inside faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def uvs_rotate(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               use_ccw: bool = False):
    ''' Rotate UV coordinates inside faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_ccw: Counter Clockwise
    :type use_ccw: bool
    '''

    pass


def vert_connect(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Connect selected vertices of faces, splitting the face

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vert_connect_concave(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None):
    ''' Make all faces convex

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vert_connect_nonplanar(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None,
                           *,
                           angle_limit: float = 0.0872665):
    ''' Split non-planar faces that exceed the angle threshold

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param angle_limit: Max Angle, Angle limit
    :type angle_limit: float
    '''

    pass


def vert_connect_path(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Connect vertices by their selection order, creating edges, splitting faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_color_add(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Add vertex color layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_color_remove(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Remove vertex color layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertices_smooth(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    factor: float = 0.0,
                    repeat: int = 1,
                    xaxis: bool = True,
                    yaxis: bool = True,
                    zaxis: bool = True,
                    wait_for_input: bool = True):
    ''' Flatten angles of selected vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param factor: Smoothing, Smoothing factor
    :type factor: float
    :param repeat: Repeat, Number of times to smooth the mesh
    :type repeat: int
    :param xaxis: X-Axis, Smooth along the X axis
    :type xaxis: bool
    :param yaxis: Y-Axis, Smooth along the Y axis
    :type yaxis: bool
    :param zaxis: Z-Axis, Smooth along the Z axis
    :type zaxis: bool
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def vertices_smooth_laplacian(override_context: typing.
                              Union[typing.Dict, 'bpy.types.Context'] = None,
                              execution_context: typing.Union[str, int] = None,
                              undo: bool = None,
                              *,
                              repeat: int = 1,
                              lambda_factor: float = 1.0,
                              lambda_border: float = 5e-05,
                              use_x: bool = True,
                              use_y: bool = True,
                              use_z: bool = True,
                              preserve_volume: bool = True):
    ''' Laplacian smooth of selected vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param repeat: Number of iterations to smooth the mesh
    :type repeat: int
    :param lambda_factor: Lambda factor
    :type lambda_factor: float
    :param lambda_border: Lambda factor in border
    :type lambda_border: float
    :param use_x: Smooth X Axis, Smooth object along X axis
    :type use_x: bool
    :param use_y: Smooth Y Axis, Smooth object along Y axis
    :type use_y: bool
    :param use_z: Smooth Z Axis, Smooth object along Z axis
    :type use_z: bool
    :param preserve_volume: Preserve Volume, Apply volume preservation after smooth
    :type preserve_volume: bool
    '''

    pass


def wireframe(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              use_boundary: bool = True,
              use_even_offset: bool = True,
              use_relative_offset: bool = False,
              use_replace: bool = True,
              thickness: float = 0.01,
              offset: float = 0.01,
              use_crease: bool = False,
              crease_weight: float = 0.01):
    ''' Create a solid wireframe from faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_boundary: Boundary, Inset face boundaries
    :type use_boundary: bool
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :type use_even_offset: bool
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
    :type use_relative_offset: bool
    :param use_replace: Replace, Remove original faces
    :type use_replace: bool
    :param thickness: Thickness
    :type thickness: float
    :param offset: Offset
    :type offset: float
    :param use_crease: Crease, Crease hub edges for an improved subdivision surface
    :type use_crease: bool
    :param crease_weight: Crease Weight
    :type crease_weight: float
    '''

    pass
