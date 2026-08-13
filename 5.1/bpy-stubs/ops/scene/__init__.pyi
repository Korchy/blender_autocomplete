import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete active scene

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class drop_scene_asset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        session_uid: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Import scene and set it as the active one in the window

        :param execution_context:
        :param undo:
        :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class freestyle_add_edge_marks_to_keying_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add the data paths to the Freestyle Edge Mark property of selected edges to the active keying set

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class freestyle_add_face_marks_to_keying_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add the data paths to the Freestyle Face Mark property of selected polygons to the active keying set

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class freestyle_alpha_modifier_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            bpy.stub_internal.rna_enums.LinestyleAlphaModifierTypeItems
        ]
        | None = "ALONG_STROKE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add an alpha transparency modifier to the line style associated with the active lineset

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class freestyle_color_modifier_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            bpy.stub_internal.rna_enums.LinestyleColorModifierTypeItems
        ]
        | None = "ALONG_STROKE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a line color modifier to the line style associated with the active lineset

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class freestyle_fill_range_by_selection(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["COLOR", "ALPHA", "THICKNESS"] | None = "COLOR",
        name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Fill the Range Min/Max entries by the min/max distance between selected mesh objects and the source object (either a user-specified object or the active camera)

                :param execution_context:
                :param undo:
                :param type: Type, Type of the modifier to work on (optional)

        COLOR
        Color -- Color modifier type.

        ALPHA
        Alpha -- Alpha modifier type.

        THICKNESS
        Thickness -- Thickness modifier type.
                :param name: Name, Name of the modifier to work on (optional, never None)
                :return: Result of the operator call.
        """

class freestyle_geometry_modifier_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            bpy.stub_internal.rna_enums.LinestyleGeometryModifierTypeItems
        ]
        | None = "2D_OFFSET",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a stroke geometry modifier to the line style associated with the active lineset

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class freestyle_lineset_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a line set into the list of line sets

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class freestyle_lineset_copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy the active line set to the internal clipboard

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class freestyle_lineset_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal["UP", "DOWN"] | None = "UP",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change the position of the active line set within the list of line sets

        :param execution_context:
        :param undo:
        :param direction: Direction, Direction to move the active line set towards (optional)
        :return: Result of the operator call.
        """

class freestyle_lineset_paste(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Paste the internal clipboard content to the active line set

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class freestyle_lineset_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the active line set from the list of line sets

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class freestyle_linestyle_new(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a new line style, reusable by multiple line sets

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class freestyle_modifier_copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate the modifier within the list of modifiers

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class freestyle_modifier_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal["UP", "DOWN"] | None = "UP",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move the modifier within the list of modifiers

        :param execution_context:
        :param undo:
        :param direction: Direction, Direction to move the chosen modifier towards (optional)
        :return: Result of the operator call.
        """

class freestyle_modifier_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the modifier from the list of modifiers

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class freestyle_module_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a style module into the list of modules

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class freestyle_module_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal["UP", "DOWN"] | None = "UP",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change the position of the style module within in the list of style modules

        :param execution_context:
        :param undo:
        :param direction: Direction, Direction to move the chosen style module towards (optional)
        :return: Result of the operator call.
        """

class freestyle_module_open(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        make_internal: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open a style module file

        :param execution_context:
        :param undo:
        :param filepath: filepath, (optional, never None)
        :param make_internal: Make internal, Make module file internal after loading (optional)
        :return: Result of the operator call.
        """

class freestyle_module_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the style module from the stack

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class freestyle_stroke_material_create(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create Freestyle stroke material for testing

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class freestyle_thickness_modifier_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            bpy.stub_internal.rna_enums.LinestyleThicknessModifierTypeItems
        ]
        | None = "ALONG_STROKE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a line thickness modifier to the line style associated with the active lineset

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class gltf2_action_filter_refresh(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Refresh list of actions

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class gpencil_brush_preset_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        remove_name: bool | None = False,
        remove_active: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add or remove Grease Pencil brush preset

        :param execution_context:
        :param undo:
        :param name: Name, Name of the preset, used to make the path name (optional, never None)
        :param remove_name: remove_name, (optional)
        :param remove_active: remove_active, (optional)
        :return: Result of the operator call.
        """

class gpencil_material_preset_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        remove_name: bool | None = False,
        remove_active: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add or remove Grease Pencil material preset

        :param execution_context:
        :param undo:
        :param name: Name, Name of the preset, used to make the path name (optional, never None)
        :param remove_name: remove_name, (optional)
        :param remove_active: remove_active, (optional)
        :return: Result of the operator call.
        """

class new(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["NEW", "EMPTY", "LINK_COPY", "FULL_COPY"] | None = "NEW",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add new scene by type

                :param execution_context:
                :param undo:
                :param type: Type, (optional)

        NEW
        New -- Add a new, empty scene with default settings.

        EMPTY
        Copy Settings -- Add a new, empty scene, and copy settings from the current scene.

        LINK_COPY
        Linked Copy -- Link in the collections from the current scene (shallow copy).

        FULL_COPY
        Full Copy -- Make a full copy of the current scene.
                :return: Result of the operator call.
        """

class new_sequencer(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["NEW", "EMPTY", "LINK_COPY", "FULL_COPY"] | None = "NEW",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add new scene by type in the sequence editor and assign to active strip

                :param execution_context:
                :param undo:
                :param type: Type, (optional)

        NEW
        New -- Add a new, empty scene with default settings.

        EMPTY
        Copy Settings -- Add a new, empty scene, and copy settings from the current scene.

        LINK_COPY
        Linked Copy -- Link in the collections from the current scene (shallow copy).

        FULL_COPY
        Full Copy -- Make a full copy of the current scene.
                :return: Result of the operator call.
        """

class new_sequencer_scene(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["NEW", "EMPTY", "LINK_COPY", "FULL_COPY"] | None = "NEW",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add new scene to be used by the sequencer

                :param execution_context:
                :param undo:
                :param type: Type, (optional)

        NEW
        New -- Add a new, empty scene with default settings.

        EMPTY
        Copy Settings -- Add a new, empty scene, and copy settings from the current scene.

        LINK_COPY
        Linked Copy -- Link in the collections from the current scene (shallow copy).

        FULL_COPY
        Full Copy -- Make a full copy of the current scene.
                :return: Result of the operator call.
        """

class render_view_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a render view

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class render_view_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the selected render view

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_layer_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["NEW", "COPY", "EMPTY"] | None = "NEW",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a view layer

                :param execution_context:
                :param undo:
                :param type: Type, (optional)

        NEW
        New -- Add a new view layer.

        COPY
        Copy Settings -- Copy settings of current view layer.

        EMPTY
        Blank -- Add a new view layer with all collections disabled.
                :return: Result of the operator call.
        """

class view_layer_add_aov(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a Shader AOV

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_layer_add_lightgroup(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a Light Group

        :param execution_context:
        :param undo:
        :param name: Name, Name of newly created lightgroup (optional, never None)
        :return: Result of the operator call.
        """

class view_layer_add_used_lightgroups(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add all used Light Groups

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_layer_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the selected view layer

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_layer_remove_aov(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove Active AOV

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_layer_remove_lightgroup(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove Active Lightgroup

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_layer_remove_unused_lightgroups(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove all unused Light Groups

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
