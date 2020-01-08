import sys
import typing


def average_normals(average_type: int = 'CUSTOM_NORMAL',
                    weight: int = 50,
                    threshold: float = 0.01):
    '''Average custom normals of selected vertices 

    :param average_type: Type, Averaging methodCUSTOM_NORMAL Custom Normal, Take Average of vert Normals.FACE_AREA Face Area, Set all vert normals by Face Area.CORNER_ANGLE Corner Angle, Set all vert normals by Corner Angle. 
    :type average_type: int
    :param weight: Weight, Weight applied per face 
    :type weight: int
    :param threshold: Threshold, Threshold value for different weights to be considered equal 
    :type threshold: float
    '''

    pass


def beautify_fill(angle_limit: float = 3.14159):
    '''Rearrange some faces to try to get less degenerated geometry 

    :param angle_limit: Max Angle, Angle limit 
    :type angle_limit: float
    '''

    pass


def bevel(offset_type: int = 'OFFSET',
          offset: float = 0.0,
          offset_pct: float = 0.0,
          segments: int = 1,
          profile: float = 0.5,
          vertex_only: bool = False,
          clamp_overlap: bool = False,
          loop_slide: bool = True,
          mark_seam: bool = False,
          mark_sharp: bool = False,
          material: int = -1,
          harden_normals: bool = False,
          face_strength_mode: int = 'NONE',
          miter_outer: int = 'SHARP',
          miter_inner: int = 'SHARP',
          spread: float = 0.1,
          release_confirm: bool = False):
    '''Cut into selected items at an angle to create flat or rounded bevel or chamfer 

    :param offset_type: Width Type, What distance Width measuresOFFSET Offset, Amount is offset of new edges from original.WIDTH Width, Amount is width of new face.DEPTH Depth, Amount is perpendicular distance from original edge to bevel face.PERCENT Percent, Amount is percent of adjacent edge length. 
    :type offset_type: int
    :param offset: Width, Bevel amount 
    :type offset: float
    :param offset_pct: Width Percent, Bevel amount for percentage method 
    :type offset_pct: float
    :param segments: Segments, Segments for curved edge 
    :type segments: int
    :param profile: Profile, Controls profile shape (0.5 = round) 
    :type profile: float
    :param vertex_only: Vertex Only, Bevel only vertices 
    :type vertex_only: bool
    :param clamp_overlap: Clamp Overlap, Do not allow beveled edges/vertices to overlap each other 
    :type clamp_overlap: bool
    :param loop_slide: Loop Slide, Prefer slide along edge to even widths 
    :type loop_slide: bool
    :param mark_seam: Mark Seams, Mark Seams along beveled edges 
    :type mark_seam: bool
    :param mark_sharp: Mark Sharp, Mark beveled edges as sharp 
    :type mark_sharp: bool
    :param material: Material, Material for bevel faces (-1 means use adjacent faces) 
    :type material: int
    :param harden_normals: Harden Normals, Match normals of new faces to adjacent faces 
    :type harden_normals: bool
    :param face_strength_mode: Face Strength Mode, Whether to set face strength, and which faces to set face strength onNONE None, Do not set face strength.NEW New, Set face strength on new faces only.AFFECTED Affected, Set face strength on new and modified faces only.ALL All, Set face strength on all faces. 
    :type face_strength_mode: int
    :param miter_outer: Outer Miter, Pattern to use for outside of mitersSHARP Sharp, Outside of miter is sharp.PATCH Patch, Outside of miter is squared-off patch.ARC Arc, Outside of miter is arc. 
    :type miter_outer: int
    :param miter_inner: Inner Miter, Pattern to use for inside of mitersSHARP Sharp, Inside of miter is sharp.ARC Arc, Inside of miter is arc. 
    :type miter_inner: int
    :param spread: Spread, Amount to spread arcs for arc inner miters 
    :type spread: float
    :param release_confirm: Confirm on Release 
    :type release_confirm: bool
    '''

    pass


def bisect(plane_co: float = (0.0, 0.0, 0.0),
           plane_no: float = (0.0, 0.0, 0.0),
           use_fill: bool = False,
           clear_inner: bool = False,
           clear_outer: bool = False,
           threshold: float = 0.0001,
           xstart: int = 0,
           xend: int = 0,
           ystart: int = 0,
           yend: int = 0,
           cursor: int = 1002):
    '''Cut geometry along a plane (click-drag to define plane) 

    :param plane_co: Plane Point, A point on the plane 
    :type plane_co: float
    :param plane_no: Plane Normal, The direction the plane points 
    :type plane_no: float
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
    :param cursor: Cursor, Mouse cursor style to use during the modal operator 
    :type cursor: int
    '''

    pass


def blend_from_shape(shape: int = '', blend: float = 1.0, add: bool = True):
    '''Blend in shape from a shape key 

    :param shape: Shape, Shape key to use for blending 
    :type shape: int
    :param blend: Blend, Blending factor 
    :type blend: float
    :param add: Add, Add rather than blend between shapes 
    :type add: bool
    '''

    pass


def bridge_edge_loops(type: int = 'SINGLE',
                      use_merge: bool = False,
                      merge_factor: float = 0.5,
                      twist_offset: int = 0,
                      number_cuts: int = 0,
                      interpolation: int = 'PATH',
                      smoothness: float = 1.0,
                      profile_shape_factor: float = 0.0,
                      profile_shape: int = 'SMOOTH'):
    '''Create a bridge of faces between two or more selected edge loops 

    :param type: Connect Loops, Method of bridging multiple loops 
    :type type: int
    :param use_merge: Merge, Merge rather than creating faces 
    :type use_merge: bool
    :param merge_factor: Merge Factor 
    :type merge_factor: float
    :param twist_offset: Twist, Twist offset for closed loops 
    :type twist_offset: int
    :param number_cuts: Number of Cuts 
    :type number_cuts: int
    :param interpolation: Interpolation, Interpolation method 
    :type interpolation: int
    :param smoothness: Smoothness, Smoothness factor 
    :type smoothness: float
    :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded 
    :type profile_shape_factor: float
    :param profile_shape: Profile Shape, Shape of the profileSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff. 
    :type profile_shape: int
    '''

    pass


def colors_reverse():
    '''Flip direction of vertex colors inside faces 

    '''

    pass


def colors_rotate(use_ccw: bool = False):
    '''Rotate vertex colors inside faces 

    :param use_ccw: Counter Clockwise 
    :type use_ccw: bool
    '''

    pass


def convex_hull(delete_unused: bool = True,
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
    '''Enclose selected vertices in a convex polyhedron 

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


def customdata_custom_splitnormals_add():
    '''Add a custom split normals layer, if none exists yet 

    '''

    pass


def customdata_custom_splitnormals_clear():
    '''Remove the custom split normals layer, if it exists 

    '''

    pass


def customdata_mask_clear():
    '''Clear vertex sculpt masking data from the mesh 

    '''

    pass


def customdata_skin_add():
    '''Add a vertex skin layer 

    '''

    pass


def customdata_skin_clear():
    '''Clear vertex skin layer 

    '''

    pass


def decimate(ratio: float = 1.0,
             use_vertex_group: bool = False,
             vertex_group_factor: float = 1.0,
             invert_vertex_group: bool = False,
             use_symmetry: bool = False,
             symmetry_axis: int = 'Y'):
    '''Simplify geometry by collapsing edges 

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
    :type symmetry_axis: int
    '''

    pass


def delete(type: str = 'VERT'):
    '''Delete selected vertices, edges or faces 

    :param type: Type, Method used for deleting mesh data 
    :type type: str
    '''

    pass


def delete_edgeloop(use_face_split: bool = True):
    '''Delete an edge loop by merging the faces on each side 

    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry 
    :type use_face_split: bool
    '''

    pass


def delete_loose(use_verts: bool = True,
                 use_edges: bool = True,
                 use_faces: bool = False):
    '''Delete loose vertices, edges or faces 

    :param use_verts: Vertices, Remove loose vertices 
    :type use_verts: bool
    :param use_edges: Edges, Remove loose edges 
    :type use_edges: bool
    :param use_faces: Faces, Remove loose faces 
    :type use_faces: bool
    '''

    pass


def dissolve_degenerate(threshold: float = 0.0001):
    '''Dissolve zero area faces and zero length edges 

    :param threshold: Merge Distance, Minimum distance between elements to merge 
    :type threshold: float
    '''

    pass


def dissolve_edges(use_verts: bool = True, use_face_split: bool = False):
    '''Dissolve edges, merging faces 

    :param use_verts: Dissolve Verts, Dissolve remaining vertices 
    :type use_verts: bool
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry 
    :type use_face_split: bool
    '''

    pass


def dissolve_faces(use_verts: bool = False):
    '''Dissolve faces 

    :param use_verts: Dissolve Verts, Dissolve remaining vertices 
    :type use_verts: bool
    '''

    pass


def dissolve_limited(angle_limit: float = 0.0872665,
                     use_dissolve_boundaries: bool = False,
                     delimit: typing.Set[int] = {'NORMAL'}):
    '''Dissolve selected edges and verts, limited by the angle of surrounding geometry 

    :param angle_limit: Max Angle, Angle limit 
    :type angle_limit: float
    :param use_dissolve_boundaries: All Boundaries, Dissolve all vertices inbetween face boundaries 
    :type use_dissolve_boundaries: bool
    :param delimit: Delimit, Delimit dissolve operationNORMAL Regular, Delimit by face directions.MATERIAL Material, Delimit by face material.SEAM Seam, Delimit by edge seams.SHARP Sharp, Delimit by sharp edges.UV UVs, Delimit by UV coordinates. 
    :type delimit: typing.Set[int]
    '''

    pass


def dissolve_mode(use_verts: bool = False,
                  use_face_split: bool = False,
                  use_boundary_tear: bool = False):
    '''Dissolve geometry based on the selection mode 

    :param use_verts: Dissolve Verts, Dissolve remaining vertices 
    :type use_verts: bool
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry 
    :type use_face_split: bool
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces 
    :type use_boundary_tear: bool
    '''

    pass


def dissolve_verts(use_face_split: bool = False,
                   use_boundary_tear: bool = False):
    '''Dissolve verts, merge edges and faces 

    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry 
    :type use_face_split: bool
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces 
    :type use_boundary_tear: bool
    '''

    pass


def dupli_extrude_cursor(rotate_source: bool = True):
    '''Duplicate and extrude selected vertices, edges or faces towards the mouse cursor 

    :param rotate_source: Rotate Source, Rotate initial selection giving better shape 
    :type rotate_source: bool
    '''

    pass


def duplicate(mode: int = 1):
    '''Duplicate selected vertices, edges or faces 

    :param mode: Mode 
    :type mode: int
    '''

    pass


def duplicate_move(MESH_OT_duplicate=None, TRANSFORM_OT_translate=None):
    '''Duplicate mesh and move 

    :param MESH_OT_duplicate: Duplicate, Duplicate selected vertices, edges or faces 
    :param TRANSFORM_OT_translate: Move, Move selected items 
    '''

    pass


def edge_collapse():
    '''Collapse selected edges 

    '''

    pass


def edge_face_add():
    '''Add an edge or face to selected 

    '''

    pass


def edge_rotate(use_ccw: bool = False):
    '''Rotate selected edge or adjoining faces 

    :param use_ccw: Counter Clockwise 
    :type use_ccw: bool
    '''

    pass


def edge_split():
    '''Split selected edges so that each neighbor face gets its own copy 

    '''

    pass


def edgering_select(extend: bool = False,
                    deselect: bool = False,
                    toggle: bool = False,
                    ring: bool = True):
    '''Select an edge ring 

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


def edges_select_sharp(sharpness: float = 0.523599):
    '''Select all sharp-enough edges 

    :param sharpness: Sharpness 
    :type sharpness: float
    '''

    pass


def extrude_context(use_normal_flip: bool = False, mirror: bool = False):
    '''Extrude selection 

    :param use_normal_flip: Flip Normals 
    :type use_normal_flip: bool
    :param mirror: Mirror Editing 
    :type mirror: bool
    '''

    pass


def extrude_context_move(MESH_OT_extrude_context=None,
                         TRANSFORM_OT_translate=None):
    '''Extrude region together along the average normal 

    :param MESH_OT_extrude_context: Extrude Context, Extrude selection 
    :param TRANSFORM_OT_translate: Move, Move selected items 
    '''

    pass


def extrude_edges_indiv(use_normal_flip: bool = False, mirror: bool = False):
    '''Extrude individual edges only 

    :param use_normal_flip: Flip Normals 
    :type use_normal_flip: bool
    :param mirror: Mirror Editing 
    :type mirror: bool
    '''

    pass


def extrude_edges_move(MESH_OT_extrude_edges_indiv=None,
                       TRANSFORM_OT_translate=None):
    '''Extrude edges and move result 

    :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only 
    :param TRANSFORM_OT_translate: Move, Move selected items 
    '''

    pass


def extrude_faces_indiv(mirror: bool = False):
    '''Extrude individual faces only 

    :param mirror: Mirror Editing 
    :type mirror: bool
    '''

    pass


def extrude_faces_move(MESH_OT_extrude_faces_indiv=None,
                       TRANSFORM_OT_shrink_fatten=None):
    '''Extrude each individual face separately along local normals 

    :param MESH_OT_extrude_faces_indiv: Extrude Individual Faces, Extrude individual faces only 
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals 
    '''

    pass


def extrude_region(use_normal_flip: bool = False, mirror: bool = False):
    '''Extrude region of faces 

    :param use_normal_flip: Flip Normals 
    :type use_normal_flip: bool
    :param mirror: Mirror Editing 
    :type mirror: bool
    '''

    pass


def extrude_region_move(MESH_OT_extrude_region=None,
                        TRANSFORM_OT_translate=None):
    '''Extrude region and move result 

    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces 
    :param TRANSFORM_OT_translate: Move, Move selected items 
    '''

    pass


def extrude_region_shrink_fatten(MESH_OT_extrude_region=None,
                                 TRANSFORM_OT_shrink_fatten=None):
    '''Extrude region together along local normals 

    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces 
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals 
    '''

    pass


def extrude_repeat(offset: float = 2.0, steps: int = 10):
    '''Extrude selected vertices, edges or faces repeatedly 

    :param offset: Offset 
    :type offset: float
    :param steps: Steps 
    :type steps: int
    '''

    pass


def extrude_vertices_move(MESH_OT_extrude_verts_indiv=None,
                          TRANSFORM_OT_translate=None):
    '''Extrude vertices and move result 

    :param MESH_OT_extrude_verts_indiv: Extrude Only Vertices, Extrude individual vertices only 
    :param TRANSFORM_OT_translate: Move, Move selected items 
    '''

    pass


def extrude_verts_indiv(mirror: bool = False):
    '''Extrude individual vertices only 

    :param mirror: Mirror Editing 
    :type mirror: bool
    '''

    pass


def face_make_planar(factor: float = 1.0, repeat: int = 1):
    '''Flatten selected faces 

    :param factor: Factor 
    :type factor: float
    :param repeat: Iterations 
    :type repeat: int
    '''

    pass


def face_split_by_edges():
    '''Weld loose edges into faces (splitting them into new faces) 

    '''

    pass


def faces_mirror_uv(direction: int = 'POSITIVE', precision: int = 3):
    '''Copy mirror UV coordinates on the X axis based on a mirrored mesh 

    :param direction: Axis Direction 
    :type direction: int
    :param precision: Precision, Tolerance for finding vertex duplicates 
    :type precision: int
    '''

    pass


def faces_select_linked_flat(sharpness: float = 0.0174533):
    '''Select linked faces by angle 

    :param sharpness: Sharpness 
    :type sharpness: float
    '''

    pass


def faces_shade_flat():
    '''Display faces flat 

    '''

    pass


def faces_shade_smooth():
    '''Display faces smooth (using vertex normals) 

    '''

    pass


def fill(use_beauty: bool = True):
    '''Fill a selected edge loop with faces 

    :param use_beauty: Beauty, Use best triangulation division 
    :type use_beauty: bool
    '''

    pass


def fill_grid(span: int = 1, offset: int = 0, use_interp_simple: bool = False):
    '''Fill grid from two loops 

    :param span: Span, Number of grid columns 
    :type span: int
    :param offset: Offset, Vertex that is the corner of the grid 
    :type offset: int
    :param use_interp_simple: Simple Blending, Use simple interpolation of grid vertices 
    :type use_interp_simple: bool
    '''

    pass


def fill_holes(sides: int = 4):
    '''Fill in holes (boundary edge loops) 

    :param sides: Sides, Number of sides in hole required to fill (zero fills all holes) 
    :type sides: int
    '''

    pass


def flip_normals():
    '''Flip the direction of selected faces’ normals (and of their vertices) 

    '''

    pass


def hide(unselected: bool = False):
    '''Hide (un)selected vertices, edges or faces 

    :param unselected: Unselected, Hide unselected rather than selected 
    :type unselected: bool
    '''

    pass


def inset(use_boundary: bool = True,
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
    '''Inset new faces into selected faces 

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
    :param use_individual: Individual, Individual Face Inset 
    :type use_individual: bool
    :param use_interpolate: Interpolate, Blend face data across the inset 
    :type use_interpolate: bool
    :param release_confirm: Confirm on Release 
    :type release_confirm: bool
    '''

    pass


def intersect(mode: int = 'SELECT_UNSELECT',
              separate_mode: int = 'CUT',
              threshold: float = 1e-06):
    '''Cut an intersection into faces 

    :param mode: SourceSELECT Self Intersect, Self intersect selected faces.SELECT_UNSELECT Selected/Unselected, Intersect selected with unselected faces. 
    :type mode: int
    :param separate_mode: Separate ModeALL All, Separate all geometry from intersections.CUT Cut, Cut into geometry keeping each side separate (Selected/Unselected only).NONE Merge, Merge all geometry from the intersection. 
    :type separate_mode: int
    :param threshold: Merge threshold 
    :type threshold: float
    '''

    pass


def intersect_boolean(operation: int = 'DIFFERENCE',
                      use_swap: bool = False,
                      threshold: float = 1e-06):
    '''Cut solid geometry from selected to unselected 

    :param operation: Boolean 
    :type operation: int
    :param use_swap: Swap, Use with difference intersection to swap which side is kept 
    :type use_swap: bool
    :param threshold: Merge threshold 
    :type threshold: float
    '''

    pass


def knife_project(cut_through: bool = False):
    '''Use other objects outlines & boundaries to project knife cuts 

    :param cut_through: Cut through, Cut through all faces, not just visible ones 
    :type cut_through: bool
    '''

    pass


def knife_tool(use_occlude_geometry: bool = True,
               only_selected: bool = False,
               wait_for_input: bool = True):
    '''Cut new topology 

    :param use_occlude_geometry: Occlude Geometry, Only cut the front most geometry 
    :type use_occlude_geometry: bool
    :param only_selected: Only Selected, Only cut selected geometry 
    :type only_selected: bool
    :param wait_for_input: Wait for Input 
    :type wait_for_input: bool
    '''

    pass


def loop_multi_select(ring: bool = False):
    '''Select a loop of connected edges by connection type 

    :param ring: Ring 
    :type ring: bool
    '''

    pass


def loop_select(extend: bool = False,
                deselect: bool = False,
                toggle: bool = False,
                ring: bool = False):
    '''Select a loop of connected edges 

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


def loop_to_region(select_bigger: bool = False):
    '''Select region of faces inside of a selected loop of edges 

    :param select_bigger: Select Bigger, Select bigger regions instead of smaller ones 
    :type select_bigger: bool
    '''

    pass


def loopcut(number_cuts: int = 1,
            smoothness: float = 0.0,
            falloff: int = 'INVERSE_SQUARE',
            object_index: int = -1,
            edge_index: int = -1,
            mesh_select_mode_init=(False, False, False)):
    '''Add a new loop between existing loops 

    :param number_cuts: Number of Cuts 
    :type number_cuts: int
    :param smoothness: Smoothness, Smoothness factor 
    :type smoothness: float
    :param falloff: Falloff, Falloff type the featherSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff. 
    :type falloff: int
    :param object_index: Object Index 
    :type object_index: int
    :param edge_index: Edge Index 
    :type edge_index: int
    '''

    pass


def loopcut_slide(MESH_OT_loopcut=None, TRANSFORM_OT_edge_slide=None):
    '''Cut mesh loop and slide it 

    :param MESH_OT_loopcut: Loop Cut, Add a new loop between existing loops 
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh 
    '''

    pass


def mark_freestyle_edge(clear: bool = False):
    '''(Un)mark selected edges as Freestyle feature edges 

    :param clear: Clear 
    :type clear: bool
    '''

    pass


def mark_freestyle_face(clear: bool = False):
    '''(Un)mark selected faces for exclusion from Freestyle feature edge detection 

    :param clear: Clear 
    :type clear: bool
    '''

    pass


def mark_seam(clear: bool = False):
    '''(Un)mark selected edges as a seam 

    :param clear: Clear 
    :type clear: bool
    '''

    pass


def mark_sharp(clear: bool = False, use_verts: bool = False):
    '''(Un)mark selected edges as sharp 

    :param clear: Clear 
    :type clear: bool
    :param use_verts: Vertices, Consider vertices instead of edges to select which edges to (un)tag as sharp 
    :type use_verts: bool
    '''

    pass


def merge(type: int = 'CENTER', uvs: bool = False):
    '''Merge selected vertices 

    :param type: Type, Merge method to use 
    :type type: int
    :param uvs: UVs, Move UVs according to merge 
    :type uvs: bool
    '''

    pass


def merge_normals():
    '''Merge custom normals of selected vertices 

    '''

    pass


def mod_weighted_strength(set: bool = False, face_strength: int = 'MEDIUM'):
    '''Set/Get strength of face (used in Weighted Normal modifier) 

    :param set: Set value, Set Value of faces 
    :type set: bool
    :param face_strength: Face Strength, Strength to use for assigning or selecting face influence for weighted normal modifier 
    :type face_strength: int
    '''

    pass


def normals_make_consistent(inside: bool = False):
    '''Make face and vertex normals point either outside or inside the mesh 

    :param inside: Inside 
    :type inside: bool
    '''

    pass


def normals_tools(mode: int = 'COPY', absolute: bool = False):
    '''Custom normals tools using Normal Vector of UI 

    :param mode: Mode, Mode of tools taking input from InterfaceCOPY Copy Normal, Copy normal to buffer.PASTE Paste Normal, Paste normal from buffer.ADD Add Normal, Add normal vector with selection.MULTIPLY Multiply Normal, Multiply normal vector with selection.RESET Reset Normal, Reset buffer and/or normal of selected element. 
    :type mode: int
    :param absolute: Absolute Coordinates, Copy Absolute coordinates or Normal vector 
    :type absolute: bool
    '''

    pass


def offset_edge_loops(use_cap_endpoint: bool = False):
    '''Create offset edge loop from the current selection 

    :param use_cap_endpoint: Cap Endpoint, Extend loop around end-points 
    :type use_cap_endpoint: bool
    '''

    pass


def offset_edge_loops_slide(MESH_OT_offset_edge_loops=None,
                            TRANSFORM_OT_edge_slide=None):
    '''Offset edge loop slide 

    :param MESH_OT_offset_edge_loops: Offset Edge Loop, Create offset edge loop from the current selection 
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh 
    '''

    pass


def point_normals(mode: int = 'COORDINATES',
                  invert: bool = False,
                  align: bool = False,
                  target_location: float = (0.0, 0.0, 0.0),
                  spherize: bool = False,
                  spherize_strength: float = 0.1):
    '''Point selected custom normals to specified Target 

    :param mode: Mode, How to define coordinates to point custom normals toCOORDINATES Coordinates, Use static coordinates (defined by various means).MOUSE Mouse, Follow mouse cursor. 
    :type mode: int
    :param invert: Invert, Invert affected normals 
    :type invert: bool
    :param align: Align, Make all affected normals parallel 
    :type align: bool
    :param target_location: Target, Target location to which normals will point 
    :type target_location: float
    :param spherize: Spherize, Interpolate between original and new normals 
    :type spherize: bool
    :param spherize_strength: Spherize Strength, Ratio of spherized normal to original normal 
    :type spherize_strength: float
    '''

    pass


def poke(offset: float = 0.0,
         use_relative_offset: bool = False,
         center_mode: int = 'MEDIAN_WEIGHTED'):
    '''Split a face into a fan 

    :param offset: Poke Offset, Poke Offset 
    :type offset: float
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry 
    :type use_relative_offset: bool
    :param center_mode: Poke Center, Poke Face Center CalculationMEDIAN_WEIGHTED Weighted Median, Weighted median face center.MEDIAN Median, Median face center.BOUNDS Bounds, Face bounds center. 
    :type center_mode: int
    '''

    pass


def polybuild_dissolve_at_cursor():
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    '''

    pass


def polybuild_face_at_cursor(mirror: bool = False,
                             use_proportional_edit: bool = False,
                             proportional_edit_falloff: int = 'SMOOTH',
                             proportional_size: float = 1.0,
                             use_proportional_connected: bool = False,
                             use_proportional_projected: bool = False,
                             release_confirm: bool = False,
                             use_accurate: bool = False):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param mirror: Mirror Editing 
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing 
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: int
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


def polybuild_face_at_cursor_move(MESH_OT_polybuild_face_at_cursor=None,
                                  TRANSFORM_OT_translate=None):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param MESH_OT_polybuild_face_at_cursor: Poly Build Face at Cursor 
    :param TRANSFORM_OT_translate: Move, Move selected items 
    '''

    pass


def polybuild_split_at_cursor(mirror: bool = False,
                              use_proportional_edit: bool = False,
                              proportional_edit_falloff: int = 'SMOOTH',
                              proportional_size: float = 1.0,
                              use_proportional_connected: bool = False,
                              use_proportional_projected: bool = False,
                              release_confirm: bool = False,
                              use_accurate: bool = False):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param mirror: Mirror Editing 
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing 
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: int
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


def polybuild_split_at_cursor_move(MESH_OT_polybuild_split_at_cursor=None,
                                   TRANSFORM_OT_translate=None):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param MESH_OT_polybuild_split_at_cursor: Poly Build Split at Cursor 
    :param TRANSFORM_OT_translate: Move, Move selected items 
    '''

    pass


def primitive_circle_add(vertices: int = 32,
                         radius: float = 1.0,
                         fill_type: int = 'NOTHING',
                         calc_uvs: bool = True,
                         enter_editmode: bool = False,
                         align: int = 'WORLD',
                         location: float = (0.0, 0.0, 0.0),
                         rotation: float = (0.0, 0.0, 0.0)):
    '''Construct a circle mesh 

    :param vertices: Vertices 
    :type vertices: int
    :param radius: Radius 
    :type radius: float
    :param fill_type: Fill TypeNOTHING Nothing, Don’t fill at all.NGON Ngon, Use ngons.TRIFAN Triangle Fan, Use triangle fans. 
    :type fill_type: int
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: bool
    :param align: Align, The alignment of the new objectWORLD World, Align the new object to the world.VIEW View, Align the new object to the view.CURSOR 3D Cursor, Use the 3D cursor orientation for the new object. 
    :type align: int
    :param location: Location, Location for the newly added object 
    :type location: float
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float
    '''

    pass


def primitive_cone_add(vertices: int = 32,
                       radius1: float = 1.0,
                       radius2: float = 0.0,
                       depth: float = 2.0,
                       end_fill_type: int = 'NGON',
                       calc_uvs: bool = True,
                       enter_editmode: bool = False,
                       align: int = 'WORLD',
                       location: float = (0.0, 0.0, 0.0),
                       rotation: float = (0.0, 0.0, 0.0)):
    '''Construct a conic mesh 

    :param vertices: Vertices 
    :type vertices: int
    :param radius1: Radius 1 
    :type radius1: float
    :param radius2: Radius 2 
    :type radius2: float
    :param depth: Depth 
    :type depth: float
    :param end_fill_type: Base Fill TypeNOTHING Nothing, Don’t fill at all.NGON Ngon, Use ngons.TRIFAN Triangle Fan, Use triangle fans. 
    :type end_fill_type: int
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: bool
    :param align: Align, The alignment of the new objectWORLD World, Align the new object to the world.VIEW View, Align the new object to the view.CURSOR 3D Cursor, Use the 3D cursor orientation for the new object. 
    :type align: int
    :param location: Location, Location for the newly added object 
    :type location: float
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float
    '''

    pass


def primitive_cube_add(size: float = 2.0,
                       calc_uvs: bool = True,
                       enter_editmode: bool = False,
                       align: int = 'WORLD',
                       location: float = (0.0, 0.0, 0.0),
                       rotation: float = (0.0, 0.0, 0.0)):
    '''Construct a cube mesh 

    :param size: Size 
    :type size: float
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: bool
    :param align: Align, The alignment of the new objectWORLD World, Align the new object to the world.VIEW View, Align the new object to the view.CURSOR 3D Cursor, Use the 3D cursor orientation for the new object. 
    :type align: int
    :param location: Location, Location for the newly added object 
    :type location: float
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float
    '''

    pass


def primitive_cube_add_gizmo(
        calc_uvs: bool = True,
        enter_editmode: bool = False,
        align: int = 'WORLD',
        location: float = (0.0, 0.0, 0.0),
        rotation: float = (0.0, 0.0, 0.0),
        matrix: float = ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0),
                         (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))):
    '''Construct a cube mesh 

    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: bool
    :param align: Align, The alignment of the new objectWORLD World, Align the new object to the world.VIEW View, Align the new object to the view.CURSOR 3D Cursor, Use the 3D cursor orientation for the new object. 
    :type align: int
    :param location: Location, Location for the newly added object 
    :type location: float
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float
    :param matrix: Matrix 
    :type matrix: float
    '''

    pass


def primitive_cylinder_add(vertices: int = 32,
                           radius: float = 1.0,
                           depth: float = 2.0,
                           end_fill_type: int = 'NGON',
                           calc_uvs: bool = True,
                           enter_editmode: bool = False,
                           align: int = 'WORLD',
                           location: float = (0.0, 0.0, 0.0),
                           rotation: float = (0.0, 0.0, 0.0)):
    '''Construct a cylinder mesh 

    :param vertices: Vertices 
    :type vertices: int
    :param radius: Radius 
    :type radius: float
    :param depth: Depth 
    :type depth: float
    :param end_fill_type: Cap Fill TypeNOTHING Nothing, Don’t fill at all.NGON Ngon, Use ngons.TRIFAN Triangle Fan, Use triangle fans. 
    :type end_fill_type: int
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: bool
    :param align: Align, The alignment of the new objectWORLD World, Align the new object to the world.VIEW View, Align the new object to the view.CURSOR 3D Cursor, Use the 3D cursor orientation for the new object. 
    :type align: int
    :param location: Location, Location for the newly added object 
    :type location: float
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float
    '''

    pass


def primitive_grid_add(x_subdivisions: int = 10,
                       y_subdivisions: int = 10,
                       size: float = 2.0,
                       calc_uvs: bool = True,
                       enter_editmode: bool = False,
                       align: int = 'WORLD',
                       location: float = (0.0, 0.0, 0.0),
                       rotation: float = (0.0, 0.0, 0.0)):
    '''Construct a grid mesh 

    :param x_subdivisions: X Subdivisions 
    :type x_subdivisions: int
    :param y_subdivisions: Y Subdivisions 
    :type y_subdivisions: int
    :param size: Size 
    :type size: float
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: bool
    :param align: Align, The alignment of the new objectWORLD World, Align the new object to the world.VIEW View, Align the new object to the view.CURSOR 3D Cursor, Use the 3D cursor orientation for the new object. 
    :type align: int
    :param location: Location, Location for the newly added object 
    :type location: float
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float
    '''

    pass


def primitive_ico_sphere_add(subdivisions: int = 2,
                             radius: float = 1.0,
                             calc_uvs: bool = True,
                             enter_editmode: bool = False,
                             align: int = 'WORLD',
                             location: float = (0.0, 0.0, 0.0),
                             rotation: float = (0.0, 0.0, 0.0)):
    '''Construct an Icosphere mesh 

    :param subdivisions: Subdivisions 
    :type subdivisions: int
    :param radius: Radius 
    :type radius: float
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: bool
    :param align: Align, The alignment of the new objectWORLD World, Align the new object to the world.VIEW View, Align the new object to the view.CURSOR 3D Cursor, Use the 3D cursor orientation for the new object. 
    :type align: int
    :param location: Location, Location for the newly added object 
    :type location: float
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float
    '''

    pass


def primitive_monkey_add(size: float = 2.0,
                         calc_uvs: bool = True,
                         enter_editmode: bool = False,
                         align: int = 'WORLD',
                         location: float = (0.0, 0.0, 0.0),
                         rotation: float = (0.0, 0.0, 0.0)):
    '''Construct a Suzanne mesh 

    :param size: Size 
    :type size: float
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: bool
    :param align: Align, The alignment of the new objectWORLD World, Align the new object to the world.VIEW View, Align the new object to the view.CURSOR 3D Cursor, Use the 3D cursor orientation for the new object. 
    :type align: int
    :param location: Location, Location for the newly added object 
    :type location: float
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float
    '''

    pass


