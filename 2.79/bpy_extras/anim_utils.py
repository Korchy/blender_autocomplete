import sys
import typing
import bpy


def bake_action(frame_start: int,
                frame_end: int,
                frame_step: int = 1,
                only_selected: bool = False,
                do_pose: bool = True,
                do_object: bool = True,
                do_visual_keying: bool = True,
                do_constraint_clear: bool = False,
                do_parents_clear: bool = False,
                do_clean: bool = False,
                action: 'bpy.types.Action' = None) -> 'bpy.types.Action':
    '''Return an image from the file path with options to search multiple paths and return a placeholder if its not found. 

    :param frame_start: First frame to bake. 
    :type frame_start: int
    :param frame_end: Last frame to bake. 
    :type frame_end: int
    :param frame_step: Frame step. 
    :type frame_step: int
    :param only_selected: Only bake selected bones. 
    :type only_selected: bool
    :param do_pose: Bake pose channels. 
    :type do_pose: bool
    :param do_object: Bake objects. 
    :type do_object: bool
    :param do_visual_keying: Use the final transformations for baking (‘visual keying’) 
    :type do_visual_keying: bool
    :param do_constraint_clear: Remove constraints after baking. 
    :type do_constraint_clear: bool
    :param do_parents_clear: Unparent after baking objects. 
    :type do_parents_clear: bool
    :param do_clean: Remove redundant keyframes after baking. 
    :type do_clean: bool
    :param action: An action to bake the data into, or None for a new action to be created. 
    :type action: 'bpy.types.Action'
    :return:  an action or None 
    '''

    pass
