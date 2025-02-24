"""
This module provides access to blenders bmesh data structures.

bmesh.ops.rst
bmesh.types.rst
bmesh.utils.rst
bmesh.geometry.rst

:maxdepth: 1
:caption: Submodules

"""

import typing
import collections.abc
import typing_extensions
import bmesh.types
import bpy.types

from . import geometry as geometry
from . import ops as ops
from . import types as types
from . import utils as utils

def from_edit_mesh(mesh: bpy.types.Mesh) -> bmesh.types.BMesh:
    """Return a BMesh from this mesh, currently the mesh must already be in editmode.

    :param mesh: The editmode mesh.
    :type mesh: bpy.types.Mesh
    :return: the BMesh associated with this mesh.
    :rtype: bmesh.types.BMesh
    """

def new(use_operators: bool = True) -> bmesh.types.BMesh:
    """

    :param use_operators: Support calling operators in `bmesh.ops` (uses some extra memory per vert/edge/face).
    :type use_operators: bool
    :return: Return a new, empty BMesh.
    :rtype: bmesh.types.BMesh
    """

def update_edit_mesh(
    mesh: bpy.types.Mesh, loop_triangles: bool = True, destructive: bool = True
):
    """Update the mesh after changes to the BMesh in editmode,
    optionally recalculating n-gon tessellation.

        :param mesh: The editmode mesh.
        :type mesh: bpy.types.Mesh
        :param loop_triangles: Option to recalculate n-gon tessellation.
        :type loop_triangles: bool
        :param destructive: Use when geometry has been added or removed.
        :type destructive: bool
    """
