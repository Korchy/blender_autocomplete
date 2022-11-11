import sys
import typing
import bpy.types
import bpy.ops.transform
import mathutils

GenericType = typing.TypeVar("GenericType")


def cyclic_toggle(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  direction: typing.Union[str, int] = 'CYCLIC_U'):
    ''' Make active spline closed/opened loop

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param direction: Direction, Direction to make surface cyclic in
    :type direction: typing.Union[str, int]
    '''

    pass


def de_select_first(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' (De)select first of visible part of each NURBS

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def de_select_last(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' (De)select last of visible part of each NURBS

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
             ratio: float = 1.0):
    ''' Simplify selected curves

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param ratio: Ratio
    :type ratio: float
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           type: typing.Union[str, int] = 'VERT'):
    ''' Delete selected control points or segments

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Which elements to delete
    :type type: typing.Union[str, int]
    '''

    pass


def dissolve_verts(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Delete selected control points, correcting surrounding handles

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def draw(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         error_threshold: float = 0.0,
         fit_method: typing.Union[int, str] = 'REFIT',
         corner_angle: float = 1.22173,
         use_cyclic: bool = True,
         stroke: bpy.types.
         bpy_prop_collection['bpy.types.OperatorStrokeElement'] = None,
         wait_for_input: bool = True):
    ''' Draw a freehand spline

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param error_threshold: Error, Error distance threshold (in object units)
    :type error_threshold: float
    :param fit_method: Fit Method
    :type fit_method: typing.Union[int, str]
    :param corner_angle: Corner Angle
    :type corner_angle: float
    :param use_cyclic: Cyclic
    :type use_cyclic: bool
    :param stroke: Stroke
    :type stroke: bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def duplicate(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Duplicate selected control points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def duplicate_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        CURVE_OT_duplicate: 'duplicate' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Duplicate curve and move

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param CURVE_OT_duplicate: Duplicate Curve, Duplicate selected control points
    :type CURVE_OT_duplicate: 'duplicate'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def extrude(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: bool = None,
            *,
            mode: typing.Union[int, str] = 'TRANSLATION'):
    ''' Extrude selected control point(s)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[int, str]
    '''

    pass


def extrude_move(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 CURVE_OT_extrude: 'extrude' = None,
                 TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Extrude curve and move result

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param CURVE_OT_extrude: Extrude, Extrude selected control point(s)
    :type CURVE_OT_extrude: 'extrude'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def handle_type_set(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    type: typing.Union[str, int] = 'AUTOMATIC'):
    ''' Set type of handles for selected control points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Spline type
    :type type: typing.Union[str, int]
    '''

    pass


def hide(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         unselected: bool = False):
    ''' Hide (un)selected control points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: bool
    '''

    pass


def make_segment(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Join two curves by their selected ends

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def match_texture_space(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Match texture space to object's bounding box

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def normals_make_consistent(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None,
                            *,
                            calc_length: bool = False):
    ''' Recalculate the direction of selected handles

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param calc_length: Length, Recalculate handle length
    :type calc_length: bool
    '''

    pass


def pen(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        extend: bool = False,
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

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
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


def primitive_bezier_circle_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        radius: float = 1.0,
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
    ''' Construct a Bezier Circle

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param radius: Radius
    :type radius: float
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


def primitive_bezier_curve_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        radius: float = 1.0,
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
    ''' Construct a Bezier Curve

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param radius: Radius
    :type radius: float
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


def primitive_nurbs_circle_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        radius: float = 1.0,
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
    ''' Construct a Nurbs Circle

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param radius: Radius
    :type radius: float
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


def primitive_nurbs_curve_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        radius: float = 1.0,
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
    ''' Construct a Nurbs Curve

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param radius: Radius
    :type radius: float
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


def primitive_nurbs_path_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        radius: float = 1.0,
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
    ''' Construct a Path

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param radius: Radius
    :type radius: float
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


def radius_set(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               radius: float = 1.0):
    ''' Set per-point radius which is used for bevel tapering

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param radius: Radius
    :type radius: float
    '''

    pass


def reveal(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           select: bool = True):
    ''' Reveal hidden control points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param select: Select
    :type select: bool
    '''

    pass


def select_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               action: typing.Union[str, int] = 'TOGGLE'):
    ''' (De)select all control points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_less(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Deselect control points at the boundary of each selection region

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_linked(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Select all control points linked to the current selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_linked_pick(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       deselect: bool = False):
    ''' Select all control points linked to already selected ones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param deselect: Deselect, Deselect linked control points rather than selecting them
    :type deselect: bool
    '''

    pass


def select_more(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Select control points at the boundary of each selection region

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_next(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Select control points following already selected ones along the curves

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
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
    ''' Deselect every Nth point starting from the active one

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


def select_previous(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Select control points preceding already selected ones along the curves

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
    ''' Randomly select some control points

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


def select_row(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Select a row of control points including active one

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_similar(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   type: typing.Union[str, int] = 'WEIGHT',
                   compare: typing.Union[str, int] = 'EQUAL',
                   threshold: float = 0.1):
    ''' Select similar curve points by property type

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


def separate(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None):
    ''' Separate selected points from connected unselected points into a new object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def shade_flat(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Set shading to flat

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def shade_smooth(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Set shading to smooth

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def shortest_path_pick(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Select shortest path between two selections

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def smooth(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Flatten angles of selected points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def smooth_radius(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Interpolate radii of selected points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def smooth_tilt(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Interpolate tilt of selected points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def smooth_weight(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Interpolate weight of selected points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def spin(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         center: typing.
         Union[typing.List[float], typing.
               Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                  0.0),
         axis: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Extrude selected boundary row around pivot point and current view axis

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param center: Center, Center in global view space
    :type center: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param axis: Axis, Axis in global view space
    :type axis: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def spline_type_set(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    type: typing.Union[str, int] = 'POLY',
                    use_handles: bool = False):
    ''' Set type of active spline

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Spline type
    :type type: typing.Union[str, int]
    :param use_handles: Handles, Use handles when converting bezier curves into polygons
    :type use_handles: bool
    '''

    pass


def spline_weight_set(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      weight: float = 1.0):
    ''' Set softbody goal weight for selected points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param weight: Weight
    :type weight: float
    '''

    pass


def split(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None):
    ''' Split off selected points from connected unselected points

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
              number_cuts: int = 1):
    ''' Subdivide selected segments

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param number_cuts: Number of Cuts
    :type number_cuts: int
    '''

    pass


def switch_direction(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Switch direction of selected splines

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def tilt_clear(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Clear the tilt of selected control points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_add(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               location: typing.
               Union[typing.List[float], typing.
                     Tuple[float, float, float], 'mathutils.Vector'] = (0.0,
                                                                        0.0,
                                                                        0.0)):
    ''' Add a new control point (linked to only selected end-curve one, if any)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param location: Location, Location to add new vertex at
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass
