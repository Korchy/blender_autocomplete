import typing
import collections.abc
import typing_extensions

class AttributeGetterSetter:
    """Helper class to get and set attributes at an index for a domain."""

class SliceHelper:
    """Helper class to handle custom slicing."""

class GreasePencilStroke(AttributeGetterSetter):
    """A helper class to get access to stroke data."""

    aspect_ratio: typing.Any
    curve_type: typing.Any
    cyclic: typing.Any
    end_cap: typing.Any
    fill_color: typing.Any
    fill_opacity: typing.Any
    material_index: typing.Any
    points: typing.Any
    select: typing.Any
    softness: typing.Any
    start_cap: typing.Any
    time_start: typing.Any

    def add_points(self, count):
        """Add new points at the end of the stroke and returns the new points as a list.

        :param count:
        """

    def remove_points(self, count):
        """Remove points at the end of the stroke.

        :param count:
        """

class GreasePencilStrokePoint(AttributeGetterSetter):
    """A helper class to get access to stroke point data."""

    delta_time: typing.Any
    opacity: typing.Any
    position: typing.Any
    radius: typing.Any
    rotation: typing.Any
    select: typing.Any
    vertex_color: typing.Any

class GreasePencilStrokePointSlice(SliceHelper):
    """A helper class that represents a slice of GreasePencilStrokePoint's."""

class GreasePencilStrokeSlice(SliceHelper):
    """A helper class that represents a slice of GreasePencilStroke's."""

def DefAttributeGetterSetters(attributes_list):
    """A class decorator that reads a list of attribute information &
    creates properties on the class with getters & setters.

    """

def def_prop_for_attribute(attr_name, type, default, doc):
    """Creates a property that can read and write an attribute."""
