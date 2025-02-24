import typing
import collections.abc
import typing_extensions
import bpy._typing.rna_enums

def delete(execution_context: int | str | None = None, undo: bool | None = None):
    """Delete active scene

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_add_edge_marks_to_keying_set(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add the data paths to the Freestyle Edge Mark property of selected edges to the active keying set

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_add_face_marks_to_keying_set(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add the data paths to the Freestyle Face Mark property of selected polygons to the active keying set

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_alpha_modifier_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy._typing.rna_enums.LinestyleAlphaModifierTypeItems | None = "ALONG_STROKE",
):
    """Add an alpha transparency modifier to the line style associated with the active lineset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy._typing.rna_enums.LinestyleAlphaModifierTypeItems | None
    """

def freestyle_color_modifier_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy._typing.rna_enums.LinestyleColorModifierTypeItems | None = "ALONG_STROKE",
):
    """Add a line color modifier to the line style associated with the active lineset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy._typing.rna_enums.LinestyleColorModifierTypeItems | None
    """

def freestyle_fill_range_by_selection(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["COLOR", "ALPHA", "THICKNESS"] | None = "COLOR",
    name: str = "",
):
    """Fill the Range Min/Max entries by the min/max distance between selected mesh objects and the source object (either a user-specified object or the active camera)

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Type of the modifier to work on

    COLOR
    Color -- Color modifier type.

    ALPHA
    Alpha -- Alpha modifier type.

    THICKNESS
    Thickness -- Thickness modifier type.
        :type type: typing.Literal['COLOR','ALPHA','THICKNESS'] | None
        :param name: Name, Name of the modifier to work on
        :type name: str
    """

def freestyle_geometry_modifier_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy._typing.rna_enums.LinestyleGeometryModifierTypeItems | None = "2D_OFFSET",
):
    """Add a stroke geometry modifier to the line style associated with the active lineset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy._typing.rna_enums.LinestyleGeometryModifierTypeItems | None
    """

def freestyle_lineset_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add a line set into the list of line sets

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_lineset_copy(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Copy the active line set to the internal clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_lineset_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Change the position of the active line set within the list of line sets

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to move the active line set towards
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def freestyle_lineset_paste(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Paste the internal clipboard content to the active line set

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_lineset_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove the active line set from the list of line sets

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_linestyle_new(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Create a new line style, reusable by multiple line sets

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_modifier_copy(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Duplicate the modifier within the list of modifiers

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_modifier_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move the modifier within the list of modifiers

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to move the chosen modifier towards
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def freestyle_modifier_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove the modifier from the list of modifiers

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_module_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add a style module into the list of modules

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_module_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Change the position of the style module within in the list of style modules

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to move the chosen style module towards
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def freestyle_module_open(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    make_internal: bool | None = True,
):
    """Open a style module file

    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str
    :param make_internal: Make internal, Make module file internal after loading
    :type make_internal: bool | None
    """

def freestyle_module_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove the style module from the stack

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_stroke_material_create(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Create Freestyle stroke material for testing

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_thickness_modifier_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy._typing.rna_enums.LinestyleThicknessModifierTypeItems
    | None = "ALONG_STROKE",
):
    """Add a line thickness modifier to the line style associated with the active lineset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy._typing.rna_enums.LinestyleThicknessModifierTypeItems | None
    """

def gltf2_action_filter_refresh(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Refresh list of actions

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def gpencil_brush_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
):
    """Add or remove grease pencil brush preset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def gpencil_material_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
):
    """Add or remove grease pencil material preset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["NEW", "EMPTY", "LINK_COPY", "FULL_COPY"] | None = "NEW",
):
    """Add new scene by type

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    NEW
    New -- Add a new, empty scene with default settings.

    EMPTY
    Copy Settings -- Add a new, empty scene, and copy settings from the current scene.

    LINK_COPY
    Linked Copy -- Link in the collections from the current scene (shallow copy).

    FULL_COPY
    Full Copy -- Make a full copy of the current scene.
        :type type: typing.Literal['NEW','EMPTY','LINK_COPY','FULL_COPY'] | None
    """

def new_sequencer(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["NEW", "EMPTY", "LINK_COPY", "FULL_COPY"] | None = "NEW",
):
    """Add new scene by type in the sequence editor and assign to active strip

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    NEW
    New -- Add a new, empty scene with default settings.

    EMPTY
    Copy Settings -- Add a new, empty scene, and copy settings from the current scene.

    LINK_COPY
    Linked Copy -- Link in the collections from the current scene (shallow copy).

    FULL_COPY
    Full Copy -- Make a full copy of the current scene.
        :type type: typing.Literal['NEW','EMPTY','LINK_COPY','FULL_COPY'] | None
    """

def render_view_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add a render view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def render_view_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove the selected render view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_layer_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["NEW", "COPY", "EMPTY"] | None = "NEW",
):
    """Add a view layer

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    NEW
    New -- Add a new view layer.

    COPY
    Copy Settings -- Copy settings of current view layer.

    EMPTY
    Blank -- Add a new view layer with all collections disabled.
        :type type: typing.Literal['NEW','COPY','EMPTY'] | None
    """

def view_layer_add_aov(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add a Shader AOV

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_layer_add_lightgroup(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
):
    """Add a Light Group

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of newly created lightgroup
    :type name: str
    """

def view_layer_add_used_lightgroups(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add all used Light Groups

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_layer_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove the selected view layer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_layer_remove_aov(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove Active AOV

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_layer_remove_lightgroup(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove Active Lightgroup

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_layer_remove_unused_lightgroups(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove all unused Light Groups

    :type execution_context: int | str | None
    :type undo: bool | None
    """
