import sys
import typing
import bpy.types


def cyclic_toggle(direction: typing.Union[str, int] = 'CYCLIC_U'):
    ''' Make active spline closed/opened loop

    :param direction: Direction, Direction to make surface cyclic in
    :type direction: typing.Union[str, int]
    '''

    pass


def de_select_first():
    ''' (De)select first of visible part of each NURBS

    '''

    pass


def de_select_last():
    ''' (De)select last of visible part of each NURBS

    '''

    pass


def decimate(ratio: float = 1.0):
    ''' Simplify selected curves

    :param ratio: Ratio
    :type ratio: float
    '''

    pass


def delete(type: typing.Union[str, int] = 'VERT'):
    ''' Delete selected control points or segments

    :param type: Type, Which elements to delete
    :type type: typing.Union[str, int]
    '''

    pass


def dissolve_verts():
    ''' Delete selected control points, correcting surrounding handles

    '''

    pass


def draw(error_threshold: float = 0.0,
         fit_method: typing.Union[str, int] = 'REFIT',
         corner_angle: float = 1.22173,
         use_cyclic: bool = True,
         stroke: typing.
         Union[typing.Dict[str, 'bpy.types.OperatorStrokeElement'], typing.
               List['bpy.types.OperatorStrokeElement'],
               'bpy_prop_collection'] = None,
         wait_for_input: bool = True):
    ''' Draw a freehand spline

    :param error_threshold: Error, Error distance threshold (in object units)
    :type error_threshold: float
    :param fit_method: Fit Method * REFIT Refit -- Incrementally refit the curve (high quality). * SPLIT Split -- Split the curve until the tolerance is met (fast).
    :type fit_method: typing.Union[str, int]
    :param corner_angle: Corner Angle
    :type corner_angle: float
    :param use_cyclic: Cyclic
    :type use_cyclic: bool
    :param stroke: Stroke
    :type stroke: typing.Union[typing.Dict[str, 'bpy.types.OperatorStrokeElement'], typing.List['bpy.types.OperatorStrokeElement'], 'bpy_prop_collection']
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def duplicate():
    ''' Duplicate selected control points

    '''

    pass


def duplicate_move(CURVE_OT_duplicate=None, TRANSFORM_OT_translate=None):
    ''' Duplicate curve and move

    :param CURVE_OT_duplicate: Duplicate Curve, Duplicate selected control points
    :param TRANSFORM_OT_translate: Move, Move selected items
    '''

    pass


def extrude(mode: typing.Union[str, int] = 'TRANSLATION'):
    ''' Extrude selected control point(s)

    :param mode: Mode
    :type mode: typing.Union[str, int]
    '''

    pass


def extrude_move(CURVE_OT_extrude=None, TRANSFORM_OT_translate=None):
    ''' Extrude curve and move result

    :param CURVE_OT_extrude: Extrude, Extrude selected control point(s)
    :param TRANSFORM_OT_translate: Move, Move selected items
    '''

    pass


def handle_type_set(type: typing.Union[str, int] = 'AUTOMATIC'):
    ''' Set type of handles for selected control points

    :param type: Type, Spline type
    :type type: typing.Union[str, int]
    '''

    pass


def hide(unselected: bool = False):
    ''' Hide (un)selected control points

    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: bool
    '''

    pass


def make_segment():
    ''' Join two curves by their selected ends

    '''

    pass


def match_texture_space():
    ''' Match texture space to object's bounding box

    '''

    pass


def normals_make_consistent(calc_length: bool = False):
    ''' Recalculate the direction of selected handles

    :param calc_length: Length, Recalculate handle length
    :type calc_length: bool
    '''

    pass


def pen(extend: bool = False,
        deselect: bool = False,
        toggle: bool = False,
        deselect_all: bool = False,
        select_passthrough: bool = False,
        extrude_point: bool = False,
        extrude_handle: typing.Union[str, int] = 'VECTOR',
        delete_point: bool = False,
        insert_point: bool = False,
        move_segment: bool = False,
        select_point: bool = False,
        move_point: bool = False,
        close_spline: bool = True,
        close_spline_method: typing.Union[str, int] = 'OFF',
        toggle_vector: bool = False,
        cycle_handle_type: bool = False):
    ''' Construct and edit splines

    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param deselect: Deselect, Remove from selection
    :type deselect: bool
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: bool
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :type select_passthrough: bool
    :param extrude_point: Extrude Point, Add a point connected to the last selected point
    :type extrude_point: bool
    :param extrude_handle: Extrude Handle Type, Type of the extruded handle
    :type extrude_handle: typing.Union[str, int]
    :param delete_point: Delete Point, Delete an existing point
    :type delete_point: bool
    :param insert_point: Insert Point, Insert Point into a curve segment
    :type insert_point: bool
    :param move_segment: Move Segment, Delete an existing point
    :type move_segment: bool
    :param select_point: Select Point, Select a point or its handles
    :type select_point: bool
    :param move_point: Move Point, Move a point or its handles
    :type move_point: bool
    :param close_spline: Close Spline, Make a spline cyclic by clicking endpoints
    :type close_spline: bool
    :param close_spline_method: Close Spline Method, The condition for close spline to activate * OFF None. * ON_PRESS On Press -- Move handles after closing the spline. * ON_CLICK On Click -- Spline closes on release if not dragged.
    :type close_spline_method: typing.Union[str, int]
    :param toggle_vector: Toggle Vector, Toggle between Vector and Auto handles
    :type toggle_vector: bool
    :param cycle_handle_type: Cycle Handle Type, Cycle between all four handle types
    :type cycle_handle_type: bool
    '''

    pass


def primitive_bezier_circle_add(radius: float = 1.0,
                                enter_editmode: bool = False,
                                align: typing.Union[str, int] = 'WORLD',
                                location: typing.List[float] = (0.0, 0.0, 0.0),
                                rotation: typing.List[float] = (0.0, 0.0, 0.0),
                                scale: typing.List[float] = (0.0, 0.0, 0.0)):
    ''' Construct a Bezier Circle

    :param radius: Radius
    :type radius: float
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.List[float]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.List[float]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.List[float]
    '''

    pass


def primitive_bezier_curve_add(radius: float = 1.0,
                               enter_editmode: bool = False,
                               align: typing.Union[str, int] = 'WORLD',
                               location: typing.List[float] = (0.0, 0.0, 0.0),
                               rotation: typing.List[float] = (0.0, 0.0, 0.0),
                               scale: typing.List[float] = (0.0, 0.0, 0.0)):
    ''' Construct a Bezier Curve

    :param radius: Radius
    :type radius: float
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.List[float]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.List[float]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.List[float]
    '''

    pass


def primitive_nurbs_circle_add(radius: float = 1.0,
                               enter_editmode: bool = False,
                               align: typing.Union[str, int] = 'WORLD',
                               location: typing.List[float] = (0.0, 0.0, 0.0),
                               rotation: typing.List[float] = (0.0, 0.0, 0.0),
                               scale: typing.List[float] = (0.0, 0.0, 0.0)):
    ''' Construct a Nurbs Circle

    :param radius: Radius
    :type radius: float
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.List[float]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.List[float]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.List[float]
    '''

    pass


def primitive_nurbs_curve_add(radius: float = 1.0,
                              enter_editmode: bool = False,
                              align: typing.Union[str, int] = 'WORLD',
                              location: typing.List[float] = (0.0, 0.0, 0.0),
                              rotation: typing.List[float] = (0.0, 0.0, 0.0),
                              scale: typing.List[float] = (0.0, 0.0, 0.0)):
    ''' Construct a Nurbs Curve

    :param radius: Radius
    :type radius: float
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.List[float]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.List[float]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.List[float]
    '''

    pass


def primitive_nurbs_path_add(radius: float = 1.0,
                             enter_editmode: bool = False,
                             align: typing.Union[str, int] = 'WORLD',
                             location: typing.List[float] = (0.0, 0.0, 0.0),
                             rotation: typing.List[float] = (0.0, 0.0, 0.0),
                             scale: typing.List[float] = (0.0, 0.0, 0.0)):
    ''' Construct a Path

    :param radius: Radius
    :type radius: float
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.List[float]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.List[float]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.List[float]
    '''

    pass


def radius_set(radius: float = 1.0):
    ''' Set per-point radius which is used for bevel tapering

    :param radius: Radius
    :type radius: float
    '''

    pass


def reveal(select: bool = True):
    ''' Reveal hidden control points

    :param select: Select
    :type select: bool
    '''

    pass


def select_all(action: typing.Union[str, int] = 'TOGGLE'):
    ''' (De)select all control points

    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_less():
    ''' Deselect control points at the boundary of each selection region

    '''

    pass


