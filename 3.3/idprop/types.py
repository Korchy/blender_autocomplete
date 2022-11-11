import sys
import typing

GenericType = typing.TypeVar("GenericType")


class IDPropertyArray:
    typecode = None
    ''' The type of the data in the array {'f': float, 'd': double, 'i': int}.'''

    def to_list(self):
        ''' Return the array as a list.

        '''
        pass


class IDPropertyGroup:
    name = None
    ''' The name of this Group.'''

    def clear(self):
        ''' Clear all members from this group.

        '''
        pass

    def get(self, key, default=None):
        ''' Return the value for key, if it exists, else default.

        '''
        pass

    def items(self):
        ''' Iterate through the items in the dict; behaves like dictionary method items.

        '''
        pass

    def keys(self):
        ''' Return the keys associated with this group as a list of strings.

        '''
        pass

    def pop(self, key: str, default):
        ''' Remove an item from the group, returning a Python representation. :raises KeyError: When the item doesn't exist.

        :param key: Name of item to remove.
        :type key: str
        :param default: Value to return when key isn't found, otherwise raise an exception.
        :type default: 
        '''
        pass

    def to_dict(self):
        ''' Return a purely python version of the group.

        '''
        pass

    def update(self, other: 'IDPropertyGroup'):
        ''' Update key, values.

        :param other: Updates the values in the group with this.
        :type other: 'IDPropertyGroup'
        '''
        pass

    def values(self):
        ''' Return the values associated with this group.

        '''
        pass


class IDPropertyGroupIterItems:
    pass


class IDPropertyGroupIterKeys:
    pass


class IDPropertyGroupIterValues:
    pass


class IDPropertyGroupViewItems:
    pass


class IDPropertyGroupViewKeys:
    pass


class IDPropertyGroupViewValues:
    pass
