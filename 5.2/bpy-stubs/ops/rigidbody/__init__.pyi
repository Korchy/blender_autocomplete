import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class bake_to_keyframes(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        frame_start: int | None = 1,
        frame_end: int | None = 250,
        step: int | None = 1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Bake rigid body transformations of selected objects to keyframes

        :param execution_context:
        :param undo:
        :param frame_start: Start Frame, Start frame for baking (in [0, 300000], optional)
        :param frame_end: End Frame, End frame for baking (in [1, 300000], optional)
        :param step: Frame Step, Frame Step (in [1, 120], optional)
        :return: Result of the operator call.
        """

class connect(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create rigid body constraints between selected rigid bodies

                :param execution_context:
                :param undo:
                :param con_type: Type, Type of generated constraint (optional)

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
                :param pivot_type: Location, Constraint pivot location (optional)

        CENTER
        Center -- Pivot location is between the constrained rigid bodies.

        ACTIVE
        Active -- Pivot location is at the active object position.

        SELECTED
        Selected -- Pivot location is at the selected object position.
                :param connection_pattern: Connection Pattern, Pattern used to connect objects (optional)

        SELECTED_TO_ACTIVE
        Selected to Active -- Connect selected objects to the active object.

        CHAIN_DISTANCE
        Chain by Distance -- Connect objects as a chain based on distance, starting at the active object.
                :return: Result of the operator call.
        """

class constraint_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[bpy.stub_internal.rna_enums.RigidbodyConstraintTypeItems]
        | None = "FIXED",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add Rigid Body Constraint to active object

        :param execution_context:
        :param undo:
        :param type: Rigid Body Constraint Type, (optional)
        :return: Result of the operator call.
        """

class constraint_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove Rigid Body Constraint from Object

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class mass_calculate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        material: typing.Literal["DEFAULT"] | None = "DEFAULT",
        density: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Automatically calculate mass values for Rigid Body Objects based on volume

        :param execution_context:
        :param undo:
        :param material: Material Preset, Type of material that objects are made of (determines material density) (optional)
        :param density: Density, Density value (kg/m^3), allows custom value if the Custom preset is used (in [1.17549e-38, inf], optional)
        :return: Result of the operator call.
        """

class object_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[bpy.stub_internal.rna_enums.RigidbodyObjectTypeItems]
        | None = "ACTIVE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add active object as Rigid Body

        :param execution_context:
        :param undo:
        :param type: Rigid Body Type, (optional)
        :return: Result of the operator call.
        """

class object_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove Rigid Body settings from Object

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class object_settings_copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy Rigid Body settings from active object to selected

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class objects_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[bpy.stub_internal.rna_enums.RigidbodyObjectTypeItems]
        | None = "ACTIVE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add selected objects as Rigid Bodies

        :param execution_context:
        :param undo:
        :param type: Rigid Body Type, (optional)
        :return: Result of the operator call.
        """

class objects_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove selected objects from Rigid Body simulation

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class shape_change(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[bpy.stub_internal.rna_enums.RigidbodyObjectShapeItems]
        | None = "MESH",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change collision shapes for selected Rigid Body Objects

        :param execution_context:
        :param undo:
        :param type: Rigid Body Shape, (optional)
        :return: Result of the operator call.
        """

class world_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add Rigid Body simulation world to the current scene

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class world_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove Rigid Body simulation world from the current scene

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
