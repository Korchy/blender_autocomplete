import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types
import mathutils

class ExportHelper:
    def check(self, _context) -> bool:
        """Validate the filepath and axis conversion settings.

        :param _context:
        :return: True when a property was updated.
        """

    def invoke(self, context: bpy.types.Context, _event) -> set[str]:
        """Invoke the file selector for exporting, setting a default filepath
        based on the current blend file name.

                :param context: The context.
                :param _event:
                :return: The operator return value.
        """

class ImportHelper:
    def check(self, _context) -> bool:
        """Validate axis conversion settings.

        :param _context:
        :return: True when a property was updated.
        """

    def invoke(self, context: bpy.types.Context, _event) -> set[str]:
        """Invoke the file selector for importing.

        :param context: The context.
        :param _event:
        :return: The operator return value.
        """

    def invoke_popup(
        self, context: bpy.types.Context, confirm_text: str = ""
    ) -> set[str]:
        """Invoke as a popup confirmation dialog when a filepath is already set,
        otherwise fall back to the file selector.

                :param context: The context.
                :param confirm_text: Label for the confirm button,
        defaults to the operator label.
                :return: The operator return value.
        """

def axis_conversion(
    from_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] = "Y",
    from_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] = "Z",
    to_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] = "Y",
    to_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] = "Z",
) -> mathutils.Matrix:
    """Each argument is an axis
    where the first 2 are a source and the second 2 are the target.

        :param from_forward: Source forward axis.
        :param from_up: Source up axis.
        :param to_forward: Target forward axis.
        :param to_up: Target up axis.
        :return: The conversion matrix.
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
        :param objects: A sequence of objects.
        :return: A dictionary where each key is an object from objects,
    values are lists of (object, matrix) tuples representing instances.
    """

def orientation_helper(
    axis_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] = "Y",
    axis_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] = "Z",
) -> collections.abc.Callable[typing.Any, typing.Any]:
    """A decorator for import/export classes, generating properties needed by the axis conversion system and IO helpers,
    with specified default values (axes).

        :param axis_forward: The default forward axis.
        :param axis_up: The default up axis.
        :return: A class decorator.
    """

def path_reference(
    filepath: str,
    base_src: str,
    base_dst: str,
    mode: typing.Literal[
        "AUTO", "ABSOLUTE", "RELATIVE", "MATCH", "STRIP", "COPY"
    ] = "AUTO",
    copy_subdir: str = "",
    copy_set: None | set[tuple[str, str]] | None = None,
    library: None | bpy.types.Library | None = None,
) -> str:
    """Return a filepath relative to a destination directory, for use with
    exporters.

        :param filepath: the file path to return,
    supporting blenders relative // prefix.
        :param base_src: the directory the filepath is relative to
    (normally the blend file).
        :param base_dst: the directory the filepath will be referenced from
    (normally the export path).
        :param mode: the method used to reference the path.
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

def poll_file_object_drop(context: bpy.types.Context) -> bool:
    """A default implementation for FileHandler poll_drop methods. Allows for both the 3D Viewport and
    the Outliner (in ViewLayer display mode) to be targets for file drag and drop.

        :param context: The context.
        :return: Whether the drop target is valid.
    """

def unique_name(
    key: typing.Any,
    name: str,
    name_dict: dict[typing.Any, str],
    name_max: int = -1,
    clean_func: None | collections.abc.Callable[str, str] | None = None,
    sep: str = ".",
) -> str:
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
        :param name_max: Maximum length of the name. When -1 the name is unlimited.
        :param clean_func: Function to call on name before creating a unique value.
        :param sep: Separator to use when between the name and a number when a
    duplicate name is found.
        :return: A unique name.
    """

def unpack_face_list(
    list_of_tuples: collections.abc.Sequence[tuple[int, ...]],
) -> list[int]:
    """Unpack a list of faces (triangles or quads) into a flat list,
    padding triangles with a zero to fit into groups of four.

        :param list_of_tuples: A sequence of face index tuples (3 or 4 elements each).
        :return: A flat list of face indices, padded with zeros.
    """

def unpack_list(list_of_tuples: collections.abc.Sequence[tuple]) -> list:
    """Flatten a sequence of tuples into a single list.

    :param list_of_tuples: A sequence of tuples to unpack.
    :return: A flat list of all values.
    """
