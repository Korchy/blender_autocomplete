"""
This module provides data types of view map components (0D and 1D
elements), base classes for defining line stylization rules
(predicates, functions, chaining iterators, and stroke shaders),
as well as helper functions for style module writing.

freestyle.types.rst
freestyle.predicates.rst
freestyle.functions.rst
freestyle.chainingiterators.rst
freestyle.shaders.rst
freestyle.utils.rst

:maxdepth: 1
:caption: Submodules

"""

import typing
import collections.abc
from . import chainingiterators
from . import functions
from . import predicates
from . import shaders
from . import types
from . import utils

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")
