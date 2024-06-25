import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def add_simple_uvs(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add cube map UVs on mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def add_texture_paint_slot(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "BASE_COLOR",
    slot_type: str | None = "IMAGE",
    name: str | typing.Any = "Untitled",
    color: typing.Any | None = (0.0, 0.0, 0.0, 1.0),
    width: typing.Any | None = 1024,
    height: typing.Any | None = 1024,
    alpha: bool | typing.Any | None = True,
    generated_type: str | None = "BLANK",
    float: bool | typing.Any | None = False,
    domain: str | None = "POINT",
    data_type: str | None = "FLOAT_COLOR",
):
    """Add a paint slot

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Material Layer Type, Material layer type of new paint slot
    :type type: str | None
    :param slot_type: Slot Type, Type of new paint slot
    :type slot_type: str | None
    :param name: Name, Name for new paint slot source
    :type name: str | typing.Any
    :param color: Color, Default fill color
    :type color: typing.Any | None
    :param width: Width, Image width
    :type width: typing.Any | None
    :param height: Height, Image height
    :type height: typing.Any | None
    :param alpha: Alpha, Create an image with an alpha channel
    :type alpha: bool | typing.Any | None
    :param generated_type: Generated Type, Fill the image with a grid for UV map testing
    :type generated_type: str | None
    :param float: 32-bit Float, Create image with 32-bit floating-point bit depth
    :type float: bool | typing.Any | None
    :param domain: Domain, Type of element that attribute is stored on
    :type domain: str | None
    :param data_type: Data Type, Type of data stored in attribute
    :type data_type: str | None
    """

    ...

def brush_colors_flip(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Swap primary and secondary brush colors

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def brush_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    sculpt_tool: str | None = "DRAW",
    vertex_tool: str | None = "DRAW",
    weight_tool: str | None = "DRAW",
    image_tool: str | None = "DRAW",
    gpencil_tool: str | None = "DRAW",
    gpencil_vertex_tool: str | None = "DRAW",
    gpencil_sculpt_tool: str | None = "SMOOTH",
    gpencil_weight_tool: str | None = "WEIGHT",
    curves_sculpt_tool: str | None = "COMB",
    toggle: bool | typing.Any | None = False,
    create_missing: bool | typing.Any | None = False,
):
    """Select a paint mode's brush by tool type

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param sculpt_tool: sculpt_tool
    :type sculpt_tool: str | None
    :param vertex_tool: vertex_tool
    :type vertex_tool: str | None
    :param weight_tool: weight_tool
    :type weight_tool: str | None
    :param image_tool: image_tool
    :type image_tool: str | None
    :param gpencil_tool: gpencil_tool
    :type gpencil_tool: str | None
    :param gpencil_vertex_tool: gpencil_vertex_tool
    :type gpencil_vertex_tool: str | None
    :param gpencil_sculpt_tool: gpencil_sculpt_tool
    :type gpencil_sculpt_tool: str | None
    :param gpencil_weight_tool: gpencil_weight_tool
    :type gpencil_weight_tool: str | None
    :param curves_sculpt_tool: curves_sculpt_tool
    :type curves_sculpt_tool: str | None
    :param toggle: Toggle, Toggle between two brushes rather than cycling
    :type toggle: bool | typing.Any | None
    :param create_missing: Create Missing, If the requested brush type does not exist, create a new brush
    :type create_missing: bool | typing.Any | None
    """

    ...

def face_select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: str | None = "TOGGLE",
):
    """Change selection for all faces

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
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
        :type action: str | None
    """

    ...

def face_select_hide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselected: bool | typing.Any | None = False,
):
    """Hide selected faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected objects
    :type unselected: bool | typing.Any | None
    """

    ...

def face_select_less(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    face_step: bool | typing.Any | None = True,
):
    """Deselect Faces connected to existing selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param face_step: Face Step, Also deselect faces that only touch on a corner
    :type face_step: bool | typing.Any | None
    """

    ...

def face_select_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select linked faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def face_select_linked_pick(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    deselect: bool | typing.Any | None = False,
):
    """Select linked faces under the cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param deselect: Deselect, Deselect rather than select items
    :type deselect: bool | typing.Any | None
    """

    ...

def face_select_loop(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    select: bool | typing.Any | None = True,
    extend: bool | typing.Any | None = False,
):
    """Select face loop under the cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select, If false, faces will be deselected
    :type select: bool | typing.Any | None
    :param extend: Extend, Extend the selection
    :type extend: bool | typing.Any | None
    """

    ...

def face_select_more(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    face_step: bool | typing.Any | None = True,
):
    """Select Faces connected to existing selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param face_step: Face Step, Also select faces that only touch on a corner
    :type face_step: bool | typing.Any | None
    """

    ...

def face_vert_reveal(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    select: bool | typing.Any | None = True,
):
    """Reveal hidden faces and vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select, Specifies whether the newly revealed geometry should be selected
    :type select: bool | typing.Any | None
    """

    ...

def grab_clone(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    delta: typing.Any | None = (0.0, 0.0),
):
    """Move the clone source image

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param delta: Delta, Delta offset of clone image in 0.0 to 1.0 coordinates
    :type delta: typing.Any | None
    """

    ...

def hide_show(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: str | None = "HIDE",
    area: str | None = "INSIDE",
    xmin: typing.Any | None = 0,
    xmax: typing.Any | None = 0,
    ymin: typing.Any | None = 0,
    ymax: typing.Any | None = 0,
    wait_for_input: bool | typing.Any | None = True,
):
    """Hide/show some vertices

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Visibility Action, Whether to hide or show vertices

    HIDE
    Hide -- Hide vertices.

    SHOW
    Show -- Show vertices.
        :type action: str | None
        :param area: Visibility Area, Which vertices to hide or show

    OUTSIDE
    Outside -- Hide or show vertices outside the selection.

    INSIDE
    Inside -- Hide or show vertices inside the selection.

    ALL
    All -- Hide or show all vertices.

    MASKED
    Masked -- Hide or show vertices that are masked (minimum mask value of 0.5).
        :type area: str | None
        :param xmin: X Min
        :type xmin: typing.Any | None
        :param xmax: X Max
        :type xmax: typing.Any | None
        :param ymin: Y Min
        :type ymin: typing.Any | None
        :param ymax: Y Max
        :type ymax: typing.Any | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | typing.Any | None
    """

    ...

def image_from_view(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
):
    """Make an image from biggest 3D view for reprojection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Name of the file
    :type filepath: str | typing.Any
    """

    ...

def image_paint(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: str | None = "NORMAL",
):
    """Paint a stroke into the image

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL
    Regular -- Apply brush normally.

    INVERT
    Invert -- Invert action of brush for duration of stroke.

    SMOOTH
    Smooth -- Switch brush to smooth mode for duration of stroke.
        :type mode: str | None
    """

    ...

def mask_box_gesture(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    xmin: typing.Any | None = 0,
    xmax: typing.Any | None = 0,
    ymin: typing.Any | None = 0,
    ymax: typing.Any | None = 0,
    wait_for_input: bool | typing.Any | None = True,
    use_front_faces_only: bool | typing.Any | None = False,
    use_limit_to_segment: bool | typing.Any | None = False,
    mode: str | None = "VALUE",
    value: typing.Any | None = 1.0,
):
    """Add mask within the box as you move the brush

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param xmin: X Min
        :type xmin: typing.Any | None
        :param xmax: X Max
        :type xmax: typing.Any | None
        :param ymin: Y Min
        :type ymin: typing.Any | None
        :param ymax: Y Max
        :type ymax: typing.Any | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | typing.Any | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | typing.Any | None
        :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
        :type use_limit_to_segment: bool | typing.Any | None
        :param mode: Mode

    VALUE
    Value -- Set mask to the level specified by the 'value' property.

    VALUE_INVERSE
    Value Inverted -- Set mask to the level specified by the inverted 'value' property.

    INVERT
    Invert -- Invert the mask.
        :type mode: str | None
        :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
        :type value: typing.Any | None
    """

    ...

def mask_flood_fill(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "VALUE",
    value: typing.Any | None = 0.0,
):
    """Fill the whole mask with a given value, or invert its values

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    VALUE
    Value -- Set mask to the level specified by the 'value' property.

    VALUE_INVERSE
    Value Inverted -- Set mask to the level specified by the inverted 'value' property.

    INVERT
    Invert -- Invert the mask.
        :type mode: str | None
        :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
        :type value: typing.Any | None
    """

    ...

