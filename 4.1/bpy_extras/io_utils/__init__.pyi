import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class ExportHelper:
    check_extension: typing.Any

    def check(self, _context):
        """

        :param _context:
        """
        ...

    def invoke(self, context, _event):
        """

        :param context:
        :param _event:
        """
        ...

class ImportHelper:
    def check(self, _context):
        """

        :param _context:
        """
        ...

    def invoke(self, context, _event):
        """

        :param context:
        :param _event:
        """
        ...

def axis_conversion(from_forward="Y", from_up="Z", to_forward="Y", to_up="Z"):
    """Each argument us an axis in ['X', 'Y', 'Z', '-X', '-Y', '-Z']
    where the first 2 are a source and the second 2 are the target.

    """

    ...

def axis_conversion(from_forward="Y", from_up="Z", to_forward="Y", to_up="Z"):
    """Each argument us an axis in ['X', 'Y', 'Z', '-X', '-Y', '-Z']
    where the first 2 are a source and the second 2 are the target.

    """

    ...

def axis_conversion_ensure(
    operator: bpy.types.Operator, forward_attr: str, up_attr: str
) -> bool:
    """Function to ensure an operator has valid axis conversion settings, intended
    to be used from `bpy.types.Operator.check`.

        :param operator: the operator to access axis attributes from.
        :type operator: bpy.types.Operator
        :param forward_attr: attribute storing the forward axis
        :type forward_attr: str
        :param up_attr: attribute storing the up axis
        :type up_attr: str
        :return: True if the value was modified.
        :rtype: bool
    """

    ...

def axis_conversion_ensure(
    operator: bpy.types.Operator, forward_attr: str, up_attr: str
) -> bool:
    """Function to ensure an operator has valid axis conversion settings, intended
    to be used from `bpy.types.Operator.check`.

        :param operator: the operator to access axis attributes from.
        :type operator: bpy.types.Operator
        :param forward_attr: attribute storing the forward axis
        :type forward_attr: str
        :param up_attr: attribute storing the up axis
        :type up_attr: str
        :return: True if the value was modified.
        :rtype: bool
    """

    ...

def create_derived_objects(
    depsgraph: bpy.types.Depsgraph, objects: list[bpy.types.Object]
) -> dict:
    """This function takes a sequence of objects, returning their instances.

        :param depsgraph: The evaluated depsgraph.
        :type depsgraph: bpy.types.Depsgraph
        :param objects: A sequencer of objects.
        :type objects: list[bpy.types.Object]
        :return: A dictionary where each key is an object from objects,
    values are lists of (`bpy.types.Object`, `mathutils.Matrix`) tuples representing instances.
        :rtype: dict
    """

    ...

def create_derived_objects(
    depsgraph: bpy.types.Depsgraph, objects: list[bpy.types.Object]
) -> dict:
    """This function takes a sequence of objects, returning their instances.

        :param depsgraph: The evaluated depsgraph.
        :type depsgraph: bpy.types.Depsgraph
        :param objects: A sequencer of objects.
        :type objects: list[bpy.types.Object]
        :return: A dictionary where each key is an object from objects,
    values are lists of (`bpy.types.Object`, `mathutils.Matrix`) tuples representing instances.
        :rtype: dict
    """

    ...

def orientation_helper(axis_forward="Y", axis_up="Z"):
    """A decorator for import/export classes, generating properties needed by the axis conversion system and IO helpers,
    with specified default values (axes).

    """

    ...

def orientation_helper(axis_forward="Y", axis_up="Z"):
    """A decorator for import/export classes, generating properties needed by the axis conversion system and IO helpers,
    with specified default values (axes).

    """

    ...

