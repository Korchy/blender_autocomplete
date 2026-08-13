import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class DiskFileHashService:
    def close(self) -> None:
        """Close the service."""

    def file_matches(self, filepath, hash_algorithm, hexhash, size_in_byes) -> None:
        """Check the file on disk, to see if it matches the given properties.

        :param filepath:
        :param hash_algorithm:
        :param hexhash:
        :param size_in_byes:
        """

    def get_hash(self, filepath, hash_algorithm) -> None:
        """Return the hash of a file on disk.

        :param filepath:
        :param hash_algorithm:
        """

    def open(self) -> None:
        """Prepare the service for use."""

    def store_hash(
        self, filepath, hash_algorithm, hash_info, pre_write_callback=None
    ) -> None:
        """Store a pre-computed hash for the given file path.

                :param filepath: the file whose hash should be stored. It does not have
        to exist on disk yet at the moment of calling this function. If the
        file does not exist, a pre_write_callback function should be given
        that ensures the file does exist after it has been called.
                :param hash_algorithm:
                :param hash_info: the files hash, size in bytes, and last-modified
        timestamp. When pre_write_callback is not None, the caller is
        trusted to provide the correct information. Otherwise the file size
        and last-modification timestamp are checked against the file on
        disk. If they mis-match, a ValueError is raised.
                :param pre_write_callback: if given, the function is called after any
        lock on the storage back-end has been obtained, and before it is
        updated. Any exception raised by this callback will abort the
        storage of the hash.

        This callback function can be used to implement the following:

        Download a file to a temp location.

        Compute its hash while downloading.

        After downloading is complete, get the file size & modification time.

        Store the hash.

        In the pre-write callback function, move the file to its final location.

        The Disk File Hashing Service unlocks the back-end.

        This ensures the hash and file on disk are consistent.
        """
