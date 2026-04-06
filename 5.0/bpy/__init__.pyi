"""
This module is used for all Blender/Python access.

```../examples/bpy.data.py```

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

from . import app as app
from . import msgbus as msgbus
from . import ops as ops
from . import path as path
from . import props as props
from . import types as types
from . import utils as utils

context: bpy.types.Context

data: bpy.types.BlendData
""" Access to Blenders internal data
"""
