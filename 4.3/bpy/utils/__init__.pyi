"""
This module contains utility functions specific to blender but
not associated with blenders internal data.

bpy.utils.previews.rst
bpy.utils.units.rst

:maxdepth: 1
:caption: Submodules

"""

import typing
import collections.abc
import typing_extensions
import bpy.types

from . import previews as previews
from . import units as units

def app_template_paths(*, path: str | None = None):
    """Returns valid application template paths.

    :param path: Optional subdir.
    :type path: str | None
    :return: App template paths.
    """

def blend_paths(
    absolute: bool = False, packed: bool = False, local: bool = False
) -> list[str]:
    """Returns a list of paths to external files referenced by the loaded .blend file.

    :param absolute: When true the paths returned are made absolute.
    :type absolute: bool
    :param packed: When true skip file paths for packed data.
    :type packed: bool
    :param local: When true skip linked library paths.
    :type local: bool
    :return: path list.
    :rtype: list[str]
    """

def escape_identifier(string: str) -> str:
    """Simple string escaping function used for animation paths.

    :param string: text
    :type string: str
    :return: The escaped string.
    :rtype: str
    """

def execfile(filepath: str, *, mod: None | None = None):
    """Execute a file path as a Python script.

    :param filepath: Path of the script to execute.
    :type filepath: str
    :param mod: Optional cached module, the result of a previous execution.
    :type mod: None | None
    :return: The module which can be passed back in as mod.
    """

def extension_path_user(package: str, *, path: str = "", create: bool = False) -> str:
    """Return a user writable directory associated with an extension.

    :param package: The __package__ of the extension.
    :type package: str
    :param path: Optional subdirectory.
    :type path: str
    :param create: Treat the path as a directory and create it if its not existing.
    :type create: bool
    :return: a path.
    :rtype: str
    """

def flip_name(name: str, strip_digits: bool = False) -> str:
    """Flip a name between left/right sides, useful for
    mirroring bone names.

        :param name: Bone name to flip.
        :type name: str
        :param strip_digits: Whether to remove .### suffix.
        :type strip_digits: bool
        :return: The flipped name.
        :rtype: str
    """

def is_path_builtin(path: str) -> bool:
    """Returns True if the path is one of the built-in paths used by Blender.

    :param path: Path you want to check if it is in the built-in settings directory
    :type path: str
    :rtype: bool
    """

def is_path_extension(path: str) -> bool:
    """Returns True if the path is from an extensions repository.

    :param path: Path to check if it is within an extension repository.
    :type path: str
    :rtype: bool
    """

def keyconfig_init(): ...
def keyconfig_set(filepath, *, report=None): ...
def load_scripts(
    *,
    reload_scripts: bool = False,
    refresh_scripts: bool = False,
    extensions: bool = True,
):
    """Load scripts and run each modules register function.

        :param reload_scripts: Causes all scripts to have their unregister method
    called before loading.
        :type reload_scripts: bool
        :param refresh_scripts: only load scripts which are not already loaded
    as modules.
        :type refresh_scripts: bool
        :param extensions: Loads additional scripts (add-ons & app-templates).
        :type extensions: bool
    """

def load_scripts_extensions(*, reload_scripts: bool = False):
    """Load extensions scripts (add-ons and app-templates)

        :param reload_scripts: Causes all scripts to have their unregister method
    called before loading.
        :type reload_scripts: bool
    """

def make_rna_paths(
    struct_name: str, prop_name: str, enum_name: str
) -> tuple[str, str, str]:
    """Create RNA "paths" from given names.

        :param struct_name: Name of a RNA struct (like e.g. "Scene").
        :type struct_name: str
        :param prop_name: Name of a RNA struct's property.
        :type prop_name: str
        :param enum_name: Name of a RNA enum identifier.
        :type enum_name: str
        :return: A triple of three "RNA paths"
    (most_complete_path, "struct.prop", "struct.prop:'enum'").
    If no enum_name is given, the third element will always be void.
        :rtype: tuple[str, str, str]
    """

def manual_language_code(default="en") -> str:
    """

        :return: The language code used for user manual URL component based on the current language user-preference,
    falling back to the default when unavailable.
        :rtype: str
    """

def manual_map(): ...
def modules_from_path(path: str, loaded_modules) -> list:
    """Load all modules in a path and return them as a list.

        :param path: this path is scanned for scripts and packages.
        :type path: str
        :param loaded_modules: already loaded module names, files matching these
    names will be ignored.
        :return: all loaded modules.
        :rtype: list
    """

def preset_find(name, preset_path, *, display_name=False, ext=".py"): ...
def preset_paths(subdir: str) -> list[str]:
    """Returns a list of paths for a specific preset.

    :param subdir: preset subdirectory (must not be an absolute path).
    :type subdir: str
    :return: Script paths.
    :rtype: list[str]
    """

def refresh_script_paths():
    """Run this after creating new script paths to update sys.path"""

def register_class(cls: typing.Any):
    """Register a subclass of a Blender type class.

        :param cls: Blender type class in:
    `bpy.types.Panel`, `bpy.types.UIList`,
    `bpy.types.Menu`, `bpy.types.Header`,
    `bpy.types.Operator`, `bpy.types.KeyingSetInfo`,
    `bpy.types.RenderEngine`, `bpy.types.AssetShelf`,
    `bpy.types.FileHandler`
        :type cls: typing.Any
    """

def register_classes_factory(classes):
    """Utility function to create register and unregister functions
    which simply registers and unregisters a sequence of classes.

    """

def register_cli_command(id: str, execute: collections.abc.Callable):
    """Register a command, accessible via the (-c / --command) command-line argument.Custom CommandsRegistering commands makes it possible to conveniently expose command line
    functionality via commands passed to (-c / --command).Using Python Argument ParsingThis example shows how the Python argparse module can be used with a custom command.Using argparse is generally recommended as it has many useful utilities and
    generates a --help message for your command.

        :param id: The command identifier (must pass an str.isidentifier check).

    If the id is already registered, a warning is printed and the command is inaccessible to prevent accidents invoking the wrong command.
        :type id: str
        :param execute: Callback, taking a single list of strings and returns an int.
    The arguments are built from all command-line arguments following the command id.
    The return value should be 0 for success, 1 on failure (specific error codes from the os module can also be used).
        :type execute: collections.abc.Callable
        :return: The command handle which can be passed to `unregister_cli_command`.
    """

def register_manual_map(manual_hook): ...
def register_preset_path(path: str) -> bool:
    """Register a preset search path.

        :param path: preset directory (must be an absolute path).

    This path must contain a "presets" subdirectory which will typically contain presets for add-ons.

    You may call bpy.utils.register_preset_path(os.path.dirname(__file__)) from an add-ons __init__.py file.
    When the __init__.py is in the same location as a presets directory.
    For example an operators preset would be located under: presets/operator/{operator.id}/
    where operator.id is the bl_idname of the operator.
        :type path: str
        :return: success
        :rtype: bool
    """

def register_submodule_factory(
    module_name: str, submodule_names: list[str]
) -> tuple[collections.abc.Callable[None], collections.abc.Callable[None]]:
    """Utility function to create register and unregister functions
    which simply load submodules,
    calling their register & unregister functions.

        :param module_name: The module name, typically __name__.
        :type module_name: str
        :param submodule_names: List of submodule names to load and unload.
        :type submodule_names: list[str]
        :return: register and unregister functions.
        :rtype: tuple[collections.abc.Callable[None], collections.abc.Callable[None]]
    """

def register_tool(
    tool_cls: bpy.types.WorkSpaceTool,
    *,
    after: None | collections.abc.Sequence[str] | None = None,
    separator: bool = False,
    group: bool = False,
):
    """Register a tool in the toolbar.

    :param tool_cls: A tool subclass.
    :type tool_cls: bpy.types.WorkSpaceTool
    :param after: Optional identifiers this tool will be added after.
    :type after: None | collections.abc.Sequence[str] | None
    :param separator: When true, add a separator before this tool.
    :type separator: bool
    :param group: When true, add a new nested group of tools.
    :type group: bool
    """

