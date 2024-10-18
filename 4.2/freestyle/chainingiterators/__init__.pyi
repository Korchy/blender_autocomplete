"""
This module contains chaining iterators used for the chaining
operation to construct long strokes by concatenating feature edges
according to selected chaining rules.  The module is also intended to
be a collection of examples for defining chaining iterators in Python.

"""

import typing
import collections.abc
import typing_extensions
import freestyle.types

class ChainPredicateIterator:
    """Class hierarchy: `freestyle.types.Iterator` >
    `freestyle.types.ViewEdgeIterator` >
    `freestyle.types.ChainingIterator` >
    `ChainPredicateIterator`A "generic" user-controlled ViewEdge iterator. This iterator is in
    particular built from a unary predicate and a binary predicate.
    First, the unary predicate is evaluated for all potential next
    ViewEdges in order to only keep the ones respecting a certain
    constraint. Then, the binary predicate is evaluated on the current
    ViewEdge together with each ViewEdge of the previous selection. The
    first ViewEdge respecting both the unary predicate and the binary
    predicate is kept as the next one. If none of the potential next
    ViewEdge respects these two predicates, None is returned.
    """

    def __init__(
        self,
        upred: freestyle.types.UnaryPredicate1D,
        bpred: freestyle.types.BinaryPredicate1D,
        restrict_to_selection: bool = True,
        restrict_to_unvisited: bool = True,
        begin: freestyle.types.ViewEdge | None = None,
        orientation: bool = True,
    ):
        """Builds a ChainPredicateIterator from a unary predicate, a binary
        predicate, a starting ViewEdge and its orientation or using the copy constructor.

                :param upred: The unary predicate that the next ViewEdge must satisfy.
                :type upred: freestyle.types.UnaryPredicate1D
                :param bpred: The binary predicate that the next ViewEdge must
        satisfy together with the actual pointed ViewEdge.
                :type bpred: freestyle.types.BinaryPredicate1D
                :param restrict_to_selection: Indicates whether to force the chaining
        to stay within the set of selected ViewEdges or not.
                :type restrict_to_selection: bool
                :param restrict_to_unvisited: Indicates whether a ViewEdge that has
        already been chained must be ignored ot not.
                :type restrict_to_unvisited: bool
                :param begin: The ViewEdge from where to start the iteration.
                :type begin: freestyle.types.ViewEdge | None
                :param orientation: If true, we'll look for the next ViewEdge among
        the ViewEdges that surround the ending ViewVertex of begin. If
        false, we'll search over the ViewEdges surrounding the ending
        ViewVertex of begin.
                :type orientation: bool
        """

    def __init__(self, brother: typing_extensions.Self):
        """Builds a ChainPredicateIterator from a unary predicate, a binary
        predicate, a starting ViewEdge and its orientation or using the copy constructor.

                :param brother: A ChainPredicateIterator object.
                :type brother: typing_extensions.Self
        """

class ChainSilhouetteIterator:
    """Class hierarchy: `freestyle.types.Iterator` >
    `freestyle.types.ViewEdgeIterator` >
    `freestyle.types.ChainingIterator` >
    `ChainSilhouetteIterator`A ViewEdge Iterator used to follow ViewEdges the most naturally. For
    example, it will follow visible ViewEdges of same nature. As soon, as
    the nature or the visibility changes, the iteration stops (by setting
    the pointed ViewEdge to 0). In the case of an iteration over a set of
    ViewEdge that are both Silhouette and Crease, there will be a
    precedence of the silhouette over the crease criterion.
    """

    def __init__(
        self,
        restrict_to_selection: bool = True,
        begin: freestyle.types.ViewEdge | None = None,
        orientation: bool = True,
    ):
        """Builds a ChainSilhouetteIterator from the first ViewEdge used for
        iteration and its orientation or the copy constructor.

                :param restrict_to_selection: Indicates whether to force the chaining
        to stay within the set of selected ViewEdges or not.
                :type restrict_to_selection: bool
                :param begin: The ViewEdge from where to start the iteration.
                :type begin: freestyle.types.ViewEdge | None
                :param orientation: If true, we'll look for the next ViewEdge among
        the ViewEdges that surround the ending ViewVertex of begin. If
        false, we'll search over the ViewEdges surrounding the ending
        ViewVertex of begin.
                :type orientation: bool
        """

    def __init__(self, brother: typing_extensions.Self):
        """Builds a ChainSilhouetteIterator from the first ViewEdge used for
        iteration and its orientation or the copy constructor.

                :param brother: A ChainSilhouetteIterator object.
                :type brother: typing_extensions.Self
        """

