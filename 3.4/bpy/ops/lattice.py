import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def flip(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         axis: typing.Optional[typing.Any] = 'U'):
    ''' Mirror all control points without inverting the lattice deform

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param axis: Flip Axis, Coordinates along this axis get flipped
    :type axis: typing.Optional[typing.Any]
    '''

    pass


def make_regular(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Set UVW control points a uniform distance apart

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Change selection of all UVW control points

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
    ''' Deselect vertices at the boundary of each selection region

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_mirror(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  axis: typing.Optional[typing.Any] = {'X'},
                  extend: typing.Union[bool, typing.Any] = False):
    ''' Select mirrored lattice points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param axis: Axis
    :type axis: typing.Optional[typing.Any]
    :param extend: Extend, Extend the selection
    :type extend: typing.Union[bool, typing.Any]
    '''

    pass


def select_more(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Select vertex directly linked to already selected ones

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
    ''' Randomly select UVW control points

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


def select_ungrouped(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     extend: typing.Union[bool, typing.Any] = False):
    ''' Select vertices without a group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend the selection
    :type extend: typing.Union[bool, typing.Any]
    '''

    pass
