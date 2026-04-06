import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def bake_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Bake Entire Fluid Simulation"""

def bake_data(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Bake Fluid Data"""

def bake_guides(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Bake Fluid Guiding"""

def bake_mesh(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Bake Fluid Mesh"""

def bake_noise(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Bake Fluid Noise"""

def bake_particles(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Bake Fluid Particles"""

def free_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Free Entire Fluid Simulation"""

def free_data(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Free Fluid Data"""

def free_guides(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Free Fluid Guiding"""

def free_mesh(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Free Fluid Mesh"""

def free_noise(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Free Fluid Noise"""

def free_particles(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Free Fluid Particles"""

def pause_bake(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Pause Bake"""

def preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add or remove a Fluid Preset

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """
