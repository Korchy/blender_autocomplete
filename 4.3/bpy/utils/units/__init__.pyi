"""
This module contains some data/methods regarding units handling.

"""

import typing
import collections.abc
import typing_extensions

def to_string(
    unit_system: str | None,
    unit_category: str | None,
    value: float | None,
    precision: int | None = 3,
    split_unit: bool | None = False,
    compatible_unit: bool | None = False,
) -> str:
    """Convert a given input float value into a string with units.

        :param unit_system: The unit system, from `bpy.utils.units.systems`.
        :type unit_system: str | None
        :param unit_category: The category of data we are converting (length, area, rotation, etc.),
    from `bpy.utils.units.categories`.
        :type unit_category: str | None
        :param value: The value to convert to a string.
        :type value: float | None
        :param precision: Number of digits after the comma.
        :type precision: int | None
        :param split_unit: Whether to use several units if needed (1m1cm), or always only one (1.01m).
        :type split_unit: bool | None
        :param compatible_unit: Whether to use keyboard-friendly units (1m2) or nicer utf-8 ones (1m²).
        :type compatible_unit: bool | None
        :return: The converted string.
        :rtype: str
    """

def to_value(
    unit_system: str | None,
    unit_category: str | None,
    str_input: str | None,
    str_ref_unit: None | str | None = None,
) -> float:
    """Convert a given input string into a float value.

        :param unit_system: The unit system, from `bpy.utils.units.systems`.
        :type unit_system: str | None
        :param unit_category: The category of data we are converting (length, area, rotation, etc.),
    from `bpy.utils.units.categories`.
        :type unit_category: str | None
        :param str_input: The string to convert to a float value.
        :type str_input: str | None
        :param str_ref_unit: A reference string from which to extract a default unit, if none is found in str_input.
        :type str_ref_unit: None | str | None
        :return: The converted/interpreted value.
        :rtype: float
    """

categories: typing.Any
""" Constant value bpy.utils.units.categories(NONE='NONE', LENGTH='LENGTH', AREA='AREA', VOLUME='VOLUME', MASS='MASS', ROTATION='ROTATION', TIME='TIME', TIME_ABSOLUTE='TIME_ABSOLUTE', VELOCITY='VELOCITY', ACCELERATION='ACCELERATION', CAMERA='CAMERA', POWER='POWER', TEMPERATURE='TEMPERATURE', WAVELENGTH='WAVELENGTH', COLOR_TEMPERATURE='COLOR_TEMPERATURE', FREQUENCY='FREQUENCY')
"""

systems: typing.Any
""" Constant value bpy.utils.units.systems(NONE='NONE', METRIC='METRIC', IMPERIAL='IMPERIAL')
"""