def primitive_plane_add(size: float = 2.0,
                        calc_uvs: bool = True,
                        enter_editmode: bool = False,
                        align: int = 'WORLD',
                        location: float = (0.0, 0.0, 0.0),
                        rotation: float = (0.0, 0.0, 0.0)):
    '''Construct a filled planar mesh with 4 vertices 

    :param size: Size 
    :type size: float
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: bool
    :param align: Align, The alignment of the new objectWORLD World, Align the new object to the world.VIEW View, Align the new object to the view.CURSOR 3D Cursor, Use the 3D cursor orientation for the new object. 
    :type align: int
    :param location: Location, Location for the newly added object 
    :type location: float
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float
    '''

    pass


def primitive_torus_add(align: int = 'WORLD',
                        location: float = (0.0, 0.0, 0.0),
                        rotation: float = (0.0, 0.0, 0.0),
                        major_segments: int = 48,
                        minor_segments: int = 12,
                        mode: int = 'MAJOR_MINOR',
                        major_radius: float = 1.0,
                        minor_radius: float = 0.25,
                        abso_major_rad: float = 1.25,
                        abso_minor_rad: float = 0.75,
                        generate_uvs: bool = True):
    '''Add a torus mesh 

    :param align: AlignWORLD World, Align the new object to the world.VIEW View, Align the new object to the view.CURSOR 3D Cursor, Use the 3D cursor orientation for the new object. 
    :type align: int
    :param location: Location 
    :type location: float
    :param rotation: Rotation 
    :type rotation: float
    :param major_segments: Major Segments, Number of segments for the main ring of the torus 
    :type major_segments: int
    :param minor_segments: Minor Segments, Number of segments for the minor ring of the torus 
    :type minor_segments: int
    :param mode: Torus DimensionsMAJOR_MINOR Major/Minor, Use the major/minor radii for torus dimensions.EXT_INT Exterior/Interior, Use the exterior/interior radii for torus dimensions. 
    :type mode: int
    :param major_radius: Major Radius, Radius from the origin to the center of the cross sections 
    :type major_radius: float
    :param minor_radius: Minor Radius, Radius of the torus’ cross section 
    :type minor_radius: float
    :param abso_major_rad: Exterior Radius, Total Exterior Radius of the torus 
    :type abso_major_rad: float
    :param abso_minor_rad: Interior Radius, Total Interior Radius of the torus 
    :type abso_minor_rad: float
    :param generate_uvs: Generate UVs, Generate a default UV map 
    :type generate_uvs: bool
    '''

    pass


def primitive_uv_sphere_add(segments: int = 32,
                            ring_count: int = 16,
                            radius: float = 1.0,
                            calc_uvs: bool = True,
                            enter_editmode: bool = False,
                            align: int = 'WORLD',
                            location: float = (0.0, 0.0, 0.0),
                            rotation: float = (0.0, 0.0, 0.0)):
    '''Construct a UV sphere mesh 

    :param segments: Segments 
    :type segments: int
    :param ring_count: Rings 
    :type ring_count: int
    :param radius: Radius 
    :type radius: float
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: bool
    :param align: Align, The alignment of the new objectWORLD World, Align the new object to the world.VIEW View, Align the new object to the view.CURSOR 3D Cursor, Use the 3D cursor orientation for the new object. 
    :type align: int
    :param location: Location, Location for the newly added object 
    :type location: float
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float
    '''

    pass


def quads_convert_to_tris(quad_method: int = 'BEAUTY',
                          ngon_method: int = 'BEAUTY'):
    '''Triangulate selected faces 

    :param quad_method: Quad Method, Method for splitting the quads into trianglesBEAUTY Beauty , Split the quads in nice triangles, slower method.FIXED Fixed, Split the quads on the first and third vertices.FIXED_ALTERNATE Fixed Alternate, Split the quads on the 2nd and 4th vertices.SHORTEST_DIAGONAL Shortest Diagonal, Split the quads based on the distance between the vertices. 
    :type quad_method: int
    :param ngon_method: Polygon Method, Method for splitting the polygons into trianglesBEAUTY Beauty, Arrange the new triangles evenly (slow).CLIP Clip, Split the polygons with an ear clipping algorithm. 
    :type ngon_method: int
    '''

    pass


def region_to_loop():
    '''Select boundary edges around the selected faces 

    '''

    pass


def remove_doubles(threshold: float = 0.0001, use_unselected: bool = False):
    '''Merge vertices based on their proximity 

    :param threshold: Merge Distance, Minimum distance between elements to merge 
    :type threshold: float
    :param use_unselected: Unselected, Merge selected to other unselected vertices 
    :type use_unselected: bool
    '''

    pass


def reveal(select: bool = True):
    '''Reveal all hidden vertices, edges and faces 

    :param select: Select 
    :type select: bool
    '''

    pass


def rip(mirror: bool = False,
        use_proportional_edit: bool = False,
        proportional_edit_falloff: int = 'SMOOTH',
        proportional_size: float = 1.0,
        use_proportional_connected: bool = False,
        use_proportional_projected: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False,
        use_fill: bool = False):
    '''Disconnect vertex or edges from connected geometry 

    :param mirror: Mirror Editing 
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing 
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: int
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


def rip_edge(mirror: bool = False,
             use_proportional_edit: bool = False,
             proportional_edit_falloff: int = 'SMOOTH',
             proportional_size: float = 1.0,
             use_proportional_connected: bool = False,
             use_proportional_projected: bool = False,
             release_confirm: bool = False,
             use_accurate: bool = False):
    '''Extend vertices along the edge closest to the cursor 

    :param mirror: Mirror Editing 
    :type mirror: bool
    :param use_proportional_edit: Proportional Editing 
    :type use_proportional_edit: bool
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: int
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


def rip_edge_move(MESH_OT_rip_edge=None, TRANSFORM_OT_translate=None):
    '''Extend vertices and move the result 

    :param MESH_OT_rip_edge: Extend Vertices, Extend vertices along the edge closest to the cursor 
    :param TRANSFORM_OT_translate: Move, Move selected items 
    '''

    pass


def rip_move(MESH_OT_rip=None, TRANSFORM_OT_translate=None):
    '''Rip polygons and move the result 

    :param MESH_OT_rip: Rip, Disconnect vertex or edges from connected geometry 
    :param TRANSFORM_OT_translate: Move, Move selected items 
    '''

    pass


def screw(steps: int = 9,
          turns: int = 1,
          center: float = (0.0, 0.0, 0.0),
          axis: float = (0.0, 0.0, 0.0)):
    '''Extrude selected vertices in screw-shaped rotation around the cursor in indicated viewport 

    :param steps: Steps, Steps 
    :type steps: int
    :param turns: Turns, Turns 
    :type turns: int
    :param center: Center, Center in global view space 
    :type center: float
    :param axis: Axis, Axis in global view space 
    :type axis: float
    '''

    pass


def select_all(action: int = 'TOGGLE'):
    '''(De)select all vertices, edges or faces 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: int
    '''

    pass


def select_axis(orientation: int = 'LOCAL',
                sign: int = 'POS',
                axis: int = 'X',
                threshold: float = 0.0001):
    '''Select all data in the mesh on a single axis 

    :param orientation: Axis Mode, Axis orientationGLOBAL Global, Align the transformation axes to world space.LOCAL Local, Align the transformation axes to the selected objects’ local space.NORMAL Normal, Align the transformation axes to average normal of selected elements (bone Y axis for pose mode).GIMBAL Gimbal, Align each axis to the Euler rotation axis as used for input.VIEW View, Align the transformation axes to the window.CURSOR Cursor, Align the transformation axes to the 3D cursor. 
    :type orientation: int
    :param sign: Axis Sign, Side to select 
    :type sign: int
    :param axis: Axis, Select the axis to compare each vertex on 
    :type axis: int
    :param threshold: Threshold 
    :type threshold: float
    '''

    pass


def select_face_by_sides(number: int = 4,
                         type: int = 'EQUAL',
                         extend: bool = True):
    '''Select vertices or faces by the number of polygon sides 

    :param number: Number of Vertices 
    :type number: int
    :param type: Type, Type of comparison to make 
    :type type: int
    :param extend: Extend, Extend the selection 
    :type extend: bool
    '''

    pass


def select_interior_faces():
    '''Select faces where all edges have more than 2 face users 

    '''

    pass


def select_less(use_face_step: bool = True):
    '''Deselect vertices, edges or faces at the boundary of each selection region 

    :param use_face_step: Face Step, Connected faces (instead of edges) 
    :type use_face_step: bool
    '''

    pass


def select_linked(delimit: typing.Set[int] = {'SEAM'}):
    '''Select all vertices connected to the current selection 

    :param delimit: Delimit, Delimit selected regionNORMAL Regular, Delimit by face directions.MATERIAL Material, Delimit by face material.SEAM Seam, Delimit by edge seams.SHARP Sharp, Delimit by sharp edges.UV UVs, Delimit by UV coordinates. 
    :type delimit: typing.Set[int]
    '''

    pass


