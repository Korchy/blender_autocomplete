import sys
import typing


def delete_metaelems():
    ''' Delete selected metaball element(s)

    '''

    pass


def duplicate_metaelems():
    ''' Duplicate selected metaball element(s)

    '''

    pass


def duplicate_move(MBALL_OT_duplicate_metaelems=None,
                   TRANSFORM_OT_translate=None):
    ''' Make copies of the selected metaball elements and move them

    :param MBALL_OT_duplicate_metaelems: Duplicate Metaball Elements, Duplicate selected metaball element(s)
    :param TRANSFORM_OT_translate: Move, Move selected items
    '''

    pass


def hide_metaelems(unselected: bool = False):
    ''' Hide (un)selected metaball element(s)

    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: bool
    '''

    pass


def reveal_metaelems(select: bool = True):
    ''' Reveal all hidden metaball elements

    :param select: Select
    :type select: bool
    '''

    pass


def select_all(action: typing.Union[str, int] = 'TOGGLE'):
    ''' Change selection of all metaball elements

    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_random_metaelems(ratio: float = 0.5,
                            seed: int = 0,
                            action: typing.Union[str, int] = 'SELECT'):
    ''' Randomly select metaball elements

    :param ratio: Ratio, Portion of items to select randomly
    :type ratio: float
    :param seed: Random Seed, Seed for the random number generator
    :type seed: int
    :param action: Action, Selection action to execute * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_similar(type: typing.Union[str, int] = 'TYPE',
                   threshold: float = 0.1):
    ''' Select similar metaballs by property types

    :param type: Type
    :type type: typing.Union[str, int]
    :param threshold: Threshold
    :type threshold: float
    '''

    pass
