import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def log2vis(msgs, settings):
    """Globally mimics deprecated fribidi_log2vis.
    msgs should be an iterable of messages to RTL-process.

    """

    ...

def protect_format_seq(msg):
    """Find some specific escaping/formatting sequences (like ", %s, etc.,
    and protect them from any modification!

    """

    ...
