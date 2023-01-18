import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def abspath(path,
            *,
            start: typing.Union[str, bytes] = None,
            library: typing.Optional['bpy.types.Library'] = None) -> str:
    ''' Returns the absolute path relative to the current blend file using the "//" prefix.

    :param start: Relative to this path, when not set the current filename is used.
    :type start: typing.Union[str, bytes]
    :param library: The library this path is from. This is only included for convenience, when the library is not None its path replaces *start*.
    :type library: typing.Optional['bpy.types.Library']
    :rtype: str
    :return: The absolute path.
    '''

    pass


def basename(path) -> str:
    ''' Equivalent to ``os.path.basename``, but skips a "//" prefix. Use for Windows compatibility.

    :rtype: str
    :return: The base name of the given path.
    '''

    pass


def clean_name(name: typing.Union[str, bytes],
               *,
               replace: typing.Optional[str] = '_') -> str:
    ''' Returns a name with characters replaced that may cause problems under various circumstances, such as writing to a file. All characters besides A-Z/a-z, 0-9 are replaced with "_" or the *replace* argument if defined.

    :param name: The path name.
    :type name: typing.Union[str, bytes]
    :param replace: The replacement for non-valid characters.
    :type replace: typing.Optional[str]
    :rtype: str
    :return: The cleaned name.
    '''

    pass


def display_name(name: typing.Optional[str],
                 *,
                 has_ext: typing.Optional[bool] = True,
                 title_case: typing.Optional[bool] = True) -> str:
    ''' Creates a display string from name to be used menus and the user interface. Intended for use with filenames and module names.

    :param name: The name to be used for displaying the user interface.
    :type name: typing.Optional[str]
    :param has_ext: Remove file extension from name.
    :type has_ext: typing.Optional[bool]
    :param title_case: Convert lowercase names to title case.
    :type title_case: typing.Optional[bool]
    :rtype: str
    :return: The display string.
    '''

    pass


def display_name_from_filepath(name: typing.Optional[str]) -> str:
    ''' Returns the path stripped of directory and extension, ensured to be utf8 compatible.

    :param name: The file path to convert.
    :type name: typing.Optional[str]
    :rtype: str
    :return: The display name.
    '''

    pass


def display_name_to_filepath(name: typing.Optional[str]) -> str:
    ''' Performs the reverse of display_name using literal versions of characters which aren't supported in a filepath.

    :param name: The display name to convert.
    :type name: typing.Optional[str]
    :rtype: str
    :return: The file path.
    '''

    pass


def ensure_ext(filepath: typing.Optional[str],
               ext: typing.Optional[str],
               *,
               case_sensitive: typing.Optional[bool] = False) -> str:
    ''' Return the path with the extension added if it is not already set.

    :param filepath: The file path.
    :type filepath: typing.Optional[str]
    :param ext: The extension to check for, can be a compound extension. Should start with a dot, such as '.blend' or '.tar.gz'.
    :type ext: typing.Optional[str]
    :param case_sensitive: Check for matching case when comparing extensions.
    :type case_sensitive: typing.Optional[bool]
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


def module_names(path: typing.Optional[str],
                 *,
                 recursive: typing.Optional[bool] = False) -> typing.List[str]:
    ''' Return a list of modules which can be imported from *path*.

    :param path: a directory to scan.
    :type path: typing.Optional[str]
    :param recursive: Also return submodule names for packages.
    :type recursive: typing.Optional[bool]
    :rtype: typing.List[str]
    :return: a list of string pairs (module_name, module_file).
    '''

    pass


def native_pathsep(path: typing.Optional[str]) -> str:
    ''' Replace the path separator with the systems native ``os.sep``.

    :param path: The path to replace.
    :type path: typing.Optional[str]
    :rtype: str
    :return: The path with system native separators.
    '''

    pass


def reduce_dirs(dirs: typing.Optional[typing.List[str]]) -> typing.List[str]:
    ''' Given a sequence of directories, remove duplicates and any directories nested in one of the other paths. (Useful for recursive path searching).

    :param dirs: Sequence of directory paths.
    :type dirs: typing.Optional[typing.List[str]]
    :rtype: typing.List[str]
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


def resolve_ncase(path: typing.Optional[str]) -> str:
    ''' Resolve a case insensitive path on a case sensitive system, returning a string with the path if found else return the original path.

    :param path: The path name to resolve.
    :type path: typing.Optional[str]
    :rtype: str
    :return: The resolved path.
    '''

    pass
