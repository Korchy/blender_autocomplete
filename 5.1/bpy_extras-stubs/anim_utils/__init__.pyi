import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

class AutoKeying:
    """Auto-keying support."""

    @classmethod
    def active_keyingset(cls, context: bpy.types.Context) -> None | bpy.types.KeyingSet:
        """Return the active keying set, if it should be used.Only returns the active keying set when the auto-key settings indicate
        it should be used, and when it is not using absolute paths (because
        thats not supported by the Copy Global Transform add-on).

                :param context: The context.
                :return: The active keying set, or None when it should not be used.
        """

    @classmethod
    def autokey_transformation(
        cls, context: bpy.types.Context, target: bpy.types.Object | bpy.types.PoseBone
    ) -> None:
        """Auto-key transformation properties.

        :param context: The context.
        :param target: The object or pose bone to keyframe.
        """

    @classmethod
    def autokeying_options(cls, context: bpy.types.Context) -> None | set[str]:
        """Retrieve the Auto Keyframe options, or None if disabled.

        :param context: The context.
        :return: The keyframing option flags, or None when auto-keying is disabled.
        """

    @classmethod
    def key_transformation(
        cls, target: bpy.types.Object | bpy.types.PoseBone, options: set[str]
    ) -> None:
        """Keyframe transformation properties, avoiding keying locked channels.

        :param target: The object or pose bone to keyframe.
        :param options: Keyframing options.
        """

    @classmethod
    def key_transformation_via_keyingset(
        cls,
        context: bpy.types.Context,
        target: bpy.types.Object | bpy.types.PoseBone,
        keyingset: bpy.types.KeyingSet,
    ) -> None:
        """Auto-key transformation properties with the given keying set.

        :param context: The context.
        :param target: The object or pose bone to keyframe.
        :param keyingset: The keying set to use.
        """

    @classmethod
    def keyframe_channels(
        cls,
        target: bpy.types.Object | bpy.types.PoseBone,
        options: set[str],
        data_path: str,
        group: str,
        locks: collections.abc.Iterable[bool],
    ) -> None:
        """Keyframe channels, avoiding keying locked channels.

        :param target: The object or pose bone to keyframe.
        :param options: Keyframing options.
        :param data_path: The data path to keyframe.
        :param group: The group name for the keyframes.
        :param locks: Per-channel lock status.
        """

    @classmethod
    def keying_options(cls, context: bpy.types.Context) -> set[str]:
        """Retrieve the general keyframing options from user preferences.

        :param context: The context.
        :return: The keyframing option flags.
        """

    @classmethod
    def keying_options_from_keyingset(
        cls, context: bpy.types.Context, keyingset: bpy.types.KeyingSet
    ) -> set[str]:
        """Retrieve the general keyframing options from user preferences.

        :param context: The context.
        :param keyingset: The keying set to read options from.
        :return: The keyframing option flags.
        """

    @classmethod
    def keytype(cls, the_keytype: str) -> None:
        """Context manager to set the key type thats inserted.

        :param the_keytype: The key type to use.
        :return: A context manager that resets the key type on exit.
        """

    @classmethod
    def options(
        cls,
        *,
        keytype: str = "",
        use_loc: bool = True,
        use_rot: bool = True,
        use_scale: bool = True,
        force_autokey: bool = False,
    ) -> None:
        """Context manager to set various keyframing options.

        :param keytype: The key type to use.
        :param use_loc: Key location channels.
        :param use_rot: Key rotation channels.
        :param use_scale: Key scale channels.
        :param force_autokey: Allow use without the user activating auto-keying.
        :return: A context manager that resets the options on exit.
        """

    @staticmethod
    def get_4d_rotlock(bone: bpy.types.PoseBone) -> list[bool]:
        """Retrieve the lock status for 4D rotation.

        :param bone: The pose bone to check.
        :return: Lock status for W, X, Y, Z rotation channels.
        """

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
    obj: bpy.types.Object,
    *,
    action: None | bpy.types.Action,
    frames: collections.abc.Iterable[int],
    bake_options,
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
) -> None | bpy.types.Action:
    """A coroutine that bakes action for a single object.

        :param obj: Object to bake.
        :param action: An action to bake the data into, or None for a new action
    to be created.
        :param bake_options: Options for baking.
        :return: an action or None
    """

def bake_action_objects(
    object_action_pairs: collections.abc.Sequence[
        tuple[bpy.types.Object, bpy.types.Action | None]
    ],
    *,
    frames: collections.abc.Iterable[int],
    bake_options,
) -> collections.abc.Sequence[bpy.types.Action]:
    """A version of `bake_action_objects_iter` that takes frames and returns the output.

        :param object_action_pairs: Sequence of object action tuples,
    action is the destination for the baked data. When None a new action will be created.
        :param frames: Frames to bake.
        :param bake_options: Options for baking.
        :return: A sequence of Action or None types (aligned with object_action_pairs)
    """

def bake_action_objects_iter(
    object_action_pairs: collections.abc.Sequence[
        tuple[bpy.types.Object, bpy.types.Action | None]
    ],
    bake_options,
) -> None:
    """A coroutine that bakes actions for multiple objects.

        :param object_action_pairs: Sequence of object action tuples,
    action is the destination for the baked data. When None a new action will be created.
        :param bake_options: Options for baking.
        :return: A generator that yields None for each frame, then finally
    yields a tuple of actions (aligned with object_action_pairs).
    """
