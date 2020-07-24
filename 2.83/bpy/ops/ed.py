import sys
import typing


def flush_edits():
    ''' Flush edit data from active editing modes

    '''

    pass


def redo():
    ''' Redo previous action

    '''

    pass


def undo():
    ''' Undo previous action

    '''

    pass


def undo_history(item: int = 0):
    ''' Redo specific action in history

    :param item: Item
    :type item: int
    '''

    pass


def undo_push(message: str = "Add an undo step *function may be moved*"):
    ''' Add an undo state (internal use only)

    :param message: Undo Message
    :type message: str
    '''

    pass


def undo_redo():
    ''' Undo and redo previous action

    '''

    pass
