import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def complete(
    line: str, cursor: int, namespace: dict, private: bool
) -> tuple[list[str], str]:
    """Returns a list of possible completions:

    :param line: incomplete text line
    :param cursor: current character position
    :param namespace: namespace
    :param private: whether private variables should be listed
    :return: list of completions, word
    """

def expand(
    line: str, cursor: int, namespace: dict[str, typing.Any], *, private: bool = True
) -> int | str:
    """This method is invoked when the user asks auto-completion,
    e.g. when Ctrl+Space is clicked.

        :param line: incomplete text line
        :param cursor: current character position
        :param namespace: namespace
        :param private: whether private variables should be listed
        :return: current expanded line, updated cursor position and scrollback
    """
