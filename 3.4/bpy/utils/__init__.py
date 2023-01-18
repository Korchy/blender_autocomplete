import sys
import typing
import bpy.types

from . import units
from . import previews

GenericType = typing.TypeVar("GenericType")


def app_template_paths(*, path: typing.Optional[str] = None) -> typing.Any:
    ''' Returns valid application template paths.

    :param path: Optional subdir.
    :type path: typing.Optional[str]
    :rtype: typing.Any
    :return: app template paths.
    '''

    pass


def blend_paths(absolute: typing.Optional[bool] = False,
                packed: typing.Optional[bool] = False,
                local: typing.Optional[bool] = False) -> typing.List[str]:
    ''' Returns a list of paths to external files referenced by the loaded .blend file.

    :param absolute: When true the paths returned are made absolute.
    :type absolute: typing.Optional[bool]
    :param packed: When true skip file paths for packed data.
    :type packed: typing.Optional[bool]
    :param local: When true skip linked library paths.
    :type local: typing.Optional[bool]
    :rtype: typing.List[str]
    :return: path list.
    '''

    pass


def escape_identifier(string: typing.Optional[str]) -> str:
    ''' Simple string escaping function used for animation paths.

    :param string: text
    :type string: typing.Optional[str]
    :rtype: str
    :return: The escaped string.
    '''

    pass


def execfile(filepath: typing.Optional[str],
             *,
             mod: typing.Optional[typing.Any] = None) -> typing.Any:
    ''' Execute a file path as a Python script.

    :param filepath: Path of the script to execute.
    :type filepath: typing.Optional[str]
    :param mod: Optional cached module, the result of a previous execution.
    :type mod: typing.Optional[typing.Any]
    :rtype: typing.Any
    :return: The module which can be passed back in as ``mod``.
    '''

    pass


def flip_name(name: typing.Optional[str],
              strip_digits: typing.Optional[bool] = False) -> str:
    ''' Flip a name between left/right sides, useful for mirroring bone names.

    :param name: Bone name to flip.
    :type name: typing.Optional[str]
    :param strip_digits: Whether to remove ``.###`` suffix.
    :type strip_digits: typing.Optional[bool]
    :rtype: str
    :return: The flipped name.
    '''

    pass


def is_path_builtin(path):
    ''' 

    '''

    pass


def keyconfig_init():
    ''' 

    '''

    pass


def keyconfig_set(filepath, *, report=None):
    ''' 

    '''

    pass


def load_scripts(*,
                 reload_scripts: typing.Optional[bool] = False,
                 refresh_scripts: typing.Optional[bool] = False):
    ''' Load scripts and run each modules register function.

    :param reload_scripts: Causes all scripts to have their unregister method called before loading.
    :type reload_scripts: typing.Optional[bool]
    :param refresh_scripts: only load scripts which are not already loaded as modules.
    :type refresh_scripts: typing.Optional[bool]
    '''

    pass


def make_rna_paths(struct_name: typing.Optional[str],
                   prop_name: typing.Optional[str],
                   enum_name: typing.Optional[str]) -> typing.Tuple:
    ''' Create RNA "paths" from given names.

    :param struct_name: Name of a RNA struct (like e.g. "Scene").
    :type struct_name: typing.Optional[str]
    :param prop_name: Name of a RNA struct's property.
    :type prop_name: typing.Optional[str]
    :param enum_name: Name of a RNA enum identifier.
    :type enum_name: typing.Optional[str]
    :rtype: typing.Tuple
    :return: A triple of three "RNA paths" (most_complete_path, "struct.prop", "struct.prop:'enum'"). If no enum_name is given, the third element will always be void.
    '''

    pass


def manual_map():
    ''' 

    '''

    pass


def modules_from_path(
        path: typing.Optional[str],
        loaded_modules: typing.Optional[typing.Set]) -> typing.List:
    ''' Load all modules in a path and return them as a list.

    :param path: this path is scanned for scripts and packages.
    :type path: typing.Optional[str]
    :param loaded_modules: already loaded module names, files matching these names will be ignored.
    :type loaded_modules: typing.Optional[typing.Set]
    :rtype: typing.List
    :return: all loaded modules.
    '''

    pass


def preset_find(name, preset_path, *, display_name=False, ext='.py'):
    ''' 

    '''

    pass


def preset_paths(subdir: typing.Optional[str]) -> typing.List:
    ''' Returns a list of paths for a specific preset.

    :param subdir: preset subdirectory (must not be an absolute path).
    :type subdir: typing.Optional[str]
    :rtype: typing.List
    :return: script paths.
    '''

    pass


def refresh_script_paths():
    ''' Run this after creating new script paths to update sys.path

    '''

    pass


def register_class(cls: typing.Optional[typing.Any]):
    ''' Register a subclass of a Blender type class. :raises ValueError: if the class is not a subclass of a registerable blender class.

    :param cls: `bpy.types.Panel`, `bpy.types.UIList`, `bpy.types.Menu`, `bpy.types.Header`, `bpy.types.Operator`, `bpy.types.KeyingSetInfo`, `bpy.types.RenderEngine`
    :type cls: typing.Optional[typing.Any]
    '''

    pass


