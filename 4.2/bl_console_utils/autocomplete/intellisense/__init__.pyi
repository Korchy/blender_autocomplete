import typing
import collections.abc
import typing_extensions

def complete(line: str, cursor: int, namespace: dict, private: bool) -> list | str:
    """Returns a list of possible completions:

    :param line: incomplete text line
    :type line: str
    :param cursor: current character position
    :type cursor: int
    :param namespace: namespace
    :type namespace: dict
    :param private: whether private variables should be listed
    :type private: bool
    :return: list of completions, word
    :rtype: list | str
    """

def expand(
    line: str, cursor: int, namespace: dict, *, private: bool = True
) -> int | str:
    """This method is invoked when the user asks auto-completion,
    e.g. when Ctrl+Space is clicked.

        :param line: incomplete text line
        :type line: str
        :param cursor: current character position
        :type cursor: int
        :param namespace: namespace
        :type namespace: dict
        :param private: whether private variables should be listed
        :type private: bool
        :return: current expanded line, updated cursor position and scrollback
        :rtype: int | str
    """
