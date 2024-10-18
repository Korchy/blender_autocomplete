import typing
import collections.abc
import typing_extensions

def generate(context, space_type, *, use_fallback_keys=True, use_reset=True):
    """Keymap for popup toolbar, currently generated each time."""
