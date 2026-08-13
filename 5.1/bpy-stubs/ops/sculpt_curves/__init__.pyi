import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums
import bpy.types

class brush_stroke(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
        | None = None,
        mode: typing.Literal["NORMAL", "INVERT"] | None = "NORMAL",
        brush_toggle: typing.Literal["None", "SMOOTH", "ERASE", "MASK"] | None = "None",
        pen_flip: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Sculpt curves using a brush

                :param execution_context:
                :param undo:
                :param stroke: Stroke, (optional)
                :param mode: Stroke Mode, Action taken when a paint stroke is made (optional)

        NORMAL
        Regular -- Apply brush normally.

        INVERT
        Invert -- Invert action of brush for duration of stroke.
                :param brush_toggle: Temporary Brush Toggle Type, Brush to use for duration of stroke (optional)

        None
        None -- Apply brush normally.

        SMOOTH
        Smooth -- Switch to smooth brush for duration of stroke.

        ERASE
        Erase -- Switch to erase brush for duration of stroke.

        MASK
        Mask -- Switch to mask brush for duration of stroke.
                :param pen_flip: Pen Flip, Whether a tablets eraser mode is being used (optional)
                :return: Result of the operator call.
        """

class min_distance_edit(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change the minimum distance used by the density brush

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_grow(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        distance: float | None = 0.1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select curves which are close to curves that are selected already

        :param execution_context:
        :param undo:
        :param distance: Distance, By how much to grow the selection (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class select_random(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        seed: int | None = 0,
        partial: bool | None = False,
        probability: float | None = 0.5,
        min: float | None = 0.0,
        constant_per_curve: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Randomizes existing selection or create new random selection

        :param execution_context:
        :param undo:
        :param seed: Seed, Source of randomness (in [-inf, inf], optional)
        :param partial: Partial, Allow points or curves to be selected partially (optional)
        :param probability: Probability, Chance of every point or curve being included in the selection (in [0, 1], optional)
        :param min: Min, Minimum value for the random selection (in [0, 1], optional)
        :param constant_per_curve: Constant per Curve, The generated random number is the same for every control point of a curve (optional)
        :return: Result of the operator call.
        """
