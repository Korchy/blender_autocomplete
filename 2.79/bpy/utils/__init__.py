import sys
import typing
from . import previews
from . import units


def app_template_paths(subdir: str = None):
    '''Returns valid application template paths. 

    :param subdir: Optional subdir. 
    :type subdir: str
    :return:  app template paths. 
    '''

    pass


def blend_paths(absolute: bool = False,
                packed: bool = False,
                local: bool = False) -> list:
    '''Returns a list of paths to external files referenced by the loaded .blend file. 

    :param absolute: When true the paths returned are made absolute. 
    :type absolute: bool
    :param packed: When true skip file paths for packed data. 
    :type packed: bool
    :param local: When true skip linked library paths. 
    :type local: bool
    :return:  path list. 
    '''

    pass


def escape_identifier(string: str) -> str:
    '''Simple string escaping function used for animation paths. 

    :param string: text 
    :type string: str
    :return:  The escaped string. 
    '''

    pass


def keyconfig_set(filepath, report=None):
    '''

    '''

    pass


def load_scripts(reload_scripts: bool = False, refresh_scripts: bool = False):
    '''Load scripts and run each modules register function. 

    :param reload_scripts: Causes all scripts to have their unregister method called before loading. 
    :type reload_scripts: bool
    :param refresh_scripts: only load scripts which are not already loaded as modules. 
    :type refresh_scripts: bool
    '''

    pass


def make_rna_paths(struct_name: str, prop_name: str, enum_name: str):
    '''Create RNA “paths” from given names. 

    :param struct_name: Name of a RNA struct (like e.g. “Scene”). 
    :type struct_name: str
    :param prop_name: Name of a RNA struct’s property. 
    :type prop_name: str
    :param enum_name: Name of a RNA enum identifier. 
    :type enum_name: str
    :return:  A triple of three “RNA paths” (most_complete_path, “struct.prop”, “struct.prop:’enum’”). If no enum_name is given, the third element will always be void. 
    '''

    pass


def manual_map():
    '''

    '''

    pass


def modules_from_path(path: str, loaded_modules: set) -> list:
    '''Load all modules in a path and return them as a list. 

    :param path: this path is scanned for scripts and packages. 
    :type path: str
    :param loaded_modules: already loaded module names, files matching these names will be ignored. 
    :type loaded_modules: set
    :return:  all loaded modules. 
    '''

    pass


def preset_find(name, preset_path, display_name=False, ext='.py'):
    '''

    '''

    pass


def preset_paths(subdir: str) -> list:
    '''Returns a list of paths for a specific preset. 

    :param subdir: preset subdirectory (must not be an absolute path). 
    :type subdir: str
    :return:  script paths. 
    '''

    pass


def refresh_script_paths():
    '''Run this after creating new script paths to update sys.path 

    '''

    pass


def register_class(cls):
    '''If the class has a register class method it will be called before registration. 

    '''

    pass


def register_manual_map(manual_hook):
    '''

    '''

    pass


def register_module(module, verbose=False):
    '''

    '''

    pass


def register_submodule_factory(module_name: str, submodule_names: list):
    '''Utility function to create register and unregister functions which simply load submodules, calling their register & unregister functions. 

    :param module_name: The module name, typically __name__. 
    :type module_name: str
    :param submodule_names: List of submodule names to load and unload. 
    :type submodule_names: list
    :return:  register and unregister functions. 
    '''

    pass


def resource_path(type: str, major: int = 2, minor: str = "") -> str:
    '''Return the base path for storing system files. 

    :param type: string in [‘USER’, ‘LOCAL’, ‘SYSTEM’]. 
    :type type: str
    :param major: major version, defaults to current. 
    :type major: int
    :param minor: minor version, defaults to current. 
    :type minor: str
    :return:  the resource path (not necessarily existing). 
    '''

    pass


def script_path_pref():
    '''returns the user preference or None 

    '''

    pass


def script_path_user():
    '''returns the env var and falls back to home dir or None 

    '''

    pass


def script_paths(subdir: str = None,
                 user_pref: bool = True,
                 check_all: bool = False,
                 use_user=True) -> list:
    '''Returns a list of valid script paths. 

    :param subdir: Optional subdir. 
    :type subdir: str
    :param user_pref: Include the user preference script path. 
    :type user_pref: bool
    :param check_all: Include local, user and system paths rather just the paths blender uses. 
    :type check_all: bool
    :return:  script paths. 
    '''

    pass


def smpte_from_frame(frame: int, fps=None, fps_base=None) -> str:
    '''If fps and fps_base are not given the current scene is used. 

    :param frame: frame number. 
    :type frame: int
    :return:  the frame string. 
    '''

    pass


def smpte_from_seconds(time: int, fps=None) -> str:
    '''If the fps is not given the current scene is used. 

    :param time: time in seconds. 
    :type time: int
    :return:  the frame string. 
    '''

    pass


def unregister_class(cls):
    '''If the class has an unregister class method it will be called before unregistering. 

    '''

    pass


def unregister_manual_map(manual_hook):
    '''

    '''

    pass


def unregister_module(module, verbose=False):
    '''

    '''

    pass


def user_resource(resource_type, path='', create: bool = False) -> str:
    '''Return a user resource path (normally from the users home directory). 

    :param type: Resource type in [‘DATAFILES’, ‘CONFIG’, ‘SCRIPTS’, ‘AUTOSAVE’]. 
    :type type: str
    :param subdir: Optional subdirectory. 
    :type subdir: str
    :param create: Treat the path as a directory and create it if its not existing. 
    :type create: bool
    :return:  a path. 
    '''

    pass
