import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete active scene"""

def drop_scene_asset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    session_uid: int | None = 0,
) -> None:
    """Import scene and set it as the active one in the window

    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    """

def freestyle_add_edge_marks_to_keying_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add the data paths to the Freestyle Edge Mark property of selected edges to the active keying set"""

def freestyle_add_face_marks_to_keying_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add the data paths to the Freestyle Face Mark property of selected polygons to the active keying set"""

def freestyle_alpha_modifier_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.LinestyleAlphaModifierTypeItems
    | None = "ALONG_STROKE",
) -> None:
    """Add an alpha transparency modifier to the line style associated with the active lineset

    :param type: Type
    """

def freestyle_color_modifier_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.LinestyleColorModifierTypeItems
    | None = "ALONG_STROKE",
) -> None:
    """Add a line color modifier to the line style associated with the active lineset

    :param type: Type
    """

def freestyle_fill_range_by_selection(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["COLOR", "ALPHA", "THICKNESS"] | None = "COLOR",
    name: str = "",
) -> None:
    """Fill the Range Min/Max entries by the min/max distance between selected mesh objects and the source object (either a user-specified object or the active camera)

        :param type: Type, Type of the modifier to work on

    COLOR
    Color -- Color modifier type.

    ALPHA
    Alpha -- Alpha modifier type.

    THICKNESS
    Thickness -- Thickness modifier type.
        :param name: Name, Name of the modifier to work on
    """

def freestyle_geometry_modifier_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.LinestyleGeometryModifierTypeItems
    | None = "2D_OFFSET",
) -> None:
    """Add a stroke geometry modifier to the line style associated with the active lineset

    :param type: Type
    """

def freestyle_lineset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a line set into the list of line sets"""

def freestyle_lineset_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the active line set to the internal clipboard"""

def freestyle_lineset_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Change the position of the active line set within the list of line sets

    :param direction: Direction, Direction to move the active line set towards
    """

def freestyle_lineset_paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Paste the internal clipboard content to the active line set"""

def freestyle_lineset_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the active line set from the list of line sets"""

def freestyle_linestyle_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create a new line style, reusable by multiple line sets"""

def freestyle_modifier_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Duplicate the modifier within the list of modifiers"""

def freestyle_modifier_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move the modifier within the list of modifiers

    :param direction: Direction, Direction to move the chosen modifier towards
    """

def freestyle_modifier_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the modifier from the list of modifiers"""

def freestyle_module_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a style module into the list of modules"""

def freestyle_module_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Change the position of the style module within in the list of style modules

    :param direction: Direction, Direction to move the chosen style module towards
    """

def freestyle_module_open(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    make_internal: bool | None = True,
) -> None:
    """Open a style module file

    :param filepath: filepath
    :param make_internal: Make internal, Make module file internal after loading
    """

def freestyle_module_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the style module from the stack"""

def freestyle_stroke_material_create(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create Freestyle stroke material for testing"""

def freestyle_thickness_modifier_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.LinestyleThicknessModifierTypeItems
    | None = "ALONG_STROKE",
) -> None:
    """Add a line thickness modifier to the line style associated with the active lineset

    :param type: Type
    """

def gltf2_action_filter_refresh(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Refresh list of actions"""

def gpencil_brush_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add or remove Grease Pencil brush preset

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def gpencil_material_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add or remove Grease Pencil material preset

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["NEW", "EMPTY", "LINK_COPY", "FULL_COPY"] | None = "NEW",
) -> None:
    """Add new scene by type

        :param type: Type

    NEW
    New -- Add a new, empty scene with default settings.

    EMPTY
    Copy Settings -- Add a new, empty scene, and copy settings from the current scene.

    LINK_COPY
    Linked Copy -- Link in the collections from the current scene (shallow copy).

    FULL_COPY
    Full Copy -- Make a full copy of the current scene.
    """

def new_sequencer(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["NEW", "EMPTY", "LINK_COPY", "FULL_COPY"] | None = "NEW",
) -> None:
    """Add new scene by type in the sequence editor and assign to active strip

        :param type: Type

    NEW
    New -- Add a new, empty scene with default settings.

    EMPTY
    Copy Settings -- Add a new, empty scene, and copy settings from the current scene.

    LINK_COPY
    Linked Copy -- Link in the collections from the current scene (shallow copy).

    FULL_COPY
    Full Copy -- Make a full copy of the current scene.
    """

def new_sequencer_scene(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["NEW", "EMPTY", "LINK_COPY", "FULL_COPY"] | None = "NEW",
) -> None:
    """Add new scene to be used by the sequencer

        :param type: Type

    NEW
    New -- Add a new, empty scene with default settings.

    EMPTY
    Copy Settings -- Add a new, empty scene, and copy settings from the current scene.

    LINK_COPY
    Linked Copy -- Link in the collections from the current scene (shallow copy).

    FULL_COPY
    Full Copy -- Make a full copy of the current scene.
    """

def render_view_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a render view"""

def render_view_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the selected render view"""

def view_layer_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["NEW", "COPY", "EMPTY"] | None = "NEW",
) -> None:
    """Add a view layer

        :param type: Type

    NEW
    New -- Add a new view layer.

    COPY
    Copy Settings -- Copy settings of current view layer.

    EMPTY
    Blank -- Add a new view layer with all collections disabled.
    """

def view_layer_add_aov(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a Shader AOV"""

def view_layer_add_lightgroup(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
) -> None:
    """Add a Light Group

    :param name: Name, Name of newly created lightgroup
    """

def view_layer_add_used_lightgroups(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add all used Light Groups"""

def view_layer_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the selected view layer"""

def view_layer_remove_aov(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove Active AOV"""

def view_layer_remove_lightgroup(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove Active Lightgroup"""

def view_layer_remove_unused_lightgroups(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove all unused Light Groups"""
