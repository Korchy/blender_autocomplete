import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
from . import backend_sqlite as backend_sqlite
from . import hash_service as hash_service
from . import types as types

def get_service(storage_path) -> None:
    """Get a disk file hash service that stores its cache on the given path.Depending on the back-end (currently there is only the SQLite back-end, and
    thus there is no choice in which one is used), the storage_path can be used
    as directory or as file prefix. The SQLite back-end uses
    {storage_path}_v{schema_version}.sqlite as storage.Once a DiskFileHashService is constructed, it is cached for future
    invocations. These cached services are cleaned up when Blender loads another
    file or when it exits.NOTE: DiskFileHashService instances should _NOT_ be used by different
    threads. When this function is used from a thread other than the main
    thread, it MUST use release_service(storage_path) once the work is done.

    """

def on_blender_exit() -> None: ...
def release_service(storage_path) -> None:
    """Close a DiskFileHashService and release its resources.Since DiskFileHashService instances should not be shared across threads,
    when your thread is done with the service, call this function. This is
    mandatory, as thread IDs can be reused; not releasing the service when
    your thread is done with it can cause hard-to-diagnose corruptions when
    the thread ID is reused by another thread.If your DFHS is only ever used from the main thread, it is not mandatory to
    release it, as thatll automatically happen when a new blend file loads or
    when Blender exits.When there is no known service for the given storage path, this is a no-op.

    """
