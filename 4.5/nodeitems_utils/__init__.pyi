import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class NodeCategory:
    @classmethod
    def poll(cls, _context) -> None:
        """

        :param _context:
        """

class NodeItem:
    label: typing.Any
    translation_context: typing.Any

    @staticmethod
    def draw(self_, layout, _context) -> None:
        """

        :param self_:
        :param layout:
        :param _context:
        """

class NodeItemCustom: ...

def draw_node_categories_menu(self_, context) -> None: ...
def has_node_categories(context) -> None: ...
def node_categories_iter(context) -> None: ...
def node_items_iter(context) -> None: ...
def register_node_categories(identifier, cat_list) -> None: ...
def unregister_node_cat_types(cats) -> None: ...
def unregister_node_categories(identifier=None) -> None: ...
