import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def bake_to_keyframes(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    frame_start: typing.Any | None = 1,
    frame_end: typing.Any | None = 250,
    step: typing.Any | None = 1,
):
    """Bake rigid body transformations of selected objects to keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame_start: Start Frame, Start frame for baking
    :type frame_start: typing.Any | None
    :param frame_end: End Frame, End frame for baking
    :type frame_end: typing.Any | None
    :param step: Frame Step, Frame Step
    :type step: typing.Any | None
    """

    ...

def connect(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    con_type: str | None = "FIXED",
    pivot_type: str | None = "CENTER",
    connection_pattern: str | None = "SELECTED_TO_ACTIVE",
):
    """Create rigid body constraints between selected rigid bodies

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param con_type: Type, Type of generated constraint

    FIXED
    Fixed -- Glue rigid bodies together.

    POINT
    Point -- Constrain rigid bodies to move around common pivot point.

    HINGE
    Hinge -- Restrict rigid body rotation to one axis.

    SLIDER
    Slider -- Restrict rigid body translation to one axis.

    PISTON
    Piston -- Restrict rigid body translation and rotation to one axis.

    GENERIC
    Generic -- Restrict translation and rotation to specified axes.

    GENERIC_SPRING
    Generic Spring -- Restrict translation and rotation to specified axes with springs.

    MOTOR
    Motor -- Drive rigid body around or along an axis.
        :type con_type: str | None
        :param pivot_type: Location, Constraint pivot location

    CENTER
    Center -- Pivot location is between the constrained rigid bodies.

    ACTIVE
    Active -- Pivot location is at the active object position.

    SELECTED
    Selected -- Pivot location is at the selected object position.
        :type pivot_type: str | None
        :param connection_pattern: Connection Pattern, Pattern used to connect objects

    SELECTED_TO_ACTIVE
    Selected to Active -- Connect selected objects to the active object.

    CHAIN_DISTANCE
    Chain by Distance -- Connect objects as a chain based on distance, starting at the active object.
        :type connection_pattern: str | None
    """

    ...

def constraint_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "FIXED",
):
    """Add Rigid Body Constraint to active object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Rigid Body Constraint Type
    :type type: str | None
    """

    ...

def constraint_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove Rigid Body Constraint from Object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def mass_calculate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    material: str | None = "DEFAULT",
    density: typing.Any | None = 1.0,
):
    """Automatically calculate mass values for Rigid Body Objects based on volume

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param material: Material Preset, Type of material that objects are made of (determines material density)
    :type material: str | None
    :param density: Density, Density value (kg/m^3), allows custom value if the 'Custom' preset is used
    :type density: typing.Any | None
    """

    ...

def object_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "ACTIVE",
):
    """Add active object as Rigid Body

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Rigid Body Type
    :type type: str | None
    """

    ...

def object_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove Rigid Body settings from Object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def object_settings_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy Rigid Body settings from active object to selected

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def objects_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "ACTIVE",
):
    """Add selected objects as Rigid Bodies

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Rigid Body Type
    :type type: str | None
    """

    ...

def objects_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove selected objects from Rigid Body simulation

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def shape_change(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "MESH",
):
    """Change collision shapes for selected Rigid Body Objects

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Rigid Body Shape
    :type type: str | None
    """

    ...

def world_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add Rigid Body simulation world to the current scene

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def world_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove Rigid Body simulation world from the current scene

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...
