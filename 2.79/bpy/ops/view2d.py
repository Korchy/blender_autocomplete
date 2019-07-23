import sys
import typing


def ndof():
    '''Use a 3D mouse device to pan/zoom the view 

    '''

    pass


def pan(deltax: int = 0, deltay: int = 0):
    '''Pan the view 

    :param deltax: Delta X 
    :type deltax: int
    :param deltay: Delta Y 
    :type deltay: int
    '''

    pass


def reset():
    '''Reset the view 

    '''

    pass


def scroll_down(deltax: int = 0, deltay: int = 0, page: bool = False):
    '''Scroll the view down 

    :param deltax: Delta X 
    :type deltax: int
    :param deltay: Delta Y 
    :type deltay: int
    :param page: Page, Scroll down one page 
    :type page: bool
    '''

    pass


def scroll_left(deltax: int = 0, deltay: int = 0):
    '''Scroll the view left 

    :param deltax: Delta X 
    :type deltax: int
    :param deltay: Delta Y 
    :type deltay: int
    '''

    pass


def scroll_right(deltax: int = 0, deltay: int = 0):
    '''Scroll the view right 

    :param deltax: Delta X 
    :type deltax: int
    :param deltay: Delta Y 
    :type deltay: int
    '''

    pass


def scroll_up(deltax: int = 0, deltay: int = 0, page: bool = False):
    '''Scroll the view up 

    :param deltax: Delta X 
    :type deltax: int
    :param deltay: Delta Y 
    :type deltay: int
    :param page: Page, Scroll up one page 
    :type page: bool
    '''

    pass


def scroller_activate():
    '''Scroll view by mouse click and drag 

    '''

    pass


def smoothview(gesture_mode: int = 0,
               xmin: int = 0,
               xmax: int = 0,
               ymin: int = 0,
               ymax: int = 0):
    '''Undocumented 

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
    '''

    pass


def zoom(deltax: float = 0.0, deltay: float = 0.0):
    '''Zoom in/out the view 

    :param deltax: Delta X 
    :type deltax: float
    :param deltay: Delta Y 
    :type deltay: float
    '''

    pass


def zoom_border(gesture_mode: int = 0,
                xmin: int = 0,
                xmax: int = 0,
                ymin: int = 0,
                ymax: int = 0):
    '''Zoom in the view to the nearest item contained in the border 

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
    '''

    pass


def zoom_in(zoomfacx: float = 0.0, zoomfacy: float = 0.0):
    '''Zoom in the view 

    :param zoomfacx: Zoom Factor X 
    :type zoomfacx: float
    :param zoomfacy: Zoom Factor Y 
    :type zoomfacy: float
    '''

    pass


def zoom_out(zoomfacx: float = 0.0, zoomfacy: float = 0.0):
    '''Zoom out the view 

    :param zoomfacx: Zoom Factor X 
    :type zoomfacx: float
    :param zoomfacy: Zoom Factor Y 
    :type zoomfacy: float
    '''

    pass
