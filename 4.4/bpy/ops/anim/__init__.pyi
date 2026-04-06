import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def change_frame(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame: float | None = 0.0,
    snap: bool | None = False,
) -> None:
    """Interactively change the current frame number

    :param frame: Frame
    :param snap: Snap
    """

def channel_select_keys(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
) -> None:
    """Select all keyframes of channel under mouse

    :param extend: Extend, Extend selection
    """

def channel_view_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    include_handles: bool | None = True,
    use_preview_range: bool | None = True,
) -> None:
    """Reset viewable area to show the channel under the cursor

    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    :param use_preview_range: Use Preview Range, Ignore frames outside of the preview range
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
) -> None:
    """Create keyframes following the current shape of F-Curves of selected channels

        :param range: Frame Range, The range in which to create new keys
        :param step: Frame Step, At which interval to add keys
        :param remove_outside_range: Remove Outside Range, Removes keys outside the given range, leaving only the newly baked
        :param interpolation_type: Interpolation Type, Choose the interpolation type with which new keys will be added

    BEZIER
    Bézier -- New keys will be Bézier.

    LIN
    Linear -- New keys will be linear.

    CONST
    Constant -- New keys will be constant.
        :param bake_modifiers: Bake Modifiers, Bake Modifiers into keyframes and delete them after
    """

def channels_clean_empty(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete all empty animation data containers from visible data-blocks"""

def channels_click(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    extend_range: bool | None = False,
    children_only: bool | None = False,
) -> None:
    """Handle mouse clicks over animation channels

    :param extend: Extend Select
    :param extend_range: Extend Range, Selection of active channel to clicked channel
    :param children_only: Select Children Only
    """

def channels_collapse(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
) -> None:
    """Collapse (close) all selected expandable animation channels

    :param all: All, Collapse all channels (not just selected ones)
    """

def channels_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete all selected animation channels"""

def channels_editable_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["TOGGLE", "DISABLE", "ENABLE", "INVERT"] | None = "TOGGLE",
    type: typing.Literal["PROTECT", "MUTE"] | None = "PROTECT",
) -> None:
    """Toggle editability of selected channels

    :param mode: Mode
    :param type: Type
    """

def channels_expand(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
) -> None:
    """Expand (open) all selected expandable animation channels

    :param all: All, Expand all channels (not just selected ones)
    """

def channels_fcurves_enable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear disabled tag from all F-Curves to get broken F-Curves working again"""

def channels_group(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "New Group",
) -> None:
    """Add selected F-Curves to a new group

    :param name: Name, Name of newly created group
    """

def channels_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["TOP", "UP", "DOWN", "BOTTOM"] | None = "DOWN",
) -> None:
    """Rearrange selected animation channels

    :param direction: Direction
    """

def channels_rename(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Rename animation channel under mouse"""

def channels_select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Toggle selection of all animation channels

        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
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
) -> None:
    """Select all animation channels within the specified region

    :param xmin: X Min
    :param xmax: X Max
    :param ymin: Y Min
    :param ymax: Y Max
    :param wait_for_input: Wait for Input
    :param deselect: Deselect, Deselect rather than select items
    :param extend: Extend, Extend selection instead of deselecting everything first
    """

def channels_select_filter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Start entering text which filters the set of channels shown to only include those with matching names"""

def channels_setting_disable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["TOGGLE", "DISABLE", "ENABLE", "INVERT"] | None = "DISABLE",
    type: typing.Literal["PROTECT", "MUTE"] | None = "PROTECT",
) -> None:
    """Disable specified setting on all selected animation channels

    :param mode: Mode
    :param type: Type
    """

def channels_setting_enable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["TOGGLE", "DISABLE", "ENABLE", "INVERT"] | None = "ENABLE",
    type: typing.Literal["PROTECT", "MUTE"] | None = "PROTECT",
) -> None:
    """Enable specified setting on all selected animation channels

    :param mode: Mode
    :param type: Type
    """

def channels_setting_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["TOGGLE", "DISABLE", "ENABLE", "INVERT"] | None = "TOGGLE",
    type: typing.Literal["PROTECT", "MUTE"] | None = "PROTECT",
) -> None:
    """Toggle specified setting on all selected animation channels

    :param mode: Mode
    :param type: Type
    """

def channels_ungroup(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove selected F-Curves from their current groups"""

def channels_view_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    include_handles: bool | None = True,
    use_preview_range: bool | None = True,
) -> None:
    """Reset viewable area to show the selected channels

    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    :param use_preview_range: Use Preview Range, Ignore frames outside of the preview range
    """

def clear_useless_actions(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_unused: bool | None = True,
) -> None:
    """Mark actions with no F-Curves for deletion after save and reload of file preserving "action libraries"

    :param only_unused: Only Unused, Only unused (Fake User only) actions get considered
    """

def convert_legacy_action(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Convert a legacy Action to a layered Action on the active object"""

def copy_driver_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the driver for the highlighted button"""

def driver_button_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add driver for the property under the cursor"""

def driver_button_edit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Edit the drivers for the connected property represented by the highlighted button"""

def driver_button_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
) -> None:
    """Remove the driver(s) for the connected property(s) represented by the highlighted button

    :param all: All, Delete drivers for all elements of the array
    """

def end_frame_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set the current frame as the preview or scene end frame"""

def keyframe_clear_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
) -> None:
    """Clear all keyframes on the currently active property

    :param all: All, Clear keyframes from all elements of the array
    """

