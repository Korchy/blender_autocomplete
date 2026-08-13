import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class AssetDownloader:
    """Downloader for asset files & their thumbnails."""

    QueueEmptyCallback: typing.Any
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

    def cancel_download(self, full_asset_url) -> None:
        """Cancel downloading a URL.If the URL was never queued, or it has already been downloaded,
        this is a no-op.

                :param full_asset_url:
        """

    def download_asset_file(self, asset_url, save_to) -> None:
        """Download an asset or preview file to a local file.Returns the URL that was queued. This is different than the given URL
        when the latter is relative.

                :param asset_url:
                :param save_to:
        """

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

    def on_timer_event(self) -> None: ...
    def report(self, level, message) -> None:
        """

        :param level:
        :param message:
        """

    def shutdown(self) -> None:
        """Stop the background downloader and call the done callback."""

    def start(self) -> None:
        """Start the background process."""

class AssetReporter:
    """Implementation of the http_dl.DownloadReporter protocol."""

    def already_downloaded(self, http_req_descr, local_file) -> None:
        """

        :param http_req_descr:
        :param local_file:
        """

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

class DownloadStatus:
    """Create a collection of name/value pairs.Example enumeration:Access them by:Enumerations can be iterated over, and know how many members they have:Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.
    """

    CANCELLED: typing.Any
    DOWNLOADING: typing.Any
    FAILED: typing.Any
    FINISHED: typing.Any
    IDLE: typing.Any
    name: typing.Any
    value: typing.Any

class PreviewReporter:
    """Implementation of the http_dl.DownloadReporter protocol."""

    def already_downloaded(self, http_req_descr, local_file) -> None:
        """

        :param http_req_descr:
        :param local_file:
        """

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

def any_asset_downloading() -> None:
    """Returns true if there is any downloader currently downloading assets."""

def cancel_download(asset_library_url, full_asset_url) -> None:
    """Cancel a running/queued asset download.Cancelling a URL that has already been fully downloaded, or one that was never
    queued is a no-op.

        :param asset_library_url: Root URL of the remote asset library. Used as an
    identifier of this library (to create a downloader per library).
    Contrary to the download function, this is NOT used to resolve relative
    URLs.
        :param full_asset_url: the URL thats queued for download. MUST be the final
    URL as returned by download_asset_file().
    """

def cancel_download_all_assets() -> None:
    """Cancel all active/queued downloads of all assets.This shuts down all asset downloaders, effectively cancelling all their downloads."""

def download_asset_file(
    asset_library_url, asset_library_local_path, asset_url, asset_hash, save_to
) -> None:
    """Download an asset file to a file on disk.

        :param asset_library_url: Root URL of the remote asset library. Used as an
    identifier of this library (to create a downloader per library), as well
    as for resolving relative URLs.
        :param asset_library_local_path: Root path of the local asset cache. Used to
    resolve relative save_to paths, but also to find the HTTP metadata
    cache for this asset library (for conditional downloads).
        :param asset_url: the URL to download. Can be absolute or relative to the
    asset library URL. If it is an empty string, the save_to path is used
    as the URL.
        :param asset_hash: the hash of the asset file, will be appended to the URL.
        :param save_to: the path on disk where to download to. While the download is
    pending, ".part" will be appended to the filename. When the download
    finishes successfully, it is renamed to the final path.
        :return: the final URL that was queued for downloading.
    """

def download_preview(
    asset_library_url, asset_library_local_path, preview_url, preview_hash, dst_filepath
) -> None:
    """Download an asset preview to a file on disk.

        :param asset_library_url: Root URL of the remote asset library. Used as an
    identifier of this library (to create a downloader per library), as well
    as for resolving relative URLs.
        :param asset_library_local_path: Root path of the local asset cache. Used to
    resolve relative save_to paths, but also to find the HTTP metadata
    cache for this asset library (for conditional downloads).
        :param preview_url: the URL to download. Can be absolute or relative.
        :param preview_hash: the hash of the thumbnail, will be appended to the URL.
        :param dst_filepath: the path on disk where to download to. While the
    download is pending, ".part" will be appended to the filename. When the
    download finishes successfully, it is renamed to the final path.
    """

def downloader_status(asset_library_url) -> None:
    """Returns the asset downloader status.Raises a KeyError if there never was a downloader for this URL."""

def on_asset_download_queue_empty() -> None:
    """Called by the asset downloader when its download queue emptied."""
