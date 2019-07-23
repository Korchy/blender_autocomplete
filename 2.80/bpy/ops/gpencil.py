import sys
import typing
import bpy


def active_frame_delete():
    '''Delete the active frame for the active Grease Pencil Layer 

    '''

    pass


def active_frames_delete_all():
    '''Delete the active frame(s) of all editable Grease Pencil layers 

    '''

    pass


def annotate(mode: int = 'DRAW',
             stroke: typing.List['bpy.types.OperatorStrokeElement'] = None,
             wait_for_input: bool = True):
    '''Make annotations on the active data 

    :param mode: Mode, Way to interpret mouse movementsDRAW Draw Freehand, Draw freehand stroke(s).DRAW_STRAIGHT Draw Straight Lines, Draw straight line segment(s).DRAW_POLY Draw Poly Line, Click to place endpoints of straight line segments (connected).ERASER Eraser, Erase Annotation strokes. 
    :type mode: int
    :param stroke: Stroke 
    :type stroke: typing.List['bpy.types.OperatorStrokeElement']
    :param wait_for_input: Wait for Input, Wait for first click instead of painting immediately 
    :type wait_for_input: bool
    '''

    pass


def blank_frame_add(all_layers: bool = False):
    '''Insert a blank frame on the current frame (all subsequently existing frames, if any, are shifted right by one frame) 

    :param all_layers: All Layers, Create blank frame in all layers, not only active 
    :type all_layers: bool
    '''

    pass


def brush_presets_create():
    '''Create a set of predefined Grease Pencil drawing brushes 

    '''

    pass


def color_hide(unselected: bool = False):
    '''Hide selected/unselected Grease Pencil colors 

    :param unselected: Unselected, Hide unselected rather than selected colors 
    :type unselected: bool
    '''

    pass


def color_isolate(affect_visibility: bool = False):
    '''Toggle whether the active color is the only one that is editable and/or visible 

    :param affect_visibility: Affect Visibility, In addition to toggling the editability, also affect the visibility 
    :type affect_visibility: bool
    '''

    pass


def color_lock_all():
    '''Lock all Grease Pencil colors to prevent them from being accidentally modified 

    '''

    pass


def color_reveal():
    '''Unhide all hidden Grease Pencil colors 

    '''

    pass


def color_select(deselect: bool = False):
    '''Select all Grease Pencil strokes using current color 

    :param deselect: Deselect, Unselect strokes 
    :type deselect: bool
    '''

    pass


def color_unlock_all():
    '''Unlock all Grease Pencil colors so that they can be edited 

    '''

    pass


