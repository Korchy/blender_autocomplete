import typing
import collections.abc
import typing_extensions

def bake_all(execution_context: int | str | None = None, undo: bool | None = None):
    """Bake Entire Fluid Simulation

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def bake_data(execution_context: int | str | None = None, undo: bool | None = None):
    """Bake Fluid Data

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def bake_guides(execution_context: int | str | None = None, undo: bool | None = None):
    """Bake Fluid Guiding

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def bake_mesh(execution_context: int | str | None = None, undo: bool | None = None):
    """Bake Fluid Mesh

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def bake_noise(execution_context: int | str | None = None, undo: bool | None = None):
    """Bake Fluid Noise

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def bake_particles(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Bake Fluid Particles

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def free_all(execution_context: int | str | None = None, undo: bool | None = None):
    """Free Entire Fluid Simulation

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def free_data(execution_context: int | str | None = None, undo: bool | None = None):
    """Free Fluid Data

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def free_guides(execution_context: int | str | None = None, undo: bool | None = None):
    """Free Fluid Guiding

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def free_mesh(execution_context: int | str | None = None, undo: bool | None = None):
    """Free Fluid Mesh

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def free_noise(execution_context: int | str | None = None, undo: bool | None = None):
    """Free Fluid Noise

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def free_particles(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Free Fluid Particles

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def pause_bake(execution_context: int | str | None = None, undo: bool | None = None):
    """Pause Bake

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
):
    """Add or remove a Fluid Preset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """
