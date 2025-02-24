import typing
import collections.abc
import typing_extensions

def apply_action(
    *, local_dir, local_dir_site_packages, wheel_list, remove_error_fn, debug
): ...
def wheel_list_deduplicate_as_skip_set(wheel_list):
    """Return all wheel paths to skip."""

def wheel_version_from_filename_for_cmp(filename):
    """Extract the version number for comparison.
    Note that this only handled the first 3 numbers,
    the trailing text is compared as a string which is not technically correct
    however this is not a priority to support since scripts should only be including stable releases,
    so comparing the first 3 numbers is sufficient. The trailing string is just a tie breaker in the
    unlikely event it differs.If supporting the full spec, comparing: "1.1.dev6" with "1.1.6rc6" for e.g.
    we could support this doesn't seem especially important as extensions should use major releases.

    """
