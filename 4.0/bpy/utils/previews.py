import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


class ImagePreviewCollection:
    ''' Dictionary-like class of previews. This is a subclass of Python's built-in dict type, used to store multiple image previews.
    '''

    def clear(self):
        ''' Clear all previews.

        '''
        pass

    def close(self):
        ''' Close the collection and clear all previews.

        '''
        pass

    def load(self,
             name: typing.Optional[str],
             filepath: typing.Optional[typing.Union[str, bytes]],
             filetype: typing.Optional[str],
             force_reload: typing.Optional[bool] = False
             ) -> 'bpy.types.ImagePreview':
        ''' Generate a new preview from given file path. :raises KeyError: if ``name`` already exists.

        :param name: The name (unique id) identifying the preview.
        :type name: typing.Optional[str]
        :param filepath: The file path to generate the preview from.
        :type filepath: typing.Optional[typing.Union[str, bytes]]
        :param filetype: The type of file, needed to generate the preview in ['IMAGE', 'MOVIE', 'BLEND', 'FONT'].
        :type filetype: typing.Optional[str]
        :param force_reload: If True, force running thumbnail manager even if preview already exists in cache.
        :type force_reload: typing.Optional[bool]
        :rtype: 'bpy.types.ImagePreview'
        :return: The Preview matching given name, or a new empty one.
        '''
        pass

    def new(self, name: typing.Optional[str]) -> 'bpy.types.ImagePreview':
        ''' Generate a new empty preview. :raises KeyError: if ``name`` already exists.

        :param name: The name (unique id) identifying the preview.
        :type name: typing.Optional[str]
        :rtype: 'bpy.types.ImagePreview'
        :return: The Preview matching given name, or a new empty one.
        '''
        pass


def new() -> 'ImagePreviewCollection':
    ''' 

    :rtype: 'ImagePreviewCollection'
    :return: a new preview collection.
    '''

    pass


def remove(pcoll: typing.Optional['ImagePreviewCollection']):
    ''' Remove the specified previews collection.

    :param pcoll: Preview collection to close.
    :type pcoll: typing.Optional['ImagePreviewCollection']
    '''

    pass
