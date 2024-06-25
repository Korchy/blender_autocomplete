import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def compat_str(text, line_length=0): ...
def graph_armature(
    obj, filepath, FAKE_PARENT=True, CONSTRAINTS=True, DRIVERS=True, XTRA_INFO=True
): ...
