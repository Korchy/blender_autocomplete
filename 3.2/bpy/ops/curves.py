import sys
import typing


def convert_to_particle_system():
    ''' Add a new or update an existing hair particle system on the surface object

    '''

    pass


def sculptmode_toggle():
    ''' Enter/Exit sculpt mode for curves

    '''

    pass


def snap_curves_to_surface(attach_mode: typing.Union[str, int] = 'NEAREST'):
    ''' Move curves so that the first point is exactly on the surface mesh

    :param attach_mode: Attach Mode, How to find the point on the surface to attach to * NEAREST Nearest -- Find the closest point on the surface for the root point of every curve and move the root there. * DEFORM Deform -- Re-attach curves to a deformed surface using the existing attachment information. This only works when the topology of the surface mesh has not changed.
    :type attach_mode: typing.Union[str, int]
    '''

    pass
