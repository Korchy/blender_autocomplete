"""

--------------------

Provides python access to calling operators, this includes operators written in
C, Python or macros.

Only keyword arguments can be used to pass operator properties.

Operators don't have return values as you might expect,
instead they return a set() which is made up of:
{'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'}

.
Common return values are {'FINISHED'}

 and {'CANCELLED'}

, the latter
meaning that the operator execution was aborted without making any changes or
saving an undo history entry.

Calling an operator in the wrong context will raise a RuntimeError

,
there is a poll() method to avoid this problem.

Note that the operator ID (bl_idname) in this example is mesh.subdivide

,
bpy.ops

 is just the access path for python.


--------------------

For calling operators keywords are used for operator properties and
positional arguments are used to define how the operator is called.

There are 2 optional positional arguments (documented in detail below).

```
bpy.ops.test.operator(execution_context, undo)
```

* execution_context - str

 (enum).
* undo - bool

 type.

Each of these arguments is optional, but must be given in the order above.

```../examples/bpy.ops.py```


--------------------

It is possible to override context members that the operator sees, so that they
act on specified rather than the selected or active data, or to execute an
operator in the different part of the user interface.

The context overrides are passed as a dictionary, with keys matching the context
member names in bpy.context.
For example to override bpy.context.active_object

,
you would pass {'active_object': object}

 to bpy.types.Context.temp_override.

[NOTE]
You will nearly always want to use a copy of the actual current context as basis
(otherwise, you'll have to find and gather all needed data yourself).

```../examples/bpy.ops.1.py```


--------------------

When calling an operator you may want to pass the execution context.

This determines the context that is given for the operator to run in, and whether
invoke() is called or only execute().

EXEC_DEFAULT

 is used by default, running only the execute()

 method, but you may
want the operator to take user interaction with INVOKE_DEFAULT

 which will also
call invoke() if existing.

The execution context is one of:

* INVOKE_DEFAULT


* INVOKE_REGION_WIN


* INVOKE_REGION_CHANNELS


* INVOKE_REGION_PREVIEW


* INVOKE_AREA


* INVOKE_SCREEN


* EXEC_DEFAULT


* EXEC_REGION_WIN


* EXEC_REGION_CHANNELS


* EXEC_REGION_PREVIEW


* EXEC_AREA


* EXEC_SCREEN



```../examples/bpy.ops.2.py```

It is also possible to run an operator in a particular part of the user
interface. For this we need to pass the window, area and sometimes a region.

```../examples/bpy.ops.3.py```

bpy.ops.*

:caption: Submodules
:maxdepth: 1
:glob:

"""

import typing
import collections.abc
from . import action
from . import anim
from . import armature
from . import asset
from . import boid
from . import brush
from . import buttons
from . import cachefile
from . import camera
from . import clip
from . import cloth
from . import collection
from . import console
from . import constraint
from . import curve
from . import curves
from . import cycles
from . import dpaint
from . import ed
from . import export_anim
from . import export_mesh
from . import export_scene
from . import file
from . import fluid
from . import font
from . import geometry
from . import gizmogroup
from . import gpencil
from . import graph
from . import grease_pencil
from . import image
from . import import_anim
from . import import_curve
from . import import_mesh
from . import import_scene
from . import info
from . import lattice
from . import marker
from . import mask
from . import material
from . import mball
from . import mesh
from . import nla
from . import node
from . import object
from . import outliner
from . import paint
from . import paintcurve
from . import palette
from . import particle
from . import pose
from . import poselib
from . import preferences
from . import ptcache
from . import render
from . import rigidbody
from . import scene
from . import screen
from . import script
from . import sculpt
from . import sculpt_curves
from . import sequencer
from . import sound
from . import spreadsheet
from . import surface
from . import text
from . import text_editor
from . import texture
from . import transform
from . import ui
from . import uilist
from . import uv
from . import view2d
from . import view3d
from . import wm
from . import workspace
from . import world

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")