def resource_path(
    type: str, major: int = bpy.app.version[0], minor: str = bpy.app.version[1]
) -> str:
    """Return the base path for storing system files.

    :param type: string in ['USER', 'LOCAL', 'SYSTEM'].
    :type type: str
    :param major: major version, defaults to current.
    :type major: int
    :param minor: minor version, defaults to current.
    :type minor: str
    :return: the resource path (not necessarily existing).
    :rtype: str
    """

def script_path_user():
    """returns the env var and falls back to home dir or None"""

def script_paths(
    *,
    subdir: str | None = None,
    user_pref: bool = True,
    check_all: bool = False,
    use_user: bool = True,
    use_system_environment: bool = True,
) -> list[str]:
    """Returns a list of valid script paths.

    :param subdir: Optional subdir.
    :type subdir: str | None
    :param user_pref: Include the user preference script paths.
    :type user_pref: bool
    :param check_all: Include local, user and system paths rather just the paths Blender uses.
    :type check_all: bool
    :param use_user: Include user paths
    :type use_user: bool
    :param use_system_environment: Include BLENDER_SYSTEM_SCRIPTS variable path
    :type use_system_environment: bool
    :return: script paths.
    :rtype: list[str]
    """

def script_paths_pref():
    """Returns a list of user preference script directories."""

def script_paths_system_environment():
    """Returns a list of system script directories from environment variables."""

def smpte_from_frame(frame: float, *, fps=None, fps_base=None) -> str:
    """Returns an SMPTE formatted string from the frame:
    HH:MM:SS:FF.If fps and fps_base are not given the current scene is used.

        :param frame: frame number.
        :type frame: float
        :return: the frame string.
        :rtype: str
    """

def smpte_from_seconds(time: float, *, fps=None, fps_base=None) -> str:
    """Returns an SMPTE formatted string from the time:
    HH:MM:SS:FF.If fps and fps_base are not given the current scene is used.

        :param time: time in seconds.
        :type time: float
        :return: the frame string.
        :rtype: str
    """

def time_from_frame(frame: float, *, fps=None, fps_base=None):
    """Returns the time from a frame number .If fps and fps_base are not given the current scene is used.

    :param frame: number.
    :type frame: float
    :return: the time in seconds.
    """

def time_to_frame(time: float, *, fps=None, fps_base=None) -> float:
    """Returns a float frame number from a time given in seconds or
    as a datetime.timedelta object.If fps and fps_base are not given the current scene is used.

        :param time: time in seconds.
        :type time: float
        :return: The frame.
        :rtype: float
    """

def unescape_identifier(string: str) -> str:
    """Simple string un-escape function used for animation paths.
    This performs the reverse of `escape_identifier`.

        :param string: text
        :type string: str
        :return: The un-escaped string.
        :rtype: str
    """

def unregister_class(cls: typing.Any):
    """Unload the Python class from blender.

        :param cls: Blender type class,
    see `bpy.utils.register_class` for classes which can
    be registered.
        :type cls: typing.Any
    """

def unregister_cli_command(handle):
    """Unregister a CLI command.

    :param handle: The return value of `register_cli_command`.
    """

def unregister_manual_map(manual_hook): ...
def unregister_preset_path(path: str) -> bool:
    """Unregister a preset search path.

        :param path: preset directory (must be an absolute path).

    This must match the registered path exactly.
        :type path: str
        :return: success
        :rtype: bool
    """

def unregister_tool(tool_cls): ...
def user_resource(resource_type: str, *, path: str = "", create: bool = False) -> str:
    """Return a user resource path (normally from the users home directory).

    :param resource_type: Resource type in ['DATAFILES', 'CONFIG', 'SCRIPTS', 'EXTENSIONS'].
    :type resource_type: str
    :param path: Optional subdirectory.
    :type path: str
    :param create: Treat the path as a directory and create it if its not existing.
    :type create: bool
    :return: a path.
    :rtype: str
    """
