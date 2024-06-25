"""
This module is used for all Blender/Python access.

```../examples/bpy.data.py```

"""

import typing
import collections.abc
import bpy.types

from . import app
from . import msgbus
from . import ops
from . import path
from . import props
from . import types
from . import utils

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")
context: bpy.types.Context

data: bpy.types.BlendData
""" Access to Blender's internal data
"""
