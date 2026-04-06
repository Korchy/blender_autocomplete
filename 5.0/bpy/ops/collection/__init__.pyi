import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def create(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
) -> None:
    """Create an object collection from selected objects

    :param name: Name, Name of the new collection
    """

def export_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Invoke all configured exporters on this collection"""

def exporter_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
) -> None:
    """Add exporter to the exporter list

    :param name: Name, FileHandler idname
    """

def exporter_export(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
) -> None:
    """Invoke the export operation

    :param index: Index, Exporter index
    """

def exporter_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move exporter up or down in the exporter list

    :param direction: Direction, Direction to move the active exporter
    """

def exporter_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
) -> None:
    """Remove exporter from the exporter list

    :param index: Index, Exporter index
    """

def objects_add_active(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    collection: str | None = "",
) -> None:
    """Add selected objects to one of the collections the active-object is part of. Optionally add to "All Collections" to ensure selected objects are included in the same collections as the active object

    :param collection: Collection, The collection to add other selected objects to
    """

def objects_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    collection: str | None = "",
) -> None:
    """Remove selected objects from a collection

    :param collection: Collection, The collection to remove this object from
    """

def objects_remove_active(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    collection: str | None = "",
) -> None:
    """Remove the object from an object collection that contains the active object

    :param collection: Collection, The collection to remove other selected objects from
    """

def objects_remove_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove selected objects from all collections"""
