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
import numpy.typing as npt
import bpy.types

from . import previews as previews
from . import units as units

def app_template_paths(*, path: None | str | None = None) -> None:
    """Returns valid application template paths.

    :param path: Optional subdir.
    :return: App template paths.
    """

def blend_paths(
    *, absolute: bool = False, packed: bool = False, local: bool = False
) -> list[str]:
    """Returns a list of paths to external files referenced by the loaded .blend file.

    :param absolute: When true the paths returned are made absolute.
    :param packed: When true include file paths for packed data.
    :param local: When true skip linked library paths.
    :return: path list.
    """

def escape_identifier(string: str) -> str:
    """Simple string escaping function used for animation paths.

    :param string: text
    :return: The escaped string.
    """

def execfile(filepath: str, *, mod: None | None = None) -> None:
    """Execute a file path as a Python script.

    :param filepath: Path of the script to execute.
    :param mod: Optional cached module, the result of a previous execution.
    :return: The module which can be passed back in as mod.
    """

def expose_bundled_modules() -> None:
    """For Blender as a Python module, add bundled VFX library python bindings
    to sys.path. These may be used instead of dedicated packages, to ensure
    the libraries are compatible with Blender.

    """

def extension_path_user(package: str, *, path: str = "", create: bool = False) -> str:
    """Return a user writable directory associated with an extension.

    :param package: The __package__ of the extension.
    :param path: Optional subdirectory.
    :param create: Treat the path as a directory and create it if its not existing.
    :return: a path.
    """

def flip_name(name: str, *, strip_digits: bool = False) -> str:
    """Flip a name between left/right sides, useful for
    mirroring bone names.

        :param name: Bone name to flip.
        :param strip_digits: Whether to remove .### suffix.
        :return: The flipped name.
    """

def is_path_builtin(path: str) -> bool:
    """Returns True if the path is one of the built-in paths used by Blender.

    :param path: Path you want to check if it is in the built-in settings directory
    """

def is_path_extension(path: str) -> bool:
    """Returns True if the path is from an extensions repository.

    :param path: Path to check if it is within an extension repository.
    """

def keyconfig_init() -> None:
    """Initialize and refresh key configurations, called from the Blender
    window manager on startup and refresh.

    """

def keyconfig_set(
    filepath: str,
    *,
    report: None | collections.abc.Callable[[set[str], str], None] | None = None,
) -> None:
    """Load and activate a key configuration from a file.

    :param filepath: The file path to the key configuration preset.
    :param report: An optional callable for reporting errors.
    """

def load_scripts(
    *,
    reload_scripts: bool = False,
    refresh_scripts: bool = False,
    extensions: bool = True,
) -> None:
    """Load scripts and run each modules register function.

        :param reload_scripts: Causes all scripts to have their unregister method
    called before loading.
        :param refresh_scripts: only load scripts which are not already loaded
    as modules.
        :param extensions: Loads additional scripts (add-ons & app-templates).
    """

def load_scripts_extensions(*, reload_scripts: bool = False) -> None:
    """Load extensions scripts (add-ons and app-templates)

        :param reload_scripts: Causes all scripts to have their unregister method
    called before loading.
    """

def make_rna_paths(
    struct_name: str, prop_name: str, enum_name: str
) -> tuple[str, str, str]:
    """Create RNA "paths" from given names.

        :param struct_name: Name of a RNA struct (like e.g. "Scene").
        :param prop_name: Name of a RNA structs property.
        :param enum_name: Name of a RNA enum identifier.
        :return: A triple of three "RNA paths"
    (most_complete_path, "struct.prop", "struct.prop:enum").
    If no enum_name is given, the third element will always be empty.
    """

def manual_language_code(default: str = "en") -> str:
    """

        :param default: The fallback language code to use when the current language is unavailable.
        :return: The language code used for user manual URL component based on the current language user-preference,
    falling back to the default when unavailable.
    """

def manual_map() -> None:
    """Yield manual URL mappings from all registered hooks.

    :return: An iterator of (prefix, mapping) pairs.
    """

def modules_from_path(path: str, loaded_modules: set[str]) -> list:
    """Load all modules in a path and return them as a list.

        :param path: this path is scanned for scripts and packages.
        :param loaded_modules: already loaded module names, files matching these
    names will be ignored.
        :return: all loaded modules.
    """

def preset_find(
    name: str, preset_path: str, *, display_name: bool = False, ext: str = ".py"
) -> None | str:
    """Search for a preset by name.

    :param name: The preset name.
    :param preset_path: The preset subdirectory (e.g. "keyconfig").
    :param display_name: When True, search by display name instead of filename.
    :param ext: The file extension for the preset.
    :return: The file path of the preset or None if not found.
    """

def preset_paths(subdir: str) -> list[str]:
    """Returns a list of paths for a specific preset.

    :param subdir: preset subdirectory (must not be an absolute path).
    :return: Script paths.
    """

def refresh_script_paths() -> None:
    """Run this after creating new script paths to update sys.path"""

def register_class(
    cls: type[
        bpy.types.Panel
        | bpy.types.UIList
        | bpy.types.Menu
        | bpy.types.Header
        | bpy.types.Operator
        | bpy.types.KeyingSetInfo
        | bpy.types.RenderEngine
        | bpy.types.AssetShelf
        | bpy.types.FileHandler
        | bpy.types.PropertyGroup
        | bpy.types.AddonPreferences
        | bpy.types.NodeTree
        | bpy.types.Node
        | bpy.types.NodeSocket
        | bpy.types.Gizmo
        | bpy.types.GizmoGroup
    ],
) -> None:
    """Register a subclass of a Blender type class.

    :param cls: Registerable Blender class type.
    """

def register_classes_factory(
    classes: collections.abc.Sequence[typing.Any],
) -> tuple[collections.abc.Callable[None], collections.abc.Callable[None]]:
    """Utility function to create register and unregister functions
    which simply registers and unregisters a sequence of classes.

        :param classes: Sequence of classes to register and unregister.
        :return: register and unregister functions.
    """

def register_cli_command(
    id: str, execute: collections.abc.Callable[[list[str]], int]
) -> typing.Any:
    """Register a command, accessible via the (-c / --command) command-line argument.Custom CommandsRegistering commands makes it possible to conveniently expose command line
    functionality via commands passed to (-c / --command).Using Python Argument ParsingThis example shows how the Python argparse module can be used with a custom command.Using argparse is generally recommended as it has many useful utilities and
    generates a --help message for your command.

        :param id: The command identifier (must pass an str.isidentifier check).

    If the id is already registered, a warning is printed and the command is inaccessible to prevent accidents invoking the wrong command.
        :param execute: Callback, taking a single list of strings and returns an int.
    The arguments are built from all command-line arguments following the command id.
    The return value should be 0 for success, 1 on failure (specific error codes from the os module can also be used).
        :return: The command handle which can be passed to `unregister_cli_command`.

    This uses Pythons capsule type however the result should be considered an opaque handle only used for unregistering.
    """

def register_manual_map(
    manual_hook: collections.abc.Callable[tuple[str, list[tuple[str, str]]]],
) -> None:
    """Register a function to provide manual URL mappings.

        :param manual_hook: A callable that returns (prefix, mapping)
    where mapping is a sequence of (pattern, url) pairs.
    """

def register_preset_path(path: str) -> bool:
    """Register a preset search path.

        :param path: preset directory (must be an absolute path).

    This path must contain a "presets" subdirectory which will typically contain presets for add-ons.

    You may call bpy.utils.register_preset_path(os.path.dirname(__file__)) from an add-ons __init__.py file.
    When the __init__.py is in the same location as a presets directory.
    For example an operators preset would be located under: presets/operator/{operator.id}/
    where operator.id is the bl_idname of the operator.
        :return: success
    """

def register_submodule_factory(
    module_name: str, submodule_names: list[str]
) -> tuple[collections.abc.Callable[None], collections.abc.Callable[None]]:
    """Utility function to create register and unregister functions
    which simply load submodules,
    calling their register & unregister functions.

        :param module_name: The module name, typically __name__.
        :param submodule_names: List of submodule names to load and unload.
        :return: register and unregister functions.
    """

def register_tool(
    tool_cls: type[bpy.types.WorkSpaceTool],
    *,
    after: None | collections.abc.Sequence[str] | set[str] | None = None,
    separator: bool = False,
    group: bool = False,
) -> None:
    """Register a tool in the toolbar.

    :param tool_cls: A tool subclass.
    :param after: Optional identifiers this tool will be added after.
    :param separator: When true, add a separator before this tool.
    :param group: When true, add a new nested group of tools.
    """

def resource_path(
    type: typing.Literal["USER", "LOCAL", "SYSTEM"],
    *,
    major: int = bpy.app.version[0],
    minor: int = bpy.app.version[1],
) -> str:
    """Return the base path for storing system files.

    :param type: The resource type.
    :param major: major version, defaults to current.
    :param minor: minor version, defaults to current.
    :return: the resource path (not necessarily existing).
    """

