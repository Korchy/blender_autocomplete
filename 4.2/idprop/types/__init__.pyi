import typing
import collections.abc
import typing_extensions

class IDPropertyArray:
    typecode: typing.Any
    """ The type of the data in the array {'f': float, 'd': double, 'i': int, 'b': bool}."""

    def to_list(self):
        """Return the array as a list."""

class IDPropertyGroup:
    name: typing.Any
    """ The name of this Group."""

    def clear(self):
        """Clear all members from this group."""

    def get(self, key, default=None):
        """Return the value for key, if it exists, else default.

        :param key:
        :param default:
        """

    def items(self):
        """Iterate through the items in the dict; behaves like dictionary method items."""

    def keys(self):
        """Return the keys associated with this group as a list of strings."""

    def pop(self, key: str, default):
        """Remove an item from the group, returning a Python representation.

        :param key: Name of item to remove.
        :type key: str
        :param default: Value to return when key isn't found, otherwise raise an exception.
        """

    def to_dict(self):
        """Return a purely Python version of the group."""

    def update(self, other: dict | typing_extensions.Self):
        """Update key, values.

        :param other: Updates the values in the group with this.
        :type other: dict | typing_extensions.Self
        """

    def values(self):
        """Return the values associated with this group."""

class IDPropertyGroupIterItems: ...
class IDPropertyGroupIterKeys: ...
class IDPropertyGroupIterValues: ...
class IDPropertyGroupViewItems: ...
class IDPropertyGroupViewKeys: ...
class IDPropertyGroupViewValues: ...