def select_linked():
    ''' Select all control points linked to the current selection

    '''

    pass


def select_linked_pick(deselect: bool = False):
    ''' Select all control points linked to already selected ones

    :param deselect: Deselect, Deselect linked control points rather than selecting them
    :type deselect: bool
    '''

    pass


def select_more():
    ''' Select control points at the boundary of each selection region

    '''

    pass


def select_next():
    ''' Select control points following already selected ones along the curves

    '''

    pass


def select_nth(skip: int = 1, nth: int = 1, offset: int = 0):
    ''' Deselect every Nth point starting from the active one

    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: int
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: int
    :param offset: Offset, Offset from the starting point
    :type offset: int
    '''

    pass


def select_previous():
    ''' Select control points preceding already selected ones along the curves

    '''

    pass


def select_random(ratio: float = 0.5,
                  seed: int = 0,
                  action: typing.Union[str, int] = 'SELECT'):
    ''' Randomly select some control points

    :param ratio: Ratio, Portion of items to select randomly
    :type ratio: float
    :param seed: Random Seed, Seed for the random number generator
    :type seed: int
    :param action: Action, Selection action to execute * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_row():
    ''' Select a row of control points including active one

    '''

    pass


def select_similar(type: typing.Union[str, int] = 'WEIGHT',
                   compare: typing.Union[str, int] = 'EQUAL',
                   threshold: float = 0.1):
    ''' Select similar curve points by property type

    :param type: Type
    :type type: typing.Union[str, int]
    :param compare: Compare
    :type compare: typing.Union[str, int]
    :param threshold: Threshold
    :type threshold: float
    '''

    pass


def separate():
    ''' Separate selected points from connected unselected points into a new object

    '''

    pass


def shade_flat():
    ''' Set shading to flat

    '''

    pass


def shade_smooth():
    ''' Set shading to smooth

    '''

    pass


def shortest_path_pick():
    ''' Select shortest path between two selections

    '''

    pass


def smooth():
    ''' Flatten angles of selected points

    '''

    pass


def smooth_radius():
    ''' Interpolate radii of selected points

    '''

    pass


def smooth_tilt():
    ''' Interpolate tilt of selected points

    '''

    pass


def smooth_weight():
    ''' Interpolate weight of selected points

    '''

    pass


def spin(center: typing.List[float] = (0.0, 0.0, 0.0),
         axis: typing.List[float] = (0.0, 0.0, 0.0)):
    ''' Extrude selected boundary row around pivot point and current view axis

    :param center: Center, Center in global view space
    :type center: typing.List[float]
    :param axis: Axis, Axis in global view space
    :type axis: typing.List[float]
    '''

    pass


def spline_type_set(type: typing.Union[str, int] = 'POLY',
                    use_handles: bool = False):
    ''' Set type of active spline

    :param type: Type, Spline type
    :type type: typing.Union[str, int]
    :param use_handles: Handles, Use handles when converting bezier curves into polygons
    :type use_handles: bool
    '''

    pass


def spline_weight_set(weight: float = 1.0):
    ''' Set softbody goal weight for selected points

    :param weight: Weight
    :type weight: float
    '''

    pass


def split():
    ''' Split off selected points from connected unselected points

    '''

    pass


def subdivide(number_cuts: int = 1):
    ''' Subdivide selected segments

    :param number_cuts: Number of Cuts
    :type number_cuts: int
    '''

    pass


def switch_direction():
    ''' Switch direction of selected splines

    '''

    pass


def tilt_clear():
    ''' Clear the tilt of selected control points

    '''

    pass


def vertex_add(location: typing.List[float] = (0.0, 0.0, 0.0)):
    ''' Add a new control point (linked to only selected end-curve one, if any)

    :param location: Location, Location to add new vertex at
    :type location: typing.List[float]
    '''

    pass
