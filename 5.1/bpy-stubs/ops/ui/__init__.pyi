import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class assign_default_button(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set this propertys current value as the new default

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class button_execute(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        skip_depressed: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Presses active button

        :param execution_context:
        :param undo:
        :param skip_depressed: Skip Depressed, (optional)
        :return: Result of the operator call.
        """

class button_string_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Unsets the text of the active button

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class copy_as_driver_button(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a new driver with this property as input, and copy it to the internal clipboard. Use Paste Driver to add it to the target property, or Paste Driver Variables to extend an existing driver

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class copy_data_path_button(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        full_path: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy the RNA data path for this property to the clipboard

        :param execution_context:
        :param undo:
        :param full_path: full_path, Copy full data path (optional)
        :return: Result of the operator call.
        """

class copy_driver_to_selected_button(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        all: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy the propertys driver from the active item to the same property of all selected items, if the same property exists

        :param execution_context:
        :param undo:
        :param all: All, Copy to selected the drivers of all elements of the array (optional)
        :return: Result of the operator call.
        """

class copy_python_command_button(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy the Python command matching this button

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class copy_to_selected_button(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        all: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy the propertys value from the active item to the same property of all selected items if the same property exists

        :param execution_context:
        :param undo:
        :param all: All, Copy to selected all elements of the array (optional)
        :return: Result of the operator call.
        """

class drop_color(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        color: collections.abc.Sequence[float] | None = (0.0, 0.0, 0.0, 0.0),
        gamma: bool | None = False,
        has_alpha: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Drop colors to buttons

        :param execution_context:
        :param undo:
        :param color: Color, Source color (array of 4 items, in [0, inf], optional)
        :param gamma: Gamma Corrected, The source color is gamma corrected (optional)
        :param has_alpha: Has Alpha, The source color contains an Alpha component (optional)
        :return: Result of the operator call.
        """

class drop_material(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        session_uid: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Drag material to Material slots in Properties

        :param execution_context:
        :param undo:
        :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class drop_name(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        string: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Drop name to button

        :param execution_context:
        :param undo:
        :param string: String, The string value to drop into the button (optional, never None)
        :return: Result of the operator call.
        """

class editsource(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Edit UI source code of the active button

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class eyedropper_bone(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Sample a bone from the 3D View or the Outliner to store in a property

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class eyedropper_color(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        prop_data_path: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Sample a color from the Blender window to store in a property

        :param execution_context:
        :param undo:
        :param prop_data_path: Data Path, Path of property to be set with the depth (optional, never None)
        :return: Result of the operator call.
        """

class eyedropper_colorramp(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Sample a color band

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class eyedropper_colorramp_point(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Point-sample a color band

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class eyedropper_depth(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        prop_data_path: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Sample depth from the 3D view

        :param execution_context:
        :param undo:
        :param prop_data_path: Data Path, Path of property to be set with the depth (optional, never None)
        :return: Result of the operator call.
        """

class eyedropper_driver(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mapping_type: typing.Literal[
            "SINGLE_MANY", "DIRECT", "MATCH", "NONE_ALL", "NONE_SINGLE"
        ]
        | None = "SINGLE_MANY",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Pick a property to use as a driver target

                :param execution_context:
                :param undo:
                :param mapping_type: Mapping Type, Method used to match target and driven properties (optional)

        SINGLE_MANY
        All from Target -- Drive all components of this property using the target picked.

        DIRECT
        Single from Target -- Drive this component of this property using the target picked.

        MATCH
        Match Indices -- Create drivers for each pair of corresponding elements.

        NONE_ALL
        Manually Create Later -- Create drivers for all properties without assigning any targets yet.

        NONE_SINGLE
        Manually Create Later (Single) -- Create driver for this property only and without assigning any targets yet.
                :return: Result of the operator call.
        """

class eyedropper_grease_pencil_color(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["MATERIAL", "PALETTE", "BRUSH"] | None = "MATERIAL",
        material_mode: typing.Literal["STROKE", "FILL", "BOTH"] | None = "STROKE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Sample a color from the Blender Window and create Grease Pencil material

        :param execution_context:
        :param undo:
        :param mode: Mode, (optional)
        :param material_mode: Material Mode, (optional)
        :return: Result of the operator call.
        """

class eyedropper_id(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Sample a data-block from the 3D View to store in a property

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class jump_to_target_button(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Switch to the target object or bone

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class list_start_filter(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Start entering filter text for the list in focus

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class override_add_button(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        all: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create an override operation

        :param execution_context:
        :param undo:
        :param all: All, Add overrides for all elements of the array (optional)
        :return: Result of the operator call.
        """

class override_idtemplate_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete the selected local override and relink its usages to the linked data-block if possible, else reset it and mark it as non editable

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class override_idtemplate_make(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a local override of the selected linked data-block, and its hierarchy of dependencies

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class override_idtemplate_reset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset the selected local override to its linked reference values

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class override_remove_button(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        all: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove an override operation

        :param execution_context:
        :param undo:
        :param all: All, Reset to default values all elements of the array (optional)
        :return: Result of the operator call.
        """

class reloadtranslation(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Force a full reload of UI translation

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class reset_default_button(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        all: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset this propertys value to its default value

        :param execution_context:
        :param undo:
        :param all: All, Reset to default values all elements of the array (optional)
        :return: Result of the operator call.
        """

class unset_property_button(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear the property and use default or generated value in operators

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_drop(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Drag and drop onto a data-set or item within the data-set

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_item_delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete selected list item

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_item_rename(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Rename the active item in the data-set view

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_item_select(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        wait_to_deselect_others: bool | None = False,
        use_select_on_click: bool | None = False,
        mouse_x: int | None = 0,
        mouse_y: int | None = 0,
        extend: bool | None = False,
        range_select: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Activate selected view item

        :param execution_context:
        :param undo:
        :param wait_to_deselect_others: Wait to Deselect Others, (optional)
        :param use_select_on_click: Act on Click, Instead of selecting on mouse press, wait to see if theres drag event. Otherwise select on mouse release (optional)
        :param mouse_x: Mouse X, (in [-inf, inf], optional)
        :param mouse_y: Mouse Y, (in [-inf, inf], optional)
        :param extend: extend, Extend Selection (optional)
        :param range_select: Range Select, Select all between clicked and active items (optional)
        :return: Result of the operator call.
        """

class view_scroll(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_start_filter(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Start entering filter text for the data-set in focus

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
