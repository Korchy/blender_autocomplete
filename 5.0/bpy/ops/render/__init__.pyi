import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def color_management_white_balance_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add or remove a white balance preset

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def cycles_integrator_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add an Integrator Preset

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def cycles_performance_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add an Performance Preset

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def cycles_sampling_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add a Sampling Preset

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def cycles_viewport_sampling_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add a Viewport Sampling Preset

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def eevee_raytracing_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add or remove an EEVEE ray-tracing preset

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def opengl(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    animation: bool | None = False,
    render_keyed_only: bool | None = False,
    sequencer: bool | None = False,
    write_still: bool | None = False,
    view_context: bool | None = True,
) -> None:
    """Take a snapshot of the active viewport

    :param animation: Animation, Render files from the animation range of this scene
    :param render_keyed_only: Render Keyframes Only, Render only those frames where selected objects have a key in their animation data. Only used when rendering animation
    :param sequencer: Sequencer, Render using the sequencers OpenGL display
    :param write_still: Write Image, Save the rendered image to the output path (used only when animation is disabled)
    :param view_context: View Context, Use the current 3D view for rendering, else use scene settings
    """

def play_rendered_anim(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Play back rendered frames/movies using an external player"""

def preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add or remove a Render Preset

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def render(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    animation: bool | None = False,
    write_still: bool | None = False,
    use_viewport: bool | None = False,
    use_sequencer_scene: bool | None = False,
    layer: str = "",
    scene: str = "",
    frame_start: int | None = 0,
    frame_end: int | None = 0,
) -> None:
    """Undocumented, consider contributing.

    :param animation: Animation, Render files from the animation range of this scene
    :param write_still: Write Image, Save the rendered image to the output path (used only when animation is disabled)
    :param use_viewport: Use 3D Viewport, When inside a 3D viewport, use layers and camera of the viewport
    :param use_sequencer_scene: Use Sequencer Scene, Render the sequencer scene instead of the active scene
    :param layer: Render Layer, Single render layer to re-render (used only when animation is disabled)
    :param scene: Scene, Scene to render, current scene if not specified
    :param frame_start: Start Frame, Frame to start rendering animation at. If not specified, the scene start frame will be assumed. This should only be specified if doing an animation render
    :param frame_end: End Frame, Frame to end rendering animation at. If not specified, the scene end frame will be assumed. This should only be specified if doing an animation render
    """

def shutter_curve_preset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    shape: typing.Literal["SHARP", "SMOOTH", "MAX", "LINE", "ROUND", "ROOT"]
    | None = "SMOOTH",
) -> None:
    """Set shutter curve

    :param shape: Mode
    """

def view_cancel(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Cancel show render view"""

def view_show(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle show render view"""
