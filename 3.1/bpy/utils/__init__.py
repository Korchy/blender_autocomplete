import sys
import typing
import bpy.types
import bpy.context

from . import previews
from . import units


def app_template_paths(*, path: str = None):
    ''' Returns valid application template paths.

    :param path: Optional subdir.
    :type path: str
    :return: app template paths.
    '''

    pass


def blend_paths(absolute: bool = False,
                packed: bool = False,
                local: bool = False) -> list:
    ''' Returns a list of paths to external files referenced by the loaded .blend file.

    :param absolute: When true the paths returned are made absolute.
    :type absolute: bool
    :param packed: When true skip file paths for packed data.
    :type packed: bool
    :param local: When true skip linked library paths.
    :type local: bool
    :rtype: list
    :return: path list.
    '''

    pass


def escape_identifier(string: str) -> str:
    ''' Simple string escaping function used for animation paths.

    :param string: text
    :type string: str
    :rtype: str
    :return: The escaped string.
    '''

    pass


def execfile(filepath: str, *, mod=None):
    ''' Execute a file path as a Python script.

    :param filepath: Path of the script to execute.
    :type filepath: str
    :param mod: Optional cached module, the result of a previous execution.
    :return: The module which can be passed back in as mod .
    '''

    pass


def flip_name(name: str, strip_digits: bool = False) -> str:
    ''' Flip a name between left/right sides, useful for mirroring bone names.

    :param name: Bone name to flip.
    :type name: str
    :param strip_digits: Whether to remove .### suffix.
    :type strip_digits: bool
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
                 reload_scripts: bool = False,
                 refresh_scripts: bool = False):
    ''' Load scripts and run each modules register function.

    :param reload_scripts: Causes all scripts to have their unregister method called before loading.
    :type reload_scripts: bool
    :param refresh_scripts: only load scripts which are not already loaded as modules.
    :type refresh_scripts: bool
    '''

    pass


def make_rna_paths(struct_name: str, prop_name: str, enum_name: str) -> tuple:
    ''' Create RNA "paths" from given names.

    :param struct_name: Name of a RNA struct (like e.g. "Scene").
    :type struct_name: str
    :param prop_name: Name of a RNA struct's property.
    :type prop_name: str
    :param enum_name: Name of a RNA enum identifier.
    :type enum_name: str
    :rtype: tuple
    :return: A triple of three "RNA paths" (most_complete_path, "struct.prop", "struct.prop:'enum'"). If no enum_name is given, the third element will always be void.
    '''

    pass


def manual_map():
    ''' 

    '''

    pass


def modules_from_path(path: str, loaded_modules: set) -> list:
    ''' Load all modules in a path and return them as a list.

    :param path: this path is scanned for scripts and packages.
    :type path: str
    :param loaded_modules: already loaded module names, files matching these names will be ignored.
    :type loaded_modules: set
    :rtype: list
    :return: all loaded modules.
    '''

    pass


def preset_find(name, preset_path, *, display_name=False, ext='.py'):
    ''' 

    '''

    pass


def preset_paths(subdir: str) -> list:
    ''' Returns a list of paths for a specific preset.

    :param subdir: preset subdirectory (must not be an absolute path).
    :type subdir: str
    :rtype: list
    :return: script paths.
    '''

    pass


def refresh_script_paths():
    ''' Run this after creating new script paths to update sys.path

    '''

    pass


def register_class(cls):
    ''' Register a subclass of a Blender type class. :raises ValueError: if the class is not a subclass of a registerable blender class.

    :param cls: bpy.types.Panel , bpy.types.UIList , bpy.types.Menu , bpy.types.Header , bpy.types.Operator , bpy.types.KeyingSetInfo , bpy.types.RenderEngine
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


def register_submodule_factory(module_name: str,
                               submodule_names: list) -> tuple:
    ''' Utility function to create register and unregister functions which simply load submodules, calling their register & unregister functions.

    :param module_name: The module name, typically __name__ .
    :type module_name: str
    :param submodule_names: List of submodule names to load and unload.
    :type submodule_names: list
    :rtype: tuple
    :return: register and unregister functions.
    '''

    pass


def register_tool(tool_cls,
                  *,
                  after: 'bpy.context.collection' = None,
                  separator: bool = False,
                  group: bool = False):
    ''' Register a tool in the toolbar.

    :param tool: A tool subclass.
    :type tool: 'bpy.types.WorkSpaceTool'
    :param space_type: Space type identifier.
    :type space_type: str
    :param after: Optional identifiers this tool will be added after.
    :type after: 'bpy.context.collection'
    :param separator: When true, add a separator before this tool.
    :type separator: bool
    :param group: When true, add a new nested group of tools.
    :type group: bool
    '''

    pass


def resource_path(type: str,
                  major: int = 'bpy.app.version[0]',
                  minor: str = 'bpy.app.version[1]') -> str:
    ''' Return the base path for storing system files.

    :param type: string in ['USER', 'LOCAL', 'SYSTEM'].
    :type type: str
    :param major: major version, defaults to current.
    :type major: int
    :param minor: minor version, defaults to current.
    :type minor: str
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
                 subdir: str = None,
                 user_pref: bool = True,
                 check_all: bool = False,
                 use_user=True) -> list:
    ''' Returns a list of valid script paths.

    :param subdir: Optional subdir.
    :type subdir: str
    :param user_pref: Include the user preference script path.
    :type user_pref: bool
    :param check_all: Include local, user and system paths rather just the paths blender uses.
    :type check_all: bool
    :rtype: list
    :return: script paths.
    '''

    pass


def smpte_from_frame(frame: int, *, fps=None, fps_base=None) -> str:
    ''' Returns an SMPTE formatted string from the *frame*: HH:MM:SS:FF . If *fps* and *fps_base* are not given the current scene is used.

    :param frame: frame number.
    :type frame: int
    :rtype: str
    :return: the frame string.
    '''

    pass


def smpte_from_seconds(time: typing.Union[int, float],
                       *,
                       fps=None,
                       fps_base=None) -> str:
    ''' Returns an SMPTE formatted string from the *time*: HH:MM:SS:FF . If *fps* and *fps_base* are not given the current scene is used.

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


def unescape_identifier(string: str) -> str:
    ''' Simple string un-escape function used for animation paths. This performs the reverse of escape_identifier .

    :param string: text
    :type string: str
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


def user_resource(resource_type, *, path: str = '',
                  create: bool = False) -> str:
    ''' Return a user resource path (normally from the users home directory).

    :param type: Resource type in ['DATAFILES', 'CONFIG', 'SCRIPTS', 'AUTOSAVE'].
    :type type: str
    :param path: Optional subdirectory.
    :type path: str
    :param create: Treat the path as a directory and create it if its not existing.
    :type create: bool
    :rtype: str
    :return: a path.
    '''

    pass
