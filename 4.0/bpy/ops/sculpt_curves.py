import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def brush_stroke(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        stroke: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorStrokeElement']] = None,
        mode: typing.Optional[typing.Any] = 'NORMAL'):
    ''' Sculpt curves using a brush

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param stroke: Stroke
    :type stroke: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param mode: Stroke Mode, Action taken when a paint stroke is made * ``NORMAL`` Regular -- Apply brush normally. * ``INVERT`` Invert -- Invert action of brush for duration of stroke. * ``SMOOTH`` Smooth -- Switch brush to smooth mode for duration of stroke.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def min_distance_edit(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Change the minimum distance used by the density brush

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_grow(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        distance: typing.Optional[typing.Any] = 0.1):
    ''' Select curves which are close to curves that are selected already

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param distance: Distance, By how much to grow the selection
    :type distance: typing.Optional[typing.Any]
    '''

    pass


def select_random(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        seed: typing.Optional[typing.Any] = 0,
        partial: typing.Optional[typing.Union[bool, typing.Any]] = False,
        probability: typing.Optional[typing.Any] = 0.5,
        min: typing.Optional[typing.Any] = 0.0,
        constant_per_curve: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = True):
    ''' Randomizes existing selection or create new random selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param seed: Seed, Source of randomness
    :type seed: typing.Optional[typing.Any]
    :param partial: Partial, Allow points or curves to be selected partially
    :type partial: typing.Optional[typing.Union[bool, typing.Any]]
    :param probability: Probability, Chance of every point or curve being included in the selection
    :type probability: typing.Optional[typing.Any]
    :param min: Min, Minimum value for the random selection
    :type min: typing.Optional[typing.Any]
    :param constant_per_curve: Constant per Curve, The generated random number is the same for every control point of a curve
    :type constant_per_curve: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass
