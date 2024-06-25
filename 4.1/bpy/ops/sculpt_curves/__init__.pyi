import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def brush_stroke(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: str | None = "NORMAL",
):
    """Sculpt curves using a brush

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
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
        :type mode: str | None
    """

    ...

def min_distance_edit(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Change the minimum distance used by the density brush

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_grow(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    distance: typing.Any | None = 0.1,
):
    """Select curves which are close to curves that are selected already

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param distance: Distance, By how much to grow the selection
    :type distance: typing.Any | None
    """

    ...

def select_random(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    seed: typing.Any | None = 0,
    partial: bool | typing.Any | None = False,
    probability: typing.Any | None = 0.5,
    min: typing.Any | None = 0.0,
    constant_per_curve: bool | typing.Any | None = True,
):
    """Randomizes existing selection or create new random selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param seed: Seed, Source of randomness
    :type seed: typing.Any | None
    :param partial: Partial, Allow points or curves to be selected partially
    :type partial: bool | typing.Any | None
    :param probability: Probability, Chance of every point or curve being included in the selection
    :type probability: typing.Any | None
    :param min: Min, Minimum value for the random selection
    :type min: typing.Any | None
    :param constant_per_curve: Constant per Curve, The generated random number is the same for every control point of a curve
    :type constant_per_curve: bool | typing.Any | None
    """

    ...
