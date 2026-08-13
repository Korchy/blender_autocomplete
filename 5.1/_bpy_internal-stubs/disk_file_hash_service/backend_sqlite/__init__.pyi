import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class SQLiteBackend:
    """DiskFileHashBackend implementation using SQLite as storage engine."""

    db_conn_ro: typing.Any
    db_conn_rw: typing.Any

    def close(self) -> None:
        """Close the database connection."""

    def fetch_hash(self, filepath, hash_algorithm) -> None:
        """Return the cached hash info of a given file.Returns a tuple (hexdigest, file size in bytes, last file mtime).

        :param filepath:
        :param hash_algorithm:
        """

    def mark_hash_as_fresh(self, filepath, hash_algorithm) -> None:
        """Store that the hash is still considered fresh.See remove_older_than().

        :param filepath:
        :param hash_algorithm:
        """

    def open(self) -> None:
        """Prepare the back-end for use.Create the directory structure & database file, and ensure the schema is as expected."""

    def remove_older_than(self, *, days) -> None:
        """Remove all hash entries that are older than this many days.When this removes all known hashes for a file, the file entry itself is
        also removed.

                :param days:
        """

    def store_hash(
        self, filepath, hash_algorithm, hash_info, pre_write_callback=None
    ) -> None:
        """Store a pre-computed hash for the given file path. The path has to exist.

        :param filepath:
        :param hash_algorithm:
        :param hash_info:
        :param pre_write_callback:
        """
