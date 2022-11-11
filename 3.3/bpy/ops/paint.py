import sys
import typing
import bpy.types
import mathutils

GenericType = typing.TypeVar("GenericType")


def add_simple_uvs(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Add cube map uvs on mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def add_texture_paint_slot(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        type: typing.Union[str, int] = 'BASE_COLOR',
        slot_type: typing.Union[str, int] = 'IMAGE',
        name: str = "Untitled",
        color: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float, float], 'mathutils.Vector'] = (0.0,
                                                                        0.0,
                                                                        0.0,
                                                                        1.0),
        width: int = 1024,
        height: int = 1024,
        alpha: bool = True,
        generated_type: typing.Union[int, str] = 'BLANK',
        float: bool = False,
        domain: typing.Union[str, int] = 'POINT',
        data_type: typing.Union[str, int] = 'COLOR'):
    ''' Add a paint slot

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Material Layer Type, Material layer type of new paint slot
    :type type: typing.Union[str, int]
    :param slot_type: Slot Type, Type of new paint slot
    :type slot_type: typing.Union[str, int]
    :param name: Name, Name for new paint slot source
    :type name: str
    :param color: Color, Default fill color
    :type color: typing.Union[typing.List[float], typing.Tuple[float, float, float, float], 'mathutils.Vector']
    :param width: Width, Image width
    :type width: int
    :param height: Height, Image height
    :type height: int
    :param alpha: Alpha, Create an image with an alpha channel
    :type alpha: bool
    :param generated_type: Generated Type, Fill the image with a grid for UV map testing
    :type generated_type: typing.Union[int, str]
    :param float: 32-bit Float, Create image with 32-bit floating-point bit depth
    :type float: bool
    :param domain: Domain, Type of element that attribute is stored on
    :type domain: typing.Union[str, int]
    :param data_type: Data Type, Type of data stored in attribute
    :type data_type: typing.Union[str, int]
    '''

    pass


