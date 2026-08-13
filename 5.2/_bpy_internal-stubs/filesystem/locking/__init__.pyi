import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class MutexAcquisitionError:
    """Raised when mutex_lock_and_open_with_retry() cannot obtain a lock."""

    args: typing.Any

def mutex_lock_and_open(file_path, mode) -> None:
    """Obtain an exclusive lock on a file.Create a file on disk, and immediately lock it for exclusive use by this
    process.

        :return: If the file was opened & locked successfully, a tuple (file,
    unlocker) is returned. Otherwise returns None. The caller should call
    unlocker(file) to unlock the mutex.
    """

def mutex_lock_and_open_with_retry(
    file_path, mode, *, max_tries, wait_time_sec
) -> None:
    """Obtain an exclusive lock on a file, retrying when that fails.See mutex_lock_and_open() for the lock semantics, and the first two parameters.

        :param max_tries: number of times the code attempts to acquire the lock.
        :return: A tuple (file, unlocker) is returned. The caller should call
    unlocker(file) to unlock the mutex.
    """
