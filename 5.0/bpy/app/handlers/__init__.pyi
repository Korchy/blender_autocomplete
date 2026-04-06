"""
This module contains callback lists


--------------------

This script shows the most simple example of adding a handler.

```../examples/bpy.app.handlers.py```


--------------------

By default handlers are freed when loading new files, in some cases you may
want the handler stay running across multiple files (when the handler is
part of an add-on for example).

For this the bpy.app.handlers.persistent decorator needs to be used.

```../examples/bpy.app.handlers.1.py```


--------------------

Altering data from handlers should be done carefully. While rendering the
frame_change_pre

 and frame_change_post

 handlers are called from one
thread and the viewport updates from a different thread. If the handler changes
data that is accessed by the viewport, this can cause a crash of Blender. In
such cases, lock the interface (Render → Lock Interface or
bpy.types.RenderSettings.use_lock_interface) before starting a render.

Below is an example of a mesh that is altered from a handler:

```../examples/bpy.app.handlers.2.py```

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

animation_playback_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on ending animation playback. Accepts two arguments: The scene data-block and the dependency graph being updated
"""

animation_playback_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on starting animation playback. Accepts two arguments: The scene data-block and the dependency graph being updated
"""

annotation_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on drawing an annotation (after). Accepts two arguments: the annotation data-block and dependency graph
"""

annotation_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on drawing an annotation (before). Accepts two arguments: the annotation data-block and dependency graph
"""

blend_import_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on linking or appending data (after). Accepts one argument: a BlendImportContext
"""

blend_import_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on linking or appending data (before). Accepts one argument: a BlendImportContext
"""

composite_cancel: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on a compositing background job (cancel). Accepts one argument: the scene data-block
"""

composite_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on a compositing background job (after). Accepts one argument: the scene data-block
"""

composite_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on a compositing background job (before). Accepts one argument: the scene data-block
"""

depsgraph_update_post: list[
    collections.abc.Callable[[bpy.types.Scene, bpy.types.Depsgraph], None]
]
""" on depsgraph update (post). Accepts two arguments: The scene data-block and the dependency graph being updated
"""

depsgraph_update_pre: list[collections.abc.Callable[[bpy.types.Scene, None], None]]
""" on depsgraph update (pre). Accepts two arguments: The scene data-block and the dependency graph being updated
"""

frame_change_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" Called after frame change for playback and rendering, after the data has been evaluated for the new frame. Accepts two arguments: The scene data-block and the dependency graph being updated
"""

frame_change_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" Called after frame change for playback and rendering, before any data is evaluated for the new frame. This makes it possible to change data and relations (for example swap an object to another mesh) for the new frame. Note that this handler is not to be used as before the frame changes event. The dependency graph is not available in this handler, as data and relations may have been altered and the dependency graph has not yet been updated for that. Accepts two arguments: The scene data-block and the dependency graph being updated
"""

load_factory_preferences_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on loading factory preferences (after)
"""

load_factory_startup_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on loading factory startup (after)
"""

load_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on loading a new blend file (after). Accepts one argument: the file being loaded, an empty string for the startup-file.
"""

load_post_fail: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on failure to load a new blend file (after). Accepts one argument: the file being loaded, an empty string for the startup-file.
"""

load_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on loading a new blend file (before).Accepts one argument: the file being loaded, an empty string for the startup-file.
"""

object_bake_cancel: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on canceling a bake job; will be called in the main thread. Accepts one argument: the object data-block being baked
"""

object_bake_complete: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on completing a bake job; will be called in the main thread. Accepts one argument: the object data-block being baked
"""

object_bake_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" before starting a bake job. Accepts one argument: the object data-block being baked
"""

persistent: typing.Any
""" Function decorator for callback functions not to be removed when loading new files
"""

redo_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on loading a redo step (after)
"""

redo_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on loading a redo step (before)
"""

render_cancel: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on canceling a render job. Accepts one argument: the scene data-block being rendered
"""

render_complete: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on completion of render job. Accepts one argument: the scene data-block being rendered
"""

render_init: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on initialization of a render job. Accepts one argument: the scene data-block being rendered
"""

render_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on render (after)
"""

render_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on render (before)
"""

render_stats: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on printing render statistics. Accepts one argument: the render stats (render/saving time plus in background mode frame/used [peak] memory).
"""

render_write: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on writing a render frame (directly after the frame is written)
"""

save_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on saving a blend file (after). Accepts one argument: the file being saved, an empty string for the startup-file.
"""

save_post_fail: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on failure to save a blend file (after). Accepts one argument: the file being saved, an empty string for the startup-file.
"""

save_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on saving a blend file (before). Accepts one argument: the file being saved, an empty string for the startup-file.
"""

translation_update_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on translation settings update
"""

undo_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on loading an undo step (after)
"""

undo_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on loading an undo step (before)
"""

version_update: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on ending the versioning code
"""

xr_session_start_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on starting an xr session (before)
"""
