import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

def connect_sockets(input: bpy.types.NodeSocket, output: bpy.types.NodeSocket) -> None:
    """Connect sockets in a node tree.This is useful because the links created through the normal Python API are
    invalid when one of the sockets is a virtual socket (grayed out sockets in
    Group Input and Group Output nodes).It replaces node_tree.links.new(input, output)

        :param input: The input socket.
        :param output: The output socket.
    """

def find_base_socket_type(socket: bpy.types.NodeSocket) -> str:
    """Find the base class of the socket.Sockets can have a subtype such as NodeSocketFloatFactor,
    but only the base type is allowed, e.g. NodeSocketFloat

        :param socket: The socket to find the base type for.
        :return: The base socket type identifier.
    """

def find_node_input(node: bpy.types.Node, name: str) -> None | bpy.types.NodeSocket:
    """Find a node input socket by name.Note that names are not unique, returns the first match.

    :param node: The node to search.
    :param name: The name of the input socket.
    :return: The input socket or None if not found.
    """
