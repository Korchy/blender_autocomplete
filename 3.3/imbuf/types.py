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

    ppm = None
    ''' pixels per meter.'''

    size = None
    ''' size of the image in pixels.'''

    def copy(self) -> 'ImBuf':
        ''' 

        :rtype: 'ImBuf'
        :return: A copy of the image.
        '''
        pass

    def crop(self, min, max):
        ''' Crop the image.

        :param min: X, Y minimum.
        :type min: 
        :param max: X, Y maximum.
        :type max: 
        '''
        pass

    def free(self):
        ''' Clear image data immediately (causing an error on re-use).

        '''
        pass

    def resize(self, size, method: str = 'FAST'):
        ''' Resize the image.

        :param size: New size.
        :type size: 
        :param method: Method of resizing ('FAST', 'BILINEAR')
        :type method: str
        '''
        pass