class pyChainSilhouetteGenericIterator:
    """Natural chaining iterator that follows the edges of the same nature
    following the topology of objects, with decreasing priority for
    silhouettes, then borders, then suggestive contours, then all other
    edge types.
    """

    def __init__(self, stayInSelection: bool = True, stayInUnvisited: bool = True):
        """Builds a pyChainSilhouetteGenericIterator object.

        :param stayInSelection: True if it is allowed to go out of the selection
        :type stayInSelection: bool
        :param stayInUnvisited: May the same ViewEdge be chained twice
        :type stayInUnvisited: bool
        """

    def init(self): ...
    def traverse(self, iter):
        """

        :param iter:
        """

class pyChainSilhouetteIterator:
    """Natural chaining iterator that follows the edges of the same nature
    following the topology of objects, with decreasing priority for
    silhouettes, then borders, then suggestive contours, then all other edge
    types.  A ViewEdge is only chained once.
    """

    def init(self): ...
    def traverse(self, iter):
        """

        :param iter:
        """

class pyExternalContourChainingIterator:
    """Chains by external contour"""

    def checkViewEdge(self, ve, orientation):
        """

        :param ve:
        :param orientation:
        """

    def init(self): ...
    def traverse(self, iter):
        """

        :param iter:
        """

class pyFillOcclusionsAbsoluteAndRelativeChainingIterator:
    """Chaining iterator that fills small occlusions regardless of the
    selection.
    """

    def __init__(self, percent: float, l: float):
        """Builds a pyFillOcclusionsAbsoluteAndRelativeChainingIterator object.

                :param percent: The maximal length of the occluded part as a
        percentage of the total chain length.
                :type percent: float
                :param l: Absolute length.
                :type l: float
        """

    def init(self): ...
    def traverse(self, iter):
        """

        :param iter:
        """

class pyFillOcclusionsAbsoluteChainingIterator:
    """Chaining iterator that fills small occlusions"""

    def __init__(self, length: int):
        """Builds a pyFillOcclusionsAbsoluteChainingIterator object.

        :param length: The maximum length of the occluded part in pixels.
        :type length: int
        """

    def init(self): ...
    def traverse(self, iter):
        """

        :param iter:
        """

class pyFillOcclusionsRelativeChainingIterator:
    """Chaining iterator that fills small occlusions"""

    def __init__(self, percent: float):
        """Builds a pyFillOcclusionsRelativeChainingIterator object.

                :param percent: The maximal length of the occluded part, expressed
        in a percentage of the total chain length.
                :type percent: float
        """

    def init(self): ...
    def traverse(self, iter):
        """

        :param iter:
        """

class pyFillQi0AbsoluteAndRelativeChainingIterator:
    """Chaining iterator that fills small occlusions regardless of the
    selection.
    """

    def __init__(self, percent: float, l: float):
        """Builds a pyFillQi0AbsoluteAndRelativeChainingIterator object.

                :param percent: The maximal length of the occluded part as a
        percentage of the total chain length.
                :type percent: float
                :param l: Absolute length.
                :type l: float
        """

    def init(self): ...
    def traverse(self, iter):
        """

        :param iter:
        """

class pyNoIdChainSilhouetteIterator:
    """Natural chaining iterator that follows the edges of the same nature
    following the topology of objects, with decreasing priority for
    silhouettes, then borders, then suggestive contours, then all other edge
    types.  It won't chain the same ViewEdge twice.
    """

    def __init__(self, stayInSelection: bool = True):
        """Builds a pyNoIdChainSilhouetteIterator object.

        :param stayInSelection: True if it is allowed to go out of the selection
        :type stayInSelection: bool
        """

    def init(self): ...
    def traverse(self, iter):
        """

        :param iter:
        """

class pySketchyChainSilhouetteIterator:
    """Natural chaining iterator with a sketchy multiple touch.  It chains the
    same ViewEdge multiple times to achieve a sketchy effect.
    """

    def __init__(self, nRounds: int = 3, stayInSelection: bool = True):
        """Builds a pySketchyChainSilhouetteIterator object.

        :param nRounds: Number of times every Viewedge is chained.
        :type nRounds: int
        :param stayInSelection: if False, edges outside of the selection can be chained.
        :type stayInSelection: bool
        """

    def init(self): ...
    def make_sketchy(self, ve):
        """Creates the sketchy effect by causing the chain to run from
        the start again. (loop over itself again)

                :param ve:
        """

    def traverse(self, iter):
        """

        :param iter:
        """

class pySketchyChainingIterator:
    """Chaining iterator designed for sketchy style. It chains the same
    ViewEdge several times in order to produce multiple strokes per
    ViewEdge.
    """

    def init(self): ...
    def traverse(self, iter):
        """

        :param iter:
        """
