"""
The Blender noise module

"""

import typing
import collections.abc
import typing_extensions
import mathutils

def cell(position: collections.abc.Sequence[float] | mathutils.Vector) -> float:
    """Returns cell noise value at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: collections.abc.Sequence[float] | mathutils.Vector
    :return: The cell noise value.
    :rtype: float
    """

def cell_vector(
    position: collections.abc.Sequence[float] | mathutils.Vector,
) -> mathutils.Vector:
    """Returns cell noise vector at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: collections.abc.Sequence[float] | mathutils.Vector
    :return: The cell noise vector.
    :rtype: mathutils.Vector
    """

def fractal(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    H: float,
    lacunarity: float,
    octaves: int,
    noise_basis: str = "PERLIN_ORIGINAL",
) -> float:
    """Returns the fractal Brownian motion (fBm) noise value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: collections.abc.Sequence[float] | mathutils.Vector
    :param H: The fractal increment factor.
    :type H: float
    :param lacunarity: The gap between successive frequencies.
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used.
    :type octaves: int
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :return: The fractal Brownian motion noise value.
    :rtype: float
    """

def hetero_terrain(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    H: float,
    lacunarity: float,
    octaves: int,
    offset: float,
    noise_basis: str = "PERLIN_ORIGINAL",
) -> float:
    """Returns the heterogeneous terrain value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: collections.abc.Sequence[float] | mathutils.Vector
    :param H: The fractal dimension of the roughest areas.
    :type H: float
    :param lacunarity: The gap between successive frequencies.
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used.
    :type octaves: int
    :param offset: The height of the terrain above 'sea level'.
    :type offset: float
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :return: The heterogeneous terrain value.
    :rtype: float
    """

def hybrid_multi_fractal(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    H: float,
    lacunarity: float,
    octaves: int,
    offset: float,
    gain: float,
    noise_basis: str = "PERLIN_ORIGINAL",
) -> float:
    """Returns hybrid multifractal value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: collections.abc.Sequence[float] | mathutils.Vector
    :param H: The fractal dimension of the roughest areas.
    :type H: float
    :param lacunarity: The gap between successive frequencies.
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used.
    :type octaves: int
    :param offset: The height of the terrain above 'sea level'.
    :type offset: float
    :param gain: Scaling applied to the values.
    :type gain: float
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :return: The hybrid multifractal value.
    :rtype: float
    """

def multi_fractal(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    H: float,
    lacunarity: float,
    octaves: int,
    noise_basis: str = "PERLIN_ORIGINAL",
) -> float:
    """Returns multifractal noise value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: collections.abc.Sequence[float] | mathutils.Vector
    :param H: The fractal increment factor.
    :type H: float
    :param lacunarity: The gap between successive frequencies.
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used.
    :type octaves: int
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :return: The multifractal noise value.
    :rtype: float
    """

def noise(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    noise_basis: str = "PERLIN_ORIGINAL",
) -> float:
    """Returns noise value from the noise basis at the position specified.

    :param position: The position to evaluate the selected noise function.
    :type position: collections.abc.Sequence[float] | mathutils.Vector
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :return: The noise value.
    :rtype: float
    """

def noise_vector(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    noise_basis: str = "PERLIN_ORIGINAL",
) -> mathutils.Vector:
    """Returns the noise vector from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: collections.abc.Sequence[float] | mathutils.Vector
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :return: The noise vector.
    :rtype: mathutils.Vector
    """

def random() -> float:
    """Returns a random number in the range [0, 1).

    :return: The random number.
    :rtype: float
    """

def random_unit_vector(size: int = 3) -> mathutils.Vector:
    """Returns a unit vector with random entries.

    :param size: The size of the vector to be produced, in the range [2, 4].
    :type size: int
    :return: The random unit vector.
    :rtype: mathutils.Vector
    """

def random_vector(size: int = 3) -> mathutils.Vector:
    """Returns a vector with random entries in the range (-1, 1).

    :param size: The size of the vector to be produced.
    :type size: int
    :return: The random vector.
    :rtype: mathutils.Vector
    """

def ridged_multi_fractal(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    H: float,
    lacunarity: float,
    octaves: int,
    offset: float,
    gain: float,
    noise_basis: str = "PERLIN_ORIGINAL",
) -> float:
    """Returns ridged multifractal value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: collections.abc.Sequence[float] | mathutils.Vector
    :param H: The fractal dimension of the roughest areas.
    :type H: float
    :param lacunarity: The gap between successive frequencies.
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used.
    :type octaves: int
    :param offset: The height of the terrain above 'sea level'.
    :type offset: float
    :param gain: Scaling applied to the values.
    :type gain: float
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :return: The ridged multifractal value.
    :rtype: float
    """

def seed_set(seed: int):
    """Sets the random seed used for random_unit_vector, and random.

        :param seed: Seed used for the random generator.
    When seed is zero, the current time will be used instead.
        :type seed: int
    """

def turbulence(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    octaves: int,
    hard: bool,
    noise_basis: str = "PERLIN_ORIGINAL",
    amplitude_scale: float = 0.5,
    frequency_scale: float = 2.0,
) -> float:
    """Returns the turbulence value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: collections.abc.Sequence[float] | mathutils.Vector
    :param octaves: The number of different noise frequencies used.
    :type octaves: int
    :param hard: Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
    :type hard: bool
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :param amplitude_scale: The amplitude scaling factor.
    :type amplitude_scale: float
    :param frequency_scale: The frequency scaling factor
    :type frequency_scale: float
    :return: The turbulence value.
    :rtype: float
    """

def turbulence_vector(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    octaves: int,
    hard: bool,
    noise_basis: str = "PERLIN_ORIGINAL",
    amplitude_scale: float = 0.5,
    frequency_scale: float = 2.0,
) -> mathutils.Vector:
    """Returns the turbulence vector from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: collections.abc.Sequence[float] | mathutils.Vector
    :param octaves: The number of different noise frequencies used.
    :type octaves: int
    :param hard: Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
    :type hard: bool
    :param noise_basis: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_basis: str
    :param amplitude_scale: The amplitude scaling factor.
    :type amplitude_scale: float
    :param frequency_scale: The frequency scaling factor
    :type frequency_scale: float
    :return: The turbulence vector.
    :rtype: mathutils.Vector
    """

def variable_lacunarity(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    distortion: float,
    noise_type1: str = "PERLIN_ORIGINAL",
    noise_type2: str = "PERLIN_ORIGINAL",
) -> float:
    """Returns variable lacunarity noise value, a distorted variety of noise, from noise type 1 distorted by noise type 2 at the specified position.

    :param position: The position to evaluate the selected noise function.
    :type position: collections.abc.Sequence[float] | mathutils.Vector
    :param distortion: The amount of distortion.
    :type distortion: float
    :param noise_type1: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_type1: str
    :param noise_type2: Enumerator in ['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
    :type noise_type2: str
    :return: The variable lacunarity noise value.
    :rtype: float
    """

def voronoi(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    distance_metric: str = "DISTANCE",
    exponent: float = 2.5,
):
    """Returns a list of distances to the four closest features and their locations.

    :param position: The position to evaluate the selected noise function.
    :type position: collections.abc.Sequence[float] | mathutils.Vector
    :param distance_metric: Enumerator in ['DISTANCE', 'DISTANCE_SQUARED', 'MANHATTAN', 'CHEBYCHEV', 'MINKOVSKY', 'MINKOVSKY_HALF', 'MINKOVSKY_FOUR'].
    :type distance_metric: str
    :param exponent: The exponent for Minkowski distance metric.
    :type exponent: float
    :return: A list of distances to the four closest features and their locations.
    """
