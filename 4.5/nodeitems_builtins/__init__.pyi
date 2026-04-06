import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import nodeitems_utils

class SortedNodeCategory(nodeitems_utils.NodeCategory): ...

class CompositorNodeCategory(SortedNodeCategory):
    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class ShaderNodeCategory(SortedNodeCategory):
    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

def register() -> None: ...
def unregister() -> None: ...
