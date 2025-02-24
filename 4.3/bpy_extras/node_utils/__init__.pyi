import typing
import collections.abc
import typing_extensions

def connect_sockets(input, output):
    """Connect sockets in a node tree.This is useful because the links created through the normal Python API are
    invalid when one of the sockets is a virtual socket (grayed out sockets in
    Group Input and Group Output nodes).It replaces node_tree.links.new(input, output)

    """

def find_base_socket_type(socket):
    """Find the base class of the socket.Sockets can have a subtype such as NodeSocketFloatFactor,
    but only the base type is allowed, e. g. NodeSocketFloat

    """

def find_node_input(node, name): ...
