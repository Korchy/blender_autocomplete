import typing
import collections.abc
import typing_extensions

def add(execution_context: int | str | None = None, undo: bool | None = None):
    """Add new cache

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def bake(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    bake: bool | None = False,
):
    """Bake physics

    :type execution_context: int | str | None
    :type undo: bool | None
    :param bake: Bake
    :type bake: bool | None
    """

def bake_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    bake: bool | None = True,
):
    """Bake all physics

    :type execution_context: int | str | None
    :type undo: bool | None
    :param bake: Bake
    :type bake: bool | None
    """

def bake_from_cache(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Bake from cache

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def free_bake(execution_context: int | str | None = None, undo: bool | None = None):
    """Delete physics bake

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def free_bake_all(execution_context: int | str | None = None, undo: bool | None = None):
    """Delete all baked caches of all objects in the current scene

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def remove(execution_context: int | str | None = None, undo: bool | None = None):
    """Delete current cache

    :type execution_context: int | str | None
    :type undo: bool | None
    """
