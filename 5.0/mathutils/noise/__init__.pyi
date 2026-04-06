"""
The Blender noise module.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import mathutils

def cell(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    /,
) -> float:
    """Returns cell noise value at the specified position.

    :param position: The position to evaluate the selected noise function.
    :return: The cell noise value.
    """

def cell_vector(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    /,
) -> mathutils.Vector:
    """Returns cell noise vector at the specified position.

    :param position: The position to evaluate the selected noise function.
    :return: The cell noise vector.
    """

def fractal(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    H: float,
    lacunarity: float,
    octaves: int,
    /,
    *,
    noise_basis="PERLIN_ORIGINAL",
) -> float:
    """Returns the fractal Brownian motion (fBm) noise value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :param H: The fractal increment factor.
    :param lacunarity: The gap between successive frequencies.
    :param octaves: The number of different noise frequencies used.
    :param noise_basis: A noise basis string.
    :return: The fractal Brownian motion noise value.
    """

def hetero_terrain(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    H: float,
    lacunarity: float,
    octaves: int,
    offset: float,
    /,
    *,
    noise_basis="PERLIN_ORIGINAL",
) -> float:
    """Returns the heterogeneous terrain value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :param H: The fractal dimension of the roughest areas.
    :param lacunarity: The gap between successive frequencies.
    :param octaves: The number of different noise frequencies used.
    :param offset: The height of the terrain above sea level.
    :param noise_basis: A noise basis string.
    :return: The heterogeneous terrain value.
    """

def hybrid_multi_fractal(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    H: float,
    lacunarity: float,
    octaves: int,
    offset: float,
    gain: float,
    /,
    *,
    noise_basis="PERLIN_ORIGINAL",
) -> float:
    """Returns hybrid multifractal value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :param H: The fractal dimension of the roughest areas.
    :param lacunarity: The gap between successive frequencies.
    :param octaves: The number of different noise frequencies used.
    :param offset: The height of the terrain above sea level.
    :param gain: Scaling applied to the values.
    :param noise_basis: A noise basis string.
    :return: The hybrid multifractal value.
    """

def multi_fractal(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    H: float,
    lacunarity: float,
    octaves: int,
    /,
    *,
    noise_basis="PERLIN_ORIGINAL",
) -> float:
    """Returns multifractal noise value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :param H: The fractal increment factor.
    :param lacunarity: The gap between successive frequencies.
    :param octaves: The number of different noise frequencies used.
    :param noise_basis: A noise basis string.
    :return: The multifractal noise value.
    """

def noise(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    /,
    *,
    noise_basis="PERLIN_ORIGINAL",
) -> float:
    """Returns noise value from the noise basis at the position specified.

    :param position: The position to evaluate the selected noise function.
    :param noise_basis: A noise basis string.
    :return: The noise value.
    """

def noise_vector(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    /,
    *,
    noise_basis="PERLIN_ORIGINAL",
) -> mathutils.Vector:
    """Returns the noise vector from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :param noise_basis: A noise basis string.
    :return: The noise vector.
    """

def random() -> float:
    """Returns a random number in the range [0, 1).

    :return: The random number.
    """

def random_unit_vector(*, size: int = 3) -> mathutils.Vector:
    """Returns a unit vector with random entries.

    :param size: The size of the vector to be produced, in the range [2, 4].
    :return: The random unit vector.
    """

def random_vector(*, size: int = 3) -> mathutils.Vector:
    """Returns a vector with random entries in the range (-1, 1).

    :param size: The size of the vector to be produced.
    :return: The random vector.
    """

def ridged_multi_fractal(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    H: float,
    lacunarity: float,
    octaves: int,
    offset: float,
    gain: float,
    /,
    *,
    noise_basis="PERLIN_ORIGINAL",
) -> float:
    """Returns ridged multifractal value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :param H: The fractal dimension of the roughest areas.
    :param lacunarity: The gap between successive frequencies.
    :param octaves: The number of different noise frequencies used.
    :param offset: The height of the terrain above sea level.
    :param gain: Scaling applied to the values.
    :param noise_basis: A noise basis string.
    :return: The ridged multifractal value.
    """

def seed_set(
    seed: int,
    /,
) -> None:
    """Sets the random seed used for random_unit_vector, and random.

        :param seed: Seed used for the random generator.
    When seed is zero, the current time will be used instead.
    """

def turbulence(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    octaves: int,
    hard: bool,
    /,
    *,
    noise_basis="PERLIN_ORIGINAL",
    amplitude_scale: float = 0.5,
    frequency_scale: float = 2.0,
) -> float:
    """Returns the turbulence value from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :param octaves: The number of different noise frequencies used.
    :param hard: Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
    :param noise_basis: A noise basis string.
    :param amplitude_scale: The amplitude scaling factor.
    :param frequency_scale: The frequency scaling factor
    :return: The turbulence value.
    """

def turbulence_vector(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    octaves: int,
    hard: bool,
    /,
    *,
    noise_basis="PERLIN_ORIGINAL",
    amplitude_scale: float = 0.5,
    frequency_scale: float = 2.0,
) -> mathutils.Vector:
    """Returns the turbulence vector from the noise basis at the specified position.

    :param position: The position to evaluate the selected noise function.
    :param octaves: The number of different noise frequencies used.
    :param hard: Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
    :param noise_basis: A noise basis string.
    :param amplitude_scale: The amplitude scaling factor.
    :param frequency_scale: The frequency scaling factor
    :return: The turbulence vector.
    """

def variable_lacunarity(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    distortion: float,
    /,
    *,
    noise_type1="PERLIN_ORIGINAL",
    noise_type2="PERLIN_ORIGINAL",
) -> float:
    """Returns variable lacunarity noise value, a distorted variety of noise, from noise type 1 distorted by noise type 2 at the specified position.

    :param position: The position to evaluate the selected noise function.
    :param distortion: The amount of distortion.
    :param noise_type1: A noise type string.
    :param noise_type2: A noise type string.
    :return: The variable lacunarity noise value.
    """

def voronoi(
    position: collections.abc.Sequence[float] | mathutils.Vector,
    /,
    *,
    distance_metric="DISTANCE",
    exponent: float = 2.5,
) -> list[list[float] | list[mathutils.Vector]]:
    """Returns a list of distances to the four closest features and their locations.

    :param position: The position to evaluate the selected noise function.
    :param distance_metric: A distance metric string.
    :param exponent: The exponent for Minkowski distance metric.
    :return: A list of distances to the four closest features and their locations.
    """
