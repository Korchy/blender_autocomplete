"""
This module provides access to GPU Platform definitions.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def backend_type_get() -> str:
    """Get actuve GPU backend.

    :return: Backend type (OPENGL, VULKAN, METAL, NONE, UNKNOWN).
    """

def device_type_get() -> str:
    """Get GPU device type.

    :return: Device type (APPLE, NVIDIA, AMD, INTEL, SOFTWARE, QUALCOMM, UNKNOWN).
    """

def renderer_get() -> str:
    """Get GPU to be used for rendering.

    :return: GPU name.
    """

def vendor_get() -> str:
    """Get GPU vendor.

    :return: Vendor name.
    """

def version_get() -> str:
    """Get GPU driver version.

    :return: Driver version.
    """
