import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class clear_texture_cache(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete Cycles texture cache files from disk

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class color_management_white_balance_preset_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        remove_name: bool | None = False,
        remove_active: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add or remove a white balance preset

        :param execution_context:
        :param undo:
        :param name: Name, Name of the preset, used to make the path name (optional, never None)
        :param remove_name: remove_name, (optional)
        :param remove_active: remove_active, (optional)
        :return: Result of the operator call.
        """

class cycles_integrator_preset_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        remove_name: bool | None = False,
        remove_active: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add an Integrator Preset

        :param execution_context:
        :param undo:
        :param name: Name, Name of the preset, used to make the path name (optional, never None)
        :param remove_name: remove_name, (optional)
        :param remove_active: remove_active, (optional)
        :return: Result of the operator call.
        """

class cycles_performance_preset_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        remove_name: bool | None = False,
        remove_active: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add an Performance Preset

        :param execution_context:
        :param undo:
        :param name: Name, Name of the preset, used to make the path name (optional, never None)
        :param remove_name: remove_name, (optional)
        :param remove_active: remove_active, (optional)
        :return: Result of the operator call.
        """

class cycles_sampling_preset_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        remove_name: bool | None = False,
        remove_active: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a Sampling Preset

        :param execution_context:
        :param undo:
        :param name: Name, Name of the preset, used to make the path name (optional, never None)
        :param remove_name: remove_name, (optional)
        :param remove_active: remove_active, (optional)
        :return: Result of the operator call.
        """

class cycles_viewport_sampling_preset_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        remove_name: bool | None = False,
        remove_active: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a Viewport Sampling Preset

        :param execution_context:
        :param undo:
        :param name: Name, Name of the preset, used to make the path name (optional, never None)
        :param remove_name: remove_name, (optional)
        :param remove_active: remove_active, (optional)
        :return: Result of the operator call.
        """

class eevee_raytracing_preset_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        remove_name: bool | None = False,
        remove_active: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add or remove an EEVEE ray-tracing preset

        :param execution_context:
        :param undo:
        :param name: Name, Name of the preset, used to make the path name (optional, never None)
        :param remove_name: remove_name, (optional)
        :param remove_active: remove_active, (optional)
        :return: Result of the operator call.
        """

class generate_texture_cache(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        generate_sequences: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Generate Cycles texture cache files for all images used in shader nodes

        :param execution_context:
        :param undo:
        :param generate_sequences: Image Sequences, Generate texture cache files for all frames of image sequences (optional)
        :return: Result of the operator call.
        """

class opengl(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        animation: bool | None = False,
        render_keyed_only: bool | None = False,
        sequencer: bool | None = False,
        write_still: bool | None = False,
        view_context: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Take a snapshot of the active viewport

        :param execution_context:
        :param undo:
        :param animation: Animation, Render files from the animation range of this scene (optional)
        :param render_keyed_only: Render Keyframes Only, Render only those frames where selected objects have a key in their animation data. Only used when rendering animation (optional)
        :param sequencer: Sequencer, Render using the sequencers OpenGL display (optional)
        :param write_still: Write Image, Save the rendered image to the output path (used only when animation is disabled) (optional)
        :param view_context: View Context, Use the current 3D view for rendering, else use scene settings (optional)
        :return: Result of the operator call.
        """

class play_rendered_anim(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Play back rendered frames/movies using an external player

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class preset_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        remove_name: bool | None = False,
        remove_active: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add or remove a Render Preset

        :param execution_context:
        :param undo:
        :param name: Name, Name of the preset, used to make the path name (optional, never None)
        :param remove_name: remove_name, (optional)
        :param remove_active: remove_active, (optional)
        :return: Result of the operator call.
        """

class render(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param animation: Animation, Render files from the animation range of this scene (optional)
        :param write_still: Write Image, Save the rendered image to the output path (used only when animation is disabled) (optional)
        :param use_viewport: Use 3D Viewport, When inside a 3D viewport, use layers and camera of the viewport (optional)
        :param use_sequencer_scene: Use Sequencer Scene, Render the sequencer scene instead of the active scene (optional)
        :param layer: Render Layer, Single render layer to re-render (used only when animation is disabled) (optional, never None)
        :param scene: Scene, Scene to render, current scene if not specified (optional, never None)
        :param frame_start: Start Frame, Frame to start rendering animation at. If not specified, the scene start frame will be assumed. This should only be specified if doing an animation render (in [-inf, inf], optional)
        :param frame_end: End Frame, Frame to end rendering animation at. If not specified, the scene end frame will be assumed. This should only be specified if doing an animation render (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class shutter_curve_preset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        shape: typing.Literal["SHARP", "SMOOTH", "MAX", "LINE", "ROUND", "ROOT"]
        | None = "SMOOTH",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set shutter curve

        :param execution_context:
        :param undo:
        :param shape: Mode, (optional)
        :return: Result of the operator call.
        """

class swap_dimensions(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Flip X and Y resolutions

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_cancel(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Cancel showing the render view

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_show(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Toggle show render view

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