def brush_colors_flip(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Swap primary and secondary brush colors

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def brush_select(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 sculpt_tool: typing.Union[int, str] = 'DRAW',
                 vertex_tool: typing.Union[int, str] = 'DRAW',
                 weight_tool: typing.Union[int, str] = 'DRAW',
                 image_tool: typing.Union[int, str] = 'DRAW',
                 gpencil_tool: typing.Union[int, str] = 'DRAW',
                 gpencil_vertex_tool: typing.Union[int, str] = 'DRAW',
                 gpencil_sculpt_tool: typing.Union[int, str] = 'SMOOTH',
                 gpencil_weight_tool: typing.Union[int, str] = 'WEIGHT',
                 curves_sculpt_tool: typing.Union[int, str] = 'COMB',
                 toggle: bool = False,
                 create_missing: bool = False):
    ''' Select a paint mode's brush by tool type

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param sculpt_tool: sculpt_tool
    :type sculpt_tool: typing.Union[int, str]
    :param vertex_tool: vertex_tool
    :type vertex_tool: typing.Union[int, str]
    :param weight_tool: weight_tool
    :type weight_tool: typing.Union[int, str]
    :param image_tool: image_tool
    :type image_tool: typing.Union[int, str]
    :param gpencil_tool: gpencil_tool
    :type gpencil_tool: typing.Union[int, str]
    :param gpencil_vertex_tool: gpencil_vertex_tool
    :type gpencil_vertex_tool: typing.Union[int, str]
    :param gpencil_sculpt_tool: gpencil_sculpt_tool
    :type gpencil_sculpt_tool: typing.Union[int, str]
    :param gpencil_weight_tool: gpencil_weight_tool
    :type gpencil_weight_tool: typing.Union[int, str]
    :param curves_sculpt_tool: curves_sculpt_tool
    :type curves_sculpt_tool: typing.Union[int, str]
    :param toggle: Toggle, Toggle between two brushes rather than cycling
    :type toggle: bool
    :param create_missing: Create Missing, If the requested brush type does not exist, create a new brush
    :type create_missing: bool
    '''

    pass


def face_select_all(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    action: typing.Union[str, int] = 'TOGGLE'):
    ''' Change selection for all faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def face_select_hide(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     unselected: bool = False):
    ''' Hide selected faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param unselected: Unselected, Hide unselected rather than selected objects
    :type unselected: bool
    '''

    pass


def face_select_linked(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Select linked faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def face_select_linked_pick(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None,
                            *,
                            deselect: bool = False):
    ''' Select linked faces under the cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param deselect: Deselect, Deselect rather than select items
    :type deselect: bool
    '''

    pass


def face_vert_reveal(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     select: bool = True):
    ''' Reveal hidden faces and vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param select: Select, Specifies whether the newly revealed geometry should be selected
    :type select: bool
    '''

    pass


def grab_clone(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        delta: typing.Union[typing.List[float], typing.
                            Tuple[float, float], 'mathutils.Vector'] = (0.0,
                                                                        0.0)):
    ''' Move the clone source image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param delta: Delta, Delta offset of clone image in 0.0 to 1.0 coordinates
    :type delta: typing.Union[typing.List[float], typing.Tuple[float, float], 'mathutils.Vector']
    '''

    pass


def hide_show(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              action: typing.Union[str, int] = 'HIDE',
              area: typing.Union[str, int] = 'INSIDE',
              xmin: int = 0,
              xmax: int = 0,
              ymin: int = 0,
              ymax: int = 0,
              wait_for_input: bool = True):
    ''' Hide/show some vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param action: Action, Whether to hide or show vertices * HIDE Hide -- Hide vertices. * SHOW Show -- Show vertices.
    :type action: typing.Union[str, int]
    :param area: Area, Which vertices to hide or show * OUTSIDE Outside -- Hide or show vertices outside the selection. * INSIDE Inside -- Hide or show vertices inside the selection. * ALL All -- Hide or show all vertices. * MASKED Masked -- Hide or show vertices that are masked (minimum mask value of 0.5).
    :type area: typing.Union[str, int]
    :param xmin: X Min
    :type xmin: int
    :param xmax: X Max
    :type xmax: int
    :param ymin: Y Min
    :type ymin: int
    :param ymax: Y Max
    :type ymax: int
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def image_from_view(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    filepath: str = ""):
    ''' Make an image from biggest 3D view for reprojection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Name of the file
    :type filepath: str
    '''

    pass


def image_paint(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                stroke: bpy.types.
                bpy_prop_collection['bpy.types.OperatorStrokeElement'] = None,
                mode: typing.Union[str, int] = 'NORMAL'):
    ''' Paint a stroke into the image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param stroke: Stroke
    :type stroke: bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']
    :param mode: Stroke Mode, Action taken when a paint stroke is made * NORMAL Regular -- Apply brush normally. * INVERT Invert -- Invert action of brush for duration of stroke. * SMOOTH Smooth -- Switch brush to smooth mode for duration of stroke.
    :type mode: typing.Union[str, int]
    '''

    pass


def mask_box_gesture(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     xmin: int = 0,
                     xmax: int = 0,
                     ymin: int = 0,
                     ymax: int = 0,
                     wait_for_input: bool = True,
                     use_front_faces_only: bool = False,
                     use_limit_to_segment: bool = False,
                     mode: typing.Union[str, int] = 'VALUE',
                     value: float = 1.0):
    ''' Add mask within the box as you move the brush

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param xmin: X Min
    :type xmin: int
    :param xmax: X Max
    :type xmax: int
    :param ymin: Y Min
    :type ymin: int
    :param ymax: Y Max
    :type ymax: int
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: bool
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    :type use_limit_to_segment: bool
    :param mode: Mode * VALUE Value -- Set mask to the level specified by the 'value' property. * VALUE_INVERSE Value Inverted -- Set mask to the level specified by the inverted 'value' property. * INVERT Invert -- Invert the mask.
    :type mode: typing.Union[str, int]
    :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
    :type value: float
    '''

    pass


def mask_flood_fill(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    mode: typing.Union[str, int] = 'VALUE',
                    value: float = 0.0):
    ''' Fill the whole mask with a given value, or invert its values

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode * VALUE Value -- Set mask to the level specified by the 'value' property. * VALUE_INVERSE Value Inverted -- Set mask to the level specified by the inverted 'value' property. * INVERT Invert -- Invert the mask.
    :type mode: typing.Union[str, int]
    :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
    :type value: float
    '''

    pass


def mask_lasso_gesture(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        path: bpy.types.
        bpy_prop_collection['bpy.types.OperatorMousePath'] = None,
        use_front_faces_only: bool = False,
        use_limit_to_segment: bool = False,
        mode: typing.Union[str, int] = 'VALUE',
        value: float = 1.0):
    ''' Add mask within the lasso as you move the brush

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param path: Path
    :type path: bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: bool
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    :type use_limit_to_segment: bool
    :param mode: Mode * VALUE Value -- Set mask to the level specified by the 'value' property. * VALUE_INVERSE Value Inverted -- Set mask to the level specified by the inverted 'value' property. * INVERT Invert -- Invert the mask.
    :type mode: typing.Union[str, int]
    :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
    :type value: float
    '''

    pass


def mask_line_gesture(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      xstart: int = 0,
                      xend: int = 0,
                      ystart: int = 0,
                      yend: int = 0,
                      flip: bool = False,
                      cursor: int = 5,
                      use_front_faces_only: bool = False,
                      use_limit_to_segment: bool = False,
                      mode: typing.Union[str, int] = 'VALUE',
                      value: float = 1.0):
    ''' Add mask to the right of a line as you move the brush

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param xstart: X Start
    :type xstart: int
    :param xend: X End
    :type xend: int
    :param ystart: Y Start
    :type ystart: int
    :param yend: Y End
    :type yend: int
    :param flip: Flip
    :type flip: bool
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: int
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: bool
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    :type use_limit_to_segment: bool
    :param mode: Mode * VALUE Value -- Set mask to the level specified by the 'value' property. * VALUE_INVERSE Value Inverted -- Set mask to the level specified by the inverted 'value' property. * INVERT Invert -- Invert the mask.
    :type mode: typing.Union[str, int]
    :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
    :type value: float
    '''

    pass


def project_image(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  image: typing.Union[str, int] = ''):
    ''' Project an edited render from the active camera back onto the object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param image: Image
    :type image: typing.Union[str, int]
    '''

    pass


def sample_color(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 location: typing.List[int] = (0, 0),
                 merged: bool = False,
                 palette: bool = False):
    ''' Use the mouse to sample a color in the image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param location: Location
    :type location: typing.List[int]
    :param merged: Sample Merged, Sample the output display color
    :type merged: bool
    :param palette: Add to Palette
    :type palette: bool
    '''

    pass


def texture_paint_toggle(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None):
    ''' Toggle texture paint mode in 3D view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vert_select_all(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    action: typing.Union[str, int] = 'TOGGLE'):
    ''' Change selection for all vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def vert_select_hide(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     unselected: bool = False):
    ''' Hide selected vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param unselected: Unselected, Hide unselected rather than selected vertices
    :type unselected: bool
    '''

    pass


def vert_select_ungrouped(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          extend: bool = False):
    ''' Select vertices without a group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend the selection
    :type extend: bool
    '''

    pass


def vertex_color_brightness_contrast(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        brightness: float = 0.0,
        contrast: float = 0.0):
    ''' Adjust vertex color brightness/contrast

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param brightness: Brightness
    :type brightness: float
    :param contrast: Contrast
    :type contrast: float
    '''

    pass


def vertex_color_dirt(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      blur_strength: float = 1.0,
                      blur_iterations: int = 1,
                      clean_angle: float = 3.14159,
                      dirt_angle: float = 0.0,
                      dirt_only: bool = False,
                      normalize: bool = True):
    ''' Generate a dirt map gradient based on cavity

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param blur_strength: Blur Strength, Blur strength per iteration
    :type blur_strength: float
    :param blur_iterations: Blur Iterations, Number of times to blur the colors (higher blurs more)
    :type blur_iterations: int
    :param clean_angle: Highlight Angle, Less than 90 limits the angle used in the tonal range
    :type clean_angle: float
    :param dirt_angle: Dirt Angle, Less than 90 limits the angle used in the tonal range
    :type dirt_angle: float
    :param dirt_only: Dirt Only, Don't calculate cleans for convex areas
    :type dirt_only: bool
    :param normalize: Normalize, Normalize the colors, increasing the contrast
    :type normalize: bool
    '''

    pass


def vertex_color_from_weight(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None):
    ''' Convert active weight into gray scale vertex colors

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_color_hsv(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     h: float = 0.5,
                     s: float = 1.0,
                     v: float = 1.0):
    ''' Adjust vertex color HSV values

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param h: Hue
    :type h: float
    :param s: Saturation
    :type s: float
    :param v: Value
    :type v: float
    '''

    pass


def vertex_color_invert(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Invert RGB values

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_color_levels(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        offset: float = 0.0,
                        gain: float = 1.0):
    ''' Adjust levels of vertex colors

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param offset: Offset, Value to add to colors
    :type offset: float
    :param gain: Gain, Value to multiply colors by
    :type gain: float
    '''

    pass


def vertex_color_set(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Fill the active vertex color layer with the current paint color

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_color_smooth(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Smooth colors across vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_paint(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 stroke: bpy.types.
                 bpy_prop_collection['bpy.types.OperatorStrokeElement'] = None,
                 mode: typing.Union[str, int] = 'NORMAL'):
    ''' Paint a stroke in the active color attribute layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param stroke: Stroke
    :type stroke: bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']
    :param mode: Stroke Mode, Action taken when a paint stroke is made * NORMAL Regular -- Apply brush normally. * INVERT Invert -- Invert action of brush for duration of stroke. * SMOOTH Smooth -- Switch brush to smooth mode for duration of stroke.
    :type mode: typing.Union[str, int]
    '''

    pass


def vertex_paint_toggle(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Toggle the vertex paint mode in 3D view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def weight_from_bones(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      type: typing.Union[str, int] = 'AUTOMATIC'):
    ''' Set the weights of the groups matching the attached armature's selected bones, using the distance between the vertices and the bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Method to use for assigning weights * AUTOMATIC Automatic -- Automatic weights from bones. * ENVELOPES From Envelopes -- Weights from envelopes with user defined radius.
    :type type: typing.Union[str, int]
    '''

    pass


def weight_gradient(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    type: typing.Union[str, int] = 'LINEAR',
                    xstart: int = 0,
                    xend: int = 0,
                    ystart: int = 0,
                    yend: int = 0,
                    flip: bool = False,
                    cursor: int = 5):
    ''' Draw a line to apply a weight gradient to selected vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    :param xstart: X Start
    :type xstart: int
    :param xend: X End
    :type xend: int
    :param ystart: Y Start
    :type ystart: int
    :param yend: Y End
    :type yend: int
    :param flip: Flip
    :type flip: bool
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: int
    '''

    pass


def weight_paint(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 stroke: bpy.types.
                 bpy_prop_collection['bpy.types.OperatorStrokeElement'] = None,
                 mode: typing.Union[str, int] = 'NORMAL'):
    ''' Paint a stroke in the current vertex group's weights

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param stroke: Stroke
    :type stroke: bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']
    :param mode: Stroke Mode, Action taken when a paint stroke is made * NORMAL Regular -- Apply brush normally. * INVERT Invert -- Invert action of brush for duration of stroke. * SMOOTH Smooth -- Switch brush to smooth mode for duration of stroke.
    :type mode: typing.Union[str, int]
    '''

    pass


def weight_paint_toggle(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Toggle weight paint mode in 3D view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def weight_sample(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Use the mouse to sample a weight in the 3D view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def weight_sample_group(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        group: typing.Union[str, int] = ''):
    ''' Select one of the vertex groups available under current mouse position

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param group: Group, Vertex group to set as active
    :type group: typing.Union[str, int]
    '''

    pass


def weight_set(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Fill the active vertex group with the current paint weight

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass
