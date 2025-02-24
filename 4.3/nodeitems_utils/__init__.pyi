import typing
import collections.abc
import typing_extensions

class NodeCategory:
    @classmethod
    def poll(cls, _context):
        """

        :param _context:
        """

class NodeItem:
    label: typing.Any
    translation_context: typing.Any

    @staticmethod
    def draw(self_, layout, _context):
        """

        :param self_:
        :param layout:
        :param _context:
        """

class NodeItemCustom: ...

def draw_node_categories_menu(self_, context): ...
def has_node_categories(context): ...
def node_categories_iter(context): ...
def node_items_iter(context): ...
def register_node_categories(identifier, cat_list): ...
def unregister_node_cat_types(cats): ...
def unregister_node_categories(identifier=None): ...
