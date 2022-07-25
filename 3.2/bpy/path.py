import sys
import typing
import bpy.types


def abspath(path,
            *,
            start: typing.Union[str, bytes] = None,
            library: 'bpy.types.Library' = None) -> str:
    ''' Returns the absolute path relative to the current blend file using the "//" prefix.

    :param start: Relative to this path, when not set the current filename is used.
    :type start: typing.Union[str, bytes]
    :param library: The library this path is from. This is only included for convenience, when the library is not None its path replaces *start*.
    :type library: 'bpy.types.Library'
    :rtype: str
    :return: The absolute path.
    '''

    pass


def basename(path) -> str:
    ''' Equivalent to os.path.basename , but skips a "//" prefix. Use for Windows compatibility.

    :rtype: str
    :return: The base name of the given path.
    '''

    pass


def clean_name(name: typing.Union[str, bytes], *, replace: str = '_') -> str:
    ''' Returns a name with characters replaced that may cause problems under various circumstances, such as writing to a file. All characters besides A-Z/a-z, 0-9 are replaced with "_" or the *replace* argument if defined.

    :param name: The path name.
    :type name: typing.Union[str, bytes]
    :param replace: The replacement for non-valid characters.
    :type replace: str
    :rtype: str
    :return: The cleaned name.
    '''

    pass


def display_name(name: str, *, has_ext: bool = True,
                 title_case: bool = True) -> str:
    ''' Creates a display string from name to be used menus and the user interface. Intended for use with filenames and module names.

    :param name: The name to be used for displaying the user interface.
    :type name: str
    :param has_ext: Remove file extension from name.
    :type has_ext: bool
    :param title_case: Convert lowercase names to title case.
    :type title_case: bool
    :rtype: str
    :return: The display string.
    '''

    pass


def display_name_from_filepath(name: str) -> str:
    ''' Returns the path stripped of directory and extension, ensured to be utf8 compatible.

    :param name: The file path to convert.
    :type name: str
    :rtype: str
    :return: The display name.
    '''

    pass


def display_name_to_filepath(name: str) -> str:
    ''' Performs the reverse of display_name using literal versions of characters which aren't supported in a filepath.

    :param name: The display name to convert.
    :type name: str
    :rtype: str
    :return: The file path.
    '''

    pass


def ensure_ext(filepath: str, ext: str, *,
               case_sensitive: bool = False) -> str:
    ''' Return the path with the extension added if it is not already set.

    :param filepath: The file path.
    :type filepath: str
    :param ext: The extension to check for, can be a compound extension. Should start with a dot, such as '.blend' or '.tar.gz'.
    :type ext: str
    :param case_sensitive: Check for matching case when comparing extensions.
    :type case_sensitive: bool
    :rtype: str
    :return: The file path with the given extension.
    '''

    pass


def is_subdir(path: typing.Union[str, bytes], directory) -> bool:
    ''' Returns true if *path* in a subdirectory of *directory*. Both paths must be absolute.

    :param path: An absolute path.
    :type path: typing.Union[str, bytes]
    :rtype: bool
    :return: Whether or not the path is a subdirectory.
    '''

    pass


def module_names(path: str, *, recursive: bool = False) -> list:
    ''' Return a list of modules which can be imported from *path*.

    :param path: a directory to scan.
    :type path: str
    :param recursive: Also return submodule names for packages.
    :type recursive: bool
    :rtype: list
    :return: a list of string pairs (module_name, module_file).
    '''

    pass


def native_pathsep(path: str) -> str:
    ''' Replace the path separator with the systems native os.sep .

    :param path: The path to replace.
    :type path: str
    :rtype: str
    :return: The path with system native separators.
    '''

    pass


def reduce_dirs(dirs: list) -> list:
    ''' Given a sequence of directories, remove duplicates and any directories nested in one of the other paths. (Useful for recursive path searching).

    :param dirs: Sequence of directory paths.
    :type dirs: list
    :rtype: list
    :return: A unique list of paths.
    '''

    pass


def relpath(path: typing.Union[str, bytes],
            *,
            start: typing.Union[str, bytes] = None) -> str:
    ''' Returns the path relative to the current blend file using the "//" prefix.

    :param path: An absolute path.
    :type path: typing.Union[str, bytes]
    :param start: Relative to this path, when not set the current filename is used.
    :type start: typing.Union[str, bytes]
    :rtype: str
    :return: The relative path.
    '''

    pass


def resolve_ncase(path: str) -> str:
    ''' Resolve a case insensitive path on a case sensitive system, returning a string with the path if found else return the original path.

    :param path: The path name to resolve.
    :type path: str
    :rtype: str
    :return: The resolved path.
    '''

    pass
