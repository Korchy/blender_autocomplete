import sys
import typing
import mathutils

GenericType = typing.TypeVar("GenericType")


def get_model_view_matrix() -> 'mathutils.Matrix':
    ''' Return a copy of the model-view matrix.

    :rtype: 'mathutils.Matrix'
    :return: A 4x4 view matrix.
    '''

    pass


def get_normal_matrix() -> 'mathutils.Matrix':
    ''' Return a copy of the normal matrix.

    :rtype: 'mathutils.Matrix'
    :return: A 3x3 normal matrix.
    '''

    pass


def get_projection_matrix() -> 'mathutils.Matrix':
    ''' Return a copy of the projection matrix.

    :rtype: 'mathutils.Matrix'
    :return: A 4x4 projection matrix.
    '''

    pass


def load_identity():
    ''' Empty stack and set to identity.

    '''

    pass


def load_matrix(
        matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']):
    ''' Load a matrix into the stack.

    :param matrix: A 4x4 matrix.
    :type matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    '''

    pass


def load_projection_matrix(
        matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']):
    ''' Load a projection matrix into the stack.

    :param matrix: A 4x4 matrix.
    :type matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    '''

    pass


def multiply_matrix(
        matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']):
    ''' Multiply the current stack matrix.

    :param matrix: A 4x4 matrix.
    :type matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
    '''

    pass


def pop():
    ''' Remove the last model-view matrix from the stack.

    '''

    pass


def pop_projection():
    ''' Remove the last projection matrix from the stack.

    '''

    pass


def push():
    ''' Add to the model-view matrix stack.

    '''

    pass


def push_pop():
    ''' Context manager to ensure balanced push/pop calls, even in the case of an error.

    '''

    pass


def push_pop_projection():
    ''' Context manager to ensure balanced push/pop calls, even in the case of an error.

    '''

    pass


def push_projection():
    ''' Add to the projection matrix stack.

    '''

    pass


def reset():
    ''' Empty stack and set to identity.

    '''

    pass


def scale(scale: typing.List):
    ''' Scale the current stack matrix.

    :param scale: Scale the current stack matrix.
    :type scale: typing.List
    '''

    pass


def scale_uniform(scale: float):
    ''' 

    :param scale: Scale the current stack matrix.
    :type scale: float
    '''

    pass


def translate(offset: typing.List):
    ''' Scale the current stack matrix.

    :param offset: Translate the current stack matrix.
    :type offset: typing.List
    '''

    pass
