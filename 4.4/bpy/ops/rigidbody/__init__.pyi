import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums

def bake_to_keyframes(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame_start: int | None = 1,
    frame_end: int | None = 250,
    step: int | None = 1,
) -> None:
    """Bake rigid body transformations of selected objects to keyframes

    :param frame_start: Start Frame, Start frame for baking
    :param frame_end: End Frame, End frame for baking
    :param step: Frame Step, Frame Step
    """

def connect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    con_type: typing.Literal[
        "FIXED",
        "POINT",
        "HINGE",
        "SLIDER",
        "PISTON",
        "GENERIC",
        "GENERIC_SPRING",
        "MOTOR",
    ]
    | None = "FIXED",
    pivot_type: typing.Literal["CENTER", "ACTIVE", "SELECTED"] | None = "CENTER",
    connection_pattern: typing.Literal["SELECTED_TO_ACTIVE", "CHAIN_DISTANCE"]
    | None = "SELECTED_TO_ACTIVE",
) -> None:
    """Create rigid body constraints between selected rigid bodies

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
        :param pivot_type: Location, Constraint pivot location

    CENTER
    Center -- Pivot location is between the constrained rigid bodies.

    ACTIVE
    Active -- Pivot location is at the active object position.

    SELECTED
    Selected -- Pivot location is at the selected object position.
        :param connection_pattern: Connection Pattern, Pattern used to connect objects

    SELECTED_TO_ACTIVE
    Selected to Active -- Connect selected objects to the active object.

    CHAIN_DISTANCE
    Chain by Distance -- Connect objects as a chain based on distance, starting at the active object.
    """

def constraint_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.RigidbodyConstraintTypeItems | None = "FIXED",
) -> None:
    """Add Rigid Body Constraint to active object

    :param type: Rigid Body Constraint Type
    """

def constraint_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove Rigid Body Constraint from Object"""

def mass_calculate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    material: str | None = "DEFAULT",
    density: float | None = 1.0,
) -> None:
    """Automatically calculate mass values for Rigid Body Objects based on volume

    :param material: Material Preset, Type of material that objects are made of (determines material density)
    :param density: Density, Density value (kg/m^3), allows custom value if the Custom preset is used
    """

def object_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.RigidbodyObjectTypeItems | None = "ACTIVE",
) -> None:
    """Add active object as Rigid Body

    :param type: Rigid Body Type
    """

def object_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove Rigid Body settings from Object"""

def object_settings_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy Rigid Body settings from active object to selected"""

def objects_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.RigidbodyObjectTypeItems | None = "ACTIVE",
) -> None:
    """Add selected objects as Rigid Bodies

    :param type: Rigid Body Type
    """

def objects_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove selected objects from Rigid Body simulation"""

def shape_change(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.RigidbodyObjectShapeItems | None = "MESH",
) -> None:
    """Change collision shapes for selected Rigid Body Objects

    :param type: Rigid Body Shape
    """

def world_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add Rigid Body simulation world to the current scene"""

def world_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove Rigid Body simulation world from the current scene"""
