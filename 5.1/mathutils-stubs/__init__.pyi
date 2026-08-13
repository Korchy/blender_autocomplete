"""
This module provides access to math operations.

[NOTE]
Classes, methods and attributes that accept vectors also accept other numeric sequences,
such as tuples, lists.

The mathutils module provides the following classes:

* Color,
* Euler,
* Matrix,
* Quaternion,
* Vector,

mathutils.geometry.rst
mathutils.bvhtree.rst
mathutils.kdtree.rst
mathutils.interpolate.rst
mathutils.noise.rst

:maxdepth: 1
:caption: Submodules

```../examples/mathutils.0.py```

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
from . import bvhtree as bvhtree
from . import geometry as geometry
from . import interpolate as interpolate
from . import kdtree as kdtree
from . import noise as noise

class Color:
    """This object gives access to Colors in Blender.Most colors returned by Blender APIs are in scene linear color space, as defined by the OpenColorIO configuration. The notable exception is user interface theming colors, which are in sRGB color space."""

    b: float
    """ Blue color channel."""

    g: float
    """ Green color channel."""

    h: float
    """ HSV Hue component in [0, 1]."""

    hsv: tuple[float, float, float]
    """ HSV Values in [0, 1]."""

    is_frozen: bool
    """ True when this object has been frozen (read-only)."""

    is_valid: bool
    """ True when the owner of this data is valid."""

    is_wrapped: bool
    """ True when this object wraps external data (read-only)."""

    owner: typing.Any
    """ The item this is wrapping or None (read-only)."""

    r: float
    """ Red color channel."""

    s: float
    """ HSV Saturation component in [0, 1]."""

    v: float
    """ HSV Value component in [0, 1]."""

    def copy(self) -> typing_extensions.Self:
        """Returns a copy of this color.

        :return: A copy of the color.
        """

    def freeze(self) -> typing_extensions.Self:
        """Make this object immutable.After this the object can be hashed, used in dictionaries & sets.

        :return: An instance of this object.
        """

    def from_aces_to_scene_linear(self) -> typing_extensions.Self:
        """Convert from ACES2065-1 linear to scene linear color space.

        :return: A color in scene linear color space.
        """

    def from_acescg_to_scene_linear(self) -> typing_extensions.Self:
        """Convert from ACEScg linear to scene linear color space.

        :return: A color in scene linear color space.
        """

    def from_rec2020_linear_to_scene_linear(self) -> typing_extensions.Self:
        """Convert from Rec.2020 linear color space to scene linear color space.

        :return: A color in scene linear color space.
        """

    def from_rec709_linear_to_scene_linear(self) -> typing_extensions.Self:
        """Convert from Rec.709 linear color space to scene linear color space.

        :return: A color in scene linear color space.
        """

    def from_scene_linear_to_aces(self) -> typing_extensions.Self:
        """Convert from scene linear to ACES2065-1 linear color space.

        :return: A color in ACES2065-1 linear color space.
        """

    def from_scene_linear_to_acescg(self) -> typing_extensions.Self:
        """Convert from scene linear to ACEScg linear color space.

        :return: A color in ACEScg linear color space.
        """

    def from_scene_linear_to_rec2020_linear(self) -> typing_extensions.Self:
        """Convert from scene linear to Rec.2020 linear color space.

        :return: A color in Rec.2020 linear color space.
        """

    def from_scene_linear_to_rec709_linear(self) -> typing_extensions.Self:
        """Convert from scene linear to Rec.709 linear color space.

        :return: A color in Rec.709 linear color space.
        """

    def from_scene_linear_to_srgb(self) -> typing_extensions.Self:
        """Convert from scene linear to sRGB color space.

        :return: A color in sRGB color space.
        """

    def from_scene_linear_to_xyz_d65(self) -> typing_extensions.Self:
        """Convert from scene linear to CIE XYZ (Illuminant D65) color space.

        :return: A color in XYZ color space.
        """

    def from_srgb_to_scene_linear(self) -> typing_extensions.Self:
        """Convert from sRGB to scene linear color space.

        :return: A color in scene linear color space.
        """

    def from_xyz_d65_to_scene_linear(self) -> typing_extensions.Self:
        """Convert from CIE XYZ (Illuminant D65) to scene linear color space.

        :return: A color in scene linear color space.
        """

    def __init__(self, rgb: collections.abc.Sequence[float] = (0.0, 0.0, 0.0)) -> None:
        """

        :param rgb:
        """

    def __get__(self, instance, owner) -> typing_extensions.Self:
        """

        :param instance:
        :param owner:
        :return:
        """

    def __set__(
        self, instance, value: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> None:
        """

        :param instance:
        :param value:
        """

    def __add__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __sub__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __mul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __truediv__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __radd__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __rsub__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __rmul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __rtruediv__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __iadd__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __isub__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __imul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __itruediv__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    @typing.overload
    def __getitem__(self, key: int) -> float:
        """

        :param key:
        :return:
        """

    @typing.overload
    def __getitem__(self, key: slice) -> tuple[float, ...]:
        """

        :param key:
        :return:
        """

    @typing.overload
    def __setitem__(self, key: int, value: float) -> None:
        """

        :param key:
        :param value:
        """

    @typing.overload
    def __setitem__(
        self, key: slice, value: collections.abc.Iterable[float] | Color
    ) -> None:
        """

        :param key:
        :param value:
        """

class Euler:
    """This object gives access to Eulers in Blender.`Euler angles <https://en.wikipedia.org/wiki/Euler_angles>`__ on Wikipedia."""

    is_frozen: bool
    """ True when this object has been frozen (read-only)."""

    is_valid: bool
    """ True when the owner of this data is valid."""

    is_wrapped: bool
    """ True when this object wraps external data (read-only)."""

    order: typing.Literal["XYZ", "XZY", "YXZ", "YZX", "ZXY", "ZYX"]
    """ Euler rotation order."""

    owner: typing.Any
    """ The item this is wrapping or None (read-only)."""

    x: float
    """ Euler axis angle in radians."""

    y: float
    """ Euler axis angle in radians."""

    z: float
    """ Euler axis angle in radians."""

    def copy(self) -> typing_extensions.Self:
        """Returns a copy of this euler.

        :return: A copy of the euler.
        """

    def freeze(self) -> typing_extensions.Self:
        """Make this object immutable.After this the object can be hashed, used in dictionaries & sets.

        :return: An instance of this object.
        """

    def make_compatible(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        /,
    ) -> None:
        """Make this euler compatible with another,
        so interpolating between them works as intended.

                :param other: Other euler rotation.
        """

    def rotate(
        self,
        other: Matrix
        | Quaternion
        | collections.abc.Sequence[collections.abc.Sequence[float]]
        | collections.abc.Sequence[float]
        | typing_extensions.Self,
        /,
    ) -> None:
        """Rotates the euler by another mathutils value.

        :param other: rotation component of mathutils value
        """

    def rotate_axis(
        self,
        axis: typing.Literal["X", "Y", "Z"],
        angle: float,
        /,
    ) -> None:
        """Rotates the euler a certain amount, wrapping the result to produce
        a unique euler rotation (no 720 degree pitches).

                :param axis: An axis string.
                :param angle: angle in radians.
        """

    def to_matrix(self) -> Matrix:
        """Return a matrix representation of the euler.

        :return: A 3x3 rotation matrix representation of the euler.
        """

    def to_quaternion(self) -> Quaternion:
        """Return a quaternion representation of the euler.

        :return: Quaternion representation of the euler.
        """

    def zero(self) -> None:
        """Set all values to zero."""

    def __init__(
        self,
        angles: collections.abc.Sequence[float] = (0.0, 0.0, 0.0),
        order: str = "XYZ",
    ) -> None:
        """

        :param angles:
        :param order:
        """

    def __get__(self, instance, owner) -> typing_extensions.Self:
        """

        :param instance:
        :param owner:
        :return:
        """

    def __set__(
        self, instance, value: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> None:
        """

        :param instance:
        :param value:
        """

    @typing.overload
    def __getitem__(self, key: int) -> float:
        """

        :param key:
        :return:
        """

    @typing.overload
    def __getitem__(self, key: slice) -> tuple[float, ...]:
        """

        :param key:
        :return:
        """

    @typing.overload
    def __setitem__(self, key: int, value: float) -> None:
        """

        :param key:
        :param value:
        """

    @typing.overload
    def __setitem__(
        self, key: slice, value: collections.abc.Iterable[float] | Euler
    ) -> None:
        """

        :param key:
        :param value:
        """

class Matrix:
    """This object gives access to Matrices in Blender, supporting square and rectangular
    matrices from 2x2 up to 4x4.
    """

    col: MatrixAccess
    """ Access the matrix by columns (read-only)."""

    is_frozen: bool
    """ True when this object has been frozen (read-only)."""

    is_identity: bool
    """ True if this is an identity matrix (read-only)."""

    is_negative: bool
    """ True if this matrix results in a negative scale, 3x3 and 4x4 only, (read-only)."""

    is_orthogonal: bool
    """ True if this matrix is orthogonal, 3x3 and 4x4 only, (read-only)."""

    is_orthogonal_axis_vectors: bool
    """ True if this matrix has orthogonal axis vectors, 3x3 and 4x4 only, (read-only)."""

    is_valid: bool
    """ True when the owner of this data is valid."""

    is_wrapped: bool
    """ True when this object wraps external data (read-only)."""

    median_scale: float
    """ The average scale applied to each axis (read-only)."""

    owner: typing.Any
    """ The item this is wrapping or None (read-only)."""

    row: MatrixAccess
    """ Access the matrix by rows (default), (read-only)."""

    translation: Vector
    """ The translation component of the matrix."""

    @classmethod
    def Diagonal(
        cls,
        vector: collections.abc.Sequence[float],
        /,
    ) -> typing_extensions.Self:
        """Create a diagonal (scaling) matrix using the values from the vector.

        :param vector: The vector of values for the diagonal.
        :return: A diagonal matrix.
        """

    @classmethod
    def Identity(
        cls,
        size: int,
        /,
    ) -> typing_extensions.Self:
        """Create an identity matrix.

        :param size: The size of the identity matrix to construct [2, 4].
        :return: A new identity matrix.
        """

    @classmethod
    def LocRotScale(
        cls,
        location: None | collections.abc.Sequence[float],
        rotation: Euler
        | None
        | Quaternion
        | collections.abc.Sequence[collections.abc.Sequence[float]]
        | collections.abc.Sequence[float]
        | typing_extensions.Self,
        scale: None | collections.abc.Sequence[float],
        /,
    ) -> typing_extensions.Self:
        """Create a matrix combining translation, rotation and scale,
        acting as the inverse of the decompose() method.Any of the inputs may be replaced with None if not needed.

                :param location: The translation component.
                :param rotation: The rotation component as a 3x3 matrix, quaternion, euler or None for no rotation.
                :param scale: The scale component.
                :return: Combined transformation as a 4x4 matrix.
        """

    @classmethod
    def OrthoProjection(
        cls,
        axis: collections.abc.Sequence[float]
        | typing.Literal["X", "Y", "XY", "XZ", "YZ"],
        size: int,
        /,
    ) -> typing_extensions.Self:
        """Create a matrix to represent an orthographic projection.

                :param axis: An axis string,
        where a single axis is for a 2D matrix.
        Or a vector for an arbitrary axis
                :param size: The size of the projection matrix to construct [2, 4].
                :return: A new projection matrix.
        """

    @classmethod
    def Rotation(
        cls,
        angle: float,
        size: int,
        axis: collections.abc.Sequence[float]
        | typing.Literal["X", "Y", "Z"]
        | None = [],
        /,
    ) -> typing_extensions.Self:
        """Create a matrix representing a rotation.

                :param angle: The angle of rotation desired, in radians.
                :param size: The size of the rotation matrix to construct [2, 4].
                :param axis: an axis string or a 3D Vector Object
        (optional when size is 2).
                :return: A new rotation matrix.
        """

    @classmethod
    def Scale(
        cls,
        factor: float,
        size: int,
        axis: collections.abc.Sequence[float] | None = [],
        /,
    ) -> typing_extensions.Self:
        """Create a matrix representing a scaling.

        :param factor: The factor of scaling to apply.
        :param size: The size of the scale matrix to construct [2, 4].
        :param axis: Direction to influence scale. (optional).
        :return: A new scale matrix.
        """

    @classmethod
    def Shear(
        cls,
        plane: typing.Literal["X", "Y", "XY", "XZ", "YZ"],
        size: int,
        factor: collections.abc.Sequence[float] | float,
        /,
    ) -> typing_extensions.Self:
        """Create a matrix to represent a shear transformation.

                :param plane: An axis string,
        where a single axis is for a 2D matrix only.
                :param size: The size of the shear matrix to construct [2, 4].
                :param factor: The factor of shear to apply. For a 2 size matrix use a single float. For a 3 or 4 size matrix pass a pair of floats corresponding with the plane axis.
                :return: A new shear matrix.
        """

    @classmethod
    def Translation(
        cls,
        vector: collections.abc.Sequence[float],
        /,
    ) -> typing_extensions.Self:
        """Create a matrix representing a translation.

        :param vector: The translation vector.
        :return: An identity matrix with a translation.
        """

    def adjugate(self) -> None:
        """Set the matrix to its adjugate.`Adjugate matrix <https://en.wikipedia.org/wiki/Adjugate_matrix>`__ on Wikipedia."""

    def adjugated(self) -> typing_extensions.Self:
        """Return an adjugated copy of the matrix.

        :return: the adjugated matrix.
        """

    def copy(self) -> typing_extensions.Self:
        """Returns a copy of this matrix.

        :return: A copy of the matrix.
        """

    def decompose(self) -> tuple[Vector, Quaternion, Vector]:
        """Return the translation, rotation, and scale components of this 4x4 matrix.

        :return: Tuple of translation, rotation, and scale.
        """

    def determinant(self) -> float:
        """Return the determinant of a matrix.`Determinant <https://en.wikipedia.org/wiki/Determinant>`__ on Wikipedia.

        :return: Return the determinant of a matrix.
        """

    def freeze(self) -> typing_extensions.Self:
        """Make this object immutable.After this the object can be hashed, used in dictionaries & sets.

        :return: An instance of this object.
        """

    def identity(self) -> None:
        """Set the matrix to the identity matrix.`Identity matrix <https://en.wikipedia.org/wiki/Identity_matrix>`__ on Wikipedia."""

    def invert(
        self,
        fallback: None
        | collections.abc.Sequence[collections.abc.Sequence[float]]
        | typing_extensions.Self
        | None = None,
        /,
    ) -> None:
        """Set the matrix to its inverse.`Inverse matrix <https://en.wikipedia.org/wiki/Inverse_matrix>`__ on Wikipedia.

                :param fallback: Set the matrix to this value when the inverse cannot be calculated
        (instead of raising a `ValueError` exception).
        """

    def invert_safe(self) -> None:
        """Set the matrix to its inverse, will never error.
        If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one.
        If tweaked matrix is still degenerated, set to the identity matrix instead.`Inverse Matrix <https://en.wikipedia.org/wiki/Inverse_matrix>`__ on Wikipedia.

        """

    def inverted(
        self,
        fallback: typing.Any | None = None,
        /,
    ) -> typing.Any | typing_extensions.Self:
        """Return an inverted copy of the matrix.

                :param fallback: return this when the inverse cant be calculated
        (instead of raising a `ValueError`).
                :return: The inverted matrix or fallback when given.
        """

    def inverted_safe(self) -> typing_extensions.Self:
        """Return an inverted copy of the matrix, will never error.
        If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one.
        If tweaked matrix is still degenerated, return the identity matrix instead.

                :return: the inverted matrix.
        """

    def lerp(
        self,
        other: collections.abc.Sequence[collections.abc.Sequence[float]]
        | typing_extensions.Self,
        factor: float,
        /,
    ) -> typing_extensions.Self:
        """Returns the interpolation of two matrices. Uses polar decomposition, see "Matrix Animation and Polar Decomposition", Shoemake and Duff, 1992.

        :param other: value to interpolate with.
        :param factor: The interpolation value in [0.0, 1.0].
        :return: The interpolated matrix.
        """

    def normalize(self) -> None:
        """Normalize each of the matrix columns (3x3 and 4x4 only)."""

    def normalized(self) -> typing_extensions.Self:
        """Return a column normalized matrix (3x3 and 4x4 only).

        :return: a column normalized matrix
        """

    def resize_4x4(self) -> None:
        """Resize the matrix to 4x4."""

    def rotate(
        self,
        other: Euler
        | Quaternion
        | collections.abc.Sequence[collections.abc.Sequence[float]]
        | collections.abc.Sequence[float]
        | typing_extensions.Self,
        /,
    ) -> None:
        """Rotates the matrix by another mathutils value.

        :param other: rotation component of mathutils value
        """

    def to_2x2(self) -> typing_extensions.Self:
        """Return a 2x2 copy of this matrix.

        :return: a new matrix.
        """

    def to_3x3(self) -> typing_extensions.Self:
        """Return a 3x3 copy of this matrix.

        :return: a new matrix.
        """

    def to_4x4(self) -> typing_extensions.Self:
        """Return a 4x4 copy of this matrix.

        :return: a new matrix.
        """

    def to_euler(
        self,
        order: typing.Literal["XYZ", "XZY", "YXZ", "YZX", "ZXY", "ZYX"] = "XYZ",
        euler_compat: Euler | None | collections.abc.Sequence[float] | None = None,
        /,
    ) -> Euler:
        """Return an Euler representation of the rotation matrix
        (3x3 or 4x4 matrix only).

                :param order: A rotation order string.
                :param euler_compat: Optional euler argument the new euler will be made
        compatible with (no axis flipping between them).
        Useful for converting a series of matrices to animation curves.
                :return: Euler representation of the matrix.
        """

    def to_quaternion(self) -> Quaternion:
        """Return a quaternion representation of the rotation matrix.

        :return: Quaternion representation of the rotation matrix.
        """

    def to_scale(self) -> Vector:
        """Return the scale part of a 3x3 or 4x4 matrix.

        :return: Return the scale of a matrix.
        """

    def to_translation(self) -> Vector:
        """Return the translation part of a 4x4 matrix.

        :return: Return the translation of a matrix.
        """

    def transpose(self) -> None:
        """Set the matrix to its transpose.`Transpose <https://en.wikipedia.org/wiki/Transpose>`__ on Wikipedia."""

    def transposed(self) -> typing_extensions.Self:
        """Return a new, transposed matrix.

        :return: a transposed matrix
        """

    def zero(self) -> None:
        """Set all the matrix values to zero."""

    def __init__(
        self,
        rows: collections.abc.Sequence[collections.abc.Sequence[float]] = (
            (1.0, 0.0, 0.0, 0.0),
            (0.0, 1.0, 0.0, 0.0),
            (0.0, 0.0, 1.0, 0.0),
            (0.0, 0.0, 0.0, 1.0),
        ),
    ) -> None:
        """

        :param rows:
        """

    def __get__(self, instance, owner) -> typing_extensions.Self:
        """

        :param instance:
        :param owner:
        :return:
        """

    def __set__(
        self,
        instance,
        value: collections.abc.Sequence[collections.abc.Sequence[float]]
        | typing_extensions.Self,
    ) -> None:
        """

        :param instance:
        :param value:
        """

    @typing.overload
    def __getitem__(self, key: int) -> Vector:
        """

        :param key:
        :return:
        """

    @typing.overload
    def __getitem__(self, key: slice) -> tuple[Vector, ...]:
        """

        :param key:
        :return:
        """

    @typing.overload
    def __setitem__(
        self, key: int, value: Vector | collections.abc.Iterable[float]
    ) -> None:
        """

        :param key:
        :param value:
        """

    @typing.overload
    def __setitem__(
        self,
        key: slice,
        value: collections.abc.Iterable[Vector | collections.abc.Iterable[float]]
        | Matrix,
    ) -> None:
        """

        :param key:
        :param value:
        """

    def __len__(self) -> int:
        """

        :return:
        """

    def __add__(
        self,
        other: collections.abc.Sequence[collections.abc.Sequence[float]]
        | typing_extensions.Self,
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __sub__(
        self,
        other: collections.abc.Sequence[collections.abc.Sequence[float]]
        | typing_extensions.Self,
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __mul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    @typing.overload
    def __matmul__(
        self,
        other: collections.abc.Sequence[collections.abc.Sequence[float]]
        | typing_extensions.Self,
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    @typing.overload
    def __matmul__(self, other: Vector | collections.abc.Sequence[float]) -> Vector:
        """

        :param other:
        :return:
        """

    def __radd__(
        self,
        other: collections.abc.Sequence[collections.abc.Sequence[float]]
        | typing_extensions.Self,
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __rsub__(
        self,
        other: collections.abc.Sequence[collections.abc.Sequence[float]]
        | typing_extensions.Self,
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __rmul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __imul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

class MatrixAccess:
    """An indexable type for accessing matrix rows or columns as `Vector` types."""

class Quaternion:
    """This object gives access to Quaternions in Blender.The constructor takes arguments in various forms:"""

    angle: float
    """ Angle of the quaternion."""

    axis: Vector
    """ Quaternion axis as a vector."""

    is_frozen: bool
    """ True when this object has been frozen (read-only)."""

    is_valid: bool
    """ True when the owner of this data is valid."""

    is_wrapped: bool
    """ True when this object wraps external data (read-only)."""

    magnitude: float
    """ Size of the quaternion (read-only)."""

    owner: typing.Any
    """ The item this is wrapping or None (read-only)."""

    w: float
    """ Quaternion component value."""

    x: float
    """ Quaternion component value."""

    y: float
    """ Quaternion component value."""

    z: float
    """ Quaternion component value."""

    def conjugate(self) -> None:
        """Set the quaternion to its conjugate (negate x, y, z)."""

    def conjugated(self) -> typing_extensions.Self:
        """Return a new conjugated quaternion.

        :return: a new quaternion.
        """

    def copy(self) -> typing_extensions.Self:
        """Returns a copy of this quaternion.

        :return: A copy of the quaternion.
        """

    def cross(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        /,
    ) -> typing_extensions.Self:
        """Return the cross product of this quaternion and another.

        :param other: The other quaternion to perform the cross product with.
        :return: The cross product.
        """

    def dot(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        /,
    ) -> float:
        """Return the dot product of this quaternion and another.

        :param other: The other quaternion to perform the dot product with.
        :return: The dot product.
        """

    def freeze(self) -> typing_extensions.Self:
        """Make this object immutable.After this the object can be hashed, used in dictionaries & sets.

        :return: An instance of this object.
        """

    def identity(self) -> None:
        """Set the quaternion to an identity quaternion."""

    def invert(self) -> None:
        """Set the quaternion to its inverse."""

    def inverted(self) -> typing_extensions.Self:
        """Return a new, inverted quaternion.

        :return: the inverted value.
        """

    def make_compatible(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        /,
    ) -> None:
        """Make this quaternion compatible with another,
        so interpolating between them works as intended.

                :param other: The reference quaternion to make this one compatible with.
        """

    def negate(self) -> None:
        """Set the quaternion to its negative."""

    def normalize(self) -> None:
        """Normalize the quaternion."""

    def normalized(self) -> typing_extensions.Self:
        """Return a new normalized quaternion.

        :return: a normalized copy.
        """

    def rotate(
        self,
        other: Euler
        | Matrix
        | collections.abc.Sequence[collections.abc.Sequence[float]]
        | collections.abc.Sequence[float]
        | typing_extensions.Self,
        /,
    ) -> None:
        """Rotates the quaternion by another mathutils value.

        :param other: rotation component of mathutils value
        """

    def rotation_difference(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        /,
    ) -> typing_extensions.Self:
        """Returns a quaternion representing the rotational difference.

        :param other: second quaternion.
        :return: the rotational difference between the two quat rotations.
        """

    def slerp(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        factor: float,
        /,
    ) -> typing_extensions.Self:
        """Returns the interpolation of two quaternions.

        :param other: value to interpolate with.
        :param factor: The interpolation value in [0.0, 1.0].
        :return: The interpolated rotation.
        """

    def to_axis_angle(self) -> tuple[Vector, float]:
        """Return the axis, angle representation of the quaternion.

        :return: Axis, angle.
        """

    def to_euler(
        self,
        order: typing.Literal["XYZ", "XZY", "YXZ", "YZX", "ZXY", "ZYX"] = "XYZ",
        euler_compat: Euler | None | collections.abc.Sequence[float] | None = None,
        /,
    ) -> Euler:
        """Return Euler representation of the quaternion.

                :param order: Rotation order.
                :param euler_compat: Optional euler argument the new euler will be made
        compatible with (no axis flipping between them).
        Useful for converting a series of quaternions to animation curves.
                :return: Euler representation of the quaternion.
        """

    def to_exponential_map(self) -> Vector:
        """Return the exponential map representation of the quaternion.This representation consists of the rotation axis multiplied by the rotation angle.
        Such a representation is useful for interpolation between multiple orientations.To convert back to a quaternion, pass it to the `Quaternion` constructor.

                :return: 3D exponential map.
        """

    def to_matrix(self) -> Matrix:
        """Return a matrix representation of the quaternion.

        :return: A 3x3 rotation matrix representation of the quaternion.
        """

    def to_swing_twist(
        self,
        axis: typing.Literal["X", "Y", "Z"],
        /,
    ) -> tuple[Quaternion, float]:
        """Split the rotation into a swing quaternion with the specified
        axis fixed at zero, and the remaining twist rotation angle.

                :param axis: Twist axis as a string.
                :return: Swing, twist angle.
        """

    def __init__(
        self,
        seq: Vector | collections.abc.Sequence[float] = (1.0, 0.0, 0.0, 0.0),
        angle: float = 0.0,
    ) -> None:
        """

        :param seq:
        :param angle:
        """

    def __get__(self, instance, owner) -> typing_extensions.Self:
        """

        :param instance:
        :param owner:
        :return:
        """

    def __set__(
        self, instance, value: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> None:
        """

        :param instance:
        :param value:
        """

    def __len__(self) -> int:
        """

        :return:
        """

    @typing.overload
    def __getitem__(self, key: int) -> float:
        """

        :param key:
        :return:
        """

    @typing.overload
    def __getitem__(self, key: slice) -> tuple[float, ...]:
        """

        :param key:
        :return:
        """

    @typing.overload
    def __setitem__(self, key: int, value: float) -> None:
        """

        :param key:
        :param value:
        """

    @typing.overload
    def __setitem__(
        self, key: slice, value: collections.abc.Iterable[float] | Quaternion
    ) -> None:
        """

        :param key:
        :param value:
        """

    def __add__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __sub__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __mul__(
        self, other: collections.abc.Sequence[float] | float | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    @typing.overload
    def __matmul__(self, other: typing_extensions.Self) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    @typing.overload
    def __matmul__(self, other: Vector) -> Vector:
        """

        :param other:
        :return:
        """

    def __radd__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __rsub__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __rmul__(
        self, other: collections.abc.Sequence[float] | float | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __imul__(
        self, other: collections.abc.Sequence[float] | float | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

class Vector:
    """This object gives access to Vectors in Blender."""

    is_frozen: bool
    """ True when this object has been frozen (read-only)."""

    is_valid: bool
    """ True when the owner of this data is valid."""

    is_wrapped: bool
    """ True when this object wraps external data (read-only)."""

    length: float
    """ Vector Length."""

    length_squared: float
    """ Vector length squared (v.dot(v))."""

    magnitude: float
    """ Vector Length."""

    owner: typing.Any
    """ The item this is wrapping or None (read-only)."""

    w: float
    """ Vector W axis (4D Vectors only)."""

    ww: typing_extensions.Self
    www: typing_extensions.Self
    wwww: typing_extensions.Self
    wwwx: typing_extensions.Self
    wwwy: typing_extensions.Self
    wwwz: typing_extensions.Self
    wwx: typing_extensions.Self
    wwxw: typing_extensions.Self
    wwxx: typing_extensions.Self
    wwxy: typing_extensions.Self
    wwxz: typing_extensions.Self
    wwy: typing_extensions.Self
    wwyw: typing_extensions.Self
    wwyx: typing_extensions.Self
    wwyy: typing_extensions.Self
    wwyz: typing_extensions.Self
    wwz: typing_extensions.Self
    wwzw: typing_extensions.Self
    wwzx: typing_extensions.Self
    wwzy: typing_extensions.Self
    wwzz: typing_extensions.Self
    wx: typing_extensions.Self
    wxw: typing_extensions.Self
    wxww: typing_extensions.Self
    wxwx: typing_extensions.Self
    wxwy: typing_extensions.Self
    wxwz: typing_extensions.Self
    wxx: typing_extensions.Self
    wxxw: typing_extensions.Self
    wxxx: typing_extensions.Self
    wxxy: typing_extensions.Self
    wxxz: typing_extensions.Self
    wxy: typing_extensions.Self
    wxyw: typing_extensions.Self
    wxyx: typing_extensions.Self
    wxyy: typing_extensions.Self
    wxyz: typing_extensions.Self
    wxz: typing_extensions.Self
    wxzw: typing_extensions.Self
    wxzx: typing_extensions.Self
    wxzy: typing_extensions.Self
    wxzz: typing_extensions.Self
    wy: typing_extensions.Self
    wyw: typing_extensions.Self
    wyww: typing_extensions.Self
    wywx: typing_extensions.Self
    wywy: typing_extensions.Self
    wywz: typing_extensions.Self
    wyx: typing_extensions.Self
    wyxw: typing_extensions.Self
    wyxx: typing_extensions.Self
    wyxy: typing_extensions.Self
    wyxz: typing_extensions.Self
    wyy: typing_extensions.Self
    wyyw: typing_extensions.Self
    wyyx: typing_extensions.Self
    wyyy: typing_extensions.Self
    wyyz: typing_extensions.Self
    wyz: typing_extensions.Self
    wyzw: typing_extensions.Self
    wyzx: typing_extensions.Self
    wyzy: typing_extensions.Self
    wyzz: typing_extensions.Self
    wz: typing_extensions.Self
    wzw: typing_extensions.Self
    wzww: typing_extensions.Self
    wzwx: typing_extensions.Self
    wzwy: typing_extensions.Self
    wzwz: typing_extensions.Self
    wzx: typing_extensions.Self
    wzxw: typing_extensions.Self
    wzxx: typing_extensions.Self
    wzxy: typing_extensions.Self
    wzxz: typing_extensions.Self
    wzy: typing_extensions.Self
    wzyw: typing_extensions.Self
    wzyx: typing_extensions.Self
    wzyy: typing_extensions.Self
    wzyz: typing_extensions.Self
    wzz: typing_extensions.Self
    wzzw: typing_extensions.Self
    wzzx: typing_extensions.Self
    wzzy: typing_extensions.Self
    wzzz: typing_extensions.Self
    x: float
    """ Vector X axis."""

    xw: typing_extensions.Self
    xww: typing_extensions.Self
    xwww: typing_extensions.Self
    xwwx: typing_extensions.Self
    xwwy: typing_extensions.Self
    xwwz: typing_extensions.Self
    xwx: typing_extensions.Self
    xwxw: typing_extensions.Self
    xwxx: typing_extensions.Self
    xwxy: typing_extensions.Self
    xwxz: typing_extensions.Self
    xwy: typing_extensions.Self
    xwyw: typing_extensions.Self
    xwyx: typing_extensions.Self
    xwyy: typing_extensions.Self
    xwyz: typing_extensions.Self
    xwz: typing_extensions.Self
    xwzw: typing_extensions.Self
    xwzx: typing_extensions.Self
    xwzy: typing_extensions.Self
    xwzz: typing_extensions.Self
    xx: typing_extensions.Self
    xxw: typing_extensions.Self
    xxww: typing_extensions.Self
    xxwx: typing_extensions.Self
    xxwy: typing_extensions.Self
    xxwz: typing_extensions.Self
    xxx: typing_extensions.Self
    xxxw: typing_extensions.Self
    xxxx: typing_extensions.Self
    xxxy: typing_extensions.Self
    xxxz: typing_extensions.Self
    xxy: typing_extensions.Self
    xxyw: typing_extensions.Self
    xxyx: typing_extensions.Self
    xxyy: typing_extensions.Self
    xxyz: typing_extensions.Self
    xxz: typing_extensions.Self
    xxzw: typing_extensions.Self
    xxzx: typing_extensions.Self
    xxzy: typing_extensions.Self
    xxzz: typing_extensions.Self
    xy: typing_extensions.Self
    xyw: typing_extensions.Self
    xyww: typing_extensions.Self
    xywx: typing_extensions.Self
    xywy: typing_extensions.Self
    xywz: typing_extensions.Self
    xyx: typing_extensions.Self
    xyxw: typing_extensions.Self
    xyxx: typing_extensions.Self
    xyxy: typing_extensions.Self
    xyxz: typing_extensions.Self
    xyy: typing_extensions.Self
    xyyw: typing_extensions.Self
    xyyx: typing_extensions.Self
    xyyy: typing_extensions.Self
    xyyz: typing_extensions.Self
    xyz: typing_extensions.Self
    xyzw: typing_extensions.Self
    xyzx: typing_extensions.Self
    xyzy: typing_extensions.Self
    xyzz: typing_extensions.Self
    xz: typing_extensions.Self
    xzw: typing_extensions.Self
    xzww: typing_extensions.Self
    xzwx: typing_extensions.Self
    xzwy: typing_extensions.Self
    xzwz: typing_extensions.Self
    xzx: typing_extensions.Self
    xzxw: typing_extensions.Self
    xzxx: typing_extensions.Self
    xzxy: typing_extensions.Self
    xzxz: typing_extensions.Self
    xzy: typing_extensions.Self
    xzyw: typing_extensions.Self
    xzyx: typing_extensions.Self
    xzyy: typing_extensions.Self
    xzyz: typing_extensions.Self
    xzz: typing_extensions.Self
    xzzw: typing_extensions.Self
    xzzx: typing_extensions.Self
    xzzy: typing_extensions.Self
    xzzz: typing_extensions.Self
    y: float
    """ Vector Y axis."""

    yw: typing_extensions.Self
    yww: typing_extensions.Self
    ywww: typing_extensions.Self
    ywwx: typing_extensions.Self
    ywwy: typing_extensions.Self
    ywwz: typing_extensions.Self
    ywx: typing_extensions.Self
    ywxw: typing_extensions.Self
    ywxx: typing_extensions.Self
    ywxy: typing_extensions.Self
    ywxz: typing_extensions.Self
    ywy: typing_extensions.Self
    ywyw: typing_extensions.Self
    ywyx: typing_extensions.Self
    ywyy: typing_extensions.Self
    ywyz: typing_extensions.Self
    ywz: typing_extensions.Self
    ywzw: typing_extensions.Self
    ywzx: typing_extensions.Self
    ywzy: typing_extensions.Self
    ywzz: typing_extensions.Self
    yx: typing_extensions.Self
    yxw: typing_extensions.Self
    yxww: typing_extensions.Self
    yxwx: typing_extensions.Self
    yxwy: typing_extensions.Self
    yxwz: typing_extensions.Self
    yxx: typing_extensions.Self
    yxxw: typing_extensions.Self
    yxxx: typing_extensions.Self
    yxxy: typing_extensions.Self
    yxxz: typing_extensions.Self
    yxy: typing_extensions.Self
    yxyw: typing_extensions.Self
    yxyx: typing_extensions.Self
    yxyy: typing_extensions.Self
    yxyz: typing_extensions.Self
    yxz: typing_extensions.Self
    yxzw: typing_extensions.Self
    yxzx: typing_extensions.Self
    yxzy: typing_extensions.Self
    yxzz: typing_extensions.Self
    yy: typing_extensions.Self
    yyw: typing_extensions.Self
    yyww: typing_extensions.Self
    yywx: typing_extensions.Self
    yywy: typing_extensions.Self
    yywz: typing_extensions.Self
    yyx: typing_extensions.Self
    yyxw: typing_extensions.Self
    yyxx: typing_extensions.Self
    yyxy: typing_extensions.Self
    yyxz: typing_extensions.Self
    yyy: typing_extensions.Self
    yyyw: typing_extensions.Self
    yyyx: typing_extensions.Self
    yyyy: typing_extensions.Self
    yyyz: typing_extensions.Self
    yyz: typing_extensions.Self
    yyzw: typing_extensions.Self
    yyzx: typing_extensions.Self
    yyzy: typing_extensions.Self
    yyzz: typing_extensions.Self
    yz: typing_extensions.Self
    yzw: typing_extensions.Self
    yzww: typing_extensions.Self
    yzwx: typing_extensions.Self
    yzwy: typing_extensions.Self
    yzwz: typing_extensions.Self
    yzx: typing_extensions.Self
    yzxw: typing_extensions.Self
    yzxx: typing_extensions.Self
    yzxy: typing_extensions.Self
    yzxz: typing_extensions.Self
    yzy: typing_extensions.Self
    yzyw: typing_extensions.Self
    yzyx: typing_extensions.Self
    yzyy: typing_extensions.Self
    yzyz: typing_extensions.Self
    yzz: typing_extensions.Self
    yzzw: typing_extensions.Self
    yzzx: typing_extensions.Self
    yzzy: typing_extensions.Self
    yzzz: typing_extensions.Self
    z: float
    """ Vector Z axis (3D Vectors only)."""

    zw: typing_extensions.Self
    zww: typing_extensions.Self
    zwww: typing_extensions.Self
    zwwx: typing_extensions.Self
    zwwy: typing_extensions.Self
    zwwz: typing_extensions.Self
    zwx: typing_extensions.Self
    zwxw: typing_extensions.Self
    zwxx: typing_extensions.Self
    zwxy: typing_extensions.Self
    zwxz: typing_extensions.Self
    zwy: typing_extensions.Self
    zwyw: typing_extensions.Self
    zwyx: typing_extensions.Self
    zwyy: typing_extensions.Self
    zwyz: typing_extensions.Self
    zwz: typing_extensions.Self
    zwzw: typing_extensions.Self
    zwzx: typing_extensions.Self
    zwzy: typing_extensions.Self
    zwzz: typing_extensions.Self
    zx: typing_extensions.Self
    zxw: typing_extensions.Self
    zxww: typing_extensions.Self
    zxwx: typing_extensions.Self
    zxwy: typing_extensions.Self
    zxwz: typing_extensions.Self
    zxx: typing_extensions.Self
    zxxw: typing_extensions.Self
    zxxx: typing_extensions.Self
    zxxy: typing_extensions.Self
    zxxz: typing_extensions.Self
    zxy: typing_extensions.Self
    zxyw: typing_extensions.Self
    zxyx: typing_extensions.Self
    zxyy: typing_extensions.Self
    zxyz: typing_extensions.Self
    zxz: typing_extensions.Self
    zxzw: typing_extensions.Self
    zxzx: typing_extensions.Self
    zxzy: typing_extensions.Self
    zxzz: typing_extensions.Self
    zy: typing_extensions.Self
    zyw: typing_extensions.Self
    zyww: typing_extensions.Self
    zywx: typing_extensions.Self
    zywy: typing_extensions.Self
    zywz: typing_extensions.Self
    zyx: typing_extensions.Self
    zyxw: typing_extensions.Self
    zyxx: typing_extensions.Self
    zyxy: typing_extensions.Self
    zyxz: typing_extensions.Self
    zyy: typing_extensions.Self
    zyyw: typing_extensions.Self
    zyyx: typing_extensions.Self
    zyyy: typing_extensions.Self
    zyyz: typing_extensions.Self
    zyz: typing_extensions.Self
    zyzw: typing_extensions.Self
    zyzx: typing_extensions.Self
    zyzy: typing_extensions.Self
    zyzz: typing_extensions.Self
    zz: typing_extensions.Self
    zzw: typing_extensions.Self
    zzww: typing_extensions.Self
    zzwx: typing_extensions.Self
    zzwy: typing_extensions.Self
    zzwz: typing_extensions.Self
    zzx: typing_extensions.Self
    zzxw: typing_extensions.Self
    zzxx: typing_extensions.Self
    zzxy: typing_extensions.Self
    zzxz: typing_extensions.Self
    zzy: typing_extensions.Self
    zzyw: typing_extensions.Self
    zzyx: typing_extensions.Self
    zzyy: typing_extensions.Self
    zzyz: typing_extensions.Self
    zzz: typing_extensions.Self
    zzzw: typing_extensions.Self
    zzzx: typing_extensions.Self
    zzzy: typing_extensions.Self
    zzzz: typing_extensions.Self

    @classmethod
    def Fill(
        cls,
        size: int,
        fill: float = 0.0,
        /,
    ) -> typing_extensions.Self:
        """Create a vector of length size with all values set to fill.

        :param size: The length of the vector to be created.
        :param fill: The value used to fill the vector.
        :return: A new vector.
        """

    @classmethod
    def Linspace(
        cls,
        start: float,
        stop: float,
        size: int,
        /,
    ) -> typing_extensions.Self:
        """Create a vector of the specified size which is filled with linearly spaced values between start and stop values.

        :param start: The start of the range used to fill the vector.
        :param stop: The end of the range used to fill the vector.
        :param size: The size of the vector to be created.
        :return: A new vector.
        """

    @classmethod
    def Range(
        cls,
        start: int,
        stop: int,
        step: int = 1,
        /,
    ) -> typing_extensions.Self:
        """Create a vector filled with a range of values.This method can also be called with a single argument, in which case the argument is interpreted as stop and start defaults to 0.

        :param start: The start of the range used to fill the vector.
        :param stop: The end of the range used to fill the vector.
        :param step: The step between successive values in the vector.
        :return: A new vector.
        """

    @classmethod
    def Repeat(
        cls,
        vector: collections.abc.Sequence[float] | typing_extensions.Self,
        size: int,
        /,
    ) -> typing_extensions.Self:
        """Create a vector by repeating the values in vector until the required size is reached.

        :param vector: The vector to draw values from.
        :param size: The size of the vector to be created.
        :return: A new vector.
        """

    def angle(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        fallback: typing.Any | None = None,
        /,
    ) -> float | typing.Any:
        """Return the angle between two vectors.

                :param other: another vector to compare the angle with
                :param fallback: return this when the angle cant be calculated (zero length vector),
        (instead of raising a `ValueError`).
                :return: angle in radians or fallback when given
        """

    def angle_signed(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        fallback: typing.Any | None = None,
        /,
    ) -> float | typing.Any:
        """Return the signed angle between two 2D vectors (clockwise is positive).

                :param other: another vector to compare the angle with
                :param fallback: return this when the angle cant be calculated (zero length vector),
        (instead of raising a `ValueError`).
                :return: angle in radians or fallback when given
        """

    def copy(self) -> typing_extensions.Self:
        """Returns a copy of this vector.

        :return: A copy of the vector.
        """

    def cross(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        /,
    ) -> float | typing_extensions.Self:
        """Return the cross product of this vector and another.

        :param other: The other vector to perform the cross product with.
        :return: The cross product as a vector or a float when 2D vectors are used.
        """

    def dot(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        /,
    ) -> float:
        """Return the dot product of this vector and another.

        :param other: The other vector to perform the dot product with.
        :return: The dot product.
        """

    def freeze(self) -> typing_extensions.Self:
        """Make this object immutable.After this the object can be hashed, used in dictionaries & sets.

        :return: An instance of this object.
        """

    def lerp(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        factor: float,
        /,
    ) -> typing_extensions.Self:
        """Returns the interpolation of two vectors.

        :param other: value to interpolate with.
        :param factor: The interpolation value in [0.0, 1.0].
        :return: The interpolated vector.
        """

    def negate(self) -> None:
        """Set all values to their negative."""

    def normalize(self) -> None:
        """Normalize the vector, making the length of the vector always 1.0."""

    def normalized(self) -> typing_extensions.Self:
        """Return a new, normalized vector.

        :return: a normalized copy of the vector
        """

    def orthogonal(self) -> typing_extensions.Self:
        """Return a perpendicular vector.

        :return: a new vector 90 degrees from this vector.
        """

    def project(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        /,
    ) -> typing_extensions.Self:
        """Return the projection of this vector onto the other.

        :param other: second vector.
        :return: the parallel projection vector
        """

    def reflect(
        self,
        mirror: collections.abc.Sequence[float] | typing_extensions.Self,
        /,
    ) -> typing_extensions.Self:
        """Return the reflection vector from the mirror argument.

        :param mirror: This vector could be a normal from the reflecting surface.
        :return: The reflected vector matching the size of this vector.
        """

    def resize(
        self,
        size: int,
        /,
    ) -> None:
        """Resize the vector to have size number of elements.

        :param size: The new size of the vector.
        """

    def resize_2d(self) -> None:
        """Resize the vector to 2D (x, y)."""

    def resize_3d(self) -> None:
        """Resize the vector to 3D (x, y, z)."""

    def resize_4d(self) -> None:
        """Resize the vector to 4D (x, y, z, w)."""

    def resized(
        self,
        size: int,
        /,
    ) -> typing_extensions.Self:
        """Return a resized copy of the vector with size number of elements.

        :param size: The new size of the vector.
        :return: A new vector.
        """

    def rotate(
        self,
        other: Euler
        | Matrix
        | Quaternion
        | collections.abc.Sequence[collections.abc.Sequence[float]]
        | collections.abc.Sequence[float],
        /,
    ) -> None:
        """Rotate the vector by a rotation value.

        :param other: rotation component of mathutils value
        """

    def rotation_difference(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        /,
    ) -> Quaternion:
        """Returns a quaternion representing the rotational difference between this
        vector and another.

                :param other: second vector.
                :return: the rotational difference between the two vectors.
        """

    def slerp(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        factor: float,
        fallback: typing.Any | None = None,
        /,
    ) -> typing_extensions.Self:
        """Returns the interpolation of two non-zero vectors (spherical coordinates).

                :param other: value to interpolate with.
                :param factor: The interpolation value typically in [0.0, 1.0].
                :param fallback: return this when the vector cant be calculated (zero length vector or direct opposites),
        (instead of raising a `ValueError`).
                :return: The interpolated vector.
        """

    def to_2d(self) -> typing_extensions.Self:
        """Return a 2d copy of the vector.

        :return: a new vector
        """

    def to_3d(self) -> typing_extensions.Self:
        """Return a 3d copy of the vector.

        :return: a new vector
        """

    def to_4d(self) -> typing_extensions.Self:
        """Return a 4d copy of the vector.

        :return: a new vector
        """

    def to_track_quat(
        self,
        track: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] = "Z",
        up: typing.Literal["X", "Y", "Z"] = "Y",
        /,
    ) -> Quaternion:
        """Return a quaternion rotation from the vector and the track and up axis.

        :param track: Track axis string.
        :param up: Up axis string.
        :return: rotation from the vector and the track and up axis.
        """

    def to_tuple(
        self,
        precision: int = -1,
        /,
    ) -> tuple[float, ...]:
        """Return this vector as a tuple with a given precision.

        :param precision: The number to round the value to in [-1, 21].
        :return: the values of the vector rounded by precision
        """

    def zero(self) -> None:
        """Set all values to zero."""

    def __init__(self, seq: collections.abc.Sequence[float] = (0.0, 0.0, 0.0)) -> None:
        """

        :param seq:
        """

    def __get__(self, instance, owner) -> typing_extensions.Self:
        """

        :param instance:
        :param owner:
        :return:
        """

    def __set__(
        self, instance, value: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> None:
        """

        :param instance:
        :param value:
        """

    def __len__(self) -> int:
        """

        :return:
        """

    @typing.overload
    def __getitem__(self, key: int) -> float:
        """

        :param key:
        :return:
        """

    @typing.overload
    def __getitem__(self, key: slice) -> tuple[float, ...]:
        """

        :param key:
        :return:
        """

    @typing.overload
    def __setitem__(self, key: int, value: float) -> None:
        """

        :param key:
        :param value:
        """

    @typing.overload
    def __setitem__(
        self, key: slice, value: collections.abc.Iterable[float] | Vector
    ) -> None:
        """

        :param key:
        :param value:
        """

    def __neg__(self) -> typing_extensions.Self:
        """

        :return:
        """

    def __add__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __sub__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    @typing.overload
    def __mul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    @typing.overload
    def __mul__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __truediv__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    @typing.overload
    def __matmul__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> float:
        """

        :param other:
        :return:
        """

    @typing.overload
    def __matmul__(
        self, other: Matrix | collections.abc.Sequence[collections.abc.Sequence[float]]
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __radd__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __rsub__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __rmul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __rtruediv__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __iadd__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __isub__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __imul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """

    def __itruediv__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :return:
        """
