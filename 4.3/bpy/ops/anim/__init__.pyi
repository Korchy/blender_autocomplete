import typing
import collections.abc
import typing_extensions

def change_frame(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame: float | None = 0.0,
    snap: bool | None = False,
):
    """Interactively change the current frame number

    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame: Frame
    :type frame: float | None
    :param snap: Snap
    :type snap: bool | None
    """

def channel_select_keys(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
):
    """Select all keyframes of channel under mouse

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection
    :type extend: bool | None
    """

def channel_view_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    include_handles: bool | None = True,
    use_preview_range: bool | None = True,
):
    """Reset viewable area to show the channel under the cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    :type include_handles: bool | None
    :param use_preview_range: Use Preview Range, Ignore frames outside of the preview range
    :type use_preview_range: bool | None
    """

def channels_bake(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    range: collections.abc.Iterable[int] | None = (0, 0),
    step: float | None = 1.0,
    remove_outside_range: bool | None = False,
    interpolation_type: typing.Literal["BEZIER", "LIN", "CONST"] | None = "BEZIER",
    bake_modifiers: bool | None = True,
):
    """Create keyframes following the current shape of F-Curves of selected channels

        :type execution_context: int | str | None
        :type undo: bool | None
        :param range: Frame Range, The range in which to create new keys
        :type range: collections.abc.Iterable[int] | None
        :param step: Frame Step, At which interval to add keys
        :type step: float | None
        :param remove_outside_range: Remove Outside Range, Removes keys outside the given range, leaving only the newly baked
        :type remove_outside_range: bool | None
        :param interpolation_type: Interpolation Type, Choose the interpolation type with which new keys will be added

    BEZIER
    Bézier -- New keys will be Bézier.

    LIN
    Linear -- New keys will be linear.

    CONST
    Constant -- New keys will be constant.
        :type interpolation_type: typing.Literal['BEZIER','LIN','CONST'] | None
        :param bake_modifiers: Bake Modifiers, Bake Modifiers into keyframes and delete them after
        :type bake_modifiers: bool | None
    """

