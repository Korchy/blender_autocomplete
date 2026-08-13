import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class add_row_filter_rule(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a filter to remove rows from the displayed data

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class change_spreadsheet_data_source(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        component_type: int | None = 0,
        attribute_domain_type: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change visible data source in the spreadsheet

        :param execution_context:
        :param undo:
        :param component_type: Component Type, (in [0, 32767], optional)
        :param attribute_domain_type: Attribute Domain Type, (in [0, 32767], optional)
        :return: Result of the operator call.
        """

class fit_column(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Resize a spreadsheet column to the width of the data

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class remove_row_filter_rule(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        index: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove a row filter from the rules

        :param execution_context:
        :param undo:
        :param index: Index, (in [0, inf], optional)
        :return: Result of the operator call.
        """

class reorder_columns(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change the order of columns

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class resize_column(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Resize a spreadsheet column

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class toggle_pin(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Turn on or off pinning

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
