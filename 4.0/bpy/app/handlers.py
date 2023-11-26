import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")
animation_playback_post: typing.List[
    typing.Callable[['bpy.types.Scene'], None]] = None
''' on ending animation playback
'''

animation_playback_pre: typing.List[typing.
                                    Callable[['bpy.types.Scene'], None]] = None
''' on starting animation playback
'''

annotation_post: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on drawing an annotation (after)
'''

annotation_pre: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on drawing an annotation (before)
'''

composite_cancel: typing.List[typing.
                              Callable[['bpy.types.Scene'], None]] = None
''' on a compositing background job (cancel)
'''

composite_post: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on a compositing background job (after)
'''

composite_pre: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on a compositing background job (before)
'''

depsgraph_update_post: typing.List[typing.
                                   Callable[['bpy.types.Scene'], None]] = None
''' on depsgraph update (post)
'''

depsgraph_update_pre: typing.List[typing.
                                  Callable[['bpy.types.Scene'], None]] = None
''' on depsgraph update (pre)
'''

frame_change_post: typing.List[typing.
                               Callable[['bpy.types.Scene'], None]] = None
''' Called after frame change for playback and rendering, after the data has been evaluated for the new frame.
'''

frame_change_pre: typing.List[typing.
                              Callable[['bpy.types.Scene'], None]] = None
''' Called after frame change for playback and rendering, before any data is evaluated for the new frame. This makes it possible to change data and relations (for example swap an object to another mesh) for the new frame. Note that this handler is **not** to be used as 'before the frame changes' event. The dependency graph is not available in this handler, as data and relations may have been altered and the dependency graph has not yet been updated for that.
'''

load_factory_preferences_post: typing.List[
    typing.Callable[['bpy.types.Scene'], None]] = None
''' on loading factory preferences (after)
'''

load_factory_startup_post: typing.List[
    typing.Callable[['bpy.types.Scene'], None]] = None
''' on loading factory startup (after)
'''

load_post: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on loading a new blend file (after). Accepts one argument: the file being loaded, an empty string for the startup-file.
'''

load_post_fail: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on failure to load a new blend file (after). Accepts one argument: the file being loaded, an empty string for the startup-file.
'''

load_pre: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on loading a new blend file (before).Accepts one argument: the file being loaded, an empty string for the startup-file.
'''

object_bake_cancel: typing.List[typing.
                                Callable[['bpy.types.Scene'], None]] = None
''' on canceling a bake job; will be called in the main thread
'''

object_bake_complete: typing.List[typing.
                                  Callable[['bpy.types.Scene'], None]] = None
''' on completing a bake job; will be called in the main thread
'''

object_bake_pre: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' before starting a bake job
'''

persistent = None
''' Function decorator for callback functions not to be removed when loading new files
'''

redo_post: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on loading a redo step (after)
'''

redo_pre: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on loading a redo step (before)
'''

render_cancel: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on canceling a render job
'''

render_complete: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on completion of render job
'''

render_init: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on initialization of a render job
'''

render_post: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on render (after)
'''

render_pre: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on render (before)
'''

render_stats: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on printing render statistics
'''

render_write: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on writing a render frame (directly after the frame is written)
'''

save_post: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on saving a blend file (after). Accepts one argument: the file being saved, an empty string for the startup-file.
'''

save_post_fail: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on failure to save a blend file (after). Accepts one argument: the file being saved, an empty string for the startup-file.
'''

save_pre: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on saving a blend file (before). Accepts one argument: the file being saved, an empty string for the startup-file.
'''

undo_post: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on loading an undo step (after)
'''

undo_pre: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on loading an undo step (before)
'''

version_update: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on ending the versioning code
'''

xr_session_start_pre: typing.List[typing.
                                  Callable[['bpy.types.Scene'], None]] = None
''' on starting an xr session (before)
'''
