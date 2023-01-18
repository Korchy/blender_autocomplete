import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def cycles_integrator_preset_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "",
        remove_name: typing.Union[bool, typing.Any] = False,
        remove_active: typing.Union[bool, typing.Any] = False):
    ''' Add an Integrator Preset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the preset, used to make the path name
    :type name: typing.Union[str, typing.Any]
    :param remove_name: remove_name
    :type remove_name: typing.Union[bool, typing.Any]
    :param remove_active: remove_active
    :type remove_active: typing.Union[bool, typing.Any]
    '''

    pass


def cycles_performance_preset_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "",
        remove_name: typing.Union[bool, typing.Any] = False,
        remove_active: typing.Union[bool, typing.Any] = False):
    ''' Add an Performance Preset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the preset, used to make the path name
    :type name: typing.Union[str, typing.Any]
    :param remove_name: remove_name
    :type remove_name: typing.Union[bool, typing.Any]
    :param remove_active: remove_active
    :type remove_active: typing.Union[bool, typing.Any]
    '''

    pass


def cycles_sampling_preset_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "",
        remove_name: typing.Union[bool, typing.Any] = False,
        remove_active: typing.Union[bool, typing.Any] = False):
    ''' Add a Sampling Preset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the preset, used to make the path name
    :type name: typing.Union[str, typing.Any]
    :param remove_name: remove_name
    :type remove_name: typing.Union[bool, typing.Any]
    :param remove_active: remove_active
    :type remove_active: typing.Union[bool, typing.Any]
    '''

    pass


def cycles_viewport_sampling_preset_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "",
        remove_name: typing.Union[bool, typing.Any] = False,
        remove_active: typing.Union[bool, typing.Any] = False):
    ''' Add a Viewport Sampling Preset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the preset, used to make the path name
    :type name: typing.Union[str, typing.Any]
    :param remove_name: remove_name
    :type remove_name: typing.Union[bool, typing.Any]
    :param remove_active: remove_active
    :type remove_active: typing.Union[bool, typing.Any]
    '''

    pass


def opengl(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None,
           *,
           animation: typing.Union[bool, typing.Any] = False,
           render_keyed_only: typing.Union[bool, typing.Any] = False,
           sequencer: typing.Union[bool, typing.Any] = False,
           write_still: typing.Union[bool, typing.Any] = False,
           view_context: typing.Union[bool, typing.Any] = True):
    ''' Take a snapshot of the active viewport

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param animation: Animation, Render files from the animation range of this scene
    :type animation: typing.Union[bool, typing.Any]
    :param render_keyed_only: Render Keyframes Only, Render only those frames where selected objects have a key in their animation data. Only used when rendering animation
    :type render_keyed_only: typing.Union[bool, typing.Any]
    :param sequencer: Sequencer, Render using the sequencer's OpenGL display
    :type sequencer: typing.Union[bool, typing.Any]
    :param write_still: Write Image, Save rendered the image to the output path (used only when animation is disabled)
    :type write_still: typing.Union[bool, typing.Any]
    :param view_context: View Context, Use the current 3D view for rendering, else use scene settings
    :type view_context: typing.Union[bool, typing.Any]
    '''

    pass


def play_rendered_anim(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None):
    ''' Play back rendered frames/movies using an external player :file: `startup/bl_operators/screen_play_rendered_anim.py\:64 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/screen_play_rendered_anim.py$64>`_

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def preset_add(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               name: typing.Union[str, typing.Any] = "",
               remove_name: typing.Union[bool, typing.Any] = False,
               remove_active: typing.Union[bool, typing.Any] = False):
    ''' Add or remove a Render Preset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the preset, used to make the path name
    :type name: typing.Union[str, typing.Any]
    :param remove_name: remove_name
    :type remove_name: typing.Union[bool, typing.Any]
    :param remove_active: remove_active
    :type remove_active: typing.Union[bool, typing.Any]
    '''

    pass


def render(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None,
           *,
           animation: typing.Union[bool, typing.Any] = False,
           write_still: typing.Union[bool, typing.Any] = False,
           use_viewport: typing.Union[bool, typing.Any] = False,
           layer: typing.Union[str, typing.Any] = "",
           scene: typing.Union[str, typing.Any] = ""):
    ''' Render active scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param animation: Animation, Render files from the animation range of this scene
    :type animation: typing.Union[bool, typing.Any]
    :param write_still: Write Image, Save rendered the image to the output path (used only when animation is disabled)
    :type write_still: typing.Union[bool, typing.Any]
    :param use_viewport: Use 3D Viewport, When inside a 3D viewport, use layers and camera of the viewport
    :type use_viewport: typing.Union[bool, typing.Any]
    :param layer: Render Layer, Single render layer to re-render (used only when animation is disabled)
    :type layer: typing.Union[str, typing.Any]
    :param scene: Scene, Scene to render, current scene if not specified
    :type scene: typing.Union[str, typing.Any]
    '''

    pass


def shutter_curve_preset(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None,
                         *,
                         shape: typing.Optional[typing.Any] = 'SMOOTH'):
    ''' Set shutter curve

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param shape: Mode
    :type shape: typing.Optional[typing.Any]
    '''

    pass


def view_cancel(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Cancel show render view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def view_show(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None):
    ''' Toggle show render view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass
