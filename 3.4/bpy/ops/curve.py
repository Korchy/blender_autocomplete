import sys
import typing
import bpy.types
import bpy.ops.transform

GenericType = typing.TypeVar("GenericType")


def cyclic_toggle(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  direction: typing.Optional[typing.Any] = 'CYCLIC_U'):
    ''' Make active spline closed/opened loop

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param direction: Direction, Direction to make surface cyclic in
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def de_select_first(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' (De)select first of visible part of each NURBS

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def de_select_last(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None):
    ''' (De)select last of visible part of each NURBS

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def decimate(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None,
             *,
             ratio: typing.Optional[typing.Any] = 1.0):
    ''' Simplify selected curves

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param ratio: Ratio
    :type ratio: typing.Optional[typing.Any]
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None,
           *,
           type: typing.Optional[typing.Any] = 'VERT'):
    ''' Delete selected control points or segments

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type, Which elements to delete
    :type type: typing.Optional[typing.Any]
    '''

    pass


def dissolve_verts(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None):
    ''' Delete selected control points, correcting surrounding handles

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def draw(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         error_threshold: typing.Optional[typing.Any] = 0.0,
         fit_method: typing.Union[str, int] = 'REFIT',
         corner_angle: typing.Optional[typing.Any] = 1.22173,
         use_cyclic: typing.Union[bool, typing.Any] = True,
         stroke: typing.Optional[bpy.types.bpy_prop_collection[
             'bpy.types.OperatorStrokeElement']] = None,
         wait_for_input: typing.Union[bool, typing.Any] = True):
    ''' Draw a freehand spline

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param error_threshold: Error, Error distance threshold (in object units)
    :type error_threshold: typing.Optional[typing.Any]
    :param fit_method: Fit Method
    :type fit_method: typing.Union[str, int]
    :param corner_angle: Corner Angle
    :type corner_angle: typing.Optional[typing.Any]
    :param use_cyclic: Cyclic
    :type use_cyclic: typing.Union[bool, typing.Any]
    :param stroke: Stroke
    :type stroke: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Union[bool, typing.Any]
    '''

    pass


def duplicate(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None):
    ''' Duplicate selected control points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def duplicate_move(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   CURVE_OT_duplicate: typing.Optional['duplicate'] = None,
                   TRANSFORM_OT_translate: typing.
                   Optional['bpy.ops.transform.translate'] = None):
    ''' Duplicate curve and move

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param CURVE_OT_duplicate: Duplicate Curve, Duplicate selected control points
    :type CURVE_OT_duplicate: typing.Optional['duplicate']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def extrude(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: typing.Optional[bool] = None,
            *,
            mode: typing.Union[str, int] = 'TRANSLATION'):
    ''' Extrude selected control point(s)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Union[str, int]
    '''

    pass


def extrude_move(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 CURVE_OT_extrude: typing.Optional['extrude'] = None,
                 TRANSFORM_OT_translate: typing.
                 Optional['bpy.ops.transform.translate'] = None):
    ''' Extrude curve and move result

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param CURVE_OT_extrude: Extrude, Extrude selected control point(s)
    :type CURVE_OT_extrude: typing.Optional['extrude']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def handle_type_set(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    type: typing.Optional[typing.Any] = 'AUTOMATIC'):
    ''' Set type of handles for selected control points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type, Spline type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def hide(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         unselected: typing.Union[bool, typing.Any] = False):
    ''' Hide (un)selected control points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: typing.Union[bool, typing.Any]
    '''

    pass


