import typing
import collections.abc
import typing_extensions

def build_property_typemap(skip_classes, skip_typemap): ...
def print_ln(data): ...
def rna2xml(
    fw=None,
    root_node="",
    root_rna=None,
    root_rna_skip=set(),
    root_ident="",
    ident_val="  ",
    skip_classes=None,
    skip_typemap=None,
    pretty_format=True,
    method="DATA",
): ...
def xml2rna(root_xml, *, root_rna=None, secure_types=None): ...
def xml_file_run(context, filepath, rna_map, secure_types=None): ...
def xml_file_write(context, filepath, rna_map, *, skip_typemap=None): ...
