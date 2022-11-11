import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def BoolProperty(name: str = "",
                 description: str = "",
                 default=False,
                 options: typing.Set = {'ANIMATABLE'},
                 override: typing.Set = 'set()',
                 tags: typing.Set = 'set()',
                 subtype: str = 'NONE',
                 update=None,
                 get=None,
                 set=None) -> 'bpy.types.BoolProperty':
    ''' Returns a new boolean property definition.

    :param name: Name used in the user interface.
    :type name: str
    :param description: Text used for the tooltip and api documentation.
    :type description: str
    :param options: rna_enum_property_flag_items .
    :type options: typing.Set
    :param override: rna_enum_property_override_flag_items .
    :type override: typing.Set
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Set
    :param subtype: rna_enum_property_subtype_number_items .
    :type subtype: str
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :param get: Function to be called when this value is 'read', This function must take 1 value (self) and return the value of the property.
    :param set: Function to be called when this value is 'written', This function must take 2 values (self, value) and return None.
    :rtype: 'bpy.types.BoolProperty'
    '''

    pass


def BoolVectorProperty(
        name: str = "",
        description: str = "",
        default: typing.List = (False, False, False),
        options: typing.Set = {'ANIMATABLE'},
        override: typing.Set = 'set()',
        tags: typing.Set = 'set()',
        subtype: str = 'NONE',
        size: typing.List[int] = 3,
        update=None,
        get=None,
        set=None) -> typing.Union[typing.List, 'bpy.types.BoolProperty']:
    ''' Returns a new vector boolean property definition.

    :param name: Name used in the user interface.
    :type name: str
    :param description: Text used for the tooltip and api documentation.
    :type description: str
    :param default: sequence of booleans the length of *size*.
    :type default: typing.List
    :param options: rna_enum_property_flag_items .
    :type options: typing.Set
    :param override: rna_enum_property_override_flag_items .
    :type override: typing.Set
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Set
    :param subtype: rna_enum_property_subtype_number_array_items .
    :type subtype: str
    :param size: Vector dimensions in [1, 32]. An int sequence can be used to define multi-dimension arrays.
    :type size: typing.List[int]
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :param get: Function to be called when this value is 'read', This function must take 1 value (self) and return the value of the property.
    :param set: Function to be called when this value is 'written', This function must take 2 values (self, value) and return None.
    :rtype: typing.Union[typing.List, 'bpy.types.BoolProperty']
    '''

    pass


def CollectionProperty(
        type=None,
        name: str = "",
        description: str = "",
        options: typing.Set = {'ANIMATABLE'},
        override: typing.Set = 'set()',
        tags: typing.Set = 'set()') -> 'bpy.types.CollectionProperty':
    ''' Returns a new collection property definition.

    :param type: bpy.types.PropertyGroup .
    :param name: Name used in the user interface.
    :type name: str
    :param description: Text used for the tooltip and api documentation.
    :type description: str
    :param options: rna_enum_property_flag_items .
    :type options: typing.Set
    :param override: rna_enum_property_override_flag_collection_items .
    :type override: typing.Set
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Set
    :rtype: 'bpy.types.CollectionProperty'
    '''

    pass


def EnumProperty(items: typing.Union[int, str, typing.Set[str]],
                 name: str = "",
                 description: str = "",
                 default: str = None,
                 options: typing.Set = {'ANIMATABLE'},
                 override: typing.Set = 'set()',
                 tags: typing.Set = 'set()',
                 update=None,
                 get=None,
                 set=None) -> 'bpy.types.EnumProperty':
    ''' Returns a new enumerator property definition.

    :param items: [(identifier, name, description, icon, number), ...] . The first three elements of the tuples are mandatory. :identifier: The identifier is used for Python access. :name: Name for the interface. :description: Used for documentation and tooltips. :icon: An icon string identifier or integer icon value (e.g. returned by bpy.types.UILayout.icon ) :number: Unique value used as the identifier for this item (stored in file data). Use when the identifier may need to change. If the *ENUM_FLAG* option is used, the values are bit-masks and should be powers of two. When an item only contains 4 items they define (identifier, name, description, number) . Separators may be added using None instead of a tuple. For dynamic values a callback can be passed which returns a list in the same format as the static list. This function must take 2 arguments (self, context) , **context may be None**. .. warning:: There is a known bug with using a callback, Python must keep a reference to the strings returned by the callback or Blender will misbehave or even crash.
    :type items: typing.Union[int, str, typing.Set[str]]
    :param name: Name used in the user interface.
    :type name: str
    :param description: Text used for the tooltip and api documentation.
    :type description: str
    :param default: The default value for this enum, a string from the identifiers used in *items*, or integer matching an item number. If the *ENUM_FLAG* option is used this must be a set of such string identifiers instead. WARNING: Strings can not be specified for dynamic enums (i.e. if a callback function is given as *items* parameter).
    :type default: str
    :param options: rna_enum_property_flag_enum_items .
    :type options: typing.Set
    :param override: rna_enum_property_override_flag_items .
    :type override: typing.Set
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Set
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :param get: Function to be called when this value is 'read', This function must take 1 value (self) and return the value of the property.
    :param set: Function to be called when this value is 'written', This function must take 2 values (self, value) and return None.
    :rtype: 'bpy.types.EnumProperty'
    '''

    pass