def mask_lasso_gesture(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_front_faces_only: bool | typing.Any | None = False,
    use_limit_to_segment: bool | typing.Any | None = False,
    mode: str | None = "VALUE",
    value: typing.Any | None = 1.0,
):
    """Add mask within the lasso as you move the brush

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param path: Path
        :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | typing.Any | None
        :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
        :type use_limit_to_segment: bool | typing.Any | None
        :param mode: Mode

    VALUE
    Value -- Set mask to the level specified by the 'value' property.

    VALUE_INVERSE
    Value Inverted -- Set mask to the level specified by the inverted 'value' property.

    INVERT
    Invert -- Invert the mask.
        :type mode: str | None
        :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
        :type value: typing.Any | None
    """

    ...

def mask_line_gesture(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    xstart: typing.Any | None = 0,
    xend: typing.Any | None = 0,
    ystart: typing.Any | None = 0,
    yend: typing.Any | None = 0,
    flip: bool | typing.Any | None = False,
    cursor: typing.Any | None = 5,
    use_front_faces_only: bool | typing.Any | None = False,
    use_limit_to_segment: bool | typing.Any | None = False,
    mode: str | None = "VALUE",
    value: typing.Any | None = 1.0,
):
    """Add mask to the right of a line as you move the brush

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param xstart: X Start
        :type xstart: typing.Any | None
        :param xend: X End
        :type xend: typing.Any | None
        :param ystart: Y Start
        :type ystart: typing.Any | None
        :param yend: Y End
        :type yend: typing.Any | None
        :param flip: Flip
        :type flip: bool | typing.Any | None
        :param cursor: Cursor, Mouse cursor style to use during the modal operator
        :type cursor: typing.Any | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | typing.Any | None
        :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
        :type use_limit_to_segment: bool | typing.Any | None
        :param mode: Mode

    VALUE
    Value -- Set mask to the level specified by the 'value' property.

    VALUE_INVERSE
    Value Inverted -- Set mask to the level specified by the inverted 'value' property.

    INVERT
    Invert -- Invert the mask.
        :type mode: str | None
        :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
        :type value: typing.Any | None
    """

    ...

def project_image(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    image: str | None = "",
):
    """Project an edited render from the active camera back onto the object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param image: Image
    :type image: str | None
    """

    ...

def sample_color(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    location: typing.Any | None = (0, 0),
    merged: bool | typing.Any | None = False,
    palette: bool | typing.Any | None = False,
):
    """Use the mouse to sample a color in the image

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location
    :type location: typing.Any | None
    :param merged: Sample Merged, Sample the output display color
    :type merged: bool | typing.Any | None
    :param palette: Add to Palette
    :type palette: bool | typing.Any | None
    """

    ...

def texture_paint_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle texture paint mode in 3D view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vert_select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: str | None = "TOGGLE",
):
    """Change selection for all vertices

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
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
        :type action: str | None
    """

    ...

def vert_select_hide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselected: bool | typing.Any | None = False,
):
    """Hide selected vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected vertices
    :type unselected: bool | typing.Any | None
    """

    ...

def vert_select_less(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    face_step: bool | typing.Any | None = True,
):
    """Deselect Vertices connected to existing selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param face_step: Face Step, Also deselect faces that only touch on a corner
    :type face_step: bool | typing.Any | None
    """

    ...

def vert_select_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select linked vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vert_select_linked_pick(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    select: bool | typing.Any | None = True,
):
    """Select linked vertices under the cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select, Whether to select or deselect linked vertices under the cursor
    :type select: bool | typing.Any | None
    """

    ...

def vert_select_more(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    face_step: bool | typing.Any | None = True,
):
    """Select Vertices connected to existing selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param face_step: Face Step, Also select faces that only touch on a corner
    :type face_step: bool | typing.Any | None
    """

    ...

def vert_select_ungrouped(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
):
    """Select vertices without a group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | typing.Any | None
    """

    ...

def vertex_color_brightness_contrast(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    brightness: typing.Any | None = 0.0,
    contrast: typing.Any | None = 0.0,
):
    """Adjust vertex color brightness/contrast

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param brightness: Brightness
    :type brightness: typing.Any | None
    :param contrast: Contrast
    :type contrast: typing.Any | None
    """

    ...