def convert(type: int = 'PATH',
            use_normalize_weights: bool = True,
            radius_multiplier: float = 1.0,
            use_link_strokes: bool = False,
            timing_mode: int = 'FULL',
            frame_range: int = 100,
            start_frame: int = 1,
            use_realtime: bool = False,
            end_frame: int = 250,
            gap_duration: float = 0.0,
            gap_randomness: float = 0.0,
            seed: int = 0,
            use_timing_data: bool = False):
    '''Convert the active Grease Pencil layer to a new Curve Object 

    :param type: Type, Which type of curve to convert toPATH Path, Animation path.CURVE Bezier Curve, Smooth Bezier curve.POLY Polygon Curve, Bezier curve with straight-line segments (vector handles). 
    :type type: int
    :param use_normalize_weights: Normalize Weight, Normalize weight (set from stroke width) 
    :type use_normalize_weights: bool
    :param radius_multiplier: Radius Fac, Multiplier for the points’ radii (set from stroke width) 
    :type radius_multiplier: float
    :param use_link_strokes: Link Strokes, Whether to link strokes with zero-radius sections of curves 
    :type use_link_strokes: bool
    :param timing_mode: Timing Mode, How to use timing data stored in strokesNONE No Timing, Ignore timing.LINEAR Linear, Simple linear timing.FULL Original, Use the original timing, gaps included.CUSTOMGAP Custom Gaps, Use the original timing, but with custom gap lengths (in frames). 
    :type timing_mode: int
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


def convert_old_files(annotation: bool = False):
    '''Convert 2.7x grease pencil files to 2.80 

    :param annotation: Annotation, Convert to Annotations 
    :type annotation: bool
    '''

    pass


def copy():
    '''Copy selected Grease Pencil points and strokes 

    '''

    pass


def data_add():
    '''Add new Grease Pencil data-block 

    '''

    pass


def data_unlink():
    '''Unlink active Annotation data-block 

    '''

    pass


def delete(type: int = 'POINTS'):
    '''Delete selected Grease Pencil strokes, vertices, or frames 

    :param type: Type, Method used for deleting Grease Pencil dataPOINTS Points, Delete selected points and split strokes into segments.STROKES Strokes, Delete selected strokes.FRAME Frame, Delete active frame. 
    :type type: int
    '''

    pass


def dissolve(type: int = 'POINTS'):
    '''Delete selected points without splitting strokes 

    :param type: Type, Method used for dissolving Stroke pointsPOINTS Dissolve, Dissolve selected points.BETWEEN Dissolve Between, Dissolve points between selected points.UNSELECT Dissolve Unselect, Dissolve all unselected points. 
    :type type: int
    '''

    pass


def draw(mode: int = 'DRAW',
         stroke: typing.List['bpy.types.OperatorStrokeElement'] = None,
         wait_for_input: bool = True,
         disable_straight: bool = False,
         disable_fill: bool = False,
         guide_last_angle: float = 0.0):
    '''Draw a new stroke in the active Grease Pencil Object 

    :param mode: Mode, Way to interpret mouse movementsDRAW Draw Freehand, Draw freehand stroke(s).DRAW_STRAIGHT Draw Straight Lines, Draw straight line segment(s).DRAW_POLY Draw Poly Line, Click to place endpoints of straight line segments (connected).ERASER Eraser, Erase Grease Pencil strokes. 
    :type mode: int
    :param stroke: Stroke 
    :type stroke: typing.List['bpy.types.OperatorStrokeElement']
    :param wait_for_input: Wait for Input, Wait for first click instead of painting immediately 
    :type wait_for_input: bool
    :param disable_straight: No Straight lines, Disable key for straight lines 
    :type disable_straight: bool
    :param disable_fill: No Fill Areas, Disable fill to use stroke as fill boundary 
    :type disable_fill: bool
    :param guide_last_angle: Angle, Speed guide angle 
    :type guide_last_angle: float
    '''

    pass


def duplicate():
    '''Duplicate the selected Grease Pencil strokes 

    '''

    pass


def duplicate_move(GPENCIL_OT_duplicate=None, TRANSFORM_OT_translate=None):
    '''Make copies of the selected Grease Pencil strokes and move them 

    :param GPENCIL_OT_duplicate: Duplicate Strokes, Duplicate the selected Grease Pencil strokes 
    :param TRANSFORM_OT_translate: Move, Move selected items 
    '''

    pass


def editmode_toggle(back: bool = False):
    '''Enter/Exit edit mode for Grease Pencil strokes 

    :param back: Return to Previous Mode, Return to previous mode 
    :type back: bool
    '''

    pass


def extrude():
    '''Extrude the selected Grease Pencil points 

    '''

    pass


def extrude_move(GPENCIL_OT_extrude=None, TRANSFORM_OT_translate=None):
    '''Extrude selected points and move them 

    :param GPENCIL_OT_extrude: Extrude Stroke Points, Extrude the selected Grease Pencil points 
    :param TRANSFORM_OT_translate: Move, Move selected items 
    '''

    pass


def fill(on_back: bool = False):
    '''Fill with color the shape formed by strokes 

    :param on_back: Draw On Back, Send new stroke to Back 
    :type on_back: bool
    '''

    pass


def frame_clean_fill(mode: int = 'ACTIVE'):
    '''Remove ‘no fill’ boundary strokes 

    :param mode: ModeACTIVE Active Frame Only, Clean active frame only.ALL All Frames, Clean all frames in all layers. 
    :type mode: int
    '''

    pass


def frame_clean_loose(limit: int = 1):
    '''Remove loose points 

    :param limit: Limit, Number of points to consider stroke as loose 
    :type limit: int
    '''

    pass


def frame_duplicate(mode: int = 'ACTIVE'):
    '''Make a copy of the active Grease Pencil Frame 

    :param mode: ModeACTIVE Active, Duplicate frame in active layer only.ALL All, Duplicate active frames in all layers. 
    :type mode: int
    '''

    pass


def generate_weights(mode: int = 'NAME',
                     armature: int = 'DEFAULT',
                     ratio: float = 0.1,
                     decay: float = 0.8):
    '''Generate automatic weights for armatures (requires armature modifier) 

    :param mode: Mode 
    :type mode: int
    :param armature: Armature, Armature to use 
    :type armature: int
    :param ratio: Ratio, Ratio between bone length and influence radius 
    :type ratio: float
    :param decay: Decay, Factor to reduce influence depending of distance to bone axis 
    :type decay: float
    '''

    pass


def guide_rotate(increment: bool = True, angle: float = 0.0):
    '''Rotate guide angle 

    :param increment: Increment, Increment angle 
    :type increment: bool
    :param angle: Angle, Guide angle 
    :type angle: float
    '''

    pass


def hide(unselected: bool = False):
    '''Hide selected/unselected Grease Pencil layers 

    :param unselected: Unselected, Hide unselected rather than selected layers 
    :type unselected: bool
    '''

    pass


def interpolate(shift: float = 0.0):
    '''Interpolate grease pencil strokes between frames 

    :param shift: Shift, Bias factor for which frame has more influence on the interpolated strokes 
    :type shift: float
    '''

    pass


def interpolate_reverse():
    '''Remove breakdown frames generated by interpolating between two Grease Pencil frames 

    '''

    pass


def interpolate_sequence():
    '''Generate ‘in-betweens’ to smoothly interpolate between Grease Pencil frames 

    '''

    pass


def layer_add():
    '''Add new layer or note for the active data-block 

    '''

    pass


def layer_change(layer: int = 'DEFAULT'):
    '''Change active Grease Pencil layer 

    :param layer: Grease Pencil Layer 
    :type layer: int
    '''

    pass


def layer_duplicate():
    '''Make a copy of the active Grease Pencil layer 

    '''

    pass


def layer_duplicate_object(object: str = "", mode: int = 'ALL'):
    '''Make a copy of the active Grease Pencil layer to new object 

    :param object: Object, Name of the destination object 
    :type object: str
    :param mode: Mode 
    :type mode: int
    '''

    pass


def layer_isolate(affect_visibility: bool = False):
    '''Toggle whether the active layer is the only one that can be edited and/or visible 

    :param affect_visibility: Affect Visibility, In addition to toggling the editability, also affect the visibility 
    :type affect_visibility: bool
    '''

    pass


def layer_merge():
    '''Merge the current layer with the layer below 

    '''

    pass


def layer_move(type: int = 'UP'):
    '''Move the active Grease Pencil layer up/down in the list 

    :param type: Type 
    :type type: int
    '''

    pass


def layer_remove():
    '''Remove active Grease Pencil layer 

    '''

    pass


def lock_all():
    '''Lock all Grease Pencil layers to prevent them from being accidentally modified 

    '''

    pass


def lock_layer():
    '''Lock and hide any color not used in any layer 

    '''

    pass


def move_to_layer(layer: int = 'DEFAULT'):
    '''Move selected strokes to another layer 

    :param layer: Grease Pencil Layer 
    :type layer: int
    '''

    pass


def paintmode_toggle(back: bool = False):
    '''Enter/Exit paint mode for Grease Pencil strokes 

    :param back: Return to Previous Mode, Return to previous mode 
    :type back: bool
    '''

    pass


def paste(type: int = 'COPY'):
    '''Paste previously copied strokes or copy and merge in active layer 

    :param type: Type 
    :type type: int
    '''

    pass


def primitive(edges: int = 4, type: int = 'BOX', wait_for_input: bool = True):
    '''Create predefined grease pencil stroke shapes 

    :param edges: Edges, Number of polygon edges 
    :type edges: int
    :param type: Type, Type of shape 
    :type type: int
    :param wait_for_input: Wait for Input 
    :type wait_for_input: bool
    '''

    pass


def reproject(type: int = 'VIEW'):
    '''Reproject the selected strokes from the current viewpoint as if they had been newly drawn (e.g. to fix problems from accidental 3D cursor movement or accidental viewport changes, or for matching deforming geometry) 

    :param type: Projection TypeFRONT Front, Reproject the strokes using the X-Z plane.SIDE Side, Reproject the strokes using the Y-Z plane.TOP Top, Reproject the strokes using the X-Y plane.VIEW View, Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using ‘Cursor’ Stroke Placement.SURFACE Surface, Reproject the strokes on to the scene geometry, as if drawn using ‘Surface’ placement.CURSOR Cursor, Reproject the strokes using the orienation of 3D cursor. 
    :type type: int
    '''

    pass


def reveal(select: bool = True):
    '''Show all Grease Pencil layers 

    :param select: Select 
    :type select: bool
    '''

    pass


def sculpt_paint(stroke: typing.List['bpy.types.OperatorStrokeElement'] = None,
                 wait_for_input: bool = True):
    '''Apply tweaks to strokes by painting over the strokes 

    :param stroke: Stroke 
    :type stroke: typing.List['bpy.types.OperatorStrokeElement']
    :param wait_for_input: Wait for Input, Enter a mini ‘sculpt-mode’ if enabled, otherwise, exit after drawing a single stroke 
    :type wait_for_input: bool
    '''

    pass


def sculptmode_toggle(back: bool = False):
    '''Enter/Exit sculpt mode for Grease Pencil strokes 

    :param back: Return to Previous Mode, Return to previous mode 
    :type back: bool
    '''

    pass


def select(extend: bool = False,
           deselect: bool = False,
           toggle: bool = False,
           deselect_all: bool = False,
           entire_strokes: bool = False,
           location: int = (0, 0)):
    '''Select Grease Pencil strokes and/or stroke points 

    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: bool
    :param deselect: Deselect, Remove from selection 
    :type deselect: bool
    :param toggle: Toggle Selection, Toggle the selection 
    :type toggle: bool
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor 
    :type deselect_all: bool
    :param entire_strokes: Entire Strokes, Select entire strokes instead of just the nearest stroke vertex 
    :type entire_strokes: bool
    :param location: Location, Mouse location 
    :type location: int
    '''

    pass


def select_all(action: int = 'TOGGLE'):
    '''Change selection of all Grease Pencil strokes currently visible 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: int
    '''

    pass


def select_alternate(unselect_ends: bool = True):
    '''Select alternative points in same strokes as already selected points 

    :param unselect_ends: Unselect Ends, Do not select the first and last point of the stroke 
    :type unselect_ends: bool
    '''

    pass


def select_box(xmin: int = 0,
               xmax: int = 0,
               ymin: int = 0,
               ymax: int = 0,
               wait_for_input: bool = True,
               mode: int = 'SET'):
    '''Select Grease Pencil strokes within a rectangular region 

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
    :param mode: ModeSET Set, Set a new selection.ADD Extend, Extend existing selection.SUB Subtract, Subtract existing selection.XOR Difference, Inverts existing selection.AND Intersect, Intersect existing selection. 
    :type mode: int
    '''

    pass


def select_circle(x: int = 0,
                  y: int = 0,
                  radius: int = 25,
                  wait_for_input: bool = True,
                  mode: int = 'SET'):
    '''Select Grease Pencil strokes using brush selection 

    :param x: X 
    :type x: int
    :param y: Y 
    :type y: int
    :param radius: Radius 
    :type radius: int
    :param wait_for_input: Wait for Input 
    :type wait_for_input: bool
    :param mode: ModeSET Set, Set a new selection.ADD Extend, Extend existing selection.SUB Subtract, Subtract existing selection. 
    :type mode: int
    '''

    pass


def select_first(only_selected_strokes: bool = False, extend: bool = False):
    '''Select first point in Grease Pencil strokes 

    :param only_selected_strokes: Selected Strokes Only, Only select the first point of strokes that already have points selected 
    :type only_selected_strokes: bool
    :param extend: Extend, Extend selection instead of deselecting all other selected points 
    :type extend: bool
    '''

    pass


def select_grouped(type: int = 'LAYER'):
    '''Select all strokes with similar characteristics 

    :param type: TypeLAYER Layer, Shared layers.MATERIAL Material, Shared materials. 
    :type type: int
    '''

    pass


def select_lasso(mode: int = 'SET',
                 path: typing.List['bpy.types.OperatorMousePath'] = None):
    '''Select Grease Pencil strokes using lasso selection 

    :param mode: ModeSET Set, Set a new selection.ADD Extend, Extend existing selection.SUB Subtract, Subtract existing selection.XOR Difference, Inverts existing selection.AND Intersect, Intersect existing selection. 
    :type mode: int
    :param path: Path 
    :type path: typing.List['bpy.types.OperatorMousePath']
    '''

    pass


def select_last(only_selected_strokes: bool = False, extend: bool = False):
    '''Select last point in Grease Pencil strokes 

    :param only_selected_strokes: Selected Strokes Only, Only select the last point of strokes that already have points selected 
    :type only_selected_strokes: bool
    :param extend: Extend, Extend selection instead of deselecting all other selected points 
    :type extend: bool
    '''

    pass


def select_less():
    '''Shrink sets of selected Grease Pencil points 

    '''

    pass


def select_linked():
    '''Select all points in same strokes as already selected points 

    '''

    pass


def select_more():
    '''Grow sets of selected Grease Pencil points 

    '''

    pass


def selection_opacity_toggle():
    '''Hide/Unhide selected points for Grease Pencil strokes setting alpha factor 

    '''

    pass


def selectmode_toggle(mode: int = 0):
    '''Set selection mode for Grease Pencil strokes 

    :param mode: Select mode, Select mode 
    :type mode: int
    '''

    pass


def snap_cursor_to_selected():
    '''Snap cursor to center of selected points 

    '''

    pass


def snap_to_cursor(use_offset: bool = True):
    '''Snap selected points/strokes to the cursor 

    :param use_offset: With Offset, Offset the entire stroke instead of selected points only 
    :type use_offset: bool
    '''

    pass


def snap_to_grid():
    '''Snap selected points to the nearest grid points 

    '''

    pass


def stroke_apply_thickness():
    '''Apply the thickness change of the layer to its strokes 

    '''

    pass


def stroke_arrange(direction: int = 'UP'):
    '''Arrange selected strokes up/down in the drawing order of the active layer 

    :param direction: Direction 
    :type direction: int
    '''

    pass


def stroke_caps_set(type: int = 'TOGGLE'):
    '''Change Stroke caps mode (rounded or flat) 

    :param type: TypeTOGGLE Both.START Start.END End.TOGGLE Default, Set as default rounded. 
    :type type: int
    '''

    pass


def stroke_change_color(material: str = ""):
    '''Move selected strokes to active material 

    :param material: Material, Name of the material 
    :type material: str
    '''

    pass


def stroke_cutter(path: typing.List['bpy.types.OperatorMousePath'] = None):
    '''Select section and cut 

    :param path: Path 
    :type path: typing.List['bpy.types.OperatorMousePath']
    '''

    pass


def stroke_cyclical_set(type: int = 'TOGGLE', geometry: bool = False):
    '''Close or open the selected stroke adding an edge from last to first point 

    :param type: Type 
    :type type: int
    :param geometry: Create Geometry, Create new geometry for closing stroke 
    :type geometry: bool
    '''

    pass


def stroke_flip():
    '''Change direction of the points of the selected strokes 

    '''

    pass


def stroke_join(type: int = 'JOIN', leave_gaps: bool = False):
    '''Join selected strokes (optionally as new stroke) 

    :param type: Type 
    :type type: int
    :param leave_gaps: Leave Gaps, Leave gaps between joined strokes instead of linking them 
    :type leave_gaps: bool
    '''

    pass


def stroke_lock_color():
    '''Lock any color not used in any selected stroke 

    '''

    pass


def stroke_merge(mode: int = 'STROKE',
                 back: bool = False,
                 additive: bool = False,
                 cyclic: bool = False,
                 clear_point: bool = False,
                 clear_stroke: bool = False):
    '''Create a new stroke with the selected stroke points 

    :param mode: Mode 
    :type mode: int
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


