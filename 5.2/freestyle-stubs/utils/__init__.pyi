"""
This module contains helper functions used for Freestyle style module
writing.

freestyle.utils.ContextFunctions.rst

:maxdepth: 1
:caption: Submodules

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types
import freestyle.types
import mathutils

from . import ContextFunctions as ContextFunctions

class BoundingBox:
    """Object representing a bounding box consisting out of 2 2D vectors"""

    def inside(self, other: typing_extensions.Self) -> bool:
        """True if self inside other, False otherwise.

        :param other: Another bounding box to test containment against.
        :return:
        """

    @classmethod
    def from_sequence(
        cls,
        sequence: collections.abc.Iterable[
            collections.abc.Sequence[float] | mathutils.Vector
        ],
    ) -> typing_extensions.Self:
        """BoundingBox from sequence of 2D or 3D Vector objects.

        :param sequence: An iterable of vectors to compute the box from.
        :return:
        """

class StrokeCollector:
    """Collects and Stores stroke objects"""

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """

        :param stroke: The stroke to collect.
        """

def angle_x_normal(it: freestyle.types.Interface0DIterator) -> float:
    """unsigned angle between a Points normal and the X axis, in radians

    :param it: An iterator over Interface0D objects.
    """

def bound(lower: float, x: float, higher: float) -> float:
    """Returns x bounded by a maximum and minimum value. Equivalent to:
    return min(max(x, lower), higher)

        :param lower: Lower bound.
        :param x: Value to clamp.
        :param higher: Upper bound.
    """

def bounding_box(
    stroke: freestyle.types.Stroke,
) -> tuple[mathutils.Vector, mathutils.Vector]:
    """Returns the maximum and minimum coordinates (the bounding box) of the strokes vertices

    :param stroke: A stroke.
    """

def curvature_from_stroke_vertex(svert: freestyle.types.StrokeVertex) -> None | float:
    """

    :param svert: A stroke vertex.
    """

def find_matching_vertex(
    id: freestyle.types.Id, it: freestyle.types.AdjacencyIterator
) -> None | freestyle.types.ViewEdge:
    """Finds the matching vertex, or returns None.

    :param id: The ID to match.
    :param it: An iterator over candidate ViewEdges.
    """

def getCurrentScene() -> bpy.types.Scene:
    """Returns the current scene.

    :return: The current scene.
    """

def get_chain_length(ve: freestyle.types.ViewEdge, orientation: bool) -> float:
    """Returns the 2d length of a given ViewEdge.

    :param ve: The ViewEdge whose chain length to compute.
    :param orientation: Direction in which to traverse the chain.
    """

def get_object_name(stroke: freestyle.types.Stroke) -> None | str:
    """Returns the name of the object that this stroke is drawn on.

    :param stroke: A stroke.
    """

def get_strokes() -> None:
    """Get all strokes that are currently available"""

def get_test_stroke() -> None:
    """Returns a static stroke object for testing"""

def integrate(
    func: freestyle.types.UnaryFunction0D,
    it: freestyle.types.Interface0DIterator,
    it_end: freestyle.types.Interface0DIterator,
    integration_type: freestyle.types.IntegrationType,
) -> float:
    """Returns a single value from a set of values evaluated at each 0D
    element of this 1D element.

        :param func: The UnaryFunction0D used to compute a value at each
    Interface0D.
        :param it: The Interface0DIterator used to iterate over the 0D
    elements of this 1D element. The integration will occur over
    the 0D elements starting from the one pointed by it.
        :param it_end: The Interface0DIterator pointing the end of the 0D
    elements of the 1D element.
        :param integration_type: The integration method used to compute a
    single value from a set of values.
        :return: The single value obtained for the 1D element. The return
    value type is float if func is of the `UnaryFunction0DDouble`
    or `UnaryFunction0DFloat` type, and int if func is of the
    `UnaryFunction0DUnsigned` type.
    """

def is_poly_clockwise(stroke: freestyle.types.Stroke) -> bool:
    """True if the stroke is orientated in a clockwise way, False otherwise

    :param stroke: A stroke whose orientation is tested.
    """

def iter_distance_along_stroke(stroke: freestyle.types.Stroke) -> None:
    """Yields the absolute distance along the stroke up to the current vertex.

    :param stroke: A stroke.
    """

def iter_distance_from_camera(
    stroke: freestyle.types.Stroke, range_min: float, range_max: float, normfac: float
) -> None:
    """Yields the distance to the camera relative to the maximum
    possible distance for every stroke vertex, constrained by
    given minimum and maximum values.

        :param stroke: A stroke.
        :param range_min: Distances below this value are clamped to 0.
        :param range_max: Distances above this value are clamped to 1.
        :param normfac: Normalization factor applied to distance - range_min.
    """

def iter_distance_from_object(
    stroke: freestyle.types.Stroke,
    location: collections.abc.Sequence[float] | mathutils.Vector,
    range_min: float,
    range_max: float,
    normfac: float,
) -> None:
    """yields the distance to the given object relative to the maximum
    possible distance for every stroke vertex, constrained by
    given minimum and maximum values.

        :param stroke: A stroke.
        :param location: Reference location in 3D space.
        :param range_min: Distances below this value are clamped to 0.
        :param range_max: Distances above this value are clamped to 1.
        :param normfac: Normalization factor applied to distance - range_min.
    """

def iter_material_value(
    stroke: freestyle.types.Stroke,
    func: collections.abc.Callable[
        [freestyle.types.Interface0DIterator], freestyle.types.Material
    ],
    attribute: str,
) -> None:
    """Yields a specific material attribute from the vertex underlying material.

    :param stroke: A stroke.
    :param func: A function returning a material for the iterators current vertex.
    :param attribute: The material attribute name (e.g. LINE, DIFF, ALPHA).
    """

def iter_t2d_along_stroke(stroke: freestyle.types.Stroke) -> None:
    """Yields the progress along the stroke.

    :param stroke: A stroke.
    """

def material_from_fedge(fe: freestyle.types.FEdge) -> None | freestyle.types.Material:
    """Get the diffuse RGBA color from an FEdge.

    :param fe: An FEdge.
    """

def normal_at_I0D(it: freestyle.types.Interface0DIterator) -> mathutils.Vector:
    """

    :param it: An iterator over Interface0D objects.
    """

def pairwise(
    iterable: collections.abc.Iterable[typing.Any],
    types: None | tuple[typing.Any, ...] | None = None,
) -> None:
    """Yields a tuple containing the previous and current object.

        :param iterable: An iterable of items.
        :param types: Container types for which the iterators incremented()
    method is used instead of standard tee-based pairing. When None
    defaults to (Stroke, StrokeVertexIterator).
    """

def rgb_to_bw(r: float, g: float, b: float) -> float:
    """Method to convert rgb to a bw intensity value.

    :param r: Red channel (0..1).
    :param g: Green channel (0..1).
    :param b: Blue channel (0..1).
    """

def simplify(
    points: collections.abc.Sequence[
        collections.abc.Sequence[float] | mathutils.Vector
    ],
    tolerance: float,
) -> tuple:
    """Simplifies a set of points.

    :param points: Points to simplify.
    :param tolerance: Maximum allowed deviation from the original curve.
    """

def stroke_curvature(it: freestyle.types.StrokeVertexIterator) -> None:
    """Compute the 2D curvature at the stroke vertex pointed by the iterator it.
    K = 1 / R
    where R is the radius of the circle going through the current vertex and its neighbors

        :param it: An iterator over a strokes vertices.
    """

def stroke_normal(stroke: freestyle.types.Stroke) -> None:
    """Compute the 2D normal at the stroke vertex pointed by the iterator
    it.  It is noted that Normal2DF0D computes normals based on
    underlying FEdges instead, which is inappropriate for strokes when
    they have already been modified by stroke geometry modifiers.The returned normals are dynamic: they update when the
    vertex position (and therefore the vertex normal) changes.
    for use in geometry modifiers it is advised to
    cast this generator function to a tuple or list

        :param stroke: A stroke.
    """

def tripplewise(iterable: collections.abc.Iterable[typing.Any]) -> None:
    """Yields a tuple containing the current object and its immediate neighbors.

    :param iterable: An iterable of items.
    """
