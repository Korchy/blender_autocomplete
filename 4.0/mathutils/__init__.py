import sys
import typing
from . import geometry
from . import interpolate
from . import noise
from . import kdtree
from . import bvhtree

GenericType = typing.TypeVar("GenericType")


class Color:
    ''' This object gives access to Colors in Blender. Most colors returned by Blender APIs are in scene linear color space, as defined by the OpenColorIO configuration. The notable exception is user interface theming colors, which are in sRGB color space. :arg rgb: (r, g, b) color values :type rgb: 3d vector
    '''

    b: float = None
    ''' Blue color channel.

    :type: float
    '''

    g: float = None
    ''' Green color channel.

    :type: float
    '''

    h: float = None
    ''' HSV Hue component in [0, 1].

    :type: float
    '''

    hsv: typing.Union[typing.Sequence[float], 'Vector'] = None
    ''' HSV Values in [0, 1].

    :type: typing.Union[typing.Sequence[float], 'Vector']
    '''

    is_frozen: bool = None
    ''' True when this object has been frozen (read-only).

    :type: bool
    '''

    is_valid: bool = None
    ''' True when the owner of this data is valid.

    :type: bool
    '''

    is_wrapped: bool = None
    ''' True when this object wraps external data (read-only).

    :type: bool
    '''

    owner = None
    ''' The item this is wrapping or None (read-only).'''

    r: float = None
    ''' Red color channel.

    :type: float
    '''

    s: float = None
    ''' HSV Saturation component in [0, 1].

    :type: float
    '''

    v: float = None
    ''' HSV Value component in [0, 1].

    :type: float
    '''

    @staticmethod
    def copy() -> 'Color':
        ''' Returns a copy of this color.

        :rtype: 'Color'
        :return: A copy of the color.
        '''
        pass

    @staticmethod
    def freeze() -> 'Color':
        ''' Make this object immutable. After this the object can be hashed, used in dictionaries & sets.

        :rtype: 'Color'
        :return: An instance of this object.
        '''
        pass

    @staticmethod
    def from_aces_to_scene_linear() -> 'Color':
        ''' Convert from ACES2065-1 linear to scene linear color space.

        :rtype: 'Color'
        :return: A color in scene linear color space.
        '''
        pass

    @staticmethod
    def from_rec709_linear_to_scene_linear() -> 'Color':
        ''' Convert from Rec.709 linear color space to scene linear color space.

        :rtype: 'Color'
        :return: A color in scene linear color space.
        '''
        pass

    @staticmethod
    def from_scene_linear_to_aces() -> 'Color':
        ''' Convert from scene linear to ACES2065-1 linear color space.

        :rtype: 'Color'
        :return: A color in ACES2065-1 linear color space.
        '''
        pass

    @staticmethod
    def from_scene_linear_to_rec709_linear() -> 'Color':
        ''' Convert from scene linear to Rec.709 linear color space.

        :rtype: 'Color'
        :return: A color in Rec.709 linear color space.
        '''
        pass

    @staticmethod
    def from_scene_linear_to_srgb() -> 'Color':
        ''' Convert from scene linear to sRGB color space.

        :rtype: 'Color'
        :return: A color in sRGB color space.
        '''
        pass

    @staticmethod
    def from_scene_linear_to_xyz_d65() -> 'Color':
        ''' Convert from scene linear to CIE XYZ (Illuminant D65) color space.

        :rtype: 'Color'
        :return: A color in XYZ color space.
        '''
        pass

    @staticmethod
    def from_srgb_to_scene_linear() -> 'Color':
        ''' Convert from sRGB to scene linear color space.

        :rtype: 'Color'
        :return: A color in scene linear color space.
        '''
        pass

    @staticmethod
    def from_xyz_d65_to_scene_linear() -> 'Color':
        ''' Convert from CIE XYZ (Illuminant D65) to scene linear color space.

        :rtype: 'Color'
        :return: A color in scene linear color space.
        '''
        pass

    def __init__(self, rgb=(0.0, 0.0, 0.0)) -> typing.Any:
        ''' 

        :rtype: typing.Any
        '''
        pass

    def __add__(self, other: typing.Union[typing.Sequence[float], 'Color']
                ) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Color']
        :rtype: 'Color'
        '''
        pass

    def __sub__(self, other: typing.Union[typing.Sequence[float], 'Color']
                ) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Color']
        :rtype: 'Color'
        '''
        pass

    def __mul__(self, other: typing.Union[int, float]) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Color'
        '''
        pass

    def __truediv__(self, other: typing.Union[int, float]) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Color'
        '''
        pass

    def __radd__(self, other: typing.Union[typing.Sequence[float], 'Color']
                 ) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Color']
        :rtype: 'Color'
        '''
        pass

    def __rsub__(self, other: typing.Union[typing.Sequence[float], 'Color']
                 ) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Color']
        :rtype: 'Color'
        '''
        pass

    def __rmul__(self, other: typing.Union[int, float]) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Color'
        '''
        pass

    def __rtruediv__(self, other: typing.Union[int, float]) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Color'
        '''
        pass

    def __iadd__(self, other: typing.Union[typing.Sequence[float], 'Color']
                 ) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Color']
        :rtype: 'Color'
        '''
        pass

    def __isub__(self, other: typing.Union[typing.Sequence[float], 'Color']
                 ) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Color']
        :rtype: 'Color'
        '''
        pass

    def __imul__(self, other: typing.Union[int, float]) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Color'
        '''
        pass

    def __itruediv__(self, other: typing.Union[int, float]) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Color'
        '''
        pass


class Euler:
    ''' This object gives access to Eulers in Blender. :arg angles: Three angles, in radians. :type angles: 3d vector :arg order: Optional order of the angles, a permutation of ``XYZ``. :type order: str
    '''

    is_frozen: bool = None
    ''' True when this object has been frozen (read-only).

    :type: bool
    '''

    is_valid: bool = None
    ''' True when the owner of this data is valid.

    :type: bool
    '''

    is_wrapped: bool = None
    ''' True when this object wraps external data (read-only).

    :type: bool
    '''

    order: str = None
    ''' Euler rotation order.

    :type: str
    '''

    owner = None
    ''' The item this is wrapping or None (read-only).'''

    x: float = None
    ''' Euler axis angle in radians.

    :type: float
    '''

    y: float = None
    ''' Euler axis angle in radians.

    :type: float
    '''

    z: float = None
    ''' Euler axis angle in radians.

    :type: float
    '''

    @staticmethod
    def copy() -> 'Euler':
        ''' Returns a copy of this euler.

        :rtype: 'Euler'
        :return: A copy of the euler.
        '''
        pass

    @staticmethod
    def freeze() -> 'Euler':
        ''' Make this object immutable. After this the object can be hashed, used in dictionaries & sets.

        :rtype: 'Euler'
        :return: An instance of this object.
        '''
        pass

    def make_compatible(self, other):
        ''' Make this euler compatible with another, so interpolating between them works as intended.

        '''
        pass

    def rotate(self,
               other: typing.Union[typing.Sequence[float], 'Euler', typing.
                                   Sequence[float], 'Quaternion', typing.
                                   Sequence[float], 'Matrix']):
        ''' Rotates the euler by another mathutils value.

        :param other: rotation component of mathutils value
        :type other: typing.Union[typing.Sequence[float], 'Euler', typing.Sequence[float], 'Quaternion', typing.Sequence[float], 'Matrix']
        '''
        pass

    def rotate_axis(self, axis: str, angle: float):
        ''' Rotates the euler a certain amount and returning a unique euler rotation (no 720 degree pitches).

        :param axis: single character in ['X, 'Y', 'Z'].
        :type axis: str
        :param angle: angle in radians.
        :type angle: float
        '''
        pass

    def to_matrix(self) -> 'Matrix':
        ''' Return a matrix representation of the euler.

        :rtype: 'Matrix'
        :return: A 3x3 rotation matrix representation of the euler.
        '''
        pass

    def to_quaternion(self) -> 'Quaternion':
        ''' Return a quaternion representation of the euler.

        :rtype: 'Quaternion'
        :return: Quaternion representation of the euler.
        '''
        pass

    def zero(self):
        ''' Set all values to zero.

        '''
        pass

    def __init__(self, angles=(0.0, 0.0, 0.0), order='XYZ') -> typing.Any:
        ''' 

        :rtype: typing.Any
        '''
        pass


