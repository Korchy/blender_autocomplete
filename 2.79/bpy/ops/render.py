import sys
import typing


def cycles_integrator_preset_add(name: str = "", remove_active: bool = False):
    '''Add an Integrator Preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: str
    :param remove_active: remove_active 
    :type remove_active: bool
    '''

    pass


def cycles_sampling_preset_add(name: str = "", remove_active: bool = False):
    '''Add a Sampling Preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: str
    :param remove_active: remove_active 
    :type remove_active: bool
    '''

    pass


def opengl(animation: bool = False,
           sequencer: bool = False,
           write_still: bool = False,
           view_context: bool = True):
    '''OpenGL render active viewport 

    :param animation: Animation, Render files from the animation range of this scene 
    :type animation: bool
    :param sequencer: Sequencer, Render using the sequencer’s OpenGL display 
    :type sequencer: bool
    :param write_still: Write Image, Save rendered the image to the output path (used only when animation is disabled) 
    :type write_still: bool
    :param view_context: View Context, Use the current 3D view for rendering, else use scene settings 
    :type view_context: bool
    '''

    pass


def play_rendered_anim():
    '''Play back rendered frames/movies using an external player 

    '''

    pass


def preset_add(name: str = "", remove_active: bool = False):
    '''Add or remove a Render Preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: str
    :param remove_active: remove_active 
    :type remove_active: bool
    '''

    pass


def render(animation: bool = False,
           write_still: bool = False,
           use_viewport: bool = False,
           layer: str = "",
           scene: str = ""):
    '''Render active scene 

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


def shutter_curve_preset(shape: int = 'SMOOTH'):
    '''Set shutter curve 

    :param shape: Mode 
    :type shape: int
    '''

    pass


def view_cancel():
    '''Cancel show render view 

    '''

    pass


def view_show():
    '''Toggle show render view 

    '''

    pass
