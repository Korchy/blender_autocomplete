import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def bake_to_keyframes(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        frame_start: typing.Optional[typing.Any] = 1,
        frame_end: typing.Optional[typing.Any] = 250,
        step: typing.Optional[typing.Any] = 1):
    ''' Bake rigid body transformations of selected objects to keyframes :File: `startup/bl_operators/rigidbody.py\:108 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/rigidbody.py#L108>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param frame_start: Start Frame, Start frame for baking
    :type frame_start: typing.Optional[typing.Any]
    :param frame_end: End Frame, End frame for baking
    :type frame_end: typing.Optional[typing.Any]
    :param step: Frame Step, Frame Step
    :type step: typing.Optional[typing.Any]
    '''

    pass


def connect(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
            execution_context: typing.Optional[typing.Union[str, int]] = None,
            undo: typing.Optional[bool] = None,
            *,
            con_type: typing.Optional[typing.Any] = 'FIXED',
            pivot_type: typing.Optional[typing.Any] = 'CENTER',
            connection_pattern: typing.Optional[typing.
                                                Any] = 'SELECTED_TO_ACTIVE'):
    ''' Create rigid body constraints between selected rigid bodies :File: `startup/bl_operators/rigidbody.py\:270 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/rigidbody.py#L270>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param con_type: Type, Type of generated constraint * ``FIXED`` Fixed -- Glue rigid bodies together. * ``POINT`` Point -- Constrain rigid bodies to move around common pivot point. * ``HINGE`` Hinge -- Restrict rigid body rotation to one axis. * ``SLIDER`` Slider -- Restrict rigid body translation to one axis. * ``PISTON`` Piston -- Restrict rigid body translation and rotation to one axis. * ``GENERIC`` Generic -- Restrict translation and rotation to specified axes. * ``GENERIC_SPRING`` Generic Spring -- Restrict translation and rotation to specified axes with springs. * ``MOTOR`` Motor -- Drive rigid body around or along an axis.
    :type con_type: typing.Optional[typing.Any]
    :param pivot_type: Location, Constraint pivot location * ``CENTER`` Center -- Pivot location is between the constrained rigid bodies. * ``ACTIVE`` Active -- Pivot location is at the active object position. * ``SELECTED`` Selected -- Pivot location is at the selected object position.
    :type pivot_type: typing.Optional[typing.Any]
    :param connection_pattern: Connection Pattern, Pattern used to connect objects * ``SELECTED_TO_ACTIVE`` Selected to Active -- Connect selected objects to the active object. * ``CHAIN_DISTANCE`` Chain by Distance -- Connect objects as a chain based on distance, starting at the active object.
    :type connection_pattern: typing.Optional[typing.Any]
    '''

    pass


def constraint_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'FIXED'):
    ''' Add Rigid Body Constraint to active object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Rigid Body Constraint Type
    :type type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def constraint_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove Rigid Body Constraint from Object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def mass_calculate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        material: typing.Optional[typing.Union[str, int, typing.
                                               Any]] = 'DEFAULT',
        density: typing.Optional[typing.Any] = 1.0):
    ''' Automatically calculate mass values for Rigid Body Objects based on volume

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param material: Material Preset, Type of material that objects are made of (determines material density)
    :type material: typing.Optional[typing.Union[str, int, typing.Any]]
    :param density: Density, Density value (kg/m^3), allows custom value if the 'Custom' preset is used
    :type density: typing.Optional[typing.Any]
    '''

    pass


def object_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'ACTIVE'):
    ''' Add active object as Rigid Body

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Rigid Body Type
    :type type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def object_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove Rigid Body settings from Object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def object_settings_copy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Copy Rigid Body settings from active object to selected :File: `startup/bl_operators/rigidbody.py\:45 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/rigidbody.py#L45>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def objects_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'ACTIVE'):
    ''' Add selected objects as Rigid Bodies

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Rigid Body Type
    :type type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def objects_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove selected objects from Rigid Body simulation

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def shape_change(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'MESH'):
    ''' Change collision shapes for selected Rigid Body Objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Rigid Body Shape
    :type type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def world_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add Rigid Body simulation world to the current scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def world_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove Rigid Body simulation world from the current scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass
