import typing
import collections.abc
import typing_extensions
import bpy._typing.rna_enums

def bake_to_keyframes(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame_start: int | None = 1,
    frame_end: int | None = 250,
    step: int | None = 1,
):
    """Bake rigid body transformations of selected objects to keyframes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame_start: Start Frame, Start frame for baking
    :type frame_start: int | None
    :param frame_end: End Frame, End frame for baking
    :type frame_end: int | None
    :param step: Frame Step, Frame Step
    :type step: int | None
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
):
    """Create rigid body constraints between selected rigid bodies

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
        :type con_type: typing.Literal['FIXED','POINT','HINGE','SLIDER','PISTON','GENERIC','GENERIC_SPRING','MOTOR'] | None
        :param pivot_type: Location, Constraint pivot location

    CENTER
    Center -- Pivot location is between the constrained rigid bodies.

    ACTIVE
    Active -- Pivot location is at the active object position.

    SELECTED
    Selected -- Pivot location is at the selected object position.
        :type pivot_type: typing.Literal['CENTER','ACTIVE','SELECTED'] | None
        :param connection_pattern: Connection Pattern, Pattern used to connect objects

    SELECTED_TO_ACTIVE
    Selected to Active -- Connect selected objects to the active object.

    CHAIN_DISTANCE
    Chain by Distance -- Connect objects as a chain based on distance, starting at the active object.
        :type connection_pattern: typing.Literal['SELECTED_TO_ACTIVE','CHAIN_DISTANCE'] | None
    """

def constraint_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy._typing.rna_enums.RigidbodyConstraintTypeItems | None = "FIXED",
):
    """Add Rigid Body Constraint to active object

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Rigid Body Constraint Type
    :type type: bpy._typing.rna_enums.RigidbodyConstraintTypeItems | None
    """

def constraint_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove Rigid Body Constraint from Object

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def mass_calculate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    material: str | None = "DEFAULT",
    density: float | None = 1.0,
):
    """Automatically calculate mass values for Rigid Body Objects based on volume

    :type execution_context: int | str | None
    :type undo: bool | None
    :param material: Material Preset, Type of material that objects are made of (determines material density)
    :type material: str | None
    :param density: Density, Density value (kg/m^3), allows custom value if the 'Custom' preset is used
    :type density: float | None
    """

def object_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy._typing.rna_enums.RigidbodyObjectTypeItems | None = "ACTIVE",
):
    """Add active object as Rigid Body

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Rigid Body Type
    :type type: bpy._typing.rna_enums.RigidbodyObjectTypeItems | None
    """

def object_remove(execution_context: int | str | None = None, undo: bool | None = None):
    """Remove Rigid Body settings from Object

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def object_settings_copy(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Copy Rigid Body settings from active object to selected

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def objects_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy._typing.rna_enums.RigidbodyObjectTypeItems | None = "ACTIVE",
):
    """Add selected objects as Rigid Bodies

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Rigid Body Type
    :type type: bpy._typing.rna_enums.RigidbodyObjectTypeItems | None
    """

def objects_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove selected objects from Rigid Body simulation

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def shape_change(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy._typing.rna_enums.RigidbodyObjectShapeItems | None = "MESH",
):
    """Change collision shapes for selected Rigid Body Objects

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Rigid Body Shape
    :type type: bpy._typing.rna_enums.RigidbodyObjectShapeItems | None
    """

def world_add(execution_context: int | str | None = None, undo: bool | None = None):
    """Add Rigid Body simulation world to the current scene

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def world_remove(execution_context: int | str | None = None, undo: bool | None = None):
    """Remove Rigid Body simulation world from the current scene

    :type execution_context: int | str | None
    :type undo: bool | None
    """
