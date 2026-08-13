import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class create(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create an object collection from selected objects

        :param execution_context:
        :param undo:
        :param name: Name, Name of the new collection (optional, never None)
        :return: Result of the operator call.
        """

class export_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Invoke all configured exporters on this collection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class exporter_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add exporter to the exporter list

        :param execution_context:
        :param undo:
        :param name: Name, FileHandler idname (optional, never None)
        :return: Result of the operator call.
        """

class exporter_export(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        index: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Invoke the export operation

        :param execution_context:
        :param undo:
        :param index: Index, Exporter index (in [0, inf], optional)
        :return: Result of the operator call.
        """

class exporter_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal["UP", "DOWN"] | None = "UP",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move exporter up or down in the exporter list

        :param execution_context:
        :param undo:
        :param direction: Direction, Direction to move the active exporter (optional)
        :return: Result of the operator call.
        """

class exporter_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        index: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove exporter from the exporter list

        :param execution_context:
        :param undo:
        :param index: Index, Exporter index (in [0, inf], optional)
        :return: Result of the operator call.
        """

class importer_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add Importer

        :param execution_context:
        :param undo:
        :param name: Name, FileHandler idname (optional, never None)
        :return: Result of the operator call.
        """

class importer_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove Importer

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class objects_add_active(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        collection: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add selected objects to one of the collections the active-object is part of. Optionally add to "All Collections" to ensure selected objects are included in the same collections as the active object

        :param execution_context:
        :param undo:
        :param collection: Collection, The collection to add other selected objects to (optional)
        :return: Result of the operator call.
        """

class objects_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        collection: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove selected objects from a collection

        :param execution_context:
        :param undo:
        :param collection: Collection, The collection to remove this object from (optional)
        :return: Result of the operator call.
        """

class objects_remove_active(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        collection: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the object from an object collection that contains the active object

        :param execution_context:
        :param undo:
        :param collection: Collection, The collection to remove other selected objects from (optional)
        :return: Result of the operator call.
        """

class objects_remove_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove selected objects from all collections

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
