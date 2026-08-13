import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class IDPropertyArray:
    """An array of values with a fixed type, supporting indexing and slicing."""

    typecode: typing.Any
    """ The type of the data in the array {'f': float (32-bit), 'd': double (64-bit), 'i': int, 'b': bool}. Both 'f' and 'd' use Python's `float` type but differ in storage precision."""

    def to_list(self) -> list[bool] | list[float] | list[int]:
        """Return the array as a list.

        :return: The array as a list.
        """

class IDPropertyGroup:
    """A dictionary-like group of ID properties, supporting key access, iteration, and membership testing."""

    name: typing.Any
    """ The name of this Group."""

    def clear(self) -> None:
        """Clear all members from this group."""

    def get(self, key: str, default: typing.Any | None = None) -> typing.Any:
        """Return the value for key, if it exists, else default.

        :param key: The key to look up.
        :param default: Value to return if key is not found.
        :return: The value for the key, or default if not found.
        """

    def items(self) -> IDPropertyGroupViewItems:
        """Return a view of the items in the group, behaves like dictionary method items.

        :return: A view of the items.
        """

    def keys(self) -> IDPropertyGroupViewKeys:
        """Return a view of the keys in the group.

        :return: A view of the keys.
        """

    def pop(self, key: str, default: typing.Any) -> typing.Any:
        """Remove an item from the group, returning a Python representation.

        :param key: Name of item to remove.
        :param default: Value to return when key isnt found (optional, a `KeyError` is raised when omitted and the key is not found).
        :return: A Python representation of the removed item, or default.
        """

    def to_dict(self) -> dict[str, typing.Any]:
        """Return a purely Python version of the group.

        :return: A dictionary representation of the group.
        """

    def update(self, other: dict[str, typing.Any] | typing_extensions.Self) -> None:
        """Update key-value pairs from other, overwriting existing keys.

        :param other: Updates the values in the group with this.
        """

    def values(self) -> IDPropertyGroupViewValues:
        """Return the values associated with this group.

        :return: A view of the values.
        """

class IDPropertyGroupIterItems:
    """Iterator over `IDPropertyGroup` items (key/value pairs)."""

class IDPropertyGroupIterKeys:
    """Iterator over `IDPropertyGroup` keys."""

class IDPropertyGroupIterValues:
    """Iterator over `IDPropertyGroup` values."""

class IDPropertyGroupViewItems(collections.abc.Iterable[tuple[str, typing.Any]]):
    """A view of `IDPropertyGroup` items as key/value pairs (supports len(), in, iteration, and reversed())."""

class IDPropertyGroupViewKeys(collections.abc.Iterable[str]):
    """A view of `IDPropertyGroup` keys (supports len(), in, iteration, and reversed())."""

class IDPropertyGroupViewValues(collections.abc.Iterable[typing.Any]):
    """A view of `IDPropertyGroup` values (supports len(), in, iteration, and reversed())."""