def make_segment(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Join two curves by their selected ends

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def match_texture_space(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Match texture space to object's bounding box

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def normals_make_consistent(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        calc_length: typing.Union[bool, typing.Any] = False):
    ''' Recalculate the direction of selected handles

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param calc_length: Length, Recalculate handle length
    :type calc_length: typing.Union[bool, typing.Any]
    '''

    pass


def pen(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Union[bool, typing.Any] = False,
        deselect: typing.Union[bool, typing.Any] = False,
        toggle: typing.Union[bool, typing.Any] = False,
        deselect_all: typing.Union[bool, typing.Any] = False,
        select_passthrough: typing.Union[bool, typing.Any] = False,
        extrude_point: typing.Union[bool, typing.Any] = False,
        extrude_handle: typing.Optional[typing.Any] = 'VECTOR',
        delete_point: typing.Union[bool, typing.Any] = False,
        insert_point: typing.Union[bool, typing.Any] = False,
        move_segment: typing.Union[bool, typing.Any] = False,
        select_point: typing.Union[bool, typing.Any] = False,
        move_point: typing.Union[bool, typing.Any] = False,
        close_spline: typing.Union[bool, typing.Any] = True,
        close_spline_method: typing.Optional[typing.Any] = 'OFF',
        toggle_vector: typing.Union[bool, typing.Any] = False,
        cycle_handle_type: typing.Union[bool, typing.Any] = False):
    ''' Construct and edit splines

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Union[bool, typing.Any]
    :param deselect: Deselect, Remove from selection
    :type deselect: typing.Union[bool, typing.Any]
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: typing.Union[bool, typing.Any]
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: typing.Union[bool, typing.Any]
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :type select_passthrough: typing.Union[bool, typing.Any]
    :param extrude_point: Extrude Point, Add a point connected to the last selected point
    :type extrude_point: typing.Union[bool, typing.Any]
    :param extrude_handle: Extrude Handle Type, Type of the extruded handle
    :type extrude_handle: typing.Optional[typing.Any]
    :param delete_point: Delete Point, Delete an existing point
    :type delete_point: typing.Union[bool, typing.Any]
    :param insert_point: Insert Point, Insert Point into a curve segment
    :type insert_point: typing.Union[bool, typing.Any]
    :param move_segment: Move Segment, Delete an existing point
    :type move_segment: typing.Union[bool, typing.Any]
    :param select_point: Select Point, Select a point or its handles
    :type select_point: typing.Union[bool, typing.Any]
    :param move_point: Move Point, Move a point or its handles
    :type move_point: typing.Union[bool, typing.Any]
    :param close_spline: Close Spline, Make a spline cyclic by clicking endpoints
    :type close_spline: typing.Union[bool, typing.Any]
    :param close_spline_method: Close Spline Method, The condition for close spline to activate * ``OFF`` None. * ``ON_PRESS`` On Press -- Move handles after closing the spline. * ``ON_CLICK`` On Click -- Spline closes on release if not dragged.
    :type close_spline_method: typing.Optional[typing.Any]
    :param toggle_vector: Toggle Vector, Toggle between Vector and Auto handles
    :type toggle_vector: typing.Union[bool, typing.Any]
    :param cycle_handle_type: Cycle Handle Type, Cycle between all four handle types
    :type cycle_handle_type: typing.Union[bool, typing.Any]
    '''

    pass


def primitive_bezier_circle_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        radius: typing.Optional[typing.Any] = 1.0,
        enter_editmode: typing.Union[bool, typing.Any] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Construct a Bezier Circle

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Union[bool, typing.Any]
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


def primitive_bezier_curve_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        radius: typing.Optional[typing.Any] = 1.0,
        enter_editmode: typing.Union[bool, typing.Any] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Construct a Bezier Curve

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Union[bool, typing.Any]
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


def primitive_nurbs_circle_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        radius: typing.Optional[typing.Any] = 1.0,
        enter_editmode: typing.Union[bool, typing.Any] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Construct a Nurbs Circle

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Union[bool, typing.Any]
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


def primitive_nurbs_curve_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        radius: typing.Optional[typing.Any] = 1.0,
        enter_editmode: typing.Union[bool, typing.Any] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Construct a Nurbs Curve

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Union[bool, typing.Any]
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


def primitive_nurbs_path_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        radius: typing.Optional[typing.Any] = 1.0,
        enter_editmode: typing.Union[bool, typing.Any] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Construct a Path

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Union[bool, typing.Any]
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


def radius_set(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               radius: typing.Optional[typing.Any] = 1.0):
    ''' Set per-point radius which is used for bevel tapering

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    '''

    pass


def reveal(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None,
           *,
           select: typing.Union[bool, typing.Any] = True):
    ''' Reveal hidden control points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param select: Select
    :type select: typing.Union[bool, typing.Any]
    '''

    pass


def select_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' (De)select all control points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param action: Action, Selection action to execute * ``TOGGLE`` Toggle -- Toggle selection for all elements. * ``SELECT`` Select -- Select all elements. * ``DESELECT`` Deselect -- Deselect all elements. * ``INVERT`` Invert -- Invert selection of all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_less(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Deselect control points at the boundary of each selection region

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_linked(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None):
    ''' Select all control points linked to the current selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_linked_pick(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       deselect: typing.Union[bool, typing.Any] = False):
    ''' Select all control points linked to already selected ones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param deselect: Deselect, Deselect linked control points rather than selecting them
    :type deselect: typing.Union[bool, typing.Any]
    '''

    pass


def select_more(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Select control points at the boundary of each selection region

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_next(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Select control points following already selected ones along the curves

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_nth(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               skip: typing.Optional[typing.Any] = 1,
               nth: typing.Optional[typing.Any] = 1,
               offset: typing.Optional[typing.Any] = 0):
    ''' Deselect every Nth point starting from the active one

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: typing.Optional[typing.Any]
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: typing.Optional[typing.Any]
    :param offset: Offset, Offset from the starting point
    :type offset: typing.Optional[typing.Any]
    '''

    pass


def select_previous(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' Select control points preceding already selected ones along the curves

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_random(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  ratio: typing.Optional[typing.Any] = 0.5,
                  seed: typing.Optional[typing.Any] = 0,
                  action: typing.Optional[typing.Any] = 'SELECT'):
    ''' Randomly select some control points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param ratio: Ratio, Portion of items to select randomly
    :type ratio: typing.Optional[typing.Any]
    :param seed: Random Seed, Seed for the random number generator
    :type seed: typing.Optional[typing.Any]
    :param action: Action, Selection action to execute * ``SELECT`` Select -- Select all elements. * ``DESELECT`` Deselect -- Deselect all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_row(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None):
    ''' Select a row of control points including active one

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_similar(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   type: typing.Optional[typing.Any] = 'WEIGHT',
                   compare: typing.Optional[typing.Any] = 'EQUAL',
                   threshold: typing.Optional[typing.Any] = 0.1):
    ''' Select similar curve points by property type

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param compare: Compare
    :type compare: typing.Optional[typing.Any]
    :param threshold: Threshold
    :type threshold: typing.Optional[typing.Any]
    '''

    pass


def separate(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None):
    ''' Separate selected points from connected unselected points into a new object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def shade_flat(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None):
    ''' Set shading to flat

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def shade_smooth(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Set shading to smooth

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def shortest_path_pick(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None):
    ''' Select shortest path between two selections

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def smooth(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None):
    ''' Flatten angles of selected points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def smooth_radius(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None):
    ''' Interpolate radii of selected points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def smooth_tilt(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Interpolate tilt of selected points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def smooth_weight(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None):
    ''' Interpolate weight of selected points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def spin(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         center: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
         axis: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Extrude selected boundary row around pivot point and current view axis

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param center: Center, Center in global view space
    :type center: typing.Optional[typing.Any]
    :param axis: Axis, Axis in global view space
    :type axis: typing.Optional[typing.Any]
    '''

    pass


def spline_type_set(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    type: typing.Optional[typing.Any] = 'POLY',
                    use_handles: typing.Union[bool, typing.Any] = False):
    ''' Set type of active spline

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type, Spline type
    :type type: typing.Optional[typing.Any]
    :param use_handles: Handles, Use handles when converting bezier curves into polygons
    :type use_handles: typing.Union[bool, typing.Any]
    '''

    pass


def spline_weight_set(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      weight: typing.Optional[typing.Any] = 1.0):
    ''' Set softbody goal weight for selected points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param weight: Weight
    :type weight: typing.Optional[typing.Any]
    '''

    pass


def split(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: typing.Optional[bool] = None):
    ''' Split off selected points from connected unselected points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def subdivide(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              number_cuts: typing.Optional[typing.Any] = 1):
    ''' Subdivide selected segments

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param number_cuts: Number of Cuts
    :type number_cuts: typing.Optional[typing.Any]
    '''

    pass


def switch_direction(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None):
    ''' Switch direction of selected splines

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def tilt_clear(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None):
    ''' Clear the tilt of selected control points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_add(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add a new control point (linked to only selected end-curve one, if any)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param location: Location, Location to add new vertex at
    :type location: typing.Optional[typing.Any]
    '''

    pass
