import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def complete(
    line: str, cursor: int, namespace: dict[str, typing.Any]
) -> tuple[str, str, str]:
    """Complete callable with call-tip.

    :param line: incomplete text line
    :param cursor: current character position
    :param namespace: namespace
    :return: (matches, world, scrollback)
    """

def get_argspec(
    func, *, strip_self: bool = True, doc: str | None = None, source: str | None = None
) -> str:
    """Get argument specifications.

    :param strip_self: strip self from argspec
    :param doc: doc string of func (optional)
    :param source: source code of func (optional)
    :return: argument specification
    """

def get_doc(obj) -> str:
    """Get the doc string or comments for an object.

    :return: doc string
    """

def reduce_newlines(text: str) -> str:
    """Reduces multiple newlines to a single newline.

    :param text: text with multiple newlines
    :return: text with single newlines
    """

def reduce_spaces(text: str) -> str:
    """Reduces multiple white-spaces to a single space.

    :param text: text with multiple spaces
    :return: text with single spaces
    """
