import sys
import typing


def report_copy():
    '''Copy selected reports to Clipboard 

    '''

    pass


def report_delete():
    '''Delete selected reports 

    '''

    pass


def report_replay():
    '''Replay selected reports 

    '''

    pass


def reports_display_update():
    '''Update the display of reports in Blender UI (internal use) 

    '''

    pass


def select_all_toggle():
    '''Select or deselect all reports 

    '''

    pass


def select_border(gesture_mode: int = 0,
                  xmin: int = 0,
                  xmax: int = 0,
                  ymin: int = 0,
                  ymax: int = 0,
                  extend: bool = True):
    '''Toggle border selection 

    :param gesture_mode: Gesture Mode 
    :type gesture_mode: int
    :param xmin: X Min 
    :type xmin: int
    :param xmax: X Max 
    :type xmax: int
    :param ymin: Y Min 
    :type ymin: int
    :param ymax: Y Max 
    :type ymax: int
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: bool
    '''

    pass


def select_pick(report_index: int = 0):
    '''Select reports by index 

    :param report_index: Report, Index of the report 
    :type report_index: int
    '''

    pass
