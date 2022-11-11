import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def bake_to_keyframes(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      frame_start: int = 1,
                      frame_end: int = 250,
                      step: int = 1):
    ''' Bake rigid body transformations of selected objects to keyframes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame_start: Start Frame, Start frame for baking
    :type frame_start: int
    :param frame_end: End Frame, End frame for baking
    :type frame_end: int
    :param step: Frame Step, Frame Step
    :type step: int
    '''

    pass


def connect(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: bool = None,
            *,
            con_type: typing.Union[str, int] = 'FIXED',
            pivot_type: typing.Union[str, int] = 'CENTER',
            connection_pattern: typing.Union[str, int] = 'SELECTED_TO_ACTIVE'):
    ''' Create rigid body constraints between selected rigid bodies

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param con_type: Type, Type of generated constraint * FIXED Fixed -- Glue rigid bodies together. * POINT Point -- Constrain rigid bodies to move around common pivot point. * HINGE Hinge -- Restrict rigid body rotation to one axis. * SLIDER Slider -- Restrict rigid body translation to one axis. * PISTON Piston -- Restrict rigid body translation and rotation to one axis. * GENERIC Generic -- Restrict translation and rotation to specified axes. * GENERIC_SPRING Generic Spring -- Restrict translation and rotation to specified axes with springs. * MOTOR Motor -- Drive rigid body around or along an axis.
    :type con_type: typing.Union[str, int]
    :param pivot_type: Location, Constraint pivot location * CENTER Center -- Pivot location is between the constrained rigid bodies. * ACTIVE Active -- Pivot location is at the active object position. * SELECTED Selected -- Pivot location is at the selected object position.
    :type pivot_type: typing.Union[str, int]
    :param connection_pattern: Connection Pattern, Pattern used to connect objects * SELECTED_TO_ACTIVE Selected to Active -- Connect selected objects to the active object. * CHAIN_DISTANCE Chain by Distance -- Connect objects as a chain based on distance, starting at the active object.
    :type connection_pattern: typing.Union[str, int]
    '''

    pass


def constraint_add(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   type: typing.Union[int, str] = 'FIXED'):
    ''' Add Rigid Body Constraint to active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Rigid Body Constraint Type
    :type type: typing.Union[int, str]
    '''

    pass


def constraint_remove(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Remove Rigid Body Constraint from Object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def mass_calculate(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   material: typing.Union[str, int] = 'DEFAULT',
                   density: float = 1.0):
    ''' Automatically calculate mass values for Rigid Body Objects based on volume

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param material: Material Preset, Type of material that objects are made of (determines material density)
    :type material: typing.Union[str, int]
    :param density: Density, Density value (kg/m^3), allows custom value if the 'Custom' preset is used
    :type density: float
    '''

    pass


def object_add(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               type: typing.Union[int, str] = 'ACTIVE'):
    ''' Add active object as Rigid Body

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Rigid Body Type
    :type type: typing.Union[int, str]
    '''

    pass


def object_remove(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Remove Rigid Body settings from Object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def object_settings_copy(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None):
    ''' Copy Rigid Body settings from active object to selected :file: startup/bl_operators/rigidbody.py\:43 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/rigidbody.py$43> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def objects_add(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                type: typing.Union[int, str] = 'ACTIVE'):
    ''' Add selected objects as Rigid Bodies

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Rigid Body Type
    :type type: typing.Union[int, str]
    '''

    pass


def objects_remove(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Remove selected objects from Rigid Body simulation

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def shape_change(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 type: typing.Union[int, str] = 'MESH'):
    ''' Change collision shapes for selected Rigid Body Objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Rigid Body Shape
    :type type: typing.Union[int, str]
    '''

    pass


def world_add(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Add Rigid Body simulation world to the current scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def world_remove(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Remove Rigid Body simulation world from the current scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass
