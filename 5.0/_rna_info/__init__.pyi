import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class InfoFunctionRNA:
    args: typing.Any
    bl_func: typing.Any
    description: typing.Any
    global_lookup: typing.Any
    identifier: typing.Any
    is_classmethod: typing.Any
    return_values: typing.Any

    def build(self) -> None: ...

class InfoOperatorRNA:
    args: typing.Any
    bl_op: typing.Any
    description: typing.Any
    func_name: typing.Any
    global_lookup: typing.Any
    identifier: typing.Any
    module_name: typing.Any
    name: typing.Any

    def build(self) -> None: ...
    def get_location(self) -> None: ...

class InfoPropertyRNA:
    array_dimensions: typing.Any
    array_length: typing.Any
    bl_prop: typing.Any
    collection_type: typing.Any
    default: typing.Any
    default_str: typing.Any
    deprecated: typing.Any
    description: typing.Any
    enum_items: typing.Any
    enum_pointer: typing.Any
    fixed_type: typing.Any
    global_lookup: typing.Any
    identifier: typing.Any
    is_argument_optional: typing.Any
    is_enum_flag: typing.Any
    is_never_none: typing.Any
    is_path_supports_blend_relative: typing.Any
    is_path_supports_templates: typing.Any
    is_readonly: typing.Any
    is_required: typing.Any
    max: typing.Any
    min: typing.Any
    name: typing.Any
    srna: typing.Any
    subtype: typing.Any
    type: typing.Any

    def build(self) -> None: ...
    def get_arg_default(self, force=True) -> None:
        """

        :param force:
        """

    def get_type_description(
        self,
        *,
        as_ret=False,
        as_arg=False,
        class_fmt="{:s}",
        mathutils_fmt="{:s}",
        literal_fmt="'{:s}'",
        collection_id="Collection",
        enum_descr_override: None | str | None = None,
    ) -> None:
        """

                :param as_ret:
                :param as_arg:
                :param class_fmt:
                :param mathutils_fmt:
                :param literal_fmt:
                :param collection_id:
                :param enum_descr_override: Optionally override items for enum.
        Otherwise expand the literal items.
        """

class InfoStructRNA:
    base: typing.Any
    bl_rna: typing.Any
    children: typing.Any
    description: typing.Any
    full_path: typing.Any
    functions: typing.Any
    global_lookup: typing.Any
    identifier: typing.Any
    module_name: typing.Any
    name: typing.Any
    nested: typing.Any
    properties: typing.Any
    py_class: typing.Any
    references: typing.Any

    def build(self) -> None: ...
    def get_bases(self) -> None: ...
    def get_nested_properties(self, ls=None) -> None:
        """

        :param ls:
        """

    def get_py_c_functions(self) -> None: ...
    def get_py_c_properties_getset(self) -> None: ...
    def get_py_functions(self) -> None: ...
    def get_py_properties(self) -> None: ...

def BuildRNAInfo() -> None: ...
def GetInfoFunctionRNA(bl_rna, parent_id) -> None: ...
def GetInfoOperatorRNA(bl_rna) -> None: ...
def GetInfoPropertyRNA(bl_rna, parent_id) -> None: ...
def GetInfoStructRNA(bl_rna) -> None: ...
def float_as_string(f) -> None: ...
def get_direct_functions(rna_type) -> None: ...
def get_direct_properties(rna_type) -> None: ...
def get_py_class_from_rna(rna_type) -> None:
    """Gets the Python type for a class which isnt necessarily added to bpy.types."""

def main() -> None: ...
def range_str(val) -> None: ...
def rna_id_ignore(rna_id) -> None: ...
