import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class _TempModuleOverride:
    module: typing.Any
    module_name: typing.Any
    module_override: typing.Any

def add_scrollback(text, text_type) -> None: ...
def autocomplete(context) -> None: ...
def banner(context) -> None: ...
def copy_as_script(context) -> None: ...
def execute(context, is_interactive) -> None: ...
def get_console(console_id) -> None:
    """helper function for console operators
    currently each text data block gets its own
    console - code.InteractiveConsole()
    ...which is stored in this function.console_id can be any hashable type

    """

def replace_help(namespace) -> None: ...
