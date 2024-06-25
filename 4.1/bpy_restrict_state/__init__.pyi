import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class RestrictBlend:
    context: typing.Any
    data: typing.Any

class _RestrictContext:
    preferences: typing.Any
    window_manager: typing.Any

class _RestrictData: ...