def stroke_separate(mode: int = 'POINT'):
    '''Separate the selected strokes or layer in a new grease pencil object 

    :param mode: ModePOINT Selected Points, Separate the selected points.STROKE Selected Strokes, Separate the selected strokes.LAYER Active Layer, Separate the strokes of the current layer. 
    :type mode: int
    '''

    pass


def stroke_simplify(factor: float = 0.0):
    '''Simplify selected stroked reducing number of points 

    :param factor: Factor 
    :type factor: float
    '''

    pass


def stroke_simplify_fixed(step: int = 1):
    '''Simplify selected stroked reducing number of points using fixed algorithm 

    :param step: Steps, Number of simplify steps 
    :type step: int
    '''

    pass


def stroke_smooth(repeat: int = 1,
                  factor: float = 0.5,
                  only_selected: bool = True,
                  smooth_position: bool = True,
                  smooth_thickness: bool = True,
                  smooth_strength: bool = False,
                  smooth_uv: bool = False):
    '''Smooth selected strokes 

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


def stroke_split():
    '''Split selected points as new stroke on same frame 

    '''

    pass


def stroke_subdivide(number_cuts: int = 1,
                     factor: float = 0.0,
                     repeat: int = 1,
                     only_selected: bool = True,
                     smooth_position: bool = True,
                     smooth_thickness: bool = True,
                     smooth_strength: bool = False,
                     smooth_uv: bool = False):
    '''Subdivide between continuous selected points of the stroke adding a point half way between them 

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


