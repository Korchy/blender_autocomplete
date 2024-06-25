import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def build_property_typemap(skip_classes, skip_typemap): ...
def print_ln(data): ...
def rna2xml(
    fw=None,
    root_node="",
    root_rna=None,
    root_rna_skip=None(),
    root_ident="",
    ident_val="  ",
    skip_classes=None,
    skip_typemap=None,
    pretty_format=True,
    method="DATA",
): ...
def xml2rna(root_xml, root_rna=None): ...
def xml_file_run(context, filepath, rna_map): ...
def xml_file_write(context, filepath, rna_map, skip_typemap=None): ...
