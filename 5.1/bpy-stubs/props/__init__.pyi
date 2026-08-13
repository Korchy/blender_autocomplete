"""
This module defines properties to extend Blender's internal data. The result of these functions is used to assign properties to classes registered with Blender and can't be used directly.

[NOTE]
All parameters to these functions must be passed as keywords.


--------------------

Custom properties can be added to any subclass of an ID,
Bone and PoseBone.

These properties can be animated, accessed by the user interface and Python
like Blender's existing properties.

[WARNING]
Access to these properties might happen in threaded context, on a per-data-block level.
This has to be carefully considered when using accessors or update callbacks.
Typically, these callbacks should not affect any other data that the one owned by their data-block.
When accessing external non-Blender data, thread safety mechanisms should be considered.

```../examples/bpy.props.0.py```


--------------------

A common use of custom properties is for Python based Operator
classes. Test this code by running it in the text editor, or by clicking the
button in the 3D Viewport's Tools panel. The latter will show the properties
in the Redo panel and allow you to change them.

```../examples/bpy.props.1.py```


--------------------

PropertyGroups can be used for collecting custom settings into one value
to avoid many individual settings mixed in together.

```../examples/bpy.props.2.py```


--------------------

Custom properties can be added to any subclass of an ID,
Bone and PoseBone.

```../examples/bpy.props.3.py```


--------------------

It can be useful to perform an action when a property is changed and can be
used to update other properties or synchronize with external data.

All properties define update functions except for CollectionProperty.

[WARNING]
Remember that these callbacks may be executed in threaded context.

[WARNING]
If the property belongs to an Operator, the update callback's first
parameter will be an OperatorProperties instance, rather than an instance
of the operator itself. This means you can't access other internal functions
of the operator, only its other properties.

```../examples/bpy.props.4.py```


--------------------

Accessor functions can be used for boolean, int, float, string and enum properties.

If get

 or set

 callbacks are defined, the property will not be stored in the ID properties
automatically. Instead, the get

 and set

 functions will be called when the property
is respectively read or written from the API, and are responsible to handle the data storage.

Note that:

* It is illegal to define a set

 callback without a matching get

 one.
* When a get

 callback is defined but no set

 one, the property is read-only.

get_transform

 and set_transform

 can be used when the returned value needs to be modified,
but the default internal storage is still used. They can only transform the value before it is
set or returned, but do not control how/where that data is stored.

[NOTE]
It is possible to define both get

/set

 and get_transform

/set_transform

 callbacks
for the same property. In practice however, this should rarely be needed, as most 'transform'
operation can also happen within a get

/set

 callback.

[WARNING]
Remember that these callbacks may be executed in threaded context.

[WARNING]
Take care when accessing other properties in these callbacks, as it can easily trigger
complex issues, such as infinite loops (if e.g. two properties try to also set the other
property's value in their own set

 callback), or unexpected side effects due to changes
in data, caused e.g. by an update

 callback.

```../examples/bpy.props.5.py```

[NOTE]
Pointer properties do not support storing references to embedded IDs (e.g. bpy.types.Scene.collection, bpy.types.Material.node_tree).
These should exclusively be referenced and accessed through their owner ID (e.g. the scene or material).

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums
import bpy.types

class _PropertyDeferred:
    """Intermediate storage for properties before registration."""

    function: typing.Any
    """ Undocumented, consider contributing."""

    keywords: typing.Any
    """ Undocumented, consider contributing."""

def BoolProperty[_GenericType1: bpy.types.bpy_struct](
    *,
    name: str | None = "",
    description: str | None = "",
    translation_context: str | None = "*",
    default: bool | None = False,
    options: set[bpy.stub_internal.rna_enums.PropertyFlagItems] = {"ANIMATABLE"},
    override: set[bpy.stub_internal.rna_enums.PropertyOverrideFlagItems] = set(),
    tags: set[str] | None = set(),
    subtype: bpy.stub_internal.rna_enums.PropertySubtypeNumberItems = "NONE",
    update: collections.abc.Callable[[_GenericType1, bpy.types.Context], None]
    | None = None,
    get: collections.abc.Callable[[_GenericType1], bool] | None = None,
    set: collections.abc.Callable[[_GenericType1, bool], None] | None = None,
    get_transform: None
    | collections.abc.Callable[[bpy.types.bpy_struct, bool, bool], bool]
    | None = None,
    set_transform: None
    | collections.abc.Callable[[bpy.types.bpy_struct, bool, bool, bool], bool]
    | None = None,
) -> _PropertyDeferred:
    """Returns a new boolean property definition.

        :param name: Name used in the user interface.
        :param description: Text used for the tooltip and api documentation.
        :param translation_context: Text used as context to disambiguate translations.
        :param default: The default value for this property.
        :param options: Enumerator in `rna_enum_property_flag_items`.
        :param override: Enumerator in `rna_enum_property_override_flag_items`.
        :param tags: Enumerator of tags that are defined by parent class.
        :param subtype: Enumerator in `rna_enum_property_subtype_number_items`.
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :param get: Function to be called when this value is read, and the default,
    system-defined storage is not used for this property.
    This function must take 1 value (self) and return the value of the property.

    Defining this callback without a matching set one will make the property read-only (even if READ_ONLY option is not set).
        :param set: Function to be called when this value is written, and the default,
    system-defined storage is not used for this property.
    This function must take 2 values (self, value) and return None.

    Defining this callback without a matching get one is invalid.
        :param get_transform: Function to be called when this value is read,
    if some additional processing must be performed on the stored value.
    This function must take three arguments (self, the stored value,
    and a boolean indicating if the property is currently set),
    and return the final, transformed value of the property.

    The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.
        :param set_transform: Function to be called when this value is written,
    if some additional processing must be performed on the given value before storing it.
    This function must take four arguments (self, the given value to store,
    the currently stored value (raw value, without any get_transform applied to it),
    and a boolean indicating if the property is currently set),
    and return the final, transformed value of the property.

    The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.
        :return: Opaque type used for registration.
    """

def BoolVectorProperty[_GenericType1: bpy.types.bpy_struct](
    *,
    name: str | None = "",
    description: str | None = "",
    translation_context: str | None = "*",
    default: collections.abc.Sequence[bool] | None = (False, False, False),
    options: set[bpy.stub_internal.rna_enums.PropertyFlagItems] = {"ANIMATABLE"},
    override: set[bpy.stub_internal.rna_enums.PropertyOverrideFlagItems] = set(),
    tags: set[str] | None = set(),
    subtype: bpy.stub_internal.rna_enums.PropertySubtypeNumberArrayItems = "NONE",
    size: collections.abc.Sequence[int] | int | None = 3,
    update: collections.abc.Callable[[_GenericType1, bpy.types.Context], None]
    | None = None,
    get: collections.abc.Callable[[_GenericType1], collections.abc.Sequence[bool]]
    | None = None,
    set: collections.abc.Callable[[_GenericType1, collections.abc.Sequence[bool]], None]
    | None = None,
    get_transform: None
    | collections.abc.Callable[
        [bpy.types.bpy_struct, collections.abc.Sequence[bool], bool],
        collections.abc.Sequence[bool],
    ]
    | None = None,
    set_transform: None
    | collections.abc.Callable[
        [
            bpy.types.bpy_struct,
            collections.abc.Sequence[bool],
            collections.abc.Sequence[bool],
            bool,
        ],
        collections.abc.Sequence[bool],
    ]
    | None = None,
) -> _PropertyDeferred:
    """Returns a new vector boolean property definition.

        :param name: Name used in the user interface.
        :param description: Text used for the tooltip and api documentation.
        :param translation_context: Text used as context to disambiguate translations.
        :param default: sequence of booleans the length of size.
        :param options: Enumerator in `rna_enum_property_flag_items`.
        :param override: Enumerator in `rna_enum_property_override_flag_items`.
        :param tags: Enumerator of tags that are defined by parent class.
        :param subtype: Enumerator in `rna_enum_property_subtype_number_array_items`.
        :param size: Vector dimensions in [1, 32]. An int sequence can be used to define multi-dimension arrays.
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :param get: Function to be called when this value is read, and the default,
    system-defined storage is not used for this property.
    This function must take 1 value (self) and return the value of the property.

    Defining this callback without a matching set one will make the property read-only (even if READ_ONLY option is not set).
        :param set: Function to be called when this value is written, and the default,
    system-defined storage is not used for this property.
    This function must take 2 values (self, value) and return None.

    Defining this callback without a matching get one is invalid.
        :param get_transform: Function to be called when this value is read,
    if some additional processing must be performed on the stored value.
    This function must take three arguments (self, the stored value,
    and a boolean indicating if the property is currently set),
    and return the final, transformed value of the property.

    The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.
        :param set_transform: Function to be called when this value is written,
    if some additional processing must be performed on the given value before storing it.
    This function must take four arguments (self, the given value to store,
    the currently stored value (raw value, without any get_transform applied to it),
    and a boolean indicating if the property is currently set),
    and return the final, transformed value of the property.

    The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.
        :return: Opaque type used for registration.
    """

def CollectionProperty(
    *,
    type: type[bpy.types.PropertyGroup] | None,
    name: str | None = "",
    description: str | None = "",
    translation_context: str | None = "*",
    options: set[bpy.stub_internal.rna_enums.PropertyFlagItems] = {"ANIMATABLE"},
    override: set[
        bpy.stub_internal.rna_enums.PropertyOverrideFlagCollectionItems
    ] = set(),
    tags: set[str] | None = set(),
) -> _PropertyDeferred:
    """Returns a new collection property definition.

    :param type: A subclass of a property group.
    :param name: Name used in the user interface.
    :param description: Text used for the tooltip and api documentation.
    :param translation_context: Text used as context to disambiguate translations.
    :param options: Enumerator in `rna_enum_property_flag_items`.
    :param override: Enumerator in `rna_enum_property_override_flag_collection_items`.
    :param tags: Enumerator of tags that are defined by parent class.
    :return: Opaque type used for registration.
    """

def EnumProperty[_GenericType1: bpy.types.bpy_struct](
    *,
    items: collections.abc.Iterable[
        tuple[str, str, str]
        | tuple[str, str, str, int]
        | tuple[str, str, str, str, int]
        | None
    ]
    | collections.abc.Callable[
        [_GenericType1, bpy.types.Context | None],
        collections.abc.Iterable[
            tuple[str, str, str]
            | tuple[str, str, str, int]
            | tuple[str, str, str, str, int]
            | None
        ],
    ],
    name: str | None = "",
    description: str | None = "",
    translation_context: str | None = "*",
    default: None | int | set[str] | str | None = None,
    options: set[bpy.stub_internal.rna_enums.PropertyFlagEnumItems] = {"ANIMATABLE"},
    override: set[bpy.stub_internal.rna_enums.PropertyOverrideFlagItems] = set(),
    tags: set[str] | None = set(),
    update: collections.abc.Callable[[_GenericType1, bpy.types.Context], None]
    | None = None,
    get: collections.abc.Callable[[_GenericType1], int] | None = None,
    set: collections.abc.Callable[[_GenericType1, int], None] | None = None,
    get_transform: None
    | collections.abc.Callable[[bpy.types.bpy_struct, int, bool], int]
    | None = None,
    set_transform: None
    | collections.abc.Callable[[bpy.types.bpy_struct, int, int, bool], int]
    | None = None,
) -> _PropertyDeferred:
    """Returns a new enumerator property definition.

        :param items: sequence of enum items formatted:
    [(identifier, name, description, icon, number), ...].

    The first three elements of the tuples are mandatory.

    identifier

    The identifier is used for Python access.
    An empty identifier means that the item is a separator

    name

    Name for the interface.

    description

    Used for documentation and tooltips.

    icon

    An icon string identifier or integer icon value
    (e.g. returned by `bpy.types.UILayout.icon`)

    number

    Unique value used as the identifier for this item (stored in file data).
    Use when the identifier may need to change. If the ENUM_FLAG option is used,
    the values are bit-masks and should be powers of two.

    When an item only contains 4 items they define (identifier, name, description, number).

    Separators may be added using either None (nameless separator),
    or a regular item tuple with an empty identifier string, in which case the name,
    if non-empty, will be displayed in the UI above the separator line.
    For dynamic values a callback can be passed which returns a list in
    the same format as the static list.
    This function must take 2 arguments (self, context), context may be None.

    There is a known bug with using a callback,
    Python must keep a reference to the strings returned by the callback or Blender
    will misbehave or even crash.
        :param name: Name used in the user interface.
        :param description: Text used for the tooltip and api documentation.
        :param translation_context: Text used as context to disambiguate translations.
        :param default: The default value for this enum, a string from the identifiers used in items, or integer matching an item number.
    If the ENUM_FLAG option is used this must be a set of such string identifiers instead.
    WARNING: Strings cannot be specified for dynamic enums
    (i.e. if a callback function is given as items parameter).
        :param options: Enumerator in `rna_enum_property_flag_enum_items`.
        :param override: Enumerator in `rna_enum_property_override_flag_items`.
        :param tags: Enumerator of tags that are defined by parent class.
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :param get: Function to be called when this value is read, and the default,
    system-defined storage is not used for this property.
    This function must take 1 value (self) and return the value of the property.

    Defining this callback without a matching set one will make the property read-only (even if READ_ONLY option is not set).
        :param set: Function to be called when this value is written, and the default,
    system-defined storage is not used for this property.
    This function must take 2 values (self, value) and return None.

    Defining this callback without a matching get one is invalid.
        :param get_transform: Function to be called when this value is read,
    if some additional processing must be performed on the stored value.
    This function must take three arguments (self, the stored value,
    and a boolean indicating if the property is currently set),
    and return the final, transformed value of the property.

    The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.
        :param set_transform: Function to be called when this value is written,
    if some additional processing must be performed on the given value before storing it.
    This function must take four arguments (self, the given value to store,
    the currently stored value (raw value, without any get_transform applied to it),
    and a boolean indicating if the property is currently set),
    and return the final, transformed value of the property.

    The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.
        :return: Opaque type used for registration.
    """

def FloatProperty[_GenericType1: bpy.types.bpy_struct](
    *,
    name: str | None = "",
    description: str | None = "",
    translation_context: str | None = "*",
    default: float | None = 0.0,
    min: float | None = -3.402823e38,
    max: float | None = 3.402823e38,
    soft_min: float | None = -3.402823e38,
    soft_max: float | None = 3.402823e38,
    step: float | None = 3,
    precision: int | None = 2,
    options: set[bpy.stub_internal.rna_enums.PropertyFlagItems] = {"ANIMATABLE"},
    override: set[bpy.stub_internal.rna_enums.PropertyOverrideFlagItems] = set(),
    tags: set[str] | None = set(),
    subtype: bpy.stub_internal.rna_enums.PropertySubtypeNumberItems = "NONE",
    unit: bpy.stub_internal.rna_enums.PropertyUnitItems = "NONE",
    update: collections.abc.Callable[[_GenericType1, bpy.types.Context], None]
    | None = None,
    get: collections.abc.Callable[[_GenericType1], float] | None = None,
    set: collections.abc.Callable[[_GenericType1, float], None] | None = None,
    get_transform: None
    | collections.abc.Callable[[bpy.types.bpy_struct, float, bool], float]
    | None = None,
    set_transform: None
    | collections.abc.Callable[[bpy.types.bpy_struct, float, float, bool], float]
    | None = None,
) -> _PropertyDeferred:
    """Returns a new float (single precision) property definition.

        :param name: Name used in the user interface.
        :param description: Text used for the tooltip and api documentation.
        :param translation_context: Text used as context to disambiguate translations.
        :param default: The default value for this property.
        :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
        :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
        :param soft_min: Soft minimum (>= min), user wont be able to drag the widget below this value in the UI.
        :param soft_max: Soft maximum (<= max), user wont be able to drag the widget above this value in the UI.
        :param step: Step of increment/decrement in UI, in [1, 100], defaults to 3 (WARNING: actual value is /100).
        :param precision: Maximum number of decimal digits to display, in [0, 6]. Fraction is automatically hidden for exact integer values of fields with unit NONE or TIME (frame count) and step divisible by 100.
        :param options: Enumerator in `rna_enum_property_flag_items`.
        :param override: Enumerator in `rna_enum_property_override_flag_items`.
        :param tags: Enumerator of tags that are defined by parent class.
        :param subtype: Enumerator in `rna_enum_property_subtype_number_items`.
        :param unit: Enumerator in `rna_enum_property_unit_items`.
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :param get: Function to be called when this value is read, and the default,
    system-defined storage is not used for this property.
    This function must take 1 value (self) and return the value of the property.

    Defining this callback without a matching set one will make the property read-only (even if READ_ONLY option is not set).
        :param set: Function to be called when this value is written, and the default,
    system-defined storage is not used for this property.
    This function must take 2 values (self, value) and return None.

    Defining this callback without a matching get one is invalid.
        :param get_transform: Function to be called when this value is read,
    if some additional processing must be performed on the stored value.
    This function must take three arguments (self, the stored value,
    and a boolean indicating if the property is currently set),
    and return the final, transformed value of the property.

    The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.
        :param set_transform: Function to be called when this value is written,
    if some additional processing must be performed on the given value before storing it.
    This function must take four arguments (self, the given value to store,
    the currently stored value (raw value, without any get_transform applied to it),
    and a boolean indicating if the property is currently set),
    and return the final, transformed value of the property.

    The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.
        :return: Opaque type used for registration.
    """

def FloatVectorProperty[_GenericType1: bpy.types.bpy_struct](
    *,
    name: str | None = "",
    description: str | None = "",
    translation_context: str | None = "*",
    default: collections.abc.Sequence[float] | None = (0.0, 0.0, 0.0),
    min: float | None = None,
    max: float | None = sys.float_info.max,
    soft_min: float | None = None,
    soft_max: float | None = sys.float_info.max,
    step: float | None = 3,
    precision: int | None = 2,
    options: set[bpy.stub_internal.rna_enums.PropertyFlagItems] = {"ANIMATABLE"},
    override: set[bpy.stub_internal.rna_enums.PropertyOverrideFlagItems] = set(),
    tags: set[str] | None = set(),
    subtype: bpy.stub_internal.rna_enums.PropertySubtypeNumberArrayItems = "NONE",
    unit: bpy.stub_internal.rna_enums.PropertyUnitItems = "NONE",
    size: collections.abc.Sequence[int] | int | None = 3,
    update: collections.abc.Callable[[_GenericType1, bpy.types.Context], None]
    | None = None,
    get: collections.abc.Callable[[_GenericType1], collections.abc.Sequence[float]]
    | None = None,
    set: collections.abc.Callable[
        [_GenericType1, collections.abc.Sequence[float]], None
    ]
    | None = None,
    get_transform: None
    | collections.abc.Callable[
        [bpy.types.bpy_struct, collections.abc.Sequence[float], bool],
        collections.abc.Sequence[float],
    ]
    | None = None,
    set_transform: None
    | collections.abc.Callable[
        [
            bpy.types.bpy_struct,
            collections.abc.Sequence[float],
            collections.abc.Sequence[float],
            bool,
        ],
        collections.abc.Sequence[float],
    ]
    | None = None,
) -> _PropertyDeferred:
    """Returns a new vector float property definition.

        :param name: Name used in the user interface.
        :param description: Text used for the tooltip and api documentation.
        :param translation_context: Text used as context to disambiguate translations.
        :param default: Sequence of floats the length of size.
        :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
        :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
        :param soft_min: Soft minimum (>= min), user wont be able to drag the widget below this value in the UI.
        :param soft_max: Soft maximum (<= max), user wont be able to drag the widget above this value in the UI.
        :param step: Step of increment/decrement in UI, in [1, 100], defaults to 3 (WARNING: actual value is /100).
        :param precision: Maximum number of decimal digits to display, in [0, 6]. Fraction is automatically hidden for exact integer values of fields with unit NONE or TIME (frame count) and step divisible by 100.
        :param options: Enumerator in `rna_enum_property_flag_items`.
        :param override: Enumerator in `rna_enum_property_override_flag_items`.
        :param tags: Enumerator of tags that are defined by parent class.
        :param subtype: Enumerator in `rna_enum_property_subtype_number_array_items`.
        :param unit: Enumerator in `rna_enum_property_unit_items`.
        :param size: Vector dimensions in [1, 32]. An int sequence can be used to define multi-dimension arrays.
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :param get: Function to be called when this value is read, and the default,
    system-defined storage is not used for this property.
    This function must take 1 value (self) and return the value of the property.

    Defining this callback without a matching set one will make the property read-only (even if READ_ONLY option is not set).
        :param set: Function to be called when this value is written, and the default,
    system-defined storage is not used for this property.
    This function must take 2 values (self, value) and return None.

    Defining this callback without a matching get one is invalid.
        :param get_transform: Function to be called when this value is read,
    if some additional processing must be performed on the stored value.
    This function must take three arguments (self, the stored value,
    and a boolean indicating if the property is currently set),
    and return the final, transformed value of the property.

    The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.
        :param set_transform: Function to be called when this value is written,
    if some additional processing must be performed on the given value before storing it.
    This function must take four arguments (self, the given value to store,
    the currently stored value (raw value, without any get_transform applied to it),
    and a boolean indicating if the property is currently set),
    and return the final, transformed value of the property.

    The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.
        :return: Opaque type used for registration.
    """

def IntProperty[_GenericType1: bpy.types.bpy_struct](
    *,
    name: str | None = "",
    description: str | None = "",
    translation_context: str | None = "*",
    default: int | None = 0,
    min: int | None = None,
    max: int | None = None,
    soft_min: int | None = None,
    soft_max: int | None = None,
    step: int | None = 1,
    options: set[bpy.stub_internal.rna_enums.PropertyFlagItems] = {"ANIMATABLE"},
    override: set[bpy.stub_internal.rna_enums.PropertyOverrideFlagItems] = set(),
    tags: set[str] | None = set(),
    subtype: bpy.stub_internal.rna_enums.PropertySubtypeNumberItems = "NONE",
    update: collections.abc.Callable[[_GenericType1, bpy.types.Context], None]
    | None = None,
    get: collections.abc.Callable[[_GenericType1], int] | None = None,
    set: collections.abc.Callable[[_GenericType1, int], None] | None = None,
    get_transform: None
    | collections.abc.Callable[[bpy.types.bpy_struct, int, bool], int]
    | None = None,
    set_transform: None
    | collections.abc.Callable[[bpy.types.bpy_struct, int, int, bool], int]
    | None = None,
) -> _PropertyDeferred:
    """Returns a new int property definition.

        :param name: Name used in the user interface.
        :param description: Text used for the tooltip and api documentation.
        :param translation_context: Text used as context to disambiguate translations.
        :param default: The default value for this property.
        :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
        :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
        :param soft_min: Soft minimum (>= min), user wont be able to drag the widget below this value in the UI.
        :param soft_max: Soft maximum (<= max), user wont be able to drag the widget above this value in the UI.
        :param step: Step of increment/decrement in UI, in [1, 100], defaults to 1 (WARNING: unused currently!).
        :param options: Enumerator in `rna_enum_property_flag_items`.
        :param override: Enumerator in `rna_enum_property_override_flag_items`.
        :param tags: Enumerator of tags that are defined by parent class.
        :param subtype: Enumerator in `rna_enum_property_subtype_number_items`.
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :param get: Function to be called when this value is read, and the default,
    system-defined storage is not used for this property.
    This function must take 1 value (self) and return the value of the property.

    Defining this callback without a matching set one will make the property read-only (even if READ_ONLY option is not set).
        :param set: Function to be called when this value is written, and the default,
    system-defined storage is not used for this property.
    This function must take 2 values (self, value) and return None.

    Defining this callback without a matching get one is invalid.
        :param get_transform: Function to be called when this value is read,
    if some additional processing must be performed on the stored value.
    This function must take three arguments (self, the stored value,
    and a boolean indicating if the property is currently set),
    and return the final, transformed value of the property.

    The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.
        :param set_transform: Function to be called when this value is written,
    if some additional processing must be performed on the given value before storing it.
    This function must take four arguments (self, the given value to store,
    the currently stored value (raw value, without any get_transform applied to it),
    and a boolean indicating if the property is currently set),
    and return the final, transformed value of the property.

    The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.
        :return: Opaque type used for registration.
    """

def IntVectorProperty[_GenericType1: bpy.types.bpy_struct](
    *,
    name: str | None = "",
    description: str | None = "",
    translation_context: str | None = "*",
    default: collections.abc.Sequence[int] | None = (0, 0, 0),
    min: int | None = None,
    max: int | None = None,
    soft_min: int | None = None,
    soft_max: int | None = None,
    step: int | None = 1,
    options: set[bpy.stub_internal.rna_enums.PropertyFlagItems] = {"ANIMATABLE"},
    override: set[bpy.stub_internal.rna_enums.PropertyOverrideFlagItems] = set(),
    tags: set[str] | None = set(),
    subtype: bpy.stub_internal.rna_enums.PropertySubtypeNumberArrayItems = "NONE",
    size: collections.abc.Sequence[int] | int | None = 3,
    update: collections.abc.Callable[[_GenericType1, bpy.types.Context], None]
    | None = None,
    get: collections.abc.Callable[[_GenericType1], collections.abc.Sequence[int]]
    | None = None,
    set: collections.abc.Callable[[_GenericType1, collections.abc.Sequence[int]], None]
    | None = None,
    get_transform: None
    | collections.abc.Callable[
        [bpy.types.bpy_struct, collections.abc.Sequence[int], bool],
        collections.abc.Sequence[int],
    ]
    | None = None,
    set_transform: None
    | collections.abc.Callable[
        [
            bpy.types.bpy_struct,
            collections.abc.Sequence[int],
            collections.abc.Sequence[int],
            bool,
        ],
        collections.abc.Sequence[int],
    ]
    | None = None,
) -> _PropertyDeferred:
    """Returns a new vector int property definition.

        :param name: Name used in the user interface.
        :param description: Text used for the tooltip and api documentation.
        :param translation_context: Text used as context to disambiguate translations.
        :param default: sequence of ints the length of size.
        :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
        :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
        :param soft_min: Soft minimum (>= min), user wont be able to drag the widget below this value in the UI.
        :param soft_max: Soft maximum (<= max), user wont be able to drag the widget above this value in the UI.
        :param step: Step of increment/decrement in UI, in [1, 100], defaults to 1 (WARNING: unused currently!).
        :param options: Enumerator in `rna_enum_property_flag_items`.
        :param override: Enumerator in `rna_enum_property_override_flag_items`.
        :param tags: Enumerator of tags that are defined by parent class.
        :param subtype: Enumerator in `rna_enum_property_subtype_number_array_items`.
        :param size: Vector dimensions in [1, 32]. An int sequence can be used to define multi-dimension arrays.
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :param get: Function to be called when this value is read, and the default,
    system-defined storage is not used for this property.
    This function must take 1 value (self) and return the value of the property.

    Defining this callback without a matching set one will make the property read-only (even if READ_ONLY option is not set).
        :param set: Function to be called when this value is written, and the default,
    system-defined storage is not used for this property.
    This function must take 2 values (self, value) and return None.

    Defining this callback without a matching get one is invalid.
        :param get_transform: Function to be called when this value is read,
    if some additional processing must be performed on the stored value.
    This function must take three arguments (self, the stored value,
    and a boolean indicating if the property is currently set),
    and return the final, transformed value of the property.

    The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.
        :param set_transform: Function to be called when this value is written,
    if some additional processing must be performed on the given value before storing it.
    This function must take four arguments (self, the given value to store,
    the currently stored value (raw value, without any get_transform applied to it),
    and a boolean indicating if the property is currently set),
    and return the final, transformed value of the property.

    The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.
        :return: Opaque type used for registration.
    """

def PointerProperty[_GenericType1: bpy.types.bpy_struct, _GenericType2: bpy.types.ID](
    *,
    type: type[bpy.types.PropertyGroup | bpy.types.ID] | None,
    name: str | None = "",
    description: str | None = "",
    translation_context: str | None = "*",
    options: set[bpy.stub_internal.rna_enums.PropertyFlagItems] = {"ANIMATABLE"},
    override: set[bpy.stub_internal.rna_enums.PropertyOverrideFlagItems] = set(),
    tags: set[str] | None = set(),
    poll: collections.abc.Callable[[_GenericType1, _GenericType2], bool] | None = None,
    update: collections.abc.Callable[[_GenericType1, bpy.types.Context], None]
    | None = None,
) -> _PropertyDeferred:
    """Returns a new pointer property definition.

        :param type: A subclass of PropertyGroup or ID.
        :param name: Name used in the user interface.
        :param description: Text used for the tooltip and api documentation.
        :param translation_context: Text used as context to disambiguate translations.
        :param options: Enumerator in `rna_enum_property_flag_items`.
        :param override: Enumerator in `rna_enum_property_override_flag_items`.
        :param tags: Enumerator of tags that are defined by parent class.
        :param poll: Function that determines whether an item is valid for this property.
    The function must take 2 values (self, object) and return a boolean.

    The return value will be checked only when assigning an item from the UI, but it is still possible to assign an "invalid" item to the property directly.
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :return: Opaque type used for registration.
    """

def RemoveProperty(*, cls: type[bpy.types.bpy_struct] | None, attr: str | None) -> None:
    """Removes a dynamically defined property.

    :param cls: The class containing the property (must be a positional argument).
    :param attr: Property name (must be passed as a keyword).
    """

def StringProperty[_GenericType1: bpy.types.bpy_struct](
    *,
    name: str | None = "",
    description: str | None = "",
    translation_context: str | None = "*",
    default: str | None = "",
    maxlen: int | None = 0,
    options: set[bpy.stub_internal.rna_enums.PropertyFlagItems] = {"ANIMATABLE"},
    override: set[bpy.stub_internal.rna_enums.PropertyOverrideFlagItems] = set(),
    tags: set[str] | None = set(),
    subtype: bpy.stub_internal.rna_enums.PropertySubtypeStringItems = "NONE",
    update: collections.abc.Callable[[_GenericType1, bpy.types.Context], None]
    | None = None,
    get: collections.abc.Callable[[_GenericType1], str] | None = None,
    set: collections.abc.Callable[[_GenericType1, str], None] | None = None,
    get_transform: None
    | collections.abc.Callable[[bpy.types.bpy_struct, str, bool], str]
    | None = None,
    set_transform: None
    | collections.abc.Callable[[bpy.types.bpy_struct, str, str, bool], str]
    | None = None,
    search: collections.abc.Callable[
        [_GenericType1, bpy.types.Context, str],
        collections.abc.Iterable[str | tuple[str, str]],
    ]
    | None = None,
    search_options: set[str] | None = {"SUGGESTION"},
) -> _PropertyDeferred:
    """Returns a new string property definition.

        :param name: Name used in the user interface.
        :param description: Text used for the tooltip and api documentation.
        :param translation_context: Text used as context to disambiguate translations.
        :param default: initializer string.
        :param maxlen: maximum length of the string.
        :param options: Enumerator in `rna_enum_property_flag_items`.
        :param override: Enumerator in `rna_enum_property_override_flag_items`.
        :param tags: Enumerator of tags that are defined by parent class.
        :param subtype: Enumerator in `rna_enum_property_subtype_string_items`.
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :param get: Function to be called when this value is read, and the default,
    system-defined storage is not used for this property.
    This function must take 1 value (self) and return the value of the property.

    Defining this callback without a matching set one will make the property read-only (even if READ_ONLY option is not set).
        :param set: Function to be called when this value is written, and the default,
    system-defined storage is not used for this property.
    This function must take 2 values (self, value) and return None.

    Defining this callback without a matching get one is invalid.
        :param get_transform: Function to be called when this value is read,
    if some additional processing must be performed on the stored value.
    This function must take three arguments (self, the stored value,
    and a boolean indicating if the property is currently set),
    and return the final, transformed value of the property.

    The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.
        :param set_transform: Function to be called when this value is written,
    if some additional processing must be performed on the given value before storing it.
    This function must take four arguments (self, the given value to store,
    the currently stored value (raw value, without any get_transform applied to it),
    and a boolean indicating if the property is currently set),
    and return the final, transformed value of the property.

    The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.
        :param search: Function to be called to show candidates for this string (shown in the UI).
    This function must take 3 values (self, context, edit_text)
    and return a sequence, iterator or generator where each item must be:

    A single string (representing a candidate to display).

    A tuple-pair of strings, where the first is a candidate and the second
    is additional information about the candidate.
        :param search_options: Set of strings in:

    SORT sorts the resulting items.

    SUGGESTION lets the user enter values not found in search candidates.
    WARNING disabling this flag causes the search callback to run on redraw,
    so only disable this flag if its not likely to cause performance issues.
        :return: Opaque type used for registration.
    """
