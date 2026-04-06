import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

def brush_edit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    pen_flip: bool | None = False,
) -> None:
    """Apply a stroke of brush to the particles

    :param stroke: Stroke
    :param pen_flip: Pen Flip, Whether a tablets eraser mode is being used
    """

def connect_hair(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
) -> None:
    """Connect hair to the emitter mesh

    :param all: All Hair, Connect all hair systems to the emitter mesh
    """

def copy_particle_systems(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    space: typing.Literal["OBJECT", "WORLD"] | None = "OBJECT",
    remove_target_particles: bool | None = True,
    use_active: bool | None = False,
) -> None:
    """Copy particle systems from the active object to selected objects

        :param space: Space, Space transform for copying from one object to another

    OBJECT
    Object -- Copy inside each objects local space.

    WORLD
    World -- Copy in world space.
        :param remove_target_particles: Remove Target Particles, Remove particle systems on the target objects
        :param use_active: Use Active, Use the active particle system from the context
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["PARTICLE", "KEY"] | None = "PARTICLE",
) -> None:
    """Delete selected particles or keys

    :param type: Type, Delete a full particle or only keys
    """

def disconnect_hair(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
) -> None:
    """Disconnect hair from the emitter mesh

    :param all: All Hair, Disconnect all hair systems from the emitter mesh
    """

def duplicate_particle_system(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_duplicate_settings: bool | None = False,
) -> None:
    """Duplicate particle system within the active object

    :param use_duplicate_settings: Duplicate Settings, Duplicate settings as well, so the new particle system uses its own settings
    """

def dupliob_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Duplicate the current instance object"""

def dupliob_move_down(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move instance object down in the list"""

def dupliob_move_up(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move instance object up in the list"""

def dupliob_refresh(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Refresh list of instance objects and their weights"""

def dupliob_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the selected instance object"""

def edited_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undo all edition performed on the particle system"""

def hair_dynamics_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add or remove a Hair Dynamics Preset

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Hide selected particles

    :param unselected: Unselected, Hide unselected rather than selected
    """

def mirror(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Duplicate and mirror the selected particles along the local X axis"""

def new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add new particle settings"""

def new_target(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a new particle target"""

def particle_edit_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle particle edit mode"""

def particle_system_remove_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove all particle system within the active object"""

def rekey(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keys_number: int | None = 2,
) -> None:
    """Change the number of keys of selected particles (root and tip keys included)

    :param keys_number: Number of Keys
    """

def remove_doubles(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    threshold: float | None = 0.0002,
) -> None:
    """Remove selected particles close enough of others

    :param threshold: Merge Distance, Threshold distance within which particles are removed
    """

def reveal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
) -> None:
    """Show hidden particles

    :param select: Select
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """(De)select all particles keys

        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
    """

def select_less(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Deselect boundary selected keys of each particle"""

def select_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all keys linked to already selected ones"""

def select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deselect: bool | None = False,
    location: collections.abc.Iterable[int] | None = (0, 0),
) -> None:
    """Select nearest particle from mouse pointer

    :param deselect: Deselect, Deselect linked keys rather than selecting them
    :param location: Location
    """

def select_more(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select keys linked to boundary selected keys of each particle"""

def select_random(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 0.5,
    seed: int | None = 0,
    action: typing.Literal["SELECT", "DESELECT"] | None = "SELECT",
    type: typing.Literal["HAIR", "POINTS"] | None = "HAIR",
) -> None:
    """Select a randomly distributed set of hair or points

        :param ratio: Ratio, Portion of items to select randomly
        :param seed: Random Seed, Seed for the random number generator
        :param action: Action, Selection action to execute

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.
        :param type: Type, Select either hair or points
    """

def select_roots(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "SELECT",
) -> None:
    """Select roots of all visible particles

        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
    """

def select_tips(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "SELECT",
) -> None:
    """Select tips of all visible particles

        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
    """

def shape_cut(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Cut hair to conform to the set shape object"""

def subdivide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Subdivide selected particles segments (adds keys)"""

def target_move_down(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move particle target down in the list"""

def target_move_up(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move particle target up in the list"""

def target_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the selected particle target"""

def unify_length(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Make selected hair the same length"""

def weight_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 1.0,
) -> None:
    """Set the weight of selected keys

    :param factor: Factor, Interpolation factor between current brush weight, and keys weights
    """
