import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class DownloadStatus:
    """Create a collection of name/value pairs.Example enumeration:Access them by:Enumerations can be iterated over, and know how many members they have:Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.
    """

    FAILED: typing.Any
    FINISHED_SUCCESSFULLY: typing.Any
    LOADING: typing.Any
    name: typing.Any
    value: typing.Any

class RemoteAssetListingBackupper:
    def create(self) -> None:
        """Create a backup of the asset librarys current listing.This only creates a backup if none exists already. If there is already
        a backup, that is an indicator that a previous download didnt succeed,
        and so the current files shouldnt be trusted to be correct; better not
        overwrite that already-existing backup with them.

        """

    def erase(self) -> None:
        """Erase the backup of the asset librarys listing, if it exists."""

    def has_backup(self) -> None: ...
    def restore(self) -> None:
        """Restore a backup of the asset librarys listing."""

    def restore_if_exists(self) -> None:
        """Restore a backup of the asset librarys listing, if it exists.If the backup doesnt exist, this is a no-op."""

class RemoteAssetListingDownloader:
    """Download a remote asset listing.Calling downloader.download_and_process() performs the following steps:The above steps always happen, even when the HTTP server returns a 304 Not
    Modified.
    """

    OnDoneCallback: typing.Any
    OnMetafilesDoneCallback: typing.Any
    OnPageDoneCallback: typing.Any
    OnUpdateCallback: typing.Any
    error_message: typing.Any
    local_path: typing.Any
    remote_url: typing.Any
    status: typing.Any

    def already_downloaded(self, http_req_descr, local_file) -> None:
        """

        :param http_req_descr:
        :param local_file:
        """

    def cancel_and_shutdown(self) -> None:
        """Cancel all downloads and shut down the background downloader."""

    def download_and_process(self) -> None:
        """Download and process the remote library index."""

    def download_error(self, http_req_descr, local_file, error) -> None:
        """

        :param http_req_descr:
        :param local_file:
        :param error:
        """

    def download_finished(self, http_req_descr, local_file) -> None:
        """

        :param http_req_descr:
        :param local_file:
        """

    def download_progress(self, http_req_descr, progress) -> None:
        """

        :param http_req_descr:
        :param progress:
        """

    def download_starts(self, http_req_descr) -> None:
        """

        :param http_req_descr:
        """

    def on_asset_page_downloaded(self, http_req_descr, unsafe_local_file) -> None:
        """

        :param http_req_descr:
        :param unsafe_local_file:
        """

    def on_timer_event(self) -> None: ...
    def parse_asset_lib_index(self, http_req_descr, unsafe_local_file) -> None:
        """

        :param http_req_descr:
        :param unsafe_local_file:
        """

    def parse_asset_lib_metadata(self, http_req_descr, unsafe_local_file) -> None:
        """

        :param http_req_descr:
        :param unsafe_local_file:
        """

    def report(self, level, message) -> None:
        """

        :param level:
        :param message:
        """

    def shutdown(self) -> None:
        """Stop the background downloader and call the done callback."""

class RemoteAssetListingLocator:
    """Construct paths for various components of a remote asset library.Basically this determines where assets are downloaded, what their filenames
    will be, and where the HTTP metadata cache is located.
    """

    catalogs_file: typing.Any
    http_metadata_cache_location: typing.Any
    listing_backup_path: typing.Any
    local_path: typing.Any
    remote_url: typing.Any

    def asset_download_path(self, asset_file) -> None:
        """Construct the absolute download path for this asset.This can raise a ValueError if the file path is not suitable (either
        downright invalid, or not ending in .blend).

                :param asset_file:
        """

    def is_system_path(self, some_path) -> None:
        """Return whether the given path is part of the asset system.This includes the asset listing directory structure, but also the SQLite file used to cache file hashes.

        :param some_path:
        """

def is_more_recent_than(library_path, max_age_sec) -> None:
    """Return whether the remote asset library listing is more recent than the given age.If the listing hasnt been downloaded, return False."""

def restore_backup_if_exists_locked(remote_url, local_path) -> None:
    """If there is a listing backup at the given path, restore it.This uses the sync mutex to ensure this only happens when there is no other
    Blender downloading that listing right now.

    """
