"""
This module provides access to the global GPU compute functions.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import gpu.types

def dispatch(
    shader: gpu.types.GPUShader, groups_x_len: int, groups_y_len: int, groups_z_len: int
) -> None:
    """Dispatches GPU compute.

    :param shader: The shader that you want to dispatch.
    :param groups_x_len: Int for group x length:
    :param groups_y_len: Int for group y length:
    :param groups_z_len: Int for group z length:
    """
