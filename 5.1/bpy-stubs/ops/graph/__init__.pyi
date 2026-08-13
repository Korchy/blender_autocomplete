import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums
import bpy.types

class bake_keys(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add keyframes on every frame between the selected keyframes

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class blend_offset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        factor: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Shift selected keys to the value of the neighboring keys as a block

        :param execution_context:
        :param undo:
        :param factor: Offset Factor, Control which key to offset towards and how far (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class blend_to_default(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        factor: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Blend selected keys to their default value from their current position

        :param execution_context:
        :param undo:
        :param factor: Factor, How much to blend to the default value (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class blend_to_ease(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        factor: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Blends keyframes from current state to an ease-in or ease-out curve

        :param execution_context:
        :param undo:
        :param factor: Blend, Favor either original data or ease curve (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class blend_to_neighbor(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        factor: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Blend selected keyframes to their left or right neighbor

        :param execution_context:
        :param undo:
        :param factor: Blend, The blend factor with 0 being the current frame (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class breakdown(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        factor: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move selected keyframes to an inbetween position relative to adjacent keys

        :param execution_context:
        :param undo:
        :param factor: Factor, Favor either the left or the right key (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class butterworth_smooth(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        cutoff_frequency: float | None = 3.0,
        filter_order: int | None = 4,
        samples_per_frame: int | None = 1,
        blend: float | None = 1.0,
        blend_in_out: int | None = 1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Smooth an F-Curve while maintaining the general shape of the curve

        :param execution_context:
        :param undo:
        :param cutoff_frequency: Frequency Cutoff (Hz), Lower values give a smoother curve (in [0, inf], optional)
        :param filter_order: Filter Order, Higher values produce a harder frequency cutoff (in [1, 32], optional)
        :param samples_per_frame: Samples per Frame, How many samples to calculate per frame, helps with subframe data (in [1, 64], optional)
        :param blend: Blend, How much to blend to the smoothed curve (in [0, inf], optional)
        :param blend_in_out: Blend In/Out, Linearly blend the smooth data to the border frames of the selection (in [0, inf], optional)
        :return: Result of the operator call.
        """

class clean(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        threshold: float | None = 0.001,
        channels: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Simplify F-Curves by removing closely spaced keyframes

        :param execution_context:
        :param undo:
        :param threshold: Threshold, (in [0, inf], optional)
        :param channels: Channels, (optional)
        :return: Result of the operator call.
        """

class click_insert(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        frame: float | None = 1.0,
        value: float | None = 1.0,
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Insert new keyframe at the cursor position for the active F-Curve

        :param execution_context:
        :param undo:
        :param frame: Frame Number, Frame to insert keyframe on (in [-inf, inf], optional)
        :param value: Value, Value for keyframe on (in [-inf, inf], optional)
        :param extend: Extend, Extend selection instead of deselecting everything first (optional)
        :return: Result of the operator call.
        """

class clickselect(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        wait_to_deselect_others: bool | None = False,
        use_select_on_click: bool | None = False,
        mouse_x: int | None = 0,
        mouse_y: int | None = 0,
        extend: bool | None = False,
        deselect_all: bool | None = False,
        column: bool | None = False,
        curves: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select keyframes by clicking on them

        :param execution_context:
        :param undo:
        :param wait_to_deselect_others: Wait to Deselect Others, (optional)
        :param use_select_on_click: Act on Click, Instead of selecting on mouse press, wait to see if theres drag event. Otherwise select on mouse release (optional)
        :param mouse_x: Mouse X, (in [-inf, inf], optional)
        :param mouse_y: Mouse Y, (in [-inf, inf], optional)
        :param extend: Extend Select, Toggle keyframe selection instead of leaving newly selected keyframes only (optional)
        :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor (optional)
        :param column: Column Select, Select all keyframes that occur on the same frame as the one under the mouse (optional)
        :param curves: Only Curves, Select all the keyframes in the curve (optional)
        :return: Result of the operator call.
        """

class copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy selected keyframes to the internal clipboard

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class cursor_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        frame: float | None = 0.0,
        value: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Interactively set the current frame and value cursor

        :param execution_context:
        :param undo:
        :param frame: Frame, (in [-1.04857e+06, 1.04857e+06], optional)
        :param value: Value, (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class decimate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["RATIO", "ERROR"] | None = "RATIO",
        factor: float | None = 0.333333,
        remove_error_margin: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Decimate F-Curves by removing keyframes that influence the curve shape the least

                :param execution_context:
                :param undo:
                :param mode: Mode, Which mode to use for decimation (optional)

        RATIO
        Ratio -- Use a percentage to specify how many keyframes you want to remove.

        ERROR
        Error Margin -- Use an error margin to specify how much the curve is allowed to deviate from the original path.
                :param factor: Factor, The ratio of keyframes to remove (in [0, 1], optional)
                :param remove_error_margin: Max Error Margin, How much the new decimated curve is allowed to deviate from the original (in [0, inf], optional)
                :return: Result of the operator call.
        """

class delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        confirm: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove all selected keyframes

        :param execution_context:
        :param undo:
        :param confirm: Confirm, Prompt for confirmation (optional)
        :return: Result of the operator call.
        """

class driver_delete_invalid(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete all visible drivers considered invalid

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class driver_variables_copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy the driver variables of the active driver

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class driver_variables_paste(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        replace: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add copied driver variables to the active driver

        :param execution_context:
        :param undo:
        :param replace: Replace Existing, Replace existing driver variables, instead of just appending to the end of the existing list (optional)
        :return: Result of the operator call.
        """

class duplicate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal[bpy.stub_internal.rna_enums.TransformModeTypeItems]
        | None = "TRANSLATION",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make a copy of all selected keyframes

        :param execution_context:
        :param undo:
        :param mode: Mode, (optional)
        :return: Result of the operator call.
        """

class duplicate_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        GRAPH_OT_duplicate: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make a copy of all selected keyframes and move them

        :param execution_context:
        :param undo:
        :param GRAPH_OT_duplicate: Duplicate Keyframes, Make a copy of all selected keyframes (optional, `bpy.ops.graph.duplicate` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class ease(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        factor: float | None = 0.0,
        sharpness: float | None = 2.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Align keyframes on a ease-in or ease-out curve

        :param execution_context:
        :param undo:
        :param factor: Curve Bend, Defines if the keys should be aligned on an ease-in or ease-out curve (in [-inf, inf], optional)
        :param sharpness: Sharpness, Higher values make the change more abrupt (in [0.001, inf], optional)
        :return: Result of the operator call.
        """

class easing_type(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            bpy.stub_internal.rna_enums.BeztripleInterpolationEasingItems
        ]
        | None = "AUTO",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set easing type for the F-Curve segments starting from the selected keyframes

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class equalize_handles(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        side: typing.Literal["LEFT", "RIGHT", "BOTH"] | None = "LEFT",
        handle_length: float | None = 5.0,
        flatten: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Ensure selected keyframes handles have equal length, optionally making them horizontal. Automatic, Automatic Clamped, or Vector handle types will be converted to Aligned

                :param execution_context:
                :param undo:
                :param side: Side, Side of the keyframes Bézier handles to affect (optional)

        LEFT
        Left -- Equalize selected keyframes left handles.

        RIGHT
        Right -- Equalize selected keyframes right handles.

        BOTH
        Both -- Equalize both of a keyframes handles.
                :param handle_length: Handle Length, Length to make selected keyframes Bézier handles (in [0.1, inf], optional)
                :param flatten: Flatten, Make the values of the selected keyframes handles the same as their respective keyframes (optional)
                :return: Result of the operator call.
        """

class euler_filter(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Fix large jumps and flips in the selected Euler Rotation F-Curves arising from rotation values being clipped when baking physics

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class extrapolation_type(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["CONSTANT", "LINEAR", "MAKE_CYCLIC", "CLEAR_CYCLIC"]
        | None = "CONSTANT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set extrapolation mode for selected F-Curves

                :param execution_context:
                :param undo:
                :param type: Type, (optional)

        CONSTANT
        Constant Extrapolation -- Values on endpoint keyframes are held.

        LINEAR
        Linear Extrapolation -- Straight-line slope of end segments are extended past the endpoint keyframes.

        MAKE_CYCLIC
        Make Cyclic (F-Modifier) -- Add Cycles F-Modifier if one does not exist already.

        CLEAR_CYCLIC
        Clear Cyclic (F-Modifier) -- Remove Cycles F-Modifier if not needed anymore.
                :return: Result of the operator call.
        """

class fmodifier_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[bpy.stub_internal.rna_enums.FmodifierTypeItems]
        | None = "NULL",
        only_active: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add F-Modifier to the active/selected F-Curves

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :param only_active: Only Active, Only add F-Modifier to active F-Curve (optional)
        :return: Result of the operator call.
        """

class fmodifier_copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy the F-Modifier(s) of the active F-Curve

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class fmodifier_paste(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        only_active: bool | None = False,
        replace: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add copied F-Modifiers to the selected F-Curves

        :param execution_context:
        :param undo:
        :param only_active: Only Active, Only paste F-Modifiers on active F-Curve (optional)
        :param replace: Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list (optional)
        :return: Result of the operator call.
        """

class frame_jump(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Place the cursor on the midpoint of selected keyframes

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class gaussian_smooth(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        factor: float | None = 1.0,
        sigma: float | None = 0.33,
        filter_width: int | None = 6,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Smooth the curve using a Gaussian filter

        :param execution_context:
        :param undo:
        :param factor: Factor, How much to blend to the default value (in [0, inf], optional)
        :param sigma: Sigma, The shape of the gaussian distribution, lower values make it sharper (in [0.001, inf], optional)
        :param filter_width: Filter Width, How far to each side the operator will average the key values (in [1, 64], optional)
        :return: Result of the operator call.
        """

class ghost_curves_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear F-Curve snapshots (Ghosts) for active Graph Editor

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class ghost_curves_create(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create snapshot (Ghosts) of selected F-Curves as background aid for active Graph Editor

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class handle_type(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[bpy.stub_internal.rna_enums.KeyframeHandleTypeItems]
        | None = "FREE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set type of handle for selected keyframes

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class hide(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        unselected: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Hide selected curves from Graph Editor view

        :param execution_context:
        :param undo:
        :param unselected: Unselected, Hide unselected rather than selected curves (optional)
        :return: Result of the operator call.
        """

class interpolation_type(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            bpy.stub_internal.rna_enums.BeztripleInterpolationModeItems
        ]
        | None = "CONSTANT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set interpolation mode for the F-Curve segments starting from the selected keyframes

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class keyframe_insert(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["ALL", "SEL", "ACTIVE", "CURSOR_ACTIVE", "CURSOR_SEL"]
        | None = "ALL",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Insert keyframes for the specified channels

                :param execution_context:
                :param undo:
                :param type: Type, (optional)

        ALL
        All Channels -- Insert a keyframe on all visible and editable F-Curves using each curves current value.

        SEL
        Only Selected Channels -- Insert a keyframe on selected F-Curves using each curves current value.

        ACTIVE
        Only Active F-Curve -- Insert a keyframe on the active F-Curve using the curves current value.

        CURSOR_ACTIVE
        Active Channels at Cursor -- Insert a keyframe for the active F-Curve at the cursor point.

        CURSOR_SEL
        Selected Channels at Cursor -- Insert a keyframe for selected F-Curves at the cursor point.
                :return: Result of the operator call.
        """

class keyframe_jump(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        next: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Jump to previous/next keyframe

        :param execution_context:
        :param undo:
        :param next: Next Keyframe, (optional)
        :return: Result of the operator call.
        """

class keys_to_samples(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Convert selected channels to an uneditable set of samples to save storage space

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class match_slope(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        factor: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Blend selected keys to the slope of neighboring ones

        :param execution_context:
        :param undo:
        :param factor: Factor, Defines which keys to use as slope and how much to blend towards them (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class mirror(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["CFRA", "VALUE", "YAXIS", "XAXIS", "MARKER"]
        | None = "CFRA",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Flip selected keyframes over the selected mirror line

                :param execution_context:
                :param undo:
                :param type: Type, (optional)

        CFRA
        By Times Over Current Frame -- Flip times of selected keyframes using the current frame as the mirror line.

        VALUE
        By Values Over Cursor Value -- Flip values of selected keyframes using the cursor value (Y/Horizontal component) as the mirror line.

        YAXIS
        By Times Over Zero Time -- Flip times of selected keyframes, effectively reversing the order they appear in.

        XAXIS
        By Values Over Zero Value -- Flip values of selected keyframes (i.e. negative values become positive, and vice versa).

        MARKER
        By Times Over First Selected Marker -- Flip times of selected keyframes using the first selected marker as the reference point.
                :return: Result of the operator call.
        """

class paste(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        offset: typing.Literal[bpy.stub_internal.rna_enums.KeyframePasteOffsetItems]
        | None = "START",
        value_offset: typing.Literal[
            bpy.stub_internal.rna_enums.KeyframePasteOffsetValueItems
        ]
        | None = "NONE",
        merge: typing.Literal[bpy.stub_internal.rna_enums.KeyframePasteMergeItems]
        | None = "MIX",
        flipped: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Paste keyframes from the internal clipboard for the selected channels, starting on the current frame

        :param execution_context:
        :param undo:
        :param offset: Frame Offset, Paste time offset of keys (optional)
        :param value_offset: Value Offset, Paste keys with a value offset (optional)
        :param merge: Type, Method of merging pasted keys and existing (optional)
        :param flipped: Flipped, Paste keyframes from mirrored bones if they exist (optional)
        :return: Result of the operator call.
        """

class previewrange_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set Preview Range based on range of selected keyframes

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class push_pull(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        factor: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Exaggerate or minimize the value of the selected keys

        :param execution_context:
        :param undo:
        :param factor: Factor, Control how far to push or pull the keys (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class reveal(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        select: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make previously hidden curves visible again in Graph Editor view

        :param execution_context:
        :param undo:
        :param select: Select, (optional)
        :return: Result of the operator call.
        """

class samples_to_keys(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Convert selected channels from samples to keyframes

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class scale_average(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        factor: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Scale selected key values by their combined average

        :param execution_context:
        :param undo:
        :param factor: Scale Factor, The scale factor applied to the curve segments (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class scale_from_neighbor(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        factor: float | None = 0.0,
        anchor: typing.Literal["LEFT", "RIGHT"] | None = "LEFT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Increase or decrease the value of selected keys in relationship to the neighboring one

        :param execution_context:
        :param undo:
        :param factor: Factor, The factor to scale keys with (in [-inf, inf], optional)
        :param anchor: Reference Key, Which end of the segment to use as a reference to scale from (optional)
        :return: Result of the operator call.
        """

class select_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"]
        | None = "TOGGLE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Toggle selection of all keyframes

                :param execution_context:
                :param undo:
                :param action: Action, Selection action to execute (optional)

        TOGGLE
        Toggle -- Toggle selection for all elements.

        SELECT
        Select -- Select all elements.

        DESELECT
        Deselect -- Deselect all elements.

        INVERT
        Invert -- Invert selection of all elements.
                :return: Result of the operator call.
        """

class select_box(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        axis_range: bool | None = False,
        include_handles: bool | None = True,
        tweak: bool | None = False,
        use_curve_selection: bool | None = True,
        xmin: int | None = 0,
        xmax: int | None = 0,
        ymin: int | None = 0,
        ymax: int | None = 0,
        wait_for_input: bool | None = True,
        mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all keyframes within the specified region

                :param execution_context:
                :param undo:
                :param axis_range: Axis Range, (optional)
                :param include_handles: Include Handles, Are handles tested individually against the selection criteria, independently from their keys. When unchecked, handles are (de)selected in unison with their keys (optional)
                :param tweak: Tweak, Operator has been activated using a click-drag event (optional)
                :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the calculated F-curve (optional)
                :param xmin: X Min, (in [-inf, inf], optional)
                :param xmax: X Max, (in [-inf, inf], optional)
                :param ymin: Y Min, (in [-inf, inf], optional)
                :param ymax: Y Max, (in [-inf, inf], optional)
                :param wait_for_input: Wait for Input, (optional)
                :param mode: Mode, (optional)

        SET
        Set -- Set a new selection.

        ADD
        Extend -- Extend existing selection.

        SUB
        Subtract -- Subtract existing selection.
                :return: Result of the operator call.
        """

class select_circle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        x: int | None = 0,
        y: int | None = 0,
        radius: int | None = 25,
        wait_for_input: bool | None = True,
        mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
        include_handles: bool | None = True,
        use_curve_selection: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select keyframe points using circle selection

                :param execution_context:
                :param undo:
                :param x: X, (in [-inf, inf], optional)
                :param y: Y, (in [-inf, inf], optional)
                :param radius: Radius, (in [1, inf], optional)
                :param wait_for_input: Wait for Input, (optional)
                :param mode: Mode, (optional)

        SET
        Set -- Set a new selection.

        ADD
        Extend -- Extend existing selection.

        SUB
        Subtract -- Subtract existing selection.
                :param include_handles: Include Handles, Are handles tested individually against the selection criteria, independently from their keys. When unchecked, handles are (de)selected in unison with their keys (optional)
                :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself (optional)
                :return: Result of the operator call.
        """

class select_column(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["KEYS", "CFRA", "MARKERS_COLUMN", "MARKERS_BETWEEN"]
        | None = "KEYS",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all keyframes on the specified frame(s)

        :param execution_context:
        :param undo:
        :param mode: Mode, (optional)
        :return: Result of the operator call.
        """

class select_key_handles(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        left_handle_action: typing.Literal["SELECT", "DESELECT", "KEEP"]
        | None = "SELECT",
        right_handle_action: typing.Literal["SELECT", "DESELECT", "KEEP"]
        | None = "SELECT",
        key_action: typing.Literal["SELECT", "DESELECT", "KEEP"] | None = "KEEP",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """For selected keyframes, select/deselect any combination of the key itself and its handles

                :param execution_context:
                :param undo:
                :param left_handle_action: Left Handle, Effect on the left handle (optional)

        SELECT
        Select.

        DESELECT
        Deselect.

        KEEP
        Keep -- Leave as is.
                :param right_handle_action: Right Handle, Effect on the right handle (optional)

        SELECT
        Select.

        DESELECT
        Deselect.

        KEEP
        Keep -- Leave as is.
                :param key_action: Key, Effect on the key itself (optional)

        SELECT
        Select.

        DESELECT
        Deselect.

        KEEP
        Keep -- Leave as is.
                :return: Result of the operator call.
        """

class select_lasso(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
        use_smooth_stroke: bool | None = False,
        smooth_stroke_factor: float | None = 0.75,
        smooth_stroke_radius: int | None = 35,
        mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
        include_handles: bool | None = True,
        use_curve_selection: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select keyframe points using lasso selection

                :param execution_context:
                :param undo:
                :param path: Path, (optional)
                :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path (optional)
                :param smooth_stroke_factor: Smooth Stroke Factor, Higher values give a smoother stroke (in [0.5, 0.99], optional)
                :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues (in [10, 200], optional)
                :param mode: Mode, (optional)

        SET
        Set -- Set a new selection.

        ADD
        Extend -- Extend existing selection.

        SUB
        Subtract -- Subtract existing selection.
                :param include_handles: Include Handles, Are handles tested individually against the selection criteria, independently from their keys. When unchecked, handles are (de)selected in unison with their keys (optional)
                :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself (optional)
                :return: Result of the operator call.
        """

class select_leftright(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["CHECK", "LEFT", "RIGHT"] | None = "CHECK",
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select keyframes to the left or the right of the current frame

        :param execution_context:
        :param undo:
        :param mode: Mode, (optional)
        :param extend: Extend Select, (optional)
        :return: Result of the operator call.
        """

class select_less(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Deselect keyframes on ends of selection islands

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_linked(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select keyframes occurring in the same F-Curves as selected ones

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_more(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select keyframes beside already selected ones

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class shear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        factor: float | None = 0.0,
        direction: typing.Literal["FROM_LEFT", "FROM_RIGHT"] | None = "FROM_LEFT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Affect the value of the keys linearly, keeping the same relationship between them using either the left or the right key as reference

                :param execution_context:
                :param undo:
                :param factor: Shear Factor, The amount of shear to apply (in [-inf, inf], optional)
                :param direction: Direction, Which end of the segment to use as a reference to shear from (optional)

        FROM_LEFT
        From Left -- Shear the keys using the left key as reference.

        FROM_RIGHT
        From Right -- Shear the keys using the right key as reference.
                :return: Result of the operator call.
        """

class smooth(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Apply weighted moving means to make selected F-Curves less bumpy

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class snap(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            "CFRA",
            "VALUE",
            "NEAREST_FRAME",
            "NEAREST_SECOND",
            "NEAREST_MARKER",
            "HORIZONTAL",
        ]
        | None = "CFRA",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Snap selected keyframes to the chosen times/values

                :param execution_context:
                :param undo:
                :param type: Type, (optional)

        CFRA
        Selection to Current Frame -- Snap selected keyframes to the current frame.

        VALUE
        Selection to Cursor Value -- Set values of selected keyframes to the cursor value (Y/Horizontal component).

        NEAREST_FRAME
        Selection to Nearest Frame -- Snap selected keyframes to the nearest (whole) frame (use to fix accidental subframe offsets).

        NEAREST_SECOND
        Selection to Nearest Second -- Snap selected keyframes to the nearest second.

        NEAREST_MARKER
        Selection to Nearest Marker -- Snap selected keyframes to the nearest marker.

        HORIZONTAL
        Flatten Handles -- Flatten handles for a smoother transition.
                :return: Result of the operator call.
        """

class snap_cursor_value(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Place the cursor value on the average value of selected keyframes

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class sound_to_samples(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        check_existing: bool | None = False,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = True,
        filter_python: bool | None = False,
        filter_font: bool | None = False,
        filter_sound: bool | None = True,
        filter_text: bool | None = False,
        filter_archive: bool | None = False,
        filter_btx: bool | None = False,
        filter_alembic: bool | None = False,
        filter_usd: bool | None = False,
        filter_obj: bool | None = False,
        filter_volume: bool | None = False,
        filter_folder: bool | None = True,
        filter_blenlib: bool | None = False,
        filemode: int | None = 9,
        show_multiview: bool | None = False,
        use_multiview: bool | None = False,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        low: float | None = 0.0,
        high: float | None = 100000.0,
        attack: float | None = 0.005,
        release: float | None = 0.2,
        threshold: float | None = 0.0,
        use_accumulate: bool | None = False,
        use_additive: bool | None = False,
        use_square: bool | None = False,
        sthreshold: float | None = 0.1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Bakes a sound wave to samples on selected channels

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
                :param filter_blender: Filter .blend files, (optional)
                :param filter_backup: Filter backup .blend files, (optional)
                :param filter_image: Filter image files, (optional)
                :param filter_movie: Filter movie files, (optional)
                :param filter_python: Filter Python files, (optional)
                :param filter_font: Filter font files, (optional)
                :param filter_sound: Filter sound files, (optional)
                :param filter_text: Filter text files, (optional)
                :param filter_archive: Filter archive files, (optional)
                :param filter_btx: Filter btx files, (optional)
                :param filter_alembic: Filter Alembic files, (optional)
                :param filter_usd: Filter USD files, (optional)
                :param filter_obj: Filter OBJ files, (optional)
                :param filter_volume: Filter OpenVDB volume files, (optional)
                :param filter_folder: Filter folders, (optional)
                :param filter_blenlib: Filter Blender IDs, (optional)
                :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
                :param show_multiview: Enable Multi-View, (optional)
                :param use_multiview: Use Multi-View, (optional)
                :param display_type: Display Type, (optional)

        DEFAULT
        Default -- Automatically determine display type for files.

        LIST_VERTICAL
        Short List -- Display files as short list.

        LIST_HORIZONTAL
        Long List -- Display files as a detailed list.

        THUMBNAIL
        Thumbnails -- Display files as thumbnails.
                :param sort_method: File sorting mode, (optional)
                :param low: Lowest Frequency, Cutoff frequency of a high-pass filter that is applied to the audio data (in [0, 100000], optional)
                :param high: Highest Frequency, Cutoff frequency of a low-pass filter that is applied to the audio data (in [0, 100000], optional)
                :param attack: Attack Time, Value for the envelope calculation that tells how fast the envelope can rise (the lower the value the steeper it can rise) (in [0, 2], optional)
                :param release: Release Time, Value for the envelope calculation that tells how fast the envelope can fall (the lower the value the steeper it can fall) (in [0, 5], optional)
                :param threshold: Threshold, Minimum amplitude value needed to influence the envelope (in [0, 1], optional)
                :param use_accumulate: Accumulate, Only the positive differences of the envelope amplitudes are summarized to produce the output (optional)
                :param use_additive: Additive, The amplitudes of the envelope are summarized (or, when Accumulate is enabled, both positive and negative differences are accumulated) (optional)
                :param use_square: Square, The output is a square curve (negative values always result in -1, and positive ones in 1) (optional)
                :param sthreshold: Square Threshold, Square only: all values with an absolute amplitude lower than that result in 0 (in [0, 1], optional)
                :return: Result of the operator call.
        """

class time_offset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        frame_offset: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Shifts the value of selected keys in time

        :param execution_context:
        :param undo:
        :param frame_offset: Frame Offset, How far in frames to offset the animation (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class view_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        include_handles: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset viewable area to show full keyframe range

        :param execution_context:
        :param undo:
        :param include_handles: Include Handles, Include handles of keyframes when calculating extents (optional)
        :return: Result of the operator call.
        """

class view_frame(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move the view to the current frame

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_selected(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        include_handles: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset viewable area to show selected keyframe range

        :param execution_context:
        :param undo:
        :param include_handles: Include Handles, Include handles of keyframes when calculating extents (optional)
        :return: Result of the operator call.
        """
