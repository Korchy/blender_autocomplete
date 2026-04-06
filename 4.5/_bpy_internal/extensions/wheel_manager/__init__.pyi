import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def apply_action(
    *, local_dir, local_dir_site_packages, wheel_list, error_fn, remove_error_fn, debug
) -> None: ...
def wheel_list_deduplicate_as_skip_set(wheel_list) -> None:
    """Return all wheel paths to skip."""

def wheel_version_from_filename_for_cmp(filename) -> None:
    """Extract the version number for comparison.
    Note that this only handled the first 3 numbers,
    the trailing text is compared as a string which is not technically correct
    however this is not a priority to support since scripts should only be including stable releases,
    so comparing the first 3 numbers is sufficient. The trailing string is just a tie breaker in the
    unlikely event it differs.If supporting the full spec, comparing: "1.1.dev6" with "1.1.6rc6" for example
    we could support this doesnt seem especially important as extensions should use major releases.

    """
