import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def cycles_integrator_preset_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        name: str = "",
        remove_name: bool = False,
        remove_active: bool = False):
    ''' Add an Integrator Preset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool
    :param remove_active: remove_active
    :type remove_active: bool
    '''

    pass


def cycles_performance_preset_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        name: str = "",
        remove_name: bool = False,
        remove_active: bool = False):
    ''' Add an Performance Preset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool
    :param remove_active: remove_active
    :type remove_active: bool
    '''

    pass


def cycles_sampling_preset_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        name: str = "",
        remove_name: bool = False,
        remove_active: bool = False):
    ''' Add a Sampling Preset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool
    :param remove_active: remove_active
    :type remove_active: bool
    '''

    pass


def cycles_viewport_sampling_preset_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        name: str = "",
        remove_name: bool = False,
        remove_active: bool = False):
    ''' Add a Viewport Sampling Preset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool
    :param remove_active: remove_active
    :type remove_active: bool
    '''

    pass


def opengl(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           animation: bool = False,
           render_keyed_only: bool = False,
           sequencer: bool = False,
           write_still: bool = False,
           view_context: bool = True):
    ''' Take a snapshot of the active viewport

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param animation: Animation, Render files from the animation range of this scene
    :type animation: bool
    :param render_keyed_only: Render Keyframes Only, Render only those frames where selected objects have a key in their animation data. Only used when rendering animation
    :type render_keyed_only: bool
    :param sequencer: Sequencer, Render using the sequencer's OpenGL display
    :type sequencer: bool
    :param write_still: Write Image, Save rendered the image to the output path (used only when animation is disabled)
    :type write_still: bool
    :param view_context: View Context, Use the current 3D view for rendering, else use scene settings
    :type view_context: bool
    '''

    pass


def play_rendered_anim(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Play back rendered frames/movies using an external player :file: startup/bl_operators/screen_play_rendered_anim.py\:65 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/screen_play_rendered_anim.py$65> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def preset_add(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               name: str = "",
               remove_name: bool = False,
               remove_active: bool = False):
    ''' Add or remove a Render Preset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool
    :param remove_active: remove_active
    :type remove_active: bool
    '''

    pass


def render(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           animation: bool = False,
           write_still: bool = False,
           use_viewport: bool = False,
           layer: str = "",
           scene: str = ""):
    ''' Render active scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param animation: Animation, Render files from the animation range of this scene
    :type animation: bool
    :param write_still: Write Image, Save rendered the image to the output path (used only when animation is disabled)
    :type write_still: bool
    :param use_viewport: Use 3D Viewport, When inside a 3D viewport, use layers and camera of the viewport
    :type use_viewport: bool
    :param layer: Render Layer, Single render layer to re-render (used only when animation is disabled)
    :type layer: str
    :param scene: Scene, Scene to render, current scene if not specified
    :type scene: str
    '''

    pass


def shutter_curve_preset(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         shape: typing.Union[str, int] = 'SMOOTH'):
    ''' Set shutter curve

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param shape: Mode
    :type shape: typing.Union[str, int]
    '''

    pass


def view_cancel(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Cancel show render view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_show(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Toggle show render view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass
