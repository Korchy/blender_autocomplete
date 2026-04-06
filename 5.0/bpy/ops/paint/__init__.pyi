import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

def add_simple_uvs(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add cube map UVs on mesh"""

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
    generated_type: bpy.stub_internal.rna_enums.ImageGeneratedTypeItems
    | None = "BLANK",
    float: bool | None = False,
    domain: bpy.stub_internal.rna_enums.ColorAttributeDomainItems | None = "POINT",
    data_type: bpy.stub_internal.rna_enums.ColorAttributeTypeItems
    | None = "FLOAT_COLOR",
) -> None:
    """Add a paint slot

    :param type: Material Layer Type, Material layer type of new paint slot
    :param slot_type: Slot Type, Type of new paint slot
    :param name: Name, Name for new paint slot source
    :param color: Color, Default fill color
    :param width: Width, Image width
    :param height: Height, Image height
    :param alpha: Alpha, Create an image with an alpha channel
    :param generated_type: Generated Type, Fill the image with a grid for UV map testing
    :param float: 32-bit Float, Create image with 32-bit floating-point bit depth
    :param domain: Domain, Type of element that attribute is stored on
    :param data_type: Data Type, Type of data stored in attribute
    """

def brush_colors_flip(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Swap primary and secondary brush colors"""

def face_select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Change selection for all faces

        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
    """

def face_select_hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Hide selected faces

    :param unselected: Unselected, Hide unselected rather than selected objects
    """

def face_select_less(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    face_step: bool | None = True,
) -> None:
    """Deselect Faces connected to existing selection

    :param face_step: Face Step, Also deselect faces that only touch on a corner
    """

def face_select_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select linked faces"""

def face_select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deselect: bool | None = False,
) -> None:
    """Select linked faces under the cursor

    :param deselect: Deselect, Deselect rather than select items
    """

def face_select_loop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
    extend: bool | None = False,
) -> None:
    """Select face loop under the cursor

    :param select: Select, If false, faces will be deselected
    :param extend: Extend, Extend the selection
    """

def face_select_more(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    face_step: bool | None = True,
) -> None:
    """Select Faces connected to existing selection

    :param face_step: Face Step, Also select faces that only touch on a corner
    """

def face_vert_reveal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
) -> None:
    """Reveal hidden faces and vertices

    :param select: Select, Specifies whether the newly revealed geometry should be selected
    """

def grab_clone(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delta: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Move the clone source image

    :param delta: Delta, Delta offset of clone image in 0.0 to 1.0 coordinates
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
) -> None:
    """Hide/show some vertices

        :param xmin: X Min
        :param xmax: X Max
        :param ymin: Y Min
        :param ymax: Y Max
        :param wait_for_input: Wait for Input
        :param action: Visibility Action, Whether to hide or show vertices

    HIDE
    Hide -- Hide vertices.

    SHOW
    Show -- Show vertices.
        :param area: Visibility Area, Which vertices to hide or show

    OUTSIDE
    Outside -- Hide or show vertices outside the selection.

    Inside
    Inside -- Hide or show vertices inside the selection.
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    """

def hide_show_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["HIDE", "SHOW"] | None = "HIDE",
) -> None:
    """Hide/show all vertices

        :param action: Visibility Action, Whether to hide or show vertices

    HIDE
    Hide -- Hide vertices.

    SHOW
    Show -- Show vertices.
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
) -> None:
    """Hide/show some vertices

        :param path: Path
        :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
        :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
        :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
        :param action: Visibility Action, Whether to hide or show vertices

    HIDE
    Hide -- Hide vertices.

    SHOW
    Show -- Show vertices.
        :param area: Visibility Area, Which vertices to hide or show

    OUTSIDE
    Outside -- Hide or show vertices outside the selection.

    Inside
    Inside -- Hide or show vertices inside the selection.
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
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
) -> None:
    """Hide/show some vertices

        :param xstart: X Start
        :param xend: X End
        :param ystart: Y Start
        :param yend: Y End
        :param flip: Flip
        :param cursor: Cursor, Mouse cursor style to use during the modal operator
        :param action: Visibility Action, Whether to hide or show vertices

    HIDE
    Hide -- Hide vertices.

    SHOW
    Show -- Show vertices.
        :param area: Visibility Area, Which vertices to hide or show

    OUTSIDE
    Outside -- Hide or show vertices outside the selection.

    Inside
    Inside -- Hide or show vertices inside the selection.
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    """

def hide_show_masked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["HIDE", "SHOW"] | None = "HIDE",
) -> None:
    """Hide/show all masked vertices above a threshold

        :param action: Visibility Action, Whether to hide or show vertices

    HIDE
    Hide -- Hide vertices.

    SHOW
    Show -- Show vertices.
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
) -> None:
    """Hide/show some vertices

        :param path: Path
        :param action: Visibility Action, Whether to hide or show vertices

    HIDE
    Hide -- Hide vertices.

    SHOW
    Show -- Show vertices.
        :param area: Visibility Area, Which vertices to hide or show

    OUTSIDE
    Outside -- Hide or show vertices outside the selection.

    Inside
    Inside -- Hide or show vertices inside the selection.
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    """

def image_from_view(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
) -> None:
    """Make an image from biggest 3D view for reprojection

    :param filepath: File Path, Name of the file
    """

def image_paint(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH", "ERASE"] | None = "NORMAL",
    pen_flip: bool | None = False,
) -> None:
    """Paint a stroke into the image

        :param stroke: Stroke
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL
    Regular -- Apply brush normally.

    INVERT
    Invert -- Invert action of brush for duration of stroke.

    SMOOTH
    Smooth -- Switch brush to smooth mode for duration of stroke.

    ERASE
    Erase -- Switch brush to erase mode for duration of stroke.
        :param pen_flip: Pen Flip, Whether a tablets eraser mode is being used
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
) -> None:
    """Mask within a rectangle defined by the cursor

        :param xmin: X Min
        :param xmax: X Max
        :param ymin: Y Min
        :param ymax: Y Max
        :param wait_for_input: Wait for Input
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :param mode: Mode

    VALUE
    Value -- Set mask to the level specified by the value property.

    VALUE_INVERSE
    Value Inverted -- Set mask to the level specified by the inverted value property.

    INVERT
    Invert -- Invert the mask.
        :param value: Value, Mask level to use when mode is Value; zero means no masking and one is fully masked
    """

def mask_flood_fill(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["VALUE", "VALUE_INVERSE", "INVERT"] | None = "VALUE",
    value: float | None = 0.0,
) -> None:
    """Fill the whole mask with a given value, or invert its values

        :param mode: Mode

    VALUE
    Value -- Set mask to the level specified by the value property.

    VALUE_INVERSE
    Value Inverted -- Set mask to the level specified by the inverted value property.

    INVERT
    Invert -- Invert the mask.
        :param value: Value, Mask level to use when mode is Value; zero means no masking and one is fully masked
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
) -> None:
    """Mask within a shape defined by the cursor

        :param path: Path
        :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
        :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
        :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :param mode: Mode

    VALUE
    Value -- Set mask to the level specified by the value property.

    VALUE_INVERSE
    Value Inverted -- Set mask to the level specified by the inverted value property.

    INVERT
    Invert -- Invert the mask.
        :param value: Value, Mask level to use when mode is Value; zero means no masking and one is fully masked
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
) -> None:
    """Mask to one side of a line defined by the cursor

        :param xstart: X Start
        :param xend: X End
        :param ystart: Y Start
        :param yend: Y End
        :param flip: Flip
        :param cursor: Cursor, Mouse cursor style to use during the modal operator
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
        :param mode: Mode

    VALUE
    Value -- Set mask to the level specified by the value property.

    VALUE_INVERSE
    Value Inverted -- Set mask to the level specified by the inverted value property.

    INVERT
    Invert -- Invert the mask.
        :param value: Value, Mask level to use when mode is Value; zero means no masking and one is fully masked
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
) -> None:
    """Mask within a shape defined by the cursor

        :param path: Path
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :param mode: Mode

    VALUE
    Value -- Set mask to the level specified by the value property.

    VALUE_INVERSE
    Value Inverted -- Set mask to the level specified by the inverted value property.

    INVERT
    Invert -- Invert the mask.
        :param value: Value, Mask level to use when mode is Value; zero means no masking and one is fully masked
    """

def project_image(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    image: str | None = "",
) -> None:
    """Project an edited render from the active camera back onto the object

    :param image: Image
    """

def sample_color(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Iterable[int] | None = (0, 0),
    merged: bool | None = False,
    palette: bool | None = False,
) -> None:
    """Use the mouse to sample a color in the image

    :param location: Location
    :param merged: Sample Merged, Sample the output display color
    :param palette: Add to Palette
    """

def texture_paint_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle texture paint mode in 3D view"""

def vert_select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Change selection for all vertices

        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
    """

def vert_select_hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Hide selected vertices

    :param unselected: Unselected, Hide unselected rather than selected vertices
    """

def vert_select_less(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    face_step: bool | None = True,
) -> None:
    """Deselect Vertices connected to existing selection

    :param face_step: Face Step, Also deselect faces that only touch on a corner
    """

def vert_select_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select linked vertices"""

def vert_select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
) -> None:
    """Select linked vertices under the cursor

    :param select: Select, Whether to select or deselect linked vertices under the cursor
    """

def vert_select_more(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    face_step: bool | None = True,
) -> None:
    """Select Vertices connected to existing selection

    :param face_step: Face Step, Also select faces that only touch on a corner
    """

def vert_select_ungrouped(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
) -> None:
    """Select vertices without a group

    :param extend: Extend, Extend the selection
    """

