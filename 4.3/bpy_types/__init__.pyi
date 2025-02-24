import typing
import collections.abc
import typing_extensions

class _GenericUI:
    @classmethod
    def append(cls, draw_func):
        """Append a draw function to this menu,
        takes the same arguments as the menus draw function

                :param draw_func:
        """

    @classmethod
    def is_extended(cls): ...
    @classmethod
    def prepend(cls, draw_func):
        """Prepend a draw function to this menu, takes the same arguments as
        the menus draw function

                :param draw_func:
        """

    @classmethod
    def remove(cls, draw_func):
        """Remove a draw function that has been added to this menu

        :param draw_func:
        """
