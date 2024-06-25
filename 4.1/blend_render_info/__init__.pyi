import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class RawBlendFileReader:
    """Return a file handle to the raw blend file data (abstracting compressed formats)."""

    ...

def main(): ...
def read_blend_rend_chunk(filepath): ...
