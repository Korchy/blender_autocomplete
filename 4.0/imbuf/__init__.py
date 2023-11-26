import sys
import typing
import imbuf.types

from . import types

GenericType = typing.TypeVar("GenericType")


def load(filepath: typing.Union[str, bytes]) -> 'imbuf.types.ImBuf':
    ''' Load an image from a file.

    :param filepath: the filepath of the image.
    :type filepath: typing.Union[str, bytes]
    :rtype: 'imbuf.types.ImBuf'
    :return: the newly loaded image.
    '''

    pass


def new(size: typing.Any) -> 'imbuf.types.ImBuf':
    ''' Load a new image.

    :param size: The size of the image in pixels.
    :type size: typing.Any
    :rtype: 'imbuf.types.ImBuf'
    :return: the newly loaded image.
    '''

    pass


def write(image: 'imbuf.types.ImBuf',
          filepath: typing.Union[str, bytes] = 'image.filepath'):
    ''' Write an image.

    :param image: the image to write.
    :type image: 'imbuf.types.ImBuf'
    :param filepath: Optional filepath of the image (fallback to the images file path).
    :type filepath: typing.Union[str, bytes]
    '''

    pass
