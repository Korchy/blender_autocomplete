import sys
import typing

GenericType = typing.TypeVar("GenericType")


class RestrictBlend:
    context = None
    ''' '''

    data = None
    ''' '''


class _RestrictContext:
    preferences = None
    ''' '''

    window_manager = None
    ''' '''


class _RestrictData:
    pass
