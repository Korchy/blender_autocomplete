import typing
import collections.abc
import typing_extensions

class _TempModuleOverride:
    module: typing.Any
    module_name: typing.Any
    module_override: typing.Any

def add_scrollback(text, text_type): ...
def autocomplete(context): ...
def banner(context): ...
def copy_as_script(context): ...
def execute(context, is_interactive): ...
def get_console(console_id):
    """helper function for console operators
    currently each text data block gets its own
    console - code.InteractiveConsole()
    ...which is stored in this function.console_id can be any hashable type

    """

def replace_help(namespace): ...
