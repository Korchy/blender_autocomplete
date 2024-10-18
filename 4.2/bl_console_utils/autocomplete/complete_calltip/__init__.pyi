import typing
import collections.abc
import typing_extensions

def complete(line: str, cursor: int, namespace: dict) -> str:
    """Complete callable with call-tip.

    :param line: incomplete text line
    :type line: str
    :param cursor: current character position
    :type cursor: int
    :param namespace: namespace
    :type namespace: dict
    :return: (matches, world, scrollback)
    :rtype: str
    """

def get_argspec(
    func, *, strip_self: bool = True, doc: str | None = None, source: str | None = None
) -> str:
    """Get argument specifications.

    :param strip_self: strip self from argspec
    :type strip_self: bool
    :param doc: doc string of func (optional)
    :type doc: str | None
    :param source: source code of func (optional)
    :type source: str | None
    :return: argument specification
    :rtype: str
    """

def get_doc(obj) -> str:
    """Get the doc string or comments for an object.

    :return: doc string
    :rtype: str
    """

def reduce_newlines(text: str) -> str:
    """Reduces multiple newlines to a single newline.

    :param text: text with multiple newlines
    :type text: str
    :return: text with single newlines
    :rtype: str
    """

def reduce_spaces(text: str) -> str:
    """Reduces multiple white-spaces to a single space.

    :param text: text with multiple spaces
    :type text: str
    :return: text with single spaces
    :rtype: str
    """
