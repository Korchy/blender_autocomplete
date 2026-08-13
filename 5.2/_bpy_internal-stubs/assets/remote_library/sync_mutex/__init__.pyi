import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def mutex_lock(local_library_path) -> None:
    """Lock the library for syncing.Create a file on disk that signals to other Blender instances that this
    remote asset library is being synced by this Blender.

        :return: true if the lock was created successfully, false if some other
    Blender already locked this library.
    """

def mutex_unlock(local_library_path) -> None:
    """Remove the lock created by mutex_lock(local_library_path)."""