def register_classes_factory(classes):
    ''' Utility function to create register and unregister functions which simply registers and unregisters a sequence of classes.

    '''

    pass


def register_manual_map(manual_hook):
    ''' 

    '''

    pass


def register_submodule_factory(
        module_name: typing.Optional[str],
        submodule_names: typing.Optional[typing.List[str]]) -> typing.Tuple:
    ''' Utility function to create register and unregister functions which simply load submodules, calling their register & unregister functions.

    :param module_name: The module name, typically ``__name__``.
    :type module_name: typing.Optional[str]
    :param submodule_names: List of submodule names to load and unload.
    :type submodule_names: typing.Optional[typing.List[str]]
    :rtype: typing.Tuple
    :return: register and unregister functions.
    '''

    pass


def register_tool(tool_cls,
                  *,
                  after: typing.Optional[typing.Any] = None,
                  separator: typing.Optional[bool] = False,
                  group: typing.Optional[bool] = False):
    ''' Register a tool in the toolbar.

    :param tool: A tool subclass.
    :type tool: typing.Optional['bpy.types.WorkSpaceTool']
    :param space_type: Space type identifier.
    :type space_type: typing.Optional[str]
    :param after: Optional identifiers this tool will be added after.
    :type after: typing.Optional[typing.Any]
    :param separator: When true, add a separator before this tool.
    :type separator: typing.Optional[bool]
    :param group: When true, add a new nested group of tools.
    :type group: typing.Optional[bool]
    '''

    pass


def resource_path(type: typing.Optional[str],
                  major: typing.Optional[int] = 'bpy.app.version[0]',
                  minor: typing.Optional[str] = 'bpy.app.version[1]') -> str:
    ''' Return the base path for storing system files.

    :param type: string in ['USER', 'LOCAL', 'SYSTEM'].
    :type type: typing.Optional[str]
    :param major: major version, defaults to current.
    :type major: typing.Optional[int]
    :param minor: minor version, defaults to current.
    :type minor: typing.Optional[str]
    :rtype: str
    :return: the resource path (not necessarily existing).
    '''

    pass


def script_path_pref():
    ''' returns the user preference or None

    '''

    pass


def script_path_user():
    ''' returns the env var and falls back to home dir or None

    '''

    pass


def script_paths(*,
                 subdir: typing.Optional[str] = None,
                 user_pref: typing.Optional[bool] = True,
                 check_all: typing.Optional[bool] = False,
                 use_user=True) -> typing.List:
    ''' Returns a list of valid script paths.

    :param subdir: Optional subdir.
    :type subdir: typing.Optional[str]
    :param user_pref: Include the user preference script path.
    :type user_pref: typing.Optional[bool]
    :param check_all: Include local, user and system paths rather just the paths Blender uses.
    :type check_all: typing.Optional[bool]
    :rtype: typing.List
    :return: script paths.
    '''

    pass


def smpte_from_frame(frame: typing.Optional[int], *, fps=None,
                     fps_base=None) -> str:
    ''' Returns an SMPTE formatted string from the *frame*: ``HH:MM:SS:FF``. If *fps* and *fps_base* are not given the current scene is used.

    :param frame: frame number.
    :type frame: typing.Optional[int]
    :rtype: str
    :return: the frame string.
    '''

    pass


def smpte_from_seconds(time: typing.Union[int, float],
                       *,
                       fps=None,
                       fps_base=None) -> str:
    ''' Returns an SMPTE formatted string from the *time*: ``HH:MM:SS:FF``. If *fps* and *fps_base* are not given the current scene is used.

    :param time: time in seconds.
    :type time: typing.Union[int, float]
    :rtype: str
    :return: the frame string.
    '''

    pass


def time_from_frame(frame, fps, fps_base):
    ''' 

    '''

    pass


def time_to_frame(time, fps, fps_base):
    ''' 

    '''

    pass


def unescape_identifier(string: typing.Optional[str]) -> str:
    ''' Simple string un-escape function used for animation paths. This performs the reverse of `escape_identifier`.

    :param string: text
    :type string: typing.Optional[str]
    :rtype: str
    :return: The un-escaped string.
    '''

    pass


def unregister_class(cls):
    ''' Unload the Python class from blender. If the class has an *unregister* class method it will be called before unregistering.

    '''

    pass


def unregister_manual_map(manual_hook):
    ''' 

    '''

    pass


def unregister_tool(tool_cls):
    ''' 

    '''

    pass


def user_resource(resource_type,
                  *,
                  path: typing.Optional[str] = '',
                  create: typing.Optional[bool] = False) -> str:
    ''' Return a user resource path (normally from the users home directory).

    :param type: Resource type in ['DATAFILES', 'CONFIG', 'SCRIPTS', 'AUTOSAVE'].
    :type type: typing.Optional[str]
    :param path: Optional subdirectory.
    :type path: typing.Optional[str]
    :param create: Treat the path as a directory and create it if its not existing.
    :type create: typing.Optional[bool]
    :rtype: str
    :return: a path.
    '''

    pass
