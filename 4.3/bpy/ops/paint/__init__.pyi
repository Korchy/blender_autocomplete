import typing
import collections.abc
import typing_extensions
import bpy._typing.rna_enums
import bpy.types
import mathutils

def add_simple_uvs(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add cube map UVs on mesh

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def add_texture_paint_slot(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "BASE_COLOR",
        "SPECULAR",
        "ROUGHNESS",
        "METALLIC",
        "NORMAL",
        "BUMP",
        "DISPLACEMENT",
    ]
    | None = "BASE_COLOR",
    slot_type: typing.Literal["IMAGE", "COLOR_ATTRIBUTE"] | None = "IMAGE",
    name: str = "Untitled",
    color: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0, 1.0),
    width: int | None = 1024,
    height: int | None = 1024,
    alpha: bool | None = True,
    generated_type: bpy._typing.rna_enums.ImageGeneratedTypeItems | None = "BLANK",
    float: bool | None = False,
    domain: bpy._typing.rna_enums.ColorAttributeDomainItems | None = "POINT",
    data_type: bpy._typing.rna_enums.ColorAttributeTypeItems | None = "FLOAT_COLOR",
):
    """Add a paint slot

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Material Layer Type, Material layer type of new paint slot
    :type type: typing.Literal['BASE_COLOR','SPECULAR','ROUGHNESS','METALLIC','NORMAL','BUMP','DISPLACEMENT'] | None
    :param slot_type: Slot Type, Type of new paint slot
    :type slot_type: typing.Literal['IMAGE','COLOR_ATTRIBUTE'] | None
    :param name: Name, Name for new paint slot source
    :type name: str
    :param color: Color, Default fill color
    :type color: collections.abc.Iterable[float] | None
    :param width: Width, Image width
    :type width: int | None
    :param height: Height, Image height
    :type height: int | None
    :param alpha: Alpha, Create an image with an alpha channel
    :type alpha: bool | None
    :param generated_type: Generated Type, Fill the image with a grid for UV map testing
    :type generated_type: bpy._typing.rna_enums.ImageGeneratedTypeItems | None
    :param float: 32-bit Float, Create image with 32-bit floating-point bit depth
    :type float: bool | None
    :param domain: Domain, Type of element that attribute is stored on
    :type domain: bpy._typing.rna_enums.ColorAttributeDomainItems | None
    :param data_type: Data Type, Type of data stored in attribute
    :type data_type: bpy._typing.rna_enums.ColorAttributeTypeItems | None
    """

def brush_colors_flip(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Swap primary and secondary brush colors

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def face_select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Change selection for all faces

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

def face_select_hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
):
    """Hide selected faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected objects
    :type unselected: bool | None
    """

def face_select_less(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    face_step: bool | None = True,
):
    """Deselect Faces connected to existing selection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param face_step: Face Step, Also deselect faces that only touch on a corner
    :type face_step: bool | None
    """

def face_select_linked(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Select linked faces

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def face_select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deselect: bool | None = False,
):
    """Select linked faces under the cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param deselect: Deselect, Deselect rather than select items
    :type deselect: bool | None
    """