def path_reference(
    filepath: str,
    base_src: str,
    base_dst: str,
    mode: str = "AUTO",
    copy_subdir: str = "",
    copy_set: set = None,
    library: bpy.types.Library | None = None,
) -> str:
    """Return a filepath relative to a destination directory, for use with
    exporters.

        :param filepath: the file path to return,
    supporting blenders relative '//' prefix.
        :type filepath: str
        :param base_src: the directory the filepath is relative too
    (normally the blend file).
        :type base_src: str
        :param base_dst: the directory the filepath will be referenced from
    (normally the export path).
        :type base_dst: str
        :param mode: the method used get the path in
    ['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP', 'COPY']
        :type mode: str
        :param copy_subdir: the subdirectory of base_dst to use when mode='COPY'.
        :type copy_subdir: str
        :param copy_set: collect from/to pairs when mode='COPY',
    pass to path_reference_copy when exporting is done.
        :type copy_set: set
        :param library: The library this path is relative to.
        :type library: bpy.types.Library | None
        :return: the new filepath.
        :rtype: str
    """

    ...

def path_reference(
    filepath: str,
    base_src: str,
    base_dst: str,
    mode: str = "AUTO",
    copy_subdir: str = "",
    copy_set: set = None,
    library: bpy.types.Library | None = None,
) -> str:
    """Return a filepath relative to a destination directory, for use with
    exporters.

        :param filepath: the file path to return,
    supporting blenders relative '//' prefix.
        :type filepath: str
        :param base_src: the directory the filepath is relative too
    (normally the blend file).
        :type base_src: str
        :param base_dst: the directory the filepath will be referenced from
    (normally the export path).
        :type base_dst: str
        :param mode: the method used get the path in
    ['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP', 'COPY']
        :type mode: str
        :param copy_subdir: the subdirectory of base_dst to use when mode='COPY'.
        :type copy_subdir: str
        :param copy_set: collect from/to pairs when mode='COPY',
    pass to path_reference_copy when exporting is done.
        :type copy_set: set
        :param library: The library this path is relative to.
        :type library: bpy.types.Library | None
        :return: the new filepath.
        :rtype: str
    """

    ...

def path_reference_copy(copy_set: set, report: typing.Any = None):
    """Execute copying files of path_reference

    :param copy_set: set of (from, to) pairs to copy.
    :type copy_set: set
    :param report: function used for reporting warnings, takes a string argument.
    :type report: typing.Any
    """

    ...

def path_reference_copy(copy_set: set, report: typing.Any = None):
    """Execute copying files of path_reference

    :param copy_set: set of (from, to) pairs to copy.
    :type copy_set: set
    :param report: function used for reporting warnings, takes a string argument.
    :type report: typing.Any
    """

    ...

def unique_name(
    key,
    name: str,
    name_dict: dict,
    name_max=-1,
    clean_func: typing.Any = None,
    sep: str = ".",
):
    """Helper function for storing unique names which may have special characters
    stripped and restricted to a maximum length.

        :param key: unique item this name belongs to, name_dict[key] will be reused
    when available.
    This can be the object, mesh, material, etc instance itself.
        :param name: The name used to create a unique value in name_dict.
        :type name: str
        :param name_dict: This is used to cache namespace to ensure no collisions
    occur, this should be an empty dict initially and only modified by this
    function.
        :type name_dict: dict
        :param clean_func: Function to call on name before creating a unique value.
        :type clean_func: typing.Any
        :param sep: Separator to use when between the name and a number when a
    duplicate name is found.
        :type sep: str
    """

    ...

def unique_name(
    key,
    name: str,
    name_dict: dict,
    name_max=-1,
    clean_func: typing.Any = None,
    sep: str = ".",
):
    """Helper function for storing unique names which may have special characters
    stripped and restricted to a maximum length.

        :param key: unique item this name belongs to, name_dict[key] will be reused
    when available.
    This can be the object, mesh, material, etc instance itself.
        :param name: The name used to create a unique value in name_dict.
        :type name: str
        :param name_dict: This is used to cache namespace to ensure no collisions
    occur, this should be an empty dict initially and only modified by this
    function.
        :type name_dict: dict
        :param clean_func: Function to call on name before creating a unique value.
        :type clean_func: typing.Any
        :param sep: Separator to use when between the name and a number when a
    duplicate name is found.
        :type sep: str
    """

    ...

def unpack_face_list(list_of_tuples): ...
def unpack_face_list(list_of_tuples): ...
def unpack_list(list_of_tuples): ...
def unpack_list(list_of_tuples): ...