def FloatProperty(name: str = "",
                  description: str = "",
                  default=0.0,
                  min: float = -3.402823e+38,
                  max: float = 3.402823e+38,
                  soft_min: float = -3.402823e+38,
                  soft_max: float = 3.402823e+38,
                  step: int = 3,
                  precision: int = 2,
                  options: typing.Set = {'ANIMATABLE'},
                  override: typing.Set = 'set()',
                  tags: typing.Set = 'set()',
                  subtype: str = 'NONE',
                  unit: str = 'NONE',
                  update=None,
                  get=None,
                  set=None) -> 'bpy.types.FloatProperty':
    ''' Returns a new float (single precision) property definition.

    :param name: Name used in the user interface.
    :type name: str
    :param description: Text used for the tooltip and api documentation.
    :type description: str
    :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
    :type min: float
    :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
    :type max: float
    :param soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
    :type soft_min: float
    :param soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
    :type soft_max: float
    :param step: actual value is /100).
    :type step: int
    :param precision: Maximum number of decimal digits to display, in [0, 6]. Fraction is automatically hidden for exact integer values of fields with unit 'NONE' or 'TIME' (frame count) and step divisible by 100.
    :type precision: int
    :param options: rna_enum_property_flag_items .
    :type options: typing.Set
    :param override: rna_enum_property_override_flag_items .
    :type override: typing.Set
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Set
    :param subtype: rna_enum_property_subtype_number_items .
    :type subtype: str
    :param unit: rna_enum_property_unit_items .
    :type unit: str
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :param get: Function to be called when this value is 'read', This function must take 1 value (self) and return the value of the property.
    :param set: Function to be called when this value is 'written', This function must take 2 values (self, value) and return None.
    :rtype: 'bpy.types.FloatProperty'
    '''

    pass


def FloatVectorProperty(
        name: str = "",
        description: str = "",
        default: typing.List = (0.0, 0.0, 0.0),
        min: float = 'sys.float_info.min',
        max: float = 'sys.float_info.max',
        soft_min: float = 'sys.float_info.min',
        soft_max: float = 'sys.float_info.max',
        step: int = 3,
        precision: int = 2,
        options: typing.Set = {'ANIMATABLE'},
        override: typing.Set = 'set()',
        tags: typing.Set = 'set()',
        subtype: str = 'NONE',
        unit: str = 'NONE',
        size: typing.List[int] = 3,
        update=None,
        get=None,
        set=None) -> typing.Union[typing.List, 'bpy.types.FloatProperty']:
    ''' Returns a new vector float property definition.

    :param name: Name used in the user interface.
    :type name: str
    :param description: Text used for the tooltip and api documentation.
    :type description: str
    :param default: sequence of floats the length of *size*.
    :type default: typing.List
    :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
    :type min: float
    :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
    :type max: float
    :param soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
    :type soft_min: float
    :param soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
    :type soft_max: float
    :param options: rna_enum_property_flag_items .
    :type options: typing.Set
    :param override: rna_enum_property_override_flag_items .
    :type override: typing.Set
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Set
    :param step: actual value is /100).
    :type step: int
    :param precision: Maximum number of decimal digits to display, in [0, 6]. Fraction is automatically hidden for exact integer values of fields with unit 'NONE' or 'TIME' (frame count) and step divisible by 100.
    :type precision: int
    :param subtype: rna_enum_property_subtype_number_array_items .
    :type subtype: str
    :param unit: rna_enum_property_unit_items .
    :type unit: str
    :param size: Vector dimensions in [1, 32]. An int sequence can be used to define multi-dimension arrays.
    :type size: typing.List[int]
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :param get: Function to be called when this value is 'read', This function must take 1 value (self) and return the value of the property.
    :param set: Function to be called when this value is 'written', This function must take 2 values (self, value) and return None.
    :rtype: typing.Union[typing.List, 'bpy.types.FloatProperty']
    '''

    pass


def IntProperty(name: str = "",
                description: str = "",
                default=0,
                min: int = -2**31,
                max: int = 2**31 - 1,
                soft_min: int = -2**31,
                soft_max: int = 2**31 - 1,
                step: int = 1,
                options: typing.Set = {'ANIMATABLE'},
                override: typing.Set = 'set()',
                tags: typing.Set = 'set()',
                subtype: str = 'NONE',
                update=None,
                get=None,
                set=None) -> 'bpy.types.IntProperty':
    ''' Returns a new int property definition.

    :param name: Name used in the user interface.
    :type name: str
    :param description: Text used for the tooltip and api documentation.
    :type description: str
    :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
    :type min: int
    :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
    :type max: int
    :param soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
    :type soft_min: int
    :param soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
    :type soft_max: int
    :param step: unused currently!).
    :type step: int
    :param options: rna_enum_property_flag_items .
    :type options: typing.Set
    :param override: rna_enum_property_override_flag_items .
    :type override: typing.Set
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Set
    :param subtype: rna_enum_property_subtype_number_items .
    :type subtype: str
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :param get: Function to be called when this value is 'read', This function must take 1 value (self) and return the value of the property.
    :param set: Function to be called when this value is 'written', This function must take 2 values (self, value) and return None.
    :rtype: 'bpy.types.IntProperty'
    '''

    pass


def IntVectorProperty(
        name: str = "",
        description: str = "",
        default: typing.List = (0, 0, 0),
        min: int = -2**31,
        max: int = 2**31 - 1,
        soft_min: int = -2**31,
        soft_max: int = 2**31 - 1,
        step: int = 1,
        options: typing.Set = {'ANIMATABLE'},
        override: typing.Set = 'set()',
        tags: typing.Set = 'set()',
        subtype: str = 'NONE',
        size: typing.List[int] = 3,
        update=None,
        get=None,
        set=None) -> typing.Union[typing.List, 'bpy.types.IntProperty']:
    ''' Returns a new vector int property definition.

    :param name: Name used in the user interface.
    :type name: str
    :param description: Text used for the tooltip and api documentation.
    :type description: str
    :param default: sequence of ints the length of *size*.
    :type default: typing.List
    :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
    :type min: int
    :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
    :type max: int
    :param soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
    :type soft_min: int
    :param soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
    :type soft_max: int
    :param step: unused currently!).
    :type step: int
    :param options: rna_enum_property_flag_items .
    :type options: typing.Set
    :param override: rna_enum_property_override_flag_items .
    :type override: typing.Set
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Set
    :param subtype: rna_enum_property_subtype_number_array_items .
    :type subtype: str
    :param size: Vector dimensions in [1, 32]. An int sequence can be used to define multi-dimension arrays.
    :type size: typing.List[int]
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :param get: Function to be called when this value is 'read', This function must take 1 value (self) and return the value of the property.
    :param set: Function to be called when this value is 'written', This function must take 2 values (self, value) and return None.
    :rtype: typing.Union[typing.List, 'bpy.types.IntProperty']
    '''

    pass


def PointerProperty(type=None,
                    name: str = "",
                    description: str = "",
                    options: typing.Set = {'ANIMATABLE'},
                    override: typing.Set = 'set()',
                    tags: typing.Set = 'set()',
                    poll=None,
                    update=None) -> 'bpy.types.PointerProperty':
    ''' Returns a new pointer property definition.

    :param type: bpy.types.ID .
    :param name: Name used in the user interface.
    :type name: str
    :param description: Text used for the tooltip and api documentation.
    :type description: str
    :param options: rna_enum_property_flag_items .
    :type options: typing.Set
    :param override: rna_enum_property_override_flag_items .
    :type override: typing.Set
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Set
    :param poll: function to be called to determine whether an item is valid for this property. The function must take 2 values (self, object) and return Bool.
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :rtype: 'bpy.types.PointerProperty'
    '''

    pass


def RemoveProperty(cls, attr: str):
    ''' Removes a dynamically defined property.

    :param cls: The class containing the property (must be a positional argument).
    :param attr: Property name (must be passed as a keyword).
    :type attr: str
    '''

    pass


def StringProperty(name: str = "",
                   description: str = "",
                   default: str = "",
                   maxlen: int = 0,
                   options: typing.Set = {'ANIMATABLE'},
                   override: typing.Set = 'set()',
                   tags: typing.Set = 'set()',
                   subtype: str = 'NONE',
                   update=None,
                   get=None,
                   set=None,
                   search=None,
                   search_options: typing.Set = {'SUGGESTION'}
                   ) -> 'bpy.types.StringProperty':
    ''' Returns a new string property definition.

    :param name: Name used in the user interface.
    :type name: str
    :param description: Text used for the tooltip and api documentation.
    :type description: str
    :param default: initializer string.
    :type default: str
    :param maxlen: maximum length of the string.
    :type maxlen: int
    :param options: rna_enum_property_flag_items .
    :type options: typing.Set
    :param override: rna_enum_property_override_flag_items .
    :type override: typing.Set
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Set
    :param subtype: rna_enum_property_subtype_string_items .
    :type subtype: str
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :param get: Function to be called when this value is 'read', This function must take 1 value (self) and return the value of the property.
    :param set: Function to be called when this value is 'written', This function must take 2 values (self, value) and return None.
    :param search: Function to be called to show candidates for this string (shown in the UI). This function must take 3 values (self, context, edit_text) and return a sequence, iterator or generator where each item must be: - A single string (representing a candidate to display). - A tuple-pair of strings, where the first is a candidate and the second is additional information about the candidate.
    :param search_options: - 'SORT' sorts the resulting items. - 'SUGGESTION' lets the user enter values not found in search candidates. **WARNING** disabling this flag causes the search callback to run on redraw, so only disable this flag if it's not likely to cause performance issues.
    :type search_options: typing.Set
    :rtype: 'bpy.types.StringProperty'
    '''

    pass
