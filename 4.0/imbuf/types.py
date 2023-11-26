import sys
import typing

GenericType = typing.TypeVar("GenericType")


class ImBuf:
    channels: int = None
    ''' Number of bit-planes.

    :type: int
    '''

    filepath: str = None
    ''' filepath associated with this image.

    :type: str
    '''

    planes: int = None
    ''' Number of bits associated with this image.

    :type: int
    '''

    ppm: typing.Any = None
    ''' pixels per meter.

    :type: typing.Any
    '''

    size: typing.Any = None
    ''' size of the image in pixels.

    :type: typing.Any
    '''

    def copy(self) -> 'ImBuf':
        ''' 

        :rtype: 'ImBuf'
        :return: A copy of the image.
        '''
        pass

    def crop(self, min: typing.Any, max: typing.Any):
        ''' Crop the image.

        :param min: X, Y minimum.
        :type min: typing.Any
        :param max: X, Y maximum.
        :type max: typing.Any
        '''
        pass

    def free(self):
        ''' Clear image data immediately (causing an error on re-use).

        '''
        pass

    def resize(self, size: typing.Any, method: str = 'FAST'):
        ''' Resize the image.

        :param size: New size.
        :type size: typing.Any
        :param method: Method of resizing ('FAST', 'BILINEAR')
        :type method: str
        '''
        pass