def vertex_color_dirt(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    blur_strength: typing.Any | None = 1.0,
    blur_iterations: typing.Any | None = 1,
    clean_angle: typing.Any | None = 3.14159,
    dirt_angle: typing.Any | None = 0.0,
    dirt_only: bool | typing.Any | None = False,
    normalize: bool | typing.Any | None = True,
):
    """Generate a dirt map gradient based on cavity

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param blur_strength: Blur Strength, Blur strength per iteration
    :type blur_strength: typing.Any | None
    :param blur_iterations: Blur Iterations, Number of times to blur the colors (higher blurs more)
    :type blur_iterations: typing.Any | None
    :param clean_angle: Highlight Angle, Less than 90 limits the angle used in the tonal range
    :type clean_angle: typing.Any | None
    :param dirt_angle: Dirt Angle, Less than 90 limits the angle used in the tonal range
    :type dirt_angle: typing.Any | None
    :param dirt_only: Dirt Only, Don't calculate cleans for convex areas
    :type dirt_only: bool | typing.Any | None
    :param normalize: Normalize, Normalize the colors, increasing the contrast
    :type normalize: bool | typing.Any | None
    """

    ...

def vertex_color_from_weight(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Convert active weight into gray scale vertex colors

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_color_hsv(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    h: typing.Any | None = 0.5,
    s: typing.Any | None = 1.0,
    v: typing.Any | None = 1.0,
):
    """Adjust vertex color Hue/Saturation/Value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param h: Hue
    :type h: typing.Any | None
    :param s: Saturation
    :type s: typing.Any | None
    :param v: Value
    :type v: typing.Any | None
    """

    ...

def vertex_color_invert(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Invert RGB values

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_color_levels(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    offset: typing.Any | None = 0.0,
    gain: typing.Any | None = 1.0,
):
    """Adjust levels of vertex colors

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Offset, Value to add to colors
    :type offset: typing.Any | None
    :param gain: Gain, Value to multiply colors by
    :type gain: typing.Any | None
    """

    ...

def vertex_color_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_alpha: bool | typing.Any | None = True,
):
    """Fill the active vertex color layer with the current paint color

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_alpha: Affect Alpha, Set color completely opaque instead of reusing existing alpha
    :type use_alpha: bool | typing.Any | None
    """

    ...

def vertex_color_smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Smooth colors across vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_paint(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: str | None = "NORMAL",
):
    """Paint a stroke in the active color attribute layer

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL
    Regular -- Apply brush normally.

    INVERT
    Invert -- Invert action of brush for duration of stroke.

    SMOOTH
    Smooth -- Switch brush to smooth mode for duration of stroke.
        :type mode: str | None
    """

    ...

def vertex_paint_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle the vertex paint mode in 3D view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def visibility_invert(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Invert the visibility of all vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def weight_from_bones(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "AUTOMATIC",
):
    """Set the weights of the groups matching the attached armature's selected bones, using the distance between the vertices and the bones

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Method to use for assigning weights

    AUTOMATIC
    Automatic -- Automatic weights from bones.

    ENVELOPES
    From Envelopes -- Weights from envelopes with user defined radius.
        :type type: str | None
    """

    ...

def weight_gradient(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "LINEAR",
    xstart: typing.Any | None = 0,
    xend: typing.Any | None = 0,
    ystart: typing.Any | None = 0,
    yend: typing.Any | None = 0,
    flip: bool | typing.Any | None = False,
    cursor: typing.Any | None = 5,
):
    """Draw a line to apply a weight gradient to selected vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    :param xstart: X Start
    :type xstart: typing.Any | None
    :param xend: X End
    :type xend: typing.Any | None
    :param ystart: Y Start
    :type ystart: typing.Any | None
    :param yend: Y End
    :type yend: typing.Any | None
    :param flip: Flip
    :type flip: bool | typing.Any | None
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: typing.Any | None
    """

    ...

def weight_paint(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: str | None = "NORMAL",
):
    """Paint a stroke in the current vertex group's weights

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL
    Regular -- Apply brush normally.

    INVERT
    Invert -- Invert action of brush for duration of stroke.

    SMOOTH
    Smooth -- Switch brush to smooth mode for duration of stroke.
        :type mode: str | None
    """

    ...

def weight_paint_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle weight paint mode in 3D view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def weight_sample(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Use the mouse to sample a weight in the 3D view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def weight_sample_group(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select one of the vertex groups available under current mouse position

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def weight_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Fill the active vertex group with the current paint weight

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...
