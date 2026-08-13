import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class DiskFileHashBackend:
    """Base class for protocol classes.Protocol classes are defined as:Such classes are primarily used with static type checkers that recognize
    structural subtyping (static duck-typing).For example:See PEP 544 for details. Protocol classes decorated with
    @typing.runtime_checkable act as simple-minded runtime protocols that check
    only the presence of given attributes, ignoring their type signatures.
    Protocol classes can be generic, they are defined as:
    """

    def close(self) -> None:
        """Close the back-end.After calling this, the back-end is not expected to work any more."""

    def fetch_hash(self, filepath, hash_algorithm) -> None:
        """Return the cached hash info of a given file.If no info is cached for this path/algorithm combo, returns None.

        :param filepath:
        :param hash_algorithm:
        """

    def mark_hash_as_fresh(self, filepath, hash_algorithm) -> None:
        """Store that the hash is still considered fresh.See remove_older_than().

        :param filepath:
        :param hash_algorithm:
        """

    def open(self) -> None:
        """Prepare the back-end for use."""

    def remove_older_than(self, *, days) -> None:
        """Remove all hash entries that are older than this many days.When this removes all known hashes for a file, the file entry itself is
        also removed.

                :param days:
        """

    def store_hash(
        self, filepath, hash_algorithm, hash_info, pre_write_callback=None
    ) -> None:
        """Store a pre-computed hash for the given file path.See DiskFileHashService.store_hash() for an explanation of the parameters.

        :param filepath:
        :param hash_algorithm:
        :param hash_info:
        :param pre_write_callback:
        """

class FileHashInfo:
    """FileHashInfo(hexhash: str, file_size_bytes: int, file_stat_mtime: float)"""