def vertex_color_brightness_contrast(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    brightness: float | None = 0.0,
    contrast: float | None = 0.0,
) -> None:
    """Adjust vertex color brightness/contrast

    :param brightness: Brightness
    :param contrast: Contrast
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
) -> None:
    """Generate a dirt map gradient based on cavity

    :param blur_strength: Blur Strength, Blur strength per iteration
    :param blur_iterations: Blur Iterations, Number of times to blur the colors (higher blurs more)
    :param clean_angle: Highlight Angle, Less than 90 limits the angle used in the tonal range
    :param dirt_angle: Dirt Angle, Less than 90 limits the angle used in the tonal range
    :param dirt_only: Dirt Only, Dont calculate cleans for convex areas
    :param normalize: Normalize, Normalize the colors, increasing the contrast
    """

def vertex_color_from_weight(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Convert active weight into gray scale vertex colors"""

def vertex_color_hsv(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    h: float | None = 0.5,
    s: float | None = 1.0,
    v: float | None = 1.0,
) -> None:
    """Adjust vertex color Hue/Saturation/Value

    :param h: Hue
    :param s: Saturation
    :param v: Value
    """

def vertex_color_invert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Invert RGB values"""

def vertex_color_levels(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: float | None = 0.0,
    gain: float | None = 1.0,
) -> None:
    """Adjust levels of vertex colors

    :param offset: Offset, Value to add to colors
    :param gain: Gain, Value to multiply colors by
    """

def vertex_color_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_alpha: bool | None = True,
) -> None:
    """Fill the active vertex color layer with the current paint color

    :param use_alpha: Affect Alpha, Set color completely opaque instead of reusing existing alpha
    """

def vertex_color_smooth(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Smooth colors across vertices"""

def vertex_paint(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH", "ERASE"] | None = "NORMAL",
    pen_flip: bool | None = False,
    override_location: bool | None = False,
) -> None:
    """Paint a stroke in the active color attribute layer

        :param stroke: Stroke
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL
    Regular -- Apply brush normally.

    INVERT
    Invert -- Invert action of brush for duration of stroke.

    SMOOTH
    Smooth -- Switch brush to smooth mode for duration of stroke.

    ERASE
    Erase -- Switch brush to erase mode for duration of stroke.
        :param pen_flip: Pen Flip, Whether a tablets eraser mode is being used
        :param override_location: Override Location, Override the given "location" array by recalculating object space positions from the provided "mouse_event" positions
    """

def vertex_paint_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle the vertex paint mode in 3D view"""

def visibility_filter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["GROW", "SHRINK"] | None = "GROW",
    iterations: int | None = 1,
    auto_iteration_count: bool | None = True,
) -> None:
    """Edit the visibility of the current mesh

        :param action: Action

    GROW
    Grow Visibility -- Grow the visibility by one face based on mesh topology.

    SHRINK
    Shrink Visibility -- Shrink the visibility by one face based on mesh topology.
        :param iterations: Iterations, Number of times that the filter is going to be applied
        :param auto_iteration_count: Auto Iteration Count, Use an automatic number of iterations based on the number of vertices of the sculpt
    """

def visibility_invert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Invert the visibility of all vertices"""

def weight_from_bones(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["AUTOMATIC", "ENVELOPES"] | None = "AUTOMATIC",
) -> None:
    """Set the weights of the groups matching the attached armatures selected bones, using the distance between the vertices and the bones

        :param type: Type, Method to use for assigning weights

    AUTOMATIC
    Automatic -- Automatic weights from bones.

    ENVELOPES
    From Envelopes -- Weights from envelopes with user defined radius.
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
) -> None:
    """Draw a line to apply a weight gradient to selected vertices

    :param type: Type
    :param xstart: X Start
    :param xend: X End
    :param ystart: Y Start
    :param yend: Y End
    :param flip: Flip
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    """

def weight_paint(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH", "ERASE"] | None = "NORMAL",
    pen_flip: bool | None = False,
    override_location: bool | None = False,
) -> None:
    """Paint a stroke in the current vertex groups weights

        :param stroke: Stroke
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL
    Regular -- Apply brush normally.

    INVERT
    Invert -- Invert action of brush for duration of stroke.

    SMOOTH
    Smooth -- Switch brush to smooth mode for duration of stroke.

    ERASE
    Erase -- Switch brush to erase mode for duration of stroke.
        :param pen_flip: Pen Flip, Whether a tablets eraser mode is being used
        :param override_location: Override Location, Override the given "location" array by recalculating object space positions from the provided "mouse_event" positions
    """

def weight_paint_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle weight paint mode in 3D view"""

def weight_sample(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Use the mouse to sample a weight in the 3D view"""

def weight_sample_group(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select one of the vertex groups available under current mouse position"""

def weight_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Fill the active vertex group with the current paint weight"""