class Matrix:
    ''' This object gives access to Matrices in Blender, supporting square and rectangular matrices from 2x2 up to 4x4. :arg rows: Sequence of rows. When omitted, a 4x4 identity matrix is constructed. :type rows: 2d number sequence
    '''

    col: 'Matrix' = None
    ''' Access the matrix by columns, 3x3 and 4x4 only, (read-only).

    :type: 'Matrix'
    '''

    is_frozen: bool = None
    ''' True when this object has been frozen (read-only).

    :type: bool
    '''

    is_identity: bool = None
    ''' True if this is an identity matrix (read-only).

    :type: bool
    '''

    is_negative: bool = None
    ''' True if this matrix results in a negative scale, 3x3 and 4x4 only, (read-only).

    :type: bool
    '''

    is_orthogonal: bool = None
    ''' True if this matrix is orthogonal, 3x3 and 4x4 only, (read-only).

    :type: bool
    '''

    is_orthogonal_axis_vectors: bool = None
    ''' True if this matrix has got orthogonal axis vectors, 3x3 and 4x4 only, (read-only).

    :type: bool
    '''

    is_valid: bool = None
    ''' True when the owner of this data is valid.

    :type: bool
    '''

    is_wrapped: bool = None
    ''' True when this object wraps external data (read-only).

    :type: bool
    '''

    median_scale: float = None
    ''' The average scale applied to each axis (read-only).

    :type: float
    '''

    owner = None
    ''' The item this is wrapping or None (read-only).'''

    row: 'Matrix' = None
    ''' Access the matrix by rows (default), (read-only).

    :type: 'Matrix'
    '''

    translation: 'Vector' = None
    ''' The translation component of the matrix.

    :type: 'Vector'
    '''

    @classmethod
    def Diagonal(cls, vector: typing.Union[typing.Sequence[float], 'Vector']
                 ) -> 'Matrix':
        ''' Create a diagonal (scaling) matrix using the values from the vector.

        :param vector: The vector of values for the diagonal.
        :type vector: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Matrix'
        :return: A diagonal matrix.
        '''
        pass

    @classmethod
    def Identity(cls, size: int) -> 'Matrix':
        ''' Create an identity matrix.

        :param size: The size of the identity matrix to construct [2, 4].
        :type size: int
        :rtype: 'Matrix'
        :return: A new identity matrix.
        '''
        pass

    @classmethod
    def LocRotScale(
            cls, location: typing.Optional['Vector'], rotation: typing.
            Optional[typing.Union[typing.Sequence[float], 'Quaternion', typing.
                                  Sequence[float], 'Euler']],
            scale: typing.Optional['Vector']) -> 'Matrix':
        ''' Create a matrix combining translation, rotation and scale, acting as the inverse of the decompose() method. Any of the inputs may be replaced with None if not needed.

        :param location: The translation component.
        :type location: typing.Optional['Vector']
        :param rotation: The rotation component.
        :type rotation: typing.Optional[typing.Union[typing.Sequence[float], 'Quaternion', typing.Sequence[float], 'Euler']]
        :param scale: The scale component.
        :type scale: typing.Optional['Vector']
        :rtype: 'Matrix'
        :return: Combined transformation matrix.
        '''
        pass

    @classmethod
    def OrthoProjection(
            cls, axis: typing.Union[str, typing.Sequence[float], 'Vector'],
            size: int) -> 'Matrix':
        ''' Create a matrix to represent an orthographic projection.

        :param axis: ['X', 'Y', 'XY', 'XZ', 'YZ'], where a single axis is for a 2D matrix. Or a vector for an arbitrary axis
        :type axis: typing.Union[str, typing.Sequence[float], 'Vector']
        :param size: The size of the projection matrix to construct [2, 4].
        :type size: int
        :rtype: 'Matrix'
        :return: A new projection matrix.
        '''
        pass

    @classmethod
    def Rotation(cls, angle: float, size: int,
                 axis: typing.Union[str, typing.Sequence[float], 'Vector']
                 ) -> 'Matrix':
        ''' Create a matrix representing a rotation.

        :param angle: The angle of rotation desired, in radians.
        :type angle: float
        :param size: The size of the rotation matrix to construct [2, 4].
        :type size: int
        :param axis: a string in ['X', 'Y', 'Z'] or a 3D Vector Object (optional when size is 2).
        :type axis: typing.Union[str, typing.Sequence[float], 'Vector']
        :rtype: 'Matrix'
        :return: A new rotation matrix.
        '''
        pass

    @classmethod
    def Scale(
            cls, factor: float, size: int,
            axis: typing.Union[typing.Sequence[float], 'Vector']) -> 'Matrix':
        ''' Create a matrix representing a scaling.

        :param factor: The factor of scaling to apply.
        :type factor: float
        :param size: The size of the scale matrix to construct [2, 4].
        :type size: int
        :param axis: Direction to influence scale. (optional).
        :type axis: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Matrix'
        :return: A new scale matrix.
        '''
        pass

    @classmethod
    def Shear(cls, plane: str, size: int, factor: float) -> 'Matrix':
        ''' Create a matrix to represent an shear transformation.

        :param plane: ['X', 'Y', 'XY', 'XZ', 'YZ'], where a single axis is for a 2D matrix only.
        :type plane: str
        :param size: The size of the shear matrix to construct [2, 4].
        :type size: int
        :param factor: The factor of shear to apply. For a 3 or 4 *size* matrix pass a pair of floats corresponding with the *plane* axis.
        :type factor: float
        :rtype: 'Matrix'
        :return: A new shear matrix.
        '''
        pass

    @classmethod
    def Translation(cls, vector: typing.Union[typing.Sequence[float], 'Vector']
                    ) -> 'Matrix':
        ''' Create a matrix representing a translation.

        :param vector: The translation vector.
        :type vector: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Matrix'
        :return: An identity matrix with a translation.
        '''
        pass

    def adjugate(self):
        ''' Set the matrix to its adjugate. :raises ValueError: if the matrix cannot be adjugate.

        '''
        pass

    def adjugated(self) -> 'Matrix':
        ''' Return an adjugated copy of the matrix. :raises ValueError: if the matrix cannot be adjugated

        :rtype: 'Matrix'
        :return: the adjugated matrix.
        '''
        pass

    def copy(self) -> 'Matrix':
        ''' Returns a copy of this matrix.

        :rtype: 'Matrix'
        :return: an instance of itself
        '''
        pass

    def decompose(self) -> 'Quaternion':
        ''' Return the translation, rotation, and scale components of this matrix.

        :rtype: 'Quaternion'
        :return: tuple of translation, rotation, and scale
        '''
        pass

    def determinant(self) -> float:
        ''' Return the determinant of a matrix.

        :rtype: float
        :return: Return the determinant of a matrix.
        '''
        pass

    @staticmethod
    def freeze() -> 'Matrix':
        ''' Make this object immutable. After this the object can be hashed, used in dictionaries & sets.

        :rtype: 'Matrix'
        :return: An instance of this object.
        '''
        pass

    def identity(self):
        ''' Set the matrix to the identity matrix.

        '''
        pass

    def invert(
            self,
            fallback: typing.Union[typing.Sequence[float], 'Matrix'] = None):
        ''' Set the matrix to its inverse.

        :param fallback: Set the matrix to this value when the inverse cannot be calculated (instead of raising a :exc:`ValueError` exception).
        :type fallback: typing.Union[typing.Sequence[float], 'Matrix']
        '''
        pass

    def invert_safe(self):
        ''' Set the matrix to its inverse, will never error. If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one. If tweaked matrix is still degenerated, set to the identity matrix instead.

        '''
        pass

    def inverted(self, fallback: typing.Any = None) -> 'Matrix':
        ''' Return an inverted copy of the matrix.

        :param fallback: return this when the inverse can't be calculated (instead of raising a :exc:`ValueError`).
        :type fallback: typing.Any
        :rtype: 'Matrix'
        :return: the inverted matrix or fallback when given.
        '''
        pass

    def inverted_safe(self) -> 'Matrix':
        ''' Return an inverted copy of the matrix, will never error. If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one. If tweaked matrix is still degenerated, return the identity matrix instead.

        :rtype: 'Matrix'
        :return: the inverted matrix.
        '''
        pass

    @staticmethod
    def lerp(other: typing.Union[typing.Sequence[float], 'Matrix'],
             factor: float) -> 'Matrix':
        ''' Returns the interpolation of two matrices. Uses polar decomposition, see "Matrix Animation and Polar Decomposition", Shoemake and Duff, 1992.

        :param other: value to interpolate with.
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :param factor: The interpolation value in [0.0, 1.0].
        :type factor: float
        :rtype: 'Matrix'
        :return: The interpolated matrix.
        '''
        pass

    def normalize(self):
        ''' Normalize each of the matrix columns.

        '''
        pass

    def normalized(self) -> 'Matrix':
        ''' Return a column normalized matrix

        :rtype: 'Matrix'
        :return: a column normalized matrix
        '''
        pass

    def resize_4x4(self):
        ''' Resize the matrix to 4x4.

        '''
        pass

    def rotate(self,
               other: typing.Union[typing.Sequence[float], 'Euler', typing.
                                   Sequence[float], 'Quaternion', typing.
                                   Sequence[float], 'Matrix']):
        ''' Rotates the matrix by another mathutils value.

        :param other: rotation component of mathutils value
        :type other: typing.Union[typing.Sequence[float], 'Euler', typing.Sequence[float], 'Quaternion', typing.Sequence[float], 'Matrix']
        '''
        pass

    def to_2x2(self) -> 'Matrix':
        ''' Return a 2x2 copy of this matrix.

        :rtype: 'Matrix'
        :return: a new matrix.
        '''
        pass

    def to_3x3(self) -> 'Matrix':
        ''' Return a 3x3 copy of this matrix.

        :rtype: 'Matrix'
        :return: a new matrix.
        '''
        pass

    def to_4x4(self) -> 'Matrix':
        ''' Return a 4x4 copy of this matrix.

        :rtype: 'Matrix'
        :return: a new matrix.
        '''
        pass

    def to_euler(self, order: str,
                 euler_compat: typing.Union[typing.Sequence[float], 'Euler']
                 ) -> 'Euler':
        ''' Return an Euler representation of the rotation matrix (3x3 or 4x4 matrix only).

        :param order: Optional rotation order argument in ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'].
        :type order: str
        :param euler_compat: Optional euler argument the new euler will be made compatible with (no axis flipping between them). Useful for converting a series of matrices to animation curves.
        :type euler_compat: typing.Union[typing.Sequence[float], 'Euler']
        :rtype: 'Euler'
        :return: Euler representation of the matrix.
        '''
        pass

    def to_quaternion(self) -> 'Quaternion':
        ''' Return a quaternion representation of the rotation matrix.

        :rtype: 'Quaternion'
        :return: Quaternion representation of the rotation matrix.
        '''
        pass

    def to_scale(self) -> 'Vector':
        ''' Return the scale part of a 3x3 or 4x4 matrix.

        :rtype: 'Vector'
        :return: Return the scale of a matrix.
        '''
        pass

    def to_translation(self) -> 'Vector':
        ''' Return the translation part of a 4 row matrix.

        :rtype: 'Vector'
        :return: Return the translation of a matrix.
        '''
        pass

    def transpose(self):
        ''' Set the matrix to its transpose.

        '''
        pass

    def transposed(self) -> 'Matrix':
        ''' Return a new, transposed matrix.

        :rtype: 'Matrix'
        :return: a transposed matrix
        '''
        pass

    def zero(self) -> 'Matrix':
        ''' Set all the matrix values to zero.

        :rtype: 'Matrix'
        '''
        pass

    def __init__(self,
                 rows=((1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0),
                       (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0,
                                              1.0))) -> typing.Any:
        ''' 

        :rtype: typing.Any
        '''
        pass

    def __getitem__(self, key: int) -> 'Vector':
        ''' 

        :param key: 
        :type key: int
        :rtype: 'Vector'
        '''
        pass

    def __len__(self) -> int:
        ''' 

        :rtype: int
        '''
        pass

    def __add__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                ) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Matrix'
        '''
        pass

    def __sub__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                ) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Matrix'
        '''
        pass

    def __mul__(self, other: typing.Union[int, float]) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Matrix'
        '''
        pass

    def __matmul__(
            self, other: typing.Union[typing.Sequence[float], 'Matrix', typing.
                                      Sequence[float], 'Vector']
    ) -> typing.Union['Matrix', 'Vector']:
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix', typing.Sequence[float], 'Vector']
        :rtype: typing.Union['Matrix', 'Vector']
        '''
        pass

    def __radd__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                 ) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Matrix'
        '''
        pass

    def __rsub__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                 ) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Matrix'
        '''
        pass

    def __rmul__(self, other: typing.Union[int, float]) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Matrix'
        '''
        pass

    def __rmatmul__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                    ) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Matrix'
        '''
        pass

    def __imul__(self, other: typing.Union[int, float]) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Matrix'
        '''
        pass

    def __imatmul__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                    ) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Matrix'
        '''
        pass