def script_path_user() -> None | str:
    """Return the user script path or None.

    :return: The user script path, or None if not found.
    """

def script_paths(
    *,
    subdir: None | str | None = None,
    user_pref: bool = True,
    check_all: bool = False,
    use_user: bool = True,
    use_system_environment: bool = True,
) -> list[str]:
    """Returns a list of valid script paths.

    :param subdir: Optional subdir.
    :param user_pref: Include the user preference script paths.
    :param check_all: Include local, user and system paths rather just the paths Blender uses.
    :param use_user: Include user paths
    :param use_system_environment: Include BLENDER_SYSTEM_SCRIPTS variable path
    :return: script paths.
    """

def script_paths_pref() -> None:
    """Returns a list of user preference script directories."""

def script_paths_system_environment() -> None:
    """Returns a list of system script directories from environment variables."""

def smpte_from_frame(
    frame: float,
    *,
    fps: None | float | None = None,
    fps_base: None | float | None = None,
) -> str:
    """Returns an SMPTE formatted string from the frame:
    HH:MM:SS:FF.If fps and fps_base are not given the current scene is used.

        :param frame: frame number.
        :param fps: Frames per second, if not given the current scene is used.
        :param fps_base: Frames per second base, if not given the current scene is used.
        :return: the frame string.
    """

def smpte_from_seconds(
    time: float,
    *,
    fps: None | float | None = None,
    fps_base: None | float | None = None,
) -> str:
    """Returns an SMPTE formatted string from the time:
    HH:MM:SS:FF.If fps and fps_base are not given the current scene is used.

        :param time: time in seconds.
        :param fps: Frames per second, if not given the current scene is used.
        :param fps_base: Frames per second base, if not given the current scene is used.
        :return: the frame string.
    """

def time_from_frame(
    frame: float,
    *,
    fps: None | float | None = None,
    fps_base: None | float | None = None,
) -> None:
    """Returns the time from a frame number.If fps and fps_base are not given the current scene is used.

    :param frame: number.
    :param fps: Frames per second, if not given the current scene is used.
    :param fps_base: Frames per second base, if not given the current scene is used.
    :return: the time in seconds.
    """

def time_to_frame(time: float, *, fps=None, fps_base=None) -> float:
    """Returns a float frame number from a time given in seconds or
    as a datetime.timedelta object.If fps and fps_base are not given the current scene is used.

        :param time: time in seconds.
        :return: The frame.
    """

def unescape_identifier(string: str) -> str:
    """Simple string un-escape function used for animation paths.
    This performs the reverse of `escape_identifier`.

        :param string: text
        :return: The un-escaped string.
    """

def unregister_class(
    cls: type[
        bpy.types.Panel
        | bpy.types.UIList
        | bpy.types.Menu
        | bpy.types.Header
        | bpy.types.Operator
        | bpy.types.KeyingSetInfo
        | bpy.types.RenderEngine
        | bpy.types.AssetShelf
        | bpy.types.FileHandler
        | bpy.types.PropertyGroup
        | bpy.types.AddonPreferences
        | bpy.types.NodeTree
        | bpy.types.Node
        | bpy.types.NodeSocket
        | bpy.types.Gizmo
        | bpy.types.GizmoGroup
    ],
) -> None:
    """Unload the Python class from blender.

        :param cls: Blender type class,
    see `bpy.utils.register_class` for classes which can
    be registered.
    """

def unregister_cli_command(handle: typing.Any) -> None:
    """Unregister a CLI command.

    :param handle: The return value of `register_cli_command`.
    """

def unregister_manual_map(
    manual_hook: collections.abc.Callable[tuple[str, list[tuple[str, str]]]],
) -> None:
    """Unregister a previously registered manual map hook.

    :param manual_hook: The hook function to remove.
    """

def unregister_preset_path(path: str) -> bool:
    """Unregister a preset search path.

        :param path: preset directory (must be an absolute path).

    This must match the registered path exactly.
        :return: success
    """

def unregister_tool(tool_cls: type[bpy.types.WorkSpaceTool]) -> None:
    """Unregister a previously registered tool.

    :param tool_cls: The tool class to unregister.
    """

def user_resource(
    resource_type: typing.Literal["DATAFILES", "CONFIG", "SCRIPTS", "EXTENSIONS"],
    *,
    path: str = "",
    create: bool = False,
) -> str:
    """Return a user resource path (normally from the users home directory).

    :param resource_type: The resource type.
    :param path: Optional subdirectory.
    :param create: Treat the path as a directory and create it if its not existing.
    :return: a path.
    """
