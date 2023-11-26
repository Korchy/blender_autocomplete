import sys
import typing
import bpy.types
import bpy.ops.transform

GenericType = typing.TypeVar("GenericType")


def attribute_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        value_float: typing.Optional[typing.Any] = 0.0,
        value_float_vector_2d: typing.Optional[typing.Any] = (0.0, 0.0),
        value_float_vector_3d: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        value_int: typing.Optional[typing.Any] = 0,
        value_int_vector_2d: typing.Optional[typing.Any] = (0, 0),
        value_color: typing.Optional[typing.Any] = (1.0, 1.0, 1.0, 1.0),
        value_bool: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Set values of the active attribute for selected elements

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param value_float: Value
    :type value_float: typing.Optional[typing.Any]
    :param value_float_vector_2d: Value
    :type value_float_vector_2d: typing.Optional[typing.Any]
    :param value_float_vector_3d: Value
    :type value_float_vector_3d: typing.Optional[typing.Any]
    :param value_int: Value
    :type value_int: typing.Optional[typing.Any]
    :param value_int_vector_2d: Value
    :type value_int_vector_2d: typing.Optional[typing.Any]
    :param value_color: Value
    :type value_color: typing.Optional[typing.Any]
    :param value_bool: Value
    :type value_bool: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def average_normals(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        average_type: typing.Optional[typing.Any] = 'CUSTOM_NORMAL',
        weight: typing.Optional[typing.Any] = 50,
        threshold: typing.Optional[typing.Any] = 0.01):
    ''' Average custom normals of selected vertices

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param average_type: Type, Averaging method * ``CUSTOM_NORMAL`` Custom Normal -- Take average of vertex normals. * ``FACE_AREA`` Face Area -- Set all vertex normals by face area. * ``CORNER_ANGLE`` Corner Angle -- Set all vertex normals by corner angle.
    :type average_type: typing.Optional[typing.Any]
    :param weight: Weight, Weight applied per face
    :type weight: typing.Optional[typing.Any]
    :param threshold: Threshold, Threshold value for different weights to be considered equal
    :type threshold: typing.Optional[typing.Any]
    '''

    pass


def beautify_fill(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        angle_limit: typing.Optional[typing.Any] = 3.14159):
    ''' Rearrange some faces to try to get less degenerated geometry

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param angle_limit: Max Angle, Angle limit
    :type angle_limit: typing.Optional[typing.Any]
    '''

    pass


def bevel(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        offset_type: typing.Optional[typing.Any] = 'OFFSET',
        offset: typing.Optional[typing.Any] = 0.0,
        profile_type: typing.Optional[typing.Any] = 'SUPERELLIPSE',
        offset_pct: typing.Optional[typing.Any] = 0.0,
        segments: typing.Optional[typing.Any] = 1,
        profile: typing.Optional[typing.Any] = 0.5,
        affect: typing.Optional[typing.Any] = 'EDGES',
        clamp_overlap: typing.Optional[typing.Union[bool, typing.Any]] = False,
        loop_slide: typing.Optional[typing.Union[bool, typing.Any]] = True,
        mark_seam: typing.Optional[typing.Union[bool, typing.Any]] = False,
        mark_sharp: typing.Optional[typing.Union[bool, typing.Any]] = False,
        material: typing.Optional[typing.Any] = -1,
        harden_normals: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        face_strength_mode: typing.Optional[typing.Any] = 'NONE',
        miter_outer: typing.Optional[typing.Any] = 'SHARP',
        miter_inner: typing.Optional[typing.Any] = 'SHARP',
        spread: typing.Optional[typing.Any] = 0.1,
        vmesh_method: typing.Optional[typing.Any] = 'ADJ',
        release_confirm: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False):
    ''' Cut into selected items at an angle to create bevel or chamfer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param offset_type: Width Type, The method for determining the size of the bevel * ``OFFSET`` Offset -- Amount is offset of new edges from original. * ``WIDTH`` Width -- Amount is width of new face. * ``DEPTH`` Depth -- Amount is perpendicular distance from original edge to bevel face. * ``PERCENT`` Percent -- Amount is percent of adjacent edge length. * ``ABSOLUTE`` Absolute -- Amount is absolute distance along adjacent edge.
    :type offset_type: typing.Optional[typing.Any]
    :param offset: Width, Bevel amount
    :type offset: typing.Optional[typing.Any]
    :param profile_type: Profile Type, The type of shape used to rebuild a beveled section * ``SUPERELLIPSE`` Superellipse -- The profile can be a concave or convex curve. * ``CUSTOM`` Custom -- The profile can be any arbitrary path between its endpoints.
    :type profile_type: typing.Optional[typing.Any]
    :param offset_pct: Width Percent, Bevel amount for percentage method
    :type offset_pct: typing.Optional[typing.Any]
    :param segments: Segments, Segments for curved edge
    :type segments: typing.Optional[typing.Any]
    :param profile: Profile, Controls profile shape (0.5 = round)
    :type profile: typing.Optional[typing.Any]
    :param affect: Affect, Affect edges or vertices * ``VERTICES`` Vertices -- Affect only vertices. * ``EDGES`` Edges -- Affect only edges.
    :type affect: typing.Optional[typing.Any]
    :param clamp_overlap: Clamp Overlap, Do not allow beveled edges/vertices to overlap each other
    :type clamp_overlap: typing.Optional[typing.Union[bool, typing.Any]]
    :param loop_slide: Loop Slide, Prefer sliding along edges to even widths
    :type loop_slide: typing.Optional[typing.Union[bool, typing.Any]]
    :param mark_seam: Mark Seams, Mark Seams along beveled edges
    :type mark_seam: typing.Optional[typing.Union[bool, typing.Any]]
    :param mark_sharp: Mark Sharp, Mark beveled edges as sharp
    :type mark_sharp: typing.Optional[typing.Union[bool, typing.Any]]
    :param material: Material Index, Material for bevel faces (-1 means use adjacent faces)
    :type material: typing.Optional[typing.Any]
    :param harden_normals: Harden Normals, Match normals of new faces to adjacent faces
    :type harden_normals: typing.Optional[typing.Union[bool, typing.Any]]
    :param face_strength_mode: Face Strength Mode, Whether to set face strength, and which faces to set face strength on * ``NONE`` None -- Do not set face strength. * ``NEW`` New -- Set face strength on new faces only. * ``AFFECTED`` Affected -- Set face strength on new and modified faces only. * ``ALL`` All -- Set face strength on all faces.
    :type face_strength_mode: typing.Optional[typing.Any]
    :param miter_outer: Outer Miter, Pattern to use for outside of miters * ``SHARP`` Sharp -- Outside of miter is sharp. * ``PATCH`` Patch -- Outside of miter is squared-off patch. * ``ARC`` Arc -- Outside of miter is arc.
    :type miter_outer: typing.Optional[typing.Any]
    :param miter_inner: Inner Miter, Pattern to use for inside of miters * ``SHARP`` Sharp -- Inside of miter is sharp. * ``ARC`` Arc -- Inside of miter is arc.
    :type miter_inner: typing.Optional[typing.Any]
    :param spread: Spread, Amount to spread arcs for arc inner miters
    :type spread: typing.Optional[typing.Any]
    :param vmesh_method: Vertex Mesh Method, The method to use to create meshes at intersections * ``ADJ`` Grid Fill -- Default patterned fill. * ``CUTOFF`` Cutoff -- A cutoff at each profile's end before the intersection.
    :type vmesh_method: typing.Optional[typing.Any]
    :param release_confirm: Confirm on Release
    :type release_confirm: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def bisect(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        plane_co: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        plane_no: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        use_fill: typing.Optional[typing.Union[bool, typing.Any]] = False,
        clear_inner: typing.Optional[typing.Union[bool, typing.Any]] = False,
        clear_outer: typing.Optional[typing.Union[bool, typing.Any]] = False,
        threshold: typing.Optional[typing.Any] = 0.0001,
        xstart: typing.Optional[typing.Any] = 0,
        xend: typing.Optional[typing.Any] = 0,
        ystart: typing.Optional[typing.Any] = 0,
        yend: typing.Optional[typing.Any] = 0,
        flip: typing.Optional[typing.Union[bool, typing.Any]] = False,
        cursor: typing.Optional[typing.Any] = 5):
    ''' Cut geometry along a plane (click-drag to define plane)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param plane_co: Plane Point, A point on the plane
    :type plane_co: typing.Optional[typing.Any]
    :param plane_no: Plane Normal, The direction the plane points
    :type plane_no: typing.Optional[typing.Any]
    :param use_fill: Fill, Fill in the cut
    :type use_fill: typing.Optional[typing.Union[bool, typing.Any]]
    :param clear_inner: Clear Inner, Remove geometry behind the plane
    :type clear_inner: typing.Optional[typing.Union[bool, typing.Any]]
    :param clear_outer: Clear Outer, Remove geometry in front of the plane
    :type clear_outer: typing.Optional[typing.Union[bool, typing.Any]]
    :param threshold: Axis Threshold, Preserves the existing geometry along the cut plane
    :type threshold: typing.Optional[typing.Any]
    :param xstart: X Start
    :type xstart: typing.Optional[typing.Any]
    :param xend: X End
    :type xend: typing.Optional[typing.Any]
    :param ystart: Y Start
    :type ystart: typing.Optional[typing.Any]
    :param yend: Y End
    :type yend: typing.Optional[typing.Any]
    :param flip: Flip
    :type flip: typing.Optional[typing.Union[bool, typing.Any]]
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: typing.Optional[typing.Any]
    '''

    pass


def blend_from_shape(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        shape: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        blend: typing.Optional[typing.Any] = 1.0,
        add: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Blend in shape from a shape key

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param shape: Shape, Shape key to use for blending
    :type shape: typing.Optional[typing.Union[str, int, typing.Any]]
    :param blend: Blend, Blending factor
    :type blend: typing.Optional[typing.Any]
    :param add: Add, Add rather than blend between shapes
    :type add: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def bridge_edge_loops(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'SINGLE',
        use_merge: typing.Optional[typing.Union[bool, typing.Any]] = False,
        merge_factor: typing.Optional[typing.Any] = 0.5,
        twist_offset: typing.Optional[typing.Any] = 0,
        number_cuts: typing.Optional[typing.Any] = 0,
        interpolation: typing.Optional[typing.Any] = 'PATH',
        smoothness: typing.Optional[typing.Any] = 1.0,
        profile_shape_factor: typing.Optional[typing.Any] = 0.0,
        profile_shape: typing.Optional[typing.Union[str, int]] = 'SMOOTH'):
    ''' Create a bridge of faces between two or more selected edge loops

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Connect Loops, Method of bridging multiple loops
    :type type: typing.Optional[typing.Any]
    :param use_merge: Merge, Merge rather than creating faces
    :type use_merge: typing.Optional[typing.Union[bool, typing.Any]]
    :param merge_factor: Merge Factor
    :type merge_factor: typing.Optional[typing.Any]
    :param twist_offset: Twist, Twist offset for closed loops
    :type twist_offset: typing.Optional[typing.Any]
    :param number_cuts: Number of Cuts
    :type number_cuts: typing.Optional[typing.Any]
    :param interpolation: Interpolation, Interpolation method
    :type interpolation: typing.Optional[typing.Any]
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: typing.Optional[typing.Any]
    :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded
    :type profile_shape_factor: typing.Optional[typing.Any]
    :param profile_shape: Profile Shape, Shape of the profile
    :type profile_shape: typing.Optional[typing.Union[str, int]]
    '''

    pass


def colors_reverse(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Flip direction of vertex colors inside faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def colors_rotate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_ccw: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Rotate color attributes inside faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_ccw: Counter Clockwise
    :type use_ccw: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def convex_hull(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        delete_unused: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_existing_faces: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = True,
        make_holes: typing.Optional[typing.Union[bool, typing.Any]] = False,
        join_triangles: typing.Optional[typing.Union[bool, typing.Any]] = True,
        face_threshold: typing.Optional[typing.Any] = 0.698132,
        shape_threshold: typing.Optional[typing.Any] = 0.698132,
        uvs: typing.Optional[typing.Union[bool, typing.Any]] = False,
        vcols: typing.Optional[typing.Union[bool, typing.Any]] = False,
        seam: typing.Optional[typing.Union[bool, typing.Any]] = False,
        sharp: typing.Optional[typing.Union[bool, typing.Any]] = False,
        materials: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Enclose selected vertices in a convex polyhedron

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param delete_unused: Delete Unused, Delete selected elements that are not used by the hull
    :type delete_unused: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_existing_faces: Use Existing Faces, Skip hull triangles that are covered by a pre-existing face
    :type use_existing_faces: typing.Optional[typing.Union[bool, typing.Any]]
    :param make_holes: Make Holes, Delete selected faces that are used by the hull
    :type make_holes: typing.Optional[typing.Union[bool, typing.Any]]
    :param join_triangles: Join Triangles, Merge adjacent triangles into quads
    :type join_triangles: typing.Optional[typing.Union[bool, typing.Any]]
    :param face_threshold: Max Face Angle, Face angle limit
    :type face_threshold: typing.Optional[typing.Any]
    :param shape_threshold: Max Shape Angle, Shape angle limit
    :type shape_threshold: typing.Optional[typing.Any]
    :param uvs: Compare UVs
    :type uvs: typing.Optional[typing.Union[bool, typing.Any]]
    :param vcols: Compare VCols
    :type vcols: typing.Optional[typing.Union[bool, typing.Any]]
    :param seam: Compare Seam
    :type seam: typing.Optional[typing.Union[bool, typing.Any]]
    :param sharp: Compare Sharp
    :type sharp: typing.Optional[typing.Union[bool, typing.Any]]
    :param materials: Compare Materials
    :type materials: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def customdata_bevel_weight_edge_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add an edge bevel weight layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def customdata_bevel_weight_edge_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Clear the edge bevel weight layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def customdata_bevel_weight_vertex_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add a vertex bevel weight layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def customdata_bevel_weight_vertex_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Clear the vertex bevel weight layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def customdata_crease_edge_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add an edge crease layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def customdata_crease_edge_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Clear the edge crease layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def customdata_crease_vertex_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add a vertex crease layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def customdata_crease_vertex_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Clear the vertex crease layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def customdata_custom_splitnormals_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add a custom split normals layer, if none exists yet

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def customdata_custom_splitnormals_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove the custom split normals layer, if it exists

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def customdata_mask_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Clear vertex sculpt masking data from the mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def customdata_skin_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add a vertex skin layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def customdata_skin_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Clear vertex skin layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def decimate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        ratio: typing.Optional[typing.Any] = 1.0,
        use_vertex_group: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        vertex_group_factor: typing.Optional[typing.Any] = 1.0,
        invert_vertex_group: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = False,
        use_symmetry: typing.Optional[typing.Union[bool, typing.Any]] = False,
        symmetry_axis: typing.Optional[typing.Union[str, int]] = 'Y'):
    ''' Simplify geometry by collapsing edges

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param ratio: Ratio
    :type ratio: typing.Optional[typing.Any]
    :param use_vertex_group: Vertex Group, Use active vertex group as an influence
    :type use_vertex_group: typing.Optional[typing.Union[bool, typing.Any]]
    :param vertex_group_factor: Weight, Vertex group strength
    :type vertex_group_factor: typing.Optional[typing.Any]
    :param invert_vertex_group: Invert, Invert vertex group influence
    :type invert_vertex_group: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_symmetry: Symmetry, Maintain symmetry on an axis
    :type use_symmetry: typing.Optional[typing.Union[bool, typing.Any]]
    :param symmetry_axis: Axis, Axis of symmetry
    :type symmetry_axis: typing.Optional[typing.Union[str, int]]
    '''

    pass


def delete(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None,
           *,
           type: typing.Optional[typing.Any] = 'VERT'):
    ''' Delete selected vertices, edges or faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type, Method used for deleting mesh data
    :type type: typing.Optional[typing.Any]
    '''

    pass


def delete_edgeloop(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_face_split: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = True):
    ''' Delete an edge loop by merging the faces on each side

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def delete_loose(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_verts: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_edges: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_faces: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Delete loose vertices, edges or faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_verts: Vertices, Remove loose vertices
    :type use_verts: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_edges: Edges, Remove loose edges
    :type use_edges: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_faces: Faces, Remove loose faces
    :type use_faces: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def dissolve_degenerate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        threshold: typing.Optional[typing.Any] = 0.0001):
    ''' Dissolve zero area faces and zero length edges

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param threshold: Merge Distance, Maximum distance between elements to merge
    :type threshold: typing.Optional[typing.Any]
    '''

    pass