def select_linked_pick(deselect: bool = False,
                       delimit: typing.Set[int] = {'SEAM'},
                       index=-1):
    '''(De)select all vertices linked to the edge under the mouse cursor 

    :param deselect: Deselect 
    :type deselect: bool
    :param delimit: Delimit, Delimit selected regionNORMAL Regular, Delimit by face directions.MATERIAL Material, Delimit by face material.SEAM Seam, Delimit by edge seams.SHARP Sharp, Delimit by sharp edges.UV UVs, Delimit by UV coordinates. 
    :type delimit: typing.Set[int]
    '''

    pass


def select_loose(extend: bool = False):
    '''Select loose geometry based on the selection mode 

    :param extend: Extend, Extend the selection 
    :type extend: bool
    '''

    pass


def select_mirror(axis: typing.Set[int] = {'X'}, extend: bool = False):
    '''Select mesh items at mirrored locations 

    :param axis: Axis 
    :type axis: typing.Set[int]
    :param extend: Extend, Extend the existing selection 
    :type extend: bool
    '''

    pass


def select_mode(use_extend: bool = False,
                use_expand: bool = False,
                type: int = 'VERT',
                action: int = 'TOGGLE'):
    '''Change selection mode 

    :param use_extend: Extend 
    :type use_extend: bool
    :param use_expand: Expand 
    :type use_expand: bool
    :param type: Type 
    :type type: int
    :param action: Action, Selection action to executeDISABLE Disable, Disable selected markers.ENABLE Enable, Enable selected markers.TOGGLE Toggle, Toggle disabled flag for selected markers. 
    :type action: int
    '''

    pass


def select_more(use_face_step: bool = True):
    '''Select more vertices, edges or faces connected to initial selection 

    :param use_face_step: Face Step, Connected faces (instead of edges) 
    :type use_face_step: bool
    '''

    pass


def select_next_item():
    '''Select the next element (using selection order) 

    '''

    pass


def select_non_manifold(extend: bool = True,
                        use_wire: bool = True,
                        use_boundary: bool = True,
                        use_multi_face: bool = True,
                        use_non_contiguous: bool = True,
                        use_verts: bool = True):
    '''Select all non-manifold vertices or edges 

    :param extend: Extend, Extend the selection 
    :type extend: bool
    :param use_wire: Wire, Wire edges 
    :type use_wire: bool
    :param use_boundary: Boundaries, Boundary edges 
    :type use_boundary: bool
    :param use_multi_face: Multiple Faces, Edges shared by 3+ faces 
    :type use_multi_face: bool
    :param use_non_contiguous: Non Contiguous, Edges between faces pointing in alternate directions 
    :type use_non_contiguous: bool
    :param use_verts: Vertices, Vertices connecting multiple face regions 
    :type use_verts: bool
    '''

    pass


def select_nth(nth: int = 2, skip: int = 1, offset: int = 0):
    '''Deselect every Nth element starting from the active vertex, edge or face 

    :param nth: Nth Element, Skip every Nth element 
    :type nth: int
    :param skip: Skip, Number of elements to skip at once 
    :type skip: int
    :param offset: Offset, Offset from the starting point 
    :type offset: int
    '''

    pass


def select_prev_item():
    '''Select the previous element (using selection order) 

    '''

    pass


def select_random(percent: float = 50.0, seed: int = 0,
                  action: int = 'SELECT'):
    '''Randomly select vertices 

    :param percent: Percent, Percentage of objects to select randomly 
    :type percent: float
    :param seed: Random Seed, Seed for the random number generator 
    :type seed: int
    :param action: Action, Selection action to executeSELECT Select, Select all elements.DESELECT Deselect, Deselect all elements. 
    :type action: int
    '''

    pass


def select_similar(type: int = 'NORMAL',
                   compare: int = 'EQUAL',
                   threshold: float = 0.0):
    '''Select similar vertices, edges or faces by property types 

    :param type: Type 
    :type type: int
    :param compare: Compare 
    :type compare: int
    :param threshold: Threshold 
    :type threshold: float
    '''

    pass


def select_similar_region():
    '''Select similar face regions to the current selection 

    '''

    pass


def select_ungrouped(extend: bool = False):
    '''Select vertices without a group 

    :param extend: Extend, Extend the selection 
    :type extend: bool
    '''

    pass


def separate(type: int = 'SELECTED'):
    '''Separate selected geometry into a new mesh 

    :param type: Type 
    :type type: int
    '''

    pass


def set_normals_from_faces(keep_sharp: bool = False):
    '''Set the custom normals from the selected faces ones 

    :param keep_sharp: Keep Sharp Edges, Do not set sharp edges to face 
    :type keep_sharp: bool
    '''

    pass


def shape_propagate_to_all():
    '''Apply selected vertex locations to all other shape keys 

    '''

    pass


def shortest_path_pick(edge_mode: int = 'SELECT',
                       use_face_step: bool = False,
                       use_topology_distance: bool = False,
                       use_fill: bool = False,
                       nth: int = 1,
                       skip: int = 1,
                       offset: int = 0,
                       index=-1):
    '''Select shortest path between two selections 

    :param edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path 
    :type edge_mode: int
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings) 
    :type use_face_step: bool
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance 
    :type use_topology_distance: bool
    :param use_fill: Fill Region, Select all paths between the source/destination elements 
    :type use_fill: bool
    :param nth: Nth Element, Skip every Nth element 
    :type nth: int
    :param skip: Skip, Number of elements to skip at once 
    :type skip: int
    :param offset: Offset, Offset from the starting point 
    :type offset: int
    '''

    pass


def shortest_path_select(edge_mode: int = 'SELECT',
                         use_face_step: bool = False,
                         use_topology_distance: bool = False,
                         use_fill: bool = False,
                         nth: int = 1,
                         skip: int = 1,
                         offset: int = 0):
    '''Selected shortest path between two vertices/edges/faces 

    :param edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path 
    :type edge_mode: int
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings) 
    :type use_face_step: bool
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance 
    :type use_topology_distance: bool
    :param use_fill: Fill Region, Select all paths between the source/destination elements 
    :type use_fill: bool
    :param nth: Nth Element, Skip every Nth element 
    :type nth: int
    :param skip: Skip, Number of elements to skip at once 
    :type skip: int
    :param offset: Offset, Offset from the starting point 
    :type offset: int
    '''

    pass


def smoothen_normals(factor: float = 0.5):
    '''Smoothen custom normals based on adjacent vertex normals 

    :param factor: Factor, Specifies weight of smooth vs original normal 
    :type factor: float
    '''

    pass


def solidify(thickness: float = 0.01):
    '''Create a solid skin by extruding, compensating for sharp angles 

    :param thickness: Thickness 
    :type thickness: float
    '''

    pass


