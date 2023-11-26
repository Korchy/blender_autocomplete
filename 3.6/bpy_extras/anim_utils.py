import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


class KeyframesCo:
    keyframes_from_fcurve = None
    ''' '''

    def add_paths(self, rna_path, total_indices):
        ''' 

        '''
        pass

    def extend_co_value(self, rna_path, frame, value):
        ''' 

        '''
        pass

    def extend_co_values(self, rna_path, total_indices, frame, values):
        ''' 

        '''
        pass

    def insert_keyframes_into_existing_action(
            self, lookup_fcurves, total_new_keys, action, action_group_name):
        ''' 

        '''
        pass

    def insert_keyframes_into_new_action(self, total_new_keys, action,
                                         action_group_name):
        ''' 

        '''
        pass


def bake_action(obj: 'bpy.types.Object', *,
                action: typing.Optional['bpy.types.Action'], frames: int,
                **kwargs) -> 'bpy.types.Action':
    ''' 

    :param obj: Object to bake.
    :type obj: 'bpy.types.Object'
    :param action: An action to bake the data into, or None for a new action to be created.
    :type action: typing.Optional['bpy.types.Action']
    :param frames: Frames to bake.
    :type frames: int
    :rtype: 'bpy.types.Action'
    :return: an action or None
    '''

    pass


def bake_action_iter(obj: 'bpy.types.Object',
                     *,
                     action: typing.Optional['bpy.types.Action'],
                     only_selected: bool = False,
                     do_pose: bool = True,
                     do_object: bool = True,
                     do_visual_keying: bool = True,
                     do_constraint_clear: bool = False,
                     do_parents_clear: bool = False,
                     do_clean: bool = False) -> 'bpy.types.Action':
    ''' An coroutine that bakes action for a single object.

    :param obj: Object to bake.
    :type obj: 'bpy.types.Object'
    :param action: An action to bake the data into, or None for a new action to be created.
    :type action: typing.Optional['bpy.types.Action']
    :param only_selected: Only bake selected bones.
    :type only_selected: bool
    :param do_pose: Bake pose channels.
    :type do_pose: bool
    :param do_object: Bake objects.
    :type do_object: bool
    :param do_visual_keying: Use the final transformations for baking ('visual keying')
    :type do_visual_keying: bool
    :param do_constraint_clear: Remove constraints after baking.
    :type do_constraint_clear: bool
    :param do_parents_clear: Unparent after baking objects.
    :type do_parents_clear: bool
    :param do_clean: Remove redundant keyframes after baking.
    :type do_clean: bool
    :rtype: 'bpy.types.Action'
    :return: an action or None
    '''

    pass


def bake_action_objects(object_action_pairs, *, frames: int,
                        **kwargs) -> typing.Iterable['bpy.types.Action']:
    ''' A version of :func:`bake_action_objects_iter` that takes frames and returns the output.

    :param frames: Frames to bake.
    :type frames: int
    :rtype: typing.Iterable['bpy.types.Action']
    :return: A sequence of Action or None types (aligned with `object_action_pairs`)
    '''

    pass


def bake_action_objects_iter(
        object_action_pairs: typing.
        Union['bpy.types.Object', 'bpy.types.Action', 'bpy.types.Sequence'],
        **kwargs):
    ''' An coroutine that bakes actions for multiple objects.

    :param object_action_pairs: Sequence of object action tuples, action is the destination for the baked data. When None a new action will be created.
    :type object_action_pairs: typing.Union['bpy.types.Object', 'bpy.types.Action', 'bpy.types.Sequence']
    '''

    pass
