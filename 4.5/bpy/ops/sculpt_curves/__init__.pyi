import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

def brush_stroke(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH", "ERASE"] | None = "NORMAL",
    pen_flip: bool | None = False,
) -> None:
    """Sculpt curves using a brush

        :param stroke: Stroke
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL
    Regular -- Apply brush normally.

    INVERT
    Invert -- Invert action of brush for duration of stroke.

    SMOOTH
    Smooth -- Switch brush to smooth mode for duration of stroke.

    ERASE
    Erase -- Switch brush to erase mode for duration of stroke.
        :param pen_flip: Pen Flip, Whether a tablets eraser mode is being used
    """

def min_distance_edit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Change the minimum distance used by the density brush"""

def select_grow(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    distance: float | None = 0.1,
) -> None:
    """Select curves which are close to curves that are selected already

    :param distance: Distance, By how much to grow the selection
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
) -> None:
    """Randomizes existing selection or create new random selection

    :param seed: Seed, Source of randomness
    :param partial: Partial, Allow points or curves to be selected partially
    :param probability: Probability, Chance of every point or curve being included in the selection
    :param min: Min, Minimum value for the random selection
    :param constant_per_curve: Constant per Curve, The generated random number is the same for every control point of a curve
    """
