import sys
import typing
import mathutils

from . import types


def cell(position: 'mathutils.Vector') -> float:
    '''Returns cell noise value at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: 'mathutils.Vector'
    :return:  The cell noise value. 
    '''

    pass


def cell_vector(position: 'mathutils.Vector') -> 'mathutils.Vector':
    '''Returns cell noise vector at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: 'mathutils.Vector'
    :return:  The cell noise vector. 
    '''

    pass


def fractal(position: 'mathutils.Vector',
            H: float,
            lacunarity: float,
            octaves: int,
            noise_basis: int = types.STDPERLIN) -> float:
    '''Returns the fractal Brownian motion (fBm) noise value from the noise basis at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: 'mathutils.Vector'
    :param H: The fractal increment factor. 
    :type H: float
    :param lacunarity: The gap between successive frequencies. 
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used. 
    :type octaves: int
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: int
    :return:  The fractal Brownian motion noise value. 
    '''

    pass


def hetero_terrain(position: 'mathutils.Vector',
                   H: float,
                   lacunarity: float,
                   octaves: int,
                   offset: float,
                   noise_basis: int = types.STDPERLIN) -> float:
    '''Returns the heterogeneous terrain value from the noise basis at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: 'mathutils.Vector'
    :param H: The fractal dimension of the roughest areas. 
    :type H: float
    :param lacunarity: The gap between successive frequencies. 
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used. 
    :type octaves: int
    :param offset: The height of the terrain above ‘sea level’. 
    :type offset: float
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: int
    :return:  The heterogeneous terrain value. 
    '''

    pass


def hybrid_multi_fractal(position: 'mathutils.Vector',
                         H: float,
                         lacunarity: float,
                         octaves: int,
                         offset: float,
                         gain: float,
                         noise_basis: int = types.STDPERLIN) -> float:
    '''Returns hybrid multifractal value from the noise basis at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: 'mathutils.Vector'
    :param H: The fractal dimension of the roughest areas. 
    :type H: float
    :param lacunarity: The gap between successive frequencies. 
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used. 
    :type octaves: int
    :param offset: The height of the terrain above ‘sea level’. 
    :type offset: float
    :param gain: Scaling applied to the values. 
    :type gain: float
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: int
    :return:  The hybrid multifractal value. 
    '''

    pass


def multi_fractal(position: 'mathutils.Vector',
                  H: float,
                  lacunarity: float,
                  octaves: int,
                  noise_basis: int = types.STDPERLIN) -> float:
    '''Returns multifractal noise value from the noise basis at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: 'mathutils.Vector'
    :param H: The fractal increment factor. 
    :type H: float
    :param lacunarity: The gap between successive frequencies. 
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used. 
    :type octaves: int
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: int
    :return:  The multifractal noise value. 
    '''

    pass


def noise(position: 'mathutils.Vector',
          noise_basis: int = types.STDPERLIN) -> float:
    '''Returns noise value from the noise basis at the position specified. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: 'mathutils.Vector'
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: int
    :return:  The noise value. 
    '''

    pass


def noise_vector(position: 'mathutils.Vector',
                 noise_basis: int = types.STDPERLIN) -> 'mathutils.Vector':
    '''Returns the noise vector from the noise basis at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: 'mathutils.Vector'
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: int
    :return:  The noise vector. 
    '''

    pass


def random() -> float:
    '''Returns a random number in the range [0, 1]. 

    :return:  The random number. 
    '''

    pass


def random_unit_vector(size=3) -> 'mathutils.Vector':
    '''Returns a unit vector with random entries. 

    :param size: The size of the vector to be produced. 
    :return:  The random unit vector. 
    '''

    pass


def ridged_multi_fractal(position: 'mathutils.Vector',
                         H: float,
                         lacunarity: float,
                         octaves: int,
                         offset: float,
                         gain: float,
                         noise_basis: int = types.STDPERLIN) -> float:
    '''Returns ridged multifractal value from the noise basis at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: 'mathutils.Vector'
    :param H: The fractal dimension of the roughest areas. 
    :type H: float
    :param lacunarity: The gap between successive frequencies. 
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used. 
    :type octaves: int
    :param offset: The height of the terrain above ‘sea level’. 
    :type offset: float
    :param gain: Scaling applied to the values. 
    :type gain: float
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: int
    :return:  The ridged multifractal value. 
    '''

    pass


def seed_set(seed):
    '''Sets the random seed used for random_unit_vector, random_vector and random. 

    :param seed: Seed used for the random generator. When seed is zero, the current time will be used instead. 
    '''

    pass


def turbulence(position: 'mathutils.Vector',
               octaves: int,
               hard,
               noise_basis: int = types.STDPERLIN,
               amplitude_scale: float = 0.5,
               frequency_scale: int = 2.0) -> float:
    '''Returns the turbulence value from the noise basis at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: 'mathutils.Vector'
    :param octaves: The number of different noise frequencies used. 
    :type octaves: int
    :param hard: Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions). 
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: int
    :param amplitude_scale: The amplitude scaling factor. 
    :type amplitude_scale: float
    :param frequency_scale: The frequency scaling factor 
    :type frequency_scale: int
    :return:  The turbulence value. 
    '''

    pass


def turbulence_vector(position: 'mathutils.Vector',
                      octaves: int,
                      hard,
                      noise_basis: int = types.STDPERLIN,
                      amplitude_scale: float = 0.5,
                      frequency_scale: int = 2.0) -> 'mathutils.Vector':
    '''Returns the turbulence vector from the noise basis at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: 'mathutils.Vector'
    :param octaves: The number of different noise frequencies used. 
    :type octaves: int
    :param hard: Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions). 
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: int
    :param amplitude_scale: The amplitude scaling factor. 
    :type amplitude_scale: float
    :param frequency_scale: The frequency scaling factor 
    :type frequency_scale: int
    :return:  The turbulence vector. 
    '''

    pass


def variable_lacunarity(position: 'mathutils.Vector',
                        distortion: float,
                        noise_type1: int = types.STDPERLIN,
                        noise_type2: int = types.STDPERLIN) -> float:
    '''Returns variable lacunarity noise value, a distorted variety of noise, from noise type 1 distorted by noise type 2 at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: 'mathutils.Vector'
    :param distortion: The amount of distortion. 
    :type distortion: float
    :param noise_type1: The type of noise to be distorted. 
    :type noise_type1: int
    :param noise_type2: The type of noise used to distort noise_type1. 
    :type noise_type2: int
    :return:  The variable lacunarity noise value. 
    '''

    pass


def voronoi(position: 'mathutils.Vector',
            distance_metric: int = noise.distance_metrics.DISTANCE,
            exponent: float = 2.5) -> typing.List['mathutils.Vector']:
    '''Returns a list of distances to the four closest features and their locations. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: 'mathutils.Vector'
    :param distance_metric: Method of measuring distance. 
    :type distance_metric: int
    :param exponent: The exponent for Minkowski distance metric. 
    :type exponent: float
    :return:  A list of distances to the four closest features and their locations. 
    '''

    pass
