import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def operator_context(layout, op_context):
    """Context manager that temporarily overrides the operator context."""

    ...