def face_select_loop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
    extend: bool | None = False,
):
    """Select face loop under the cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select, If false, faces will be deselected
    :type select: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def face_select_more(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    face_step: bool | None = True,
):
    """Select Faces connected to existing selection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param face_step: Face Step, Also select faces that only touch on a corner
    :type face_step: bool | None
    """

def face_vert_reveal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
):
    """Reveal hidden faces and vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select, Specifies whether the newly revealed geometry should be selected
    :type select: bool | None
    """

def grab_clone(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delta: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Move the clone source image

    :type execution_context: int | str | None
    :type undo: bool | None
    :param delta: Delta, Delta offset of clone image in 0.0 to 1.0 coordinates
    :type delta: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def hide_show(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    action: typing.Literal["HIDE", "SHOW"] | None = "HIDE",
    area: typing.Literal["OUTSIDE", "Inside"] | None = "Inside",
    use_front_faces_only: bool | None = False,
):
    """Hide/show some vertices

        :type execution_context: int | str | None
        :type undo: bool | None
        :param xmin: X Min
        :type xmin: int | None
        :param xmax: X Max
        :type xmax: int | None
        :param ymin: Y Min
        :type ymin: int | None
        :param ymax: Y Max
        :type ymax: int | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | None
        :param action: Visibility Action, Whether to hide or show vertices

    HIDE
    Hide -- Hide vertices.

    SHOW
    Show -- Show vertices.
        :type action: typing.Literal['HIDE','SHOW'] | None
        :param area: Visibility Area, Which vertices to hide or show

    OUTSIDE
    Outside -- Hide or show vertices outside the selection.

    Inside
    Inside -- Hide or show vertices inside the selection.
        :type area: typing.Literal['OUTSIDE','Inside'] | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | None
    """

def hide_show_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["HIDE", "SHOW"] | None = "HIDE",
):
    """Hide/show all vertices

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Visibility Action, Whether to hide or show vertices

    HIDE
    Hide -- Hide vertices.

    SHOW
    Show -- Show vertices.
        :type action: typing.Literal['HIDE','SHOW'] | None
    """

def hide_show_lasso_gesture(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_smooth_stroke: bool | None = False,
    smooth_stroke_factor: float | None = 0.75,
    smooth_stroke_radius: int | None = 35,
    action: typing.Literal["HIDE", "SHOW"] | None = "HIDE",
    area: typing.Literal["OUTSIDE", "Inside"] | None = "Inside",
    use_front_faces_only: bool | None = False,
):
    """Hide/show some vertices

        :type execution_context: int | str | None
        :type undo: bool | None
        :param path: Path
        :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
        :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
        :type use_smooth_stroke: bool | None
        :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
        :type smooth_stroke_factor: float | None
        :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
        :type smooth_stroke_radius: int | None
        :param action: Visibility Action, Whether to hide or show vertices

    HIDE
    Hide -- Hide vertices.

    SHOW
    Show -- Show vertices.
        :type action: typing.Literal['HIDE','SHOW'] | None
        :param area: Visibility Area, Which vertices to hide or show

    OUTSIDE
    Outside -- Hide or show vertices outside the selection.

    Inside
    Inside -- Hide or show vertices inside the selection.
        :type area: typing.Literal['OUTSIDE','Inside'] | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | None
    """

def hide_show_line_gesture(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xstart: int | None = 0,
    xend: int | None = 0,
    ystart: int | None = 0,
    yend: int | None = 0,
    flip: bool | None = False,
    cursor: int | None = 5,
    action: typing.Literal["HIDE", "SHOW"] | None = "HIDE",
    area: typing.Literal["OUTSIDE", "Inside"] | None = "Inside",
    use_front_faces_only: bool | None = False,
    use_limit_to_segment: bool | None = False,
):
    """Hide/show some vertices

        :type execution_context: int | str | None
        :type undo: bool | None
        :param xstart: X Start
        :type xstart: int | None
        :param xend: X End
        :type xend: int | None
        :param ystart: Y Start
        :type ystart: int | None
        :param yend: Y End
        :type yend: int | None
        :param flip: Flip
        :type flip: bool | None
        :param cursor: Cursor, Mouse cursor style to use during the modal operator
        :type cursor: int | None
        :param action: Visibility Action, Whether to hide or show vertices

    HIDE
    Hide -- Hide vertices.

    SHOW
    Show -- Show vertices.
        :type action: typing.Literal['HIDE','SHOW'] | None
        :param area: Visibility Area, Which vertices to hide or show

    OUTSIDE
    Outside -- Hide or show vertices outside the selection.

    Inside
    Inside -- Hide or show vertices inside the selection.
        :type area: typing.Literal['OUTSIDE','Inside'] | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | None
        :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
        :type use_limit_to_segment: bool | None
    """

def hide_show_masked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["HIDE", "SHOW"] | None = "HIDE",
):
    """Hide/show all masked vertices above a threshold

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Visibility Action, Whether to hide or show vertices

    HIDE
    Hide -- Hide vertices.

    SHOW
    Show -- Show vertices.
        :type action: typing.Literal['HIDE','SHOW'] | None
    """

def hide_show_polyline_gesture(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    action: typing.Literal["HIDE", "SHOW"] | None = "HIDE",
    area: typing.Literal["OUTSIDE", "Inside"] | None = "Inside",
    use_front_faces_only: bool | None = False,
):
    """Hide/show some vertices

        :type execution_context: int | str | None
        :type undo: bool | None
        :param path: Path
        :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
        :param action: Visibility Action, Whether to hide or show vertices

    HIDE
    Hide -- Hide vertices.

    SHOW
    Show -- Show vertices.
        :type action: typing.Literal['HIDE','SHOW'] | None
        :param area: Visibility Area, Which vertices to hide or show

    OUTSIDE
    Outside -- Hide or show vertices outside the selection.

    Inside
    Inside -- Hide or show vertices inside the selection.
        :type area: typing.Literal['OUTSIDE','Inside'] | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | None
    """

def image_from_view(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
):
    """Make an image from biggest 3D view for reprojection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Name of the file
    :type filepath: str
    """

def image_paint(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH", "ERASE"] | None = "NORMAL",
):
    """Paint a stroke into the image

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

    ERASE
    Erase -- Switch brush to erase mode for duration of stroke.
        :type mode: typing.Literal['NORMAL','INVERT','SMOOTH','ERASE'] | None
    """

def mask_box_gesture(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    use_front_faces_only: bool | None = False,
    mode: typing.Literal["VALUE", "VALUE_INVERSE", "INVERT"] | None = "VALUE",
    value: float | None = 1.0,
):
    """Mask within a rectangle defined by the cursor

        :type execution_context: int | str | None
        :type undo: bool | None
        :param xmin: X Min
        :type xmin: int | None
        :param xmax: X Max
        :type xmax: int | None
        :param ymin: Y Min
        :type ymin: int | None
        :param ymax: Y Max
        :type ymax: int | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | None
        :param mode: Mode

    VALUE
    Value -- Set mask to the level specified by the 'value' property.

    VALUE_INVERSE
    Value Inverted -- Set mask to the level specified by the inverted 'value' property.

    INVERT
    Invert -- Invert the mask.
        :type mode: typing.Literal['VALUE','VALUE_INVERSE','INVERT'] | None
        :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
        :type value: float | None
    """

def mask_flood_fill(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["VALUE", "VALUE_INVERSE", "INVERT"] | None = "VALUE",
    value: float | None = 0.0,
):
    """Fill the whole mask with a given value, or invert its values

        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    VALUE
    Value -- Set mask to the level specified by the 'value' property.

    VALUE_INVERSE
    Value Inverted -- Set mask to the level specified by the inverted 'value' property.

    INVERT
    Invert -- Invert the mask.
        :type mode: typing.Literal['VALUE','VALUE_INVERSE','INVERT'] | None
        :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
        :type value: float | None
    """

def mask_lasso_gesture(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_smooth_stroke: bool | None = False,
    smooth_stroke_factor: float | None = 0.75,
    smooth_stroke_radius: int | None = 35,
    use_front_faces_only: bool | None = False,
    mode: typing.Literal["VALUE", "VALUE_INVERSE", "INVERT"] | None = "VALUE",
    value: float | None = 1.0,
):
    """Mask within a shape defined by the cursor

        :type execution_context: int | str | None
        :type undo: bool | None
        :param path: Path
        :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
        :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
        :type use_smooth_stroke: bool | None
        :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
        :type smooth_stroke_factor: float | None
        :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
        :type smooth_stroke_radius: int | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | None
        :param mode: Mode

    VALUE
    Value -- Set mask to the level specified by the 'value' property.

    VALUE_INVERSE
    Value Inverted -- Set mask to the level specified by the inverted 'value' property.

    INVERT
    Invert -- Invert the mask.
        :type mode: typing.Literal['VALUE','VALUE_INVERSE','INVERT'] | None
        :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
        :type value: float | None
    """

def mask_line_gesture(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xstart: int | None = 0,
    xend: int | None = 0,
    ystart: int | None = 0,
    yend: int | None = 0,
    flip: bool | None = False,
    cursor: int | None = 5,
    use_front_faces_only: bool | None = False,
    use_limit_to_segment: bool | None = False,
    mode: typing.Literal["VALUE", "VALUE_INVERSE", "INVERT"] | None = "VALUE",
    value: float | None = 1.0,
):
    """Mask to one side of a line defined by the cursor

        :type execution_context: int | str | None
        :type undo: bool | None
        :param xstart: X Start
        :type xstart: int | None
        :param xend: X End
        :type xend: int | None
        :param ystart: Y Start
        :type ystart: int | None
        :param yend: Y End
        :type yend: int | None
        :param flip: Flip
        :type flip: bool | None
        :param cursor: Cursor, Mouse cursor style to use during the modal operator
        :type cursor: int | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | None
        :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
        :type use_limit_to_segment: bool | None
        :param mode: Mode

    VALUE
    Value -- Set mask to the level specified by the 'value' property.

    VALUE_INVERSE
    Value Inverted -- Set mask to the level specified by the inverted 'value' property.

    INVERT
    Invert -- Invert the mask.
        :type mode: typing.Literal['VALUE','VALUE_INVERSE','INVERT'] | None
        :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
        :type value: float | None
    """

def mask_polyline_gesture(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_front_faces_only: bool | None = False,
    mode: typing.Literal["VALUE", "VALUE_INVERSE", "INVERT"] | None = "VALUE",
    value: float | None = 1.0,
):
    """Mask within a shape defined by the cursor

        :type execution_context: int | str | None
        :type undo: bool | None
        :param path: Path
        :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | None
        :param mode: Mode

    VALUE
    Value -- Set mask to the level specified by the 'value' property.

    VALUE_INVERSE
    Value Inverted -- Set mask to the level specified by the inverted 'value' property.

    INVERT
    Invert -- Invert the mask.
        :type mode: typing.Literal['VALUE','VALUE_INVERSE','INVERT'] | None
        :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
        :type value: float | None
    """

def project_image(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    image: str | None = "",
):
    """Project an edited render from the active camera back onto the object

    :type execution_context: int | str | None
    :type undo: bool | None
    :param image: Image
    :type image: str | None
    """

def sample_color(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Iterable[int] | None = (0, 0),
    merged: bool | None = False,
    palette: bool | None = False,
):
    """Use the mouse to sample a color in the image

    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location
    :type location: collections.abc.Iterable[int] | None
    :param merged: Sample Merged, Sample the output display color
    :type merged: bool | None
    :param palette: Add to Palette
    :type palette: bool | None
    """

def texture_paint_toggle(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Toggle texture paint mode in 3D view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vert_select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Change selection for all vertices

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

def vert_select_hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
):
    """Hide selected vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected vertices
    :type unselected: bool | None
    """

def vert_select_less(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    face_step: bool | None = True,
):
    """Deselect Vertices connected to existing selection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param face_step: Face Step, Also deselect faces that only touch on a corner
    :type face_step: bool | None
    """

def vert_select_linked(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Select linked vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vert_select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
):
    """Select linked vertices under the cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select, Whether to select or deselect linked vertices under the cursor
    :type select: bool | None
    """

def vert_select_more(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    face_step: bool | None = True,
):
    """Select Vertices connected to existing selection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param face_step: Face Step, Also select faces that only touch on a corner
    :type face_step: bool | None
    """

def vert_select_ungrouped(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
):
    """Select vertices without a group

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def vertex_color_brightness_contrast(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    brightness: float | None = 0.0,
    contrast: float | None = 0.0,
):
    """Adjust vertex color brightness/contrast

    :type execution_context: int | str | None
    :type undo: bool | None
    :param brightness: Brightness
    :type brightness: float | None
    :param contrast: Contrast
    :type contrast: float | None
    """

