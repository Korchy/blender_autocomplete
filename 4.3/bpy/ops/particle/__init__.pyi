import typing
import collections.abc
import typing_extensions
import bpy.types

def brush_edit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
):
    """Apply a stroke of brush to the particles

    :type execution_context: int | str | None
    :type undo: bool | None
    :param stroke: Stroke
    :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
    """

def connect_hair(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
):
    """Connect hair to the emitter mesh

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All Hair, Connect all hair systems to the emitter mesh
    :type all: bool | None
    """

def copy_particle_systems(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    space: typing.Literal["OBJECT", "WORLD"] | None = "OBJECT",
    remove_target_particles: bool | None = True,
    use_active: bool | None = False,
):
    """Copy particle systems from the active object to selected objects

        :type execution_context: int | str | None
        :type undo: bool | None
        :param space: Space, Space transform for copying from one object to another

    OBJECT
    Object -- Copy inside each object's local space.

    WORLD
    World -- Copy in world space.
        :type space: typing.Literal['OBJECT','WORLD'] | None
        :param remove_target_particles: Remove Target Particles, Remove particle systems on the target objects
        :type remove_target_particles: bool | None
        :param use_active: Use Active, Use the active particle system from the context
        :type use_active: bool | None
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["PARTICLE", "KEY"] | None = "PARTICLE",
):
    """Delete selected particles or keys

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Delete a full particle or only keys
    :type type: typing.Literal['PARTICLE','KEY'] | None
    """

def disconnect_hair(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
):
    """Disconnect hair from the emitter mesh

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All Hair, Disconnect all hair systems from the emitter mesh
    :type all: bool | None
    """

def duplicate_particle_system(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_duplicate_settings: bool | None = False,
):
    """Duplicate particle system within the active object

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_duplicate_settings: Duplicate Settings, Duplicate settings as well, so the new particle system uses its own settings
    :type use_duplicate_settings: bool | None
    """

def dupliob_copy(execution_context: int | str | None = None, undo: bool | None = None):
    """Duplicate the current instance object

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def dupliob_move_down(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Move instance object down in the list

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def dupliob_move_up(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Move instance object up in the list

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def dupliob_refresh(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Refresh list of instance objects and their weights

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def dupliob_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove the selected instance object

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def edited_clear(execution_context: int | str | None = None, undo: bool | None = None):
    """Undo all edition performed on the particle system

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def hair_dynamics_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
):
    """Add or remove a Hair Dynamics Preset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
):
    """Hide selected particles

    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: bool | None
    """

def mirror(execution_context: int | str | None = None, undo: bool | None = None):
    """Duplicate and mirror the selected particles along the local X axis

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def new(execution_context: int | str | None = None, undo: bool | None = None):
    """Add new particle settings

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def new_target(execution_context: int | str | None = None, undo: bool | None = None):
    """Add a new particle target

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def particle_edit_toggle(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Toggle particle edit mode

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def rekey(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keys_number: int | None = 2,
):
    """Change the number of keys of selected particles (root and tip keys included)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param keys_number: Number of Keys
    :type keys_number: int | None
    """

def remove_doubles(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    threshold: float | None = 0.0002,
):
    """Remove selected particles close enough of others

    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Merge Distance, Threshold distance within which particles are removed
    :type threshold: float | None
    """

def reveal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
):
    """Show hidden particles

    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | None
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """(De)select all particles' keys

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
        :type action: typing.Literal['TOGGLE','SELECT','DESELECT','INVERT'] | None
    """

def select_less(execution_context: int | str | None = None, undo: bool | None = None):
    """Deselect boundary selected keys of each particle

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked(execution_context: int | str | None = None, undo: bool | None = None):
    """Select all keys linked to already selected ones

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deselect: bool | None = False,
    location: collections.abc.Iterable[int] | None = (0, 0),
):
    """Select nearest particle from mouse pointer

    :type execution_context: int | str | None
    :type undo: bool | None
    :param deselect: Deselect, Deselect linked keys rather than selecting them
    :type deselect: bool | None
    :param location: Location
    :type location: collections.abc.Iterable[int] | None
    """

def select_more(execution_context: int | str | None = None, undo: bool | None = None):
    """Select keys linked to boundary selected keys of each particle

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_random(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 0.5,
    seed: int | None = 0,
    action: typing.Literal["SELECT", "DESELECT"] | None = "SELECT",
    type: typing.Literal["HAIR", "POINTS"] | None = "HAIR",
):
    """Select a randomly distributed set of hair or points

        :type execution_context: int | str | None
        :type undo: bool | None
        :param ratio: Ratio, Portion of items to select randomly
        :type ratio: float | None
        :param seed: Random Seed, Seed for the random number generator
        :type seed: int | None
        :param action: Action, Selection action to execute

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.
        :type action: typing.Literal['SELECT','DESELECT'] | None
        :param type: Type, Select either hair or points
        :type type: typing.Literal['HAIR','POINTS'] | None
    """

def select_roots(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "SELECT",
):
    """Select roots of all visible particles

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
        :type action: typing.Literal['TOGGLE','SELECT','DESELECT','INVERT'] | None
    """

def select_tips(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "SELECT",
):
    """Select tips of all visible particles

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
        :type action: typing.Literal['TOGGLE','SELECT','DESELECT','INVERT'] | None
    """

def shape_cut(execution_context: int | str | None = None, undo: bool | None = None):
    """Cut hair to conform to the set shape object

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def subdivide(execution_context: int | str | None = None, undo: bool | None = None):
    """Subdivide selected particles segments (adds keys)

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def target_move_down(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Move particle target down in the list

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def target_move_up(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Move particle target up in the list

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def target_remove(execution_context: int | str | None = None, undo: bool | None = None):
    """Remove the selected particle target

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def unify_length(execution_context: int | str | None = None, undo: bool | None = None):
    """Make selected hair the same length

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def weight_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 1.0,
):
    """Set the weight of selected keys

    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, Interpolation factor between current brush weight, and keys' weights
    :type factor: float | None
    """
