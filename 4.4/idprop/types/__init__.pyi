import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class IDPropertyArray:
    typecode: typing.Any
    """ The type of the data in the array {'f': float, 'd': double, 'i': int, 'b': bool}."""

    def to_list(self) -> None:
        """Return the array as a list."""

class IDPropertyGroup:
    name: typing.Any
    """ The name of this Group."""

    def clear(self) -> None:
        """Clear all members from this group."""

    def get(self, key, default=None) -> None:
        """Return the value for key, if it exists, else default.

        :param key:
        :param default:
        """

    def items(self) -> None:
        """Iterate through the items in the dict; behaves like dictionary method items."""

    def keys(self) -> None:
        """Return the keys associated with this group as a list of strings."""

    def pop(self, key: str, default: typing.Any) -> None:
        """Remove an item from the group, returning a Python representation.

        :param key: Name of item to remove.
        :param default: Value to return when key isnt found, otherwise raise an exception.
        """

    def to_dict(self) -> None:
        """Return a purely Python version of the group."""

    def update(self, other: dict[str, typing.Any] | typing_extensions.Self) -> None:
        """Update key, values.

        :param other: Updates the values in the group with this.
        """

    def values(self) -> None:
        """Return the values associated with this group."""

class IDPropertyGroupIterItems: ...
class IDPropertyGroupIterKeys: ...
class IDPropertyGroupIterValues: ...
class IDPropertyGroupViewItems(collections.abc.Iterable[tuple[str, typing.Any]]): ...
class IDPropertyGroupViewKeys(collections.abc.Iterable[str]): ...
class IDPropertyGroupViewValues(collections.abc.Iterable[typing.Any]): ...