def vertex_color_dirt(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    blur_strength: float | None = 1.0,
    blur_iterations: int | None = 1,
    clean_angle: float | None = 3.14159,
    dirt_angle: float | None = 0.0,
    dirt_only: bool | None = False,
    normalize: bool | None = True,
):
    """Generate a dirt map gradient based on cavity

    :type execution_context: int | str | None
    :type undo: bool | None
    :param blur_strength: Blur Strength, Blur strength per iteration
    :type blur_strength: float | None
    :param blur_iterations: Blur Iterations, Number of times to blur the colors (higher blurs more)
    :type blur_iterations: int | None
    :param clean_angle: Highlight Angle, Less than 90 limits the angle used in the tonal range
    :type clean_angle: float | None
    :param dirt_angle: Dirt Angle, Less than 90 limits the angle used in the tonal range
    :type dirt_angle: float | None
    :param dirt_only: Dirt Only, Don't calculate cleans for convex areas
    :type dirt_only: bool | None
    :param normalize: Normalize, Normalize the colors, increasing the contrast
    :type normalize: bool | None
    """

def vertex_color_from_weight(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Convert active weight into gray scale vertex colors

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vertex_color_hsv(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    h: float | None = 0.5,
    s: float | None = 1.0,
    v: float | None = 1.0,
):
    """Adjust vertex color Hue/Saturation/Value

    :type execution_context: int | str | None
    :type undo: bool | None
    :param h: Hue
    :type h: float | None
    :param s: Saturation
    :type s: float | None
    :param v: Value
    :type v: float | None
    """

def vertex_color_invert(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Invert RGB values

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vertex_color_levels(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: float | None = 0.0,
    gain: float | None = 1.0,
):
    """Adjust levels of vertex colors

    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Offset, Value to add to colors
    :type offset: float | None
    :param gain: Gain, Value to multiply colors by
    :type gain: float | None
    """

def vertex_color_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_alpha: bool | None = True,
):
    """Fill the active vertex color layer with the current paint color

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_alpha: Affect Alpha, Set color completely opaque instead of reusing existing alpha
    :type use_alpha: bool | None
    """

def vertex_color_smooth(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Smooth colors across vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vertex_paint(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH", "ERASE"] | None = "NORMAL",
):
    """Paint a stroke in the active color attribute layer

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

    ERASE
    Erase -- Switch brush to erase mode for duration of stroke.
        :type mode: typing.Literal['NORMAL','INVERT','SMOOTH','ERASE'] | None
    """

def vertex_paint_toggle(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Toggle the vertex paint mode in 3D view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def visibility_filter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["GROW", "SHRINK"] | None = "GROW",
    iterations: int | None = 1,
    auto_iteration_count: bool | None = True,
):
    """Edit the visibility of the current mesh

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action

    GROW
    Grow Visibility -- Grow the visibility by one face based on mesh topology.

    SHRINK
    Shrink Visibility -- Shrink the visibility by one face based on mesh topology.
        :type action: typing.Literal['GROW','SHRINK'] | None
        :param iterations: Iterations, Number of times that the filter is going to be applied
        :type iterations: int | None
        :param auto_iteration_count: Auto Iteration Count, Use an automatic number of iterations based on the number of vertices of the sculpt
        :type auto_iteration_count: bool | None
    """

def visibility_invert(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Invert the visibility of all vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def weight_from_bones(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["AUTOMATIC", "ENVELOPES"] | None = "AUTOMATIC",
):
    """Set the weights of the groups matching the attached armature's selected bones, using the distance between the vertices and the bones

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Method to use for assigning weights

    AUTOMATIC
    Automatic -- Automatic weights from bones.

    ENVELOPES
    From Envelopes -- Weights from envelopes with user defined radius.
        :type type: typing.Literal['AUTOMATIC','ENVELOPES'] | None
    """

def weight_gradient(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["LINEAR", "RADIAL"] | None = "LINEAR",
    xstart: int | None = 0,
    xend: int | None = 0,
    ystart: int | None = 0,
    yend: int | None = 0,
    flip: bool | None = False,
    cursor: int | None = 5,
):
    """Draw a line to apply a weight gradient to selected vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['LINEAR','RADIAL'] | None
    :param xstart: X Start
    :type xstart: int | None
    :param xend: X End
    :type xend: int | None
    :param ystart: Y Start
    :type ystart: int | None
    :param yend: Y End
    :type yend: int | None
    :param flip: Flip
    :type flip: bool | None
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: int | None
    """

def weight_paint(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH", "ERASE"] | None = "NORMAL",
):
    """Paint a stroke in the current vertex group's weights

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

    ERASE
    Erase -- Switch brush to erase mode for duration of stroke.
        :type mode: typing.Literal['NORMAL','INVERT','SMOOTH','ERASE'] | None
    """

def weight_paint_toggle(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Toggle weight paint mode in 3D view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def weight_sample(execution_context: int | str | None = None, undo: bool | None = None):
    """Use the mouse to sample a weight in the 3D view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def weight_sample_group(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Select one of the vertex groups available under current mouse position

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def weight_set(execution_context: int | str | None = None, undo: bool | None = None):
    """Fill the active vertex group with the current paint weight

    :type execution_context: int | str | None
    :type undo: bool | None
    """