def keyframe_clear_v3d(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
) -> None:
    """Remove all keyframe animation for selected objects

    :param confirm: Confirm, Prompt for confirmation
    """

def keyframe_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "DEFAULT",
) -> None:
    """Delete keyframes on the current frame for all properties in the specified Keying Set

    :param type: Keying Set, The Keying Set to use
    """

def keyframe_delete_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
) -> None:
    """Delete current keyframe of current UI-active property

    :param all: All, Delete keyframes from all elements of the array
    """

def keyframe_delete_by_name(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str = "",
) -> None:
    """Alternate access to Delete Keyframe for keymaps to use

    :param type: Keying Set, The Keying Set to use
    """

def keyframe_delete_v3d(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
) -> None:
    """Remove keyframes on current frame for selected objects and bones

    :param confirm: Confirm, Prompt for confirmation
    """

def keyframe_insert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "DEFAULT",
) -> None:
    """Insert keyframes on the current frame using either the active keying set, or the user preferences if no keying set is active

    :param type: Keying Set, The Keying Set to use
    """

def keyframe_insert_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
) -> None:
    """Insert a keyframe for current UI-active property

    :param all: All, Insert a keyframe for all element of the array
    """

def keyframe_insert_by_name(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str = "",
) -> None:
    """Alternate access to Insert Keyframe for keymaps to use

    :param type: Keying Set, The Keying Set to use
    """

def keyframe_insert_menu(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "DEFAULT",
    always_prompt: bool | None = False,
) -> None:
    """Insert Keyframes for specified Keying Set, with menu of available Keying Sets if undefined

    :param type: Keying Set, The Keying Set to use
    :param always_prompt: Always Show Menu
    """

def keying_set_active_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "DEFAULT",
) -> None:
    """Set a new active keying set

    :param type: Keying Set, The Keying Set to use
    """

def keying_set_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a new (empty) keying set to the active Scene"""

def keying_set_export(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    filter_folder: bool | None = True,
    filter_text: bool | None = True,
    filter_python: bool | None = True,
) -> None:
    """Export Keying Set to a Python script

    :param filepath: filepath
    :param filter_folder: Filter folders
    :param filter_text: Filter text
    :param filter_python: Filter Python
    """

def keying_set_path_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add empty path to active keying set"""

def keying_set_path_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove active Path from active keying set"""

def keying_set_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the active keying set"""

def keyingset_button_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
) -> None:
    """Add current UI-active property to current keying set

    :param all: All, Add all elements of the array to a Keying Set
    """

def keyingset_button_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove current UI-active property from current keying set"""

def merge_animation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Merge the animation of the selected objects into the action of the active object. Actions are not deleted by this, but might end up with zero users"""

def paste_driver_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Paste the driver in the internal clipboard to the highlighted button"""

def previewrange_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear preview range"""

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
) -> None:
    """Interactively define frame range used for playback

    :param xmin: X Min
    :param xmax: X Max
    :param ymin: Y Min
    :param ymax: Y Max
    :param wait_for_input: Wait for Input
    """

def scene_range_frame(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset the horizontal view to the current scene frame range, taking the preview range into account if it is active"""

def separate_slots(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move all slots of the action on the active object into newly created, separate actions. All users of those slots will be reassigned to the new actions. The current action wont be deleted but will be empty and might end up having zero users"""

def slot_channels_move_to_new_action(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move the selected slots into a newly created action"""

def slot_new_for_id(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create a new action slot for this data-block, to hold its animation"""

def slot_unassign_from_constraint(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Un-assign the action slot from this constraint"""

def slot_unassign_from_id(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Un-assign the action slot, effectively making this data-block non-animated"""

def slot_unassign_from_nla_strip(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Un-assign the action slot from this NLA strip, effectively making it non-animated"""

def start_frame_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set the current frame as the preview or scene start frame"""

def update_animated_transform_constraints(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_convert_to_radians: bool | None = True,
) -> None:
    """Update f-curves/drivers affecting Transform constraints (use it with files from 2.70 and earlier)

    :param use_convert_to_radians: Convert to Radians, Convert f-curves/drivers affecting rotations to radians.Warning: Use this only once
    """

def view_curve_in_graph_editor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
    isolate: bool | None = False,
) -> None:
    """Frame the property under the cursor in the Graph Editor

    :param all: Show All, Frame the whole array property instead of only the index under the cursor
    :param isolate: Isolate, Hides all F-Curves other than the ones being framed
    """
