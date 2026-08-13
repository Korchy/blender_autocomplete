import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class APIVersionError:
    """Raised when none of the API versions declared by a remote asset library are supported by Blender."""

    args: typing.Any

class CLIArguments:
    """Parsed command-line arguments."""

def add_cli_parser(subparsers) -> None:
    """Add argparser for this subcommand."""

def cli_main(arguments_raw) -> None:
    """Generate the index for the passed-on-the-CLI asset library path."""
