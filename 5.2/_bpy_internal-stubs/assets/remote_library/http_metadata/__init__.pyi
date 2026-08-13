import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class ExtraFileMetadataProvider:
    """HTTP Metadata provider that can check an extra file.This is to support the following file sets:The downloader will get the request to download to file-unsafe.json.
    However, if file.json is still fresh (i.e. the HTTP metadata for the URL
    is applicable to that file), the downloader should be able to do a
    conditional download (instead of an unconditional one).This is implemented as a wrapper for any other MetadataProvider, rather than
    subclassing a specific one, so that its independent of the underlying
    logic.
    """

    def forget(self, http_req_descr) -> None:
        """

        :param http_req_descr:
        """

    def is_valid(self, meta, http_req_descr, local_path) -> None:
        """Determine whether this metadata is still valid, given the other parameters.

        :param meta:
        :param http_req_descr:
        :param local_path:
        """

    def load(self, http_req_descr) -> None:
        """Return the metadata for the given request.Return None if there is no metadata known for this request. This does
        not check any already-downloaded file on disk and just returns the
        metadata as-is.

                :param http_req_descr:
        """

    def save(self, http_req_descr, meta) -> None:
        """

        :param http_req_descr:
        :param meta:
        """

def safe_to_unsafe_filename(safe_file_path) -> None:
    """path/to/some_file.json -> path/to/some_file.unsafe-json"""

def unsafe_to_safe_filename(unsafe_file_path) -> None:
    """path/to/some_file.unsafe-json -> path/to/some_file.json"""