def stroke_trim():
    '''Trim selected stroke to first loop or intersection 

    '''

    pass


def unlock_all():
    '''Unlock all Grease Pencil layers so that they can be edited 

    '''

    pass


def vertex_group_assign():
    '''Assign the selected vertices to the active vertex group 

    '''

    pass


def vertex_group_deselect():
    '''Deselect all selected vertices assigned to the active vertex group 

    '''

    pass


def vertex_group_invert():
    '''Invert weights to the active vertex group 

    '''

    pass


def vertex_group_normalize():
    '''Normalize weights to the active vertex group 

    '''

    pass


def vertex_group_normalize_all(lock_active: bool = True):
    '''Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0 

    :param lock_active: Lock Active, Keep the values of the active group while normalizing others 
    :type lock_active: bool
    '''

    pass


def vertex_group_remove_from():
    '''Remove the selected vertices from active or all vertex group(s) 

    '''

    pass


def vertex_group_select():
    '''Select all the vertices assigned to the active vertex group 

    '''

    pass


def vertex_group_smooth(factor: float = 0.5, repeat: int = 1):
    '''Smooth weights to the active vertex group 

    :param factor: Factor 
    :type factor: float
    :param repeat: Iterations 
    :type repeat: int
    '''

    pass


def weightmode_toggle(back: bool = False):
    '''Enter/Exit weight paint mode for Grease Pencil strokes 

    :param back: Return to Previous Mode, Return to previous mode 
    :type back: bool
    '''

    pass
