import typing
import collections.abc
import typing_extensions
import bpy.types

def brush_stroke(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH", "ERASE"] | None = "NORMAL",
):
    """Sculpt curves using a brush

        :type execution_context: int | str | None
        :type undo: bool | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL
    Regular -- Apply brush normally.

    INVERT
    Invert -- Invert action of brush for duration of stroke.

    SMOOTH
    Smooth -- Switch brush to smooth mode for duration of stroke.

    ERASE
    Erase -- Switch brush to erase mode for duration of stroke.
        :type mode: typing.Literal['NORMAL','INVERT','SMOOTH','ERASE'] | None
    """

def min_distance_edit(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Change the minimum distance used by the density brush

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_grow(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    distance: float | None = 0.1,
):
    """Select curves which are close to curves that are selected already

    :type execution_context: int | str | None
    :type undo: bool | None
    :param distance: Distance, By how much to grow the selection
    :type distance: float | None
    """

def select_random(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    seed: int | None = 0,
    partial: bool | None = False,
    probability: float | None = 0.5,
    min: float | None = 0.0,
    constant_per_curve: bool | None = True,
):
    """Randomizes existing selection or create new random selection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param seed: Seed, Source of randomness
    :type seed: int | None
    :param partial: Partial, Allow points or curves to be selected partially
    :type partial: bool | None
    :param probability: Probability, Chance of every point or curve being included in the selection
    :type probability: float | None
    :param min: Min, Minimum value for the random selection
    :type min: float | None
    :param constant_per_curve: Constant per Curve, The generated random number is the same for every control point of a curve
    :type constant_per_curve: bool | None
    """
