import sys
import typing


class GPUOffscreen:
    '''unbind(restore=True) '''

    color_texture: int = None
    '''Color texture. 

    :type: int
    '''

    height: int = None
    '''Texture height. 

    :type: int
    '''

    width: int = None
    '''Texture width. 

    :type: int
    '''
