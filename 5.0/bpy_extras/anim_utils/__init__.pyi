import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

class AutoKeying:
    """Auto-keying support.Retrieve the lock status for 4D rotation."""

class BakeOptions:
    """BakeOptions(only_selected: bool, do_pose: bool, do_object: bool, do_visual_keying: bool, do_constraint_clear: bool, do_parents_clear: bool, do_clean: bool, do_location: bool, do_rotation: bool, do_scale: bool, do_bbone: bool, do_custom_props: bool)"""

class KeyframesCo:
    """A buffer for keyframe Co unpacked values per FCurveKey. FCurveKeys are added using
    add_paths(), Co values stored using extend_co_values(), then finally use
    insert_keyframes_into_*_action() for efficiently inserting keys into the F-curves.Users are limited to one Action Group per instance.
    """

    keyframes_from_fcurve: typing.Any

    def add_paths(self, rna_path, total_indices) -> None:
        """

        :param rna_path:
        :param total_indices:
        """

    def extend_co_value(self, rna_path, frame, value) -> None:
        """

        :param rna_path:
        :param frame:
        :param value:
        """

    def extend_co_values(self, rna_path, total_indices, frame, values) -> None:
        """

        :param rna_path:
        :param total_indices:
        :param frame:
        :param values:
        """

    def insert_keyframes_into_existing_action(
        self, lookup_fcurves, total_new_keys, channelbag
    ) -> None:
        """Assumes the action already exists, that it might already have F-curves. Otherwise, the
        only difference between versions is performance and implementation simplicity.

                :param lookup_fcurves: : This is only used for efficiency.
        Its a substitute for channelbag.fcurves.find() which is a potentially expensive linear search.
                :param total_new_keys:
                :param channelbag:
        """

    def insert_keyframes_into_new_action(
        self, total_new_keys, channelbag, group_name
    ) -> None:
        """Assumes the action is new, that it has no F-curves. Otherwise, the only difference between versions is
        performance and implementation simplicity.

                :param total_new_keys:
                :param channelbag:
                :param group_name: Name of the Group that F-curves are added to.
        """

def action_ensure_channelbag_for_slot(action, slot) -> None:
    """Ensure a layer and a keyframe strip exists, then ensure that strip has a channelbag for the slot."""

def action_get_channelbag_for_slot(action, slot) -> None:
    """Returns the first channelbag found for the slot.
    In case there are multiple layers or strips they are iterated until a
    channelbag for that slot is found. In case no matching channelbag is found, returns None.

    """

def action_get_first_suitable_slot(action, target_id_type) -> None:
    """Return the first Slot of the given Action thats suitable for the given ID type.Typically you should not need this function; when an Action is assigned to a
    data-block, just use the slot that was assigned along with it.

    """

def animdata_get_channelbag_for_assigned_slot(anim_data) -> None:
    """Return the channelbag used in the given anim_data or None if there is no Action
    + Slot combination defined.

    """

def bake_action(
    obj: bpy.types.Object, *, action: None | bpy.types.Action, frames: int, bake_options
) -> None | bpy.types.Action:
    """

        :param obj: Object to bake.
        :param action: An action to bake the data into, or None for a new action
    to be created.
        :param frames: Frames to bake.
        :param bake_options: Options for baking.
        :return: Action or None.
    """

def bake_action_iter(
    obj: bpy.types.Object, *, action: None | bpy.types.Action, bake_options
) -> bpy.types.Action:
    """An coroutine that bakes action for a single object.

        :param obj: Object to bake.
        :param action: An action to bake the data into, or None for a new action
    to be created.
        :param bake_options: Boolean options of what to include into the action bake.
        :return: an action or None
    """

def bake_action_objects(
    object_action_pairs, *, frames, bake_options
) -> collections.abc.Sequence[bpy.types.Action]:
    """A version of `bake_action_objects_iter` that takes frames and returns the output.

    :param frames: Frames to bake.
    :param bake_options: Options for baking.
    :return: A sequence of Action or None types (aligned with object_action_pairs)
    """

def bake_action_objects_iter(object_action_pairs, bake_options) -> None:
    """An coroutine that bakes actions for multiple objects.

        :param object_action_pairs: Sequence of object action tuples,
    action is the destination for the baked data. When None a new action will be created.
        :param bake_options: Options for baking.
    """