def sort_elements(type: int = 'VIEW_ZAXIS',
                  elements: typing.Set[int] = {'VERT'},
                  reverse: bool = False,
                  seed: int = 0):
    '''The order of selected vertices/edges/faces is modified, based on a given method 

    :param type: Type, Type of re-ordering operation to applyVIEW_ZAXIS View Z Axis, Sort selected elements from farthest to nearest one in current view.VIEW_XAXIS View X Axis, Sort selected elements from left to right one in current view.CURSOR_DISTANCE Cursor Distance, Sort selected elements from nearest to farthest from 3D cursor.MATERIAL Material, Sort selected elements from smallest to greatest material index (faces only!).SELECTED Selected, Move all selected elements in first places, preserving their relative order (WARNING: this will affect unselected elements’ indices as well!).RANDOMIZE Randomize, Randomize order of selected elements.REVERSE Reverse, Reverse current order of selected elements. 
    :type type: int
    :param elements: Elements, Which elements to affect (vertices, edges and/or faces) 
    :type elements: typing.Set[int]
    :param reverse: Reverse, Reverse the sorting effect 
    :type reverse: bool
    :param seed: Seed, Seed for random-based operations 
    :type seed: int
    '''

    pass


def spin(steps: int = 9,
         dupli: bool = False,
         angle: float = 1.5708,
         use_auto_merge: bool = True,
         use_normal_flip: bool = False,
         center: float = (0.0, 0.0, 0.0),
         axis: float = (0.0, 0.0, 0.0)):
    '''Extrude selected vertices in a circle around the cursor in indicated viewport 

    :param steps: Steps, Steps 
    :type steps: int
    :param dupli: Duplicate, Make Duplicates 
    :type dupli: bool
    :param angle: Angle, Rotation for each step 
    :type angle: float
    :param use_auto_merge: Auto Merge, Merge first/last when the angle is a full revolution 
    :type use_auto_merge: bool
    :param use_normal_flip: Flip Normals 
    :type use_normal_flip: bool
    :param center: Center, Center in global view space 
    :type center: float
    :param axis: Axis, Axis in global view space 
    :type axis: float
    '''

    pass


def split():
    '''Split off selected geometry from connected unselected geometry 

    '''

    pass


def split_normals():
    '''Split custom normals of selected vertices 

    '''

    pass


def subdivide(number_cuts: int = 1,
              smoothness: float = 0.0,
              ngon: bool = True,
              quadcorner: int = 'STRAIGHT_CUT',
              fractal: float = 0.0,
              fractal_along_normal: float = 0.0,
              seed: int = 0):
    '''Subdivide selected edges 

    :param number_cuts: Number of Cuts 
    :type number_cuts: int
    :param smoothness: Smoothness, Smoothness factor 
    :type smoothness: float
    :param ngon: Create N-Gons, When disabled, newly created faces are limited to 3-4 sided faces 
    :type ngon: bool
    :param quadcorner: Quad Corner Type, How to subdivide quad corners (anything other than Straight Cut will prevent ngons) 
    :type quadcorner: int
    :param fractal: Fractal, Fractal randomness factor 
    :type fractal: float
    :param fractal_along_normal: Along Normal, Apply fractal displacement along normal only 
    :type fractal_along_normal: float
    :param seed: Random Seed, Seed for the random number generator 
    :type seed: int
    '''

    pass


def subdivide_edgering(number_cuts: int = 10,
                       interpolation: int = 'PATH',
                       smoothness: float = 1.0,
                       profile_shape_factor: float = 0.0,
                       profile_shape: int = 'SMOOTH'):
    '''Subdivide perpendicular edges to the selected edge ring 

    :param number_cuts: Number of Cuts 
    :type number_cuts: int
    :param interpolation: Interpolation, Interpolation method 
    :type interpolation: int
    :param smoothness: Smoothness, Smoothness factor 
    :type smoothness: float
    :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded 
    :type profile_shape_factor: float
    :param profile_shape: Profile Shape, Shape of the profileSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff. 
    :type profile_shape: int
    '''

    pass


def symmetrize(direction: int = 'NEGATIVE_X', threshold: float = 0.0001):
    '''Enforce symmetry (both form and topological) across an axis 

    :param direction: Direction, Which sides to copy from and to 
    :type direction: int
    :param threshold: Threshold, Limit for snap middle vertices to the axis center 
    :type threshold: float
    '''

    pass


def symmetry_snap(direction: int = 'NEGATIVE_X',
                  threshold: float = 0.05,
                  factor: float = 0.5,
                  use_center: bool = True):
    '''Snap vertex pairs to their mirrored locations 

    :param direction: Direction, Which sides to copy from and to 
    :type direction: int
    :param threshold: Threshold, Distance within which matching vertices are searched 
    :type threshold: float
    :param factor: Factor, Mix factor of the locations of the vertices 
    :type factor: float
    :param use_center: Center, Snap middle vertices to the axis center 
    :type use_center: bool
    '''

    pass


def tris_convert_to_quads(face_threshold: float = 0.698132,
                          shape_threshold: float = 0.698132,
                          uvs: bool = False,
                          vcols: bool = False,
                          seam: bool = False,
                          sharp: bool = False,
                          materials: bool = False):
    '''Join triangles into quads 

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


def unsubdivide(iterations: int = 2):
    '''UnSubdivide selected edges & faces 

    :param iterations: Iterations, Number of times to unsubdivide 
    :type iterations: int
    '''

    pass


def uv_texture_add():
    '''Add UV Map 

    '''

    pass


def uv_texture_remove():
    '''Remove UV Map 

    '''

    pass


def uvs_reverse():
    '''Flip direction of UV coordinates inside faces 

    '''

    pass


def uvs_rotate(use_ccw: bool = False):
    '''Rotate UV coordinates inside faces 

    :param use_ccw: Counter Clockwise 
    :type use_ccw: bool
    '''

    pass


def vert_connect():
    '''Connect selected vertices of faces, splitting the face 

    '''

    pass


def vert_connect_concave():
    '''Make all faces convex 

    '''

    pass


def vert_connect_nonplanar(angle_limit: float = 0.0872665):
    '''Split non-planar faces that exceed the angle threshold 

    :param angle_limit: Max Angle, Angle limit 
    :type angle_limit: float
    '''

    pass


def vert_connect_path():
    '''Connect vertices by their selection order, creating edges, splitting faces 

    '''

    pass


def vertex_color_add():
    '''Add vertex color layer 

    '''

    pass


def vertex_color_remove():
    '''Remove vertex color layer 

    '''

    pass


def vertices_smooth(factor: float = 0.5,
                    repeat: int = 1,
                    xaxis: bool = True,
                    yaxis: bool = True,
                    zaxis: bool = True):
    '''Flatten angles of selected vertices 

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
    '''

    pass


def vertices_smooth_laplacian(repeat: int = 1,
                              lambda_factor: float = 1.0,
                              lambda_border: float = 5e-05,
                              use_x: bool = True,
                              use_y: bool = True,
                              use_z: bool = True,
                              preserve_volume: bool = True):
    '''Laplacian smooth of selected vertices 

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


def wireframe(use_boundary: bool = True,
              use_even_offset: bool = True,
              use_relative_offset: bool = False,
              use_replace: bool = True,
              thickness: float = 0.01,
              offset: float = 0.01,
              use_crease: bool = False,
              crease_weight: float = 0.01):
    '''Create a solid wire-frame from faces 

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
    :param use_crease: Crease, Crease hub edges for improved subsurf 
    :type use_crease: bool
    :param crease_weight: Crease weight 
    :type crease_weight: float
    '''

    pass
