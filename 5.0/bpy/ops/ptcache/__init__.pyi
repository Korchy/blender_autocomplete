import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add new cache"""

def bake(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    bake: bool | None = False,
) -> None:
    """Bake physics

    :param bake: Bake
    """

def bake_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    bake: bool | None = True,
) -> None:
    """Bake all physics

    :param bake: Bake
    """

def bake_from_cache(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Bake from cache"""

def free_bake(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete physics bake"""

def free_bake_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete all baked caches of all objects in the current scene"""

def remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete current cache"""
