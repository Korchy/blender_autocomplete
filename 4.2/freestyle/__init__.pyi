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
import typing_extensions
from . import chainingiterators as chainingiterators
from . import functions as functions
from . import predicates as predicates
from . import shaders as shaders
from . import types as types
from . import utils as utils