def channels_clean_empty(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Delete all empty animation data containers from visible data-blocks

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def channels_click(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    extend_range: bool | None = False,
    children_only: bool | None = False,
):
    """Handle mouse clicks over animation channels

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend Select
    :type extend: bool | None
    :param extend_range: Extend Range, Selection of active channel to clicked channel
    :type extend_range: bool | None
    :param children_only: Select Children Only
    :type children_only: bool | None
    """

def channels_collapse(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
):
    """Collapse (close) all selected expandable animation channels

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All, Collapse all channels (not just selected ones)
    :type all: bool | None
    """

def channels_delete(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Delete all selected animation channels

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def channels_editable_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["TOGGLE", "DISABLE", "ENABLE", "INVERT"] | None = "TOGGLE",
    type: typing.Literal["PROTECT", "MUTE"] | None = "PROTECT",
):
    """Toggle editability of selected channels

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['TOGGLE','DISABLE','ENABLE','INVERT'] | None
    :param type: Type
    :type type: typing.Literal['PROTECT','MUTE'] | None
    """

def channels_expand(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
):
    """Expand (open) all selected expandable animation channels

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All, Expand all channels (not just selected ones)
    :type all: bool | None
    """

def channels_fcurves_enable(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Clear 'disabled' tag from all F-Curves to get broken F-Curves working again

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def channels_group(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "New Group",
):
    """Add selected F-Curves to a new group

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of newly created group
    :type name: str
    """

def channels_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["TOP", "UP", "DOWN", "BOTTOM"] | None = "DOWN",
):
    """Rearrange selected animation channels

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction
    :type direction: typing.Literal['TOP','UP','DOWN','BOTTOM'] | None
    """

def channels_rename(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Rename animation channel under mouse

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def channels_select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Toggle selection of all animation channels

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
        :type action: typing.Literal['TOGGLE','SELECT','DESELECT','INVERT'] | None
    """

def channels_select_box(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    deselect: bool | None = False,
    extend: bool | None = True,
):
    """Select all animation channels within the specified region

    :type execution_context: int | str | None
    :type undo: bool | None
    :param xmin: X Min
    :type xmin: int | None
    :param xmax: X Max
    :type xmax: int | None
    :param ymin: Y Min
    :type ymin: int | None
    :param ymax: Y Max
    :type ymax: int | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | None
    :param deselect: Deselect, Deselect rather than select items
    :type deselect: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | None
    """

def channels_select_filter(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Start entering text which filters the set of channels shown to only include those with matching names

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def channels_setting_disable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["TOGGLE", "DISABLE", "ENABLE", "INVERT"] | None = "DISABLE",
    type: typing.Literal["PROTECT", "MUTE"] | None = "PROTECT",
):
    """Disable specified setting on all selected animation channels

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['TOGGLE','DISABLE','ENABLE','INVERT'] | None
    :param type: Type
    :type type: typing.Literal['PROTECT','MUTE'] | None
    """

def channels_setting_enable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["TOGGLE", "DISABLE", "ENABLE", "INVERT"] | None = "ENABLE",
    type: typing.Literal["PROTECT", "MUTE"] | None = "PROTECT",
):
    """Enable specified setting on all selected animation channels

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['TOGGLE','DISABLE','ENABLE','INVERT'] | None
    :param type: Type
    :type type: typing.Literal['PROTECT','MUTE'] | None
    """

def channels_setting_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["TOGGLE", "DISABLE", "ENABLE", "INVERT"] | None = "TOGGLE",
    type: typing.Literal["PROTECT", "MUTE"] | None = "PROTECT",
):
    """Toggle specified setting on all selected animation channels

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['TOGGLE','DISABLE','ENABLE','INVERT'] | None
    :param type: Type
    :type type: typing.Literal['PROTECT','MUTE'] | None
    """

def channels_ungroup(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove selected F-Curves from their current groups

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def channels_view_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    include_handles: bool | None = True,
    use_preview_range: bool | None = True,
):
    """Reset viewable area to show the selected channels

    :type execution_context: int | str | None
    :type undo: bool | None
    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    :type include_handles: bool | None
    :param use_preview_range: Use Preview Range, Ignore frames outside of the preview range
    :type use_preview_range: bool | None
    """

def clear_useless_actions(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_unused: bool | None = True,
):
    """Mark actions with no F-Curves for deletion after save and reload of file preserving "action libraries"

    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_unused: Only Unused, Only unused (Fake User only) actions get considered
    :type only_unused: bool | None
    """

def convert_legacy_action(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Convert a legacy Action to a layered Action on the active object

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def copy_driver_button(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Copy the driver for the highlighted button

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def driver_button_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add driver for the property under the cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def driver_button_edit(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Edit the drivers for the connected property represented by the highlighted button

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def driver_button_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
):
    """Remove the driver(s) for the connected property(s) represented by the highlighted button

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All, Delete drivers for all elements of the array
    :type all: bool | None
    """

def end_frame_set(execution_context: int | str | None = None, undo: bool | None = None):
    """Set the current frame as the preview or scene end frame

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def keyframe_clear_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
):
    """Clear all keyframes on the currently active property

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All, Clear keyframes from all elements of the array
    :type all: bool | None
    """

def keyframe_clear_v3d(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
):
    """Remove all keyframe animation for selected objects

    :type execution_context: int | str | None
    :type undo: bool | None
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool | None
    """

def keyframe_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "DEFAULT",
):
    """Delete keyframes on the current frame for all properties in the specified Keying Set

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Keying Set, The Keying Set to use
    :type type: str | None
    """

def keyframe_delete_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
):
    """Delete current keyframe of current UI-active property

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All, Delete keyframes from all elements of the array
    :type all: bool | None
    """

def keyframe_delete_by_name(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str = "",
):
    """Alternate access to 'Delete Keyframe' for keymaps to use

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Keying Set, The Keying Set to use
    :type type: str
    """

