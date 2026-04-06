import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types
import mathutils

class ExportHelper:
    def check(self, _context) -> None:
        """

        :param _context:
        """

    def invoke(self, context, _event) -> None:
        """

        :param context:
        :param _event:
        """

class ImportHelper:
    def check(self, _context) -> None:
        """

        :param _context:
        """

    def invoke(self, context, _event) -> None:
        """

        :param context:
        :param _event:
        """

    def invoke_popup(self, context, confirm_text="") -> None:
        """

        :param context:
        :param confirm_text:
        """

def axis_conversion(from_forward="Y", from_up="Z", to_forward="Y", to_up="Z") -> None:
    """Each argument is an axis in [X, Y, Z, -X, -Y, -Z]
    where the first 2 are a source and the second 2 are the target.
    :rtype: `mathutils.Matrix`

    """

def axis_conversion_ensure(
    operator: bpy.types.Operator, forward_attr: str, up_attr: str
) -> bool:
    """Function to ensure an operator has valid axis conversion settings, intended
    to be used from `bpy.types.Operator.check`.

        :param operator: the operator to access axis attributes from.
        :param forward_attr: attribute storing the forward axis
        :param up_attr: attribute storing the up axis
        :return: True if the value was modified.
    """

def create_derived_objects(
    depsgraph: bpy.types.Depsgraph, objects: collections.abc.Sequence[bpy.types.Object]
) -> dict[bpy.types.Object, list[tuple[bpy.types.Object, mathutils.Matrix]]]:
    """This function takes a sequence of objects, returning their instances.

        :param depsgraph: The evaluated depsgraph.
        :param objects: A sequencer of objects.
        :return: A dictionary where each key is an object from objects,
    values are lists of (object, matrix) tuples representing instances.
    """

def orientation_helper(axis_forward="Y", axis_up="Z") -> None:
    """A decorator for import/export classes, generating properties needed by the axis conversion system and IO helpers,
    with specified default values (axes).

    """

def path_reference(
    filepath: str,
    base_src: str,
    base_dst: str,
    mode: str = "AUTO",
    copy_subdir: str = "",
    copy_set: set[tuple[str, str]] | None = None,
    library: None | bpy.types.Library | None = None,
) -> str:
    """Return a filepath relative to a destination directory, for use with
    exporters.

        :param filepath: the file path to return,
    supporting blenders relative // prefix.
        :param base_src: the directory the filepath is relative too
    (normally the blend file).
        :param base_dst: the directory the filepath will be referenced from
    (normally the export path).
        :param mode: the method used get the path in
    [AUTO, ABSOLUTE, RELATIVE, MATCH, STRIP, COPY]
        :param copy_subdir: the subdirectory of base_dst to use when mode=COPY.
        :param copy_set: collect from/to pairs when mode=COPY,
    pass to path_reference_copy when exporting is done.
        :param library: The library this path is relative to.
        :return: the new filepath.
    """

def path_reference_copy(
    copy_set: set[tuple[str, str]], report: collections.abc.Callable[str, None] = print
) -> None:
    """Execute copying files of path_reference

    :param copy_set: set of (from, to) pairs to copy.
    :param report: function used for reporting warnings, takes a string argument.
    """

def poll_file_object_drop(context) -> None:
    """A default implementation for FileHandler poll_drop methods. Allows for both the 3D Viewport and
    the Outliner (in ViewLayer display mode) to be targets for file drag and drop.

    """

def unique_name(
    key: typing.Any,
    name: str,
    name_dict: dict,
    name_max=-1,
    clean_func: typing.Any | None = None,
    sep: str = ".",
) -> None:
    """Helper function for storing unique names which may have special characters
    stripped and restricted to a maximum length.

        :param key: Unique item this name belongs to, name_dict[key] will be reused
    when available.
    This can be the object, mesh, material, etc instance itself.
    Any hashable object associated with the name.
        :param name: The name used to create a unique value in name_dict.
        :param name_dict: This is used to cache namespace to ensure no collisions
    occur, this should be an empty dict initially and only modified by this
    function.
        :param clean_func: Function to call on name before creating a unique value.
        :param sep: Separator to use when between the name and a number when a
    duplicate name is found.
    """

def unpack_face_list(list_of_tuples) -> None: ...
def unpack_list(list_of_tuples) -> None: ...
