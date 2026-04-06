import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def compat_str(text, line_length=0) -> None: ...
def graph_armature(
    obj, filepath, FAKE_PARENT=True, CONSTRAINTS=True, DRIVERS=True, XTRA_INFO=True
) -> None: ...