class Quaternion:
    ''' This object gives access to Quaternions in Blender. :arg seq: size 3 or 4 :type seq: `Vector` :arg angle: rotation angle, in radians :type angle: float The constructor takes arguments in various forms: (), *no args* Create an identity quaternion (*wxyz*) Create a quaternion from a ``(w, x, y, z)`` vector. (*exponential_map*) Create a quaternion from a 3d exponential map vector. .. seealso:: :meth:`to_exponential_map` (*axis, angle*) Create a quaternion representing a rotation of *angle* radians over *axis*. .. seealso:: :meth:`to_axis_angle`
    '''

    angle: float = None
    ''' Angle of the quaternion.

    :type: float
    '''

    axis: typing.Union[typing.Sequence[float], 'Vector'] = None
    ''' Quaternion axis as a vector.

    :type: typing.Union[typing.Sequence[float], 'Vector']
    '''

    is_frozen: bool = None
    ''' True when this object has been frozen (read-only).

    :type: bool
    '''

    is_valid: bool = None
    ''' True when the owner of this data is valid.

    :type: bool
    '''

    is_wrapped: bool = None
    ''' True when this object wraps external data (read-only).

    :type: bool
    '''

    magnitude: float = None
    ''' Size of the quaternion (read-only).

    :type: float
    '''

    owner = None
    ''' The item this is wrapping or None (read-only).'''

    w: float = None
    ''' Quaternion axis value.

    :type: float
    '''

    x: float = None
    ''' Quaternion axis value.

    :type: float
    '''

    y: float = None
    ''' Quaternion axis value.

    :type: float
    '''

    z: float = None
    ''' Quaternion axis value.

    :type: float
    '''

    @staticmethod
    def conjugate():
        ''' Set the quaternion to its conjugate (negate x, y, z).

        '''
        pass

    @staticmethod
    def conjugated() -> 'Quaternion':
        ''' Return a new conjugated quaternion.

        :rtype: 'Quaternion'
        :return: a new quaternion.
        '''
        pass

    @staticmethod
    def copy() -> 'Quaternion':
        ''' Returns a copy of this quaternion.

        :rtype: 'Quaternion'
        :return: A copy of the quaternion.
        '''
        pass

    def cross(self, other: typing.Union[typing.Sequence[float], 'Quaternion']
              ) -> 'Quaternion':
        ''' Return the cross product of this quaternion and another.

        :param other: The other quaternion to perform the cross product with.
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        :return: The cross product.
        '''
        pass

    def dot(self, other: typing.Union[typing.Sequence[float], 'Quaternion']
            ) -> float:
        ''' Return the dot product of this quaternion and another.

        :param other: The other quaternion to perform the dot product with.
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :rtype: float
        :return: The dot product.
        '''
        pass

    @staticmethod
    def freeze() -> 'Quaternion':
        ''' Make this object immutable. After this the object can be hashed, used in dictionaries & sets.

        :rtype: 'Quaternion'
        :return: An instance of this object.
        '''
        pass

    @staticmethod
    def identity() -> 'Quaternion':
        ''' Set the quaternion to an identity quaternion.

        :rtype: 'Quaternion'
        '''
        pass

    @staticmethod
    def invert():
        ''' Set the quaternion to its inverse.

        '''
        pass

    @staticmethod
    def inverted() -> 'Quaternion':
        ''' Return a new, inverted quaternion.

        :rtype: 'Quaternion'
        :return: the inverted value.
        '''
        pass

    def make_compatible(self, other):
        ''' Make this quaternion compatible with another, so interpolating between them works as intended.

        '''
        pass

    @staticmethod
    def negate() -> 'Quaternion':
        ''' Set the quaternion to its negative.

        :rtype: 'Quaternion'
        '''
        pass

    @staticmethod
    def normalize():
        ''' Normalize the quaternion.

        '''
        pass

    @staticmethod
    def normalized() -> 'Quaternion':
        ''' Return a new normalized quaternion.

        :rtype: 'Quaternion'
        :return: a normalized copy.
        '''
        pass

    def rotate(self,
               other: typing.Union[typing.Sequence[float], 'Euler', typing.
                                   Sequence[float], 'Quaternion', typing.
                                   Sequence[float], 'Matrix']):
        ''' Rotates the quaternion by another mathutils value.

        :param other: rotation component of mathutils value
        :type other: typing.Union[typing.Sequence[float], 'Euler', typing.Sequence[float], 'Quaternion', typing.Sequence[float], 'Matrix']
        '''
        pass

    @staticmethod
    def rotation_difference(
            other: typing.Union[typing.Sequence[float], 'Quaternion']
    ) -> 'Quaternion':
        ''' Returns a quaternion representing the rotational difference.

        :param other: second quaternion.
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        :return: the rotational difference between the two quat rotations.
        '''
        pass

    @staticmethod
    def slerp(other: typing.Union[typing.Sequence[float], 'Quaternion'],
              factor: float) -> 'Quaternion':
        ''' Returns the interpolation of two quaternions.

        :param other: value to interpolate with.
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :param factor: The interpolation value in [0.0, 1.0].
        :type factor: float
        :rtype: 'Quaternion'
        :return: The interpolated rotation.
        '''
        pass

    def to_axis_angle(self) -> typing.Tuple['Vector', 'float']:
        ''' Return the axis, angle representation of the quaternion.

        :rtype: typing.Tuple['Vector', 'float']
        :return: axis, angle.
        '''
        pass

    def to_euler(self, order: str,
                 euler_compat: typing.Union[typing.Sequence[float], 'Euler']
                 ) -> 'Euler':
        ''' Return Euler representation of the quaternion.

        :param order: Optional rotation order argument in ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'].
        :type order: str
        :param euler_compat: Optional euler argument the new euler will be made compatible with (no axis flipping between them). Useful for converting a series of matrices to animation curves.
        :type euler_compat: typing.Union[typing.Sequence[float], 'Euler']
        :rtype: 'Euler'
        :return: Euler representation of the quaternion.
        '''
        pass

    def to_exponential_map(self) -> 'Vector':
        ''' Return the exponential map representation of the quaternion. This representation consist of the rotation axis multiplied by the rotation angle. Such a representation is useful for interpolation between multiple orientations. To convert back to a quaternion, pass it to the `Quaternion` constructor.

        :rtype: 'Vector'
        :return: exponential map.
        '''
        pass

    def to_matrix(self) -> 'Matrix':
        ''' Return a matrix representation of the quaternion.

        :rtype: 'Matrix'
        :return: A 3x3 rotation matrix representation of the quaternion.
        '''
        pass

    def to_swing_twist(
            self, axis: typing.Any) -> typing.Tuple['Quaternion', 'float']:
        ''' Split the rotation into a swing quaternion with the specified axis fixed at zero, and the remaining twist rotation angle.

        :param axis:  twist axis as a string in ['X', 'Y', 'Z']
        :type axis: typing.Any
        :rtype: typing.Tuple['Quaternion', 'float']
        :return: swing, twist angle.
        '''
        pass

    def __init__(self, seq=(1.0, 0.0, 0.0, 0.0)) -> typing.Any:
        ''' 

        :rtype: typing.Any
        '''
        pass

    def __len__(self) -> int:
        ''' 

        :rtype: int
        '''
        pass

    def __getitem__(self, key: int) -> float:
        ''' 

        :param key: 
        :type key: int
        :rtype: float
        '''
        pass

    def __setitem__(self, key: int, value: float) -> float:
        ''' 

        :param key: 
        :type key: int
        :param value: 
        :type value: float
        :rtype: float
        '''
        pass

    def __add__(self, other: typing.Union[typing.Sequence[float], 'Quaternion']
                ) -> 'Quaternion':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        '''
        pass

    def __sub__(self, other: typing.Union[typing.Sequence[float], 'Quaternion']
                ) -> 'Quaternion':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        '''
        pass

    def __mul__(self, other: typing.Union[int, float, typing.
                                          Sequence[float], 'Quaternion']
                ) -> 'Quaternion':
        ''' 

        :param other: 
        :type other: typing.Union[int, float, typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        '''
        pass

    def __matmul__(
            self, other: typing.Union[typing.Sequence[float], 'Vector', typing.
                                      Sequence[float], 'Quaternion']
    ) -> typing.Union['Vector', 'Quaternion']:
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector', typing.Sequence[float], 'Quaternion']
        :rtype: typing.Union['Vector', 'Quaternion']
        '''
        pass

    def __radd__(self,
                 other: typing.Union[typing.Sequence[float], 'Quaternion']
                 ) -> 'Quaternion':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        '''
        pass

    def __rsub__(self,
                 other: typing.Union[typing.Sequence[float], 'Quaternion']
                 ) -> 'Quaternion':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        '''
        pass

    def __rmul__(self, other: typing.Union[int, float, typing.
                                           Sequence[float], 'Quaternion']
                 ) -> 'Quaternion':
        ''' 

        :param other: 
        :type other: typing.Union[int, float, typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        '''
        pass

    def __rmatmul__(self, other: typing.Union[typing.Sequence[float], 'Vector']
                    ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        '''
        pass

    def __imul__(self, other: typing.Union[int, float, typing.
                                           Sequence[float], 'Quaternion']
                 ) -> 'Quaternion':
        ''' 

        :param other: 
        :type other: typing.Union[int, float, typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        '''
        pass

    def __imatmul__(self, other: typing.Union[typing.Sequence[float], 'Vector']
                    ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        '''
        pass


class Vector:
    ''' This object gives access to Vectors in Blender. :arg seq: Components of the vector, must be a sequence of at least two :type seq: sequence of numbers
    '''

    is_frozen: bool = None
    ''' True when this object has been frozen (read-only).

    :type: bool
    '''

    is_valid: bool = None
    ''' True when the owner of this data is valid.

    :type: bool
    '''

    is_wrapped: bool = None
    ''' True when this object wraps external data (read-only).

    :type: bool
    '''

    length: float = None
    ''' Vector Length.

    :type: float
    '''

    length_squared: float = None
    ''' Vector length squared (v.dot(v)).

    :type: float
    '''

    magnitude: float = None
    ''' Vector Length.

    :type: float
    '''

    owner = None
    ''' The item this is wrapping or None (read-only).'''

    w: float = None
    ''' Vector W axis (4D Vectors only).

    :type: float
    '''

    ww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    www = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwwx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwwy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwwz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wwzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxwx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxwy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxwz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wxzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wywx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wywy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wywz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wyzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzwx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzwy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzwz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    wzzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    x: float = None
    ''' Vector X axis.

    :type: float
    '''

    xw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwwx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwwy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwwz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xwzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxwx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxwy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxwz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xxzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xywx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xywy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xywz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xyzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzwx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzwy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzwz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    xzzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    y: float = None
    ''' Vector Y axis.

    :type: float
    '''

    yw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywwx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywwy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywwz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    ywzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxwx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxwy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxwz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yxzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yywx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yywy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yywz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yyzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzwx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzwy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzwz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    yzzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    z: float = None
    ''' Vector Z axis (3D Vectors only).

    :type: float
    '''

    zw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwwx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwwy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwwz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zwzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxwx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxwy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxwz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zxzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zywx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zywy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zywz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zyzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzww = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzwx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzwy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzwz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzxw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzxx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzxy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzxz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzyw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzyx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzyy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzyz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzzw = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzzx = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzzy = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    zzzz = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.'''

    @classmethod
    def Fill(cls, size: int, fill: float = 0.0):
        ''' Create a vector of length size with all values set to fill.

        :param size: The length of the vector to be created.
        :type size: int
        :param fill: The value used to fill the vector.
        :type fill: float
        '''
        pass

    @classmethod
    def Linspace(cls, start: int, stop: int, size: int):
        ''' Create a vector of the specified size which is filled with linearly spaced values between start and stop values.

        :param start: The start of the range used to fill the vector.
        :type start: int
        :param stop: The end of the range used to fill the vector.
        :type stop: int
        :param size: The size of the vector to be created.
        :type size: int
        '''
        pass

    @classmethod
    def Range(cls, start: int, stop: int, step: int = 1):
        ''' Create a filled with a range of values.

        :param start: The start of the range used to fill the vector.
        :type start: int
        :param stop: The end of the range used to fill the vector.
        :type stop: int
        :param step: The step between successive values in the vector.
        :type step: int
        '''
        pass

    @classmethod
    def Repeat(cls, vector, size: int):
        ''' Create a vector by repeating the values in vector until the required size is reached.

        :param tuple: The vector to draw values from.
        :type tuple: typing.Union[typing.Sequence[float], 'Vector']
        :param size: The size of the vector to be created.
        :type size: int
        '''
        pass

    @staticmethod
    def angle(other: typing.Union[typing.Sequence[float], 'Vector'],
              fallback: typing.Any = None) -> float:
        ''' Return the angle between two vectors.

        :param other: another vector to compare the angle with
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :param fallback: return this when the angle can't be calculated (zero length vector), (instead of raising a :exc:`ValueError`).
        :type fallback: typing.Any
        :rtype: float
        :return: angle in radians or fallback when given
        '''
        pass

    @staticmethod
    def angle_signed(other: typing.Union[typing.Sequence[float], 'Vector'],
                     fallback: typing.Any) -> float:
        ''' Return the signed angle between two 2D vectors (clockwise is positive).

        :param other: another vector to compare the angle with
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :param fallback: return this when the angle can't be calculated (zero length vector), (instead of raising a :exc:`ValueError`).
        :type fallback: typing.Any
        :rtype: float
        :return: angle in radians or fallback when given
        '''
        pass

    @staticmethod
    def copy() -> 'Vector':
        ''' Returns a copy of this vector.

        :rtype: 'Vector'
        :return: A copy of the vector.
        '''
        pass

    def cross(self, other: typing.Union[typing.Sequence[float], 'Vector']
              ) -> 'Vector':
        ''' Return the cross product of this vector and another.

        :param other: The other vector to perform the cross product with.
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        :return: The cross product.
        '''
        pass

    def dot(self,
            other: typing.Union[typing.Sequence[float], 'Vector']) -> float:
        ''' Return the dot product of this vector and another.

        :param other: The other vector to perform the dot product with.
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: float
        :return: The dot product.
        '''
        pass

    @staticmethod
    def freeze() -> 'Vector':
        ''' Make this object immutable. After this the object can be hashed, used in dictionaries & sets.

        :rtype: 'Vector'
        :return: An instance of this object.
        '''
        pass

    @staticmethod
    def lerp(other: typing.Union[typing.Sequence[float], 'Vector'],
             factor: float) -> 'Vector':
        ''' Returns the interpolation of two vectors.

        :param other: value to interpolate with.
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :param factor: The interpolation value in [0.0, 1.0].
        :type factor: float
        :rtype: 'Vector'
        :return: The interpolated vector.
        '''
        pass

    def negate(self):
        ''' Set all values to their negative.

        '''
        pass

    def normalize(self):
        ''' Normalize the vector, making the length of the vector always 1.0.

        '''
        pass

    def normalized(self) -> 'Vector':
        ''' Return a new, normalized vector.

        :rtype: 'Vector'
        :return: a normalized copy of the vector
        '''
        pass

    def orthogonal(self) -> 'Vector':
        ''' Return a perpendicular vector.

        :rtype: 'Vector'
        :return: a new vector 90 degrees from this vector.
        '''
        pass

    @staticmethod
    def project(
            other: typing.Union[typing.Sequence[float], 'Vector']) -> 'Vector':
        ''' Return the projection of this vector onto the *other*.

        :param other: second vector.
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        :return: the parallel projection vector
        '''
        pass

    def reflect(self, mirror: typing.Union[typing.Sequence[float], 'Vector']
                ) -> 'Vector':
        ''' Return the reflection vector from the *mirror* argument.

        :param mirror: This vector could be a normal from the reflecting surface.
        :type mirror: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        :return: The reflected vector matching the size of this vector.
        '''
        pass

    def resize(self, size=3):
        ''' Resize the vector to have size number of elements.

        '''
        pass

    def resize_2d(self):
        ''' Resize the vector to 2D (x, y).

        '''
        pass

    def resize_3d(self):
        ''' Resize the vector to 3D (x, y, z).

        '''
        pass

    def resize_4d(self):
        ''' Resize the vector to 4D (x, y, z, w).

        '''
        pass

    def resized(self, size=3) -> 'Vector':
        ''' Return a resized copy of the vector with size number of elements.

        :rtype: 'Vector'
        :return: a new vector
        '''
        pass

    @staticmethod
    def rotate(other: typing.Union[typing.Sequence[float], 'Euler', typing.
                                   Sequence[float], 'Quaternion', typing.
                                   Sequence[float], 'Matrix']):
        ''' Rotate the vector by a rotation value.

        :param other: rotation component of mathutils value
        :type other: typing.Union[typing.Sequence[float], 'Euler', typing.Sequence[float], 'Quaternion', typing.Sequence[float], 'Matrix']
        '''
        pass

    @staticmethod
    def rotation_difference(
            other: typing.Union[typing.Sequence[float], 'Vector']
    ) -> 'Quaternion':
        ''' Returns a quaternion representing the rotational difference between this vector and another.

        :param other: second vector.
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Quaternion'
        :return: the rotational difference between the two vectors.
        '''
        pass

    @staticmethod
    def slerp(other: typing.Union[typing.Sequence[float], 'Vector'],
              factor: float,
              fallback: typing.Any = None) -> 'Vector':
        ''' Returns the interpolation of two non-zero vectors (spherical coordinates).

        :param other: value to interpolate with.
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :param factor: The interpolation value typically in [0.0, 1.0].
        :type factor: float
        :param fallback: return this when the vector can't be calculated (zero length vector or direct opposites), (instead of raising a :exc:`ValueError`).
        :type fallback: typing.Any
        :rtype: 'Vector'
        :return: The interpolated vector.
        '''
        pass

    def to_2d(self) -> 'Vector':
        ''' Return a 2d copy of the vector.

        :rtype: 'Vector'
        :return: a new vector
        '''
        pass

    def to_3d(self) -> 'Vector':
        ''' Return a 3d copy of the vector.

        :rtype: 'Vector'
        :return: a new vector
        '''
        pass

    def to_4d(self) -> 'Vector':
        ''' Return a 4d copy of the vector.

        :rtype: 'Vector'
        :return: a new vector
        '''
        pass

    def to_track_quat(self, track: str, up: str) -> 'Quaternion':
        ''' Return a quaternion rotation from the vector and the track and up axis.

        :param track: Track axis in ['X', 'Y', 'Z', '-X', '-Y', '-Z'].
        :type track: str
        :param up: Up axis in ['X', 'Y', 'Z'].
        :type up: str
        :rtype: 'Quaternion'
        :return: rotation from the vector and the track and up axis.
        '''
        pass

    def to_tuple(self, precision: int = -1) -> typing.Tuple:
        ''' Return this vector as a tuple with.

        :param precision: The number to round the value to in [-1, 21].
        :type precision: int
        :rtype: typing.Tuple
        :return: the values of the vector rounded by *precision*
        '''
        pass

    def zero(self):
        ''' Set all values to zero.

        '''
        pass

    def __init__(self, seq=(0.0, 0.0, 0.0)) -> typing.Any:
        ''' 

        :rtype: typing.Any
        '''
        pass

    def __len__(self) -> int:
        ''' 

        :rtype: int
        '''
        pass

    def __getitem__(self, key: int) -> float:
        ''' 

        :param key: 
        :type key: int
        :rtype: float
        '''
        pass

    def __setitem__(self, key: int, value: float) -> float:
        ''' 

        :param key: 
        :type key: int
        :param value: 
        :type value: float
        :rtype: float
        '''
        pass

    def __neg__(self) -> 'Vector':
        ''' 

        :rtype: 'Vector'
        '''
        pass

    def __add__(self, other: typing.Union[typing.Sequence[float], 'Vector']
                ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        '''
        pass

    def __sub__(self, other: typing.Union[typing.Sequence[float], 'Vector']
                ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        '''
        pass

    def __mul__(self, other: typing.Union[int, float]) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Vector'
        '''
        pass

    def __truediv__(self, other: typing.Union[int, float]) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Vector'
        '''
        pass

    def __matmul__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                   ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Vector'
        '''
        pass

    def __radd__(self, other: typing.Union[typing.Sequence[float], 'Vector']
                 ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        '''
        pass

    def __rsub__(self, other: typing.Union[typing.Sequence[float], 'Vector']
                 ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        '''
        pass

    def __rmul__(self, other: typing.Union[int, float]) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Vector'
        '''
        pass

    def __rtruediv__(self, other: typing.Union[int, float]) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Vector'
        '''
        pass

    def __rmatmul__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                    ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Vector'
        '''
        pass

    def __iadd__(self, other: typing.Union[typing.Sequence[float], 'Vector']
                 ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        '''
        pass

    def __isub__(self, other: typing.Union[typing.Sequence[float], 'Vector']
                 ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        '''
        pass

    def __imul__(self, other: typing.Union[int, float]) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Vector'
        '''
        pass

    def __itruediv__(self, other: typing.Union[int, float]) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Vector'
        '''
        pass

    def __imatmul__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                    ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Vector'
        '''
        pass
