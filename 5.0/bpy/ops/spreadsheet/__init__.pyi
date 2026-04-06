import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def add_row_filter_rule(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a filter to remove rows from the displayed data"""

def change_spreadsheet_data_source(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    component_type: int | None = 0,
    attribute_domain_type: int | None = 0,
) -> None:
    """Change visible data source in the spreadsheet

    :param component_type: Component Type
    :param attribute_domain_type: Attribute Domain Type
    """

def fit_column(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Resize a spreadsheet column to the width of the data"""

def remove_row_filter_rule(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
) -> None:
    """Remove a row filter from the rules

    :param index: Index
    """

def reorder_columns(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Change the order of columns"""

def resize_column(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Resize a spreadsheet column"""

def toggle_pin(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Turn on or off pinning"""
