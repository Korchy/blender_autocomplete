import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def open_external_editor(filepath, line, column): ...
