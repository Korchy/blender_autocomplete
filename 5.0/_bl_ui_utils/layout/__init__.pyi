import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def operator_context(layout, op_context) -> None:
    """Context manager that temporarily overrides the operator context."""
