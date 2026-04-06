"""
This module has a similar scope to os.path, containing utility
functions for dealing with paths in Blender.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

def abspath(
    path, *, start: bytes | str | None = None, library: bpy.types.Library | None = None
) -> str:
    """Returns the absolute path relative to the current blend file
    using the "//" prefix.

        :param start: Relative to this path,
    when not set the current filename is used.
        :param library: The library this path is from. This is only included for
    convenience, when the library is not None its path replaces start.
        :return: The absolute path.
    """

def basename(path) -> str:
    """Equivalent to os.path.basename, but skips a "//" prefix.Use for Windows compatibility.

    :return: The base name of the given path.
    """

def clean_name(name: bytes | str, *, replace: str = "_") -> str:
    """Returns a name with characters replaced that
    may cause problems under various circumstances,
    such as writing to a file.All characters besides A-Z/a-z, 0-9 are replaced with "_"
    or the replace argument if defined.

        :param name: The path name.
        :param replace: The replacement for non-valid characters.
        :return: The cleaned name.
    """

def display_name(name: str, *, has_ext: bool = True, title_case: bool = True) -> str:
    """Creates a display string from name to be used menus and the user interface.
    Intended for use with filenames and module names.

        :param name: The name to be used for displaying the user interface.
        :param has_ext: Remove file extension from name.
        :param title_case: Convert lowercase names to title case.
        :return: The display string.
    """

def display_name_from_filepath(name: str) -> str:
    """Returns the path stripped of directory and extension,
    ensured to be utf8 compatible.

        :param name: The file path to convert.
        :return: The display name.
    """

def display_name_to_filepath(name: str) -> str:
    """Performs the reverse of display_name using literal versions of characters
    which arent supported in a filepath.

        :param name: The display name to convert.
        :return: The file path.
    """

def ensure_ext(filepath: str, ext: str, *, case_sensitive: bool = False) -> str:
    """Return the path with the extension added if it is not already set.

        :param filepath: The file path.
        :param ext: The extension to check for, can be a compound extension. Should
    start with a dot, such as .blend or .tar.gz.
        :param case_sensitive: Check for matching case when comparing extensions.
        :return: The file path with the given extension.
    """

def is_subdir(path: bytes | str, directory) -> bool:
    """Returns true if path in a subdirectory of directory.
    Both paths must be absolute.

        :param path: An absolute path.
        :return: Whether or not the path is a subdirectory.
    """

def module_names(
    path: str, *, recursive: bool = False, package: str = ""
) -> list[tuple[str, str]]:
    """Return a list of modules which can be imported from path.

    :param path: a directory to scan.
    :param recursive: Also return submodule names for packages.
    :param package: Optional string, used as the prefix for module names (without the trailing ".").
    :return: a list of string pairs (module_name, module_file).
    """

def native_pathsep(path: str) -> str:
    """Replace the path separator with the systems native os.sep.

    :param path: The path to replace.
    :return: The path with system native separators.
    """

def reduce_dirs(dirs: collections.abc.Sequence[str]) -> list[str]:
    """Given a sequence of directories, remove duplicates and
    any directories nested in one of the other paths.
    (Useful for recursive path searching).

        :param dirs: Sequence of directory paths.
        :return: A unique list of paths.
    """

def relpath(path: bytes | str, *, start: bytes | str | None = None) -> str:
    """Returns the path relative to the current blend file using the "//" prefix.

        :param path: An absolute path.
        :param start: Relative to this path,
    when not set the current filename is used.
        :return: The relative path.
    """

def resolve_ncase(path: str) -> str:
    """Resolve a case insensitive path on a case sensitive system,
    returning a string with the path if found else return the original path.

        :param path: The path name to resolve.
        :return: The resolved path.
    """
