import typing
import collections.abc
import typing_extensions

class InfoFunctionRNA:
    args: typing.Any
    bl_func: typing.Any
    description: typing.Any
    global_lookup: typing.Any
    identifier: typing.Any
    is_classmethod: typing.Any
    return_values: typing.Any

    def build(self): ...

class InfoOperatorRNA:
    args: typing.Any
    bl_op: typing.Any
    description: typing.Any
    func_name: typing.Any
    global_lookup: typing.Any
    identifier: typing.Any
    module_name: typing.Any
    name: typing.Any

    def build(self): ...
    def get_location(self): ...

class InfoPropertyRNA:
    array_dimensions: typing.Any
    array_length: typing.Any
    bl_prop: typing.Any
    collection_type: typing.Any
    default: typing.Any
    default_str: typing.Any
    description: typing.Any
    enum_items: typing.Any
    enum_pointer: typing.Any
    fixed_type: typing.Any
    global_lookup: typing.Any
    identifier: typing.Any
    is_argument_optional: typing.Any
    is_enum_flag: typing.Any
    is_never_none: typing.Any
    is_readonly: typing.Any
    is_required: typing.Any
    max: typing.Any
    min: typing.Any
    name: typing.Any
    srna: typing.Any
    subtype: typing.Any
    type: typing.Any

    def build(self): ...
    def get_arg_default(self, force=True):
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
        collection_id="Collection",
        enum_descr_override: str | None = None,
    ):
        """

                :param as_ret:
                :param as_arg:
                :param class_fmt:
                :param mathutils_fmt:
                :param collection_id:
                :param enum_descr_override: Optionally override items for enum.
        Otherwise expand the literal items.
                :type enum_descr_override: str | None
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

    def build(self): ...
    def get_bases(self): ...
    def get_nested_properties(self, ls=None):
        """

        :param ls:
        """

    def get_py_c_functions(self): ...
    def get_py_c_properties_getset(self): ...
    def get_py_functions(self): ...
    def get_py_properties(self): ...

def BuildRNAInfo(): ...
def GetInfoFunctionRNA(bl_rna, parent_id): ...
def GetInfoOperatorRNA(bl_rna): ...
def GetInfoPropertyRNA(bl_rna, parent_id): ...
def GetInfoStructRNA(bl_rna): ...
def float_as_string(f): ...
def get_direct_functions(rna_type): ...
def get_direct_properties(rna_type): ...
def get_py_class_from_rna(rna_type):
    """Gets the Python type for a class which isn't necessarily added to bpy.types."""

def main(): ...
def range_str(val): ...
def rna_id_ignore(rna_id): ...
