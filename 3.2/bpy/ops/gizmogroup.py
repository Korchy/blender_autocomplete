import sys
import typing


def gizmo_select(extend: bool = False,
                 deselect: bool = False,
                 toggle: bool = False,
                 deselect_all: bool = False,
                 select_passthrough: bool = False):
    ''' Select the currently highlighted gizmo

    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param deselect: Deselect, Remove from selection
    :type deselect: bool
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: bool
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :type select_passthrough: bool
    '''

    pass


def gizmo_tweak():
    ''' Tweak the active gizmo

    '''

    pass