def dissolve_edges(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_verts: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_face_split: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False):
    ''' Dissolve edges, merging faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_verts: Dissolve Vertices, Dissolve remaining vertices
    :type use_verts: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def dissolve_faces(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_verts: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Dissolve faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_verts: Dissolve Vertices, Dissolve remaining vertices
    :type use_verts: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def dissolve_limited(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        angle_limit: typing.Optional[typing.Any] = 0.0872665,
        use_dissolve_boundaries: typing.Optional[typing.Union[bool, typing.
                                                              Any]] = False,
        delimit: typing.Optional[typing.Any] = {'NORMAL'}):
    ''' Dissolve selected edges and vertices, limited by the angle of surrounding geometry

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param angle_limit: Max Angle, Angle limit
    :type angle_limit: typing.Optional[typing.Any]
    :param use_dissolve_boundaries: All Boundaries, Dissolve all vertices in between face boundaries
    :type use_dissolve_boundaries: typing.Optional[typing.Union[bool, typing.Any]]
    :param delimit: Delimit, Delimit dissolve operation
    :type delimit: typing.Optional[typing.Any]
    '''

    pass


def dissolve_mode(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_verts: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_face_split: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        use_boundary_tear: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False):
    ''' Dissolve geometry based on the selection mode

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_verts: Dissolve Vertices, Dissolve remaining vertices
    :type use_verts: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces
    :type use_boundary_tear: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def dissolve_verts(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_face_split: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        use_boundary_tear: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False):
    ''' Dissolve vertices, merge edges and faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces
    :type use_boundary_tear: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def dupli_extrude_cursor(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        rotate_source: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Duplicate and extrude selected vertices, edges or faces towards the mouse cursor

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param rotate_source: Rotate Source, Rotate initial selection giving better shape
    :type rotate_source: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def duplicate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 1):
    ''' Duplicate selected vertices, edges or faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def duplicate_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        MESH_OT_duplicate: typing.Optional['duplicate'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Duplicate mesh and move

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param MESH_OT_duplicate: Duplicate, Duplicate selected vertices, edges or faces
    :type MESH_OT_duplicate: typing.Optional['duplicate']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def edge_collapse(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Collapse isolated edge and face regions, merging data such as UVs and color attributes. This can collapse edge-rings as well as regions of connected faces into vertices

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def edge_face_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add an edge or face to selected

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def edge_rotate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_ccw: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Rotate selected edge or adjoining faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_ccw: Counter Clockwise
    :type use_ccw: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def edge_split(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'EDGE'):
    ''' Split selected edges so that each neighbor face gets its own copy

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type, Method to use for splitting * ``EDGE`` Faces by Edges -- Split faces along selected edges. * ``VERT`` Faces & Edges by Vertices -- Split faces and edges connected to selected vertices.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def edgering_select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False,
        deselect: typing.Optional[typing.Union[bool, typing.Any]] = False,
        toggle: typing.Optional[typing.Union[bool, typing.Any]] = False,
        ring: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Select an edge ring

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend the selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    :param deselect: Deselect, Remove from the selection
    :type deselect: typing.Optional[typing.Union[bool, typing.Any]]
    :param toggle: Toggle Select, Toggle the selection
    :type toggle: typing.Optional[typing.Union[bool, typing.Any]]
    :param ring: Select Ring, Select ring
    :type ring: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def edges_select_sharp(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        sharpness: typing.Optional[typing.Any] = 0.523599):
    ''' Select all sharp enough edges

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param sharpness: Sharpness
    :type sharpness: typing.Optional[typing.Any]
    '''

    pass


def extrude_context(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_normal_flip: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        use_dissolve_ortho_edges: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = False,
        mirror: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Extrude selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_dissolve_ortho_edges: Dissolve Orthogonal Edges
    :type use_dissolve_ortho_edges: typing.Optional[typing.Union[bool, typing.Any]]
    :param mirror: Mirror Editing
    :type mirror: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def extrude_context_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        MESH_OT_extrude_context: typing.Optional['extrude_context'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Extrude region together along the average normal

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param MESH_OT_extrude_context: Extrude Context, Extrude selection
    :type MESH_OT_extrude_context: typing.Optional['extrude_context']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def extrude_edges_indiv(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_normal_flip: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        mirror: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Extrude individual edges only

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: typing.Optional[typing.Union[bool, typing.Any]]
    :param mirror: Mirror Editing
    :type mirror: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def extrude_edges_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        MESH_OT_extrude_edges_indiv: typing.
        Optional['extrude_edges_indiv'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Extrude edges and move result

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only
    :type MESH_OT_extrude_edges_indiv: typing.Optional['extrude_edges_indiv']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def extrude_faces_indiv(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mirror: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Extrude individual faces only

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mirror: Mirror Editing
    :type mirror: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def extrude_faces_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        MESH_OT_extrude_faces_indiv: typing.
        Optional['extrude_faces_indiv'] = None,
        TRANSFORM_OT_shrink_fatten: typing.
        Optional['bpy.ops.transform.shrink_fatten'] = None):
    ''' Extrude each individual face separately along local normals

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param MESH_OT_extrude_faces_indiv: Extrude Individual Faces, Extrude individual faces only
    :type MESH_OT_extrude_faces_indiv: typing.Optional['extrude_faces_indiv']
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals
    :type TRANSFORM_OT_shrink_fatten: typing.Optional['bpy.ops.transform.shrink_fatten']
    '''

    pass


def extrude_manifold(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        MESH_OT_extrude_region: typing.Optional['extrude_region'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Extrude, dissolves edges whose faces form a flat surface and intersect new edges

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :type MESH_OT_extrude_region: typing.Optional['extrude_region']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def extrude_region(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_normal_flip: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        use_dissolve_ortho_edges: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = False,
        mirror: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Extrude region of faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_dissolve_ortho_edges: Dissolve Orthogonal Edges
    :type use_dissolve_ortho_edges: typing.Optional[typing.Union[bool, typing.Any]]
    :param mirror: Mirror Editing
    :type mirror: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def extrude_region_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        MESH_OT_extrude_region: typing.Optional['extrude_region'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Extrude region and move result

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :type MESH_OT_extrude_region: typing.Optional['extrude_region']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def extrude_region_shrink_fatten(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        MESH_OT_extrude_region: typing.Optional['extrude_region'] = None,
        TRANSFORM_OT_shrink_fatten: typing.
        Optional['bpy.ops.transform.shrink_fatten'] = None):
    ''' Extrude region together along local normals

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :type MESH_OT_extrude_region: typing.Optional['extrude_region']
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals
    :type TRANSFORM_OT_shrink_fatten: typing.Optional['bpy.ops.transform.shrink_fatten']
    '''

    pass


def extrude_repeat(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        steps: typing.Optional[typing.Any] = 10,
        offset: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale_offset: typing.Optional[typing.Any] = 1.0):
    ''' Extrude selected vertices, edges or faces repeatedly

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param steps: Steps
    :type steps: typing.Optional[typing.Any]
    :param offset: Offset, Offset vector
    :type offset: typing.Optional[typing.Any]
    :param scale_offset: Scale Offset
    :type scale_offset: typing.Optional[typing.Any]
    '''

    pass


def extrude_vertices_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        MESH_OT_extrude_verts_indiv: typing.
        Optional['extrude_verts_indiv'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Extrude vertices and move result

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param MESH_OT_extrude_verts_indiv: Extrude Only Vertices, Extrude individual vertices only
    :type MESH_OT_extrude_verts_indiv: typing.Optional['extrude_verts_indiv']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def extrude_verts_indiv(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mirror: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Extrude individual vertices only

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mirror: Mirror Editing
    :type mirror: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def face_make_planar(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 1.0,
        repeat: typing.Optional[typing.Any] = 1):
    ''' Flatten selected faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor
    :type factor: typing.Optional[typing.Any]
    :param repeat: Iterations
    :type repeat: typing.Optional[typing.Any]
    '''

    pass


def face_set_extract(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        add_boundary_loop: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        smooth_iterations: typing.Optional[typing.Any] = 4,
        apply_shrinkwrap: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        add_solidify: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Create a new mesh object from the selected Face Set

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param add_boundary_loop: Add Boundary Loop, Add an extra edge loop to better preserve the shape when applying a subdivision surface modifier
    :type add_boundary_loop: typing.Optional[typing.Union[bool, typing.Any]]
    :param smooth_iterations: Smooth Iterations, Smooth iterations applied to the extracted mesh
    :type smooth_iterations: typing.Optional[typing.Any]
    :param apply_shrinkwrap: Project to Sculpt, Project the extracted mesh into the original sculpt
    :type apply_shrinkwrap: typing.Optional[typing.Union[bool, typing.Any]]
    :param add_solidify: Extract as Solid, Extract the mask as a solid object with a solidify modifier
    :type add_solidify: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def face_split_by_edges(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Weld loose edges into faces (splitting them into new faces)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def faces_mirror_uv(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        direction: typing.Optional[typing.Any] = 'POSITIVE',
        precision: typing.Optional[typing.Any] = 3):
    ''' Copy mirror UV coordinates on the X axis based on a mirrored mesh :File: `startup/bl_operators/mesh.py\:130 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/mesh.py#L130>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param direction: Axis Direction
    :type direction: typing.Optional[typing.Any]
    :param precision: Precision, Tolerance for finding vertex duplicates
    :type precision: typing.Optional[typing.Any]
    '''

    pass


def faces_select_linked_flat(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        sharpness: typing.Optional[typing.Any] = 0.0174533):
    ''' Select linked faces by angle

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param sharpness: Sharpness
    :type sharpness: typing.Optional[typing.Any]
    '''

    pass


def faces_shade_flat(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Display faces flat

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def faces_shade_smooth(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Display faces smooth (using vertex normals)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def fill(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         use_beauty: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Fill a selected edge loop with faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_beauty: Beauty, Use best triangulation division
    :type use_beauty: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def fill_grid(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        span: typing.Optional[typing.Any] = 1,
        offset: typing.Optional[typing.Any] = 0,
        use_interp_simple: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False):
    ''' Fill grid from two loops

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param span: Span, Number of grid columns
    :type span: typing.Optional[typing.Any]
    :param offset: Offset, Vertex that is the corner of the grid
    :type offset: typing.Optional[typing.Any]
    :param use_interp_simple: Simple Blending, Use simple interpolation of grid vertices
    :type use_interp_simple: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def fill_holes(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        sides: typing.Optional[typing.Any] = 4):
    ''' Fill in holes (boundary edge loops)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param sides: Sides, Number of sides in hole required to fill (zero fills all holes)
    :type sides: typing.Optional[typing.Any]
    '''

    pass


def flip_normals(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        only_clnors: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Flip the direction of selected faces' normals (and of their vertices)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param only_clnors: Custom Normals Only, Only flip the custom loop normals of the selected elements
    :type only_clnors: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def flip_quad_tessellation(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Flips the tessellation of selected quads

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def hide(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         unselected: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Hide (un)selected vertices, edges or faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def inset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_boundary: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_even_offset: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True,
        use_relative_offset: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = False,
        use_edge_rail: typing.Optional[typing.Union[bool, typing.Any]] = False,
        thickness: typing.Optional[typing.Any] = 0.0,
        depth: typing.Optional[typing.Any] = 0.0,
        use_outset: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_select_inset: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        use_individual: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        use_interpolate: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True,
        release_confirm: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False):
    ''' Inset new faces into selected faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_boundary: Boundary, Inset face boundaries
    :type use_boundary: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :type use_even_offset: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
    :type use_relative_offset: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_edge_rail: Edge Rail, Inset the region along existing edges
    :type use_edge_rail: typing.Optional[typing.Union[bool, typing.Any]]
    :param thickness: Thickness
    :type thickness: typing.Optional[typing.Any]
    :param depth: Depth
    :type depth: typing.Optional[typing.Any]
    :param use_outset: Outset, Outset rather than inset
    :type use_outset: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_select_inset: Select Outer, Select the new inset faces
    :type use_select_inset: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_individual: Individual, Individual face inset
    :type use_individual: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_interpolate: Interpolate, Blend face data across the inset
    :type use_interpolate: typing.Optional[typing.Union[bool, typing.Any]]
    :param release_confirm: Confirm on Release
    :type release_confirm: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def intersect(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'SELECT_UNSELECT',
        separate_mode: typing.Optional[typing.Any] = 'CUT',
        threshold: typing.Optional[typing.Any] = 1e-06,
        solver: typing.Optional[typing.Any] = 'EXACT'):
    ''' Cut an intersection into faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Source * ``SELECT`` Self Intersect -- Self intersect selected faces. * ``SELECT_UNSELECT`` Selected/Unselected -- Intersect selected with unselected faces.
    :type mode: typing.Optional[typing.Any]
    :param separate_mode: Separate Mode * ``ALL`` All -- Separate all geometry from intersections. * ``CUT`` Cut -- Cut into geometry keeping each side separate (Selected/Unselected only). * ``NONE`` Merge -- Merge all geometry from the intersection.
    :type separate_mode: typing.Optional[typing.Any]
    :param threshold: Merge Threshold
    :type threshold: typing.Optional[typing.Any]
    :param solver: Solver, Which Intersect solver to use * ``FAST`` Fast -- Faster solver, some limitations. * ``EXACT`` Exact -- Exact solver, slower, handles more cases.
    :type solver: typing.Optional[typing.Any]
    '''

    pass


def intersect_boolean(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        operation: typing.Optional[typing.Any] = 'DIFFERENCE',
        use_swap: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_self: typing.Optional[typing.Union[bool, typing.Any]] = False,
        threshold: typing.Optional[typing.Any] = 1e-06,
        solver: typing.Optional[typing.Any] = 'EXACT'):
    ''' Cut solid geometry from selected to unselected

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param operation: Boolean Operation, Which boolean operation to apply
    :type operation: typing.Optional[typing.Any]
    :param use_swap: Swap, Use with difference intersection to swap which side is kept
    :type use_swap: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_self: Self Intersection, Do self-union or self-intersection
    :type use_self: typing.Optional[typing.Union[bool, typing.Any]]
    :param threshold: Merge Threshold
    :type threshold: typing.Optional[typing.Any]
    :param solver: Solver, Which Boolean solver to use * ``FAST`` Fast -- Faster solver, some limitations. * ``EXACT`` Exact -- Exact solver, slower, handles more cases.
    :type solver: typing.Optional[typing.Any]
    '''

    pass


def knife_project(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        cut_through: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Use other objects outlines and boundaries to project knife cuts

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param cut_through: Cut Through, Cut through all faces, not just visible ones
    :type cut_through: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def knife_tool(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_occlude_geometry: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = True,
        only_selected: typing.Optional[typing.Union[bool, typing.Any]] = False,
        xray: typing.Optional[typing.Union[bool, typing.Any]] = True,
        visible_measurements: typing.Optional[typing.Any] = 'NONE',
        angle_snapping: typing.Optional[typing.Any] = 'NONE',
        angle_snapping_increment: typing.Optional[typing.Any] = 0.523599,
        wait_for_input: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = True):
    ''' Cut new topology

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_occlude_geometry: Occlude Geometry, Only cut the front most geometry
    :type use_occlude_geometry: typing.Optional[typing.Union[bool, typing.Any]]
    :param only_selected: Only Selected, Only cut selected geometry
    :type only_selected: typing.Optional[typing.Union[bool, typing.Any]]
    :param xray: X-Ray, Show cuts hidden by geometry
    :type xray: typing.Optional[typing.Union[bool, typing.Any]]
    :param visible_measurements: Measurements, Visible distance and angle measurements * ``NONE`` None -- Show no measurements. * ``BOTH`` Both -- Show both distances and angles. * ``DISTANCE`` Distance -- Show just distance measurements. * ``ANGLE`` Angle -- Show just angle measurements.
    :type visible_measurements: typing.Optional[typing.Any]
    :param angle_snapping: Angle Snapping, Angle snapping mode * ``NONE`` None -- No angle snapping. * ``SCREEN`` Screen -- Screen space angle snapping. * ``RELATIVE`` Relative -- Angle snapping relative to the previous cut edge.
    :type angle_snapping: typing.Optional[typing.Any]
    :param angle_snapping_increment: Angle Snap Increment, The angle snap increment used when in constrained angle mode
    :type angle_snapping_increment: typing.Optional[typing.Any]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def loop_multi_select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        ring: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select a loop of connected edges by connection type

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param ring: Ring
    :type ring: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def loop_select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False,
        deselect: typing.Optional[typing.Union[bool, typing.Any]] = False,
        toggle: typing.Optional[typing.Union[bool, typing.Any]] = False,
        ring: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select a loop of connected edges

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend Select, Extend the selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    :param deselect: Deselect, Remove from the selection
    :type deselect: typing.Optional[typing.Union[bool, typing.Any]]
    :param toggle: Toggle Select, Toggle the selection
    :type toggle: typing.Optional[typing.Union[bool, typing.Any]]
    :param ring: Select Ring, Select ring
    :type ring: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def loop_to_region(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        select_bigger: typing.Optional[typing.Union[bool, typing.
                                                    Any]] = False):
    ''' Select region of faces inside of a selected loop of edges

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param select_bigger: Select Bigger, Select bigger regions instead of smaller ones
    :type select_bigger: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def loopcut(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        number_cuts: typing.Optional[typing.Any] = 1,
        smoothness: typing.Optional[typing.Any] = 0.0,
        falloff: typing.Optional[typing.Union[str, int]] = 'INVERSE_SQUARE',
        object_index: typing.Optional[typing.Any] = -1,
        edge_index: typing.Optional[typing.Any] = -1,
        mesh_select_mode_init: typing.Optional[
            typing.Union[typing.List[bool], typing.Any]] = (False, False,
                                                            False)):
    ''' Add a new loop between existing loops

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param number_cuts: Number of Cuts
    :type number_cuts: typing.Optional[typing.Any]
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: typing.Optional[typing.Any]
    :param falloff: Falloff, Falloff type of the feather
    :type falloff: typing.Optional[typing.Union[str, int]]
    :param object_index: Object Index
    :type object_index: typing.Optional[typing.Any]
    :param edge_index: Edge Index
    :type edge_index: typing.Optional[typing.Any]
    :type mesh_select_mode_init: typing.Optional[typing.Union[typing.List[bool], typing.Any]]
    '''

    pass


def loopcut_slide(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        MESH_OT_loopcut: typing.Optional['loopcut'] = None,
        TRANSFORM_OT_edge_slide: typing.
        Optional['bpy.ops.transform.edge_slide'] = None):
    ''' Cut mesh loop and slide it

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param MESH_OT_loopcut: Loop Cut, Add a new loop between existing loops
    :type MESH_OT_loopcut: typing.Optional['loopcut']
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh
    :type TRANSFORM_OT_edge_slide: typing.Optional['bpy.ops.transform.edge_slide']
    '''

    pass


def mark_freestyle_edge(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        clear: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' (Un)mark selected edges as Freestyle feature edges

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param clear: Clear
    :type clear: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def mark_freestyle_face(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        clear: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' (Un)mark selected faces for exclusion from Freestyle feature edge detection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param clear: Clear
    :type clear: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def mark_seam(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        clear: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' (Un)mark selected edges as a seam

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param clear: Clear
    :type clear: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def mark_sharp(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        clear: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_verts: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' (Un)mark selected edges as sharp

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param clear: Clear
    :type clear: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_verts: Vertices, Consider vertices instead of edges to select which edges to (un)tag as sharp
    :type use_verts: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def merge(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None,
          *,
          type: typing.Optional[typing.Any] = 'CENTER',
          uvs: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Merge selected vertices

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type, Merge method to use
    :type type: typing.Optional[typing.Any]
    :param uvs: UVs, Move UVs according to merge
    :type uvs: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def merge_normals(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Merge custom normals of selected vertices

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def mod_weighted_strength(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        set: typing.Optional[typing.Union[bool, typing.Any]] = False,
        face_strength: typing.Optional[typing.Any] = 'MEDIUM'):
    ''' Set/Get strength of face (used in Weighted Normal modifier)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param set: Set Value, Set value of faces
    :type set: typing.Optional[typing.Union[bool, typing.Any]]
    :param face_strength: Face Strength, Strength to use for assigning or selecting face influence for weighted normal modifier
    :type face_strength: typing.Optional[typing.Any]
    '''

    pass


def normals_make_consistent(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        inside: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Make face and vertex normals point either outside or inside the mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param inside: Inside
    :type inside: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def normals_tools(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'COPY',
        absolute: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Custom normals tools using Normal Vector of UI

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode, Mode of tools taking input from interface * ``COPY`` Copy Normal -- Copy normal to the internal clipboard. * ``PASTE`` Paste Normal -- Paste normal from the internal clipboard. * ``ADD`` Add Normal -- Add normal vector with selection. * ``MULTIPLY`` Multiply Normal -- Multiply normal vector with selection. * ``RESET`` Reset Normal -- Reset the internal clipboard and/or normal of selected element.
    :type mode: typing.Optional[typing.Any]
    :param absolute: Absolute Coordinates, Copy Absolute coordinates or Normal vector
    :type absolute: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def offset_edge_loops(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_cap_endpoint: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False):
    ''' Create offset edge loop from the current selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_cap_endpoint: Cap Endpoint, Extend loop around end-points
    :type use_cap_endpoint: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def offset_edge_loops_slide(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        MESH_OT_offset_edge_loops: typing.Optional['offset_edge_loops'] = None,
        TRANSFORM_OT_edge_slide: typing.
        Optional['bpy.ops.transform.edge_slide'] = None):
    ''' Offset edge loop slide

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param MESH_OT_offset_edge_loops: Offset Edge Loop, Create offset edge loop from the current selection
    :type MESH_OT_offset_edge_loops: typing.Optional['offset_edge_loops']
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh
    :type TRANSFORM_OT_edge_slide: typing.Optional['bpy.ops.transform.edge_slide']
    '''

    pass


def paint_mask_extract(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mask_threshold: typing.Optional[typing.Any] = 0.5,
        add_boundary_loop: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        smooth_iterations: typing.Optional[typing.Any] = 4,
        apply_shrinkwrap: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        add_solidify: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Create a new mesh object from the current paint mask

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mask_threshold: Threshold, Minimum mask value to consider the vertex valid to extract a face from the original mesh
    :type mask_threshold: typing.Optional[typing.Any]
    :param add_boundary_loop: Add Boundary Loop, Add an extra edge loop to better preserve the shape when applying a subdivision surface modifier
    :type add_boundary_loop: typing.Optional[typing.Union[bool, typing.Any]]
    :param smooth_iterations: Smooth Iterations, Smooth iterations applied to the extracted mesh
    :type smooth_iterations: typing.Optional[typing.Any]
    :param apply_shrinkwrap: Project to Sculpt, Project the extracted mesh into the original sculpt
    :type apply_shrinkwrap: typing.Optional[typing.Union[bool, typing.Any]]
    :param add_solidify: Extract as Solid, Extract the mask as a solid object with a solidify modifier
    :type add_solidify: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def paint_mask_slice(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mask_threshold: typing.Optional[typing.Any] = 0.5,
        fill_holes: typing.Optional[typing.Union[bool, typing.Any]] = True,
        new_object: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Slices the paint mask from the mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mask_threshold: Threshold, Minimum mask value to consider the vertex valid to extract a face from the original mesh
    :type mask_threshold: typing.Optional[typing.Any]
    :param fill_holes: Fill Holes, Fill holes after slicing the mask
    :type fill_holes: typing.Optional[typing.Union[bool, typing.Any]]
    :param new_object: Slice to New Object, Create a new object from the sliced mask
    :type new_object: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def point_normals(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'COORDINATES',
        invert: typing.Optional[typing.Union[bool, typing.Any]] = False,
        align: typing.Optional[typing.Union[bool, typing.Any]] = False,
        target_location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        spherize: typing.Optional[typing.Union[bool, typing.Any]] = False,
        spherize_strength: typing.Optional[typing.Any] = 0.1):
    ''' Point selected custom normals to specified Target

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode, How to define coordinates to point custom normals to * ``COORDINATES`` Coordinates -- Use static coordinates (defined by various means). * ``MOUSE`` Mouse -- Follow mouse cursor.
    :type mode: typing.Optional[typing.Any]
    :param invert: Invert, Invert affected normals
    :type invert: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, Make all affected normals parallel
    :type align: typing.Optional[typing.Union[bool, typing.Any]]
    :param target_location: Target, Target location to which normals will point
    :type target_location: typing.Optional[typing.Any]
    :param spherize: Spherize, Interpolate between original and new normals
    :type spherize: typing.Optional[typing.Union[bool, typing.Any]]
    :param spherize_strength: Spherize Strength, Ratio of spherized normal to original normal
    :type spherize_strength: typing.Optional[typing.Any]
    '''

    pass


def poke(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         offset: typing.Optional[typing.Any] = 0.0,
         use_relative_offset: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
         center_mode: typing.Optional[typing.Any] = 'MEDIAN_WEIGHTED'):
    ''' Split a face into a fan

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param offset: Poke Offset, Poke Offset
    :type offset: typing.Optional[typing.Any]
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
    :type use_relative_offset: typing.Optional[typing.Union[bool, typing.Any]]
    :param center_mode: Poke Center, Poke face center calculation * ``MEDIAN_WEIGHTED`` Weighted Median -- Weighted median face center. * ``MEDIAN`` Median -- Median face center. * ``BOUNDS`` Bounds -- Face bounds center.
    :type center_mode: typing.Optional[typing.Any]
    '''

    pass


def polybuild_delete_at_cursor(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mirror: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_proportional_edit: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
        proportional_edit_falloff: typing.Optional[typing.
                                                   Union[str, int]] = 'SMOOTH',
        proportional_size: typing.Optional[typing.Any] = 1.0,
        use_proportional_connected: typing.Optional[typing.Union[bool, typing.
                                                                 Any]] = False,
        use_proportional_projected: typing.Optional[typing.Union[bool, typing.
                                                                 Any]] = False,
        release_confirm: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        use_accurate: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mirror: Mirror Editing
    :type mirror: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: typing.Optional[typing.Union[bool, typing.Any]]
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Optional[typing.Union[str, int]]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param use_proportional_connected: Connected
    :type use_proportional_connected: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: typing.Optional[typing.Union[bool, typing.Any]]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def polybuild_dissolve_at_cursor(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def polybuild_extrude_at_cursor_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        MESH_OT_polybuild_transform_at_cursor: typing.
        Optional['polybuild_transform_at_cursor'] = None,
        MESH_OT_extrude_edges_indiv: typing.
        Optional['extrude_edges_indiv'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor
    :type MESH_OT_polybuild_transform_at_cursor: typing.Optional['polybuild_transform_at_cursor']
    :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only
    :type MESH_OT_extrude_edges_indiv: typing.Optional['extrude_edges_indiv']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def polybuild_face_at_cursor(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        create_quads: typing.Optional[typing.Union[bool, typing.Any]] = True,
        mirror: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_proportional_edit: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
        proportional_edit_falloff: typing.Optional[typing.
                                                   Union[str, int]] = 'SMOOTH',
        proportional_size: typing.Optional[typing.Any] = 1.0,
        use_proportional_connected: typing.Optional[typing.Union[bool, typing.
                                                                 Any]] = False,
        use_proportional_projected: typing.Optional[typing.Union[bool, typing.
                                                                 Any]] = False,
        release_confirm: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        use_accurate: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param create_quads: Create Quads, Automatically split edges in triangles to maintain quad topology
    :type create_quads: typing.Optional[typing.Union[bool, typing.Any]]
    :param mirror: Mirror Editing
    :type mirror: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: typing.Optional[typing.Union[bool, typing.Any]]
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Optional[typing.Union[str, int]]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param use_proportional_connected: Connected
    :type use_proportional_connected: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: typing.Optional[typing.Union[bool, typing.Any]]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def polybuild_face_at_cursor_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        MESH_OT_polybuild_face_at_cursor: typing.
        Optional['polybuild_face_at_cursor'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param MESH_OT_polybuild_face_at_cursor: Poly Build Face at Cursor
    :type MESH_OT_polybuild_face_at_cursor: typing.Optional['polybuild_face_at_cursor']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def polybuild_split_at_cursor(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mirror: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_proportional_edit: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
        proportional_edit_falloff: typing.Optional[typing.
                                                   Union[str, int]] = 'SMOOTH',
        proportional_size: typing.Optional[typing.Any] = 1.0,
        use_proportional_connected: typing.Optional[typing.Union[bool, typing.
                                                                 Any]] = False,
        use_proportional_projected: typing.Optional[typing.Union[bool, typing.
                                                                 Any]] = False,
        release_confirm: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        use_accurate: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mirror: Mirror Editing
    :type mirror: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: typing.Optional[typing.Union[bool, typing.Any]]
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Optional[typing.Union[str, int]]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param use_proportional_connected: Connected
    :type use_proportional_connected: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: typing.Optional[typing.Union[bool, typing.Any]]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def polybuild_split_at_cursor_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        MESH_OT_polybuild_split_at_cursor: typing.
        Optional['polybuild_split_at_cursor'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param MESH_OT_polybuild_split_at_cursor: Poly Build Split at Cursor
    :type MESH_OT_polybuild_split_at_cursor: typing.Optional['polybuild_split_at_cursor']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def polybuild_transform_at_cursor(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mirror: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_proportional_edit: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
        proportional_edit_falloff: typing.Optional[typing.
                                                   Union[str, int]] = 'SMOOTH',
        proportional_size: typing.Optional[typing.Any] = 1.0,
        use_proportional_connected: typing.Optional[typing.Union[bool, typing.
                                                                 Any]] = False,
        use_proportional_projected: typing.Optional[typing.Union[bool, typing.
                                                                 Any]] = False,
        release_confirm: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        use_accurate: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mirror: Mirror Editing
    :type mirror: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: typing.Optional[typing.Union[bool, typing.Any]]
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Optional[typing.Union[str, int]]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param use_proportional_connected: Connected
    :type use_proportional_connected: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: typing.Optional[typing.Union[bool, typing.Any]]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def polybuild_transform_at_cursor_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        MESH_OT_polybuild_transform_at_cursor: typing.
        Optional['polybuild_transform_at_cursor'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor
    :type MESH_OT_polybuild_transform_at_cursor: typing.Optional['polybuild_transform_at_cursor']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def primitive_circle_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        vertices: typing.Optional[typing.Any] = 32,
        radius: typing.Optional[typing.Any] = 1.0,
        fill_type: typing.Optional[typing.Any] = 'NOTHING',
        calc_uvs: typing.Optional[typing.Union[bool, typing.Any]] = True,
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Construct a circle mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param vertices: Vertices
    :type vertices: typing.Optional[typing.Any]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param fill_type: Fill Type * ``NOTHING`` Nothing -- Don't fill at all. * ``NGON`` N-Gon -- Use n-gons. * ``TRIFAN`` Triangle Fan -- Use triangle fans.
    :type fill_type: typing.Optional[typing.Any]
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: typing.Optional[typing.Union[bool, typing.Any]]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def primitive_cone_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        vertices: typing.Optional[typing.Any] = 32,
        radius1: typing.Optional[typing.Any] = 1.0,
        radius2: typing.Optional[typing.Any] = 0.0,
        depth: typing.Optional[typing.Any] = 2.0,
        end_fill_type: typing.Optional[typing.Any] = 'NGON',
        calc_uvs: typing.Optional[typing.Union[bool, typing.Any]] = True,
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Construct a conic mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param vertices: Vertices
    :type vertices: typing.Optional[typing.Any]
    :param radius1: Radius 1
    :type radius1: typing.Optional[typing.Any]
    :param radius2: Radius 2
    :type radius2: typing.Optional[typing.Any]
    :param depth: Depth
    :type depth: typing.Optional[typing.Any]
    :param end_fill_type: Base Fill Type * ``NOTHING`` Nothing -- Don't fill at all. * ``NGON`` N-Gon -- Use n-gons. * ``TRIFAN`` Triangle Fan -- Use triangle fans.
    :type end_fill_type: typing.Optional[typing.Any]
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: typing.Optional[typing.Union[bool, typing.Any]]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def primitive_cube_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        size: typing.Optional[typing.Any] = 2.0,
        calc_uvs: typing.Optional[typing.Union[bool, typing.Any]] = True,
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Construct a cube mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param size: Size
    :type size: typing.Optional[typing.Any]
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: typing.Optional[typing.Union[bool, typing.Any]]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def primitive_cube_add_gizmo(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        calc_uvs: typing.Optional[typing.Union[bool, typing.Any]] = True,
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        matrix: typing.Optional[typing.Any] = ((0.0, 0.0, 0.0,
                                                0.0), (0.0, 0.0, 0.0, 0.0),
                                               (0.0, 0.0, 0.0,
                                                0.0), (0.0, 0.0, 0.0, 0.0))):
    ''' Construct a cube mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: typing.Optional[typing.Union[bool, typing.Any]]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    :param matrix: Matrix
    :type matrix: typing.Optional[typing.Any]
    '''

    pass


def primitive_cylinder_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        vertices: typing.Optional[typing.Any] = 32,
        radius: typing.Optional[typing.Any] = 1.0,
        depth: typing.Optional[typing.Any] = 2.0,
        end_fill_type: typing.Optional[typing.Any] = 'NGON',
        calc_uvs: typing.Optional[typing.Union[bool, typing.Any]] = True,
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Construct a cylinder mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param vertices: Vertices
    :type vertices: typing.Optional[typing.Any]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param depth: Depth
    :type depth: typing.Optional[typing.Any]
    :param end_fill_type: Cap Fill Type * ``NOTHING`` Nothing -- Don't fill at all. * ``NGON`` N-Gon -- Use n-gons. * ``TRIFAN`` Triangle Fan -- Use triangle fans.
    :type end_fill_type: typing.Optional[typing.Any]
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: typing.Optional[typing.Union[bool, typing.Any]]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def primitive_grid_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        x_subdivisions: typing.Optional[typing.Any] = 10,
        y_subdivisions: typing.Optional[typing.Any] = 10,
        size: typing.Optional[typing.Any] = 2.0,
        calc_uvs: typing.Optional[typing.Union[bool, typing.Any]] = True,
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Construct a grid mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param x_subdivisions: X Subdivisions
    :type x_subdivisions: typing.Optional[typing.Any]
    :param y_subdivisions: Y Subdivisions
    :type y_subdivisions: typing.Optional[typing.Any]
    :param size: Size
    :type size: typing.Optional[typing.Any]
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: typing.Optional[typing.Union[bool, typing.Any]]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def primitive_ico_sphere_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        subdivisions: typing.Optional[typing.Any] = 2,
        radius: typing.Optional[typing.Any] = 1.0,
        calc_uvs: typing.Optional[typing.Union[bool, typing.Any]] = True,
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Construct an Icosphere mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param subdivisions: Subdivisions
    :type subdivisions: typing.Optional[typing.Any]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: typing.Optional[typing.Union[bool, typing.Any]]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def primitive_monkey_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        size: typing.Optional[typing.Any] = 2.0,
        calc_uvs: typing.Optional[typing.Union[bool, typing.Any]] = True,
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Construct a Suzanne mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param size: Size
    :type size: typing.Optional[typing.Any]
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: typing.Optional[typing.Union[bool, typing.Any]]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def primitive_plane_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        size: typing.Optional[typing.Any] = 2.0,
        calc_uvs: typing.Optional[typing.Union[bool, typing.Any]] = True,
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Construct a filled planar mesh with 4 vertices

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param size: Size
    :type size: typing.Optional[typing.Any]
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: typing.Optional[typing.Union[bool, typing.Any]]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def primitive_torus_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        major_segments: typing.Optional[typing.Any] = 48,
        minor_segments: typing.Optional[typing.Any] = 12,
        mode: typing.Optional[typing.Any] = 'MAJOR_MINOR',
        major_radius: typing.Optional[typing.Any] = 1.0,
        minor_radius: typing.Optional[typing.Any] = 0.25,
        abso_major_rad: typing.Optional[typing.Any] = 1.25,
        abso_minor_rad: typing.Optional[typing.Any] = 0.75,
        generate_uvs: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Construct a torus mesh :File: `startup/bl_operators/add_mesh_torus.py\:220 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/add_mesh_torus.py#L220>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param align: Align * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation
    :type rotation: typing.Optional[typing.Any]
    :param major_segments: Major Segments, Number of segments for the main ring of the torus
    :type major_segments: typing.Optional[typing.Any]
    :param minor_segments: Minor Segments, Number of segments for the minor ring of the torus
    :type minor_segments: typing.Optional[typing.Any]
    :param mode: Dimensions Mode * ``MAJOR_MINOR`` Major/Minor -- Use the major/minor radii for torus dimensions. * ``EXT_INT`` Exterior/Interior -- Use the exterior/interior radii for torus dimensions.
    :type mode: typing.Optional[typing.Any]
    :param major_radius: Major Radius, Radius from the origin to the center of the cross sections
    :type major_radius: typing.Optional[typing.Any]
    :param minor_radius: Minor Radius, Radius of the torus' cross section
    :type minor_radius: typing.Optional[typing.Any]
    :param abso_major_rad: Exterior Radius, Total Exterior Radius of the torus
    :type abso_major_rad: typing.Optional[typing.Any]
    :param abso_minor_rad: Interior Radius, Total Interior Radius of the torus
    :type abso_minor_rad: typing.Optional[typing.Any]
    :param generate_uvs: Generate UVs, Generate a default UV map
    :type generate_uvs: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def primitive_uv_sphere_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        segments: typing.Optional[typing.Any] = 32,
        ring_count: typing.Optional[typing.Any] = 16,
        radius: typing.Optional[typing.Any] = 1.0,
        calc_uvs: typing.Optional[typing.Union[bool, typing.Any]] = True,
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Construct a UV sphere mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param segments: Segments
    :type segments: typing.Optional[typing.Any]
    :param ring_count: Rings
    :type ring_count: typing.Optional[typing.Any]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: typing.Optional[typing.Union[bool, typing.Any]]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def quads_convert_to_tris(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        quad_method: typing.Optional[typing.Union[str, int]] = 'BEAUTY',
        ngon_method: typing.Optional[typing.Union[str, int]] = 'BEAUTY'):
    ''' Triangulate selected faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param quad_method: Quad Method, Method for splitting the quads into triangles
    :type quad_method: typing.Optional[typing.Union[str, int]]
    :param ngon_method: N-gon Method, Method for splitting the n-gons into triangles
    :type ngon_method: typing.Optional[typing.Union[str, int]]
    '''

    pass


def region_to_loop(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select boundary edges around the selected faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def remove_doubles(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        threshold: typing.Optional[typing.Any] = 0.0001,
        use_unselected: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        use_sharp_edge_from_normals: typing.Optional[
            typing.Union[bool, typing.Any]] = False):
    ''' Merge vertices based on their proximity

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param threshold: Merge Distance, Maximum distance between elements to merge
    :type threshold: typing.Optional[typing.Any]
    :param use_unselected: Unselected, Merge selected to other unselected vertices
    :type use_unselected: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_sharp_edge_from_normals: Sharp Edges, Calculate sharp edges using custom normal data (when available)
    :type use_sharp_edge_from_normals: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def reveal(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None,
           *,
           select: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Reveal all hidden vertices, edges and faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param select: Select
    :type select: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def rip(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mirror: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_proportional_edit: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
        proportional_edit_falloff: typing.Optional[typing.
                                                   Union[str, int]] = 'SMOOTH',
        proportional_size: typing.Optional[typing.Any] = 1.0,
        use_proportional_connected: typing.Optional[typing.Union[bool, typing.
                                                                 Any]] = False,
        use_proportional_projected: typing.Optional[typing.Union[bool, typing.
                                                                 Any]] = False,
        release_confirm: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        use_accurate: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_fill: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Disconnect vertex or edges from connected geometry

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mirror: Mirror Editing
    :type mirror: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: typing.Optional[typing.Union[bool, typing.Any]]
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Optional[typing.Union[str, int]]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param use_proportional_connected: Connected
    :type use_proportional_connected: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: typing.Optional[typing.Union[bool, typing.Any]]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_fill: Fill, Fill the ripped region
    :type use_fill: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def rip_edge(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mirror: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_proportional_edit: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
        proportional_edit_falloff: typing.Optional[typing.
                                                   Union[str, int]] = 'SMOOTH',
        proportional_size: typing.Optional[typing.Any] = 1.0,
        use_proportional_connected: typing.Optional[typing.Union[bool, typing.
                                                                 Any]] = False,
        use_proportional_projected: typing.Optional[typing.Union[bool, typing.
                                                                 Any]] = False,
        release_confirm: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        use_accurate: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Extend vertices along the edge closest to the cursor

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mirror: Mirror Editing
    :type mirror: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: typing.Optional[typing.Union[bool, typing.Any]]
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: typing.Optional[typing.Union[str, int]]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param use_proportional_connected: Connected
    :type use_proportional_connected: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: typing.Optional[typing.Union[bool, typing.Any]]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def rip_edge_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        MESH_OT_rip_edge: typing.Optional['rip_edge'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Extend vertices and move the result

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param MESH_OT_rip_edge: Extend Vertices, Extend vertices along the edge closest to the cursor
    :type MESH_OT_rip_edge: typing.Optional['rip_edge']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def rip_move(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None,
             *,
             MESH_OT_rip: typing.Optional['rip'] = None,
             TRANSFORM_OT_translate: typing.
             Optional['bpy.ops.transform.translate'] = None):
    ''' Rip polygons and move the result

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param MESH_OT_rip: Rip, Disconnect vertex or edges from connected geometry
    :type MESH_OT_rip: typing.Optional['rip']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def screw(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None,
          *,
          steps: typing.Optional[typing.Any] = 9,
          turns: typing.Optional[typing.Any] = 1,
          center: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
          axis: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Extrude selected vertices in screw-shaped rotation around the cursor in indicated viewport

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param steps: Steps, Steps
    :type steps: typing.Optional[typing.Any]
    :param turns: Turns, Turns
    :type turns: typing.Optional[typing.Any]
    :param center: Center, Center in global view space
    :type center: typing.Optional[typing.Any]
    :param axis: Axis, Axis in global view space
    :type axis: typing.Optional[typing.Any]
    '''

    pass


def select_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' (De)select all vertices, edges or faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param action: Action, Selection action to execute * ``TOGGLE`` Toggle -- Toggle selection for all elements. * ``SELECT`` Select -- Select all elements. * ``DESELECT`` Deselect -- Deselect all elements. * ``INVERT`` Invert -- Invert selection of all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_axis(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        orientation: typing.Optional[typing.Union[str, int]] = 'LOCAL',
        sign: typing.Optional[typing.Any] = 'POS',
        axis: typing.Optional[typing.Union[str, int]] = 'X',
        threshold: typing.Optional[typing.Any] = 0.0001):
    ''' Select all data in the mesh on a single axis

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param orientation: Axis Mode, Axis orientation
    :type orientation: typing.Optional[typing.Union[str, int]]
    :param sign: Axis Sign, Side to select
    :type sign: typing.Optional[typing.Any]
    :param axis: Axis, Select the axis to compare each vertex on
    :type axis: typing.Optional[typing.Union[str, int]]
    :param threshold: Threshold
    :type threshold: typing.Optional[typing.Any]
    '''

    pass


def select_face_by_sides(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        number: typing.Optional[typing.Any] = 4,
        type: typing.Optional[typing.Any] = 'EQUAL',
        extend: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Select vertices or faces by the number of polygon sides

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param number: Number of Vertices
    :type number: typing.Optional[typing.Any]
    :param type: Type, Type of comparison to make
    :type type: typing.Optional[typing.Any]
    :param extend: Extend, Extend the selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_interior_faces(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select faces where all edges have more than 2 face users

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_less(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_face_step: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Deselect vertices, edges or faces at the boundary of each selection region

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_face_step: Face Step, Connected faces (instead of edges)
    :type use_face_step: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_linked(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        delimit: typing.Optional[typing.Any] = {'SEAM'}):
    ''' Select all vertices connected to the current selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param delimit: Delimit, Delimit selected region
    :type delimit: typing.Optional[typing.Any]
    '''

    pass


def select_linked_pick(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        deselect: typing.Optional[typing.Union[bool, typing.Any]] = False,
        delimit: typing.Optional[typing.Any] = {'SEAM'},
        object_index: typing.Optional[typing.Any] = -1,
        index: typing.Optional[typing.Any] = -1):
    ''' (De)select all vertices linked to the edge under the mouse cursor

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param deselect: Deselect
    :type deselect: typing.Optional[typing.Union[bool, typing.Any]]
    :param delimit: Delimit, Delimit selected region
    :type delimit: typing.Optional[typing.Any]
    :type object_index: typing.Optional[typing.Any]
    :type index: typing.Optional[typing.Any]
    '''

    pass


def select_loose(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select loose geometry based on the selection mode

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend the selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_mirror(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        axis: typing.Optional[typing.Any] = {'X'},
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select mesh items at mirrored locations

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param axis: Axis
    :type axis: typing.Optional[typing.Any]
    :param extend: Extend, Extend the existing selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_mode(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_extend: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_expand: typing.Optional[typing.Union[bool, typing.Any]] = False,
        type: typing.Optional[typing.Union[str, int]] = 'VERT',
        action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Change selection mode

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_extend: Extend
    :type use_extend: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_expand: Expand
    :type use_expand: typing.Optional[typing.Union[bool, typing.Any]]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    :param action: Action, Selection action to execute * ``DISABLE`` Disable -- Disable selected markers. * ``ENABLE`` Enable -- Enable selected markers. * ``TOGGLE`` Toggle -- Toggle disabled flag for selected markers.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_more(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_face_step: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Select more vertices, edges or faces connected to initial selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_face_step: Face Step, Connected faces (instead of edges)
    :type use_face_step: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_next_item(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select the next element (using selection order) :File: `startup/bl_operators/mesh.py\:195 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/mesh.py#L195>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_non_manifold(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_wire: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_boundary: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_multi_face: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_non_contiguous: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = True,
        use_verts: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Select all non-manifold vertices or edges

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend the selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_wire: Wire, Wire edges
    :type use_wire: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_boundary: Boundaries, Boundary edges
    :type use_boundary: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_multi_face: Multiple Faces, Edges shared by more than two faces
    :type use_multi_face: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_non_contiguous: Non Contiguous, Edges between faces pointing in alternate directions
    :type use_non_contiguous: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_verts: Vertices, Vertices connecting multiple face regions
    :type use_verts: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_nth(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        skip: typing.Optional[typing.Any] = 1,
        nth: typing.Optional[typing.Any] = 1,
        offset: typing.Optional[typing.Any] = 0):
    ''' Deselect every Nth element starting from the active vertex, edge or face

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: typing.Optional[typing.Any]
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: typing.Optional[typing.Any]
    :param offset: Offset, Offset from the starting point
    :type offset: typing.Optional[typing.Any]
    '''

    pass


def select_prev_item(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select the previous element (using selection order) :File: `startup/bl_operators/mesh.py\:220 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/mesh.py#L220>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_random(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        ratio: typing.Optional[typing.Any] = 0.5,
        seed: typing.Optional[typing.Any] = 0,
        action: typing.Optional[typing.Any] = 'SELECT'):
    ''' Randomly select vertices

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param ratio: Ratio, Portion of items to select randomly
    :type ratio: typing.Optional[typing.Any]
    :param seed: Random Seed, Seed for the random number generator
    :type seed: typing.Optional[typing.Any]
    :param action: Action, Selection action to execute * ``SELECT`` Select -- Select all elements. * ``DESELECT`` Deselect -- Deselect all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_similar(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'NORMAL',
        compare: typing.Optional[typing.Any] = 'EQUAL',
        threshold: typing.Optional[typing.Any] = 0.0):
    ''' Select similar vertices, edges or faces by property types

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param compare: Compare
    :type compare: typing.Optional[typing.Any]
    :param threshold: Threshold
    :type threshold: typing.Optional[typing.Any]
    '''

    pass


def select_similar_region(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select similar face regions to the current selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_ungrouped(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select vertices without a group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend the selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def separate(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None,
             *,
             type: typing.Optional[typing.Any] = 'SELECTED'):
    ''' Separate selected geometry into a new mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def set_normals_from_faces(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        keep_sharp: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Set the custom normals from the selected faces ones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param keep_sharp: Keep Sharp Edges, Do not set sharp edges to face
    :type keep_sharp: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def shape_propagate_to_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Apply selected vertex locations to all other shape keys

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def shortest_path_pick(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        edge_mode: typing.Optional[typing.Any] = 'SELECT',
        use_face_step: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_topology_distance: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
        use_fill: typing.Optional[typing.Union[bool, typing.Any]] = False,
        skip: typing.Optional[typing.Any] = 0,
        nth: typing.Optional[typing.Any] = 1,
        offset: typing.Optional[typing.Any] = 0,
        index: typing.Optional[typing.Any] = -1):
    ''' Select shortest path between two selections

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path
    :type edge_mode: typing.Optional[typing.Any]
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :type use_face_step: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :type use_topology_distance: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :type use_fill: typing.Optional[typing.Union[bool, typing.Any]]
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: typing.Optional[typing.Any]
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: typing.Optional[typing.Any]
    :param offset: Offset, Offset from the starting point
    :type offset: typing.Optional[typing.Any]
    :type index: typing.Optional[typing.Any]
    '''

    pass


def shortest_path_select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        edge_mode: typing.Optional[typing.Any] = 'SELECT',
        use_face_step: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_topology_distance: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
        use_fill: typing.Optional[typing.Union[bool, typing.Any]] = False,
        skip: typing.Optional[typing.Any] = 0,
        nth: typing.Optional[typing.Any] = 1,
        offset: typing.Optional[typing.Any] = 0):
    ''' Selected shortest path between two vertices/edges/faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path
    :type edge_mode: typing.Optional[typing.Any]
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :type use_face_step: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :type use_topology_distance: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :type use_fill: typing.Optional[typing.Union[bool, typing.Any]]
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: typing.Optional[typing.Any]
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: typing.Optional[typing.Any]
    :param offset: Offset, Offset from the starting point
    :type offset: typing.Optional[typing.Any]
    '''

    pass


def smooth_normals(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 0.5):
    ''' Smooth custom normals based on adjacent vertex normals

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor, Specifies weight of smooth vs original normal
    :type factor: typing.Optional[typing.Any]
    '''

    pass


def solidify(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None,
             *,
             thickness: typing.Optional[typing.Any] = 0.01):
    ''' Create a solid skin by extruding, compensating for sharp angles

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param thickness: Thickness
    :type thickness: typing.Optional[typing.Any]
    '''

    pass


def sort_elements(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'VIEW_ZAXIS',
        elements: typing.Optional[typing.Any] = {'VERT'},
        reverse: typing.Optional[typing.Union[bool, typing.Any]] = False,
        seed: typing.Optional[typing.Any] = 0):
    ''' The order of selected vertices/edges/faces is modified, based on a given method

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type, Type of reordering operation to apply * ``VIEW_ZAXIS`` View Z Axis -- Sort selected elements from farthest to nearest one in current view. * ``VIEW_XAXIS`` View X Axis -- Sort selected elements from left to right one in current view. * ``CURSOR_DISTANCE`` Cursor Distance -- Sort selected elements from nearest to farthest from 3D cursor. * ``MATERIAL`` Material -- Sort selected faces from smallest to greatest material index. * ``SELECTED`` Selected -- Move all selected elements in first places, preserving their relative order. Warning: This will affect unselected elements' indices as well. * ``RANDOMIZE`` Randomize -- Randomize order of selected elements. * ``REVERSE`` Reverse -- Reverse current order of selected elements.
    :type type: typing.Optional[typing.Any]
    :param elements: Elements, Which elements to affect (vertices, edges and/or faces)
    :type elements: typing.Optional[typing.Any]
    :param reverse: Reverse, Reverse the sorting effect
    :type reverse: typing.Optional[typing.Union[bool, typing.Any]]
    :param seed: Seed, Seed for random-based operations
    :type seed: typing.Optional[typing.Any]
    '''

    pass


def spin(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        steps: typing.Optional[typing.Any] = 12,
        dupli: typing.Optional[typing.Union[bool, typing.Any]] = False,
        angle: typing.Optional[typing.Any] = 1.5708,
        use_auto_merge: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_normal_flip: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        center: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        axis: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Extrude selected vertices in a circle around the cursor in indicated viewport

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param steps: Steps, Steps
    :type steps: typing.Optional[typing.Any]
    :param dupli: Use Duplicates
    :type dupli: typing.Optional[typing.Union[bool, typing.Any]]
    :param angle: Angle, Rotation for each step
    :type angle: typing.Optional[typing.Any]
    :param use_auto_merge: Auto Merge, Merge first/last when the angle is a full revolution
    :type use_auto_merge: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: typing.Optional[typing.Union[bool, typing.Any]]
    :param center: Center, Center in global view space
    :type center: typing.Optional[typing.Any]
    :param axis: Axis, Axis in global view space
    :type axis: typing.Optional[typing.Any]
    '''

    pass


def split(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None):
    ''' Split off selected geometry from connected unselected geometry

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def split_normals(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Split custom normals of selected vertices

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def subdivide(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        number_cuts: typing.Optional[typing.Any] = 1,
        smoothness: typing.Optional[typing.Any] = 0.0,
        ngon: typing.Optional[typing.Union[bool, typing.Any]] = True,
        quadcorner: typing.Optional[typing.Any] = 'STRAIGHT_CUT',
        fractal: typing.Optional[typing.Any] = 0.0,
        fractal_along_normal: typing.Optional[typing.Any] = 0.0,
        seed: typing.Optional[typing.Any] = 0):
    ''' Subdivide selected edges

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param number_cuts: Number of Cuts
    :type number_cuts: typing.Optional[typing.Any]
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: typing.Optional[typing.Any]
    :param ngon: Create N-Gons, When disabled, newly created faces are limited to 3 and 4 sided faces
    :type ngon: typing.Optional[typing.Union[bool, typing.Any]]
    :param quadcorner: Quad Corner Type, How to subdivide quad corners (anything other than Straight Cut will prevent n-gons)
    :type quadcorner: typing.Optional[typing.Any]
    :param fractal: Fractal, Fractal randomness factor
    :type fractal: typing.Optional[typing.Any]
    :param fractal_along_normal: Along Normal, Apply fractal displacement along normal only
    :type fractal_along_normal: typing.Optional[typing.Any]
    :param seed: Random Seed, Seed for the random number generator
    :type seed: typing.Optional[typing.Any]
    '''

    pass


def subdivide_edgering(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        number_cuts: typing.Optional[typing.Any] = 10,
        interpolation: typing.Optional[typing.Any] = 'PATH',
        smoothness: typing.Optional[typing.Any] = 1.0,
        profile_shape_factor: typing.Optional[typing.Any] = 0.0,
        profile_shape: typing.Optional[typing.Union[str, int]] = 'SMOOTH'):
    ''' Subdivide perpendicular edges to the selected edge-ring

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param number_cuts: Number of Cuts
    :type number_cuts: typing.Optional[typing.Any]
    :param interpolation: Interpolation, Interpolation method
    :type interpolation: typing.Optional[typing.Any]
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: typing.Optional[typing.Any]
    :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded
    :type profile_shape_factor: typing.Optional[typing.Any]
    :param profile_shape: Profile Shape, Shape of the profile
    :type profile_shape: typing.Optional[typing.Union[str, int]]
    '''

    pass


def symmetrize(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        direction: typing.Optional[typing.Union[str, int]] = 'NEGATIVE_X',
        threshold: typing.Optional[typing.Any] = 0.0001):
    ''' Enforce symmetry (both form and topological) across an axis

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param direction: Direction, Which sides to copy from and to
    :type direction: typing.Optional[typing.Union[str, int]]
    :param threshold: Threshold, Limit for snap middle vertices to the axis center
    :type threshold: typing.Optional[typing.Any]
    '''

    pass


def symmetry_snap(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        direction: typing.Optional[typing.Union[str, int]] = 'NEGATIVE_X',
        threshold: typing.Optional[typing.Any] = 0.05,
        factor: typing.Optional[typing.Any] = 0.5,
        use_center: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Snap vertex pairs to their mirrored locations

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param direction: Direction, Which sides to copy from and to
    :type direction: typing.Optional[typing.Union[str, int]]
    :param threshold: Threshold, Distance within which matching vertices are searched
    :type threshold: typing.Optional[typing.Any]
    :param factor: Factor, Mix factor of the locations of the vertices
    :type factor: typing.Optional[typing.Any]
    :param use_center: Center, Snap middle vertices to the axis center
    :type use_center: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def tris_convert_to_quads(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        face_threshold: typing.Optional[typing.Any] = 0.698132,
        shape_threshold: typing.Optional[typing.Any] = 0.698132,
        uvs: typing.Optional[typing.Union[bool, typing.Any]] = False,
        vcols: typing.Optional[typing.Union[bool, typing.Any]] = False,
        seam: typing.Optional[typing.Union[bool, typing.Any]] = False,
        sharp: typing.Optional[typing.Union[bool, typing.Any]] = False,
        materials: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Join triangles into quads

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param face_threshold: Max Face Angle, Face angle limit
    :type face_threshold: typing.Optional[typing.Any]
    :param shape_threshold: Max Shape Angle, Shape angle limit
    :type shape_threshold: typing.Optional[typing.Any]
    :param uvs: Compare UVs
    :type uvs: typing.Optional[typing.Union[bool, typing.Any]]
    :param vcols: Compare VCols
    :type vcols: typing.Optional[typing.Union[bool, typing.Any]]
    :param seam: Compare Seam
    :type seam: typing.Optional[typing.Union[bool, typing.Any]]
    :param sharp: Compare Sharp
    :type sharp: typing.Optional[typing.Union[bool, typing.Any]]
    :param materials: Compare Materials
    :type materials: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def unsubdivide(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        iterations: typing.Optional[typing.Any] = 2):
    ''' Un-subdivide selected edges and faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param iterations: Iterations, Number of times to un-subdivide
    :type iterations: typing.Optional[typing.Any]
    '''

    pass


def uv_texture_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add UV map

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def uv_texture_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove UV map

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def uvs_reverse(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Flip direction of UV coordinates inside faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def uvs_rotate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_ccw: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Rotate UV coordinates inside faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_ccw: Counter Clockwise
    :type use_ccw: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def vert_connect(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Connect selected vertices of faces, splitting the face

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vert_connect_concave(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Make all faces convex

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vert_connect_nonplanar(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        angle_limit: typing.Optional[typing.Any] = 0.0872665):
    ''' Split non-planar faces that exceed the angle threshold

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param angle_limit: Max Angle, Angle limit
    :type angle_limit: typing.Optional[typing.Any]
    '''

    pass


def vert_connect_path(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Connect vertices by their selection order, creating edges, splitting faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertices_smooth(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 0.0,
        repeat: typing.Optional[typing.Any] = 1,
        xaxis: typing.Optional[typing.Union[bool, typing.Any]] = True,
        yaxis: typing.Optional[typing.Union[bool, typing.Any]] = True,
        zaxis: typing.Optional[typing.Union[bool, typing.Any]] = True,
        wait_for_input: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = True):
    ''' Flatten angles of selected vertices

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Smoothing, Smoothing factor
    :type factor: typing.Optional[typing.Any]
    :param repeat: Repeat, Number of times to smooth the mesh
    :type repeat: typing.Optional[typing.Any]
    :param xaxis: X-Axis, Smooth along the X axis
    :type xaxis: typing.Optional[typing.Union[bool, typing.Any]]
    :param yaxis: Y-Axis, Smooth along the Y axis
    :type yaxis: typing.Optional[typing.Union[bool, typing.Any]]
    :param zaxis: Z-Axis, Smooth along the Z axis
    :type zaxis: typing.Optional[typing.Union[bool, typing.Any]]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def vertices_smooth_laplacian(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        repeat: typing.Optional[typing.Any] = 1,
        lambda_factor: typing.Optional[typing.Any] = 1.0,
        lambda_border: typing.Optional[typing.Any] = 5e-05,
        use_x: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_y: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_z: typing.Optional[typing.Union[bool, typing.Any]] = True,
        preserve_volume: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True):
    ''' Laplacian smooth of selected vertices

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param repeat: Number of iterations to smooth the mesh
    :type repeat: typing.Optional[typing.Any]
    :param lambda_factor: Lambda factor
    :type lambda_factor: typing.Optional[typing.Any]
    :param lambda_border: Lambda factor in border
    :type lambda_border: typing.Optional[typing.Any]
    :param use_x: Smooth X Axis, Smooth object along X axis
    :type use_x: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_y: Smooth Y Axis, Smooth object along Y axis
    :type use_y: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_z: Smooth Z Axis, Smooth object along Z axis
    :type use_z: typing.Optional[typing.Union[bool, typing.Any]]
    :param preserve_volume: Preserve Volume, Apply volume preservation after smooth
    :type preserve_volume: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def wireframe(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_boundary: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_even_offset: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True,
        use_relative_offset: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = False,
        use_replace: typing.Optional[typing.Union[bool, typing.Any]] = True,
        thickness: typing.Optional[typing.Any] = 0.01,
        offset: typing.Optional[typing.Any] = 0.01,
        use_crease: typing.Optional[typing.Union[bool, typing.Any]] = False,
        crease_weight: typing.Optional[typing.Any] = 0.01):
    ''' Create a solid wireframe from faces

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_boundary: Boundary, Inset face boundaries
    :type use_boundary: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :type use_even_offset: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
    :type use_relative_offset: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_replace: Replace, Remove original faces
    :type use_replace: typing.Optional[typing.Union[bool, typing.Any]]
    :param thickness: Thickness
    :type thickness: typing.Optional[typing.Any]
    :param offset: Offset
    :type offset: typing.Optional[typing.Any]
    :param use_crease: Crease, Crease hub edges for an improved subdivision surface
    :type use_crease: typing.Optional[typing.Union[bool, typing.Any]]
    :param crease_weight: Crease Weight
    :type crease_weight: typing.Optional[typing.Any]
    '''

    pass
