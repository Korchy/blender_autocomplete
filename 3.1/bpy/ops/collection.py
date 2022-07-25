import sys
import typing


def create(name: str = "Collection"):
    ''' Create an object collection from selected objects

    :param name: Name, Name of the new collection
    :type name: str
    '''

    pass


def objects_add_active(collection: typing.Union[str, int] = ''):
    ''' Add the object to an object collection that contains the active object

    :param collection: Collection, The collection to add other selected objects to
    :type collection: typing.Union[str, int]
    '''

    pass


def objects_remove(collection: typing.Union[str, int] = ''):
    ''' Remove selected objects from a collection

    :param collection: Collection, The collection to remove this object from
    :type collection: typing.Union[str, int]
    '''

    pass


def objects_remove_active(collection: typing.Union[str, int] = ''):
    ''' Remove the object from an object collection that contains the active object

    :param collection: Collection, The collection to remove other selected objects from
    :type collection: typing.Union[str, int]
    '''

    pass


def objects_remove_all():
    ''' Remove selected objects from all collections

    '''

    pass
