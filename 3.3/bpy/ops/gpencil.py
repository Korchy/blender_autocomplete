import sys
import typing
import bpy.types
import bpy.ops.transform
import mathutils

GenericType = typing.TypeVar("GenericType")


def active_frame_delete(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Delete the active frame for the active Grease Pencil Layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def active_frames_delete_all(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None):
    ''' Delete the active frame(s) of all editable Grease Pencil layers

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def annotate(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             mode: typing.Union[str, int] = 'DRAW',
             arrowstyle_start: typing.Union[str, int] = 'NONE',
             arrowstyle_end: typing.Union[str, int] = 'NONE',
             use_stabilizer: bool = False,
             stabilizer_factor: float = 0.75,
             stabilizer_radius: int = 35,
             stroke: bpy.types.
             bpy_prop_collection['bpy.types.OperatorStrokeElement'] = None,
             wait_for_input: bool = True):
    ''' Make annotations on the active data

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode, Way to interpret mouse movements * DRAW Draw Freehand -- Draw freehand stroke(s). * DRAW_STRAIGHT Draw Straight Lines -- Draw straight line segment(s). * DRAW_POLY Draw Poly Line -- Click to place endpoints of straight line segments (connected). * ERASER Eraser -- Erase Annotation strokes.
    :type mode: typing.Union[str, int]
    :param arrowstyle_start: Start Arrow Style, Stroke start style * NONE None -- Don't use any arrow/style in corner. * ARROW Arrow -- Use closed arrow style. * ARROW_OPEN Open Arrow -- Use open arrow style. * ARROW_OPEN_INVERTED Segment -- Use perpendicular segment style. * DIAMOND Square -- Use square style.
    :type arrowstyle_start: typing.Union[str, int]
    :param arrowstyle_end: End Arrow Style, Stroke end style * NONE None -- Don't use any arrow/style in corner. * ARROW Arrow -- Use closed arrow style. * ARROW_OPEN Open Arrow -- Use open arrow style. * ARROW_OPEN_INVERTED Segment -- Use perpendicular segment style. * DIAMOND Square -- Use square style.
    :type arrowstyle_end: typing.Union[str, int]
    :param use_stabilizer: Stabilize Stroke, Helper to draw smooth and clean lines. Press Shift for an invert effect (even if this option is not active)
    :type use_stabilizer: bool
    :param stabilizer_factor: Stabilizer Stroke Factor, Higher values gives a smoother stroke
    :type stabilizer_factor: float
    :param stabilizer_radius: Stabilizer Stroke Radius, Minimum distance from last point before stroke continues
    :type stabilizer_radius: int
    :param stroke: Stroke
    :type stroke: bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']
    :param wait_for_input: Wait for Input, Wait for first click instead of painting immediately
    :type wait_for_input: bool
    '''

    pass


def annotation_active_frame_delete(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Delete the active frame for the active Annotation Layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def annotation_add(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Add new Annotation data-block

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def bake_grease_pencil_animation(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        frame_start: int = 1,
        frame_end: int = 250,
        step: int = 1,
        only_selected: bool = False,
        frame_target: int = 1,
        project_type: typing.Union[str, int] = 'KEEP'):
    ''' Bake grease pencil object transform to grease pencil keyframes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame_start: Start Frame, The start frame
    :type frame_start: int
    :param frame_end: End Frame, The end frame of animation
    :type frame_end: int
    :param step: Step, Step between generated frames
    :type step: int
    :param only_selected: Only Selected Keyframes, Convert only selected keyframes
    :type only_selected: bool
    :param frame_target: Target Frame, Destination frame
    :type frame_target: int
    :param project_type: Projection Type * KEEP No Reproject. * FRONT Front -- Reproject the strokes using the X-Z plane. * SIDE Side -- Reproject the strokes using the Y-Z plane. * TOP Top -- Reproject the strokes using the X-Y plane. * VIEW View -- Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using 'Cursor' Stroke Placement. * CURSOR Cursor -- Reproject the strokes using the orientation of 3D cursor.
    :type project_type: typing.Union[str, int]
    '''

    pass


def bake_mesh_animation(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        target: typing.Union[str, int] = 'NEW',
                        frame_start: int = 1,
                        frame_end: int = 250,
                        step: int = 1,
                        thickness: int = 1,
                        angle: float = 1.22173,
                        offset: float = 0.001,
                        seams: bool = False,
                        faces: bool = True,
                        only_selected: bool = False,
                        frame_target: int = 1,
                        project_type: typing.Union[str, int] = 'VIEW'):
    ''' Bake mesh animation to grease pencil strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param target: Target Object, Target grease pencil
    :type target: typing.Union[str, int]
    :param frame_start: Start Frame, The start frame
    :type frame_start: int
    :param frame_end: End Frame, The end frame of animation
    :type frame_end: int
    :param step: Step, Step between generated frames
    :type step: int
    :param thickness: Thickness
    :type thickness: int
    :param angle: Threshold Angle, Threshold to determine ends of the strokes
    :type angle: float
    :param offset: Stroke Offset, Offset strokes from fill
    :type offset: float
    :param seams: Only Seam Edges, Convert only seam edges
    :type seams: bool
    :param faces: Export Faces, Export faces as filled strokes
    :type faces: bool
    :param only_selected: Only Selected Keyframes, Convert only selected keyframes
    :type only_selected: bool
    :param frame_target: Target Frame, Destination frame
    :type frame_target: int
    :param project_type: Projection Type * KEEP No Reproject. * FRONT Front -- Reproject the strokes using the X-Z plane. * SIDE Side -- Reproject the strokes using the Y-Z plane. * TOP Top -- Reproject the strokes using the X-Y plane. * VIEW View -- Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using 'Cursor' Stroke Placement. * CURSOR Cursor -- Reproject the strokes using the orientation of 3D cursor.
    :type project_type: typing.Union[str, int]
    '''

    pass


def blank_frame_add(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    all_layers: bool = False):
    ''' Insert a blank frame on the current frame (all subsequently existing frames, if any, are shifted right by one frame)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param all_layers: All Layers, Create blank frame in all layers, not only active
    :type all_layers: bool
    '''

    pass


def brush_reset(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Reset brush to default parameters

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def brush_reset_all(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Delete all mode brushes and recreate a default set

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def convert(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: bool = None,
            *,
            type: typing.Union[str, int] = 'PATH',
            bevel_depth: float = 0.0,
            bevel_resolution: int = 0,
            use_normalize_weights: bool = True,
            radius_multiplier: float = 1.0,
            use_link_strokes: bool = False,
            timing_mode: typing.Union[str, int] = 'FULL',
            frame_range: int = 100,
            start_frame: int = 1,
            use_realtime: bool = False,
            end_frame: int = 250,
            gap_duration: float = 0.0,
            gap_randomness: float = 0.0,
            seed: int = 0,
            use_timing_data: bool = False):
    ''' Convert the active Grease Pencil layer to a new Curve Object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Which type of curve to convert to * PATH Path -- Animation path. * CURVE Bezier Curve -- Smooth Bezier curve. * POLY Polygon Curve -- Bezier curve with straight-line segments (vector handles).
    :type type: typing.Union[str, int]
    :param bevel_depth: Bevel Depth
    :type bevel_depth: float
    :param bevel_resolution: Bevel Resolution, Bevel resolution when depth is non-zero
    :type bevel_resolution: int
    :param use_normalize_weights: Normalize Weight, Normalize weight (set from stroke width)
    :type use_normalize_weights: bool
    :param radius_multiplier: Radius Factor, Multiplier for the points' radii (set from stroke width)
    :type radius_multiplier: float
    :param use_link_strokes: Link Strokes, Whether to link strokes with zero-radius sections of curves
    :type use_link_strokes: bool
    :param timing_mode: Timing Mode, How to use timing data stored in strokes * NONE No Timing -- Ignore timing. * LINEAR Linear -- Simple linear timing. * FULL Original -- Use the original timing, gaps included. * CUSTOMGAP Custom Gaps -- Use the original timing, but with custom gap lengths (in frames).
    :type timing_mode: typing.Union[str, int]
    :param frame_range: Frame Range, The duration of evaluation of the path control curve
    :type frame_range: int
    :param start_frame: Start Frame, The start frame of the path control curve
    :type start_frame: int
    :param use_realtime: Realtime, Whether the path control curve reproduces the drawing in realtime, starting from Start Frame
    :type use_realtime: bool
    :param end_frame: End Frame, The end frame of the path control curve (if Realtime is not set)
    :type end_frame: int
    :param gap_duration: Gap Duration, Custom Gap mode: (Average) length of gaps, in frames (Note: Realtime value, will be scaled if Realtime is not set)
    :type gap_duration: float
    :param gap_randomness: Gap Randomness, Custom Gap mode: Number of frames that gap lengths can vary
    :type gap_randomness: float
    :param seed: Random Seed, Custom Gap mode: Random generator seed
    :type seed: int
    :param use_timing_data: Has Valid Timing, Whether the converted Grease Pencil layer has valid timing data (internal use)
    :type use_timing_data: bool
    '''

    pass


def convert_old_files(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      annotation: bool = False):
    ''' Convert 2.7x grease pencil files to 2.80

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param annotation: Annotation, Convert to Annotations
    :type annotation: bool
    '''

    pass


def copy(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None):
    ''' Copy selected Grease Pencil points and strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def data_unlink(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Unlink active Annotation data-block

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           type: typing.Union[str, int] = 'POINTS'):
    ''' Delete selected Grease Pencil strokes, vertices, or frames

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Method used for deleting Grease Pencil data * POINTS Points -- Delete selected points and split strokes into segments. * STROKES Strokes -- Delete selected strokes. * FRAME Frame -- Delete active frame.
    :type type: typing.Union[str, int]
    '''

    pass


def dissolve(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             type: typing.Union[str, int] = 'POINTS'):
    ''' Delete selected points without splitting strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Method used for dissolving stroke points * POINTS Dissolve -- Dissolve selected points. * BETWEEN Dissolve Between -- Dissolve points between selected points. * UNSELECT Dissolve Unselect -- Dissolve all unselected points.
    :type type: typing.Union[str, int]
    '''

    pass


def draw(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         mode: typing.Union[str, int] = 'DRAW',
         stroke: bpy.types.
         bpy_prop_collection['bpy.types.OperatorStrokeElement'] = None,
         wait_for_input: bool = True,
         disable_straight: bool = False,
         disable_fill: bool = False,
         disable_stabilizer: bool = False,
         guide_last_angle: float = 0.0):
    ''' Draw a new stroke in the active Grease Pencil object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode, Way to interpret mouse movements * DRAW Draw Freehand -- Draw freehand stroke(s). * DRAW_STRAIGHT Draw Straight Lines -- Draw straight line segment(s). * ERASER Eraser -- Erase Grease Pencil strokes.
    :type mode: typing.Union[str, int]
    :param stroke: Stroke
    :type stroke: bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']
    :param wait_for_input: Wait for Input, Wait for first click instead of painting immediately
    :type wait_for_input: bool
    :param disable_straight: No Straight lines, Disable key for straight lines
    :type disable_straight: bool
    :param disable_fill: No Fill Areas, Disable fill to use stroke as fill boundary
    :type disable_fill: bool
    :param disable_stabilizer: No Stabilizer
    :type disable_stabilizer: bool
    :param guide_last_angle: Angle, Speed guide angle
    :type guide_last_angle: float
    '''

    pass


def duplicate(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Duplicate the selected Grease Pencil strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def duplicate_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        GPENCIL_OT_duplicate: 'duplicate' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Make copies of the selected Grease Pencil strokes and move them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param GPENCIL_OT_duplicate: Duplicate Strokes, Duplicate the selected Grease Pencil strokes
    :type GPENCIL_OT_duplicate: 'duplicate'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def editmode_toggle(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    back: bool = False):
    ''' Enter/Exit edit mode for Grease Pencil strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param back: Return to Previous Mode, Return to previous mode
    :type back: bool
    '''

    pass


def extract_palette_vertex(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None,
                           *,
                           selected: bool = False,
                           threshold: int = 1):
    ''' Extract all colors used in Grease Pencil Vertex and create a Palette

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param selected: Only Selected, Convert only selected strokes
    :type selected: bool
    :param threshold: Threshold
    :type threshold: int
    '''

    pass


def extrude(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: bool = None):
    ''' Extrude the selected Grease Pencil points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def extrude_move(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 GPENCIL_OT_extrude: 'extrude' = None,
                 TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Extrude selected points and move them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param GPENCIL_OT_extrude: Extrude Stroke Points, Extrude the selected Grease Pencil points
    :type GPENCIL_OT_extrude: 'extrude'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def fill(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         on_back: bool = False):
    ''' Fill with color the shape formed by strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param on_back: Draw on Back, Send new stroke to back
    :type on_back: bool
    '''

    pass


def frame_clean_duplicate(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          type: typing.Union[str, int] = 'ALL'):
    ''' Remove any duplicated frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def frame_clean_fill(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     mode: typing.Union[str, int] = 'ACTIVE'):
    ''' Remove 'no fill' boundary strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode * ACTIVE Active Frame Only -- Clean active frame only. * ALL All Frames -- Clean all frames in all layers.
    :type mode: typing.Union[str, int]
    '''

    pass


def frame_clean_loose(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      limit: int = 1):
    ''' Remove loose points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param limit: Limit, Number of points to consider stroke as loose
    :type limit: int
    '''

    pass


def frame_duplicate(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    mode: typing.Union[str, int] = 'ACTIVE'):
    ''' Make a copy of the active Grease Pencil Frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode * ACTIVE Active -- Duplicate frame in active layer only. * ALL All -- Duplicate active frames in all layers.
    :type mode: typing.Union[str, int]
    '''

    pass


def generate_weights(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     mode: typing.Union[str, int] = 'NAME',
                     armature: typing.Union[str, int] = 'DEFAULT',
                     ratio: float = 0.1,
                     decay: float = 0.8):
    ''' Generate automatic weights for armatures (requires armature modifier)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param armature: Armature, Armature to use
    :type armature: typing.Union[str, int]
    :param ratio: Ratio, Ratio between bone length and influence radius
    :type ratio: float
    :param decay: Decay, Factor to reduce influence depending of distance to bone axis
    :type decay: float
    '''

    pass


def guide_rotate(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 increment: bool = True,
                 angle: float = 0.0):
    ''' Rotate guide angle

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param increment: Increment, Increment angle
    :type increment: bool
    :param angle: Angle, Guide angle
    :type angle: float
    '''

    pass


def hide(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         unselected: bool = False):
    ''' Hide selected/unselected Grease Pencil layers

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param unselected: Unselected, Hide unselected rather than selected layers
    :type unselected: bool
    '''

    pass


def image_to_grease_pencil(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None,
                           *,
                           size: float = 0.005,
                           mask: bool = False):
    ''' Generate a Grease Pencil Object using Image as source

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param size: Point Size, Size used for grease pencil points
    :type size: float
    :param mask: Generate Mask, Create an inverted image for masking using alpha channel
    :type mask: bool
    '''

    pass


def interpolate(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                shift: float = 0.0,
                layers: typing.Union[str, int] = 'ACTIVE',
                interpolate_selected_only: bool = False,
                flip: typing.Union[str, int] = 'AUTO',
                smooth_steps: int = 1,
                smooth_factor: float = 0.0,
                release_confirm: bool = False):
    ''' Interpolate grease pencil strokes between frames

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param shift: Shift, Bias factor for which frame has more influence on the interpolated strokes
    :type shift: float
    :param layers: Layer, Layers included in the interpolation
    :type layers: typing.Union[str, int]
    :param interpolate_selected_only: Only Selected, Interpolate only selected strokes
    :type interpolate_selected_only: bool
    :param flip: Flip Mode, Invert destination stroke to match start and end with source stroke
    :type flip: typing.Union[str, int]
    :param smooth_steps: Iterations, Number of times to smooth newly created strokes
    :type smooth_steps: int
    :param smooth_factor: Smooth, Amount of smoothing to apply to interpolated strokes, to reduce jitter/noise
    :type smooth_factor: float
    :param release_confirm: Confirm on Release
    :type release_confirm: bool
    '''

    pass


def interpolate_reverse(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Remove breakdown frames generated by interpolating between two Grease Pencil frames

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def interpolate_sequence(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         step: int = 1,
                         layers: typing.Union[str, int] = 'ACTIVE',
                         interpolate_selected_only: bool = False,
                         flip: typing.Union[str, int] = 'AUTO',
                         smooth_steps: int = 1,
                         smooth_factor: float = 0.0,
                         type: typing.Union[str, int] = 'LINEAR',
                         easing: typing.Union[str, int] = 'AUTO',
                         back: float = 1.702,
                         amplitude: float = 0.15,
                         period: float = 0.15):
    ''' Generate 'in-betweens' to smoothly interpolate between Grease Pencil frames

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param step: Step, Number of frames between generated interpolated frames
    :type step: int
    :param layers: Layer, Layers included in the interpolation
    :type layers: typing.Union[str, int]
    :param interpolate_selected_only: Only Selected, Interpolate only selected strokes
    :type interpolate_selected_only: bool
    :param flip: Flip Mode, Invert destination stroke to match start and end with source stroke
    :type flip: typing.Union[str, int]
    :param smooth_steps: Iterations, Number of times to smooth newly created strokes
    :type smooth_steps: int
    :param smooth_factor: Smooth, Amount of smoothing to apply to interpolated strokes, to reduce jitter/noise
    :type smooth_factor: float
    :param type: Type, Interpolation method to use the next time 'Interpolate Sequence' is run * LINEAR Linear -- Straight-line interpolation between A and B (i.e. no ease in/out). * CUSTOM Custom -- Custom interpolation defined using a curve map. * SINE Sinusoidal -- Sinusoidal easing (weakest, almost linear but with a slight curvature). * QUAD Quadratic -- Quadratic easing. * CUBIC Cubic -- Cubic easing. * QUART Quartic -- Quartic easing. * QUINT Quintic -- Quintic easing. * EXPO Exponential -- Exponential easing (dramatic). * CIRC Circular -- Circular easing (strongest and most dynamic). * BACK Back -- Cubic easing with overshoot and settle. * BOUNCE Bounce -- Exponentially decaying parabolic bounce, like when objects collide. * ELASTIC Elastic -- Exponentially decaying sine wave, like an elastic band.
    :type type: typing.Union[str, int]
    :param easing: Easing, Which ends of the segment between the preceding and following grease pencil frames easing interpolation is applied to * AUTO Automatic Easing -- Easing type is chosen automatically based on what the type of interpolation used (e.g. 'Ease In' for transitional types, and 'Ease Out' for dynamic effects). * EASE_IN Ease In -- Only on the end closest to the next keyframe. * EASE_OUT Ease Out -- Only on the end closest to the first keyframe. * EASE_IN_OUT Ease In and Out -- Segment between both keyframes.
    :type easing: typing.Union[str, int]
    :param back: Back, Amount of overshoot for 'back' easing
    :type back: float
    :param amplitude: Amplitude, Amount to boost elastic bounces for 'elastic' easing
    :type amplitude: float
    :param period: Period, Time between bounces for elastic easing
    :type period: float
    '''

    pass


def layer_active(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 layer: int = 0):
    ''' Active Grease Pencil layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param layer: Grease Pencil Layer
    :type layer: int
    '''

    pass


def layer_add(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Add new layer or note for the active data-block

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def layer_annotation_add(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None):
    ''' Add new Annotation layer or note for the active data-block

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def layer_annotation_move(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          type: typing.Union[str, int] = 'UP'):
    ''' Move the active Annotation layer up/down in the list

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def layer_annotation_remove(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None):
    ''' Remove active Annotation layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def layer_change(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 layer: typing.Union[str, int] = 'DEFAULT'):
    ''' Change active Grease Pencil layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param layer: Grease Pencil Layer
    :type layer: typing.Union[str, int]
    '''

    pass


def layer_duplicate(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    mode: typing.Union[str, int] = 'ALL'):
    ''' Make a copy of the active Grease Pencil layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    '''

    pass


def layer_duplicate_object(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None,
                           *,
                           mode: typing.Union[str, int] = 'ALL',
                           only_active: bool = True):
    ''' Make a copy of the active Grease Pencil layer to selected object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param only_active: Only Active, Copy only active Layer, uncheck to append all layers
    :type only_active: bool
    '''

    pass


def layer_isolate(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  affect_visibility: bool = False):
    ''' Toggle whether the active layer is the only one that can be edited and/or visible

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param affect_visibility: Affect Visibility, In addition to toggling the editability, also affect the visibility
    :type affect_visibility: bool
    '''

    pass


def layer_mask_add(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   name: str = ""):
    ''' Add new layer as masking

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Layer, Name of the layer
    :type name: str
    '''

    pass


def layer_mask_move(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    type: typing.Union[str, int] = 'UP'):
    ''' Move the active Grease Pencil mask layer up/down in the list

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def layer_mask_remove(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Remove Layer Mask

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def layer_merge(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                mode: typing.Union[str, int] = 'ACTIVE'):
    ''' Combine Layers

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode * ACTIVE Active -- Combine active layer into the layer below. * ALL All -- Combine all layers into the active layer.
    :type mode: typing.Union[str, int]
    '''

    pass


def layer_move(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               type: typing.Union[str, int] = 'UP'):
    ''' Move the active Grease Pencil layer up/down in the list

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def layer_remove(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Remove active Grease Pencil layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def lock_all(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None):
    ''' Lock all Grease Pencil layers to prevent them from being accidentally modified

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def lock_layer(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Lock and hide any color not used in any layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def material_hide(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  unselected: bool = False):
    ''' Hide selected/unselected Grease Pencil materials

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param unselected: Unselected, Hide unselected rather than selected colors
    :type unselected: bool
    '''

    pass


def material_isolate(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     affect_visibility: bool = False):
    ''' Toggle whether the active material is the only one that is editable and/or visible

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param affect_visibility: Affect Visibility, In addition to toggling the editability, also affect the visibility
    :type affect_visibility: bool
    '''

    pass


def material_lock_all(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Lock all Grease Pencil materials to prevent them from being accidentally modified

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def material_lock_unused(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None):
    ''' Lock any material not used in any selected stroke

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def material_reveal(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Unhide all hidden Grease Pencil materials

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def material_select(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    deselect: bool = False):
    ''' Select/Deselect all Grease Pencil strokes using current material

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param deselect: Deselect, Unselect strokes
    :type deselect: bool
    '''

    pass


def material_set(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 slot: typing.Union[str, int] = 'DEFAULT'):
    ''' Set active material

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param slot: Material Slot
    :type slot: typing.Union[str, int]
    '''

    pass


def material_to_vertex_color(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None,
                             *,
                             remove: bool = True,
                             palette: bool = True,
                             selected: bool = False,
                             threshold: int = 3):
    ''' Replace materials in strokes with Vertex Color

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param remove: Remove Unused Materials, Remove any unused material after the conversion
    :type remove: bool
    :param palette: Create Palette, Create a new palette with colors
    :type palette: bool
    :param selected: Only Selected, Convert only selected strokes
    :type selected: bool
    :param threshold: Threshold
    :type threshold: int
    '''

    pass


def material_unlock_all(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Unlock all Grease Pencil materials so that they can be edited

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def materials_copy_to_object(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None,
                             *,
                             only_active: bool = True):
    ''' Append Materials of the active Grease Pencil to other object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param only_active: Only Active, Append only active material, uncheck to append all materials
    :type only_active: bool
    '''

    pass


def move_to_layer(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  layer: int = 0,
                  new_layer_name: str = ""):
    ''' Move selected strokes to another layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param layer: Grease Pencil Layer
    :type layer: int
    :param new_layer_name: Name, Name of the newly added layer
    :type new_layer_name: str
    '''

    pass


def paintmode_toggle(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     back: bool = False):
    ''' Enter/Exit paint mode for Grease Pencil strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param back: Return to Previous Mode, Return to previous mode
    :type back: bool
    '''

    pass


def paste(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None,
          *,
          type: typing.Union[str, int] = 'ACTIVE',
          paste_back: bool = False):
    ''' Paste previously copied strokes to active layer or to original layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    :param paste_back: Paste on Back, Add pasted strokes behind all strokes
    :type paste_back: bool
    '''

    pass


def primitive_box(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  subdivision: int = 3,
                  edges: int = 1,
                  type: typing.Union[str, int] = 'BOX',
                  wait_for_input: bool = True):
    ''' Create predefined grease pencil stroke box shapes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param subdivision: Subdivisions, Number of subdivision by edges
    :type subdivision: int
    :param edges: Edges, Number of points by edge
    :type edges: int
    :param type: Type, Type of shape
    :type type: typing.Union[str, int]
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def primitive_circle(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     subdivision: int = 94,
                     edges: int = 1,
                     type: typing.Union[str, int] = 'CIRCLE',
                     wait_for_input: bool = True):
    ''' Create predefined grease pencil stroke circle shapes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param subdivision: Subdivisions, Number of subdivision by edges
    :type subdivision: int
    :param edges: Edges, Number of points by edge
    :type edges: int
    :param type: Type, Type of shape
    :type type: typing.Union[str, int]
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def primitive_curve(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    subdivision: int = 62,
                    edges: int = 1,
                    type: typing.Union[str, int] = 'CURVE',
                    wait_for_input: bool = True):
    ''' Create predefined grease pencil stroke curve shapes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param subdivision: Subdivisions, Number of subdivision by edges
    :type subdivision: int
    :param edges: Edges, Number of points by edge
    :type edges: int
    :param type: Type, Type of shape
    :type type: typing.Union[str, int]
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def primitive_line(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   subdivision: int = 6,
                   edges: int = 1,
                   type: typing.Union[str, int] = 'LINE',
                   wait_for_input: bool = True):
    ''' Create predefined grease pencil stroke lines

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param subdivision: Subdivisions, Number of subdivision by edges
    :type subdivision: int
    :param edges: Edges, Number of points by edge
    :type edges: int
    :param type: Type, Type of shape
    :type type: typing.Union[str, int]
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def primitive_polyline(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       subdivision: int = 6,
                       edges: int = 1,
                       type: typing.Union[str, int] = 'POLYLINE',
                       wait_for_input: bool = True):
    ''' Create predefined grease pencil stroke polylines

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param subdivision: Subdivisions, Number of subdivision by edges
    :type subdivision: int
    :param edges: Edges, Number of points by edge
    :type edges: int
    :param type: Type, Type of shape
    :type type: typing.Union[str, int]
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def recalc_geometry(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Update all internal geometry data

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def reproject(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              type: typing.Union[str, int] = 'VIEW',
              keep_original: bool = False):
    ''' Reproject the selected strokes from the current viewpoint as if they had been newly drawn (e.g. to fix problems from accidental 3D cursor movement or accidental viewport changes, or for matching deforming geometry)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Projection Type * FRONT Front -- Reproject the strokes using the X-Z plane. * SIDE Side -- Reproject the strokes using the Y-Z plane. * TOP Top -- Reproject the strokes using the X-Y plane. * VIEW View -- Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using 'Cursor' Stroke Placement. * SURFACE Surface -- Reproject the strokes on to the scene geometry, as if drawn using 'Surface' placement. * CURSOR Cursor -- Reproject the strokes using the orientation of 3D cursor.
    :type type: typing.Union[str, int]
    :param keep_original: Keep Original, Keep original strokes and create a copy before reprojecting instead of reproject them
    :type keep_original: bool
    '''

    pass


def reset_transform_fill(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         mode: typing.Union[str, int] = 'ALL'):
    ''' Reset any UV transformation and back to default values

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    '''

    pass


def reveal(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           select: bool = True):
    ''' Show all Grease Pencil layers

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param select: Select
    :type select: bool
    '''

    pass


def sculpt_paint(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 stroke: bpy.types.
                 bpy_prop_collection['bpy.types.OperatorStrokeElement'] = None,
                 wait_for_input: bool = True):
    ''' Apply tweaks to strokes by painting over the strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param stroke: Stroke
    :type stroke: bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']
    :param wait_for_input: Wait for Input, Enter a mini 'sculpt-mode' if enabled, otherwise, exit after drawing a single stroke
    :type wait_for_input: bool
    '''

    pass


def sculptmode_toggle(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      back: bool = False):
    ''' Enter/Exit sculpt mode for Grease Pencil strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param back: Return to Previous Mode, Return to previous mode
    :type back: bool
    '''

    pass


def segment_add(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                modifier: str = ""):
    ''' Add a segment to the dash modifier

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def segment_move(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 modifier: str = "",
                 type: typing.Union[str, int] = 'UP'):
    ''' Move the active dash segment up or down

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def segment_remove(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   modifier: str = "",
                   index: int = 0):
    ''' Remove the active segment from the dash modifier

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param index: Index, Index of the segment to remove
    :type index: int
    '''

    pass


def select(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           extend: bool = False,
           deselect: bool = False,
           toggle: bool = False,
           deselect_all: bool = False,
           select_passthrough: bool = False,
           entire_strokes: bool = False,
           location: typing.List[int] = (0, 0),
           use_shift_extend: bool = False):
    ''' Select Grease Pencil strokes and/or stroke points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param deselect: Deselect, Remove from selection
    :type deselect: bool
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: bool
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :type select_passthrough: bool
    :param entire_strokes: Entire Strokes, Select entire strokes instead of just the nearest stroke vertex
    :type entire_strokes: bool
    :param location: Location, Mouse location
    :type location: typing.List[int]
    :param use_shift_extend: Extend
    :type use_shift_extend: bool
    '''

    pass


def select_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               action: typing.Union[str, int] = 'TOGGLE'):
    ''' Change selection of all Grease Pencil strokes currently visible

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_alternate(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     unselect_ends: bool = False):
    ''' Select alternative points in same strokes as already selected points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param unselect_ends: Unselect Ends, Do not select the first and last point of the stroke
    :type unselect_ends: bool
    '''

    pass


def select_box(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               xmin: int = 0,
               xmax: int = 0,
               ymin: int = 0,
               ymax: int = 0,
               wait_for_input: bool = True,
               mode: typing.Union[str, int] = 'SET'):
    ''' Select Grease Pencil strokes within a rectangular region

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
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection. * XOR Difference -- Invert existing selection. * AND Intersect -- Intersect existing selection.
    :type mode: typing.Union[str, int]
    '''

    pass


def select_circle(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  x: int = 0,
                  y: int = 0,
                  radius: int = 25,
                  wait_for_input: bool = True,
                  mode: typing.Union[str, int] = 'SET'):
    ''' Select Grease Pencil strokes using brush selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param x: X
    :type x: int
    :param y: Y
    :type y: int
    :param radius: Radius
    :type radius: int
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection.
    :type mode: typing.Union[str, int]
    '''

    pass


def select_first(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 only_selected_strokes: bool = False,
                 extend: bool = False):
    ''' Select first point in Grease Pencil strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param only_selected_strokes: Selected Strokes Only, Only select the first point of strokes that already have points selected
    :type only_selected_strokes: bool
    :param extend: Extend, Extend selection instead of deselecting all other selected points
    :type extend: bool
    '''

    pass


def select_grouped(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   type: typing.Union[str, int] = 'LAYER'):
    ''' Select all strokes with similar characteristics

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type * LAYER Layer -- Shared layers. * MATERIAL Material -- Shared materials.
    :type type: typing.Union[str, int]
    '''

    pass


def select_lasso(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 mode: typing.Union[str, int] = 'SET',
                 path: bpy.types.
                 bpy_prop_collection['bpy.types.OperatorMousePath'] = None):
    ''' Select Grease Pencil strokes using lasso selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection. * XOR Difference -- Invert existing selection. * AND Intersect -- Intersect existing selection.
    :type mode: typing.Union[str, int]
    :param path: Path
    :type path: bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']
    '''

    pass


def select_last(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                only_selected_strokes: bool = False,
                extend: bool = False):
    ''' Select last point in Grease Pencil strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param only_selected_strokes: Selected Strokes Only, Only select the last point of strokes that already have points selected
    :type only_selected_strokes: bool
    :param extend: Extend, Extend selection instead of deselecting all other selected points
    :type extend: bool
    '''

    pass


def select_less(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Shrink sets of selected Grease Pencil points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_linked(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Select all points in same strokes as already selected points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_more(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Grow sets of selected Grease Pencil points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_random(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  ratio: float = 0.5,
                  seed: int = 0,
                  action: typing.Union[str, int] = 'SELECT',
                  unselect_ends: bool = False):
    ''' Select random points for non selected strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param ratio: Ratio, Portion of items to select randomly
    :type ratio: float
    :param seed: Random Seed, Seed for the random number generator
    :type seed: int
    :param action: Action, Selection action to execute * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements.
    :type action: typing.Union[str, int]
    :param unselect_ends: Unselect Ends, Do not select the first and last point of the stroke
    :type unselect_ends: bool
    '''

    pass


def select_vertex_color(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        threshold: int = 0):
    ''' Select all points with similar vertex color of current selected

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param threshold: Threshold, Tolerance of the selection. Higher values select a wider range of similar colors
    :type threshold: int
    '''

    pass


def selection_opacity_toggle(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None):
    ''' Hide/Unhide selected points for Grease Pencil strokes setting alpha factor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def selectmode_toggle(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      mode: int = 0):
    ''' Set selection mode for Grease Pencil strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Select Mode, Select mode
    :type mode: int
    '''

    pass


def set_active_material(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Set the selected stroke material as the active material

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def snap_cursor_to_selected(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None):
    ''' Snap cursor to center of selected points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def snap_to_cursor(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   use_offset: bool = True):
    ''' Snap selected points/strokes to the cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_offset: With Offset, Offset the entire stroke instead of selected points only
    :type use_offset: bool
    '''

    pass


def snap_to_grid(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Snap selected points to the nearest grid points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def stroke_apply_thickness(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None):
    ''' Apply the thickness change of the layer to its strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def stroke_arrange(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   direction: typing.Union[str, int] = 'UP'):
    ''' Arrange selected strokes up/down in the display order of the active layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param direction: Direction
    :type direction: typing.Union[str, int]
    '''

    pass


def stroke_caps_set(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    type: typing.Union[str, int] = 'TOGGLE'):
    ''' Change stroke caps mode (rounded or flat)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type * TOGGLE Both. * START Start. * END End. * DEFAULT Default -- Set as default rounded.
    :type type: typing.Union[str, int]
    '''

    pass


def stroke_change_color(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        material: str = ""):
    ''' Move selected strokes to active material

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param material: Material, Name of the material
    :type material: str
    '''

    pass


def stroke_cutter(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  path: bpy.types.
                  bpy_prop_collection['bpy.types.OperatorMousePath'] = None,
                  flat_caps: bool = False):
    ''' Select section and cut

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param path: Path
    :type path: bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']
    :param flat_caps: Flat Caps
    :type flat_caps: bool
    '''

    pass


def stroke_cyclical_set(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        type: typing.Union[str, int] = 'TOGGLE',
                        geometry: bool = False):
    ''' Close or open the selected stroke adding an edge from last to first point

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    :param geometry: Create Geometry, Create new geometry for closing stroke
    :type geometry: bool
    '''

    pass


def stroke_editcurve_set_handle_type(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        type: typing.Union[str, int] = 'AUTOMATIC'):
    ''' Set the type of a edit curve handle

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Spline type
    :type type: typing.Union[str, int]
    '''

    pass


def stroke_enter_editcurve_mode(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        error_threshold: float = 0.1):
    ''' Called to transform a stroke into a curve

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param error_threshold: Error Threshold, Threshold on the maximum deviation from the actual stroke
    :type error_threshold: float
    '''

    pass


def stroke_flip(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Change direction of the points of the selected strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def stroke_join(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                type: typing.Union[str, int] = 'JOIN',
                leave_gaps: bool = False):
    ''' Join selected strokes (optionally as new stroke)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    :param leave_gaps: Leave Gaps, Leave gaps between joined strokes instead of linking them
    :type leave_gaps: bool
    '''

    pass


def stroke_merge(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 mode: typing.Union[str, int] = 'STROKE',
                 back: bool = False,
                 additive: bool = False,
                 cyclic: bool = False,
                 clear_point: bool = False,
                 clear_stroke: bool = False):
    ''' Create a new stroke with the selected stroke points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param back: Draw on Back, Draw new stroke below all previous strokes
    :type back: bool
    :param additive: Additive Drawing, Add to previous drawing
    :type additive: bool
    :param cyclic: Cyclic, Close new stroke
    :type cyclic: bool
    :param clear_point: Dissolve Points, Dissolve old selected points
    :type clear_point: bool
    :param clear_stroke: Delete Strokes, Delete old selected strokes
    :type clear_stroke: bool
    '''

    pass


def stroke_merge_by_distance(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None,
                             *,
                             threshold: float = 0.001,
                             use_unselected: bool = False):
    ''' Merge points by distance

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param threshold: Threshold
    :type threshold: float
    :param use_unselected: Unselected, Use whole stroke, not only selected points
    :type use_unselected: bool
    '''

    pass


def stroke_merge_material(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          hue_threshold: float = 0.001,
                          sat_threshold: float = 0.001,
                          val_threshold: float = 0.001):
    ''' Replace materials in strokes merging similar

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param hue_threshold: Hue Threshold
    :type hue_threshold: float
    :param sat_threshold: Saturation Threshold
    :type sat_threshold: float
    :param val_threshold: Value Threshold
    :type val_threshold: float
    '''

    pass


def stroke_normalize(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     mode: typing.Union[str, int] = 'THICKNESS',
                     factor: float = 1.0,
                     value: int = 10):
    ''' Normalize stroke attributes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode, Attribute to be normalized * THICKNESS Thickness -- Normalizes the stroke thickness by making all points use the same thickness value. * OPACITY Opacity -- Normalizes the stroke opacity by making all points use the same opacity value.
    :type mode: typing.Union[str, int]
    :param factor: Factor
    :type factor: float
    :param value: Value, Value
    :type value: int
    '''

    pass


def stroke_reset_vertex_color(override_context: typing.
                              Union[typing.Dict, 'bpy.types.Context'] = None,
                              execution_context: typing.Union[str, int] = None,
                              undo: bool = None,
                              *,
                              mode: typing.Union[str, int] = 'BOTH'):
    ''' Reset vertex color for all or selected strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode * STROKE Stroke -- Reset Vertex Color to Stroke only. * FILL Fill -- Reset Vertex Color to Fill only. * BOTH Stroke & Fill -- Reset Vertex Color to Stroke and Fill.
    :type mode: typing.Union[str, int]
    '''

    pass


def stroke_sample(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  length: float = 0.1,
                  sharp_threshold: float = 0.1):
    ''' Sample stroke points to predefined segment length

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param length: Length
    :type length: float
    :param sharp_threshold: Sharp Threshold
    :type sharp_threshold: float
    '''

    pass


def stroke_separate(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    mode: typing.Union[str, int] = 'POINT'):
    ''' Separate the selected strokes or layer in a new grease pencil object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode * POINT Selected Points -- Separate the selected points. * STROKE Selected Strokes -- Separate the selected strokes. * LAYER Active Layer -- Separate the strokes of the current layer.
    :type mode: typing.Union[str, int]
    '''

    pass


def stroke_simplify(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    factor: float = 0.0):
    ''' Simplify selected stroked reducing number of points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param factor: Factor
    :type factor: float
    '''

    pass


def stroke_simplify_fixed(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          step: int = 1):
    ''' Simplify selected stroked reducing number of points using fixed algorithm

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param step: Steps, Number of simplify steps
    :type step: int
    '''

    pass


def stroke_smooth(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  repeat: int = 2,
                  factor: float = 1.0,
                  only_selected: bool = True,
                  smooth_position: bool = True,
                  smooth_thickness: bool = True,
                  smooth_strength: bool = False,
                  smooth_uv: bool = False):
    ''' Smooth selected strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param repeat: Repeat
    :type repeat: int
    :param factor: Factor
    :type factor: float
    :param only_selected: Selected Points, Smooth only selected points in the stroke
    :type only_selected: bool
    :param smooth_position: Position
    :type smooth_position: bool
    :param smooth_thickness: Thickness
    :type smooth_thickness: bool
    :param smooth_strength: Strength
    :type smooth_strength: bool
    :param smooth_uv: UV
    :type smooth_uv: bool
    '''

    pass


def stroke_split(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Split selected points as new stroke on same frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def stroke_subdivide(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     number_cuts: int = 1,
                     factor: float = 0.0,
                     repeat: int = 1,
                     only_selected: bool = True,
                     smooth_position: bool = True,
                     smooth_thickness: bool = True,
                     smooth_strength: bool = False,
                     smooth_uv: bool = False):
    ''' Subdivide between continuous selected points of the stroke adding a point half way between them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param number_cuts: Number of Cuts
    :type number_cuts: int
    :param factor: Smooth
    :type factor: float
    :param repeat: Repeat
    :type repeat: int
    :param only_selected: Selected Points, Smooth only selected points in the stroke
    :type only_selected: bool
    :param smooth_position: Position
    :type smooth_position: bool
    :param smooth_thickness: Thickness
    :type smooth_thickness: bool
    :param smooth_strength: Strength
    :type smooth_strength: bool
    :param smooth_uv: UV
    :type smooth_uv: bool
    '''

    pass


def stroke_trim(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Trim selected stroke to first loop or intersection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def tint_flip(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Switch tint colors :file: startup/bl_ui/properties_grease_pencil_common.py\:876 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_ui/properties_grease_pencil_common.py$876> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def trace_image(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                target: typing.Union[str, int] = 'NEW',
                thickness: int = 10,
                resolution: int = 5,
                scale: float = 1.0,
                sample: float = 0.0,
                threshold: float = 0.5,
                turnpolicy: typing.Union[str, int] = 'MINORITY',
                mode: typing.Union[str, int] = 'SINGLE',
                use_current_frame: bool = True):
    ''' Extract Grease Pencil strokes from image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param target: Target Object, Target grease pencil
    :type target: typing.Union[str, int]
    :param thickness: Thickness
    :type thickness: int
    :param resolution: Resolution, Resolution of the generated curves
    :type resolution: int
    :param scale: Scale, Scale of the final stroke
    :type scale: float
    :param sample: Sample, Distance to sample points, zero to disable
    :type sample: float
    :param threshold: Color Threshold, Determine the lightness threshold above which strokes are generated
    :type threshold: float
    :param turnpolicy: Turn Policy, Determines how to resolve ambiguities during decomposition of bitmaps into paths * BLACK Black -- Prefers to connect black (foreground) components. * WHITE White -- Prefers to connect white (background) components. * LEFT Left -- Always take a left turn. * RIGHT Right -- Always take a right turn. * MINORITY Minority -- Prefers to connect the color (black or white) that occurs least frequently in the local neighborhood of the current position. * MAJORITY Majority -- Prefers to connect the color (black or white) that occurs most frequently in the local neighborhood of the current position. * RANDOM Random -- Choose pseudo-randomly.
    :type turnpolicy: typing.Union[str, int]
    :param mode: Mode, Determines if trace simple image or full sequence * SINGLE Single -- Trace the current frame of the image. * SEQUENCE Sequence -- Trace full sequence.
    :type mode: typing.Union[str, int]
    :param use_current_frame: Start At Current Frame, Trace Image starting in current image frame
    :type use_current_frame: bool
    '''

    pass


def transform_fill(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        mode: typing.Union[str, int] = 'ROTATE',
        location: typing.Union[typing.List[float], typing.
                               Tuple[float, float], 'mathutils.Vector'] = (
                                   0.0, 0.0),
        rotation: float = 0.0,
        scale: float = 0.0,
        release_confirm: bool = False):
    ''' Transform grease pencil stroke fill

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param location: Location
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float], 'mathutils.Vector']
    :param rotation: Rotation
    :type rotation: float
    :param scale: Scale
    :type scale: float
    :param release_confirm: Confirm on Release
    :type release_confirm: bool
    '''

    pass


def unlock_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Unlock all Grease Pencil layers so that they can be edited

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_color_brightness_contrast(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        mode: typing.Union[str, int] = 'BOTH',
        brightness: float = 0.0,
        contrast: float = 0.0):
    ''' Adjust vertex color brightness/contrast

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param brightness: Brightness
    :type brightness: float
    :param contrast: Contrast
    :type contrast: float
    '''

    pass


def vertex_color_hsv(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     mode: typing.Union[str, int] = 'BOTH',
                     h: float = 0.5,
                     s: float = 1.0,
                     v: float = 1.0):
    ''' Adjust vertex color HSV values

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
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
                        undo: bool = None,
                        *,
                        mode: typing.Union[str, int] = 'BOTH'):
    ''' Invert RGB values

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    '''

    pass


def vertex_color_levels(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        mode: typing.Union[str, int] = 'BOTH',
                        offset: float = 0.0,
                        gain: float = 1.0):
    ''' Adjust levels of vertex colors

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param offset: Offset, Value to add to colors
    :type offset: float
    :param gain: Gain, Value to multiply colors by
    :type gain: float
    '''

    pass


def vertex_color_set(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     mode: typing.Union[str, int] = 'BOTH',
                     factor: float = 1.0):
    ''' Set active color to all selected vertex

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param factor: Factor, Mix Factor
    :type factor: float
    '''

    pass


def vertex_group_assign(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Assign the selected vertices to the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_group_deselect(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Deselect all selected vertices assigned to the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_group_invert(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Invert weights to the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_group_normalize(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None):
    ''' Normalize weights to the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_group_normalize_all(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        lock_active: bool = True):
    ''' Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param lock_active: Lock Active, Keep the values of the active group while normalizing others
    :type lock_active: bool
    '''

    pass


def vertex_group_remove_from(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None):
    ''' Remove the selected vertices from active or all vertex group(s)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_group_select(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Select all the vertices assigned to the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_group_smooth(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        factor: float = 0.5,
                        repeat: int = 1):
    ''' Smooth weights to the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param factor: Factor
    :type factor: float
    :param repeat: Iterations
    :type repeat: int
    '''

    pass


def vertex_paint(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 stroke: bpy.types.
                 bpy_prop_collection['bpy.types.OperatorStrokeElement'] = None,
                 wait_for_input: bool = True):
    ''' Paint stroke points with a color

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param stroke: Stroke
    :type stroke: bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def vertexmode_toggle(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      back: bool = False):
    ''' Enter/Exit vertex paint mode for Grease Pencil strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param back: Return to Previous Mode, Return to previous mode
    :type back: bool
    '''

    pass


def weight_paint(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 stroke: bpy.types.
                 bpy_prop_collection['bpy.types.OperatorStrokeElement'] = None,
                 wait_for_input: bool = True):
    ''' Paint stroke points with a color

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param stroke: Stroke
    :type stroke: bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def weightmode_toggle(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      back: bool = False):
    ''' Enter/Exit weight paint mode for Grease Pencil strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param back: Return to Previous Mode, Return to previous mode
    :type back: bool
    '''

    pass
