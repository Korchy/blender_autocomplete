import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class _GenericUI:
    @classmethod
    def append(cls, draw_func) -> None:
        """Append a draw function to this menu,
        takes the same arguments as the menus draw function

                :param draw_func:
        """

    @classmethod
    def is_extended(cls) -> None: ...
    @classmethod
    def prepend(cls, draw_func) -> None:
        """Prepend a draw function to this menu, takes the same arguments as
        the menus draw function

                :param draw_func:
        """

    @classmethod
    def remove(cls, draw_func) -> None:
        """Remove a draw function that has been added to this menu

        :param draw_func:
        """