def keyframe_delete_v3d(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
):
    """Remove keyframes on current frame for selected objects and bones

    :type execution_context: int | str | None
    :type undo: bool | None
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool | None
    """

def keyframe_insert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "DEFAULT",
):
    """Insert keyframes on the current frame using either the active keying set, or the user preferences if no keying set is active

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Keying Set, The Keying Set to use
    :type type: str | None
    """

def keyframe_insert_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
):
    """Insert a keyframe for current UI-active property

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All, Insert a keyframe for all element of the array
    :type all: bool | None
    """

def keyframe_insert_by_name(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str = "",
):
    """Alternate access to 'Insert Keyframe' for keymaps to use

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Keying Set, The Keying Set to use
    :type type: str
    """

def keyframe_insert_menu(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "DEFAULT",
    always_prompt: bool | None = False,
):
    """Insert Keyframes for specified Keying Set, with menu of available Keying Sets if undefined

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Keying Set, The Keying Set to use
    :type type: str | None
    :param always_prompt: Always Show Menu
    :type always_prompt: bool | None
    """

def keying_set_active_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "DEFAULT",
):
    """Set a new active keying set

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Keying Set, The Keying Set to use
    :type type: str | None
    """

def keying_set_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add a new (empty) keying set to the active Scene

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def keying_set_export(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    filter_folder: bool | None = True,
    filter_text: bool | None = True,
    filter_python: bool | None = True,
):
    """Export Keying Set to a Python script

    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str
    :param filter_folder: Filter folders
    :type filter_folder: bool | None
    :param filter_text: Filter text
    :type filter_text: bool | None
    :param filter_python: Filter Python
    :type filter_python: bool | None
    """

def keying_set_path_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add empty path to active keying set

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def keying_set_path_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove active Path from active keying set

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def keying_set_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove the active keying set

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def keyingset_button_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
):
    """Add current UI-active property to current keying set

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All, Add all elements of the array to a Keying Set
    :type all: bool | None
    """

def keyingset_button_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove current UI-active property from current keying set

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def merge_animation(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Merge the animation of the selected objects into the action of the active object. Actions are not deleted by this, but might end up with zero users

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def paste_driver_button(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Paste the driver in the internal clipboard to the highlighted button

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def previewrange_clear(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Clear preview range

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def previewrange_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
):
    """Interactively define frame range used for playback

    :type execution_context: int | str | None
    :type undo: bool | None
    :param xmin: X Min
    :type xmin: int | None
    :param xmax: X Max
    :type xmax: int | None
    :param ymin: Y Min
    :type ymin: int | None
    :param ymax: Y Max
    :type ymax: int | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | None
    """

def scene_range_frame(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Reset the horizontal view to the current scene frame range, taking the preview range into account if it is active

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def slot_new_for_id(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Create a new action slot for this data-block, to hold its animation

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def slot_new_for_object(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Create a new Slot for this object, on the Action already assigned to it

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def slot_unassign_from_constraint(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Un-assign the action slot from this constraint

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def slot_unassign_from_id(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Un-assign the action slot, effectively making this data-block non-animated

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def slot_unassign_from_nla_strip(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Un-assign the action slot from this NLA strip, effectively making it non-animated

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def start_frame_set(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Set the current frame as the preview or scene start frame

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def update_animated_transform_constraints(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_convert_to_radians: bool | None = True,
):
    """Update f-curves/drivers affecting Transform constraints (use it with files from 2.70 and earlier)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_convert_to_radians: Convert to Radians, Convert f-curves/drivers affecting rotations to radians.Warning: Use this only once
    :type use_convert_to_radians: bool | None
    """

def view_curve_in_graph_editor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
    isolate: bool | None = False,
):
    """Frame the property under the cursor in the Graph Editor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: Show All, Frame the whole array property instead of only the index under the cursor
    :type all: bool | None
    :param isolate: Isolate, Hides all F-Curves other than the ones being framed
    :type isolate: bool | None
    """
