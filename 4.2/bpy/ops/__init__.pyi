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
import typing_extensions
from . import action as action
from . import anim as anim
from . import armature as armature
from . import asset as asset
from . import boid as boid
from . import brush as brush
from . import buttons as buttons
from . import cachefile as cachefile
from . import camera as camera
from . import clip as clip
from . import cloth as cloth
from . import collection as collection
from . import console as console
from . import constraint as constraint
from . import curve as curve
from . import curves as curves
from . import cycles as cycles
from . import dpaint as dpaint
from . import ed as ed
from . import export_anim as export_anim
from . import export_scene as export_scene
from . import extensions as extensions
from . import file as file
from . import fluid as fluid
from . import font as font
from . import geometry as geometry
from . import gizmogroup as gizmogroup
from . import gpencil as gpencil
from . import graph as graph
from . import grease_pencil as grease_pencil
from . import image as image
from . import import_anim as import_anim
from . import import_curve as import_curve
from . import import_scene as import_scene
from . import info as info
from . import lattice as lattice
from . import marker as marker
from . import mask as mask
from . import material as material
from . import mball as mball
from . import mesh as mesh
from . import nla as nla
from . import node as node
from . import object as object
from . import outliner as outliner
from . import paint as paint
from . import paintcurve as paintcurve
from . import palette as palette
from . import particle as particle
from . import pose as pose
from . import poselib as poselib
from . import preferences as preferences
from . import ptcache as ptcache
from . import render as render
from . import rigidbody as rigidbody
from . import scene as scene
from . import screen as screen
from . import script as script
from . import sculpt as sculpt
from . import sculpt_curves as sculpt_curves
from . import sequencer as sequencer
from . import sound as sound
from . import spreadsheet as spreadsheet
from . import surface as surface
from . import text as text
from . import text_editor as text_editor
from . import texture as texture
from . import transform as transform
from . import ui as ui
from . import uilist as uilist
from . import uv as uv
from . import view2d as view2d
from . import view3d as view3d
from . import wm as wm
from . import workspace as workspace
from . import world as world
