import typing
import collections.abc
import typing_extensions
import bpy.types

class BakeOptions:
    """BakeOptions(only_selected: bool, do_pose: bool, do_object: bool, do_visual_keying: bool, do_constraint_clear: bool, do_parents_clear: bool, do_clean: bool, do_location: bool, do_rotation: bool, do_scale: bool, do_bbone: bool, do_custom_props: bool)"""

class KeyframesCo:
    """A buffer for keyframe Co unpacked values per FCurveKey. FCurveKeys are added using
    add_paths(), Co values stored using extend_co_values(), then finally use
    insert_keyframes_into_*_action() for efficiently inserting keys into the F-curves.Users are limited to one Action Group per instance.
    """

    keyframes_from_fcurve: typing.Any

    def add_paths(self, rna_path, total_indices):
        """

        :param rna_path:
        :param total_indices:
        """

    def extend_co_value(self, rna_path, frame, value):
        """

        :param rna_path:
        :param frame:
        :param value:
        """

    def extend_co_values(self, rna_path, total_indices, frame, values):
        """

        :param rna_path:
        :param total_indices:
        :param frame:
        :param values:
        """

    def insert_keyframes_into_existing_action(
        self, lookup_fcurves, total_new_keys, action, action_group_name: str
    ):
        """Assumes the action already exists, that it might already have F-curves. Otherwise, the
        only difference between versions is performance and implementation simplicity.

                :param lookup_fcurves: : This is only used for efficiency.
        It's a substitute for action.fcurves.find() which is a potentially expensive linear search.
                :param total_new_keys:
                :param action:
                :param action_group_name: Name of Action Group that F-curves are added to.
                :type action_group_name: str
        """

    def insert_keyframes_into_new_action(
        self, total_new_keys, action, action_group_name: str
    ):
        """Assumes the action is new, that it has no F-curves. Otherwise, the only difference between versions is
        performance and implementation simplicity.

                :param total_new_keys:
                :param action:
                :param action_group_name: Name of Action Group that F-curves are added to.
                :type action_group_name: str
        """

def bake_action(
    obj: bpy.types.Object, *, action: bpy.types.Action | None, frames, bake_options
) -> bpy.types.Action:
    """

        :param obj: Object to bake.
        :type obj: bpy.types.Object
        :param action: An action to bake the data into, or None for a new action
    to be created.
        :type action: bpy.types.Action | None
        :param frames: Frames to bake.
        :return: an action or None
        :rtype: bpy.types.Action
    """

def bake_action_iter(
    obj: bpy.types.Object, *, action: bpy.types.Action | None, bake_options
) -> bpy.types.Action:
    """An coroutine that bakes action for a single object.

        :param obj: Object to bake.
        :type obj: bpy.types.Object
        :param action: An action to bake the data into, or None for a new action
    to be created.
        :type action: bpy.types.Action | None
        :param bake_options: Boolean options of what to include into the action bake.
        :return: an action or None
        :rtype: bpy.types.Action
    """

def bake_action_objects(
    object_action_pairs, *, frames, bake_options
) -> list[bpy.types.Action]:
    """A version of `bake_action_objects_iter` that takes frames and returns the output.

    :param frames: Frames to bake.
    :return: A sequence of Action or None types (aligned with object_action_pairs)
    :rtype: list[bpy.types.Action]
    """

def bake_action_objects_iter(object_action_pairs, bake_options):
    """An coroutine that bakes actions for multiple objects.

        :param object_action_pairs: Sequence of object action tuples,
    action is the destination for the baked data. When None a new action will be created.
    """
