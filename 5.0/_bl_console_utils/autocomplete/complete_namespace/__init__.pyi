import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def complete(word: str, namespace: dict, *, private: bool = True) -> list[str]:
    """Complete word within a namespace with the standard rlcompleter
    module. Also supports index or key access [].

        :param word: word to be completed
        :param namespace: namespace
        :param private: whether private attribute/methods should be returned
        :return: completion matches
    """

def complete_indices(
    word: str, namespace: dict, *, obj=None, base: str | None = None
) -> list[str]:
    """Complete a list or dictionary with its indices:

    :param word: word to be completed
    :param namespace: namespace
    :param obj: object evaluated from base
    :param base: sub-string which can be evaluated into an object.
    :return: completion matches
    """

def complete_names(word: str, namespace: dict[str, typing.Any]) -> list[str]:
    """Complete variable names or attributes

    :param word: word to be completed
    :param namespace: namespace
    :return: completion matches
    """

def is_dict(obj) -> None:
    """Returns whether obj is a dictionary"""

def is_struct_seq(obj) -> None:
    """Returns whether obj is a structured sequence subclass: sys.float_info"""
