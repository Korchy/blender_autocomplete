"""
This module provides access to GPU Platform definitions.

"""

import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def backend_type_get() -> str:
    """Get actuve GPU backend.

    :return: Backend type ('OPENGL', 'VULKAN', 'METAL', 'NONE', 'UNKNOWN').
    :rtype: str
    """

    ...

def device_type_get() -> str:
    """Get GPU device type.

    :return: Device type ('APPLE', 'NVIDIA', 'AMD', 'INTEL', 'SOFTWARE', 'QUALCOMM', 'UNKNOWN').
    :rtype: str
    """

    ...

def renderer_get() -> str:
    """Get GPU to be used for rendering.

    :return: GPU name.
    :rtype: str
    """

    ...

def vendor_get() -> str:
    """Get GPU vendor.

    :return: Vendor name.
    :rtype: str
    """

    ...

def version_get() -> str:
    """Get GPU driver version.

    :return: Driver version.
    :rtype: str
    """

    ...
