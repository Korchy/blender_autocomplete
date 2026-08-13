"""
This module provides bmesh utility functions for splitting, joining, and modifying mesh elements.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bmesh.types

def edge_rotate(
    edge: bmesh.types.BMEdge, ccw: bool = False
) -> None | bmesh.types.BMEdge:
    """Rotate the edge and return the newly created edge.
    If rotating the edge fails, None will be returned.

        :param edge: The edge to rotate.
        :param ccw: When True the edge will be rotated counter clockwise.
        :return: The newly rotated edge.
    """

def edge_split(
    edge: bmesh.types.BMEdge, vert: bmesh.types.BMVert, fac: float
) -> tuple[bmesh.types.BMEdge, bmesh.types.BMVert]:
    """Split an edge, return the newly created data.

    :param edge: The edge to split.
    :param vert: One of the verts on the edge, defines the split direction.
    :param fac: The point on the edge where the new vert will be created [0 - 1].
    :return: The newly created (edge, vert) pair.
    """

def face_flip(face: bmesh.types.BMFace) -> None:
    """Flip the faces direction.

    :param face: Face to flip.
    """

def face_join(
    faces: collections.abc.Sequence[bmesh.types.BMFace], remove: bool = True
) -> None | bmesh.types.BMFace:
    """Joins a sequence of faces.

    :param faces: Sequence of faces.
    :param remove: Remove the edges and vertices between the faces.
    :return: The newly created face or None on failure.
    """

def face_split(
    face: bmesh.types.BMFace,
    vert_a: bmesh.types.BMVert,
    vert_b: bmesh.types.BMVert,
    *,
    coords: collections.abc.Sequence[collections.abc.Sequence[float]] = (),
    use_exist: bool = True,
    source: None | bmesh.types.BMEdge | None = None,
) -> tuple[bmesh.types.BMFace, bmesh.types.BMLoop]:
    """Face split with optional intermediate points.

    :param face: The face to cut.
    :param vert_a: First vertex to cut in the face (face must contain the vert).
    :param vert_b: Second vertex to cut in the face (face must contain the vert).
    :param coords: Optional sequence of 3D points in between vert_a and vert_b.
    :param use_exist: Use an existing edge if it exists (only used when coords argument is empty or omitted)
    :param source: Newly created edge will copy settings from this one.
    :return: The newly created face and loop.
    """

def face_split_edgenet(
    face: bmesh.types.BMFace, edgenet: collections.abc.Sequence[bmesh.types.BMEdge]
) -> tuple[bmesh.types.BMFace, ...]:
    """Splits a face into any number of regions defined by an edgenet.

    :param face: The face to split.
    :param edgenet: Sequence of edges.
    :return: The newly created faces.
    """

def face_vert_separate(
    face: bmesh.types.BMFace, vert: bmesh.types.BMVert
) -> None | bmesh.types.BMVert:
    """Rip a vertex in a face away and add a new vertex.

    :param face: The face to separate.
    :param vert: A vertex in the face to separate.
    :return: The newly created vertex or None on failure.
    """

def loop_separate(loop: bmesh.types.BMLoop) -> None | bmesh.types.BMVert:
    """Rip a vertex in a face away and add a new vertex.

    :param loop: The loop to separate.
    :return: The newly created vertex or None on failure.
    """

def uv_select_check(
    bm: bmesh.types.BMesh,
    /,
    *,
    sync: bool = True,
    flush: bool = False,
    contiguous: bool = False,
) -> None | dict[str, int]:
    """Check UV selection state for consistency issues.

    :param bm: The BMesh to check.
    :param sync: Check the data is properly synchronized between UVs and the underlying mesh. Failure to synchronize with the mesh selection may cause tools not to behave properly.
    :param flush: Check the selection has been properly flushed between elements (based on the current `bmesh.types.BMesh.select_mode`).
    :param contiguous: Check connected UVs and edges have a matching selection state.
    :return: An error dictionary or None when there are no errors found.
    """

def vert_collapse_edge(
    vert: bmesh.types.BMVert, edge: bmesh.types.BMEdge
) -> bmesh.types.BMEdge:
    """Collapse a vertex into an edge.

    :param vert: The vert that will be collapsed.
    :param edge: The edge to collapse into.
    :return: The resulting edge from the collapse operation.
    """

def vert_collapse_faces(
    vert: bmesh.types.BMVert, edge: bmesh.types.BMEdge, fac: float, join_faces: bool
) -> bmesh.types.BMEdge:
    """Collapses a vertex that has only two manifold edges onto a vertex it shares an edge with.

    :param vert: The vert that will be collapsed.
    :param edge: The edge to collapse into.
    :param fac: The factor to use when merging customdata [0 - 1].
    :param join_faces: When true the faces around the vertex will be joined otherwise collapse the vertex by merging the 2 edges this vertex connects to into one.
    :return: The resulting edge from the collapse operation.
    """

def vert_dissolve(vert: bmesh.types.BMVert) -> bool:
    """Dissolve this vertex (will be removed).

    :param vert: The vert to be dissolved.
    :return: True when the vertex dissolve is successful.
    """

def vert_separate(
    vert: bmesh.types.BMVert, edges: collections.abc.Sequence[bmesh.types.BMEdge]
) -> tuple[bmesh.types.BMVert, ...]:
    """Separate this vertex at every edge.

    :param vert: The vert to be separated.
    :param edges: The edges to separate.
    :return: The newly separated verts (including the vertex passed).
    """

def vert_splice(vert: bmesh.types.BMVert, vert_target: bmesh.types.BMVert) -> None:
    """Splice vert into vert_target, merging them.

    :param vert: The vertex to be removed.
    :param vert_target: The vertex to merge into.
    """
