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
    file or when it exits.

    """

def on_blender_exit() -> None: ...
