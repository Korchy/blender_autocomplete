"""
This module contains some data/methods regarding units handling.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def to_string(
    unit_system: str | None,
    unit_category: str | None,
    value: float | None,
    *,
    precision: int | None = 3,
    split_unit: bool | None = False,
    compatible_unit: bool | None = False,
) -> str:
    """Convert a given input float value into a string with units.

        :param unit_system: The unit system, from `bpy.utils.units.systems`.
        :param unit_category: The category of data we are converting (length, area, rotation, etc.),
    from `bpy.utils.units.categories`.
        :param value: The value to convert to a string.
        :param precision: Number of digits after the comma.
        :param split_unit: Whether to use several units if needed (1m1cm), or always only one (1.01m).
        :param compatible_unit: Whether to use keyboard-friendly units (1m2) or nicer UTF8 ones (1m).
        :return: The converted string.
    """

def to_value(
    unit_system: str | None,
    unit_category: str | None,
    str_input: str | None,
    *,
    str_ref_unit: None | str | None = None,
) -> float:
    """Convert a given input string into a float value.

        :param unit_system: The unit system, from `bpy.utils.units.systems`.
        :param unit_category: The category of data we are converting (length, area, rotation, etc.),
    from `bpy.utils.units.categories`.
        :param str_input: The string to convert to a float value.
        :param str_ref_unit: A reference string from which to extract a default unit, if none is found in str_input.
        :return: The converted/interpreted value.
    """

categories: typing.Any
""" Constant value bpy.utils.units.categories(NONE=NONE, LENGTH=LENGTH, AREA=AREA, VOLUME=VOLUME, MASS=MASS, ROTATION=ROTATION, TIME=TIME, TIME_ABSOLUTE=TIME_ABSOLUTE, VELOCITY=VELOCITY, ACCELERATION=ACCELERATION, CAMERA=CAMERA, POWER=POWER, TEMPERATURE=TEMPERATURE, WAVELENGTH=WAVELENGTH, COLOR_TEMPERATURE=COLOR_TEMPERATURE, FREQUENCY=FREQUENCY)
"""

systems: typing.Any
""" Constant value bpy.utils.units.systems(NONE=NONE, METRIC=METRIC, IMPERIAL=IMPERIAL)
"""
