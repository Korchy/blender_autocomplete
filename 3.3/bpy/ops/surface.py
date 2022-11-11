import sys
import typing
import bpy.types
import mathutils

GenericType = typing.TypeVar("GenericType")


def primitive_nurbs_surface_circle_add(
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
    ''' Construct a Nurbs surface Circle

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


def primitive_nurbs_surface_curve_add(
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
    ''' Construct a Nurbs surface Curve

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


def primitive_nurbs_surface_cylinder_add(
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
    ''' Construct a Nurbs surface Cylinder

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


def primitive_nurbs_surface_sphere_add(
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
    ''' Construct a Nurbs surface Sphere

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


def primitive_nurbs_surface_surface_add(
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
    ''' Construct a Nurbs surface Patch

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


def primitive_nurbs_surface_torus_add(
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
    ''' Construct a Nurbs surface Torus

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
