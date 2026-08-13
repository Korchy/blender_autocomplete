import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class RestrictBlend:
    context: typing.Any
    data: typing.Any

class _RestrictContext:
    preferences: typing.Any
    window_manager: typing.Any

class _RestrictData: ...
