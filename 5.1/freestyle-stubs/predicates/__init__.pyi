"""
This module contains predicates operating on vertices (0D elements)
and polylines (1D elements).  It is also intended to be a collection
of examples for predicate definition in Python.

User-defined predicates inherit one of the following base classes,
depending on the object type (0D or 1D) to operate on and the arity
(unary or binary):

* freestyle.types.BinaryPredicate0D
* freestyle.types.BinaryPredicate1D
* freestyle.types.UnaryPredicate0D
* freestyle.types.UnaryPredicate1D

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import freestyle.types

class AndBP1D: ...
class AndUP1D: ...

class ContourUP1D:
    """Class hierarchy: `freestyle.types.UnaryPredicate1D` > `ContourUP1D`"""

    def __call__(self, inter: freestyle.types.Interface1D) -> bool:
        """Returns true if the Interface1D is a contour. An Interface1D is a
        contour if it is bordered by a different shape on each of its sides.

                :param inter: An Interface1D object.
                :return: True if the Interface1D is a contour, false otherwise.
        """

class DensityLowerThanUP1D:
    """Class hierarchy: `freestyle.types.UnaryPredicate1D` > `DensityLowerThanUP1D`"""

    def __init__(self, threshold: float, sigma: float = 2.0) -> None:
        """Builds a DensityLowerThanUP1D object.

                :param threshold: The value of the threshold density. Any Interface1D
        having a density lower than this threshold will match.
                :param sigma: The sigma value defining the density evaluation window
        size used in the `freestyle.functions.DensityF0D` functor.
        """

    def __call__(self, inter: freestyle.types.Interface1D) -> bool:
        """Returns true if the density evaluated for the Interface1D is less
        than a user-defined density value.

                :param inter: An Interface1D object.
                :return: True if the density is lower than a threshold.
        """

class EqualToChainingTimeStampUP1D:
    """Class hierarchy: `freestyle.types.UnaryPredicate1D` > `freestyle.types.EqualToChainingTimeStampUP1D`"""

    def __init__(self, ts: int) -> None:
        """Builds a EqualToChainingTimeStampUP1D object.

        :param ts: A time stamp value.
        """

    def __call__(self, inter: freestyle.types.Interface1D) -> bool:
        """Returns true if the Interface1Ds time stamp is equal to a certain
        user-defined value.

                :param inter: An Interface1D object.
                :return: True if the time stamp is equal to a user-defined value.
        """

class EqualToTimeStampUP1D:
    """Class hierarchy: `freestyle.types.UnaryPredicate1D` > `EqualToTimeStampUP1D`"""

    def __init__(self, ts: int) -> None:
        """Builds a EqualToTimeStampUP1D object.

        :param ts: A time stamp value.
        """

    def __call__(self, inter: freestyle.types.Interface1D) -> bool:
        """Returns true if the Interface1Ds time stamp is equal to a certain
        user-defined value.

                :param inter: An Interface1D object.
                :return: True if the time stamp is equal to a user-defined value.
        """

class ExternalContourUP1D:
    """Class hierarchy: `freestyle.types.UnaryPredicate1D` > `ExternalContourUP1D`"""

    def __call__(self, inter: freestyle.types.Interface1D) -> bool:
        """Returns true if the Interface1D is an external contour.
        An Interface1D is an external contour if it is bordered by no shape on
        one of its sides.

                :param inter: An Interface1D object.
                :return: True if the Interface1D is an external contour, false
        otherwise.
        """

class FalseBP1D:
    """Class hierarchy: `freestyle.types.BinaryPredicate1D` > `FalseBP1D`"""

    def __call__(
        self, inter1: freestyle.types.Interface1D, inter2: freestyle.types.Interface1D
    ) -> bool:
        """Always returns false.

        :param inter1: The first Interface1D object.
        :param inter2: The second Interface1D object.
        :return: False.
        """

class FalseUP0D:
    """Class hierarchy: `freestyle.types.UnaryPredicate0D` > `FalseUP0D`"""

    def __call__(self, it: freestyle.types.Interface0DIterator) -> bool:
        """Always returns false.

        :param it: An Interface0DIterator object.
        :return: False.
        """

class FalseUP1D:
    """Class hierarchy: `freestyle.types.UnaryPredicate1D` > `FalseUP1D`"""

    def __call__(self, inter: freestyle.types.Interface1D) -> bool:
        """Always returns false.

        :param inter: An Interface1D object.
        :return: False.
        """

class Length2DBP1D:
    """Class hierarchy: `freestyle.types.BinaryPredicate1D` > `Length2DBP1D`"""

    def __call__(
        self, inter1: freestyle.types.Interface1D, inter2: freestyle.types.Interface1D
    ) -> bool:
        """Returns true if the 2D length of inter1 is less than the 2D length
        of inter2.

                :param inter1: The first Interface1D object.
                :param inter2: The second Interface1D object.
                :return: True or false.
        """

class MaterialBP1D:
    """Checks whether the two supplied ViewEdges have the same material."""

class NotBP1D: ...
class NotUP1D: ...
class ObjectNamesUP1D: ...
class OrBP1D: ...
class OrUP1D: ...
class QuantitativeInvisibilityRangeUP1D: ...

class QuantitativeInvisibilityUP1D:
    """Class hierarchy: `freestyle.types.UnaryPredicate1D` > `QuantitativeInvisibilityUP1D`"""

    def __init__(self, qi: int = 0) -> None:
        """Builds a QuantitativeInvisibilityUP1D object.

                :param qi: The Quantitative Invisibility you want the Interface1D to
        have.
        """

    def __call__(self, inter: freestyle.types.Interface1D) -> bool:
        """Returns true if the Quantitative Invisibility evaluated at an
        Interface1D, using the
        `freestyle.functions.QuantitativeInvisibilityF1D` functor,
        equals a certain user-defined value.

                :param inter: An Interface1D object.
                :return: True if Quantitative Invisibility equals a user-defined
        value.
        """

class SameShapeIdBP1D:
    """Class hierarchy: `freestyle.types.BinaryPredicate1D` > `SameShapeIdBP1D`"""

    def __call__(
        self, inter1: freestyle.types.Interface1D, inter2: freestyle.types.Interface1D
    ) -> bool:
        """Returns true if inter1 and inter2 belong to the same shape.

        :param inter1: The first Interface1D object.
        :param inter2: The second Interface1D object.
        :return: True or false.
        """

class ShapeUP1D:
    """Class hierarchy: `freestyle.types.UnaryPredicate1D` > `ShapeUP1D`"""

    def __init__(self, first: int, second: int = 0) -> None:
        """Builds a ShapeUP1D object.

        :param first: The first Id component.
        :param second: The second Id component.
        """

    def __call__(self, inter: freestyle.types.Interface1D) -> bool:
        """Returns true if the shape to which the Interface1D belongs to has the
        same `freestyle.types.Id` as the one specified by the user.

                :param inter: An Interface1D object.
                :return: True if Interface1D belongs to the shape of the
        user-specified Id.
        """

class TrueBP1D:
    """Class hierarchy: `freestyle.types.BinaryPredicate1D` > `TrueBP1D`"""

    def __call__(
        self, inter1: freestyle.types.Interface1D, inter2: freestyle.types.Interface1D
    ) -> bool:
        """Always returns true.

        :param inter1: The first Interface1D object.
        :param inter2: The second Interface1D object.
        :return: True.
        """

class TrueUP0D:
    """Class hierarchy: `freestyle.types.UnaryPredicate0D` > `TrueUP0D`"""

    def __call__(self, it: freestyle.types.Interface0DIterator) -> bool:
        """Always returns true.

        :param it: An Interface0DIterator object.
        :return: True.
        """

class TrueUP1D:
    """Class hierarchy: `freestyle.types.UnaryPredicate1D` > `TrueUP1D`"""

    def __call__(self, inter: freestyle.types.Interface1D) -> bool:
        """Always returns true.

        :param inter: An Interface1D object.
        :return: True.
        """

class ViewMapGradientNormBP1D:
    """Class hierarchy: `freestyle.types.BinaryPredicate1D` > `ViewMapGradientNormBP1D`"""

    def __init__(
        self,
        level: int,
        integration_type: freestyle.types.IntegrationType = IntegrationType.MEAN,
        sampling: float = 2.0,
    ) -> None:
        """Builds a ViewMapGradientNormBP1D object.

                :param level: The level of the pyramid from which the pixel must be
        read.
                :param integration_type: The integration method used to compute a single value
        from a set of values.
                :param sampling: The resolution used to sample the chain:
        GetViewMapGradientNormF0D is evaluated at each sample point and
        the result is obtained by combining the resulting values into a
        single one, following the method specified by integration_type.
        """

    def __call__(
        self, inter1: freestyle.types.Interface1D, inter2: freestyle.types.Interface1D
    ) -> bool:
        """Returns true if the evaluation of the Gradient norm Function is
        higher for inter1 than for inter2.

                :param inter1: The first Interface1D object.
                :param inter2: The second Interface1D object.
                :return: True or false.
        """

class WithinImageBoundaryUP1D:
    """Class hierarchy: `freestyle.types.UnaryPredicate1D` > `WithinImageBoundaryUP1D`"""

    def __init__(self, xmin: float, ymin: float, xmax: float, ymax: float) -> None:
        """Builds an WithinImageBoundaryUP1D object.

        :param xmin: X lower bound of the image boundary.
        :param ymin: Y lower bound of the image boundary.
        :param xmax: X upper bound of the image boundary.
        :param ymax: Y upper bound of the image boundary.
        """

    def __call__(self, inter) -> None:
        """Returns true if the Interface1D intersects with image boundary.

        :param inter:
        """

class pyBackTVertexUP0D:
    """Check whether an Interface0DIterator references a TVertex and is
    the one that is hidden (inferred from the context).
    """

class pyClosedCurveUP1D: ...
class pyDensityFunctorUP1D: ...
class pyDensityUP1D: ...
class pyDensityVariableSigmaUP1D: ...
class pyHighDensityAnisotropyUP1D: ...
class pyHighDirectionalViewMapDensityUP1D: ...
class pyHighSteerableViewMapDensityUP1D: ...
class pyHighViewMapDensityUP1D: ...
class pyHighViewMapGradientNormUP1D: ...
class pyHigherCurvature2DAngleUP0D: ...
class pyHigherLengthUP1D: ...
class pyHigherNumberOfTurnsUP1D: ...
class pyIsInOccludersListUP1D: ...
class pyIsOccludedByIdListUP1D: ...
class pyIsOccludedByItselfUP1D: ...
class pyIsOccludedByUP1D: ...
class pyLengthBP1D: ...
class pyLowDirectionalViewMapDensityUP1D: ...
class pyLowSteerableViewMapDensityUP1D: ...
class pyNFirstUP1D: ...
class pyNatureBP1D: ...
class pyNatureUP1D: ...
class pyParameterUP0D: ...
class pyParameterUP0DGoodOne: ...
class pyProjectedXBP1D: ...
class pyProjectedYBP1D: ...
class pyShapeIdListUP1D: ...
class pyShapeIdUP1D: ...
class pyShuffleBP1D: ...
class pySilhouetteFirstBP1D: ...
class pyUEqualsUP0D: ...
class pyVertexNatureUP0D: ...
class pyViewMapGradientNormBP1D: ...
class pyZBP1D: ...
class pyZDiscontinuityBP1D: ...
class pyZSmallerUP1D: ...
