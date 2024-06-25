import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def complete(word: str, namespace: dict, private: bool = True) -> list[str]:
    """Complete word within a namespace with the standard rlcompleter
    module. Also supports index or key access [].

        :param word: word to be completed
        :type word: str
        :param namespace: namespace
        :type namespace: dict
        :param private: whether private attribute/methods should be returned
        :type private: bool
        :return: completion matches
        :rtype: list[str]
    """

    ...

def complete_indices(
    word: str, namespace: dict, obj=None, base: str = None
) -> list[str]:
    """Complete a list or dictionary with its indices:

    :param word: word to be completed
    :type word: str
    :param namespace: namespace
    :type namespace: dict
    :param obj: object evaluated from base
    :param base: sub-string which can be evaluated into an object.
    :type base: str
    :return: completion matches
    :rtype: list[str]
    """

    ...

def complete_names(word: str, namespace: dict) -> list[str]:
    """Complete variable names or attributes

    :param word: word to be completed
    :type word: str
    :param namespace: namespace
    :type namespace: dict
    :return: completion matches
    :rtype: list[str]
    """

    ...

def is_dict(obj):
    """Returns whether obj is a dictionary"""

    ...

def is_struct_seq(obj):
    """Returns whether obj is a structured sequence subclass: sys.float_info"""

    ...
